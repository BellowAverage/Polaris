
--- 
title:  HDU - 6629 - string matching（扩展KMP） 
tags: []
categories: [] 

---
**题目链接：**

**题意：给你一个字符串<img alt="S" class="mathcode" src="https://private.codecogs.com/gif.latex?S">，让你求对于<img alt="S" class="mathcode" src="https://private.codecogs.com/gif.latex?S">每一个字符串的后缀<img alt="T" class="mathcode" src="https://private.codecogs.com/gif.latex?T">（<img alt="S!=T" class="mathcode" src="https://private.codecogs.com/gif.latex?S%21%3DT">），与<img alt="S" class="mathcode" src="https://private.codecogs.com/gif.latex?S">匹配最长公共前缀的总次数。**

**思路：**对于<img alt="S" class="mathcode" src="https://private.codecogs.com/gif.latex?S">和<img alt="S" class="mathcode" src="https://private.codecogs.com/gif.latex?S">做扩展KMP，得到<img alt="extend[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?extend%5Bi%5D">数组**（<img alt="extend[i]" class="mathcode" src="https://private.codecogs.com/gif.latex?extend%5Bi%5D">**表示**<img alt="S" class="mathcode" src="https://private.codecogs.com/gif.latex?S">**与<img alt="S[i,n-1]" class="mathcode" src="https://private.codecogs.com/gif.latex?S%5Bi%2Cn-1%5D">  <img alt="(0&lt;=i&lt;n)" class="mathcode" src="https://private.codecogs.com/gif.latex?%280%3C%3Di%3Cn%29">的最长公共前缀**），**然后从<img alt="extend[1]" class="mathcode" src="https://private.codecogs.com/gif.latex?extend%5B1%5D">开始统计即可。

```
#include &lt;bits/stdc++.h&gt;
#define ll long long
using namespace std;
const int N = 1e6 + 7;
int Next[N], extend[N];

void getNext(char str[])
{
    int i = 0, j, po, len = strlen(str);
    Next[0] = len;
    while(str[i] == str[i+1] &amp;&amp; i + 1 &lt; len) i++; Next[1] = i;
    po = 1;
    for(i = 2; i &lt; len; i++)
    {
        if(Next[i-po] + i &lt; Next[po]+po)
            Next[i] = Next[i-po];
        else
        {
            j = Next[po] + po - i;
            if(j &lt; 0) j = 0;
            while(i + j &lt; len &amp;&amp; str[j] == str[j+i]) j++; Next[i] = j;
            po = i;
        }
    }
}

void EXKMP(char s1[],char s2[])
{
    int i = 0, j, po, len = strlen(s1), l2 = strlen(s2);
    getNext(s2);
    while(s1[i] == s2[i] &amp;&amp; i &lt; l2 &amp;&amp; i &lt; len) i++; extend[0] = i;
    po = 0;
    for(i = 1; i &lt; len; i++)
    {
        if(Next[i-po] + i &lt; extend[po] + po)
            extend[i] = Next[i-po];
        else
        {
            j = extend[po] + po - i;
            if(j &lt; 0) j = 0;
            while(i + j &lt; len &amp;&amp; j &lt; l2 &amp;&amp; s1[j+i] == s2[j]) j++; extend[i] = j;
            po = i;
        }
    }
}
char s[N], t[N];
int main()
{
    int T; scanf("%d",&amp;T);
    while(T--)
    {
        scanf("%s", s);
        EXKMP(s, s);
        int n = strlen(s);
        ll ans = 0;
        for(int i = 1; i &lt; n; i++)
        {
            if(extend[i] == 0) ans ++;
            else if(extend[i] == n - i) ans += extend[i];
            else ans += extend[i] + 1;
        }
        printf("%lld\n", ans);
    }
    return 0;
}

```

 
