
--- 
title:  POJ - 3255 - Roadblocks （次短路） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**1是起点，n为终点，求次短路。

**思路：**维护最短路的时候更新次短路。
1. 当前距离小于最短路，那么当前最短路变成次短路，更新最短路。1. 若当前距离不能更新最短路，但比次短路小，更新次短路（也就是介于次短路和最短路之间时更新次短路）
```
#include &lt;iostream&gt;
#include &lt;string.h&gt;
#include &lt;algorithm&gt;
#include &lt;vector&gt;
#include &lt;queue&gt;
#include &lt;stdio.h&gt;
using namespace std;
const int maxn = 1e5 + 7;
#define inf 0x3f3f3f3f
#define pii pair&lt;int, int&gt;
int n, m, s, t;
int d[maxn], p[maxn], vis[maxn];
vector &lt;pii&gt; E[maxn];
void init()
{
    for(int i = 0; i &lt;= n; i++) E[i].clear();
    memset(d,0x3f,sizeof(d));
    memset(p,0x3f,sizeof(p));
    memset(vis,0,sizeof(vis));
}
void Dijkstra()
{
    d[s] = 0;
    priority_queue&lt;pii&gt; Q;
    Q.push({-d[s], s});
    while(!Q.empty())
    {
        int now = Q.top().second;
        int val = -Q.top().first;
        Q.pop();if(p[now] &lt; val) continue;
        for(int j = 0; j &lt; E[now].size(); j++)
        {
            int v = E[now][j].first; int w = val + E[now][j].second;
            if(d[v] &gt; w)
                swap(d[v], w), Q.push({-d[v], v});
            if(p[v] &gt; w &amp;&amp; d[v] &lt; w)
                p[v] = w, Q.push({-p[v], v});
        }
    }
}
int main()
{
    while(~scanf("%d%d",&amp;n,&amp;m))
    {
        init(); int a, b, x;
        while(m--)
        {
            scanf("%d%d%d",&amp;a,&amp;b,&amp;x);
            E[a].push_back({b,x});
            E[b].push_back({a,x});
        }
        s = 1; Dijkstra();
        printf("%d\n",p[n]);
    }
    return 0;
}
/*
4 4
1 2 100
2 4 200
2 3 250
3 4 100
*/

```

 
