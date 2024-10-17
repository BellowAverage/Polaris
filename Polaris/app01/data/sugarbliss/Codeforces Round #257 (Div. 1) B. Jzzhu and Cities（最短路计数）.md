
--- 
title:  Codeforces Round #257 (Div. 1) B. Jzzhu and Cities（最短路计数） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**这个国家有n个城市，编号1-n，编号1的城市为首都，城市之间有m条双向道路连接，同时有k条火车路线可以直接让其他城市与首都城市连接，每条火车路线也存在自己的长度，因为火车路线的修建存在一定花费，现在需要保证首都在其余的n-1个城市的距离最短的情况下，去除一些没必要的火车道路，问最多能去除几条。

**思路：**直接把火车路线和普通的公路全部建图，然后从源点1开始求到其他点的最短路，我们可以把最后求出的到每个城市的最短路dis与火车路线的距离进行比较，如果dis小于火车路线，说明此时这条火车路线根本不可能参与，所以去除，如果dis等于火车路线，就需要判断有没有其他路线可以到达（最短路计数），如果有就去除。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int maxn = 4e5 + 7;
#define inf 0x3f3f3f3f
#define pii pair&lt;int, int&gt;
int n, m, k, s, t;
int d[maxn], vis[maxn], p[maxn];
vector&lt;pii&gt;E[maxn];
void init()
{
    for(int i = 0; i &lt;= n; i++) E[i].clear();
    memset(d,0x3f,sizeof(d));
    memset(vis,0,sizeof(vis));
}
void Dijkstra()
{
    d[s] = 0;
    priority_queue&lt;pii&gt; Q;
    Q.push({-d[s],s});
    while(!Q.empty())
    {
        int now = Q.top().second;
        Q.pop(); if(vis[now]) continue;
        vis[now] = 1;
        for(int j = 0; j &lt; E[now].size(); j++)
        {
            int v = E[now][j].first;
            if(d[v] == d[now]+E[now][j].second) p[v]++;
            if(d[v] &gt; d[now]+E[now][j].second)
            {
                d[v] = d[now]+E[now][j].second;
                Q.push({-d[v],v}); p[v] = 1;
            }
        }
    }
}
struct node
{
    int v, x;
}pre[maxn];
int main()
{
    scanf("%d%d%d",&amp;n, &amp;m, &amp;k);
    init();
    int a, b, x;
    while(m--)
    {
        scanf("%d%d%d",&amp;a,&amp;b,&amp;x);
        E[a].push_back({b,x});
        E[b].push_back({a,x});
    }
    for(int i = 1; i &lt;= k; i++)
    {
        scanf("%d%d",&amp;pre[i].v, &amp;pre[i].x);
        E[1].push_back({pre[i].v,pre[i].x});
        E[pre[i].v].push_back({1,pre[i].x});
    }
    s = 1; Dijkstra();
    int ans = 0;
    for(int i = 1; i &lt;= k; i++)
    {
        int u = pre[i].v;
        if(d[u] &lt; pre[i].x) ans++;
        if(d[u] == pre[i].x &amp;&amp; p[u] &gt; 1) p[u]--, ans++;
    }
    printf("%d\n", ans);
    return 0;
}
/*
5 5 3
1 2 1
2 3 2
1 3 3
3 4 4
1 5 5
3 5
4 5
5 5
*/

```

 
