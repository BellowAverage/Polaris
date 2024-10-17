
--- 
title:  2019牛客暑期多校训练营（第九场）H - Cutting Bamboos（主席树 + 二分） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有 <img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n"> 棵树和 <img alt="q" class="mathcode" src="https://private.codecogs.com/gif.latex?q"> 次询问。每次询问 <img alt="(l, r, x, y)" class="mathcode" src="https://private.codecogs.com/gif.latex?%28l%2C%20r%2C%20x%2C%20y%29"> 表示在 <img alt="l" class="mathcode" src="https://private.codecogs.com/gif.latex?l"> 到 <img alt="r" class="mathcode" src="https://private.codecogs.com/gif.latex?r"> 的范围内砍  <img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y"> 次，将所有的树高都砍为<img alt="0" class="mathcode" src="https://private.codecogs.com/gif.latex?0">，但是要保证每一刀砍出来的长度(砍去树高于该高度的和)都是相同的。问你第 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 次砍的时候砍的高度在哪里。有精度误差。每次只对本次操作有影响，操作完后，树回到原来的高度。

**思路：**先求出所有树的高度之和<img alt="sum" class="mathcode" src="https://private.codecogs.com/gif.latex?sum">，那么<img alt="sum/y" class="mathcode" src="https://private.codecogs.com/gif.latex?sum/y">表示每次砍多少，显然<img alt="sum*x/y" class="mathcode" src="https://private.codecogs.com/gif.latex?sum*x/y">表示总的需要砍的树。所以我们要二分第** **<img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 次砍的高度<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">（也就是二分答案），我们要求高于<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">部分的总和<img alt="tmp" class="mathcode" src="https://private.codecogs.com/gif.latex?tmp">与**<img alt="sum*x/y" class="mathcode" src="https://private.codecogs.com/gif.latex?sum*x/y">**比较，直接求<img alt="tmp" class="mathcode" src="https://private.codecogs.com/gif.latex?tmp">显然不好求，但是我们可以用总的高于<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">树的总和 - 高于<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">树的数量 * <img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">来求（也就是说我们要求<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">上面的部分和，我们可以用总的减去<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">下面的，因为<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">下面的总是整齐的，所以直接乘就行了）。最后用主席树维护大于<img alt="mid" class="mathcode" src="https://private.codecogs.com/gif.latex?mid">的树的总和与树的数量即可。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef pair&lt;int, int&gt; pii;
typedef pair&lt;ll, ll&gt; pll;
#define mp make_pair
#define pb push_back
#define all(x) x.begin(), x.end()
#define bug prllf("*********\n")
#define debug(x) cerr&lt;&lt;#x&lt;&lt;" = "&lt;&lt;(x)&lt;&lt;endl
#define debugp(x) cerr&lt;&lt;#x&lt;&lt;"= {"&lt;&lt;(x.first)&lt;&lt;", "&lt;&lt;(x.second)&lt;&lt;"}"&lt;&lt;endl
#define debug2(x, y) cerr&lt;&lt;"{"&lt;&lt;#x&lt;&lt;", "&lt;&lt;#y&lt;&lt;"} = {"&lt;&lt;(x)&lt;&lt;", "&lt;&lt;(y)&lt;&lt;"}"&lt;&lt;endl
#define IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
const int mod = 1e9 + 7;
const double eps = 1e-8;
const double pi = acos(-1);
const ll inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;
const int N = 2e5 + 7;
struct node{int l, r, num; ll sum;} T[N*25];
int root[N], cnt;
ll cut_num, cut_sum;
void update(int l,int r,int &amp;now, int pre, int pos)
{
    T[++cnt] = T[pre], T[cnt].num++, T[cnt].sum += pos, now = cnt;
    if(l == r) return;
    int mid = (l + r) &gt;&gt; 1;
    if(mid &gt;= pos) update(l, mid, T[now].l, T[pre].l, pos);
    else update(mid+1, r, T[now].r, T[pre].r, pos);
}
void query(int l, int r, int x, int y, int pos)
{
    if(pos &gt; r) return ;
    if(pos &lt;= l)
    {
        cut_num += T[y].num - T[x].num;
        cut_sum += T[y].sum - T[x].sum;
        return ;
    }
    ll mid = (l + r) &gt;&gt; 1;
    query(l, mid, T[x].l, T[y].l, pos);
    query(mid + 1, r, T[x].r, T[y].r, pos);
}
int n, q, x, y, ql, qr, len = 100000;
int main()
{
    scanf("%d%d", &amp;n, &amp;q);
    for(int i = 1; i &lt;= n; i++)
        scanf("%d", &amp;x), update(1, len, root[i], root[i-1], x);
    while(q--)
    {
        scanf("%d%d%d%d", &amp;ql, &amp;qr, &amp;x, &amp;y);
        double tmp = 1.0 * (T[root[qr]].sum - T[root[ql-1]].sum) * x / y;
        double l = 0, r = 100000.0, mid;
        while(fabs(l - r) &gt; eps)
        {
            cut_num = 0, cut_sum = 0;
            mid = (l + r) / 2.0;
            query(1, len, root[ql-1], root[qr], ceil(mid));
            if(tmp &gt;= 1.0 * cut_sum - 1.0 * cut_num * mid) r = mid;
            else l = mid;
        }
        printf("%.15f\n", r);
    }
}

```

 
