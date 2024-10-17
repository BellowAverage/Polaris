
--- 
title:  HDU6574  - 2019CCPC-江西省赛H - Rng（概率+递推） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**区间<img alt="[1,n]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B1%2Cn%5D">内选两个线段，求两个线段不相交的概率。

**思路：**线段相交有两种情况，第一种<img alt="" class="has" height="38" src="https://img-blog.csdnimg.cn/20190723154953968.png" width="129">第二个线段的右端点<img alt="R2" class="mathcode" src="https://private.codecogs.com/gif.latex?R2">在第一个线段内，这种情况我们只需要<img alt="R2" class="mathcode" src="https://private.codecogs.com/gif.latex?R2">在区间<img alt="[L1,R1]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5BL1%2CR1%5D">之间即可，不需要管<img alt="L2" class="mathcode" src="https://private.codecogs.com/gif.latex?L2">的位置，我们在区间<img alt="[1,n]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B1%2Cn%5D">找一点 **<img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">** 作为<img alt="R1" class="mathcode" src="https://private.codecogs.com/gif.latex?R1">的概率是 <img alt="\frac{1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D"> ，然后在<img alt="R1" class="mathcode" src="https://private.codecogs.com/gif.latex?R1">的左边找一点 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 作为<img alt="L1" class="mathcode" src="https://private.codecogs.com/gif.latex?L1">概率是 <img alt="\frac{1}{i}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bi%7D"> ，<img alt="R2" class="mathcode" src="https://private.codecogs.com/gif.latex?R2">在<img alt="[L1,R1]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5BL1%2CR1%5D">之间的概率就是<img alt="\frac{i-j+1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7Bi-j&amp;plus;1%7D%7Bn%7D">，第一种情况概率就是<img alt="\frac{1}{n}\sum_{i=1}^{n}\frac{1}{i}\sum_{j=1}^{i}\frac{i-j+1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cfrac%7B1%7D%7Bi%7D%5Csum_%7Bj%3D1%7D%5E%7Bi%7D%5Cfrac%7Bi-j&amp;plus;1%7D%7Bn%7D">，化简一下<img alt="\frac{1}{n}\sum_{i=1}^{n}\frac{1}{i}\sum_{j=1}^{i}\frac{i-j+1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cfrac%7B1%7D%7Bi%7D%5Csum_%7Bj%3D1%7D%5E%7Bi%7D%5Cfrac%7Bi-j&amp;plus;1%7D%7Bn%7D"> <img alt="\rightarrow" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Crightarrow"> <img alt="\frac{1}{n}\sum_{i=1}^{n}\frac{i+1}{2n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cfrac%7Bi&amp;plus;1%7D%7B2n%7D"> <img alt="\rightarrow" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Crightarrow"> <img alt="\frac{n+3}{4n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7Bn&amp;plus;3%7D%7B4n%7D">。

