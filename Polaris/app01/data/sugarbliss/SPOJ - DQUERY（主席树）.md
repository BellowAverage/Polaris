
--- 
title:  SPOJ - DQUERY（主席树） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**询问区间不同数字的个数。

**思路：**这题莫队，树状数组都可以写，主席树做法：我们需要维护每个数最后一次出现位置，所有最后一次出现位置对整个区间有1的贡献，也就是对每一个数建一棵线段树，如果这个数之前出现过则再建一棵树删除。

```
#include &lt;cstdio&gt;
#include &lt;vector&gt;
#include &lt;cstring&gt;
#include &lt;iostream&gt;
#include &lt;algorithm&gt;
using namespace std;
typedef long long ll ;
const int maxn = 2e5+7;
const int mod = 1e9+7;
int n, m, cnt, root[maxn], a[maxn], pre[maxn], l, r, k, ans;
vector&lt;int&gt; v;
struct node{int l, r, sum;} T[maxn*25];
int getid(int x){return lower_bound(v.begin(),v.end(),x)-v.begin()+1;}

void update(int l,int r,int &amp;now, int pre, int pos, int c)
{
    T[++cnt] = T[pre], T[cnt].sum += c, now = cnt;
    if(l == r) return;
    int mid = (l + r) &gt;&gt; 1;
    if(mid &gt;= pos) update(l, mid, T[now].l, T[pre].l, pos, c);
    else update(mid + 1, r, T[now].r, T[pre].r, pos, c);
}
int query(int l, int r, int rt, int L, int R)
{
    if(L &lt;= l &amp;&amp; r &lt;= R) return T[rt].sum;
    int mid = (l + r) / 2;
    int res = 0;
    if(mid &gt;= L)  res += query(l, mid, T[rt].l, L, R);
    if(mid &lt; R)  res += query(mid+1, r, T[rt].r, L, R);
    return res;
}
int main()
{
    scanf("%d",&amp;n);
    for(int i = 1; i &lt;= n; i++) scanf("%d",&amp;a[i]),v.push_back(a[i]);
    sort(v.begin(),v.end()); v.erase(unique(v.begin(),v.end()),v.end());
    for(int i = 1; i &lt;= n; i++)
    {
        int pos = getid(a[i]);
        update(1, n, root[i], root[i-1], i, 1);
        if(pre[pos]) update(1, n, root[i], root[i], pre[pos], -1);
        pre[pos] = i;
    }
    scanf("%d", &amp;m);
    for(int i = 1; i &lt;= m; i++)
    {
        scanf("%d%d", &amp;l, &amp;r);
        printf("%d\n", query(1, n, root[r], l, r));
    }
    return 0;
}
/*
5
1 1 2 1 3
3
1 5
2 4
3 5
*/

```

 
