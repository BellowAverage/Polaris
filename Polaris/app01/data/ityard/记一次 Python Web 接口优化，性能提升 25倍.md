
--- 
title:  记一次 Python Web 接口优化，性能提升 25倍 
tags: []
categories: [] 

---
>  
  作者：Lin_R    
  https://segmentfault.com/a/1190000020956724 
 

**背景**

我们负责的一个业务平台，有次在发现设置页面的加载特别特别地慢，简直就是令人发指

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktsbk5qSHlkQXlGSWliNHc3TlBvaWJvYUNpYjFkZlFvd21mQjZTYTgzY2c2SUV4ckZycXllV25pYWN3LzY0MA?x-oss-process=image/format,png">

让用户等待 36s 肯定是不可能的，于是我们就要开启优化之旅了。

**投石问路**

既然是网站的响应问题，可以通过 Chrome 这个强大的工具帮助我们快速找到优化方向。

通过 Chrome 的 Network 除了可以看到接口请求耗时之外，还能看到一个时间的分配情况，选择一个配置没有那么多的项目，简单请求看看：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktUeWlhaWF6QWt5bWljZDNKaFFlZ1NJNnluYWljbEpSbGdNNTZFZHg3S2ljWTBVdGljc0pnQ0I0ZjYyZGcvNjQw?x-oss-process=image/format,png">

虽然只是一个只有三条记录的项目，加载项目设置都需要 17s，通过 Timing, 可以看到总的请求共耗时 **17.67s** ，但有 **17.57s** 是在 Waiting(TTFB) 状态。

```
TTFB 是 Time to First Byte 的缩写，指的是浏览器开始收到服务器响应数据的时间（后台处理时间+重定向时间），是反映服务端响应速度的重要指标。

```

```
Profile 火焰图 + 代码调优

```

那么大概可以知道优化的大方向是在后端接口处理上面，后端代码是 Python + Flask 实现的，先不盲猜，直接上 Profile：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscks1bUJ0Uk5XYnVha0kwdjd2cFVPbGdIYXltT3VxWGliaWNPaFFRSjd3YWN4YlMzd2I1bmliMUJjaWN3LzY0MA?x-oss-process=image/format,png">

**第一波优化：功能交互重新设计**

说实话看到这段代码是绝望的：完全看不出什么？只是看到很多 gevent 和 Threading，因为太多协程或者线程？

这时候一定要结合代码来分析（**为了简短篇幅，参数部分用 “...” 代替**）：

```
def get_max_cpus(project_code, gids):
    """
    """
    ...
    # 再定义一个获取 cpu 的函数
    def get_max_cpu(project_setting, gid, token, headers):
        group_with_machines = utils.get_groups(...)
        hostnames = get_info_from_machines_info(...)
        res = fetchers.MonitorAPIFetcher.get(...)
        vals = [
            round(100 - val, 4)
            for ts, val in res['series'][0]['data']
            if not utils.is_nan(val)
        ]
        max_val = max(vals) if vals else float('nan')
        max_cpus[gid] = max_val
       
    #  启动线程批量请求
    for gid in gids:
        t = Thread(target=get_max_cpu, args=(...))
        threads.append(t)
        t.start()
        
    # 回收线程
    for t in threads:
        t.join()


    return max_cpus

```

通过代码可以看到，为了更加快速获取 **gids** 所有的 **cpu_max** 数据，为每个 gid 分配一个线程去请求，最终再返回最大值。

这里会出现两个问题：
1. 在一个 web api 做线程的 **创建 和 销毁** 是有很大成本的，因为接口会频繁被触发，线程的操作也会频繁发生，应该尽可能使用线程池之类的，降低系统花销；1. 该请求是加载某个 gid (群组) 下面的机器过去 7 天的 CPU 最大值，可以简单拍脑袋想下，这个值不是实时值也不是一个均值，而是一个最大值，很多时候可能并没有想象中那么大价值；
既然知道问题，那就有针对性的方案：
1. 调整功能设计，不再默认加载 CPU 最大值，换成用户点击加载（一来降低并发的可能，二来不会影响整体）；1. 因为 1 的调整，去掉多线程实现；
再看第一波优化后的火焰图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktTS3hSd1BMSWZZYlJEMnhLN3hMUDBVb1FldUYxa21ZZGlhZEFDRjRtRlpqOWliVmVNS3d3Sk5VUS82NDA?x-oss-process=image/format,png">

