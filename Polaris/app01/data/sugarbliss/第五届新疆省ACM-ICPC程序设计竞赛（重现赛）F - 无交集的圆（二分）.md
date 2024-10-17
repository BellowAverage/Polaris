
--- 
title:  第五届新疆省ACM-ICPC程序设计竞赛（重现赛）F - 无交集的圆（二分） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**对于每一个圆，我们求出每一个圆的最高点和最低点，然后对于每一个圆二分查找其他圆的最低点比当前圆的最高点高的个数，然后统计答案即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
double a[N], b[N], y, r;
int main()
{
    int n; scanf("%d",&amp;n);
    for(int i = 0; i &lt; n; i++)
    {
        scanf("%lf %lf", &amp;y, &amp;r);
        a[i] = y - r;
        b[i] = y + r;
    }
    sort(a, a + n);
    int ans = 0;
    for(int i = 0; i &lt; n; i++)
    {
        int k = upper_bound(a, a + n, b[i]) - a;
        ans += n - k;
    }
    printf("%d\n",ans);
}

```

 
