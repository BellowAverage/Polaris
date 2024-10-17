
--- 
title:  STL 之 equal_range用法 
tags: []
categories: [] 

---
**equal_range**是C++ STL中的一种二分查找的算法，lower_bound返回区间的第一个大于等于<img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">的迭代器，upper_bound返回区间的第一个大于<img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">的迭代器，而**equal_range则是以pair的形式将两者都返回。**可以用来查询有序区间数字 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 出现的次数。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
int main()
{
    int a[] = {1,2,2,3,3,3,9,10};
    auto p = equal_range(a, a + 8, 3) ;
    printf("%d %d\n", *p.first, *p.second);
    //分别对应lower_bound和upper_bound的值
    printf("%d\n", p.second - p.first);
    //返回有序区间内数字3出现的次数
}

```

 
