
--- 
title:  Educational Codeforces Round 61 (Rated for Div. 2) - F. Clear the String（区间dp） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一个字符串，相邻的相同字符可以删除，问至少多少次可以让字符串为空？

**思路：**定义<img alt="dp[i][j]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D">表示删除区间<img alt="i\rightarrow j" class="mathcode" src="https://private.codecogs.com/gif.latex?i%5Crightarrow%20j">的字符需要的最少次数，那么<img alt="s[i]=s[j]" class="mathcode" src="https://private.codecogs.com/gif.latex?s%5Bi%5D%3Ds%5Bj%5D">时，<img alt="dp[i][j]=min(dp[i][j-1],dp[i+1][j])" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D%3Dmin%28dp%5Bi%5D%5Bj-1%5D%2Cdp%5Bi&amp;plus;1%5D%5Bj%5D%29">，<img alt="s[i]!=s[j]" class="mathcode" src="https://private.codecogs.com/gif.latex?s%5Bi%5D%21%3Ds%5Bj%5D">时，<img alt="dp[i][j]=min(dp[i][j-1],dp[i+1][j])+1" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D%3Dmin%28dp%5Bi%5D%5Bj-1%5D%2Cdp%5Bi&amp;plus;1%5D%5Bj%5D%29&amp;plus;1">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 5e3 + 7;
int dp[505][505];
char s[505];
int main()
{
    int n; scanf("%d",&amp;n);
    scanf("%s", s+1);
    memset(dp, 0x3f, sizeof dp);
    for(int i = 1; i &lt;= n; i++)
        dp[i][i] = 1;
    for(int l = 2; l &lt;= n; l++)
    {
        for(int i = 1; i + l - 1 &lt;= n; i++)
        {
            int j = i + l - 1;
            if(s[i] == s[j]) dp[i][j] = min(dp[i+1][j], dp[i][j-1]);
            else dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1;
            for(int k = i; k &lt; j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]);
        }
    }
    printf("%d\n",dp[1][n]);
}
```

 
