
--- 
title:  poj - 2926 - Requirements（多维曼哈顿距离） 
tags: []
categories: [] 

---
**题目链接：**

**思路：二维空间上两个坐标之间的曼哈顿距离<img alt="(x1, y1)" class="mathcode" src="https://private.codecogs.com/gif.latex?%28x1%2C%20y1%29"> 和 <img alt="(x2, y2)" class="mathcode" src="https://private.codecogs.com/gif.latex?%28x2%2C%20y2%29">，<img alt="|x1-x2| +|y1-y2|" class="mathcode" src="https://private.codecogs.com/gif.latex?%7Cx1-x2%7C%20&amp;plus;%7Cy1-y2%7C">去掉绝对值符号后共有下列四种情况：**

**<img alt="\left \{ (x1-x2) + (y1-y2) \right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x1-x2%29%20&amp;plus;%20%28y1-y2%29%20%5Cright%20%5C%7D">**

**<img alt="\left \{ (x1-x2) + (y2-y1)\right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x1-x2%29%20&amp;plus;%20%28y2-y1%29%5Cright%20%5C%7D">**

**<img alt="\left \{ (x2-x1)+ (y1-y2) \right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x2-x1%29&amp;plus;%20%28y1-y2%29%20%5Cright%20%5C%7D">**

**<img alt="\left \{ (x2-x1) + (y2-y1) \right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x2-x1%29%20&amp;plus;%20%28y2-y1%29%20%5Cright%20%5C%7D">**

**转化一下：**

**<img alt="\left \{ (x1+y1) - (x2+y2) \right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x1&amp;plus;y1%29%20-%20%28x2&amp;plus;y2%29%20%5Cright%20%5C%7D">**

<img alt="\left \{ (x1-y1) - (x2-y2) \right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x1-y1%29%20-%20%28x2-y2%29%20%5Cright%20%5C%7D">

<img alt="\left \{ (-x1+y1)- (-x2+y2)\right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28-x1&amp;plus;y1%29-%20%28-x2&amp;plus;y2%29%5Cright%20%5C%7D">

<img alt="\left \{ (-x1-y1)- (-x2-y2)\right \}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28-x1-y1%29-%20%28-x2-y2%29%5Cright%20%5C%7D">

**显然，任意给两个点，我们分别计算上述四种情况，那么最大值就是曼哈顿距离。如果我们用1表示+号，用0表示-号那么对应为：**

**<img alt="\left \{ (x1+y1) - (x2+y2) \right \}\leftrightarrow(1,1,1,1)" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x1&amp;plus;y1%29%20-%20%28x2&amp;plus;y2%29%20%5Cright%20%5C%7D%5Cleftrightarrow%281%2C1%2C1%2C1%29">**

<img alt="\left \{ (x1-y1) - (x2-y2) \right \}\leftrightarrow (1,0,1,0)" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28x1-y1%29%20-%20%28x2-y2%29%20%5Cright%20%5C%7D%5Cleftrightarrow%20%281%2C0%2C1%2C0%29">

<img alt="\left \{ (-x1+y1)- (-x2+y2)\right \}\leftrightarrow (0,1,0,1)" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28-x1&amp;plus;y1%29-%20%28-x2&amp;plus;y2%29%5Cright%20%5C%7D%5Cleftrightarrow%20%280%2C1%2C0%2C1%29">

<img alt="\left \{ (-x1-y1)- (-x2-y2)\right \}\leftrightarrow (0,0,0,0)" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%20%5C%7B%20%28-x1-y1%29-%20%28-x2-y2%29%5Cright%20%5C%7D%5Cleftrightarrow%20%280%2C0%2C0%2C0%29">

**所以我们可以二进制枚举即可，也就是枚举<img alt="2^{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?2%5E%7B2%7D">种情况，扩展到n维也是一个道理，无非是枚举****<img alt="2^{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?2%5E%7Bn%7D">种情况。**

```
#include &lt;stdio.h&gt;
#include &lt;iostream&gt;
#include &lt;vector&gt;
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;
const int mod = 998244353;
const double eps = 1e-8;

const int N = 1e5 + 7;
int n;
double x, a[N][10];
double get_Manhattan(int d) //d维曼哈顿，两点之间最大值
{
    double ans = 0;
    for(int i = 0; i &lt; (1 &lt;&lt; d); i++)
    {
        double mi = inf, mx = -inf;
        for(int k = 0; k &lt; n; k++)
        {
            double t = 0;
            for(int j = 0; j &lt; d; j++)
            {
                if(i &amp; (1 &lt;&lt; j)) t += a[k][j];
                else t -= a[k][j];
            }
            mi = min(mi, t);
            mx = max(mx, t);
        }
        ans = max(mx - mi, ans);
    }
    return ans;
}
int main()
{
    while(~scanf("%d",&amp;n))
    {
        for(int i = 0; i &lt; n; i++)
            for(int j = 0; j &lt; 5; j++)
                scanf("%lf", &amp;a[i][j]);
        double ans = get_Manhattan(5);
        printf("%.2f\n", ans);
    }
}
```

 

 
