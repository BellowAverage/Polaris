
--- 
title:  Codeforces Global Round 4 - 1178E. Archaeology（鸽巢原理） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给出一个只包含 <img alt="a,b,c" class="mathcode" src="https://private.codecogs.com/gif.latex?a%2Cb%2Cc"> 的字符串 <img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s"> ，保证任意两个连续的字符都不相同，要求选出一个子序列 <img alt="t" class="mathcode" src="https://private.codecogs.com/gif.latex?t"> 使得它是一个回文串，并且<img alt="|t|\geq \left \lfloor \frac{|s|}{2} \right \rfloor" class="mathcode" src="https://private.codecogs.com/gif.latex?%7Ct%7C%5Cgeq%20%5Cleft%20%5Clfloor%20%5Cfrac%7B%7Cs%7C%7D%7B2%7D%20%5Cright%20%5Crfloor">。

**思路：**贪心从两端取，因为任意两个连续的字符都不相同，再根据，左端的两个字符和右端的两个字符，必然会有两个相等，所以我们两个两个找即可。

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
const int N = 1e6 + 7;
string s;
int vis[N];
int main()
{
    IO; cin &gt;&gt; s;
    int l = 0, r = s.length() - 1;
    while(l &lt;= r)
    {
        if(l == r) {vis[l] = 1; break;}
        if(s[l] == s[r]) vis[l] = vis[r] = 1;
        else if(s[l] == s[r-1]) vis[l] = vis[r-1] = 1;
        else if(s[l+1] == s[r]) vis[l+1] = vis[r] = 1;
        else if(s[l+1] == s[r-1]) vis[l+1] = vis[r-1] = 1;
        l += 2, r -= 2;
    }
    for(int i = 0; i &lt; s.length(); i++)
        if(vis[i]) cout &lt;&lt; s[i];
    cout &lt;&lt; '\n';
}

```

 
