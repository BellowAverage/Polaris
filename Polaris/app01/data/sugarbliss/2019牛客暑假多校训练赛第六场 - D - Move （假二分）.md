
--- 
title:  2019牛客暑假多校训练赛第六场 - D - Move （假二分） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 个物品的体积和 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 个相同体积的盒子，让你将 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 个物品装进 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 个盒子，在物品体积小于盒子体积的前提下尽量先装体积较大的物品。问盒子的最小体积。

**思路：**本题不具有单调性（物品的体积不连续），暴力枚举答案即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e3 + 7;
int a[N], b[N], n, k;
multiset &lt;int&gt; s;
multiset&lt;int&gt; ::iterator it;
int check(int x)
{
    s.clear();
    for(int i = 1; i &lt;= n; i++) s.insert(a[i]);
    for(int i = 0; i &lt; k; i++)
    {
        int v = x;
        while(!s.empty() &amp;&amp; (it = s.upper_bound(v) ) != s.begin())
        {
            it--; v -= *it;
            s.erase(it);
        }
        if(s.empty()) return 1;
    }
    return 0;
}
int main()
{
    int T; scanf("%d",&amp;T);
    for(int Cas = 1; Cas &lt;= T; Cas++)
    {
        scanf("%d%d",&amp;n, &amp;k);
        int sum = 0, mx = 0;
        for(int i = 1; i &lt;= n; i++)
            scanf("%d",&amp;a[i]), sum += a[i], mx = max(mx, a[i]);
        int ans = max(mx, (int)ceil(1.0 * sum / k));
        while(1)
        {
            if(check(ans))
            {
                printf("Case #%d: %d\n",Cas, ans);
                break;
            }
            ans++;
        }
    }
}
/*
1
15 5
39 39 39 39 39 60 60 60 60 60 100 100 100 100 10
*/

```

 
