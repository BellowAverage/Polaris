
--- 
title:  牛客假日团队赛2 - D - Dining（最大流） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有n头牛，f种草料，d种水，每种草料和每种水仅有一个单位，每头牛要吃一个单位草料和喝一个单位水。每头牛只对一部分草料和一部分水感兴趣。问你最多能完全满足多少头牛（草料和水均满意）？

**思路：**用拆点来限制流量，建立超级源点超级汇点，超级源点与每种食物相连，流量为1。每头牛拆点，流量为1（此处限制流量，一头牛只能转移1的流量）。每头牛拆点，牛左与所有满意的食物相连，流量为1，牛右再与所有满意的水相连，流量为1，每种水再与超级汇点相连，流量为1。最终最大流即为答案。

```
#include &lt;iostream&gt;
#include &lt;cstring&gt;
#include &lt;cstdio&gt;
#include &lt;queue&gt;
const int N = 1e4 + 7, M = 3e5 + 7, inf = 0x3f3f3f3f;
using namespace std;
int n, f, d, s, t, head[N], cnt, deep[N],cur[N];
queue &lt;int&gt; Q;
struct node
{
    int next,to,vi;
} edge[M&lt;&lt;1];

void add(int u,int v,int vi)
{
    edge[cnt] = (node){head[u],v,vi}; head[u] = cnt++;
    edge[cnt] = (node){head[v],u,0};  head[v] = cnt++;
}

bool bfs()
{
    memset(deep,-1,sizeof(deep));
    Q.push(s); deep[s] = 0;
    while(!Q.empty())
    {
        int u =  Q.front(); Q.pop();
        for(int i = head[u]; ~i; i = edge[i].next)
        {
            int v = edge[i].to;
            if(deep[v] == -1 &amp;&amp; edge[i].vi &gt; 0)
                deep[v] = deep[u] + 1, Q.push(v);
        }
    }
    return (deep[t] &gt; 0);
}

int dfs(int now,int t,int lim)
{
    int ret = 0, cost = 0;
    if(now == t) return lim;
    for(int i = cur[now] ; ~i; i = edge[i].next)
    {
        int v = edge[i].to;
        if(deep[v] != deep[now] + 1) continue;
        cost = dfs(v, t, min(lim - ret, edge[i].vi));
        edge[i].vi -= cost, edge[i^1].vi += cost;
        ret += cost;
        if(edge[i].vi) cur[now] = i;
        if(ret == lim) return lim;
    }
    if(!ret) deep[now] = -1;
    return ret;
}

int max_flow(int n)
{
    int ret = 0;
    while(bfs())
    {
        for(int i = 0; i &lt;= n; i++) cur[i] = head[i];
        ret += dfs(s,t,inf);
    }
    return ret;
}

int main()
{
    scanf("%d%d%d",&amp;n,&amp;f,&amp;d);
    cnt = 0; int u, v;
    memset(head, -1, sizeof(head));
    s = 0, t = 500;
    for(int i = 1; i &lt;= f; i++) add(s, i, 1);
    for(int i = 1; i &lt;= d; i++) add(i + 300, t, 1);
    for(int i = 1; i &lt;= n; i++)
    {
        scanf("%d%d",&amp;f,&amp;d);
        while(f--)
        {
            scanf("%d",&amp;v);
            add(v, i + 100, 1);
        }
        add(i + 100, i + 200, 1);
        while(d--)
        {
            scanf("%d",&amp;v);
            add(i + 200, v + 300, 1);
        }

    }
    int ans = max_flow(500);
    printf("%d\n",ans);

    return 0;
}

```

  
