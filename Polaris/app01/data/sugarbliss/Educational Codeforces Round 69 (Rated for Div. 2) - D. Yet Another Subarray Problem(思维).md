
--- 
title:  Educational Codeforces Round 69 (Rated for Div. 2) - D. Yet Another Subarray Problem(思维) 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一段序列 <img alt="a_i" class="mathcode" src="https://private.codecogs.com/gif.latex?a_i"> ，让你选 <img alt="l,r" class="mathcode" src="https://private.codecogs.com/gif.latex?l%2Cr"> 使得 <img alt="\sum_{i=l}^{r}a_i-k*\left \lceil \frac{r-l+1}{m}\right \rceil" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Csum_%7Bi%3Dl%7D%5E%7Br%7Da_i-k*%5Cleft%20%5Clceil%20%5Cfrac%7Br-l&amp;plus;1%7D%7Bm%7D%5Cright%20%5Crceil"> 最大。

**思路：**考虑到 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m"> 最大为10，这题突破点在 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m"> 。当所选子段长度能整除以 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m"> 的时候，再添加一个数才会使得我们多去减一个 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 。如果能将 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 和 <img alt="a_i" class="mathcode" src="https://private.codecogs.com/gif.latex?a_i">合并到一个序列，我们就能用前缀和解决问题。我们可以枚举 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m"> 的余数作为区间的右端点 <img alt="r" class="mathcode" src="https://private.codecogs.com/gif.latex?r"> （只有枚举所有的余数才能取到所有的 <img alt="l,r" class="mathcode" src="https://private.codecogs.com/gif.latex?l%2Cr"> ），在余数的位置 <img alt="-k" class="mathcode" src="https://private.codecogs.com/gif.latex?-k"> ，因为每隔 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m"> 才出现 <img alt="-k" class="mathcode" src="https://private.codecogs.com/gif.latex?-k"> 操作，然后前缀和更新<img alt="ans" class="mathcode" src="https://private.codecogs.com/gif.latex?ans">即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef pair&lt;int, int&gt; pii;
typedef pair&lt;ll, ll&gt; pll;
#define mp make_pair
#define pb push_back
#define all(x) x.begin(), x.end()
#define bug prllf("*********\n")
#define debug(x) cerr&lt;&lt;#x&lt;&lt;" = "&lt;&lt;(x)&lt;&lt;endl
#define debugp(x) cerr&lt;&lt;#x&lt;&lt;"= {"&lt;&lt;(x.first)&lt;&lt;", "&lt;&lt;(x.second)&lt;&lt;"}"&lt;&lt;endl
#define debug2(x, y) cerr&lt;&lt;"{"&lt;&lt;#x&lt;&lt;", "&lt;&lt;#y&lt;&lt;"} = {"&lt;&lt;(x)&lt;&lt;", "&lt;&lt;(y)&lt;&lt;"}"&lt;&lt;endl
#define IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;
const int mod = 998244353;
const double eps = 1e-8;
const double pi = acos(-1);
const int N = 3e5 + 7;
int n, m, k, a[N], b[N];
int main()
{
    IO; cin &gt;&gt; n &gt;&gt; m &gt;&gt; k;
    for(int i = 0; i &lt; n; i++) cin &gt;&gt; a[i];
    ll ans = 0;
    for(int s = 0; s &lt; m; s++)
    {
        for(int i = 0; i &lt; n; i++) b[i] = a[i] - (i % m == s ? k : 0);
        ll tmp = 0;
        for(int i = 0; i &lt; n; i++)
        {
            tmp = max(tmp + b[i], 0ll);
            if(i % m == s) ans = max(ans, tmp);
        }
    }
    cout &lt;&lt; ans &lt;&lt; endl;
}
/*
7 3 10
2 -4 15 -3 4 8 3
*/

```

 
