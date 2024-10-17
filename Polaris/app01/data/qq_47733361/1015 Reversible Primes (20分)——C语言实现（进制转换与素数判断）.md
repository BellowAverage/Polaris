
--- 
title:  1015 Reversible Primes (20分)——C语言实现（进制转换与素数判断） 
tags: []
categories: [] 

---
A reversible prime in any number system is a prime whose “reverse” in that number system is also a prime. For example in the decimal system 73 is a reversible prime because its reverse 37 is also a prime.

Now given any two positive integers N (&lt; 105) and D (1 &lt; D &lt;= 10), you are supposed to tell if N is a reversible prime with radix D.

### Input Specification:

The input file consists of several test cases. Each case occupies a line which contains two integers N and D. The input is finished by a negative N.

### Output Specification:

For each test case, print in one line “Yes” if N is a reversible prime with radix D, or “No” if not.

### Sample Input:

```
73 10
23 2
23 10
-2

```

### Sample Output:

```
Yes
Yes
No

```

### 题目大意：

给定一个十进制的数n，若该数是素数并且在d进制下反转后（首尾交换），再次转换为十进制的数还是素数，则输出“Yes”；否则输出“No”。

### 思路：

把给定的数n，一直除以进制d，并保存每次的余数到数组a[ ]，进行进制转换，由于此操作后就是反转好的d进制数，因此，可直接再次转换成十进制，进行素数判断。

### 学习：

本题需要判断在-2时输出结束，采用EOF；**scanf("%d, %d", &amp;a, &amp;b);** 如果a和b都被成功读入，那么scanf的返回值就是2； 如果只有a被成功读入，返回值为1； 如果a和b都未被成功读入，返回值为0； 如果遇到错误或遇到end of file，返回值为EOF，且返回值为int型。 具体EOF用法：

### AC代码：

```
#include&lt;stdio.h&gt;
#include&lt;math.h&gt;

int Isprime(int n){<!-- -->
	if(n &lt;= 1) return 0;
	for(int i = 2; i &lt;= sqrt(n); i++){<!-- -->
		if(n % i == 0) return 0;
	}
	return 1;
}
int main(){<!-- -->
	int n, d;
	while(scanf("%d %d", &amp;n, &amp;d) == 2){<!-- -->
		if(!Isprime(n)) printf("No\n");
		else{<!-- -->
			int len = 0, a[100];
			do{<!-- -->
				a[len++] = n % d;
				n = n / d;
			}while(n != 0);
			for(int i = 0; i &lt; len; i++){<!-- -->
				n = n * d + a[i];
			}
			if(Isprime(n)) printf("Yes\n");
			else printf("No\n");
		}
	}
	return 0;
} 

```
