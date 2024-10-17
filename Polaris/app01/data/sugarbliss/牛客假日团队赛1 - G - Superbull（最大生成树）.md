
--- 
title:  牛客假日团队赛1 - G - Superbull（最大生成树） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有<img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">头牛比赛，每场比赛都选任意两头牛，每场比赛会影响总得分，总得分会加上选手 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 的 <img alt="id" class="mathcode" src="https://private.codecogs.com/gif.latex?id"> 和选手 <img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y"> 的 <img alt="id" class="mathcode" src="https://private.codecogs.com/gif.latex?id"> 按位异或的值，每局比赛你都要钦定一头牛输掉，输掉的牛不能继续比赛，求总得分的最大值。

**思路：**在任意两头牛之间连一条路径，权值就是<img alt="a[i]\oplus a[j]" class="mathcode" src="https://private.codecogs.com/gif.latex?a%5Bi%5D%5Coplus%20a%5Bj%5D">，然后跑一遍最大生成树就行。因为通过题目很容易知道有<img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">个点<img alt="n-1" class="mathcode" src="https://private.codecogs.com/gif.latex?n-1">条边，考虑树，最后的答案，两点间只有一条路径，而且题目中给定的是一个图，再考虑生成树。答案要求最大值，因此就是最大生成树。记得开<img alt="long long" class="mathcode" src="https://private.codecogs.com/gif.latex?long%20long">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e6 + 7;
struct node {int s, e; ll w; } edge[N&lt;&lt;2];
bool cmp(node a, node b) {return a.w &gt; b.w; }
ll f[N], a[N];
int n, tot;
void init()
{
    for(int i = 0; i &lt;= n; i++) f[i] = i;
    tot = 0;
}
void add(int u, int v, ll w)
{
    edge[tot].s = u;
    edge[tot].e = v;
    edge[tot++].w = w;
}
int Find(int x)
{
    if(x != f[x]) return f[x] = Find(f[x]);
    return x;
}
void unint(int a, int b)
{
    int r1 = Find(a);
    int r2 = Find(b);
    if(r1 != r2) f[r1] = r2;
}
ll Kruskal()
{
    ll ans = 0;
    sort(edge, edge + tot, cmp);
    for(int i = 0; i &lt; tot; i++)
    {
        int x = Find(edge[i].s);
        int y = Find(edge[i].e);
        if(x != y)
            ans += edge[i].w, f[x] = y;
    }
    return ans;
}
int main()
{
    scanf("%d",&amp;n); init();
    for(int i = 1; i &lt;= n; i++) scanf("%lld",&amp;a[i]);
    for(int i = 1; i &lt;= n; i++)
        for(int j = i + 1; j &lt;= n; j++)
            add(i, j, a[i]^a[j]);
    ll sum = Kruskal();
    printf("%lld\n",sum);
}

```

 
