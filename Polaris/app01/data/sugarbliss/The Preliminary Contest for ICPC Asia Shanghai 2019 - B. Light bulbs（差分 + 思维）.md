
--- 
title:  The Preliminary Contest for ICPC Asia Shanghai 2019 - B. Light bulbs（差分 + 思维） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**一排 N个初始关着的灯泡，M个操作，每个操作使得区间 [L,R] 的状态反转，求最后开着灯泡的数量。

**思路：**内存只有8192K，考虑差分，但不能直接遍历，考虑到每一个区间只有奇数才会有贡献，而 M 只有1000，直接遍历区间计算贡献即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef pair&lt;int, int&gt; pii;
typedef pair&lt;ll, int&gt; pli;
typedef pair&lt;ll, ll&gt; pll;
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
const int N = 2e5 + 7;
int n, m;
map &lt;int, int &gt; mp;
int main()
{
    int T, ca = 1; scanf("%d", &amp;T);
    while(T--)
    {
        scanf("%d%d",&amp;n, &amp;m);
        while(m--)
        {
            int x, y; scanf("%d%d",&amp;x, &amp;y);
            mp[x]++; mp[y+1]--;
        }
        int pre = 0, ans = 0, sum = 0;
        for(auto x : mp)
        {
            if(sum &amp; 1) ans += x.first - pre;
            pre = x.first;
            sum += x.second;
        }
        mp.clear();
        printf("Case #%d: %d\n", ca++, ans);
    }
}

```

 
