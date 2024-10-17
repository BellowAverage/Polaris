
--- 
title:  牛客练习赛4 - A - Laptop（二维偏序） 
tags: []
categories: [] 

---
**题目链接：**

**思路：二维偏序问题，按照第一维排序，再用树状数组处理第二维即可。**

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
int n, c[N];
vector&lt;int&gt; v;
void add(int x, int y) {while(x &lt;= n) c[x] += y, x += x&amp;-x;}
int sum(int x) {int ret = 0;while(x &gt; 0) ret += c[x], x -= x&amp;-x; return ret;}
int getid(int x){return lower_bound(v.begin(),v.end(),x)-v.begin() + 1;}
struct node
{
    int x, y;
    bool operator &lt;(const node &amp;tmp)const{
        return x &lt; tmp.x;
    }
}a[N];

int main()
{
    IO; cin &gt;&gt; n;
    for(int i = 0; i &lt; n; i++)
    {
        cin &gt;&gt; a[i].x &gt;&gt; a[i].y;
        v.push_back(a[i].y);
    }
    sort(a, a + n);
    sort(all(v)); v.erase(unique(all(v)), v.end());
    int ans = 0;
    for(int i = n - 1; i &gt;= 0; i--)
    {
        int pos = getid(a[i].y);
        if(sum(pos) != n - 1 - i) ans++;
        add(pos, 1);
    }
    cout &lt;&lt; ans &lt;&lt; endl;
}
```

 
