
--- 
title:  HDU - 2767 - Proving Equivalences(强连通，缩点) 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给出n个点和m条有向边，问最少须添加多少个边，使得有向图成为一个强连通图。

**思路：**对于有向图的强连通图中的每一个顶点一定有它的入度和出度都不为0，为了使每一个点的入度和出度都不为0，我们只需要从出度为0的点连出一条边同时把它连入入度为0的点，尽可能多的一一对应，所以添加的边数就是max(入度为0的点数，出度为0的点数)。**注意：如果一个图本身就是强连通图，答案为0。**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
vector &lt;int&gt; E[N], v[N];
stack &lt;int&gt; sta;
int n, m, x, y, op;
int dfn[N], low[N], vis[N], color[N], tot, cnt, res, flag;
int in[N], out[N];
void init()
{
    tot = cnt = 0;
    for(int i = 0; i &lt;= n; i++)
    {
        vis[i] = low[i] = dfn[i] = color[i] = in[i] = out[i] = 0;
        E[i].clear();
    }
        
}
void tarjan(int now)
{
    low[now] = dfn[now] = ++cnt;
    sta.push(now);
    vis[now] = 1;
    for(int i = 0; i &lt; E[now].size(); i++)
    {
        int v = E[now][i];
        if(!dfn[v])
        {
            tarjan(v);
            low[now] = min(low[now], low[v]);
        }
        else if(vis[v])
            low[now] = min(low[now], dfn[v]);
    }
    if(dfn[now] == low[now])
    {
        tot++;
        while(1)
        {
            int tmp = sta.top(); sta.pop();
            vis[tmp]--;
            color[tmp] = tot;
            if(tmp == now) break;
        }
    }
}
int main()
{
    int T; scanf("%d", &amp;T);
    while(T--)
    {
        scanf("%d%d",&amp;n, &amp;m);
        init();
        while(m--)
        {
            scanf("%d%d",&amp;x, &amp;y);
            E[x].push_back(y);
        }
        for(int i = 1; i &lt;= n; i++)
            if(!dfn[i]) tarjan(i);
        for(int i = 1; i &lt;= n; i++)
        {
            for(int j = 0; j &lt; E[i].size(); j++)
            {
                int v = E[i][j];
                if(color[i] != color[v])
                    in[color[v]]++, out[color[i]]++;
            }
        }
        int t1 = 0, t2 = 0;
        for(int i = 1; i &lt;= tot; i++)
        {
            if(!in[i]) t1++;
            if(!out[i]) t2++;
        }
        if(tot == 1) puts("0");
        else printf("%d\n", max(t1, t2));
    }
}

```

 