这次看的火焰图虽然还有很大的优化空间，但起码看起来有点正常的样子了。

**第二波优化：Mysql 操作优化处理**

我们再从页面标记处（接口逻辑处）放大火焰图观察：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktLUUhuSHpaY2tCMURGcUtrbkFMMjVFOXhiNWtIOGJpYXZwdlhIRWRYaDRjVlhqVzlYMkZxa1FnLzY0MA?x-oss-process=image/format,png">

看到好大一片操作都是由 `utils.py:get_group_profile_settings` 这个函数引起的数据库操作热点。

同理，也是需要通过代码分析：

```
def get_group_profile_settings(project_code, gids):
    
    # 获取 Mysql ORM 操作对象
    ProfileSetting = unpurview(sandman.endpoint_class('profile_settings'))
    session = get_postman_session()
    
    profile_settings = {}
    for gid in gids:
        compound_name = project_code + ':' + gid
        result = session.query(ProfileSetting).filter(
            ProfileSetting.name == compound_name
        ).first()
        
        if result:
            result = result.as_dict()
            tag_indexes = result.get('tag_indexes')
            profile_settings[gid] = {
                'tag_indexes': tag_indexes,
                'interval': result['interval'],
                'status': result['status'],
                'profile_machines': result['profile_machines'],
                'thread_settings': result['thread_settings']
            }
            ...(省略)
    return profile_settings

```

看到 Mysql ，第一个反应就是 **索引问题**，所以优先去看看数据库的索引情况，如果有索引的话应该不会是瓶颈：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscks2Z0JrYjdiZ0JJVXl4aWNEdVVhODBMa1k5UFVDM2RKbVBpYzhUQmZ0U2pVNmtvUWx5VUNZbHBuZy82NDA?x-oss-process=image/format,png">

很奇怪这里明明已经有了索引了，为什么速度还是这个鬼样子呢！

正当毫无头绪的时候，突然想起在 **第一波优化** 的时候， 发现 gid（群组）越多的影响越明显，然后看回上面的代码，看到那句：

```
for gid in gids: 
    ...

```

我仿佛明白了什么。

这里是每个 gid 都去查询一次数据库，而项目经常有 20 ~ 50+ 个群组，那肯定直接爆炸了。

其实 Mysql 是支持单字段多值的查询，而且每条记录并没有太多的数据，我可以尝试下用 Mysql 的 OR 语法，除了避免多次网络请求，还能避开那该死的 **for**

正当我想事不宜迟直接搞起的时候，余光瞥见在刚才的代码还有一个地方可以优化，那就是：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktycnhkdFVmUGczVG5PSmNlWFFGRFJoMWFpYm9xMFBKSG43MXZjd2hJUGliZ0d6OFlTT3hxM0ZTdy82NDA?x-oss-process=image/format,png">

看到这里，熟悉的朋友大概会明白是怎么回事。

**GetAttr** 这个方法是Python 获取对象的 **方法/属性** 时候会用到，虽然不可不用，但是如果在使用太过频繁也会有一定的性能损耗。

结合代码一起来看：

```
def get_group_profile_settings(project_code, gids):
    
    # 获取 Mysql ORM 操作对象
    ProfileSetting = unpurview(sandman.endpoint_class('profile_settings'))
    session = get_postman_session()
    
    profile_settings = {}
    for gid in gids:
        compound_name = project_code + ':' + gid
        result = session.query(ProfileSetting).filter(
            ProfileSetting.name == compound_name
        ).first()
        ...

```

在这个遍历很多次的 **for** 里面，**session.query(ProfileSetting)** 被反复无效执行了，然后 **filter** 这个属性方法也被频繁读取和执行，所以这里也可以被优化。

