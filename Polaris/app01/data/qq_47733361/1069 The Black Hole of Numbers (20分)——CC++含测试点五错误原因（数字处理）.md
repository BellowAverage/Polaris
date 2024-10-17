
--- 
title:  1069 The Black Hole of Numbers (20分)——C/C++含测试点五错误原因（数字处理） 
tags: []
categories: [] 

---
For any 4-digit integer except the ones with all the digits being the same, if we sort the digits in non-increasing order first, and then in non-decreasing order, a new number can be obtained by taking the second number from the first one. Repeat in this manner we will soon end up at the number 6174 – the “black hole” of 4-digit numbers. This number is named Kaprekar Constant.

For example, start from 6767, we’ll get:

>  
 7766 - 6677 = 1089 9810 - 0189 = 9621 9621 - 1269 = 8352 8532 - 2358 = 6174 7641 - 1467 = 6174 … … 


Given any 4-digit number, you are supposed to illustrate the way it gets into the black hole.

### Input Specification:

Each input file contains one test case which gives a positive integer N in the range (0, 10000).

### Output Specification:

If all the 4 digits of N are the same, print in one line the equation “N - N = 0000”. Else print each step of calculation in a line until 6174 comes out as the difference. All the numbers must be printed as 4-digit numbers.

### Sample Input 1:

```
6767

```

### Sample Output 1:

```
7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174

```

### Sample Input 2:

```
2222

```

### Sample Output 2:

```
2222 - 2222 = 0000

```

### 题目大意：

给定一个数字，对每位数重新排列，找到最大数与最小数，相减的差再进行如上操作，直到最后的差为6174，此为——4位数的黑洞。这个数叫做Kaprekar常数。如果四个数字相同则输出“n - n = 0000”，注意要保持四位有效数。

### 分析及思路：

把每位数字存入数组中，使用sort排序，在转换为四位数相减并输出。 测试点五错误的原因是没有考虑输入的数为6174，因此此时应使用do—while()，不管如何走一遍循环体。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;algorithm&gt;
using namespace  std;

int a[4];
bool cmp(int x, int y){<!-- -->
	return x &gt; y;
}
int main(){<!-- -->
	int n, t;
	cin &gt;&gt; n;
	t = n;
	do{<!-- -->
		int big = 0, small = 0, i = 0, flag = 1;
		while(n &gt; 0){<!-- -->
			a[i++] = n % 10;
			n /= 10;
		} 
		for(i = 1; i &lt; 4; i++){<!-- -->
			if(a[i] != a[i-1]) flag = 0;
		}
		if(flag == 1) {<!-- -->
			printf("%04d - %04d = 0000", t, t);
			break;
		}
		sort(a, a + 4);
		for(int i = 0; i &lt; 3; i++){<!-- -->
			small = (small + a[i])*10;
		}
		small += a[3];
		sort(a, a + 4, cmp);
		for(i = 0; i &lt; 3; i++){<!-- -->
			big = (big + a[i])*10;
		}
		big += a[3];
		n = big - small;
		printf("%04d - %04d = %04d\n", big, small, n);
	}while(n != 6174);
	return 0;
}

```
