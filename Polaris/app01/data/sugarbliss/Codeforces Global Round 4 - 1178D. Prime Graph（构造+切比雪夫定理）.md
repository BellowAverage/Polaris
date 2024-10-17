
--- 
title:  Codeforces Global Round 4 - 1178D. Prime Graph（构造+切比雪夫定理） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给出 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 个点，要求构成一个简单图，使得边的总数是素数，并且每个点的度数也是素数。

**思路：**如果 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 是素数直接把这些点连成一个环即可，如果 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 不是质数，那么从 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">  <img alt="(i\leq 1\leq n)" class="mathcode" src="https://private.codecogs.com/gif.latex?%28i%5Cleq%201%5Cleq%20n%29">开始，在圆环中加入 <img alt="i\rightarrow i+\frac{n}{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?i%5Crightarrow%20i&amp;plus;%5Cfrac%7Bn%7D%7B2%7D"> 的边。这样一定会连<img alt="n+\frac{n}{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?n&amp;plus;%5Cfrac%7Bn%7D%7B2%7D">条边，而且每一个点的度数不是2就是3。根据：<img alt="\frac{3n}{4}\sim \frac{3n}{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B3n%7D%7B4%7D%5Csim%20%5Cfrac%7B3n%7D%7B2%7D">之间一定有一个素数，所以保证有解。

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
const int N = 1e5 + 7;
bool is_prime[N + 5];
void Euler_prime()
{
    ll prime[N + 5];
    int i, j, c = 0;
    memset(is_prime, true, sizeof(is_prime));
    for(i = 2; i &lt;= N; i++)
    {
        if(is_prime[i])
            prime[c++] = i;
        for(j = 0; j &lt; c &amp;&amp; prime[j] * i &lt;= N; j++)
        {
            is_prime[prime[j] * i] = false;
            if(i % prime[j] == 0) break;
        }
    }
}
int n;
int main()
{
    IO; Euler_prime(); cin &gt;&gt; n;
    if(is_prime[n])
    {
        cout &lt;&lt; n &lt;&lt; endl;
        for(int i = 2; i &lt;= n; i++)
            cout &lt;&lt; i - 1 &lt;&lt; " " &lt;&lt; i &lt;&lt; '\n';
        cout &lt;&lt; n &lt;&lt; " " &lt;&lt; 1 &lt;&lt; '\n';
    }
    else
    {
        int k = n;
        while(!is_prime[k]) k++;
        cout &lt;&lt; k &lt;&lt; '\n';
        for(int i = 2; i &lt;= n; i++)
            cout &lt;&lt; i - 1 &lt;&lt; " " &lt;&lt; i &lt;&lt; '\n';
        cout &lt;&lt; n &lt;&lt; " " &lt;&lt; 1 &lt;&lt; '\n';
        for(int i = 1; i &lt;= k - n; i++)
            cout &lt;&lt; i &lt;&lt; " " &lt;&lt; i + n / 2 &lt;&lt; '\n';
    }
}
```

 
