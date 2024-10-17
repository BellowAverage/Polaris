
--- 
title:  1104 Sum of Number Segments (20 分)——C语言（排列组合）含测试点二错误原因 
tags: []
categories: [] 

---
Given a sequence of positive numbers, a segment is defined to be a consecutive subsequence. For example, given the sequence { 0.1, 0.2, 0.3, 0.4 }, we have 10 segments: (0.1) (0.1, 0.2) (0.1, 0.2, 0.3) (0.1, 0.2, 0.3, 0.4) (0.2) (0.2, 0.3) (0.2, 0.3, 0.4) (0.3) (0.3, 0.4) and (0.4).

Now given a sequence, you are supposed to find the sum of all the numbers in all the segments. For the previous example, the sum of all the 10 segments is 0.1 + 0.3 + 0.6 + 1.0 + 0.2 + 0.5 + 0.9 + 0.3 + 0.7 + 0.4 = 5.0.

### Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N, the size of the sequence which is no more than 10^5. The next line contains N positive numbers in the sequence, each no more than 1.0, separated by a space.

### Output Specification:

For each test case, print in one line the sum of all the numbers in all the segments, accurate up to 2 decimal places.

### Sample Input:

```
4
0.1 0.2 0.3 0.4

```

### Sample Output:

```
5.00

```

### 题目大意：

求一个序列的所有子序列和。

### 分析及思路：

主要公式：**temp * i * (n - i + 1)** <img src="https://img-blog.csdnimg.cn/20210220155715481.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210220155730526.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 由上面两组数据很容易得到公式 temp * i * (n - i + 1)。

### 错误：

测试点二一直不对，最后终于明白是因为double类型，在N比较大时，double类型的值多次累加导致的精度误差。 原因就在于计算机内部的加减乘除运算是通过加法器二进制运算来完成的，而二进制是无法准确表示一个浮点数的，只能在有限的精度内逼近这个值。 因此我们可以通过把一些数据扩大一定的倍数进行运算，最后再除去扩大的倍数。

### AC代码：

```
#include&lt;stdio.h&gt;

int main(){<!-- -->
	int n;
	long long sum = 0;
	scanf("%d", &amp;n);
	for(int i = 1; i &lt;= n; i++){<!-- -->
		double temp;
		scanf("%lf", &amp;temp);
		sum += (long long)(temp * 1000) * i * (n + 1 - i);
	}
	printf("%.2f", sum/1000.0);
	return 0;
} 

```
