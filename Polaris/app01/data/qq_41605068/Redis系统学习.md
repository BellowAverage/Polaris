
--- 
title:  Redis系统学习 
tags: []
categories: [] 

---
## 0、常见问题

>  
 报错：WRONGPASS invalid username-password pair or user is disabled. 
 问题复现： 
 1.配置文件用的properties 
 2.spring-data-redis版本用的&lt;version&gt;2.6.6&lt;/version&gt; 
 3.配置信息： 
 <img alt="" height="338" src="https://img-blog.csdnimg.cn/d7e23b1919b9402f9fc3c81c1f6da80b.png" width="1184"> 
 ** 解决方法**： 
 <img alt="" height="305" src="https://img-blog.csdnimg.cn/633d6f6db9954c6797ea1451ca60ade0.png" width="1070"> 
  


## 一、引入依赖

```
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-data-redis&lt;/artifactId&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-cache&lt;/artifactId&gt;
        &lt;/dependency&gt;
```

## 二、配置

```
spring:
  redis:
    ## Redis数据库索引（默认为0）0-15
    database: 0
    ## Redis服务器地址
    host: 127.0.0.1
    ## Redis服务器连接端口
    port: 6379
    ## Redis服务器用户名
    username: root
    ## Redis服务器连接密码（默认为空）
    password: 123456
    jedis:
      pool:
        ## 连接池最大连接数（使用负值表示没有限制)
        max-active: 8
        ## 连接池最大阻塞等待时间（使用负值表示没有限制）
        max-wait: -1
        ## 连接池中的最大空闲连接
        max-idle: 8
        ## 连接池中的最小空闲连接
        min-idle: 0
    ## 连接超时时间（毫秒）
    timeout: 60000
```

>  
  到我们SpringBoot2.x版本，其内置的Redis中间件再也不是Jedis了，而是换成了`lettuce`。我们点进redis依赖就可以发现： 
 <img alt="" src="https://img-blog.csdnimg.cn/32f900a3d1d547c18a2ff8acefd9766c.png"> 
 区别： 
 - lettuce： Lettuce 是 一种可伸缩，线程安全，完全非阻塞的Redis客户端，多个线程可以共享一个RedisConnection,它利用Netty NIO 框架来高效地管理多个连接，从而提供了异步和同步数据访问方式，用于构建非阻塞的反应性应用程序。- Jedis： Jedis 在实现上是直连 redis server，多线程环境下非线程安全，除非使用连接池，为每个 redis实例增加 物理连接。 这种方式更加类似于我们 BIO 一条线程连一个客户端，并且是阻塞式的，会一直连接着客户端等待客户端的命令 
 <img alt="" height="738" src="https://img-blog.csdnimg.cn/91e12dbfbbca4f739d8fa07f2f578566.png" width="1199"> 
  
  增加依赖： 
 <pre><code class="language-html">        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-data-redis&lt;/artifactId&gt;
            &lt;version&gt;2.7.0&lt;/version&gt;
            &lt;exclusions&gt;
                &lt;exclusion&gt;
                    &lt;groupId&gt;io.lettuce&lt;/groupId&gt;
                    &lt;artifactId&gt;lettuce-core&lt;/artifactId&gt;
                &lt;/exclusion&gt;
            &lt;/exclusions&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;redis.clients&lt;/groupId&gt;
            &lt;artifactId&gt;jedis&lt;/artifactId&gt;
        &lt;/dependency&gt;</code></pre> 
  修改后： 
 <img alt="" height="525" src="https://img-blog.csdnimg.cn/703b3c870eeb4dda81587b3ddc7d7d45.png" width="1115"> 
  


## 三、Redis常见问题

### 3.1缓存穿透

        缓存穿透指查询一个一定不存在的数据，由于缓存不命中就会从数据库查询，查不到数据则不写入缓存，这将导致这个不存在的数据都要到数据库查询，造成缓存穿透。这种情况其实就是因为数据库不存在的数据无法写入缓存，解决这个问题的方法，就是把这种数据库查不到值的情况也考虑进去。

