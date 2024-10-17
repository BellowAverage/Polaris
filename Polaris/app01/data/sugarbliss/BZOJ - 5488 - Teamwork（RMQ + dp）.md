
--- 
title:  BZOJ - 5488 - Teamwork（RMQ + dp） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**可以直接<img alt="dp" class="mathcode" src="https://private.codecogs.com/gif.latex?dp">也可以<img alt="dp+RMQ" class="mathcode" src="https://private.codecogs.com/gif.latex?dp&amp;plus;RMQ">**。**

**<img alt="dp+RMQ" class="mathcode" src="https://private.codecogs.com/gif.latex?dp&amp;plus;RMQ">思路**：定义<img alt="dp[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D">表示前 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 个数分组的最优解，明显可以从<img alt="\begin{bmatrix}dp[i-k], dp[i-1] \end{bmatrix}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7Ddp%5Bi-k%5D%2C%20dp%5Bi-1%5D%20%5Cend%7Bbmatrix%7D">转移到<img alt="dp[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D">，其中区间最值用RMQ求出即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e5 + 7;
int a[N][21], dp[N], n, k;
void ST()
{
    for(int j = 1; (1&lt;&lt;j) &lt;= n; j++)
        for(int i = 1; (i+(1&lt;&lt;j)-1) &lt;= n; i++)
            a[i][j] = max(a[i][j-1], a[i+(1&lt;&lt;(j-1))][j-1]);
}
int RMQ(int l, int r)
{
    int k = (int)(log(r-l+1)/log(2.0));
    return max(a[l][k],a[r-(1&lt;&lt;k)+1][k]);
}
int main()
{
    scanf("%d%d",&amp;n,&amp;k);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d", &amp;a[i][0]);
    ST();
    for(int i = 1; i &lt;= n; i++)
        for(int j = max(i - k, 0); j &lt; i; j++)
            dp[i] = max(dp[i], dp[j] + RMQ(j+1, i) * (i - j));
    printf("%d\n",dp[n]);
}

```

**直接<img alt="dp" class="mathcode" src="https://private.codecogs.com/gif.latex?dp">思路**：<img alt="dp[j]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bj%5D">表示前 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 个数字中后 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 个数字分一组时的最优解，<img alt="mx[j]" class="mathcode" src="https://private.codecogs.com/gif.latex?mx%5Bj%5D">，表示前 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 个数字中后 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 个数字分一组时的最大值。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e4 + 7;
ll a[N], dp[N], mx[N], tmp;
int n, k;
int main()
{
    scanf("%d%d",&amp;n,&amp;k);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d",&amp;a[i]);
    for(int i = 1; i &lt;= n; i++)
    {
        tmp = dp[1];
        for(int j = min(i, k); j &gt; 1; j--)
        {
            tmp = max(tmp, dp[j]);
            mx[j] = max(mx[j-1], a[i]);
            dp[j] = dp[j-1] - mx[j-1] * (j-1) + mx[j] * j;
        }
        dp[1] = tmp + a[i];
        mx[1] = a[i];
    }
    ll ans = 0;
    for(int i = 1; i &lt;= k; i++)
        ans = max(ans, dp[i]);
    cout &lt;&lt; ans &lt;&lt; endl;
}

```

 
