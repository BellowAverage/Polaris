
--- 
title:  HDU - 3949 - XOR（线性基求第k小的异或和） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**求第k小的异或和。

**思路：**我们要将线性基改造成每一位相互独立。 具体操作就是如果<img alt="i &lt; j" class="mathcode" src="https://private.codecogs.com/gif.latex?i%20%3C%20j">，<img alt="a_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7Bj%7D"> 的第 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 位是1，就将<img alt="a_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7Bj%7D">异或上<img alt="a_{i}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7Bi%7D">。 经过一系列操作之后，对于二进制的某一位 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 。只有 <img alt="a_{i}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7Bi%7D"> 的这一位是1，其他都是0。 所以查询的时候将 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 二进制拆分，对于1的位，就异或上对应的线性基。 最终得出的答案就是k小值。由于异或和可能为0，所以要判断一下线性基里的元素和总的元素个数是否相等，不想等则代表异或和为0，<img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k">--即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
#define ll long long
int n, q; ll x, cnt;
struct Linear_basis
{
    ll d[61], p[61];
    void init()
    {
        memset(d,0,sizeof(d));
        memset(p,0,sizeof(p));
        cnt = 0;
    }
    bool add(ll val)
    {
        for(int i = 60; i &gt;= 0; i--)
            if(val &amp; (1LL &lt;&lt; i))
            {
                if(!d[i])
                {
                    d[i] = val;
                    break;
                }
                val^=d[i];
            }
        return val &gt; 0;
    }
    ll query_max()
    {
        ll ret = 0;
        for(int i = 60; i &gt;= 0; i--)
            if((ret ^ d[i]) &gt; ret)
                ret ^= d[i];
        return ret;
    }
    ll query_min()
    {
        for(int i = 0;i &lt;= 60; i++)
            if(d[i])
                return d[i];
        return 0;
    }
    void rebuild()
    {
        for(int i = 60; i &gt;= 0; i--)
            for(int j = i - 1; j &gt;= 0; j--)
                if(d[i] &amp; (1LL &lt;&lt; j))
                    d[i] ^= d[j];
        for(int i = 0; i &lt;= 60; i++)
            if(d[i]) p[cnt++] = d[i];
    }
    ll kth_query(ll k)
    {
        int ret = 0;
        if(k &gt;= (1LL &lt;&lt; cnt))
            return -1;
        for(int i = 60; i &gt;= 0; i--)
            if(k &amp; (1LL &lt;&lt; i))
                ret ^= p[i];
        return ret;
    }
}LB;
int main()
{
    int T, cas = 1; scanf("%d",&amp;T);
    while(T--)
    {
        printf("Case #%d:\n", cas++);
        LB.init();
        scanf("%d",&amp;n);
        for(int i = 1; i &lt;= n; i++)
            scanf("%lld", &amp;x), LB.add(x);
        LB.rebuild();
        scanf("%d",&amp;q);
        while(q--)
        {
            scanf("%lld", &amp;x);
            if(cnt != n) x--;
            printf("%lld\n", LB.kth_query(x));
        }
    }
}

```

 