#### 解决方案：
- 缓存空值，将数据库查询不到的则作为空值存入，那么下次可以从缓存中获取key值是空值可以判断出数据库不存在这个值。- 使用布隆过滤器，布隆过滤器能判断一个 key 一定不存在（不保证一定存在，因为布隆过滤器结构原因，不能删除，但是旧值可能被新值替换，而将旧值删除后它可能依旧判断其可能存在），在缓存的基础上，构建布隆过滤器数据结构，在布隆过滤器中存储对应的 key，如果存在，则说明 key 对应的值为空。
### 3.2缓存击穿

 缓存击穿针对某些高频访问的key，当这个key失效的瞬间，大量的请求击穿了缓存，直接请求数据库。

#### 解决方案：
- 设置二级缓存- 设置高频key缓存永不过期- 使用互斥锁，在执行过程中，如果缓存过期，那么先获取分布式锁，在执行从数据库中加载数据，如果找到数据就加入缓存，没有就继续该有的动作，在这个过程中能保证只有一个线程操作数据库，避免了对数据库的大量请求。
### 3.3缓存雪崩

缓存雪崩指缓存服务器重启、或者大量缓存集中在某一个时间段失效，这样失效的时候，会给后端系统带来很大压力，造成数据库的故障。

#### 解决方法：
- 缓存高可用设计，Redis sentinel和Redis Cluster等- 请求限流与服务熔断降级机制，限制服务请求次数，当服务不可用时快速熔断降级。- 设置缓存过期时间一定的随机分布，避免集中在同一时间缓存失效，可以在设计时将时间定为一个固定值+随机值。- 定时更新缓存策略，对于实时性要求不高的数据，定时进行更新。
## 四、分布式锁

我们知道目前常见的分布式锁有基于zookeeper和基于redis的，基于zookeeper是一个持久节点下的临时顺序节点的抢占，是一个队列机制。而基于redis则是对某个redis缓存key的抢占。两者优缺点如下：
||优点|缺点
|zookeeper| 1.有封装好的框架，容易实现 2.有等待锁的队列，大大提升抢锁效率。 |添加和删除节点性能较低

2.有等待锁的队列，大大提升抢锁效率。
|redis|Set和Del指令性能较高| 1.实现复杂，需要考虑超时，原子性，误删等情形。  2.没有等待锁的队列，只能在客户端自旋来等待，效率低下。 



可以看出，redis实现分布式锁需要设置超时时间，如果不设置超时时间会出现什么问题呢？如果获取锁之后在解锁过程中出现宕机，则会导致死锁现象。因此需要设置超时时间来避免死锁现象。在redis2.8版本之前获取锁及设置超时时间分为setnx和expire两个步骤完成，如果这两个步骤之间出现宕机现象，依然会存在死锁现象。因此，redis2.8版本做了修改，将setnx和expire两个作为一个方法实现，避免了宕机引起的死锁现象。

## 五、Redis的数据类型

**五种数据类型类比Java：**
- string -- String- hash -- HashMap- list -- LinkList- set -- HashSet- Zset -- TreeSet
**数据存储格式：**
- Redis自身是一个Map类型的存储方式，所有的数据都是采用key:value的形式存储- 以上所讨论的数据类型都是存储的数据类型，也就是value部门的类型，key部门永远都是字符串
### 5.0序列化规则比较

可查看**org.springframework.data.redis.serializer**默认序列化规则为 

<img alt="" height="553" src="https://img-blog.csdnimg.cn/20210113143601511.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

1.JdkSerializationRedisSerializer

用JdkSerializationRedisSerializer序列化的话，被序列化的对象必须实现Serializable接口。在存储内容时，除了属性的内容外还存了其它内容在里面，总长度长，且不容易阅读。

2.GenericJackson2JsonRedisSerializer

3.Jackson2JsonRedisSerializer

用JacksonJsonRedisSerializer序列化的话，被序列化的对象不用实现Serializable接口。Jackson是利用反射和getter和setter方法进行读取的，如果不想因为getter和setter方法来影响存储，就要使用注解来定义被序列化的对象。Jackson序列化的结果清晰，容易阅读，而且存储字节少，速度快，推荐。

**Jackson2JsonRedisSerializer序列化和反序列化效率高，JdkSerializationRedisSerializer序列化后的结果最短**

```
@Configuration
public class BeanConfig {

    @Bean
    public RedisTemplate&lt;String,Object&gt; getRedisString(LettuceConnectionFactory factory){
        RedisTemplate&lt;String, Object&gt; redisTemplate = new RedisTemplate&lt;&gt;();
        redisTemplate.setConnectionFactory(factory);
        Jackson2JsonRedisSerializer&lt;Object&gt; redisSerializer = new Jackson2JsonRedisSerializer&lt;&gt;(Object.class);
        redisTemplate.setDefaultSerializer(redisSerializer);
        return redisTemplate;
    }
}
```

 参考表：

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20201229180349554.png">

 5.1string

