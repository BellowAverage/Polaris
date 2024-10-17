
--- 
title:  HDU - 4666 - Hyperspace（动态多维曼哈顿距离） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**一开始**点的个数为零，有两个操作**就是**0表示增加一个点，1表示删除一个点，**每次操作都要输出最大曼哈顿距离。

**思路：加强版，**不同的是本题需要一个数据结构来维护最大值最小值，比如线段树，mu，或者搞两个堆。

#### multiset：

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
int n, k, x, a[N][10];
multiset &lt;int&gt; tmp[N];
int main()
{
    while(~scanf("%d%d",&amp;n,&amp;k))
    {
        for(int i = 0; i &lt; (1 &lt;&lt; k); i++)
            tmp[i].clear();
        for(int p = 1; p &lt;= n; p++)
        {
            int op; scanf("%d",&amp;op);
            int ans = 0;
            if(op == 0)
            {
                for(int i = 0; i &lt; k; i++)
                    scanf("%d", &amp;a[p][i]);
                for(int i = 0; i &lt; (1 &lt;&lt; k); i++)
                {
                    int t = 0;
                    for(int j = 0; j &lt; k; j++)
                    {
                        if(i &amp; (1 &lt;&lt; j)) t += a[p][j];
                        else t -= a[p][j];
                    }
                    tmp[i].insert(t);
                }
            }
            else
            {
                scanf("%d", &amp;x);
                for(int i = 0; i &lt; (1 &lt;&lt; k); i++)
                {
                    int t = 0;
                    for(int j = 0; j &lt; k; j++)
                    {
                        if(i &amp; (1 &lt;&lt; j)) t += a[x][j];
                        else t -= a[x][j];
                    }
                    tmp[i].erase(tmp[i].find(t));
                }
            }
            for(int i = 0; i &lt; (1 &lt;&lt; k); i++)
                ans = max(ans, *tmp[i].rbegin() - *tmp[i].begin());
            printf("%d\n", ans);
        }

    }
}
```

#### priority_queue ：

```
#include &lt;cstdio&gt;
#include &lt;algorithm&gt;
#include &lt;queue&gt;
#include &lt;cstring&gt;
#include &lt;iostream&gt;
using namespace std;
#define N 60010
#define inf 0x3fffffff
int q, k, a[5];
bool vis[N];
struct node1 {
    int x, id;
    bool operator&lt;(const node1&amp; a) const {
        return x &lt; a.x;
    }
}t1;
struct node2 {
    int x, id;
    bool operator&lt;(const node2&amp; a) const {
        return x &gt; a.x;
    }
}t2;
priority_queue&lt;node1&gt; q1[1&lt;&lt;5];
priority_queue&lt;node2&gt; q2[1&lt;&lt;5];

int main() {
    while (scanf("%d%d", &amp;q, &amp;k) == 2) {
        int t;
        memset(vis, false, sizeof(vis));
        for (int i=0; i&lt;(1&lt;&lt;k); i++) {
            while (!q1[i].empty()) q1[i].pop();
            while (!q2[i].empty()) q2[i].pop();
        }
        int c, ans, mi, mx;
        for (int p=1; p&lt;=q; p++) {
            scanf("%d", &amp;t);
            if (t == 0) {
                for (int i=0; i&lt;k; i++) scanf("%d", &amp;a[i]);
                for (int s=0; s&lt;(1&lt;&lt;k); s++) {
                    c = 0;
                    for (int i=0; i&lt;k; i++)
                        if ((1&lt;&lt;i) &amp; s) c += a[i];
                        else c -= a[i];
                    t1.x = t2.x = c;
                    t1.id = t2.id = p;
                    q1[s].push(t1);
                    q2[s].push(t2);
                }
            } else {
                scanf("%d", &amp;c);
                vis[c] = true;
            }
            ans = 0;
            for (int s=0; s&lt;(1&lt;&lt;k); s++) {
                while (true) {
                    t1 = q1[s].top();
                    if (!vis[t1.id]) break;
                    q1[s].pop();
                }
                while (true) {
                    t2 = q2[s].top();
                    if (!vis[t2.id]) break;
                    q2[s].pop();
                }
                ans = max(ans, t1.x-t2.x);
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}

```

 
