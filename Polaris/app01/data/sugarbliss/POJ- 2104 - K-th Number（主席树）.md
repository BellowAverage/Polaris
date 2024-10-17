
--- 
title:  POJ- 2104 - K-th Number（主席树） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**静态区间第k小，主席树模板题。

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
int n, m, cnt, root[maxn], a[maxn], l, r, k;
vector&lt;int&gt; v;
struct node{int l, r, sum;} T[maxn*25];
int getid(int x){return lower_bound(v.begin(),v.end(),x)-v.begin()+1;}

void update(int l,int r,int &amp;now, int pre, int pos)
{
    T[++cnt] = T[pre], T[cnt].sum++, now = cnt;
    if(l == r) return;
    int mid = (l + r) / 2;
    if(mid&gt;=pos) update(l, mid, T[now].l, T[pre].l, pos);
    else update(mid+1, r, T[now].r, T[pre].r, pos);
}
int query(int l, int r, int L, int R, int k)
{
    if(l == r) return l;
    int mid = (l + r) / 2;
    int sum = T[T[R].l].sum - T[T[L].l].sum;
    if(sum &gt;= k) return query(l, mid, T[L].l, T[R].l, k);
    else return query(mid+1, r, T[L].r, T[R].r, k - sum);
}
int main(void)
{
    scanf("%d%d",&amp;n,&amp;m);
    for(int i = 1; i &lt;= n; i++) scanf("%d",&amp;a[i]),v.push_back(a[i]);
    sort(v.begin(),v.end()); v.erase(unique(v.begin(),v.end()),v.end());

    for(int i = 1; i &lt;= n; i++) update(1,n,root[i],root[i-1],getid(a[i]));
    for(int i = 1; i &lt;= m; i++)
    {
        scanf("%d%d%d", &amp;l, &amp;r, &amp;k);
        printf("%d\n",v[query(1,n,root[l-1],root[r],k)-1]);
    }
    return 0;
}
```

 
