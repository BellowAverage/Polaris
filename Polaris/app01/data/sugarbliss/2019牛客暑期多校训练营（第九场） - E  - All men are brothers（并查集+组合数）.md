
--- 
title:  2019牛客暑期多校训练营（第九场） - E  - All men are brothers（并查集+组合数） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**有N个人M个操作，每次操作让两个人互相认识，认识关系可以互相传递，求每次操作完毕后，选4个互相不认识的人的方案数。

**思路：**首先未操作之前<img alt="ans=C_{n}^{4}" class="mathcode" src="https://private.codecogs.com/gif.latex?ans%3DC_%7Bn%7D%5E%7B4%7D">，考虑每次操作对答案的影响，我们设合并的两个集合是<img alt="" class="mathcode" src="https://private.codecogs.com/gif.latex?"><img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">，<img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y">，对于<img alt="" class="mathcode" src="https://private.codecogs.com/gif.latex?"><img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">，<img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y">集合未合并之前，我们可以在<img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">，<img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y">，集合中各挑选一个数，然后在<img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">，<img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y">，集合外挑选两个数，注意集合外挑选时要排除两个数在一个集合的情况。我们用<img alt="pre" class="mathcode" src="https://private.codecogs.com/gif.latex?pre">表示挑选两个陌生人的方案数，此时<img alt="ans -= a * b * (pre - a * (n - a) - b * (n - b) + a * b);" class="mathcode" src="https://private.codecogs.com/gif.latex?ans%20-%3D%20a%20*%20b%20*%20%28pre%20-%20a%20*%20%28n%20-%20a%29%20-%20b%20*%20%28n%20-%20b%29%20&amp;plus;%20a%20*%20b%29%3B">（<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a">和<img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b">表示<img alt="" class="mathcode" src="https://private.codecogs.com/gif.latex?"><img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x">，<img alt="y" class="mathcode" src="https://private.codecogs.com/gif.latex?y">内元素的个数，<img alt="a * (n - a)" class="mathcode" src="https://private.codecogs.com/gif.latex?a%20*%20%28n%20-%20a%29">表示合并之前<img alt="a" class="mathcode" src="https://private.codecogs.com/gif.latex?a">对<img alt="pre" class="mathcode" src="https://private.codecogs.com/gif.latex?pre">的贡献，<img alt="b" class="mathcode" src="https://private.codecogs.com/gif.latex?b">同理，但这样多减了一个<img alt="a*b" class="mathcode" src="https://private.codecogs.com/gif.latex?a*b">，所以还要加过来），注意运算可能超<img alt="long long" class="mathcode" src="https://private.codecogs.com/gif.latex?long%20long">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e5 + 7;
int n, m, x, y;
int tot[N], f[N];
void init(){for(int i = 1; i &lt;= n; i++) f[i] = i, tot[i] = 1;}
int findd(int x){return f[x] == x ? x : f[x] = findd(f[x]);}
int main()
{
    scanf("%d%d",&amp;n, &amp;m); init();
    ll ans = (__int128) n * (n - 1) * (n - 2) * (n - 3) / 24;
    ll pre = n * (n - 1) / 2;
    printf("%lld\n", ans);
    while(m--)
    {
        scanf("%d%d", &amp;x, &amp;y);
        int rx = findd(x), ry = findd(y);
        if(rx != ry)
        {
            ll a = tot[rx], b = tot[ry];
            ans -= a * b * (pre - a * (n - a) - b * (n - b) + a * b);
            pre -= a * b;
            tot[ry] += tot[rx];
            f[rx] = ry;
        }
        printf("%lld\n", ans);
    }
}
/*
6 6
1 2
3 4
4 5
3 5
3 6
2 4
*/

```

当然维护集合外挑选两个陌生人的操作，也可以用总的挑选两个数的方案数 - 在一个集合里挑选两个数的方案。<img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s">表示集合内挑选两个数的方案，未合并前<img alt="a,b" class="mathcode" src="https://private.codecogs.com/gif.latex?a%2Cb">集合对<img alt="s" class="mathcode" src="https://private.codecogs.com/gif.latex?s">都有贡献，所以合并<img alt="a,b" class="mathcode" src="https://private.codecogs.com/gif.latex?a%2Cb">集合时要把这个贡献减掉<img alt="s -= (a * (a - 1) / 2 + b * (b - 1) / 2);" class="mathcode" src="https://private.codecogs.com/gif.latex?s%20-%3D%20%28a%20*%20%28a%20-%201%29%20/%202%20&amp;plus;%20b%20*%20%28b%20-%201%29%20/%202%29%3B">维护集合外两个元素时会超<img alt="long long" class="mathcode" src="https://private.codecogs.com/gif.latex?long%20long">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll unsigned long long
const int N = 1e5 + 7;
ll n, m, x, y;
ll tot[N], f[N];
void init(){for(int i = 1; i &lt;= n; i++) f[i] = i, tot[i] = 1;}
ll findd(ll x){return f[x] == x ? x : f[x] = findd(f[x]);}
int main()
{
    cin &gt;&gt; n &gt;&gt; m; init();
    ll ans = (__int128)n * (n - 1) * (n - 2) * (n - 3) / 24;
    ll s = 0;
    cout &lt;&lt; ans &lt;&lt; endl;
    while(m--)
    {
        cin &gt;&gt; x &gt;&gt; y;
        ll rx = findd(x), ry = findd(y);
        if(rx != ry)
        {
            ll a = tot[rx], b = tot[ry];
            ll k = n - a - b;
            s -= (a * (a - 1) / 2 + b * (b - 1) / 2);
            ans -= a * b * (k * (k - 1) / 2 - s);
            tot[ry] += tot[rx];
            s += (tot[ry] * (tot[ry] - 1)) / 2;
            f[rx] = ry;
        }
        cout &lt;&lt; ans &lt;&lt; endl;
    }
}
/*
6 6
1 2
3 4
4 5
3 5
3 6
2 4
*/

```

 
