
--- 
title:  HDU - 5249 - KPI（权值线段树） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有三种操作：
1. in x 表示加入数 x。1. out 表示 弹出最早元素。 1. query 表示查询当前的序列中位数 即 第 floor(m/2)+1 的数字。 
** 思路：**用队列找最早的元素，权值线段树查询即可，本题需要离散化。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
#define lefs l,m,rt&lt;&lt;1
#define rigs m+1,r,rt&lt;&lt;1|1
#define lef rt &lt;&lt; 1
#define rig rt &lt;&lt; 1 | 1
#define mid (l+r)&gt;&gt;1
#define abb int l,int r,int rt
const int N = 1e4 + 7;
int sum[N&lt;&lt;2], a[N], n, p;
char str[10];
queue &lt;int&gt; q;
vector &lt;int&gt; v;
inline init()
{
    memset(sum, 0, sizeof sum);
    memset(a, 0, sizeof a);
    v.clear();
    while(!q.empty()) q.pop();
}
inline int getid(int x){return lower_bound(v.begin(), v.end(), x)-v.begin()+1;}
inline void pushup(int rt)
{
    sum[rt] = sum[rt&lt;&lt;1] + sum[rt&lt;&lt;1|1];
}
inline void update(int p, int c, abb)
{
    if(l == r)
    {
        sum[rt] += c;
        return ;
    }
    int m = mid;
    if(p &lt;= m) update(p, c, lefs);
    else update(p, c, rigs);
    pushup(rt);
}
inline int query(int L, int R, abb)
{
    if(L &lt;= l &amp;&amp; r &lt;= R)
        return sum[rt];
    int m = mid, res = 0;
    if(m &gt;= L)  res += query(L, R, lefs);
    if(m &lt; R)  res += query(L, R, rigs);
    return res;
}
inline int query_kth(int k, abb)
{
    if(l == r) return l;
    int m = mid;
    if(k &lt;= sum[lef]) return query_kth(k, lefs);
    else return query_kth(k - sum[lef], rigs);
}
int main()
{
    int cas = 1;
    while(~scanf("%d", &amp;n))
    {
        init();
        printf("Case #%d:\n", cas++);
        for(int i = 1; i &lt;= n; i++)
        {
            scanf("%s", str);
            if(str[0] == 'i') scanf("%d", &amp;a[i]), v.push_back(a[i]);
            else if(str[0] == 'o') a[i] = -1;
            else a[i] = -2;
        }
        sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()), v.end());
        int cnt = v.size();
        for(int i = 1; i &lt;= n; i++)
        {
            if(a[i] &gt;= 0)
            {
                p = getid(a[i]); q.push(p);
                update(p, 1, 1, cnt, 1);
            }
            else if(a[i] == -1)
            {
                p = q.front(); q.pop();
                update(p, -1, 1, cnt, 1);
            }
            else printf("%d\n",v.at(query_kth(q.size()/2+1, 1, cnt, 1)-1));
        }
    }

    return 0;
}

```

 
