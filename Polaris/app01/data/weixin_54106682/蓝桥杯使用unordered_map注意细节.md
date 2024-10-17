
--- 
title:  蓝桥杯使用unordered_map注意细节 
tags: []
categories: [] 

---
> 
   今天在做蓝桥杯真题的时候，发现在蓝桥杯官网上进行代码提交，出现了编译错误，进去看了以后发现是蓝桥杯测评时，无法识别unordered_map. 
 

具体报错如下所示：

进行搜索后，发现在蓝桥杯提交的代码若用到了unordered_map或者unordered_set，需要加入头文件

#include&lt;tr1/unordered_set&gt;

#include&lt;tr1/unordered_map&gt;

以及命名空间using namespace std::tr1;

```
#include&lt;tr1/unordered_set&gt;
#include&lt;tr1/unordered_map&gt;
using namespace std::tr1;
```

另外需要注意的是，加入了该命名空间using namespace std::tr1;后，依然需要加入命名空间using namespace std; 否则若代码中使用了pair语法，则会发生编译错误。

并且在使用unordered_map&lt;int,pair&lt;int,int&gt; &gt; s时,需要注意&gt; &gt;之间有一个空格，若不添加空格，会出现如下报错。


