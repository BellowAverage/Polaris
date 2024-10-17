
--- 
title:  HashMap 实现原理 
tags: []
categories: [] 

---
##### 简介

HashMap 根据键的 hashCode 进行数据的存取，大多数情况下可以直接定位到它的值，从而具有很高的效率，是无序的，要想具有顺序可用 LinkedHashMap； 键值均可为 null；是非线程安全的，如果需要满足线程安全，可以用 Collections 的 synchronizedMap 或者使用 ConcurrentHashMap。

##### JDK1.7 中实现

<img src="https://img-blog.csdnimg.cn/2019100108484978.png#pic_center" alt="">

JDK1.7 中 HashMap 采用数组+链表的实现方式，Entry 是 HashMap 中的一个内部类，他的成员变量包括：key（键）、value（值）、next（用于实现链表结构，指向下一个链表节点）、hash（存放的是当前 key 的 hashCode）。
- `put` 方法
```
public V put(K key, V value) {<!-- -->
        if (table == EMPTY_TABLE) {<!-- --> //是否初始化            inflateTable(threshold);
        }
        if (key == null) //放置在0号位置
            return putForNullKey(value);
        int hash = hash(key); //计算hash值
        int i = indexFor(hash, table.length);  //计算在Entry[]中的存储位置
        for (Entry&lt;K,V&gt; e = table[i]; e != null; e = e.next) {<!-- -->
            Object k;
            if (e.hash == hash &amp;&amp; ((k = e.key) == key || key.equals(k))) {<!-- -->
                V oldValue = e.value;
                e.value = value;
                e.recordAccess(this);
                return oldValue;
            }
        }

        modCount++;
        addEntry(hash, key, value, i); //添加到Map中
        return null;
}

```

在添加键值对时，首先判断 table 是否初始化，如果没有，则进行初始化；然后判断 key 是否为 null，如果为 null，放置在 Entry[] 的 0 号位置，不为 null，计算在 Entry[] 数组的存储位置；判断该位置上是否存在元素，如果存在，则遍历该 Entry[] 数组位置上的链表；判断 key 是否存在，如果 key 已经存在，则用新的 value 值，替换点旧的 value 值，并将旧的 value 值返回；将 key-vlaue 生成 Entry 实体，添加到 HashMap 中的 Entry[] 数组中。
- `get` 方法
```
public V get(Object key) {<!-- -->
     if (key == null)
         //返回table[0] 的value值
         return getForNullKey();
     Entry&lt;K,V&gt; entry = getEntry(key);

     return null == entry ? null : entry.getValue();
}
final Entry&lt;K,V&gt; getEntry(Object key) {<!-- -->
     if (size == 0) {<!-- -->
         return null;
     }

     int hash = (key == null) ? 0 : hash(key);
     for (Entry&lt;K,V&gt; e = table[indexFor(hash, table.length)];
         e != null;
         e = e.next) {<!-- -->
         Object k;
         if (e.hash == hash &amp;&amp;
             ((k = e.key) == key || (key != null &amp;&amp; key.equals(k))))
            return e;
      }
     return null;
}

```

首先计算hash值，然后调用indexFor()方法得到该key在table中的存储位置，得到该位置的单链表，遍历链表找到key和其对应的Entry，通过entry.value返回value值。

##### JDK1.8 中实现

在JDK1.8中，HashMap存储的数据结构由数组+链表的方式，变为数组+链表+红黑树的存储方式，提升了性能；解决了JDK1.7版在并发条件下出现死循环的问题。 问题

`问`：如果两个key的hashCode相同，如何获取值对象？ `答`：当调用get方法时，HashMap会使用key的hashCode值，找到bucket位置，因为hashCode相同，bucket会发生碰撞，然后遍历链表，通过key的equals方法找到键值对。

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
