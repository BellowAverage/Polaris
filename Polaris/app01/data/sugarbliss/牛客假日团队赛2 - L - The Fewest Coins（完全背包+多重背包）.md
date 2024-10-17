
--- 
title:  牛客假日团队赛2 - L - The Fewest Coins（完全背包+多重背包） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**顾客来老板那买东西，价值M元，有N种钱，每种钱顾客有一定数量，而老板有无限数量。求最少用多少张钞票可以满足交易，比如样例，顾客出50+25元，老板找5元，即可满足，需要3张。

**思路：**顾客用多重背包转移状态，老板用完全背包。这里的背包求得是最小价值，且要恰好装满。故初始化数组时应将<img alt="dp" class="mathcode" src="https://private.codecogs.com/gif.latex?dp">初始化为<img alt="inf" class="mathcode" src="https://private.codecogs.com/gif.latex?inf">，<img alt="dp[0] = 0" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5B0%5D%20%3D%200">。背包的容量上限为<img alt="mx*mx + t" class="mathcode" src="https://private.codecogs.com/gif.latex?mx*mx%20&amp;plus;%20t">，证明使用鸽巢原理，自行百度吧。(上限设大点也行，20000左右)。

```
#include &lt;stdio.h&gt;
#include &lt;math.h&gt;
#include &lt;string.h&gt;
#include &lt;algorithm&gt;
#include &lt;iostream&gt;
using namespace std;
#define debug(x) cerr&lt;&lt;#x&lt;&lt;'='&lt;&lt;(x)&lt;&lt;endl;
#define debugp(x) cerr&lt;&lt;#x&lt;&lt;"= {"&lt;&lt;(x.first)&lt;&lt;", "&lt;&lt;(x.second)&lt;&lt;"}"&lt;&lt;endl;
#define debug2(x, y) cerr&lt;&lt;"{"&lt;&lt;#x&lt;&lt;", "&lt;&lt;#y&lt;&lt;"} = {"&lt;&lt;(x)&lt;&lt;", "&lt;&lt;(y)&lt;&lt;"}"&lt;&lt;endl;
#define inf 0x3f3f3f3f
const int maxn = 2e6 + 7;
typedef long long ll;
int dp1[maxn], dp2[maxn], v[maxn], w[maxn];
int a[maxn], k[maxn];
int main()
{
    int n, t, p, cnt = 0; scanf("%d%d",&amp;n,&amp;t);
    int mx = 0;
    for(int i = 1; i &lt;= n; i++) 
        scanf("%d",&amp;a[i]), mx = max(mx, a[i]);
    mx = mx * mx + t;
    for(int i = 1; i &lt;= n; i++) scanf("%d",&amp;k[i]);
    for(int i = 1; i &lt;= n; i++)
    {
        p = 1;
        while(k[i] &gt; p)
        {
            w[cnt] = p * a[i];
            v[cnt++] = p * 1;
            k[i] -= p;
            p *= 2;
        }
        w[cnt] = k[i] * a[i];
        v[cnt++] = k[i] * 1;
    }
    memset(dp1, 0x3f, sizeof dp1);
    memset(dp2, 0x3f, sizeof dp2);
    dp1[0] = 0, dp2[0] = 0;
    for(int i = 0; i &lt; cnt; i++)
        for(int j = mx; j &gt;= w[i]; j--)
            dp1[j] = min(dp1[j], dp1[j - w[i]] + v[i]);
    for(int i = 1; i &lt;= n; i++)
        for(int j = a[i]; j &lt;= mx; j++)
            dp2[j] = min(dp2[j], dp2[j - a[i]] + 1);
    int ans = inf;
    for(int i = t; i &lt;= mx; i++)
        ans = min(ans, dp1[i] + dp2[i-t]);
    if(ans &gt;= mx) puts("-1");
    else cout &lt;&lt; ans &lt;&lt; endl;
}

```

 

 