#### **常用命令：**

>  
 set key value                                  #添加/修改 
 mset key1 value1 key2 value2...   #添加/修改多个数据 
 get key                                          #h获取数据 
 mget  key1  key2  ..                      #获取多个数据 
 del key                                         #删除数据 
 strlen  key                                   #获取数据字符个数 
 <s>**更多：**</s> 


#### Java操作：

```
//********************添加********************
//方法1
redisTemplate.opsForValue().set("key","value",60,TimeUnit.SECONDS);//获取ValueOperations对象，通过key-value同时设置
//方法2
redisTemplate.boundValueOps("key").set("value",60,TimeUnit.SECONDS)//获取BoundValueOperations，通过key获取value对象，设置值
//********************设置时间********************
//方法1 如上↑
//方法2(单独设置)
redisTemplate.boundValueOps("").expire(60,TimeUnit.SECONDS)
//********************获取值********************
//方法1
redisTemplate.opsForValue().get("key"); //通过ValueOperations对象获取
//方法2
redisTemplate.boundValueOps("key").get(); //通过BoundValueOperations对象获取
//********************删除********************
redisTemplate.delete("key");
//********************键值递增/递减********************
redisTemplate.boundValueOps("").increment(3L);
```

#### 注意事项：
1. string在redis内部存储默认就是一个字符串，当遇到增减类操作incr,decr时会转成数值型进行计算1. redis所有的操作都是原子性的，采用单线程处理所有业务，命令是一个一个执行的，因此无需考虑并发带来的数据影响。1. 按数值进行操作的数据，如果原始数据不能转成数值，或超过了redis数值上线范围，将会报错。9223372036854775807 (java中long型数据最大值，Long.MAX_VALUE)
### 业务场景1（String类型作为数值时的增减）：

大型企业级应用中，分表操作是基本操作，使用多张表存储同类型数据，但是对应的主键id必须保证统一性，不能重复。 Oracle数据库具有sequence设定，可以解决该问题，但是MySQL数据库并不具有类似的机制，那么如何解决？

#### 解决方案：
- 设置数值数据增加指定范围的值
>  
 incr key             //自增1 incrby key increment  //增加指定数值 incrbyfloat key increment  //增加一个浮点数 

- 设置数值数据减少指定范围的值
>  
 decr key             //自减1 decrby key increment //减少指定数值 


### 业务场景2（String 数据时效性设置）：

场景一：“某某综艺”，启动海选投票，只能通过微信投票，每个微信号每4个小时只能投1票。

场景二：电商商家开启热门商品推荐，热门商品不能一直处于热门期，每种商品热门期维持3天，3天后自动取消热门

场景三：新闻网站会出现热点新闻，热点新闻最大的特征是对时效性，如何自动控制热点新闻的时效性

#### 解决方案：

给用户设置一个唯一的id，并为其设置一个有效时长，当时间已经超过设定时间后将id删除。即：**设置数据具有指定的声明周期**

>  
 setex key seconds value //增加、修改键值对并为其设定生命周期 psetex key milliseconds value //功能与上面一直，秒的单位不同 


### 业务场景3（高热度数据访问加速）：

主页高频访问信息显示控制，例如微博大V主页显示粉丝数与微博数量，这些数据就是热度数据，不断发生变化，这些数据如何放入Redis？

<img alt="" height="155" src="https://img-blog.csdnimg.cn/20210114183106355.png" width="369">

#### 解决方案：

在Redis中以json格式存储大V用户，定时刷新。

数据库中热点数据key命名惯例：

<img alt="" height="166" src="https://img-blog.csdnimg.cn/20210114183218331.png" width="592">

### 5.2Hash

为了区别与Redis中的键值对的称呼，hash中的键成为field，而key特征Redis的键。

```
//**********************添加********************
//添加一个Map
redisTemplate.boundHashOps("HashKey").putAll(hashMap );
//**********************获取值**********************
//获取所有的 小key==HashMap的key
Set keys1 = redisTemplate.boundHashOps("Key").keys();
//获取所有的值
List user = redisTemplate.opsForHash().values("key");
//根据key - key获取value
redisTemplate.opsForHash().hashOps.get("key", "小key");
//获取value的键值对
Map user = redisTemplate.opsForHash().entries("user");
//**********************判断**********************
//判断Hash中是否含有该值
Boolean isEmpty = redisTemplate.boundHashOps("key").hasKey("小Key");


```

