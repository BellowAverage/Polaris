
--- 
title:  Codeforces Round #576 (Div. 2) - D. Welfare State（思维 or 线段树） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一个序列，有两个操作：
1. 将p位置改为x。1. 将小于x的值改为x。
**思路： **先说思维，我们想一下如果只有操作2，那么是不是只有操作2中**最大的x起作用，**那么引入操作1，那么就是**操作1之后的最大x有关系**，所以我们维护操作1修改的位置，维护一个后缀mx（因为后面影响前面），如果没有操作1，那直接和mx[1]取最大值即可，如果有操作1就和pos[p]的下一个位置取最大即可。

```
#include&lt;bits/stdc++.h&gt;
using namespace std;
const int N = 2e5 + 7;
int a[N], pos[N], mx[N], n;
int main()
{
    scanf("%d",&amp;n);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d",&amp;a[i]);
    int q; scanf("%d",&amp;q);
    for(int i = 1; i &lt;= q; i++)
    {
        int op, x, y;
        scanf("%d", &amp;op);
        if(op == 1)
        {
            scanf("%d%d",&amp;x, &amp;y);
            a[x] = y;
            pos[x] = i;
        }
        else scanf("%d", &amp;mx[i]);
    }
    for(int i = q; i &gt;= 1; i--)
        mx[i] = max(mx[i+1], mx[i]);
    for(int i = 1; i &lt;= n; i++)
        printf("%d%c",max(a[i], mx[pos[i] + 1]), i == n ? '\n' : ' ');
	return 0;
}
```

**线段树思路：**当看到单点修改和区间修改时，第一反应就是线段树，主要是操作2该怎么维护，由上面的分析我们知道操作1会把操作2分成两部分，当进行操作2时，我们就维护根节点lazy[1]的最大值，当我们进行操作1时将标记下传，当传到最后一个父节点时，我们就维护两个叶子节点的值（清空标记），再进行操作2时会维护新的lazy[1]（原来的已经下传），查询时输出<img alt="max(a[rt], lazy[1])" class="mathcode" src="https://private.codecogs.com/gif.latex?max%28a%5Brt%5D%2C%20lazy%5B1%5D%29">即可。

```
#include &lt;iostream&gt;
#include &lt;stdio.h&gt;
using namespace std;
#define ll long long
#define lson l,m,rt&lt;&lt;1
#define rson m+1,r,rt&lt;&lt;1|1
#define mid (l+r)&gt;&gt;1
#define abb int l,int r,int rt
const int N = 2e5 + 7;
int lazy[N&lt;&lt;2], a[N&lt;&lt;2];
inline void pushdown(abb)
{
    if(lazy[rt])
    {
        lazy[rt&lt;&lt;1] = max(lazy[rt&lt;&lt;1], lazy[rt]);
        lazy[rt&lt;&lt;1|1] = max(lazy[rt&lt;&lt;1|1], lazy[rt]);
        int m = mid;
        if(l == m) a[rt&lt;&lt;1] = max(a[rt&lt;&lt;1], lazy[rt]);
        if(m + 1 == r) a[rt&lt;&lt;1|1] = max(a[rt&lt;&lt;1|1], lazy[rt]);
        lazy[rt] = 0;
    }
}

inline void build(abb)
{
    lazy[rt] = 0;
    if(l == r)
    {
        scanf("%d", &amp;a[rt]);
        return ;
    }
    int m = mid;
    build(lson); build(rson);
}
inline void update(int p, int c, abb)
{
    lazy[p] = max(lazy[p], c);
}
inline void update_point(int p, int c, abb)
{
    if(l == r)
    {
        a[rt] = c;
        return ;
    }
    pushdown(l, r, rt);
    int m = mid;
    if(p &lt;= m) update_point(p, c, lson);
    else update_point(p, c, rson);
}
inline int query_point(int p, abb)
{
    if(l == r)
        return max(a[rt], lazy[1]);
    pushdown(l, r, rt);
    int m = mid;
    if(p &lt;= m)  query_point(p, lson);
    else  query_point(p, rson);
}
int main()
{
    int m, n; scanf("%d",&amp;n);
    build(1, n, 1);
    scanf("%d",&amp;m);
    while(m--)
    {
        int c, p, op;
        scanf("%d",&amp;op);
        if(op == 1)
        {
            scanf("%d%d", &amp;p, &amp;c);
            update_point(p, c, 1, n, 1);
        }
        if(op == 2)
        {
            scanf("%d", &amp;c);
            update(1, c, 1, n, 1);
        }
    }
    for(int i = 1; i &lt;= n; i++)
        printf("%d%c",query_point(i, 1, n, 1), i == n ? '\n' : ' ');
    return 0;
}

```

 
