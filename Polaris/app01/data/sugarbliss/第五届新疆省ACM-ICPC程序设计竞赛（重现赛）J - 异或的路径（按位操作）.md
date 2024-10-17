
--- 
title:  第五届新疆省ACM-ICPC程序设计竞赛（重现赛）J - 异或的路径（按位操作） 
tags: []
categories: [] 

---
**题目链接：**

**思路：<img alt="w_{i}" class="mathcode" src="https://private.codecogs.com/gif.latex?w_%7Bi%7D">**表示从根到 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 的异或和，**<img alt="w_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?w_%7Bj%7D">**表示从根到 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 的异或和，那么<img alt="i,j" class="mathcode" src="https://private.codecogs.com/gif.latex?i%2Cj">两点之间的路径异或和就可以用<img alt="w_{i}\oplus w_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?w_%7Bi%7D%5Coplus%20w_%7Bj%7D">表示。显然<img alt="w_{i}" class="mathcode" src="https://private.codecogs.com/gif.latex?w_%7Bi%7D">可以用<img alt="dfs" class="mathcode" src="https://private.codecogs.com/gif.latex?dfs">求出，考虑到<img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">的范围，显然不能暴力，只能按位考虑，要求的是异或和，那么每一位的贡献就是1的个数和0的个数乘积，然后乘上每一个二进制位对十进制的贡献，由于每对<img alt="i,j" class="mathcode" src="https://private.codecogs.com/gif.latex?i%2Cj">都会出现两次，最后<img alt="ans\ll =1" class="mathcode" src="https://private.codecogs.com/gif.latex?ans%5Cll%20%3D1">即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
#define pii pair&lt;int, int&gt;
const int mod = 1e9 + 7;
const int N = 1e5 + 7;
vector &lt;pii&gt; G[N];
int w[N];
void dfs(int u)
{
    for(auto p: G[u])
    {
        w[p.first] = w[u] ^ p.second;
        dfs(p.first);
    }
}
int main()
{
    int n; scanf("%d",&amp;n);
    for(int i = 2; i &lt;= n; i++)
    {
        int f, x;
        scanf("%d%d",&amp;f, &amp;x);
        G[f].push_back({i, x});
    }
    dfs(1); ll ans = 0, cnt;
    for(int i = 0; i &lt; 20; i++)
    {
        cnt = 0;
        for(int j = 2; j &lt;= n; j++)
            if((w[j] &gt;&gt; i) &amp; 1) cnt++;
        ans = (ans % mod + ((1 &lt;&lt; i) % mod * cnt % mod * (n - cnt) % mod)) % mod;
    }
    ans &lt;&lt;= 1; ans %= mod;
    cout &lt;&lt; ans &lt;&lt; endl;
}

```

 
