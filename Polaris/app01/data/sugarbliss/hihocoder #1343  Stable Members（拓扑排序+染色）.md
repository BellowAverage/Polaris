
--- 
title:  hihocoder #1343 : Stable Members（拓扑排序+染色） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给一个有向无环图,定义一个点为unstable当且仅当删掉一个点（不能为它自己或点0）时，它不能与点0连通；其他点则为stable，求图中有几个stable点。

**思路：**对于每个顶点v，采用染色的方法：即对于某个顶点v，采用拓扑排序的方法遍历其儿子节点，如果当前儿子节点所有的父顶点都已经被染成顶点v的颜色，则将当前儿子节点染色成与v相同的颜色，并标记为unstable，然后入队。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
int n, k, x, color[N], unstable[N];
vector &lt;int&gt; son[N], father[N];
bool judge(int k, int col)
{
    for(int i = 0; i &lt; father[k].size(); i++)
        if(color[father[k][i]] != col)
            return false;
    return true;
}
void topsort(int k)
{
    if(color[k] != 0) return ;
    color[k] = k;
    queue &lt;int&gt; q;
    q.push(k);
    while(!q.empty())
    {
        int now = q.front();
        q.pop();
        for(int i = 0; i &lt; son[now].size(); i++)
        {
            if(judge(son[now][i], color[now]) &amp;&amp; !unstable[son[now][i]])
            {
                color[son[now][i]] = color[now];
                unstable[son[now][i]] = 1;
                q.push(son[now][i]);
            }
        }
    }
}
int main()
{
    scanf("%d",&amp;n);
    for(int i = 1; i &lt;= n; i++)
    {
        scanf("%d",&amp;k);
        while(k--)
        {
            scanf("%d",&amp;x);
            son[x].push_back(i);
            father[i].push_back(x);
        }
    }
    int ans = n;
    for(int i = 1; i &lt;= n; i++) topsort(i);
    for(int i = 1; i &lt;= n; i++)
        ans -= unstable[i];
    cout &lt;&lt; ans &lt;&lt; endl;
}

```

 
