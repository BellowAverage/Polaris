
--- 
title:  牛客假日团队赛2 - G - County Fair Events（贪心） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有n个任务，每个任务有开始时间和持续时间，让你求最多完成几个任务。

**思路：**最大不相交覆盖问题，对线段的右端点进行升序排序，每加入一个线段，然后选择后面若干个右端点相同的线段，选择左端点最大的那一条，如果加入以后不会跟之前的线段产生公共部分，那么就加入，否则就继续判断后面的线段。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5+ 7;
struct node
{
    int x, y;
}a[N];
bool cmp(node a, node b)
{
    if(a.y == b.y) a.x &gt; b.x;
    return a.y &lt; b.y;
}
int main()
{
    int n;
    scanf("%d",&amp;n);
    for(int i = 0; i &lt; n; i++)
    {
        scanf("%d%d",&amp;a[i].x, &amp;a[i].y);
        a[i].y += a[i].x;
    }
    sort(a, a + n, cmp);
    int cnt = 1, p = 0;
    for(int i = 1; i &lt; n; i++)
    {
        if(a[i].x &gt;= a[p].y)
            cnt++, p = i;
    }
    cout &lt;&lt; cnt &lt;&lt; endl;
}
```

 
