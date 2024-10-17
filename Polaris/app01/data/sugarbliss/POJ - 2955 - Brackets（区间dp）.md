
--- 
title:  POJ - 2955 - Brackets（区间dp） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**最长括号匹配序列的长度。

思路：定义<img alt="dp[i][j]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D">表示区间<img alt="i\rightarrow j" class="mathcode" src="https://private.codecogs.com/gif.latex?i%5Crightarrow%20j">最多匹配的括号个数。

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;iostream&gt;
using namespace std;
const int N = 1e5 + 7;
bool judge(char a, char b)
{
    if(a == '(' &amp;&amp; b == ')') return true;
    if(a == '[' &amp;&amp; b == ']') return true;
    return false;
}
int dp[105][105];
int main()
{
    string s;
    while(cin &gt;&gt; s)
    {
        if(s == "end") break;
        int n = s.length();
        memset(dp, 0, sizeof dp);
        for(int l = 2; l &lt;= n; l++)
        {
            for(int i = 0; i + l - 1 &lt; n; i++)
            {
                int j = i + l - 1;
                if(judge(s[i], s[j])) dp[i][j] = dp[i+1][j-1] + 1;
                else dp[i][j] = max(dp[i][j-1], dp[i+1][j]);
                for(int k = i; k &lt; j; k++)
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j]);
            }
        }
        printf("%d\n",dp[0][n-1] * 2);
    }
}

```

 
