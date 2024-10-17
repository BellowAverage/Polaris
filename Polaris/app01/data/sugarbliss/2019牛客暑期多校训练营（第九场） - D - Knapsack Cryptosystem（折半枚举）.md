
--- 
title:  2019牛客暑期多校训练营（第九场） - D - Knapsack Cryptosystem（折半枚举） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**挑选若干个数使得和为s。

**思路：**考虑二进制枚举，但是n的范围是36，直接枚举会超时，所以我们把数组分两部分枚举，然后用map映射一下即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
ll a[50], sum, s;
int m, n;
map &lt;ll, string&gt; mp1, mp2;
string str;
int main()
{
    scanf("%d%lld",&amp;n, &amp;s);
    for(int i = 0; i &lt; n; i++) scanf("%lld", &amp;a[i]);
    m = n / 2; n = n - m;
    for(int i = 0; i &lt; (1 &lt;&lt; m); i++)
    {
        sum = 0; str = "";
        for(int j = 0; j &lt; m; j++)
        {
            if(i &amp; (1 &lt;&lt; j))
                sum += a[j], str += '1';
            else str += '0';
        }
        mp1[sum] = str;
    }
    for(int i = 0; i &lt; (1 &lt;&lt; n); i++)
    {
        sum = 0; str = "";
        for(int j = 0; j &lt; n; j++)
        {
            if(i &amp; (1 &lt;&lt; j))
                sum += a[m+j], str += '1';
            else str += '0';
        }
        mp2[sum] = str;
    }
    for(auto it : mp1)
        if(mp2.count(s-it.first))
            return cout &lt;&lt; it.second &lt;&lt; mp2[s-it.first] &lt;&lt; endl, 0;
}

```

 
