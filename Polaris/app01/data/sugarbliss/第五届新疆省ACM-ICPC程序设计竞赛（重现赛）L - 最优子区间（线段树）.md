
--- 
title:  第五届新疆省ACM-ICPC程序设计竞赛（重现赛）L - 最优子区间（线段树） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**由于要求的是区间中数字恰好出现一次的个数作为得分，所以我们预处理出每一个数字从右向左第一次出现的位置<img alt="pre[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?pre%5Bi%5D">，若当前数字第一次出现则<img alt="pre[i]=0" class="mathcode" src="https://private.codecogs.com/gif.latex?pre%5Bi%5D%3D0">，对于每一个数字 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> ，定义<img alt="f[j,i]" class="mathcode" src="https://private.codecogs.com/gif.latex?f%5Bj%2Ci%5D">  <img alt="(1&lt;=j&lt;=i )" class="mathcode" src="https://private.codecogs.com/gif.latex?%281%3C%3Dj%3C%3Di%20%29">表示当前区间 <img alt="[j,i]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Bj%2Ci%5D"> 的得分，用线段树维护<img alt="f[j,i]" class="mathcode" src="https://private.codecogs.com/gif.latex?f%5Bj%2Ci%5D">，对于当前数字 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> ，要在区间<img alt="[pre[i]+1,i]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Bpre%5Bi%5D&amp;plus;1%2Ci%5D">加一（也就是当前数字 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 对区间<img alt="[pre[i]+1,i]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Bpre%5Bi%5D&amp;plus;1%2Ci%5D">的贡献加一），如果 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 之前出现过，则区间<img alt="[pre[pre[i]]+1,pre[i]]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Bpre%5Bpre%5Bi%5D%5D&amp;plus;1%2Cpre%5Bi%5D%5D">要减一，线段树提供区间修改，和最值查询。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
int pre[N], a[N], vis[N], lazy[N &lt;&lt; 2], tree[N &lt;&lt; 2];
void pushup(int rt)
{
    tree[rt] = max(tree[rt&lt;&lt;1], tree[rt&lt;&lt;1|1]);
}
void pushdown(int l, int r, int rt)
{
    if(tree[rt])
    {
        lazy[rt&lt;&lt;1] += lazy[rt];
        lazy[rt&lt;&lt;1|1] += lazy[rt];
        tree[rt&lt;&lt;1] += lazy[rt];
        tree[rt&lt;&lt;1|1] += lazy[rt];
        lazy[rt] = 0;
    }
}
void update(int L, int R, int val, int l, int r, int rt)
{
    if(l &gt;= L &amp;&amp; r &lt;= R)
    {
        tree[rt] += val;
        lazy[rt] += val;
        return ;
    }
    pushdown(l, r, rt);
    int m = (l + r) &gt;&gt; 1;
    if(m &gt;= L) update(L, R, val, l, m, rt &lt;&lt; 1);
    if(m &lt; R) update(L, R, val, m + 1, r, rt &lt;&lt; 1 | 1);
    pushup(rt);
}
int main()
{
    int n; scanf("%d",&amp;n);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d",&amp;a[i]);
    for(int i = 1; i &lt;= n; i++)
    {
        if(vis[a[i]]) pre[i] = vis[a[i]];
        vis[a[i]] = i;
    }
    int ans = 0;
    for(int i = 1; i &lt;= n; i++)
    {
        update(pre[i] + 1, i, 1, 1, n, 1);
        if(pre[i]) update(pre[pre[i]] + 1, pre[i], -1, 1, n, 1);
        ans = max(ans, tree[1]);
    }
    cout &lt;&lt; ans &lt;&lt; endl;
}

```

 
