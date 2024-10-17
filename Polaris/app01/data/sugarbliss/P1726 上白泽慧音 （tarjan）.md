
--- 
title:  P1726 上白泽慧音 （tarjan） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**求最大强联通分量，若存在两个最大的，输出字典序最小的。

**思路：**裸的Tarjan算法，讲之前需要介绍一些辅助数组：
1. dfn[ ]：表示这个点的时间戳，也就是第几个搜到的1. low[ ]：表示这个点能到达的最小时间戳，或者说是这个点以及其子孙节点连的所有点中dfn[ ]最小的。1. stack：表示当前所有可能构成强连通分量的点1. vis[ ]：表示一个点是否在stack中。
**首先从1节点进行深度优先搜索，过程中用栈维护可能构成强连通分量的点。**

**当遇到一个点时，有如下判断：**
- 如果这个点没有访问过，就将这个点加入栈。- 如果这个点访问过，且在栈里，与这个点的low或dfn比较，更新自己的low。
**回溯时更新low。**

**当一个点遍历所有的边后这个点的low还是等于dfn，将这个点及以上出栈，这个点及栈以上的点构成一个强连通分量。**

**这个图不一定是一个连通图，所以跑Tarjan时要枚举每个点，若dfn[ ] == 0，则继续进行Tarjan。**

**由于本题要输出最大强连通分量的最小字典序，我们可以用染色法将一个联通分量的点染成一个颜色，输出时直接从小到大输出即可。**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
vector &lt;int&gt; E[N], v[N];
stack &lt;int&gt; sta;
int n, m, x, y, op;
int dfn[N], low[N], vis[N], color[N], col, cnt, res, flag;
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
        col++;
        int t = 0;
        while(1)
        {
            int tmp = sta.top(); sta.pop();
            vis[tmp]--; t++;
            color[tmp] = col;
            if(tmp == now) break;
        }
        if(t &gt; res)
        {
            res = t;
            flag = col;
        }
    }
}
int main()
{
    scanf("%d%d",&amp;n, &amp;m);
    while(m--)
    {
        scanf("%d%d%d",&amp;x, &amp;y, &amp;op);
        E[x].push_back(y);
        if(op == 2)
        E[y].push_back(x);
    }
    for(int i = 1; i &lt;= n; i++)
        if(!dfn[i]) tarjan(i);
    printf("%d\n", res);
    for(int i = 1; i &lt;= n; i++)
    {
        if(color[i] == flag)
            printf("%d ", i);
    }
}
/*
5 5
1 2 1
1 3 2
2 4 2
5 1 2
3 5 1
*/


```

** **
