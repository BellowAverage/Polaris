
--- 
title:  2019牛客暑期多校训练营（第一场）E - ABBA（dp） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有多少个长度为<img alt="2(n+m)" class="mathcode" src="https://private.codecogs.com/gif.latex?2%28n&amp;plus;m%29">的AB序列，可以划分为n个AB子序列，m个BA子序列。

**思路：**数据范围和题型可以看出是dp，对于空字符串要么先放A要么先放B，对于先放A，每一个满足条件的字符串都必然满足前n个A与B匹配，后m个A与B匹配的这种分配情况。对于先放B与此类似。

定义<img alt="dp[i][j]" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi%5D%5Bj%5D">，表示 i 个A，j 个B时**合法**字符串的方案数，<img alt="dp[0][0]=1" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5B0%5D%5B0%5D%3D1">，表示0个AB子序列和0个BA子序列的方案数为1。

对于先放A，前n个A一定贡献给AB子序列，当第n+1个A出现时，则这个A一定是贡献给BA子序列，当<img alt="j&gt;i-n" class="mathcode" src="https://private.codecogs.com/gif.latex?j%3Ei-n">时，此时可以放A，比如<img alt="j = 3, i-n=2" class="mathcode" src="https://private.codecogs.com/gif.latex?j%20%3D%203%2C%20i-n%3D2">，此时可以再放一个A组成3个BA子序列，也就是此时多的B只能给A当前缀组成BA。

此时：<img alt="dp[i+1][j] = dp[i+1][j] + dp[i][j] ;" class="mathcode" src="https://private.codecogs.com/gif.latex?dp%5Bi&amp;plus;1%5D%5Bj%5D%20%3D%20dp%5Bi&amp;plus;1%5D%5Bj%5D%20&amp;plus;%20dp%5Bi%5D%5Bj%5D%20%3B">  放B与此类似。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 2e3 + 7;
const int mod = 1e9 + 7;
int n, m, dp[N][N];
int main()
{
    while(~scanf("%d%d",&amp;n,&amp;m))
    {
        for(int i = 0; i &lt;= n + m; i++)
            for(int j = 0; j &lt;= n + m; j++)
                dp[i][j] = 0;
        dp[0][0] = 1;
        for(int i = 0; i &lt;= n + m; i++)
        {
            for(int j = 0; j &lt;= n + m; j++)
            {
                if(j &gt; i - n)
                    dp[i+1][j] = (dp[i+1][j] % mod + dp[i][j] % mod) % mod;
                if(i &gt; j - m)
                    dp[i][j+1] = (dp[i][j+1] % mod + dp[i][j] % mod) % mod;
            }
        }
        printf("%d\n", dp[n+m][n+m]);
    }
}

```

 
