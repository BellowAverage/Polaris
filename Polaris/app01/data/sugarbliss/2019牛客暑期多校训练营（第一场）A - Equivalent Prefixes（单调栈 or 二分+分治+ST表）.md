
--- 
title:  2019牛客暑期多校训练营（第一场）A - Equivalent Prefixes（单调栈 or 二分+分治+ST表） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**两个长度为n的数组，求最大的m，使得1到m之内的所有区间的最小值的位置相同。

**思路1：**构造两个单调递减栈，当栈内元素个数不同时显然不符合题意break即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
int a[N], b[N], n;
int main()
{
    while(~scanf("%d",&amp;n))
    {
        for(int i = 0; i &lt; n; i++)
            scanf("%d",&amp;a[i]);
        for(int i = 0; i &lt; n; i++)
            scanf("%d",&amp;b[i]);
        stack &lt;int&gt; s1, s2;
        int ans;
        for(int i = 0; i &lt; n; i++)
        {
            while(!s1.empty() &amp;&amp; a[i] &lt; s1.top()) s1.pop();
            s1.push(a[i]);
            while(!s2.empty() &amp;&amp; b[i] &lt; s2.top()) s2.pop();
            s2.push(b[i]);
            if(s1.size() != s2.size()) break;
            ans = i + 1;
        }
        printf("%d\n",ans);
    }
 
}
```

**思路2：**用ST表预处理区间的最小值，然后二分答案，分治判断check函数即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int maxn = 1e5+5;
int n, q, x, y, Mib, Mia, a[maxn][21], b[maxn][21];
map &lt;int, int&gt;ma, mb;
void ST()
{
    for(int j = 1; (1&lt;&lt;j) &lt;= n; j++)
    {
        for(int i = 1; (i+(1&lt;&lt;j)-1) &lt;= n; i++)
        {
            a[i][j] = min(a[i][j-1], a[i+(1&lt;&lt;(j-1))][j-1]);
            b[i][j] = min(b[i][j-1], b[i+(1&lt;&lt;(j-1))][j-1]);
        }
    }
}
void RMQ(int l, int r)
{
    int k = (int)(log(r-l+1)/log(2.0));
    Mia = ma[min(a[l][k],a[r-(1&lt;&lt;k)+1][k])];
    Mib = mb[min(b[l][k],b[r-(1&lt;&lt;k)+1][k])];
}
bool check(int l, int r)
{
    if(l &gt;= r) return true;
    RMQ(l, r);
    if(Mia == Mib)
        return check(l, Mia-1) &amp;&amp; check(Mia+1, r);
    return false;
}
int main()
{
    while(~scanf("%d",&amp;n))
    {
        for(int i = 1; i &lt;= n; i++)
            scanf("%d", &amp;a[i][0]), ma[a[i][0]] = i;
        for(int i = 1; i &lt;= n; i++)
            scanf("%d", &amp;b[i][0]), mb[b[i][0]] = i;
        ST(); int ans, flag = 0;
        int l = 1, r = n, mid;
        while(l &lt;= r)
        {
            mid = (l + r) &gt;&gt; 1;
            if(check(1, mid))
            {
                ans = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        printf("%d\n",ans);
    }

}

```

 
