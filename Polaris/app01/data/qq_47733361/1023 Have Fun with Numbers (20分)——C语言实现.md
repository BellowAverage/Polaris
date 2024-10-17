
--- 
title:  1023 Have Fun with Numbers (20分)——C语言实现 
tags: []
categories: [] 

---
Notice that the number 123456789 is a 9-digit number consisting exactly the numbers from 1 to 9, with no duplication. Double it we will obtain 246913578, which happens to be another 9-digit number consisting exactly the numbers from 1 to 9, only in a different permutation. Check to see the result if we double it again!

Now you are suppose to check if there are more numbers with this property. That is, double a given number with k digits, you are to tell if the resulting number consists of only a permutation of the digits in the original number.

### Input Specification:

Each input contains one test case. Each case contains one positive integer with no more than 20 digits.

### Output Specification:

For each test case, first print in a line “Yes” if doubling the input number gives a number that consists of only a permutation of the digits in the original number, or “No” if not. Then in the next line, print the doubled number.

### Sample Input:

```
1234567899

```

### Sample Output:

```
Yes
2469135798

```

### 题目大意：

给定一个数字由1—9组成的数字k，查询其翻倍后的数是否是由翻倍前的数字构成。

### 思路：

定义数组a[] = {0}, 记录原数字中单个数字的个数，如果是该数则a[i]++；翻倍后的数字变换成单个数字时a[i]–；最后判断a数组是否全为0。

### 代码：

```
#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
int main(){<!-- -->
	int flag = 0, flag1 = 0, i;
	char str[25];
	int a[25] = {<!-- -->0};
	scanf("%s", str);
	int len = strlen(str);
	for(i = len-1; i &gt;=0; i--){<!-- -->
		int temp = str[i] - '0';
		a[temp]++;
		temp = temp * 2 + flag;
		flag = 0;
		if(temp &gt;= 10){<!-- -->
			temp %= 10;
			flag = 1;
		}
		str[i] = temp + '0';
		a[temp]--;

	}
	for(i = 0; i &lt; len; i++){<!-- -->
		if(a[i] != 0){<!-- -->
			flag1 = 1;
		}
	}
	printf("%s", (flag1 == 1 || flag == 1) ? "No\n" : "Yes\n");
	if(flag == 1) 
		printf("1");
	printf("%s", str);
	return 0;
}

```
