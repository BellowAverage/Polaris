
--- 
title:  牛客小白月赛18 - E - Forsaken的数列（splay模板） 
tags: []
categories: [] 

---
**题目链接：**

```
#include &lt;iostream&gt;
#include &lt;cstdio&gt;
#include &lt;cstring&gt;
#include &lt;stack&gt;
#include &lt;vector&gt;
#include &lt;algorithm&gt;
#include &lt;queue&gt;
#define rep(i) for (int i=0; i&lt;n; i++)
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
typedef long long ll;
const int N=1000005, inf=0x3f3f3f3f;

typedef struct splaynode* node;
struct splaynode {
    node pre, ch[2];
    ll value, lazy, max, sum;
    int size, rev;
    void init(int _value) {
        pre=ch[0]=ch[1]=NULL;
        max=value=sum=_value;
        lazy=rev=0;
        size=1;
    }
}mem[N];
int memtop;

stack&lt;node&gt; S;
node root;

inline int getsize(node &amp;x) {
    return x ? x-&gt;size : 0;
}

void pushdown(node &amp;x) {
    if (!x) return;
    if (x-&gt;lazy) {
        ll w = x-&gt;lazy;
        x-&gt;value += w;
        if (x-&gt;ch[0]) {
            x-&gt;ch[0]-&gt;lazy += w;
            x-&gt;ch[0]-&gt;max += w;
            x-&gt;ch[0]-&gt;sum += w*getsize(x-&gt;ch[0]);
        }
        if (x-&gt;ch[1]) {
            x-&gt;ch[1]-&gt;lazy += w;
            x-&gt;ch[1]-&gt;max += w;
            x-&gt;ch[1]-&gt;sum += w*getsize(x-&gt;ch[1]);
        }
        x-&gt;lazy = 0;
    }
    if (x-&gt;rev) {
        node t = x-&gt;ch[0];
        x-&gt;ch[0] = x-&gt;ch[1];
        x-&gt;ch[1] = t;
        x-&gt;rev = 0;
        if (x-&gt;ch[0]) x-&gt;ch[0]-&gt;rev ^= 1;
        if (x-&gt;ch[1]) x-&gt;ch[1]-&gt;rev ^= 1;
    }
}

void update(node &amp;x) {
    if (!x) return;
    x-&gt;size = 1;
    x-&gt;max = x-&gt;value;
    x-&gt;sum = x-&gt;value;
    if (x-&gt;ch[0]) {
        x-&gt;sum += x-&gt;ch[0]-&gt;sum;
        x-&gt;max = max(x-&gt;max, x-&gt;ch[0]-&gt;max);
        x-&gt;size += x-&gt;ch[0]-&gt;size;
    }
    if (x-&gt;ch[1]) {
        x-&gt;sum += x-&gt;ch[1]-&gt;sum;
        x-&gt;max = max(x-&gt;max, x-&gt;ch[1]-&gt;max);
        x-&gt;size += x-&gt;ch[1]-&gt;size;
    }
}

void rotate(node &amp;x, int d) {
    node y = x-&gt;pre;
    pushdown(y);
    pushdown(x);
    pushdown(x-&gt;ch[d]);
    y-&gt;ch[!d] = x-&gt;ch[d];
    if (x-&gt;ch[d] != NULL) x-&gt;ch[d]-&gt;pre = y;
    x-&gt;pre = y-&gt;pre;
    if (y-&gt;pre != NULL)
        if (y-&gt;pre-&gt;ch[0] == y) y-&gt;pre-&gt;ch[0] = x; else y-&gt;pre-&gt;ch[1] = x;
    x-&gt;ch[d] = y;
    y-&gt;pre = x;
    update(y);
    if (y == root) root = x;
}

void splay(node &amp;src, node &amp;dst) {
    pushdown(src);
    while (src!=dst) {
        if (src-&gt;pre==dst) {
            if (dst-&gt;ch[0]==src) rotate(src, 1); else rotate(src, 0);
            break;
        }
        else {
            node y=src-&gt;pre, z=y-&gt;pre;
            if (z-&gt;ch[0]==y) {
                if (y-&gt;ch[0]==src) {
                    rotate(y, 1);
                    rotate(src, 1);
                }else {
                    rotate(src, 0);
                    rotate(src, 1);
                }
            }
            else {
                if (y-&gt;ch[1]==src) {
                    rotate(y, 0);
                    rotate(src, 0);
                }else {
                    rotate(src, 1);
                    rotate(src, 0);
                }
            }
            if (z==dst) break;
        }
        update(src);
    }
    update(src);
}

void select(int k, node &amp;f) {
    int tmp;
    node t = root;
    while (1) {
        pushdown(t);
        tmp = getsize(t-&gt;ch[0]);
        if (k == tmp + 1) break;
        if (k &lt;= tmp) t = t-&gt;ch[0];
        else {
            k -= tmp + 1;
            t = t-&gt;ch[1];
        }
    }
    pushdown(t);
    splay(t, f);
}

inline void selectsegment(int l,int r) {
    select(l, root);
    select(r + 2, root-&gt;ch[1]);
}

void insert(int pos, int value) {  //在pos位置后面插入一个新值value
    selectsegment(pos + 1, pos);
    node t;
    node x = root-&gt;ch[1];
    pushdown(root);
    pushdown(x);
    if (!S.empty()) {
        t = S.top();
        S.pop();
    } else {
        t = &amp;mem[memtop++];
    }
    t-&gt;init(value);
    t-&gt;ch[1] = x;
    x-&gt;pre = t;
    root-&gt;ch[1] = t;
    t-&gt;pre = root;
    splay(x, root);
}

void add(int a,int b, int value) {  //区间[a,b]中的数都加上value
    selectsegment(a, b);
    node x = root-&gt;ch[1]-&gt;ch[0];
    pushdown(x);
    update(x);
    x-&gt;max += value;
    x-&gt;lazy += value;
    splay(x, root);
}

void reverse(int a, int b) {   //区间[a,b]中的数翻转
    selectsegment(a, b);
    root-&gt;ch[1]-&gt;ch[0]-&gt;rev ^= 1;
    node x = root-&gt;ch[1]-&gt;ch[0];
    splay(x, root);
}

void revolve(int a, int b, int t) { //区间[a,b]中的数向后循环移t位
    node p1, p2;
    selectsegment(a, b);
    select(b + 1 - t, root-&gt;ch[1]-&gt;ch[0]);
    p1 = root-&gt;ch[1]-&gt;ch[0];
    pushdown(p1);
    p2 = p1-&gt;ch[1];
    p1-&gt;ch[1] = NULL;

    select(a + 1, root-&gt;ch[1]-&gt;ch[0]);
    p1 = root-&gt;ch[1]-&gt;ch[0];
    pushdown(p1);
    p1-&gt;ch[0] = p2;
    p2-&gt;pre = p1;

    splay(p2, root);
}

ll getmax(int a, int b) {   //取[a,b]中最小的值
    selectsegment(a, b);
    node x = root-&gt;ch[1];
    pushdown(x);
    x = x-&gt;ch[0];
    pushdown(x);
    update(x);
    return x-&gt;max;
}

ll getsum(int a, int b) {
    selectsegment(a, b);
    node x = root-&gt;ch[1];
    pushdown(x);
    x = x-&gt;ch[0];
    pushdown(x);
    update(x);
    return x-&gt;sum;
}

void erase(int pos) {               //抹去第pos个元素
    selectsegment(pos, pos);
    pushdown(root-&gt;ch[1]);
    S.push(root-&gt;ch[1]-&gt;ch[0]);        //回收内存
    root-&gt;ch[1]-&gt;ch[0] = NULL;
    node x = root-&gt;ch[1];
    splay(x, root);
}


void cutandmove(int a,int b,int c)
{
    selectsegment(a,b);
    node CutRoot=root-&gt;ch[1]-&gt;ch[0];
    CutRoot-&gt;pre=NULL;
    root-&gt;ch[1]-&gt;size-=CutRoot-&gt;size;
    root-&gt;ch[1]-&gt;ch[0]=NULL;
    selectsegment(c+1,c);

    CutRoot-&gt;pre=root-&gt;ch[1];
    root-&gt;ch[1]-&gt;ch[0]=CutRoot;
    root-&gt;ch[1]-&gt;size+=CutRoot-&gt;size;
}

void cut(int a,int b)
{
    selectsegment(a,b);
    node CutRoot=root-&gt;ch[1]-&gt;ch[0];
    CutRoot-&gt;pre=NULL;
    root-&gt;size-=CutRoot-&gt;size;
    root-&gt;ch[1]-&gt;size-=CutRoot-&gt;size;
    root-&gt;ch[1]-&gt;ch[0]=NULL;
}

vector&lt;int&gt; ans;
void inorder(node x)
{
    if (!x) return;
    pushdown(x);
    inorder(x-&gt;ch[0]);
    if (x-&gt;value!=inf) ans.push_back(x-&gt;value);
    inorder(x-&gt;ch[1]);
}

void initsplaytree(ll *a, int n) {
    memtop = 0;
    root = &amp;mem[memtop++];
    root-&gt;init(inf);
    root-&gt;ch[1] = &amp;mem[memtop++];
    root-&gt;ch[1]-&gt;init(inf);
    while (!S.empty()) S.pop();
    rep(i) insert(i, a[i]);
}

ll v[N];
int main() {
    int n, m, op;
    scanf("%d", &amp;n);
    rep(i) scanf("%lld", &amp;v[i]);
    scanf("%d", &amp;m);
    initsplaytree(v, n);
    while (m--) {
        scanf("%d", &amp;op);
        int l, r, pos, d;
        if(op == 1) scanf("%d", &amp;pos), insert(pos-1, 0);
        else if(op == 2) scanf("%d%d%d", &amp;l, &amp;r, &amp;d), add(l, r, d);
        else scanf("%d%d", &amp;l, &amp;r), printf("%lld\n", getsum(l, r));
    }
    return 0;
}

```

 
