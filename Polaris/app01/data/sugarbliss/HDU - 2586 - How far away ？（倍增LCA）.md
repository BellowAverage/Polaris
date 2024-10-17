
--- 
title:  HDU - 2586 - How far away ？（倍增LCA） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一颗无根树，让你求树上<img alt="u,v" class="mathcode" src="https://private.codecogs.com/gif.latex?u%2Cv">两点的距离。

**思路：**以任意一点 <img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s"> 为根节点建一颗树，然后求询问两点<img alt="u,v" class="mathcode" src="https://private.codecogs.com/gif.latex?u%2Cv">的<img alt="LCA(u,v)=rt" class="mathcode" src="https://private.codecogs.com/gif.latex?LCA%28u%2Cv%29%3Drt">，然后用<img alt="dis[x]" class="mathcode" src="https://private.codecogs.com/gif.latex?dis%5Bx%5D">表示根节点 <img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s"> 到点 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 的距离那么答案就是，<img alt="ans = dis[x]-dis[rt]+dis[y]-dis[rt]" class="mathcode" src="https://private.codecogs.com/gif.latex?ans%20%3D%20dis%5Bx%5D-dis%5Brt%5D&amp;plus;dis%5By%5D-dis%5Brt%5D">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 4e4 + 7;
int n, m, lg[N], deep[N], fa[N][20], dis[N];
#define pii pair &lt;int, int&gt;
vector &lt;pii&gt; E[N];
void dfs(int x, int fath)
{
    fa[x][0] = fath;
    deep[x] = deep[fath] + 1;
    for(int i = 1; (1 &lt;&lt; i) &lt;= n; i++)
        fa[x][i] = fa[fa[x][i-1]][i-1];
    for(int i = 0; i &lt; E[x].size(); i++)
    {
        int v = E[x][i].first;
        if(v != fath)
        {
            dis[v] = dis[x] + E[x][i].second;
            dfs(v, x);
        }
    }
}
int lca(int x, int y)
{
    if(deep[y] &gt; deep[x])
        swap(x, y);
    while(deep[x] &gt; deep[y])
        x = fa[x][lg[deep[x]-deep[y]]];
    if(x == y) return x;
    for(int i = lg[deep[x]]; i &gt;= 0; i--)
        if(fa[x][i] != fa[y][i])
            x = fa[x][i], y = fa[y][i];
    return fa[x][0];
}
int main()
{
    int T; scanf("%d",&amp;T);
    while(T--)
    {
        scanf("%d%d",&amp;n, &amp;m);
        for(int i = 1; i &lt; n; i++)
        {
            int u, v, w;
            scanf("%d%d%d",&amp;u, &amp;v, &amp;w);
            E[u].push_back({v, w});
            E[v].push_back({u, w});
        }
        lg[0] = -1;
        for(int i = 1; i &lt;= n; i++)
            lg[i] = lg[i &gt;&gt; 1] + 1;
        dfs(1, 0);
        while(m--)
        {
            int x, y, ans;
            scanf("%d%d",&amp;x, &amp;y);
            ans = dis[x] + dis[y] - 2 * dis[lca(x, y)];
            printf("%d\n",ans);
        }
    }
}

```

 
