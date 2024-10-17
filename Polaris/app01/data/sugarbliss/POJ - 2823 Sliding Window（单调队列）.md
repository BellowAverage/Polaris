
--- 
title:  POJ - 2823 Sliding Window（单调队列） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给定一个数列，从左至右输出每个长度为k的数列段内的最小数和最大数。

**思路：**单调队列维护两端，它的头端可以出数，尾部可以进数，通常用于解决局部性的最值问题。单调栈只维护一端，通常维护全局的单调性。单调栈大小没有上限，而单调队列通常有大小限制。所以本题选择用单调队列解。

**代码中数组的解释： **
- <img alt="dl" class="mathcode" src="https://private.codecogs.com/gif.latex?dl">数组用来表示一个单调队列- <img alt="id" class="mathcode" src="https://private.codecogs.com/gif.latex?id">数组表示单调队列里每个元素在原数组中的下标
**本题只需维护两个队列（单调递减队列，头部肯定是最大值，所以用来求最大值，反之求最小值）**
- 当<img alt="i&gt;=k" class="mathcode" src="https://private.codecogs.com/gif.latex?i%3E%3Dk">时输出<img alt="dl[le]" class="mathcode" src="https://private.codecogs.com/gif.latex?dl%5Ble%5D">（因为是滑动窗口，<img alt="le" class="mathcode" src="https://private.codecogs.com/gif.latex?le">是随着窗口改变的）- <img alt="dl[le]" class="mathcode" src="https://private.codecogs.com/gif.latex?dl%5Ble%5D">表示队首元素在原数组中的下标，当<img alt="i&gt;=id[le] + k" class="mathcode" src="https://private.codecogs.com/gif.latex?i%3E%3Did%5Ble%5D%20&amp;plus;%20k">（此时 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i"> 已经超出了窗口的范围，那么此时<img alt="le" class="mathcode" src="https://private.codecogs.com/gif.latex?le">就要向前移）
 

```
#include &lt;stdio.h&gt;
#include &lt;iostream&gt;
using namespace std;
const int N = 1e6+7;

int a[N], dl[N], id[N], le, ri;
int n, k;

void get_min()
{
    le = 1, ri = 0;
    for(int i = 1; i &lt;= n; i++)
    {
        while(le &lt;= ri &amp;&amp; a[i] &lt; dl[ri]) ri--;
        dl[++ri] = a[i];
        id[ri] = i;
        if(id[le] + k &lt;= i) le++;
        if(i &gt;= k) printf("%d%c",dl[le],i == n ? '\n' : ' ');
    }
}
void get_max()
{
    le = 1, ri = 0;
    for(int i = 1; i &lt;= n; i++)
    {
        while(le &lt;= ri &amp;&amp; a[i] &gt; dl[ri]) ri--;
        dl[++ri] = a[i];
        id[ri] = i;
        if(id[le] + k &lt;= i) le++;
        if(i &gt;= k) printf("%d%c",dl[le],i == n ? '\n':' ');
    }
}
int main()
{
    while(~scanf("%d%d",&amp;n,&amp;k))
    {
        for(int i = 1; i &lt;= n; i++) scanf("%d",&amp;a[i]);
        get_min();
        get_max();
    }

}
```

 