总结下的问题就是：

```
1. 数据库的查询没有批量查询；
2. ORM 的对象太多重复的生成，导致性能损耗；
3. 属性读取后没有复用，导致在遍历次数较大的循环体内频繁 getAttr，成本被放大；

```

那么对症下药就是：

```
def get_group_profile_settings(project_code, gids):
    
    # 获取 Mysql ORM 操作对象
    ProfileSetting = unpurview(sandman.endpoint_class('profile_settings'))
    session = get_postman_session()
    
    
    # 批量查询 并将 filter 提到循环之外
    query_results = query_instance.filter(
        ProfileSetting.name.in_(project_code + ':' + gid for gid in gids)
    ).all()


    # 对全部的查询结果再单条处理
    profile_settings = {}
    for result in query_results:
        if not result:
            continue
        result = result.as_dict()
        gid = result['name'].split(':')[1]
        tag_indexes = result.get('tag_indexes')
        profile_settings[gid] = {
            'tag_indexes': tag_indexes,
            'interval': result['interval'],
            'status': result['status'],
            'profile_machines': result['profile_machines'],
            'thread_settings': result['thread_settings']
        }


            ...(省略)
    return profile_settings

```

```
优化后的火焰图：

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktMNEJwREhFdXV0S20yTURQZjF5OUc3Z2ZvaDNXNnFQYlJHbjJDRTBqNldDcDBydmFCcmZTZ2cvNjQw?x-oss-process=image/format,png">

对比下优化前的相同位置的火焰图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFscktwcGljQ3ByWndGa3lxZ2pEaWNpYXlMcmliM1VSbzdFSzJpYzVEMUF2QjhGZTI2YW11N1I5SWsyMW82Zy82NDA?x-oss-process=image/format,png">

明显的优化点：优化前的，最底部的 **utils.py:get_group_profile_settings** 和 数据库相关的热点大大缩减。

**优化效果**

同一个项目的接口的响应时长从 37.6 s 优化成 1.47s，具体的截图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2VFUmljTEYxRVRCZE01MVV0QWFsckttbGtKMXczSk5nNzhFcW54bUdKM2ljQnJDaWM3VXc4V3FLakxkYUtXQWxJc2NrNnBwOXRCbVFIQS82NDA?x-oss-process=image/format,png">

如同一句名言：

```
如果一个数据结构足够优秀，那么它是不需要多好的算法。

```

在优化功能的时候，最快的优化就是：**去掉那个功能！**

其次快就是调整那个功能触发的 **频率** 或者 **复杂度**！

从上到下，从用户使用场景去考虑这个功能优化方式，往往会带来更加简单高效的结果，嘿嘿！

当然很多时候我们是无法那么幸运的，如果我们实在无法去掉或者调整，那么就发挥做程序猿的价值咯：**Profile**

针对 Python 可以尝试：cProflile + gprof2dot

而针对 Go 可以使用: pprof + go-torch

很多时候看到的代码问题都不一定是真正的性能瓶颈，需要结合工具来客观分析，这样才能有效直击痛点！

其实这个 1.47s，其实还不是最好的结果，还可以有更多优化的空间，比如：
1. 前端渲染和呈现的方式，因为整个表格是有很多数据组装后再呈现的，响应慢的单元格可以默认先显示 **菊花**，数据返回再更新；1. 火焰图看到还有挺多细节可以优化，可以替换请求数据的外部接口，比如再优化彻底 **GetAttr** 相关的逻辑；1. 更极端就是直接 Python 转 GO；
但是这些优化已经不是那么迫切了，因为这个 1.47s 是比较大型项目的优化结果了，绝大部分的项目其实不到 1s 就能返回

再优化可能付出更大成本，而结果可能也只是从 **500ms** 到 **400ms** 而已，结果并不那么高性价比。

所以我们一定要时刻清晰自己优化的目标，时刻考虑 **投入产出比**，在有限的时间做出比较高的价值（如果有空闲时间当然可以尽情干到底）

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
