
--- 
title:  “==” “equals()” “hashCode()” 傻傻分不清 
tags: []
categories: [] 

---
## 简介

#### `==`

对于基本数据类型 byte、short、char、int、long、float、double，boolean，`==` 比较的是它们的值；而对于引用类型，如：类、接口、数组等，`==` 比较的是他们在内存中的存放地址。

#### `equals()`

默认情况下，`equals` 方法是调用 Object 类的 `equals` 方法，Object 的 `equals` 方法是用于判断对象的内存地址引用是不是同一个（是不是同一个对象）；当然有一些类重写了 `equals` 方法，只进行内容的比较，如 String 类。

#### `hashCode()`

`hashCode` 方法采用哈希算法（哈希算法也称为散列算法，是将数据依特定算法直接指定到一个地址上），返回的就是一个 hash 码，用途是在对对象进行散列的时候作为 key 输入，因此我们需要每个对象的 hash 码尽可能不同，这样才能保证散列的存取性能。

## 总结
-  `equals` 相等的两个对象，它们的 `hashCode` 一定相等，反之不成立。 -  `hashCode` 方法只有在集合中用到。 -  String、Integer、Boolean、Double 等这些类都重写了 `equals` 和`hashCode` 方法，这两个方法是根据对象的内容来比较和计算`hashCode` 的。 
**为什么重写 `equels` 方法就必须重写 `hashCode` 方法？**

1）如果两个对象根据 `equals` 返回 True，根据定义，则其 `hashCode` 方法返回的 hash 值一定要相等，则就必须重写 `hashCode` 方法，直接使用 Object 类的 `hashCode` 方法不一定相等；

2）如果两个对象根据 `equals` 返回 False，不要求 `hashCode` 必须不一样，但为不同的对象产生不同的整数结果可以提高哈希表的性能。

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
