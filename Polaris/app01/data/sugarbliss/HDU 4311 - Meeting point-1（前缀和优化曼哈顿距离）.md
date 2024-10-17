
--- 
title:  HDU 4311 - Meeting point-1（前缀和优化曼哈顿距离） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给定n个点，找出一点使得该点到其余各点的曼哈顿距离总和最小，输出最小值。

**思路：**分别对横纵坐标排序，比如说横坐标 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> ，排好序后如果点 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 为所求，则前<img alt="i-1" class="mathcode" src="https://private.codecogs.com/gif.latex?i-1">个点的 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 坐标小于<img alt="x[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?x%5Bi%5D">，<img alt="i+1" class="mathcode" src="https://private.codecogs.com/gif.latex?i&amp;plus;1"> 到 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 这 <img alt="n-i" class="mathcode" src="https://private.codecogs.com/gif.latex?n-i"> 个点的 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 坐标大于<img alt="x[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?x%5Bi%5D">，则 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 轴对应的结果为<img alt="(i-1)*x[i]-s[i-1]+s[n]-s[i]-(n-i)*x[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?%28i-1%29*x%5Bi%5D-s%5Bi-1%5D&amp;plus;s%5Bn%5D-s%5Bi%5D-%28n-i%29*x%5Bi%5D">，<img alt="s[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?s%5Bi%5D"> 为前 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 个点的坐标值和。对 <img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y"> 轴也做同样处理，枚举取出最大值即可。

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
const int N = 1e5 + 7;
int n;
ll s[N];
struct node
{
    ll x, y, sumx, sumy;
}a[N];
bool cmp1(node a, node b) {return a.x &lt; b.x;}
bool cmp2(node a, node b) {return a.y &lt; b.y;}
int main()
{
    IO; int T; cin &gt;&gt; T;
    while(T--)
    {
        cin &gt;&gt; n;
        for(int i = 1; i &lt;= n; i++)
            cin &gt;&gt; a[i].x &gt;&gt; a[i].y;
        memset(s, 0, sizeof s);
        sort(a + 1, a + 1 + n, cmp1);
        for(int i = 1; i &lt;= n; i++)
            s[i] = s[i-1] + a[i].x;
        for(int i = 1; i &lt;= n; i++)
            a[i].sumx = (i - 1) * a[i].x - s[i-1] + s[n] - s[i] - (n - i) * a[i].x;
        memset(s, 0, sizeof s);
        sort(a + 1, a + 1 + n, cmp2);
        for(int i = 1; i &lt;= n; i++)
            s[i] = s[i-1] + a[i].y;
        for(int i = 1; i &lt;= n; i++)
            a[i].sumy = (i - 1) * a[i].y - s[i-1] + s[n] - s[i] - (n - i) * a[i].y;
        ll ans = INF;
        for(int i = 1; i &lt;= n; i++)
            ans = min(ans, a[i].sumx + a[i].sumy);
        cout &lt;&lt; ans &lt;&lt; '\n';
    }
}
```

 
