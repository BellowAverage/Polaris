
--- 
title:  第五届新疆省ACM-ICPC程序设计竞赛（重现赛）H - 虚无的后缀（DP or 贪心） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**两个数乘积末尾0的个数只和两个书数中2和5因子的个数有关，统计每一个数中2和5的个数，我们用<img alt="dp[i][j][s]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D%5Bs%5D">表示前<img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">个数字中选<img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j">个数字，其中有<img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s">个5因子时（<img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s">表示总的因子），2因子的个数。

<img alt="dp" class="mathcode" src="https://private.codecogs.com/gif.latex?dp">方程就是：<img alt="dp[i][j][s] = max(dp[i][j][s], dp[i-1][j-1][s-c5[i]] + c2[i])" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D%5Bs%5D%20%3D%20max%28dp%5Bi%5D%5Bj%5D%5Bs%5D%2C%20dp%5Bi-1%5D%5Bj-1%5D%5Bs-c5%5Bi%5D%5D%20&amp;plus;%20c2%5Bi%5D%29">。由于数据范围，要用滚动数组优化：

优化后就是：<img alt="dp[j][s] = max(dp[j][s], dp[j-1][s-c5[i]] + c2[i])" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bj%5D%5Bs%5D%20%3D%20max%28dp%5Bj%5D%5Bs%5D%2C%20dp%5Bj-1%5D%5Bs-c5%5Bi%5D%5D%20&amp;plus;%20c2%5Bi%5D%29">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e4 + 7;
int c2[N], c5[N], dp[201][N];
int main()
{
    ll n, k, x;
    cin &gt;&gt; n &gt;&gt; k;
    for(int i = 1; i &lt;= n; i++)
    {
        scanf("%lld",&amp;x);
        while(x % 5 == 0)
        {
            c5[i]++;
            x /= 5;
        }
        while(x % 2 == 0)
        {
            c2[i]++;
            x /= 2;
        }
    }
    memset(dp, -0x3f, sizeof dp);
    dp[0][0] = 0; int ans = 0;
    for(int i = 1; i &lt;= n; i++)
        for(int j = k; j &gt;= 1; j--)
            for(int s = n*36; s &gt;= c5[i]; s--)
                dp[j][s] = max(dp[j][s], dp[j-1][s-c5[i]] + c2[i]);
    for(int s = 0; s &lt;= n*36; s++)
        ans = max(ans, min(dp[k][s], s));
    cout &lt;&lt; ans &lt;&lt; endl;
}
/*
2 2
20 5
*/

```

**贪心思路：让选取k个数，那我们去掉n-k个贡献较小的数即可。**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e4 + 7;
int c2[N], c5[N], vis[N];
int main()
{
    ll x; int n, k, s2 = 0, s5 = 0;
    scanf("%d%d",&amp;n, &amp;k);
    for(int i = 1; i &lt;= n; i++)
    {
        scanf("%lld",&amp;x);
        while(x % 5 == 0)
        {
            c5[i]++, s5++;
            x /= 5;
        }
        while(x % 2 == 0)
        {
            c2[i]++, s2++;
            x /= 2;
        }
    }
    int tmp = 0, p;
    for(int i = 1; i &lt;= n - k; i++)
    {
        tmp = 0;
        for(int j = 1; j &lt;= n; j++)
        {
            int v = min(s5 - c5[j], s2 - c2[j]);
            if(!vis[j] &amp;&amp; v &gt; tmp)
            {
                tmp = v;
                p = j;
            }
        }
        vis[p] = 1;
        s5 -= c5[p];
        s2 -= c2[p];
    }
    cout &lt;&lt; min(s5, s2) &lt;&lt; endl;
}
/*
2 2
20 5
*/

```

 