#### 注意事项：
- hash类型下的value只能存储字符串，不允许存储其他类型数据，不存在嵌套现象。如果数据未获取到，对应的值为(nil)- 每个hash可以存储232-1个键值对- hash类型十分贴近对象的数据存储形式，并且可以灵活添加删除对象属性。但**hash设计不是为了存储大量对象的，切记不可滥用**，更不可以将hash作为对象列表使用- hgetall操作可以获取全部属性，如果内部fiekd过多，遍历整体数据效率就会很低，有可能成为数据访问瓶颈。
#### 业务场景1（购物车）：

<img alt="" height="435" src="https://img-blog.csdnimg.cn/20210114183700228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="643">

#### 解决方案：

<img alt="" height="277" src="https://img-blog.csdnimg.cn/20210114183737871.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="761">

#### 业务场景2（抢购，限购发放优惠券，激活码）：

商家id为key，抢购的商品ID为field，vallue为数量

#### 解决方案：
- 以商家id作为key- 将参与抢购的商品id作为field- 将参与抢购的商品数量作为对应的value- 抢购时使用降至的方式控制产品数量
### 5.3Set

```
//*******************获取值*******************
Set set1 = redisTemplate.boundSetOps("setKey").members();
//查询value是否存在
Boolean isEmpty = redisTemplate.boundSetOps("setKey").isMember("setValue2");
//获取value的长度
Long size = redisTemplate.boundSetOps("setKey").size();
//*******************删除**********************
//移除制定value
Long result1 = redisTemplate.boundSetOps("setKey").remove("setValue1");
//删除key
Boolean result2 = redisTemplate.delete("setKey");


```

### 5.4List

```
//********************添加******************
ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
redisTemplate.boundListOps("listKey").rightPushAll(list);
redisTemplate.boundListOps("listKey").leftPushAll(list);
//********************获取值****************
List listKey1 = redisTemplate.boundListOps("listKey").range(0, 10); //其实索引-结束索引
//从左弹出一个元素
String listKey2 = (String) redisTemplate.boundListOps("listKey").leftPop();  //从左侧弹出一个元素
//从右弹出一个元素
String listKey3 = (String) redisTemplate.boundListOps("listKey").rightPop(); //从右侧弹出一个元素
//根据索引查询元素
String listKey4 = (String) redisTemplate.boundListOps("listKey").index(1);
//获取长度
Long size = redisTemplate.boundListOps("listKey").size();
//********************修改********************
//修改List中的某条数据(key，索引，值)
redisTemplate.boundListOps("listKey").set(3L,"listLeftValue3");
//********************删除********************
//移除N个值为value(key,移除个数，值)
redisTemplate.boundListOps("listKey").remove(3L,"value");



```

#### 注意事项：
- list 中保存的数据都是string类型的，数据总容量式是有限的，最多232-1个元素（4294967295）- list具有索引的概念，但是操作数据时候通常以队列的形式进行入队出队操作，或以栈的形式进入栈出栈的操作- 获取全部数据操作结束索引设置为-1- list 可以对数据进行分页操作，通过第一页的信息来自list，第2页及更多的信息通过数据库的形式加载
### 业务场景1（微信朋友圈点赞）：

微信朋友圈点赞，要求按照点赞顺序显示点赞好友信息。 如果取消点赞，移除对应好友信息。

<img alt="" height="574" src="https://img-blog.csdnimg.cn/20210114184146501.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="377">

#### 解决方案：
- 移除指定数据
>  
 lrem key count value //count为移除的数量，value为移除哪个值 


### 业务场景2（最新消息的展示）：
- twitter、新浪微博、腾讯微博中个人用于的关注列表需要按照用户的关注顺序进行展示，粉丝列表需要将最近关注的粉丝列在前面<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2020052520203445.png">- 新闻、资讯类网站如何将最新的新闻或资讯按照发生的事件顺序展示- 企业运营过程中，系统将产生出大量的运营数据，如何保障堕胎服务器操作日志的统一顺序输出？
#### 解决方案：
- 依赖list的数据具有顺序的特征对信息进行管理- 使用队列模型解决多路信息汇总合并的问题- 使用栈模型解决最新消息的问题
### 5.5Zset

