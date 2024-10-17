
--- 
title:  HDU - 3078 - Network （倍增LCA） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给定一棵树，树上每个点都有权值，输入三个数<img alt="k,a,b" class="mathcode" src="https://private.codecogs.com/gif.latex?k%2Ca%2Cb">有两种操作: k a b，k == 0时把a点的权值改为b，k &gt; 0时求a到b路径上第k大的权值
- <img alt="k==0" class="mathcode" src="https://private.codecogs.com/gif.latex?k%3D%3D0">，将 <img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点的权值改为 <img alt="" class="mathcode" src="https://private.codecogs.com/gif.latex?"><img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b">。- <img alt="k &gt; 0" class="mathcode" src="https://private.codecogs.com/gif.latex?k%20%3E%200">，求 <img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点到 <img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b"> 点路径上的第 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 大权值。
** 思路：**<img alt="k==0" class="mathcode" src="https://private.codecogs.com/gif.latex?k%3D%3D0">时直接修改就行了，<img alt="k &gt; 0" class="mathcode" src="https://private.codecogs.com/gif.latex?k%20%3E%200">时，考虑到<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点到 <img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b"> 点路径上的第 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 大权值，我们可以把<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点到 <img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b"> 点路径上的权值全部存起来，然后排序取第 <img alt="k" class="mathcode" src="https://private.codecogs.com/gif.latex?k"> 个即可，不好直接求<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点到 <img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b"> 点路径上的权值，我们可以求出<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点 和 <img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b"> 点的最近公共祖先 <img alt="rt" class="mathcode" src="https://private.codecogs.com/gif.latex?rt"> ，然后分别求<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a"> 点到 <img alt="rt" class="mathcode" src="https://private.codecogs.com/gif.latex?rt"> 点和<img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b"> 点到 <img alt="rt" class="mathcode" src="https://private.codecogs.com/gif.latex?rt"> 点路径上的权值。看似暴力实则可行。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 8e4 + 7;
int n, m, lg[N], deep[N], fa[N][20];
int a[N], b[N], cnt;
#define pii pair &lt;int, int&gt;
vector &lt;int&gt; E[N];
bool cmp(int a, int b) {return a &gt; b;}
void dfs(int x, int fath)
{
    fa[x][0] = fath;
    deep[x] = deep[fath] + 1;
    for(int i = 1; (1 &lt;&lt; i) &lt;= n; i++)
        fa[x][i] = fa[fa[x][i-1]][i-1];
    for(int i = 0; i &lt; E[x].size(); i++)
    {
        if(E[x][i] != fath)
            dfs(E[x][i], x);
    }
}
int lca(int x, int y)
{
    if(deep[y] &gt; deep[x]) swap(x, y);
    while(deep[x] &gt; deep[y])
        x = fa[x][lg[deep[x]-deep[y]]];
    if(x == y) return x;
    for(int i = lg[deep[x]]; i &gt;= 0; i--)
        if(fa[x][i] != fa[y][i])
            x = fa[x][i], y = fa[y][i];
    return fa[x][0];
}
void solve(int s, int e)
{
    while(s != e)
    {
        b[cnt++] = a[s];
        s = fa[s][0];
    }
}
int main()
{
    scanf("%d%d",&amp;n, &amp;m);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d",&amp;a[i]);
    for(int i = 1; i &lt; n; i++)
    {
        int u, v;
        scanf("%d%d",&amp;u, &amp;v);
        E[u].push_back(v);
        E[v].push_back(u);
    }
    lg[0] = -1;
    for(int i = 1; i &lt;= n; i++)
        lg[i] = lg[i &gt;&gt; 1] + 1;
    dfs(1, 0);
    while(m--)
    {
        int x, y, ans, k;
        scanf("%d%d%d",&amp;k, &amp;x, &amp;y);
        if(k == 0) a[x] = y;
        else
        {
            int rt = lca(x, y); cnt = 0;
            solve(x, rt); solve(y, rt);
            b[cnt++] = a[rt];
            sort(b, b + cnt, cmp);
            if(k &gt; cnt) puts("invalid request!");
            else printf("%d\n",b[k-1]);
        }
    }
}

```
