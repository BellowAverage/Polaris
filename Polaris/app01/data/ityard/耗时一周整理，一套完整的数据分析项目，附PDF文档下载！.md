
--- 
title:  耗时一周整理，一套完整的数据分析项目，附PDF文档下载！ 
tags: []
categories: [] 

---
### 项目背景

总有一些从事数据分析的朋友会问：**能不能分享一些真实的数据分析实战案例呢？**

今天为大家分享曾经做过的一个真实的企业级项目，经过一个月的整理，完整大纲和部分项目截图如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/d6f56e8269d365132d167ef7db3d38c4.png">

大家跟着我做完整个项目，一定会有很大收获。

哈哈，这次有所不同，我还专门为大家录制了视频讲解，学习起来毫无压力。

<img src="https://img-blog.csdnimg.cn/img_convert/da51f428cda10b40caa07f5538e82eb8.png">

**完整文档**、**项目使用到的数据集**、**所有代码**，**均已打包**，大家文末自由获取即可。

<img src="https://img-blog.csdnimg.cn/img_convert/25f6f53ccda482eef9baaeb776f41373.gif">

### 项目思路

该项目的目的是为了设计出一套完整的智能营销数据分析系统，通过**业务驱动**或**数据导向**，针对性的指定营销策略。

**整个项目的设计思路如下：**

<img src="https://img-blog.csdnimg.cn/img_convert/f4f78e3668a6ac1a0eefbf27d86f9727.png">

综合上面得到的用户最终进行推送订阅，达到智能营销的目的。

### 项目解决方案部分展示

##### 1、不同表之间的关联图

该项目涉及太多的表，我们**第一步**就是要**弄清楚不同表之间的联系。**

<img src="https://img-blog.csdnimg.cn/img_convert/ce13408753a48f7f0b6db386b082306c.png">

##### 2、相关数据集介绍

数据来源于企业真实脱敏的数据，对业务的发展起到了正相关的作用，使得这套系统的设计非常贴合真实环境，为智能营销起到指导性作用。

<img src="https://img-blog.csdnimg.cn/img_convert/1c3bfd8f33f5ee0421dffb3b2380f6b4.png">

##### 3、项目完整的可执行SQL

**你是否写过超过100行的SQL代码呢？**或者说，写出过这么多有关联的SQL呢？赶紧学习起来吧！

<img src="https://img-blog.csdnimg.cn/img_convert/46b9ffc7daff861cc173deeb2de51463.png">

```
比如用车消费能力，这里脚本太长只展示一部分：
use ccdb;
-- 创建临时表
DROP TEMPORARY TABLE IF EXISTS d_type_user_tmp;

CREATE TEMPORARY TABLE user_layer_tmp
select * from
(
select 'A类用户' as user_type, '大于等于3单用户' as details,  one_user_cnt as user_cnt from c_type_user_tmp
union all
select 'B类用户' as user_type, '等于2单用户' as details,  two_user_cnt as user_cnt from b_type_user_tmp
union all
select 'C类用户' as user_type , '等于1单用户' as details,  thr_user_cnt as user_cnt from a_type_user_tmp
union all
select 'D类用户' as user_type, '历史有完单，最近90天无完单用户' as details, 90_user_cnt as user_cnt  from d_type_user_tmp
)t ;

```

##### 4、分析结果的可视化

包含柱形图、条形图、饼图、组合图、漏斗图等等的应用，**你是否结合过SQL一起应用过呢？**

<img src="https://img-blog.csdnimg.cn/img_convert/cfec02e0198c85ce3b2213774cb8edf8.png">

### 文档领取

怕有的朋友下载起来贼慢，**还为****大家准备了一个百度云内容下载器**，那速度，杠杠的！

<img src="https://img-blog.csdnimg.cn/img_convert/a1e35b9cd14c962f661c1e3bf50c5064.png">

相信通过本资料的学习，你一定会受益匪浅。

**<strong>↓↓↓文档获取**↓↓↓</strong>

**长按扫描二维码，即可获取**

**????????????**

**<img src="https://img-blog.csdnimg.cn/img_convert/f45808f80139a63ad813978ad107c4a3.png">**
