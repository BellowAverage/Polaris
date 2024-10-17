
--- 
title:  第五届新疆省ACM-ICPC程序设计竞赛（重现赛）D - O(n!）（贪心） 
tags: []
categories: [] 

---
**题目链接：**

**思路：**对于前两个商品<img alt="\left\{\begin{matrix} a_{1} &amp;p_{1} \\ a_{2} &amp; p_{2} \end{matrix}\right." class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20a_%7B1%7D%20%26p_%7B1%7D%20%5C%5C%20a_%7B2%7D%20%26%20p_%7B2%7D%20%5Cend%7Bmatrix%7D%5Cright.">，有两种购买方式要么先买<img alt="a_{1}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7B1%7D">，<img alt="ans_{1}=a_{1}+a_{2}*p_{1}" class="mathcode" src="https://private.codecogs.com/gif.latex?ans_%7B1%7D%3Da_%7B1%7D&amp;plus;a_%7B2%7D*p_%7B1%7D">，要么先买<img alt="a_{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7B2%7D">，<img alt="ans_{2}=a_{2}+a_{1}*p_{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?ans_%7B2%7D%3Da_%7B2%7D&amp;plus;a_%7B1%7D*p_%7B2%7D">，如果<img alt="ans_{1}&lt;ans_{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?ans_%7B1%7D%3Cans_%7B2%7D">，显然<img alt="a_{1}+a_{2}*p_{1} &lt;a_{2}+a_{1}*p_{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7B1%7D&amp;plus;a_%7B2%7D*p_%7B1%7D%20%3Ca_%7B2%7D&amp;plus;a_%7B1%7D*p_%7B2%7D">，为了<img alt="ans" class="mathcode" src="https://private.codecogs.com/gif.latex?ans">取到最小值，**<img alt="a_{1}+a_{2}*p_{1} &lt;a_{2}+a_{1}*p_{2}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7B1%7D&amp;plus;a_%7B2%7D*p_%7B1%7D%20%3Ca_%7B2%7D&amp;plus;a_%7B1%7D*p_%7B2%7D">，**我们依次为关键字排序即可。对于贪心的正确性，对于1,2两个商品可以取到最优，全部的呢？其实这是局部最优到全局最优的过程，想想冒泡排序的原理就理解了。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1e5 + 7;
int a[N], vis[N], n;
double p[N], k[N];
struct node
{
    int a;
    double p;
}v[N];
bool cmp(node x, node y)
{
    return x.a + y.a * x.p &lt; y.a + x.a * y.p;
}
int main()
{
    scanf("%d",&amp;n);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d %lf", &amp;v[i].a, &amp;v[i].p);
    sort(v + 1, v + 1 + n, cmp);
    double ans = v[1].a, res = v[1].p;
    for(int i = 2; i &lt;= n; i++)
    {
        ans += v[i].a * res;
        res *= v[i].p;
    }
    printf("%.6f\n",ans);
}

```
