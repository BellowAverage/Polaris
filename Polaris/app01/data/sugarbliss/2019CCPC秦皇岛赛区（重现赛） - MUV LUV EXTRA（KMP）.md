
--- 
title:  2019CCPC秦皇岛赛区（重现赛） - MUV LUV EXTRA（KMP） 
tags: []
categories: [] 

---
**题目链接：**

**思路： **枚举开始出现的部分长度，最优的循环节就是最后 <img alt="p" class="mathcode" src="https://private.codecogs.com/gif.latex?p"> 个字符构成的字符串的最小循环节，由于<img alt="KMP" class="mathcode" src="https://private.codecogs.com/gif.latex?KMP">可以求前缀的最小循环节，考虑把字符串反转，使用<img alt="KMP" class="mathcode" src="https://private.codecogs.com/gif.latex?KMP">可以求出每一个前缀的最小循环节：<img alt="i-next[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?i-next%5Bi%5D">，即求出了每一个后缀的最小循环节。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef pair&lt;int, int&gt; pii;
typedef pair&lt;ll, int&gt; pli;
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
template&lt;class T, class S&gt; inline void add(T&amp; a, S b) {a += b; if(a &gt;= mod) a -= mod;}
template&lt;class T, class S&gt; inline void sub(T&amp; a, S b) {a -= b; if(a &lt; 0) a += mod;}
template&lt;class T, class S&gt; inline bool chkmax(T&amp; a, S b) {return a &lt; b ? a = b, true : false;}
template&lt;class T, class S&gt; inline bool chkmin(T&amp; a, S b) {return a &gt; b ? a = b, true : false;}
const int N = 1e7 + 7;
ll Next[N];
string s, str;
void getnext(ll l)
{
    ll j = 0 , k = -1 ;
    Next[0] = -1;
    while(j &lt; l)
    {
        if( k == -1 || s[j] == s[k] )
            Next[++j] = ++k;
        else
            k = Next[k];
    }
}
ll a, b;
int main()
{
    IO; ll n, len;
    while(cin &gt;&gt; a &gt;&gt; b)
    {
        cin &gt;&gt; s;
        s = s.substr(s.find('.') + 1);
        n = s.length(); reverse(s.begin(), s.end());
        getnext(n);
        ll ans = -INF;
        for(ll i = 1; i &lt;= n; i++)
        {
            len = i - Next[i];
            ans = max((i * a - len * b), ans);
        }
        cout &lt;&lt; ans &lt;&lt; endl;
    }
    return 0;
}

```

 
