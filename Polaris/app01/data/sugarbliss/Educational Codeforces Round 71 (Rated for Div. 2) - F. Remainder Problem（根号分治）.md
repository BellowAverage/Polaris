
--- 
title:  Educational Codeforces Round 71 (Rated for Div. 2) - F. Remainder Problem（根号分治） 
tags: []
categories: [] 

---
**题目链接：**

**题意：一个长度为<img alt="5e5" class="mathcode" src="https://private.codecogs.com/gif.latex?5e5">的数组，初始为空，支持两种操作：**
- 1，x，y，表示将<img alt="a[x]+y" class="mathcode" src="https://private.codecogs.com/gif.latex?a%5Bx%5D&amp;plus;y">- 2，x，y，表示求所有下标模 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 为 <img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y"> 的数的和
**思路：分成两部分，<img alt="\sqrt{5e5}\approx 710" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Csqrt%7B5e5%7D%5Capprox%20710">，对于 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 大于710的直接暴力求和，小于等于710的维护一个<img alt="b[i][j]" class="mathcode" src="https://private.codecogs.com/gif.latex?b%5Bi%5D%5Bj%5D">表示模 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 为 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 的<img alt="sum" class="mathcode" src="https://private.codecogs.com/gif.latex?sum">和。对于每一个1操作，<img alt="" class="mathcode" src="https://private.codecogs.com/gif.latex?"><img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">只对<img alt="x\%i" class="mathcode" src="https://private.codecogs.com/gif.latex?x%5C%25i">有贡献，所以<img alt="b[i][x \% i] += y(1\leq i\leq 710)" class="mathcode" src="https://private.codecogs.com/gif.latex?b%5Bi%5D%5Bx%20%5C%25%20i%5D%20&amp;plus;%3D%20y%281%5Cleq%20i%5Cleq%20710%29">。**

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
const int N = 5e5 + 7;
inline int read()
{
    char ch = getchar(); int x = 0, f = 1;
    while(ch &lt; '0' || ch &gt; '9') {if(ch == '-') f = -1; ch = getchar();}
    while('0' &lt;= ch &amp;&amp; ch &lt;= '9') {x = x * 10 + ch - '0'; ch = getchar();}
    return x * f;
}
int a[N], b[720][720];
int main()
{
    IO; int q; cin &gt;&gt; q;
    while(q--)
    {
        int op, x, y;
        cin &gt;&gt; op &gt;&gt; x &gt;&gt; y;
        if(op == 1)
        {
            a[x] += y;
            for(int i = 1; i &lt;= 710; i++) b[i][x % i] += y;
        }
        else
        {
            if(x &lt;= 710) cout &lt;&lt; b[x][y] &lt;&lt; endl;
            else
            {
                ll ans = 0;
                for(int i = y; i &lt;= 5e5; i += x) ans += a[i];
                cout &lt;&lt; ans &lt;&lt; endl;
            }
        }
    }
    return 0;
}
```

 
