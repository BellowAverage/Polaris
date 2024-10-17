
--- 
title:  第五届新疆省ACM-ICPC程序设计竞赛（重现赛）E - 斐波那契串（二分） 
tags: []
categories: [] 

---
**题目链接：**

**思路：我们可以发现第x个串的第y个字符，和第一个串的长度大于等于y的这个串的第y个字符一样，先预处理串的长度，然后二分查找这个位置，然后暴力查找。**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e4 + 7;
ll f[N];
int main()
{
    string s[3]; int Q, k;
    cin &gt;&gt; s[1] &gt;&gt; s[2];
    f[1] = s[1].length();
    f[2] = s[2].length();
    for(int i = 3; f[i-1] &lt;= 1e18 ; i++)
        f[i] = f[i-1] + f[i-2], k = i;
    cin &gt;&gt; Q;
    while(Q--)
    {
        ll x, y;
        cin &gt;&gt; x &gt;&gt; y;
        if(x &gt; 2)
        x = lower_bound(f, f + k, y) - f;
        while(x &gt; 2)
        {
            if(y &gt; f[x-1])
            {
                y -= f[x-1];
                x -= 2;
            }
            else x--;
        }
        cout &lt;&lt; s[x][y-1] &lt;&lt; endl;
    }
}

```

 
