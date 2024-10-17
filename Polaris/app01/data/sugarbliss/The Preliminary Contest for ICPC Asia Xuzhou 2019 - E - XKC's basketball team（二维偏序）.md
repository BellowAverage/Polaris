
--- 
title:  The Preliminary Contest for ICPC Asia Xuzhou 2019 - E - XKC's basketball team（二维偏序） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给出一个长度为n的数列，给出m的值。对于每一个 arr[i] 问在数列中从 i 位置向右比 arr[i] + m 大的值的位置与 i 之间最多有多少个数。

**思路：**用线段树来记录区间最大值，优先从右子树开始查询是否存在大于 arr[i] + m的值，找到返回下标即该值在原数列中的位置，找不到返回-1。

```
#include &lt;iostream&gt;
#include &lt;stdio.h&gt;
using namespace std;
#define ll long long
#define lson l,m,rt&lt;&lt;1
#define rson m+1,r,rt&lt;&lt;1|1
#define mid (l+r)&gt;&gt;1
#define abb int l,int r,int rt
const int N = 5e5 + 7;
int sum[N&lt;&lt;2], ans[N], a[N], n, m;

inline void build(abb)
{
    if(l == r)
    {
        sum[rt] = a[l];
        return ;
    }
    int m = mid;
    build(lson); build(rson);
    sum[rt] = max(sum[rt&lt;&lt;1], sum[rt&lt;&lt;1|1]);
}

inline int query(int p, int tmp, abb)
{
    if(l == r) return l;
    int m = mid;
    if(sum[p&lt;&lt;1|1] &gt;= tmp)  query(p&lt;&lt;1|1, tmp, rson);
    else if(sum[p&lt;&lt;1] &gt;= tmp)  query(p&lt;&lt;1, tmp, lson);
    else return -1;
}
int main()
{
    scanf("%d%d", &amp;n, &amp;m);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d", &amp;a[i]);
    build(1, n, 1);
    for(int i = 1; i &lt;= n; i++)
    {
        int pos = query(1, a[i] + m, 1, n, 1);
        if(pos == -1 || pos &lt;= i) ans[i] = -1;
        else ans[i] = pos - i - 1;
    }
    for(int i = 1; i &lt;= n; i++)
        printf("%d%c", ans[i], i == n ? '\n' : ' ');
    return 0;
}

```

 
