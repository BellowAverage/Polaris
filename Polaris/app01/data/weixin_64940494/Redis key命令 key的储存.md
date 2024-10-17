
--- 
title:  Redis key命令 key的储存 
tags: []
categories: [] 

---
        Redis是目前使用比较广泛的nosql数据库，它也是一种基于key-value结构的数据库且支持多种数据类型，Redis中它的存储是使用一张hash表用于存储所有的key和对应value的地址。因此key的命令是我们必须要掌握的。

##### 前项

>  
  数据准备，首先我们先在redis中设置一些数据 arr1 =  beijing      
 arr2 = shanghai    
 arr3 = shenzhen  
 arr4 = guangzhou 
 param1 = guangdong    
 param2=hunan  
 param3 = jiangxi  
 param4 = hubei 


##### Key命令使用

######  1. keys [pattern] 

查看当前库的key(*代表通配符)。该命令慎用，keys命令会扫描所有key,由于redis的执行是串行执行，当key过多时使用keys命令时会导致阻塞其他命令的执行，从而导致redis服务的崩溃。大多数生产使用redis时会将keys命令禁用。

keys *  查看所有的key<img alt="" height="154" src="https://img-blog.csdnimg.cn/41fe689348aa444fac908f43302b7f90.png" width="262">

 keys arr* 匹配以arr开头的key

 <img alt="" height="83" src="https://img-blog.csdnimg.cn/68ba7286d85b4d22af3984b78498fd3c.png" width="478">

  keys *guangzhou  匹配以guangzhou结尾的key 

<img alt="" height="69" src="https://img-blog.csdnimg.cn/be3981c73a1d442e9aa1b159e7a5a149.png" width="526">

           keys param1  指定查看key为param1

 <img alt="" height="38" src="https://img-blog.csdnimg.cn/401aa77d791847acb37aefe4f0abe779.png" width="433">

######   2. exists [key . . .] 

判断key是否存在,可以同时判断多个key

exists arr1  判断arr1 是否存在 返回1则存在 返回0则不存在

<img alt="" height="36" src="https://img-blog.csdnimg.cn/68d11675252443e7a6e21909afe7ba2e.png" width="407">

<img alt="" height="34" src="https://img-blog.csdnimg.cn/4a35f00667f343c3840d805971e89556.png" width="473">

exists arr1 arr2 arr3 同时判断arr1 arr2 arr3 是否存在 匹配到n个key则返回n

如果都不存在则返回0

 <img alt="" height="35" src="https://img-blog.csdnimg.cn/57b86d9d44e3496cb3fe35d53910ee19.png" width="530">

 <img alt="" height="68" src="https://img-blog.csdnimg.cn/77930790683b4f88a23dac210e12d1d0.png" width="550">

###### 3. type key

查看key的类型，只能支持单个判断

<img alt="" height="36" src="https://img-blog.csdnimg.cn/773eeb7343fb4df797c8d938c9f72b98.png" width="514">

###### 4. del [key . . .]

删除指定的key 删除n个key 则返回n   

unlink [key . . .]异步删除

 <img alt="" height="38" src="https://img-blog.csdnimg.cn/1f8cf57ab7a14978a8b87f44378e696c.png" width="550">

###### 5. exprie key [second]

设置key的过期时间<img alt="" height="39" src="https://img-blog.csdnimg.cn/e0bd30a4a657483eadf44e44ba01d793.png" width="513">

###### 6. ttl key

查看key还剩多少时间过期，数字代表剩下多少秒， -2 代表已过期， -1 代表永不过期

 <img alt="" height="221" src="https://img-blog.csdnimg.cn/d73add88e3c54f3d88681dcfe4afa8a7.png" width="568">

###### 7. dbsize 

查看当前key的数量

<img alt="" height="122" src="https://img-blog.csdnimg.cn/bc60d2fdec164fc79d4c492eb5752798.png" width="432">

##### Key的存储

redis中对key的存储使用的是一张全局的hashtable来存储，将每个key使用siphash函数生成一个64位的数字作为存储在hashtable里的索引。

当不同的键被落在同一个索引下时，使用链表结构来存储。如下图：

<img alt="" height="551" src="https://img-blog.csdnimg.cn/094a972412254a4b8e1e421e9e95841b.jpeg" width="651">

###### 渐进式rehash

当相同的索引键链表节点数过大，超过整个hashtable的数量时，那么查找key的效率就会降低，因此redis则会对该全局hashtable进行rehash的操作。

如果 key的数量过大时直接进行rehash操作进行扩容时有可能会导致redis服务阻塞，因此redis则采用的是渐进式的rehash操作。

###### 渐进式rehash的过程

redis在启动时内部默认会分配两个hashtable（ht0 、ht1），在正常使用时则使用其中一个ht0，当需要进行rehash操作时ht1才需要被使用到。

渐进式rehash的操作步骤：

1、首先将原ht1的空间扩容，让ht1同时有ht0 和 ht1两个哈希表的空间大小。

2、进行rehash操作时，在ht0中维护一个索引计数器 rehashidx ， 并将它的值设置为 0 。

3、在rehash期间，当执行添加、删除、查找或者更新操作时，redis会将ht0 哈希表在 rehashidx 索引上的所有键值对 rehash 到 ht1，同时rehashidx 的值加1。

4、当rehash的次数不断增多时，ht0的所有键值对都会被 rehash 至 ht1，此时rehashidx 属性的值设为 -1 ，则代表rehash 操作已经全部完成，那么ht1和ht0的位置进行交换，前面提到的默认操作都是在ht0上的。

        总之，rehash操作主要是解决由于hash冲突导致key链表过大影响性能，而使用渐进式rehash操作则是未来避免key数量过大因rehash导致redis服务的阻塞。这些机制最终的目的都是为了能够提高redis服务的性能。
