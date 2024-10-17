
--- 
title:  牛客假日团队赛1 - J - (dfs染色） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**对于传出每一个球最后一定在两头奶牛之间来回传递，先从第一头奶牛向右传递，将接过球的奶牛标记一种颜色，如果出现来回传递的情况就<img alt="return" class="mathcode" src="https://private.codecogs.com/gif.latex?return">，然后从没有被染色的奶牛再次传递，并染新的颜色，由于颜色会覆盖，所以最后颜色的种类数就是答案。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e3 + 7;
int n, a[N], vis[N], b[N], color = 1;
void dfs(int pos)
{
    if(vis[pos] == color) return ;
    vis[pos] = color;
    if(pos == 1) dfs(2);
    if(pos == n) dfs(n-1);
    if(a[pos] - a[pos-1] &lt;= a[pos+1] - a[pos]) dfs(pos-1);
    else dfs(pos+1);
}
int main()
{
    scanf("%d",&amp;n);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d",&amp;a[i]);
    sort(a + 1, a + 1 + n);
    for(int i = 1; i &lt;= n; i++)
    {
        if(!vis[i]) dfs(i);
        color++;
    }
    int cnt = 0;
    for(int i = 1; i &lt;= n; i++) b[vis[i]] = 1;
    for(int i = 1; i &lt;= n; i++) if(b[i]) cnt++;
    cout &lt;&lt; cnt &lt;&lt; endl;
}

```

 
