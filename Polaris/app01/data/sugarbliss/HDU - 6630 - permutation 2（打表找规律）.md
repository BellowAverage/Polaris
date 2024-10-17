
--- 
title:  HDU - 6630 - permutation 2（打表找规律） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你<img alt="1" class="mathcode" src="https://private.codecogs.com/gif.latex?1"> ~ <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">数字组成的序列固定开头和结尾，并且相邻两个数字绝对值之差小于等于2，问方案数？

**思路：**打表发现**<img alt="1" class="mathcode" src="https://private.codecogs.com/gif.latex?1"> ~ <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">**的方案为<img alt="f[n]=f[n-1]+f[n-3]" class="mathcode" src="https://private.codecogs.com/gif.latex?f%5Bn%5D%3Df%5Bn-1%5D&amp;plus;f%5Bn-3%5D">，那么其余情况也与**<img alt="1" class="mathcode" src="https://private.codecogs.com/gif.latex?1"> ~ <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">**的方案有关，观察发现<img alt="x == 1 || y == n" class="mathcode" src="https://private.codecogs.com/gif.latex?x%20%3D%3D%201%20%7C%7C%20y%20%3D%3D%20n">时方案为<img alt="f[y-x]" class="mathcode" src="https://private.codecogs.com/gif.latex?f%5By-x%5D">，其他为<img alt="f[y-x-1]" class="mathcode" src="https://private.codecogs.com/gif.latex?f%5By-x-1%5D">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
const int mod = 998244353;
#define ll long long
ll f[N];
int n, x, y;
int main()
{
    f[1] = 1; f[2] = 1;
    for(int i = 3; i &lt;= N; i++)
        f[i] = (f[i-1] % mod + f[i-3] % mod) % mod;
    int T; scanf("%d", &amp;T);
    while(T--)
    {
        scanf("%d%d%d",&amp;n, &amp;x, &amp;y);
        if(x == 1 &amp;&amp; y == n) printf("%lld\n", f[y]);
        else if(x == 1 || y == n) printf("%lld\n", f[y-x]);
        else printf("%lld\n", f[y-x-1]);
    }
}

```

 
