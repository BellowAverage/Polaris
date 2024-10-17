
--- 
title:  2019牛客暑期多校训练营（第六场）- J - Upgrading Technology（思维） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**你有<img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">个技能每个技能有<img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m">级，从 <img alt="j-1" class="mathcode" src="https://private.codecogs.com/gif.latex?j-1"> 级升级到 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 级需要支付<img alt="C_{ij}" class="mathcode" src="https://private.codecogs.com/gif.latex?C_%7Bij%7D">元（<img alt="C_{ij}&lt;0" class="mathcode" src="https://private.codecogs.com/gif.latex?C_%7Bij%7D%3C0"> 时表示获得<img alt="C_{ij}" class="mathcode" src="https://private.codecogs.com/gif.latex?C_%7Bij%7D">元），当所有技能都升级到 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 级时，获得额外奖励 <img alt="d_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?d_%7Bj%7D">元 （<img alt="d_{j}&lt;0" class="mathcode" src="https://private.codecogs.com/gif.latex?d_%7Bj%7D%3C0"> 时表示失去 <img alt="d_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?d_%7Bj%7D"> 元）元，询问最大的利润，最小利润为0（即升级0个技能）。

**思路：**枚举所有技能的最低等级 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> <img alt="(0&lt;=j&lt;=m)" class="mathcode" src="https://private.codecogs.com/gif.latex?%280%3C%3Dj%3C%3Dm%29">，然后判断每一个技能在最低等级的基础上能不能获得额外的利润（<img alt="C_{ij}" class="mathcode" src="https://private.codecogs.com/gif.latex?C_%7Bij%7D"> 和 <img alt="d_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?d_%7Bj%7D"> 都有可能小于0），为保证当前的最低等级是 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> ，不能所有的技能都升级超过 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> ，所以我们还要维护一个额外利润的最小值，用总的额外利润减去最小利润就是当前等级 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 获得额外利润。这题可以直接暴力三层<img alt="for" class="mathcode" src="https://private.codecogs.com/gif.latex?for">，也可以用后缀数组，ST表，或线段树优化。

**暴力：**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
#define inf 1e18
const int N = 1e3 + 7;
int n, m;
ll c[N][N], d[N], s[N], x;
int main()
{
    int T; scanf("%d",&amp;T);
    for(int Cas = 1; Cas &lt;= T; Cas++)
    {
        scanf("%d%d",&amp;n, &amp;m);
        for(int i = 1; i &lt;= n; i++)
            for(int j = 1; j &lt;= m; j++)
                scanf("%lld", &amp;x), c[i][j] = c[i][j-1] - x;
        for(int i = 1; i &lt;= m; i++)
        {
            scanf("%lld", &amp;d[i]), d[i] += d[i-1];
            s[i] = d[i];
            for(int j = 1; j &lt;= n; j++)
                s[i] += c[j][i];
        }
        ll ans = 0;
        for(int i = 0; i &lt;= m; i++)
        {
            ll tmp = 0, mi = inf, cnt = 0;
            if(i != m)
            for(int j = 1; j &lt;= n; j++)
            {
                ll mx = -inf;
                for(int k = i + 1; k &lt;= m; k++)
                    mx = max(mx, c[j][k] - c[j][i]);
                if(mx &gt; 0)
                {
                    tmp += mx;
                    cnt++;
                    mi = min(mi, mx);
                }
            }
            if(cnt == n) tmp -= mi;
            ans = max(ans, s[i] + tmp);
        }
        printf("Case #%d: %lld\n",Cas, ans);
    }
}
```

**后缀数组优化：**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 1e3 + 7;
int n, m;
ll c[N][N], mx[N][N], d[N], s[N], x;
int main()
{
    int T; scanf("%d",&amp;T);
    for(int Cas = 1; Cas &lt;= T; Cas++)
    {
        scanf("%d%d",&amp;n, &amp;m);
        for(int i = 1; i &lt;= n; i++)
        {
            for(int j = 1; j &lt;= m; j++)
                scanf("%lld", &amp;x), c[i][j] = c[i][j-1] - x;
            mx[i][m+1] = -1ll &lt;&lt; 60;
            for(int j = m; j &gt;= 0; j--)
                mx[i][j] = max(c[i][j], mx[i][j+1]);
        }
        for(int j = 1; j &lt;= m; j++)
            scanf("%lld", &amp;d[j]), d[j] += d[j-1];

        ll ans = 0;
        for(int j = 0; j &lt;= m; j++)
        {
            ll tmp = -1ll&lt;&lt;60;
            for(int i = 1; i &lt;= n; i++)
                tmp = max(tmp, c[i][j] - mx[i][j]);
            for(int i = 1; i &lt;= n; i++)
                tmp += mx[i][j];
            ans = max(ans, tmp + d[j]);
        }
        printf("Case #%d: %lld\n",Cas, ans);
    }
}
/*
2
2 2
1 2
2 -1
4 1
3 3
1 2 3
1 2 3
1 2 3
6 7 8
*/

```

**ST表优化（注意不升级的情况）：**

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
#define inf 1e18
const int N = 1e3 + 7;
int n, m;
ll c[N][N], d[N], s[N], a[N][N][21], lg[N], x;
void ST()
{
    lg[0] = -1;
    for(int i = 1; i &lt;= m + 1; i++)
        lg[i] = lg[i &gt;&gt; 1] + 1;
    for(int i = 1; i &lt;= n; i++)
        for(int j = 1; j &lt;= m + 1; j++)
            a[i][j][0] = c[i][j];
    for(int k = 1; k &lt;= n; k++)
    for(int j = 1; (1&lt;&lt;j) &lt;= m + 1; j++)
        for(int i = 1; (i+(1&lt;&lt;j)-1) &lt;= m + 1; i++)
            a[k][i][j] = max(a[k][i][j-1], a[k][i+(1&lt;&lt;(j-1))][j-1]);
}
ll RMQ(int p, int l, int r)
{
    int k = lg[r-l+1];
    return max(a[p][l][k],a[p][r-(1&lt;&lt;k)+1][k]);
}
 
int main()
{
    int T; scanf("%d",&amp;T);
    for(int Cas = 1; Cas &lt;= T; Cas++)
    {
        scanf("%d%d",&amp;n, &amp;m);
        for(int i = 1; i &lt;= n; i++) c[i][0] = 0;
        for(int i = 1; i &lt;= n; i++)
            for(int j = 2; j &lt;= m + 1; j++)
                scanf("%lld", &amp;x), c[i][j] = c[i][j-1] - x;
        ST();
        for(int i = 2; i &lt;= m + 1; i++)
            scanf("%lld", &amp;d[i]), d[i] += d[i-1];
 
        ll ans = 0;
        for(int j = 1; j &lt;= m + 1; j++)
        {
            ll tmp = 0, mx = -1ll &lt;&lt; 60;
            for(int i = 1; i &lt;= n; i++)
            {
                ll res = RMQ(i, j, m + 1);
                tmp += res; mx = max(mx, c[i][j] - res);
            }
            ans = max(ans, tmp + mx + d[j]);
        }
        printf("Case #%d: %lld\n",Cas, ans);
    }
}
/*
2
2 2
1 2
2 -1
4 1
3 3
1 2 3
1 2 3
1 2 3
6 7 8
*/
```

 
