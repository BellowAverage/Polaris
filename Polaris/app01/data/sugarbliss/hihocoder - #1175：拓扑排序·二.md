
--- 
title:  hihocoder - #1175：拓扑排序·二 
tags: []
categories: [] 

---
**题目链接：**

**思路：**拓扑排序过程中，统计病毒数量即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
const int mod = 142857;
int n, m, k, x, a[N], in[N];
vector &lt;int&gt; E[N];
queue &lt;int&gt; q;
void topsort()
{
    for(int i = 1; i &lt;= n; i++)
        if(!in[i]) q.push(i);
    while(!q.empty())
    {
        int now = q.front();
        q.pop();
        for(int i = 0; i &lt; E[now].size(); i++)
        {
            int v = E[now][i];
            if(--in[v] == 0) q.push(v);
            a[v] = (a[v] + a[now]) % mod;
        }
    }
}
int main()
{
    scanf("%d%d%d",&amp;n,&amp;m,&amp;k);
    while(k--)
    {
        scanf("%d",&amp;x);
        a[x]++;
    }
    while(m--)
    {
        int s, e;
        scanf("%d%d",&amp;s, &amp;e);
        E[s].push_back(e);
        in[e]++;
    }
    topsort(); int ans = 0;
    for(int i = 1; i &lt;= n; i++)
        ans = (ans + a[i]) % mod;
    cout &lt;&lt; ans &lt;&lt; endl;
}

```

 