```
//***********************添加***************
redisTemplate.boundZSetOps("zSetKey").add("zSetVaule", 100D);
//插入多个元素，并设置分数
DefaultTypedTuple&lt;String&gt; p1 = new DefaultTypedTuple&lt;&gt;("zSetVaule1", 2.1D);
DefaultTypedTuple&lt;String&gt; p2 = new DefaultTypedTuple&lt;&gt;("zSetVaule2", 3.3D);
redisTemplate.boundZSetOps("zSetKey").add(new HashSet&lt;&gt;(Arrays.asList(p1,p2)));
//***********************获取值*************
//按照排名先后(从小到大)打印指定区间内的元素, -1为打印全部
Set&lt;String&gt; range = redisTemplate.boundZSetOps("zSetKey").range(key, 0, -1);
//获得指定元素的分数
Double score = redisTemplate.boundZSetOps("zSetKey").score("zSetVaule");
//返回集合内的成员个数
Long size = redisTemplate.boundZSetOps("zSetKey").size();
//返回集合内指定分数范围的成员个数（Double类型）
Long COUNT = redisTemplate.boundZSetOps("zSetKey").count(0D, 2.2D);
//返回集合内元素在指定分数范围内的排名（从小到大）
Set byScore = redisTemplate.boundZSetOps("zSetKey").rangeByScore(0D, 2.2D);
//带偏移量和个数，(key，起始分数，最大分数，偏移量，个数)
Set&lt;String&gt; ranking2 = redisTemplate.opsForZSet().rangeByScore("zSetKey", 0D, 2.2D 1, 3);
//返回集合内元素的排名，以及分数（从小到大）
Set&lt;TypedTuple&lt;String&gt;&gt; tuples = redisTemplate.boundZSetOps("zSetKey").rangeWithScores(0L, 3L);
for (TypedTuple&lt;String&gt; tuple : tuples) {
      System.out.println(tuple.getValue() + " : " + tuple.getScore());
}
//返回指定成员的排名
//从小到大
Long startRank = redisTemplate.boundZSetOps("zSetKey").rank("zSetVaule");
//从大到小
Long endRank = redisTemplate.boundZSetOps("zSetKey").reverseRank("zSetVaule");
//********************删除*******************
//从集合中删除指定元素
redisTemplate.boundZSetOps("zSetKey").remove("zSetVaule");
//删除指定索引范围的元素（Long类型、Double类型）
redisTemplate.boundZSetOps("zSetKey").removeRange(0L,3L);
redisTemplate.boundZSetOps("zSetKey").removeRangeByScorssse(0D,2.2D);
//********************修改*******************
//为指定元素加分（Double类型）
Double score = redisTemplate.boundZSetOps("zSetKey").incrementScore("zSetVaule",1.1D);


```

#### 注意事项：

set类型不允许数据重复，如果添加的数据在set中已经存在，将只保留一份 set虽然与hash的存储结构相同，但是无法启用hash中存储值的空间

#### 应用于同类信息的关联搜索，二度关联搜索，深度关联搜索：
- 显示共同关注（一度）- 显示共同好友（一度）- 由用户A出发，获取到好友用户B的好友信息列表（一度）- 由用户A出发，获取到好友用户B的购物清单列表（二度）- 由用户A出发，获取到好友用户B的游戏充值列表（二度）
#### 业务场景1（随机操作数据）：

****应用于随机推荐类信息检索，例如热点歌单推荐，热点新闻推荐，热点旅游线路，应用APP推荐，大V推荐等。****

每位用户首次使用进入头条时候会设置3项爱好的内容，但是后期为了增加用户的活跃度，兴趣点，必须让用户对其他信息类别逐渐产生兴趣，增加客户留存度，如何实现？

#### 业务分析：
- 系统分析出各个分类的最新或最热点信息条目并组织成set集合- 随机挑选其中部分信息- 配合用户关注信息分类中的热点信息组织展示的全信息集合
#### 解决方案：
- 随机获取集合中指定数量的数据
>  
 srandmember key [count] 

- 随机获取集合中的某个数据并将该数据移出集合
>  
 spop key 


#### 业务场景2（共同好友）：

<img alt="" height="541" src="https://img-blog.csdnimg.cn/20210114184905711.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="747">

#### 解决方案：
- 求两个集合的交、并、差集
>  
 sinter key1 [key2] //交集 sunion key1 [key2] //并集 sdiff key1 [key2] //差集(key1有但是key2没有的) 