第二种情况<img alt="" class="has" height="40" src="https://img-blog.csdnimg.cn/20190723160857263.png" width="129">，此时要满足<img alt="R2&gt;R1,L2&lt;=R1" class="mathcode" src="https://private.codecogs.com/gif.latex?R2%3ER1%2CL2%3C%3DR1">，同样我们在区间<img alt="[1,n]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B1%2Cn%5D">找一点 **<img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">** 作为<img alt="R1" class="mathcode" src="https://private.codecogs.com/gif.latex?R1">的概率是 <img alt="\frac{1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D"> ，我们在<img alt="R1" class="mathcode" src="https://private.codecogs.com/gif.latex?R1">右边找一点 <img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j"> 作为<img alt="R2" class="mathcode" src="https://private.codecogs.com/gif.latex?R2">概率也是<img alt="\frac{1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D">，为什么呢？设事件<img alt="A" class="mathcode" src="https://private.codecogs.com/gif.latex?A">在区间<img alt="[1,n]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B1%2Cn%5D">选择区间<img alt="[i+1,n]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Bi&amp;plus;1%2Cn%5D">，那么<img alt="P(A)=\frac{n-(i+1)+1}{n}=\frac{n-i}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?P%28A%29%3D%5Cfrac%7Bn-%28i&amp;plus;1%29&amp;plus;1%7D%7Bn%7D%3D%5Cfrac%7Bn-i%7D%7Bn%7D">，设事件<img alt="B" class="mathcode" src="https://private.codecogs.com/gif.latex?B">在区间<img alt="[i+1,n]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Bi&amp;plus;1%2Cn%5D">选一点，那么<img alt="P(B)=\frac{1}{n-(i+1)+1}=\frac{1}{n-i}" class="mathcode" src="https://private.codecogs.com/gif.latex?P%28B%29%3D%5Cfrac%7B1%7D%7Bn-%28i&amp;plus;1%29&amp;plus;1%7D%3D%5Cfrac%7B1%7D%7Bn-i%7D">，那么在事件<img alt="A" class="mathcode" src="https://private.codecogs.com/gif.latex?A">的前提下事件<img alt="B" class="mathcode" src="https://private.codecogs.com/gif.latex?B">发生的概率为<img alt="P(B|A)=\frac{1}{n-i}" class="mathcode" src="https://private.codecogs.com/gif.latex?P%28B%7CA%29%3D%5Cfrac%7B1%7D%7Bn-i%7D">，<img alt="P(AB)=P(B|A)*P(A)=\frac{n-i}{n}*\frac{1}{n-i}=\frac{1}{n}" class="mathcode" src="https://private.codecogs.com/gif.latex?P%28AB%29%3DP%28B%7CA%29*P%28A%29%3D%5Cfrac%7Bn-i%7D%7Bn%7D*%5Cfrac%7B1%7D%7Bn-i%7D%3D%5Cfrac%7B1%7D%7Bn%7D">。<img alt="L2" class="mathcode" src="https://private.codecogs.com/gif.latex?L2">可以从区间<img alt="[1,j]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B1%2Cj%5D">，但是要满足<img alt="L2&lt;=R1" class="mathcode" src="https://private.codecogs.com/gif.latex?L2%3C%3DR1">，所以只能从<img alt="[1,i]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B1%2Ci%5D">选概率为<img alt="\frac{i}{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7Bi%7D%7Bj%7D">，第二种情况概率就是<img alt="\frac{1}{n}\sum_{i=1}^{n}\frac{1}{n}\sum_{j=i+1}^{n} \frac{i}{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3Di&amp;plus;1%7D%5E%7Bn%7D%20%5Cfrac%7Bi%7D%7Bj%7D">，化简一下<img alt="\frac{1}{n}\sum_{i=1}^{n}\frac{1}{n}\sum_{j=i+1}^{n} \frac{i}{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3Di&amp;plus;1%7D%5E%7Bn%7D%20%5Cfrac%7Bi%7D%7Bj%7D"> <img alt="\rightarrow" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Crightarrow"> <img alt="\sum_{i=1}^{n}\frac{i}{n^{2}} \sum_{j=i+1}^{n} \frac{1}{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cfrac%7Bi%7D%7Bn%5E%7B2%7D%7D%20%5Csum_%7Bj%3Di&amp;plus;1%7D%5E%7Bn%7D%20%5Cfrac%7B1%7D%7Bj%7D">

第二层<img alt="for" class="mathcode" src="https://private.codecogs.com/gif.latex?for">可以用逆元前缀和优化。时间复杂度<img alt="O(n)" class="mathcode" src="https://private.codecogs.com/gif.latex?O%28n%29">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
#define ll long long
const int N = 4e6 + 7;
const int MOD = 1e9 + 7;
ll inv[N], sum[N];
int main()
{
    inv[1] = 1; sum[1] = 1;
    for(int i = 2; i &lt;= N; i++)
    {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
        sum[i] = sum[i-1] + inv[i];
    }
    int n; scanf("%d",&amp;n);
    ll ans = 0;
    for(int i = 1; i &lt;= n; i++)
    {
        ll temp = i * inv[n] % MOD * inv[n] % MOD;
        temp = (temp * (sum[n] - sum[i] + MOD) % MOD) % MOD;
        ans = (ans + temp) % MOD;
    }
    ans = (ans + (n + 3) * inv[4*n] % MOD) % MOD;
    cout &lt;&lt; ans &lt;&lt; endl;
}

```

 
