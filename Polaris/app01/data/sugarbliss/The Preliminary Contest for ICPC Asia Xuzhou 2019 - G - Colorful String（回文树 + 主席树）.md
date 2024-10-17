
--- 
title:  The Preliminary Contest for ICPC Asia Xuzhou 2019 - G - Colorful String（回文树 + 主席树） 
tags: []
categories: [] 

---
**题目链接：**

**题意：给你一个串s，询问s中所有的回文串中不同子母的和。**

**思路：用回文树统计每一个回文串的长度和个数，用主席树统计回文串不同子母的个数即可。**

**PS：****回文树的功能：**

**1.求串S前缀0~i内本质不同回文串的个数（两个串长度不同或者长度相同且至少有一个字符不同便是本质不同）****2.求串S内每一个本质不同回文串出现的次数****3.求串S内回文串的个数（其实就是1和2结合起来）****4.求以下标i结尾的回文串的个数**

```
#include &lt;cstdio&gt;
#include &lt;iostream&gt;
#include &lt;cstring&gt;
using namespace std;
#define ll long long
const int N=5e5+10;
char s[N];
int n,last,len[N],fail[N],cnt[N],p,nex[N][26];
int tot, root[N], a[N], pre[N], l, r, k, ans;
int s_len[N], pos[N];
struct node{int l, r, sum;} T[N*25];
void update(int l,int r,int &amp;now, int pre, int pos, int c)
{
    T[++tot] = T[pre], T[tot].sum += c, now = tot;
    if(l == r) return;
    int mid = (l + r) &gt;&gt; 1;
    if(mid &gt;= pos) update(l, mid, T[now].l, T[pre].l, pos, c);
    else update(mid + 1, r, T[now].r, T[pre].r, pos, c);
}
int query(int l, int r, int rt, int L, int R)
{
    if(L &lt;= l &amp;&amp; r &lt;= R) return T[rt].sum;
    int mid = (l + r) / 2;
    int res = 0;
    if(mid &gt;= L)  res += query(l, mid, T[rt].l, L, R);
    if(mid &lt; R)  res += query(mid+1, r, T[rt].r, L, R);
    return res;
}
int main()
{
    scanf("%s",s+1); n=strlen(s+1);
    for(int i = 1; i &lt;= n; i++) a[i] = s[i] - 'a' + 1;
    for(int i = 1; i &lt;= n; i++)
    {
        update(1, n, root[i], root[i-1], i, 1);
        if(pre[a[i]]) update(1, n, root[i], root[i], pre[a[i]], -1);
        pre[a[i]] = i;
    }
    p = 1; len[1] = -1; fail[0] = 1; fail[1] = -1;
    for(int i = 1; i &lt;= n; i++)
    {
        while(s[i-len[last]-1] != s[i])
            last = fail[last];
        int &amp;g = nex[last][s[i]-'a'];
        if(!g)
        {
            g = ++p, len[g] = len[last] + 2;
            if(len[g] &gt; 1) pos[p] = i; //记录回文串的下标
            int k = fail[last];
            while (k != -1 &amp;&amp; s[i-len[k]-1] != s[i]) k = fail[k];
            if(k == -1) fail[g] = 0;
            else fail[g] = nex[k][s[i]-'a'];
        }
        cnt[g]++;
        last = g;
    }
    for(int i = p; i &gt;= 0; i--) cnt[fail[i]] += cnt[i];
    ll ans = n;
    for(int i = 2; i &lt;= p; i++)
        if(len[i] &gt; 1) ans += query(1, n, root[pos[i]], pos[i] - len[i] + 1, pos[i]) * cnt[i];
    printf("%lld\n", ans);
}
/*
abacdaaabaaa
26
*/

```

 