- 求两个集合的交、并、差集并存储到指定集合中
>  
 sinterstore destination key1 [key2] sunionstore destination key1 [key2] sdiffstore destination key1 [key2] 

- 将指定数据从原始集合移动到目标集合中
>  
 smove source destination member 


#### 业务场景3（同类型不重复数据的合并操作）：

<img alt="" height="432" src="https://img-blog.csdnimg.cn/20210114185303983.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="916">

#### 解决方案：

依赖set集合数据不重复的特征，依赖set集合hash存储结构特征完成数据过滤与快速查询
- 根据用户id获取用户所有角色- 根据用户所有角色获取用户所有操作权限放入set集合- 根据用户所有觉得获取用户所有数据全选放入set集合
## 六、使用
|@Cacheable|方法、类|key为请求参数，value为返回结果|value、key和condition
|@CacheEvict||清空缓存|
|@CachePut||方法调用，value为返回结果|

### 5.1@Cacheable

Spring在缓存方法的返回值时是以键值对进行缓存的，值就是方法的返回结果，至于键的话，Spring又支持两种策略，默认策略和自定义策略，这个稍后会进行说明。需要注意的是当一个支持缓存的方法在对象内部被调用时是不会触发缓存功能的。@Cacheable可以指定三个属性，value、key和condition。

#### value属性

value属性是必须指定的，其表示当前方法的返回值是会被缓存在哪个Cache上的，对应Cache的名称。其可以是一个Cache也可以是多个Cache，当需要指定多个Cache时其是一个数组。   

```
@Cacheable(“cache1”)//Cache是发生在cache1上的
public User find(Integer id) {
  return null;
}
 
@Cacheable({“cache1”, “cache2”})//Cache是发生在cache1和cache2上的
public User find(Integer id) {
   return null;
}
```

#### key属性

key属性是用来指定Spring缓存方法的返回结果时对应的key的。该属性支持SpringEL表达式。当我们没有指定该属性时，Spring将使用默认策略生成key。我们这里先来看看自定义策略，至于默认策略会在后文单独介绍。

自定义策略是指我们可以通过Spring的EL表达式来指定我们的key。这里的EL表达式可以使用方法参数及它们对应的属性。使用方法参数时我们可以直接使用“#参数名”或者“#p [参数index]

```
@Cacheable(value=”users”, key=”#id”)
public User find(Integer id) {
   return null;
}
 
@Cacheable(value=”users”, key=”#p0”)
public User find(Integer id) {
    return null;
}
 
@Cacheable(value=”users”, key=”#user.id”)
public User find(User user) {
    return null;
}
 
@Cacheable(value=”users”, key=”#p0.id”)
public User find(User user) {
    return null;
}
 
```

 除了上述使用方法参数作为key之外，Spring还为我们提供了一个root对象可以用来生成key。通过该root对象我们可以获取到以下信息。
| 属性名称 |描述|示例
| methodName | 当前方法名 | #root.methodName 

当前方法名
| method | 当前方法 | #root.method.name 

当前方法
| target | 当前被调用的对象 | #root.target 

当前被调用的对象
| targetClass | 当前被调用的对象的class | #root.targetClass 

当前被调用的对象的class
| args | 当前方法参数组成的数组 | #root.args[0] 

当前方法参数组成的数组
| caches | 当前被调用的方法使用的Cache | #root.caches[0].name 

当前被调用的方法使用的Cache

当我们要使用root对象的属性作为key时我们也可以将“#root”省略，因为Spring默认使用的就是root对象的属性。如：   

```
@Cacheable(value={“users”, “xxx”}, key=”caches[1].name”)
public User find(User user) {
      return null;
}
```

#### condition属性

有的时候我们可能并不希望缓存一个方法所有的返回结果。通过condition属性可以实现这一功能。condition属性默认为空，表示将缓存所有的调用情形。其值是通过SpringEL表达式来指定的，当为true时表示进行缓存处理；当为false时表示不进行缓存处理，即每次调用该方法时该方法都会执行一次。如下示例表示只有当user的id为偶数时才会进行缓存。

```
@Cacheable(value={“users”}, key=”#user.id”, condition=”#user.id%2==0”)
 
   public User find(User user) {
 
      System.out.println(“find user by user “ + user);
 
      return user;
 
   }
```

#### 使用：

>  
 启动类增加：   @EnableCaching 


