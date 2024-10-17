
--- 
title:  Redis List列表常用命令和数据结构 
tags: []
categories: [] 

---
#### 前言        

Redis中的List列表是一个单键多值，简单的字符串列表，是按照插入的顺序进行排序。它是一个双向的链表式结构，可以在列表的头和尾进行操作，对头尾两端的操作性能很高，操作中间节点时的性能会较差。

####  **一、常用的命令**

##### 1. lpush/rpush

添加列表操作，lpush在列表的左边添加值，rpush在列表的右边添加值。

>  
 lpush/rpush &lt;key&gt; &lt;val1&gt; &lt;val2&gt; &lt;val3&gt;... 


<img alt="" height="69" src="https://img-blog.csdnimg.cn/3a24dd99b73f4538a77813c7c4cdaf6c.png" width="487">

##### 2. lrange

返回列表中指定范围的值。

>  
 lrange &lt;key&gt; &lt;start&gt; &lt;end&gt;  


返回列表中指定START到END的元素，其中 0 表示列表的第一个元素， 1 表示列表的第二个元素，以 -1 表示列表的最后一个元素， -2 表示列表的倒数第二个元素

 <img alt="" height="160" src="https://img-blog.csdnimg.cn/9440ab75ba264cd986e89fd8d649eaf7.png" width="496">

##### 3.  lpop/rpo

从列表中取值，lpop从左边开始取值,rpop从右边取值。 

lpop/rpop &lt;key&gt; &lt;count&gt;

从左边/右边取出 count个值并返回，如果key的值都被取出后key则失效。

<img alt="" height="130" src="https://img-blog.csdnimg.cn/fcbb77c7d4d944d3a8f54f29d63a2e72.png" width="468">

##### 4. rpoplpush

列表取值并插入到另一个列表的左边

>  
 rpoplpush &lt;key1&gt; &lt;key2&gt;  


从key1列表中取出一个值插入到key2列表的左边

 <img alt="" height="34" src="https://img-blog.csdnimg.cn/fc3cfbba3f274b3e95d702d6db2ba660.png" width="491">



##### 5. lindex

按照索引下标获取元素

>  
 lindex &lt;key&gt; &lt;index&gt; 


##### 6. llen

获取列表的长度

>  
 llen &lt;key&gt; 


##### 7. linsert

在value值后面/前面插入newvalue值

>  
 linsert &lt;key&gt; after/before &lt;value&gt; &lt;newvalue&gt;  


##### 8. lrem

删除列表值，从左边删除

>  
 lrem &lt;key&gt; &lt;n&gt; &lt;value&gt; 


从左边删除n个value

##### 9.  lset

设置列表值

>  
 lset &lt;key&gt; &lt;index&gt; &lt;value&gt; 


将索引为index的值替换成value

#### ** 二、数据结构**

Redis List列表使用的数据结构不是简简单单使用链表，它是使用quickList(快速链表)。

快速链表是由多个压缩列表(ziplist)组成的双向链表。

##### 1. 压缩列表(ziplist)

当列表的所有值大小小于64字节且元素数量小于512个时，则会使用压缩列表，压缩列表是一块连续的内存，它是经过特殊编码的双向列表结构，用于提高内存使用效率。

压缩列表是由一系列的entry组成，每个entry可以存放不同数据类型的数据。

<img alt="" height="90" src="https://img-blog.csdnimg.cn/31b37e0d823f4a2e82b97f0ddcdef108.jpeg" width="626">

ZLbytes：类型为uint32_t, 存储了当前ziplist所用的内存的字节数。 ZLtail：类型为uint32_t, 它是ziplist中最后一个entry的偏移量，用于快速定位最后一个entry, 以快速完成pop等操作。 ZLlen：类型为uint16_t, ziplit中entry的总数量，用于做快速统计entry的数量。 ZLend：结束字节, 其值为全F, 即0xff。

##### 2. 快速链表(quickList)

将多个ziplist通过使用prev和next指针双向连接起来。每一个quicklistnode就是一个ziplist加prev和next指针。

quickList结构图：

<img alt="" height="237" src="https://img-blog.csdnimg.cn/8e1f975a32794e74beaf9522457fc926.jpeg" width="591">

#### 总结

       quickList的使用主要是为了能够节省内存，提高链表的效率，它的每个节点都是一个ziplist，每个节点都可以存储多个元素数据，当进行更新时只需要修改ziplist的内存数据不会影响到其他节点的内存分配情况，因此它即节省了内存也降低了更新的复杂程度，同时每个节点都有存有对应的统计数据，也提高了整个链表的查询效率。
