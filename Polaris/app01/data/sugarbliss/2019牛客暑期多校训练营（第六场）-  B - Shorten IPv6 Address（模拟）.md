
--- 
title:  2019牛客暑期多校训练营（第六场）-  B - Shorten IPv6 Address（模拟） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**您将获得一个IPv6地址，该地址是128位二进制字符串。请根据以下规则确定其最短的表示：

以十六进制表示形式表示地址，并使用冒号'：'分割每四个十六进制数字。每四个数字称为一个字段。例如，'0000：0000：0123：4567：89ab：0000：0000：0000'。 可以省略字段中的前导零。例如，上述IPv6地址可以缩短为'0：0：123：4567：89ab：0：0：0'。 由至少两个字段组成的连续零字段（靠近它们的冒号）可以用双冒号'::'替换。此外，地址中不能使用多个双冒号。例如，上面的IPv6地址可以缩短为'0：0：123：4567：89ab ::'或':: 123：4567：89ab：0：0：0'，但不能缩写为':: 123：4567： 89ab ::”。 如果有多个相同长度的最短格式，请使用字典序（将缩短的IPv6地址视为字符串）最小的一个。

**思路：**先将二进制转化为十进制，每次一定会删去一段连续且尽可能长的 0，有一个坑点是首尾和中间同样长度的 0 对答案的贡献是不一样的，用一个数组确定双冒号的位置，用<img alt="%x" class="mathcode" src="https://private.codecogs.com/gif.latex?%25x"><img alt="%x" class="mathcode" src="https://private.codecogs.com/gif.latex?%25x"><img alt="%x" class="mathcode" src="https://private.codecogs.com/gif.latex?%25x">%x直接转化十六进制输出即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1000;
int a[10], r[10];
char s[N];
int main ()
{
    int Case;
    scanf("%d", &amp;Case);
    for(int cas = 1; cas &lt;= Case; cas++)
    {
        scanf("%s", s + 1);
        for(int i = 1; i &lt;= 8; i++)
        {
            a[i] = 0;
            for(int j = 1; j &lt;= 16; j++)
                a[i] = a[i] * 2 + s[(i - 1) * 16 + j] - '0';
        }
        printf("Case #%d: ", cas);
        memset(r, 0, sizeof(r));
        int id = 0;
        for(int i = 8; i &gt;= 1; i--)
        {
            if (a[i] == 0) r[i] = r[i+1] + 1;
            if (r[id] &lt; r[i]) id = i;
            if (r[id] == r[i] &amp;&amp; r[id] + id - 1 == 8 &amp;&amp; i != 1) id = i;
        }
        for(int i = 1; i &lt;= 8; i++)
        {
            if(i == id &amp;&amp; r[i] &gt;= 2)
            {
                if (id == 1) printf(":");
                printf(":");
                i = i + r[i] - 1;
            }
            else
            {
                printf("%x", a[i]);
                if (i != 8) printf(":");
            }
        }
        puts("");
    }
}

```
