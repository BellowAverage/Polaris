
--- 
title:  Redis字符串 string类型 SDS数据结构 
tags: []
categories: [] 

---
        string 类型是我们在Redis中使用最多也是最基本、最常见的类型，string 类型跟memcahed一样都是按照 key-value 键值对的方式来存储的。

        string 类型是二进制安全的，它可以包含任何数据，包括图片、视频和序列化的对象，一个Redis字符串中value最大为 **512MB 。**

**      一、字符串常用的命令**

set &lt;key&gt; &lt;value &gt; 设置key - value  set相同的key时会被覆盖

get &lt;key&gt;  获取某个key的值

append &lt;key&gt; &lt;value&gt; 在可以的末尾追加某个值

strlen &lt;key&gt; 获取key的长度

setnx &lt;key&gt; &lt;value&gt; 设置key的值 ，只有key不存在时才可以设置key的值

incr &lt;key&gt; 将key中存储的值为数字时 数字增1， 只能对存储的值时数字时进行操作如果值为空则新增的值为1

decr &lt;key&gt;  将key中存储的值为数字时 数字减1

incrby / decrby &lt;key&gt; &lt;num&gt;  将key中存储的值为数字时,数字增/减num值

mset &lt;key1&gt; &lt;value1&gt; &lt;key2&gt; &lt;value2&gt; ... 批量设置多个key value

msetnx  &lt;key1&gt; &lt;value1&gt; &lt;key2&gt; &lt;value2&gt; ... 批量设置多个key value 只有key不存在时才可以设置key的值,如果其中有一个失败其他的key设置都不成功

mget &lt;key1&gt; &lt;key2&gt; ... 批量获取多个key的值

getrange &lt;key&gt; &lt;start&gt; &lt;end&gt; 截取key从start到end之间的值

setrange &lt;key&gt; &lt;start&gt; &lt;value&gt; 在key中start位置插入value值

setex &lt;key&gt; &lt;time&gt;  设置过期时间

getset &lt;key&gt; &lt;value&gt; 获取到key的值同时将值覆盖为新的value值 返回旧的value值

####         二、字符串的数据结构

         Redis字符串的数据结构为 简单动态字符串 SDS (Simple Dynamic String),采用预分配冗余空间的方式来减少内存的频繁分配。

** 1. SDS 结构**

        Redis 的字符串和 C 语言的字符串一样最后一个字符为空字符，这个空字符不会被计算在 len 里头。



<img alt="" height="230" src="https://img-blog.csdnimg.cn/e296a11539fd4f2291ab8f07633168bf.png" width="982">


- free: 空闲空间大小- len: 使用空间大小- buf: 存储空间
      **  2.SDS动态扩展操作**

        Redis动态扩展三个操作：

        1). 计算空闲空间是否足够。

        2). 开辟足够大小的空间。

        3). 开辟已使用相同的长度的空闲空间。（如果使用长度&gt;=1M 则开辟1M 空闲空间。如果使用长度

    **    3. Redis 字符串的性能优势**
- 快速获取字符串长度
        由于在 SDS 里存了已使用字符长度 len，所以当想获取字符串长度时直接返回 len 即可，时间复杂度为 O(1)。如果使用 C 语言的字符串的话它的字符串长度获取函数时间复杂度为 O(n)，n 为字符个数，因为他是从头到尾（到空字符'\0'）遍历相加。
- 避免缓冲区溢出
        C语言字符串在追加是需要提前开辟需要的空间，如果不开辟则造成缓冲区溢出。而Redis每次在追加字符串时都会先计算出空闲空间大小是否足够，然后开辟空间至满足所需要的的空间。
- 降低空间分配次数提升内存使用效率
        字符串的追加操作会涉及到内存分配问题，然而内存分配问题会牵扯内存划分算法以及系统调用，如果频繁发生的话影响性能，所以redis采取了两种优化方案：

        a). 空间预分配

        对于追加操作来说，Redis 不仅会开辟空间至够用而且还会预分配未使用的空间(free)来用于下一次操作。至于未使用的空间(free)的大小则由修改后的字符串长度决定。

        当修改后的字符串长度 len &lt; 1M，则会分配与 len 相同长度的未使用的空间(free) 当修改后的字符串长度 len &gt;= 1M，则会分配 1M 长度的未使用的空间(free)

        有了这个预分配策略之后会减少内存分配次数，因为分配之前会检查已有的 free 空间是否够，如果够则不开辟

        b). 惰性空间回收

        惰性空间回收适用于字符串缩减操作,当字符串减少时 Redis 不会立即回收减少的部分，而是会分配给下一个需要内存的程序。当然，Redis 也提供了回收内存的 api，可以自己手动调用来回收缩减部分的内存


