
--- 
title:  Codeforces Round #575 (Div. 3) D1D2 - RGB Substring(思维) 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一个只含有<img alt="R,G,B" class="mathcode" src="https://private.codecogs.com/gif.latex?R%2CG%2CB">的字符串让你做最小的修改，使得存在长度为 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 的子串，满足是 "<img alt="RGBRGBRGB..." class="mathcode" src="https://private.codecogs.com/gif.latex?RGBRGBRGB...">"的子串。

**思路：**考虑只有<img alt="R,G,B" class="mathcode" src="https://private.codecogs.com/gif.latex?R%2CG%2CB">三个字符，只有三种可能<img alt="R" class="mathcode" src="https://private.codecogs.com/gif.latex?R">开头，<img alt="G" class="mathcode" src="https://private.codecogs.com/gif.latex?G">开头，<img alt="B" class="mathcode" src="https://private.codecogs.com/gif.latex?B">开头，我们可以暴力用原串匹配三种可能的字符串，选其中最小的即为答案，时间复杂度<img alt="O(kn)" class="mathcode" src="https://private.codecogs.com/gif.latex?O%28kn%29">过<img alt="D1" class="mathcode" src="https://private.codecogs.com/gif.latex?D1">没问题，对于<img alt="D2" class="mathcode" src="https://private.codecogs.com/gif.latex?D2">我们可以用前缀和优化，如果不匹配需要修改令<img alt="pre[i] = 1" class="mathcode" src="https://private.codecogs.com/gif.latex?pre%5Bi%5D%20%3D%201">，反之为0，然后求前缀和，维护<img alt="pre[i]-pre[i-k]" class="mathcode" src="https://private.codecogs.com/gif.latex?pre%5Bi%5D-pre%5Bi-k%5D">的最小值即可。

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
const int N = 2e5 + 7;
inline int read()
{
    char ch = getchar(); int x = 0, f = 1;
    while(ch &lt; '0' || ch &gt; '9') {if(ch == '-') f = -1; ch = getchar();}
    while('0' &lt;= ch &amp;&amp; ch &lt;= '9') {x = x * 10 + ch - '0'; ch = getchar();}
    return x * f;
}
int n, k, pre[N];
char str[N], s[4] = "RGB";
int main()
{
    int T; T = read();
    while(T--)
    {
        n = read(); k = read(); scanf("%s",str + 1);
        int ans = inf;
        for(int i = 0; i &lt; 3; i++)
        {
            for(int j = 1; j &lt;= n; j++)
                if(str[j] != s[(j + i) % 3]) pre[j] = 1;
                else pre[j] = 0;
            for(int j = 1; j &lt;= n; j++) pre[j] += pre[j - 1];
            for(int j = k; j &lt;= n; j++)
                ans = min(ans, pre[j] - pre[j-k]);
        }
        printf("%d\n", ans);
    }
    return 0;
}

```

 
