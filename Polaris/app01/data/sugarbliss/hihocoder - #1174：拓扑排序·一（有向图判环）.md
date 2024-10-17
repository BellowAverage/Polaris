
--- 
title:  hihocoder - #1174：拓扑排序·一（有向图判环） 
tags: []
categories: [] 

---
**题目链接：**

**思路**：拓扑排序过程中统计入度为0的点的个数是否为n即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
const int mod = 142857;
int n, m, cnt, x, in[N];
vector &lt;int&gt; E[N];
queue &lt;int&gt; q;
void init()
{
    for(int i = 1; i &lt;= n; i++)
        in[i] = 0, E[i].clear();
    cnt = 0;
}
bool topsort()
{
    for(int i = 1; i &lt;= n; i++)
        if(!in[i]) q.push(i);
    while(!q.empty())
    {
        int now = q.front();
        q.pop(); cnt++;
        for(int i = 0; i &lt; E[now].size(); i++)
        {
            int v = E[now][i];
            if(--in[v] == 0) q.push(v);
        }
    }
    return cnt == n;
}
int main()
{
    int T; scanf("%d",&amp;T);
    while(T--)
    {
        scanf("%d%d",&amp;n,&amp;m);
        init();
        while(m--)
        {
            int s, e;
            scanf("%d%d",&amp;s, &amp;e);
            E[s].push_back(e);
            in[e]++;
        }
        if(topsort()) puts("Correct");
        else puts("Wrong");
    }
}

```

 
