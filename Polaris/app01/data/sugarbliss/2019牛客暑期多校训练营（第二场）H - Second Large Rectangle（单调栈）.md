
--- 
title:  2019牛客暑期多校训练营（第二场）H - Second Large Rectangle（单调栈） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**求全是1的次大子矩阵。

**思路：**的变形，不能直接把所有的面积存起来然后排序取第二大的，因为次大子矩阵可能在最大子矩阵里面比如：
|1|0|0
|1|1|1
|1|1|1

如果全部存起来排序取第二大输出是3，正确答案是4。所以我们求面积的时候顺便求一下<img alt="(x-1)*y" class="mathcode" src="https://private.codecogs.com/gif.latex?%28x-1%29*y">和<img alt="x*(y-1)" class="mathcode" src="https://private.codecogs.com/gif.latex?x*%28y-1%29">，然后维护次大子矩阵即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e3 + 7;
int n, m, ans;
string str[N];
int h[N], a[N], mx1, mx2;
stack &lt;int&gt; s;
void solve(int x)
{
    if(x &gt; mx1)
        mx2 = mx1, mx1 = x;
    else if(x &gt; mx2) mx2 = x;
}
int main()
{
    scanf("%d%d",&amp;n, &amp;m);
    for(int i = 0; i &lt; n; i++)
    {
        cin &gt;&gt; str[i];
        for(int j = 1; j &lt;= m; j++)
        {
            if(str[i][j-1] == '1') a[j] += 1;
            else a[j] = 0;
            h[j] = a[j];
        }
        s.push(0);
        for(int j = 1; j &lt;= m + 1; j++)
        {
            while(h[j] &lt; h[s.top()])
            {
                int index = s.top();
                s.pop();
                int x = j - 1 - s.top(), y = h[index];
                solve(x * y);
                solve((x - 1)* y);
                solve(x * (y - 1));
            }
            s.push(j);
        }
    }
    cout &lt;&lt; mx2 &lt;&lt; endl;
}

```

 
