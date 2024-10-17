
--- 
title:  1058 A+B in Hogwarts (20分)——C语言（进位） 
tags: []
categories: [] 

---
If you are a fan of Harry Potter, you would know the world of magic has its own currency system – as Hagrid explained it to Harry, “Seventeen silver Sickles to a Galleon and twenty-nine Knuts to a Sickle, it’s easy enough.” Your job is to write a program to compute A+B where A and B are given in the standard form of Galleon.Sickle.Knut (Galleon is an integer in [0,10^7], Sickle is an integer in [0, 17), and Knut is an integer in [0, 29)).

### Input Specification:

Each input file contains one test case which occupies a line with A and B in the standard form, separated by one space.

### Output Specification:

For each test case you should output the sum of A and B in one line, with the same format as the input.

### Sample Input:

```
3.2.1 10.16.27

```

### Sample Output:

```
14.1.28

```

### 题目大意：

给定两个a.b.c形式的数列，c的范围为[0，29），b的范围为[0,17），a的范围为[0,10^7]；让两个数列相加进行进位，输出相加后的数列。

### 思路及分析：

先判断c，如果c1+c2大于等于26，b+1，c = （c1+c2）%26；同理在判断b，最后输出相加的数。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;cstdio&gt;
using namespace std;

int main(){<!-- -->
	int a1, b1, c1;
	int a2, b2, c2;
	int a, b, c;
	scanf("%d.%d.%d %d.%d.%d", &amp;a1, &amp;b1, &amp;c1, &amp;a2, &amp;b2, &amp;c2);
	if(c1 + c2 &gt;= 29){<!-- -->
		c = c1 + c2 - 29;
		b1++;
	} else{<!-- -->
		c = c1 + c2;
	}
	if(b1 + b2 &gt;= 17){<!-- -->
		b = b1 + b2 - 17;
		a1++;
	}else{<!-- -->
		b = b1 + b2;
	} 
	a = a1 + a2;
	printf("%d.%d.%d", a, b, c);
	return 0;
} 

```