```
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
public @interface Cacheable {   
 //与cacheNames相同，@AliasFor是取别名
    @AliasFor("cacheNames")
    String[] value() default {};
    @AliasFor("value")
    //缓存组件名，数据存在缓存组件中以key:value的形式存储
    String[] cacheNames() default {};
    
	//与keyGenerator 2选1只能用一个，就是缓存的key
    String key() default "";
	//key的生成器；可以自己指定key的组件id 与上面的key二选一使用
    String keyGenerator() default "";
	//指定缓存管理器；或者cacheResolver指定获取解析器
    String cacheManager() default "";
    //
    String cacheResolver() default "";
    //指定符合条件的情况才缓存，例如condition="#id&gt;0"
    String condition() default "";
    /*
    否定缓存，当unless指定条件为true，方法返回值就不会被缓存；
    可以获取到结果进行判断。 unless="#result==null"
    */
    String unless() default "";
    //是否使用异步模式
    boolean sync() default false;
}
```



### 5.2@CachePut

@CachePut 的作用 主要针对方法配置，能够根据方法的请求参数对其结果进行缓存，和 @Cacheable 不同的是，它每次都会触发真实方法的调用

|参数|解释|example
|------
|value|缓存的名称，在 spring 配置文件中定义，必须指定至少一个|@CachePut(value=”my cache”)
|key|缓存的 key，可以为空，如果指定要按照 SpEL 表达式编写，如果不指定，则缺省按照方法的所有参数进行组合|@CachePut(value=”testcache”,key=”#userName”)
|condition|缓存的条件，可以为空，使用 SpEL 编写，返回 true 或者 false，只有为 true 才进行缓存|@CachePut(value=”testcache”,condition=”#userName.length()&gt;2”)

### 5.3**@CacheEvict**

@CachEvict 的作用 主要针对方法配置，能够根据一定的条件对缓存进行清空
|value|缓存的名称，在 spring 配置文件中定义，必须指定至少一个|@CacheEvict(value=”my cache”)
|key|缓存的 key，可以为空，如果指定要按照 SpEL 表达式编写，如果不指定，则缺省按照方法的所有参数进行组合|@CacheEvict(value=”testcache”,key=”#userName”)
|condition|缓存的条件，可以为空，使用 SpEL 编写，返回 true 或者 false，只有为 true 才进行缓存|@CacheEvict(value=”testcache”,condition=”#userName.length()&gt;2”)
|allEntries|是否清空所有缓存内容，缺省为 false，如果指定为 true，则方法调用后将立即清空所有缓存|@CachEvict(value=”testcache”,allEntries=true)
|beforeInvocation|是否在方法执行前就清空，缺省为 false，如果指定为 true，则在方法还没有执行的时候就清空缓存，缺省情况下，如果方法执行抛出异常，则不会清空缓存|@CachEvict(value=”testcache”，beforeInvocation=true)

### 5.4**@CacheConfig**

所有的@Cacheable（）里面都有一个value＝“xxx”的属性，这显然如果方法多了，写起来也是挺累的，如果可以一次性声明完 那就省事了， 所以，有了@CacheConfig这个配置，@CacheConfig is a class-level annotation that allows to share the cache names，如果你在你的方法写别的名字，那么依然以方法的名字为准。

```
@CacheConfig ( "books" )
public class BookRepositoryImpl implements BookRepository {
 
   @Cacheable
   public Book findBook(ISBN isbn) {...}
}
```

### 5.5**@Caching**

```
@Caching (put = {
@CachePut (value = "user" , key = "#user.id" ),
@CachePut (value = "user" , key = "#user.username" ),
@CachePut (value = "user" , key = "#user.email" )
})
public User save(User user) {<!-- -->
```

有时候我们可能组合多个Cache注解使用；比如用户新增成功后，我们要添加id–&gt;user；username—&gt;user；email—&gt;user的缓存；此时就需要@Caching组合多个注解标签了。

```
@Caching (put = {
@CachePut (value = "user" , key = "#user.id" ),
@CachePut (value = "user" , key = "#user.username" ),
@CachePut (value = "user" , key = "#user.email" )
})
public User save(User user) {<!-- -->
```

六、补充知识

更新中.............



## 【其它】Bean配置

```
@Bean
    public RedisTemplate&lt;String,Object&gt; getRedisString(LettuceConnectionFactory factory){
        RedisTemplate redisTemplate = new RedisTemplate();
        redisTemplate.setConnectionFactory(factory);
        Jackson2JsonRedisSerializer&lt;Object&gt; redisSerializer = new Jackson2JsonRedisSerializer(Object.class);
        redisTemplate.setDefaultSerializer(redisSerializer);
        return redisTemplate;
    }
```

## 动态切换Redis库

```
public RedisTemplate&lt;String, Object&gt; getRedisTemplate(RedisTemplate&lt;String, Object&gt; redisTemplate,int index)
    {
        LettuceConnectionFactory factory = (LettuceConnectionFactory)redisTemplate.getConnectionFactory();
        factory.setDatabase(index);
        factory.afterPropertiesSet();
        redisTemplate.setConnectionFactory(factory);
        factory.initConnection();
        return redisTemplate;
    }
```

<img alt="111111" src="https://img-blog.csdnimg.cn/20200706155203147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI2NDQ5MDg1,size_16,color_FFFFFF,t_70">

## redis并发竞争key问题如何解决

### 1. 问题描述

并发竞争key这个问题简单讲就是：

>  
 同时有多个客户端去set一个key。 


#### 示例场景 1

例如有多个请求一起去对某个商品减库存，通常操作流程是：
-  取出当前库存值 -  计算新库存值 -  写入新库存值 
假设当前库存值为 `20`，现在有2个连接都要减 `5`，结果库存值应该是 `10` 才对，但存在下面这种情况：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy93djNLNmo0aWJsOTByNlFEZmhISWZpY3h2THhvM0gyMXIwdkllVkVCbE43ZjRlaWNmSDFldXJUWHR2ZzgxUzBxNHY1aWFzMjdMdmc1TWpwdENaYjAxV2NqZEEvNjQw?x-oss-process=image/format,png">

#### 示例场景 2

比如有3个请求有序的修改某个key，按正常顺序的话，数据版本应该是 `1-&gt;2-&gt;3`，最后应该是 `3`。

但如果第二个请求由于网络原因迟到了，数据版本就变为了 `1-&gt;3-&gt;2`，最后值为 `2`，出问题了。

### 2. 解决方案

#### 2.1 乐观锁

乐观锁适用于大家一起抢着改同一个key，对修改顺序没有要求的场景。

`watch` 命令可以方便的实现乐观锁。

>  
 需要注意的是，如果你的 redis 使用了数据分片的方式，那么这个方法就不适用了。 


`watch` 命令会监视给定的每一个key，当 `exec` 时如果监视的任一个key自从调用watch后发生过变化，则整个事务会回滚，不执行任何动作。

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy93djNLNmo0aWJsOTByNlFEZmhISWZpY3h2THhvM0gyMXIwTHc1b2VLcG5KekZ0ZWNpY1BFMGlibUhuNkI2cXNXMGJ5QTVPNWZ2RnpnQnkxbmliTzAwMFRhbjVRLzY0MA?x-oss-process=image/format,png">

#### 2.2 分布式锁

适合分布式环境，不用关心 redis 是否为分片集群模式。

在业务层进行控制，操作 redis 之前，先去申请一个分布式锁，拿到锁的才能操作。

分布式锁的实现方式很多，比如 ZooKeeper、Redis 等。

#### 2.3 时间戳

适合有序需求场景，例如 `A` 需要把 key 设置为 `a`，然后 `B` 设置为 `b`，`C` 再设置为 `c`，最后的值应该是 `c`。

这时就可以考虑使用时间戳的方式：

>  
 A =&gt; set key1 {a 11:01} 
 B =&gt; set key1 {b 11:02} 
 C =&gt; set key1 {c 11:03} 


就是在写入时保存一个时间戳，写入前先比较自己的时间戳是不是早于现有记录的时间戳，如果早于，就不写入了。

假设 B 先执行了，key1 的值为 `{b 11:02}`，当A执行时，发现自己的时间戳`11:01`早于现有值，就不执行 set 操作了。

#### 2.4 消息队列

在并发量很大的情况下，可以通过消息队列进行串行化处理。这在高并发场景中是一种很常见的解决方案。

### 3. 小结

“Redis 并发竞争” 问题就是高并发写同一个key时导致的值错误。

常用的解决方法：
-  乐观锁，注意不要在分片集群中使用 -  分布式锁，适合分布式系统环境 -  时间戳，适合有序场景 -  消息队列，串行化处理 

