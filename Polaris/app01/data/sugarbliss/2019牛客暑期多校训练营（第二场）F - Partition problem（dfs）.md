
--- 
title:  2019牛客暑期多校训练营（第二场）F - Partition problem（dfs） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一个N，现在有2*N个人，你要做的就是把这2*N个人分成两队一队N个人，下表就是每个人对其他人的作用，让你求两个队伍作用的最大值，队伍作用的最大值是每个人对另一支队伍的作用的和。

**思路：**先把所有人分到一队，另一个队对n个人只有要和不要两选择，dfs暴力枚举这个人是不是分进另一个队伍里，然后取最大值即可。

```
#include&lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
ll d[30], ans;
int a[30][30], n;
vector&lt;int&gt; v;
void dfs(int pos, ll sum)
{
    if(v.size() == n)
    {
        ans = max(ans, sum);
        return ;
    }
    if(pos &gt; 2 * n) return ;
    ll now = d[pos];
    for(auto x : v) now -= 2 * a[pos][x];
        //减去pos和x分一队的贡献
    v.push_back(pos);
    dfs(pos + 1, sum + now);
    v.pop_back();
    dfs(pos + 1, sum);
}
int main()
{
    scanf("%d", &amp;n);
    for(int i = 1; i &lt;= 2 * n; i++)
        for(int j = 1; j &lt;= 2 * n; j++)
            scanf("%d",&amp;a[i][j]), d[i] += a[i][j];
    dfs(1, 0);
    printf("%lld\n", ans);
    return 0;
}

```

 
