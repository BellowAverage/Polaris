
--- 
title:  STL之优先队列详解 
tags: []
categories: [] 

---
>  
 普通的队列是一种先进先出的数据结构，元素在队列尾追加，而从队列头删除。在优先队列中，元素被赋予优先级。当访问元素时，具有最高优先级的元素最先删除。优先队列具有最高级先出 （first in, largest out）的行为特征。通常采用堆数据结构来实现。 ——百度百科 


### 一、引入

优先队列具有的基本操作（back操作没有）；

```
q.size();//返回q里元素个数
q.empty();//返回q是否为空，空则返回1，否则返回0
q.push(k);//在q的末尾插入k
q.pop();//删掉q的第一个元素
q.top();//返回q的第一个元素

```

除此之外，优先队列具有可**自动排序**的功能：默认降序 优先队列的本质是堆实现。

### 二、头文件及声明

优先队列头文件与普通队列一样：

```
#include &lt;queue&gt;

```

优先队列声明格式为： **priority_queue&lt;结构类型&gt; 队列名;** 如下：

```
priority_queue &lt;int&gt; q;  //默认降序
priority_queue &lt;double&gt; p;

```

除此之外，还有如下格式：

```
priority_queue &lt;int, vector&lt;int&gt;, less&lt;int&gt; &gt; p; //降序
priority_queue &lt;int, vector&lt;int&gt;, greater&lt;int&gt; &gt; q;  //升序
//注意：此处两个"&gt;"之间必须有空格，否则会成为右移运算符“&gt;&gt;”

```

降序可省略书写，当然建议全部写成上面的格式，这样不会在你想用升序的时候突然忘记怎么写了，当然还有一个最主要的好处，那就是你可可以好好的装一装cow B 哈哈哈哈！！！
