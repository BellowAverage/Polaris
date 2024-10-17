
--- 
title:  2019牛客暑期多校训练营（第八场）- C - CDMA（构造） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**给你一个<img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m">，<img alt="m\in\begin{Bmatrix} 2^k|k=1,2,3...10 \end{Bmatrix}" class="mathcode" src="https://private.codecogs.com/gif.latex?m%5Cin%5Cbegin%7BBmatrix%7D%202%5Ek%7Ck%3D1%2C2%2C3...10%20%5Cend%7BBmatrix%7D">，构造一个<img alt="m*m" class="mathcode" src="https://private.codecogs.com/gif.latex?m*m">的矩阵，矩阵由<img alt="1" class="mathcode" src="https://private.codecogs.com/gif.latex?1">和<img alt="-1" class="mathcode" src="https://private.codecogs.com/gif.latex?-1">组成，并且矩阵的任意两行相乘的和为0。

**思路：**首先 <img alt="m = 2" class="mathcode" src="https://private.codecogs.com/gif.latex?m%20%3D%202"> 时的答案已经知道，考虑用 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m">构造出 <img alt="2m" class="mathcode" src="https://private.codecogs.com/gif.latex?2m"> 的解，不妨设方阵<img alt="A" class="mathcode" src="https://private.codecogs.com/gif.latex?A">为 <img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m"> 的解，那么下面这个方阵则是 <img alt="2m" class="mathcode" src="https://private.codecogs.com/gif.latex?2m"> 的一个解：<img alt="\begin{bmatrix} A &amp; A\\ A &amp; -A \end{bmatrix}" class="mathcode" src="https://private.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20A%20%26%20A%5C%5C%20A%20%26%20-A%20%5Cend%7Bbmatrix%7D">。

```
#include &lt;bits/stdc++.h&gt;
using namespace std;
const int N = 1025;
int a[N][N];
int main()
{
    int n; scanf("%d",&amp;n);
    a[1][1] = a[1][2] = a[2][1] = 1;
    a[2][2] = -1;
    for(int k = 2; k &lt; n; k *= 2)
        for(int i = 1; i &lt;= k; i++)
            for(int j = 1; j &lt;= k; j++)
                a[i][j+k] = a[i+k][j] = a[i][j], a[i+k][j+k] = -a[i][j];

    for(int i = 1; i &lt;= n; i++)
        for(int j = 1; j &lt;= n; j++)
            printf("%d%c",a[i][j], j == n ? '\n' : ' ');
}

```

 
