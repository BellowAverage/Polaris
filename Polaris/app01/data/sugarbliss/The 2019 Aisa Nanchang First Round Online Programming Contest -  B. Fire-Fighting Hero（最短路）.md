
--- 
title:  The 2019 Aisa Nanchang First Round Online Programming Contest -  B. Fire-Fighting Hero（最短路） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**V个消防点，S消防点有一个消防英雄，K表示消防队所在消防点的位置，C是比例系数，消防英雄要和消防队挑战，挑战是：消防英雄到其他消防点的最短路径的最大值与消防队从其消防点的任何一点到其他消防点的最短路径的最大值进行比较。比较的时候消防英雄的最大值要乘以 1/C，时间小的win，如果时间相等，消防英雄win，输出胜者的最大值（如果是消防英雄获胜，输出未乘1/C之前的值）。

**思路：**消防英雄的最大值可以直接跑Dijkstra求，对于消防队可以建立超级源点求，这样使用两次Dijkstra算法可求出两个最短路径的最大值。比较时将消防队乘以C可避免分数操作。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e5 + 7;
#define inf 0x3f3f3f3f
#define pii pair&lt;int, int&gt;
int n, m, s, t;
int d[N], vis[N];
vector&lt;pii&gt;edge[N];
void init()
{
    for(int i = 0; i &lt;= N; i++) edge[i].clear();
    memset(d,0x3f,sizeof(d));
    memset(vis,0,sizeof(vis));
}
void Dijkstra(int s)
{
    d[s] = 0;
    priority_queue&lt;pii&gt; Q;
    Q.push({-d[s],s});
    while(!Q.empty())
    {
        int now = Q.top().second;
        Q.pop(); if(vis[now]) continue;
        vis[now] = 1;
        for(int j = 0; j &lt; edge[now].size(); j++)
        {
            int v = edge[now][j].first;
            if(d[v] &gt; d[now]+edge[now][j].second)
            {
                d[v] = d[now]+edge[now][j].second;
                Q.push({-d[v],v});
            }
        }
    }
}
int V, E, S, K, C;
int main()
{
    int T; scanf("%d", &amp;T);
    while(T--)
    {
        init();
        scanf("%d%d%d%d%d",&amp;V, &amp;E, &amp;S, &amp;K, &amp;C);
        s = 0; int a, b, x;
        for(int i = 0; i &lt; K; i++)
        {
            scanf("%d", &amp;b);
            edge[s].push_back({b, 0});
        }
        while(E--)
        {
            scanf("%d%d%d",&amp;a,&amp;b,&amp;x);
            edge[a].push_back({b,x});
            edge[b].push_back({a,x});
        }
        int ans1 = 0, ans2 = 0;
        Dijkstra(S);
        for(int i = 1; i &lt;= V; i++)
            if(d[i] != inf) ans1 = max(ans1, d[i]);

        memset(d,0x3f,sizeof(d));
        memset(vis,0,sizeof(vis));
        Dijkstra(s);
        for(int i = 1; i &lt;= V; i++)
            if(d[i] != inf) ans2 = max(ans2, d[i]);

        if(ans1 &lt;= ans2 * C) printf("%d\n", ans1);
        else printf("%d\n", ans2);
    }
    return 0;
}

```

  
