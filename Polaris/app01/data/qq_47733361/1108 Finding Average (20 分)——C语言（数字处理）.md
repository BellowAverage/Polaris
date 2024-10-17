
--- 
title:  1108 Finding Average (20 分)——C语言（数字处理） 
tags: []
categories: [] 

---
The basic task is simple: given N real numbers, you are supposed to calculate their average. But what makes it complicated is that some of the input numbers might not be legal. A legal input is a real number in [−1000,1000] and is accurate up to no more than 2 decimal places. When you calculate the average, those illegal numbers must not be counted in.

### Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤100). Then N numbers are given in the next line, separated by one space.

### Output Specification:

For each illegal input number, print in a line ERROR: X is not a legal number where X is the input. Then finally print in a line the result: The average of K numbers is Y where K is the number of legal inputs and Y is their average, accurate to 2 decimal places. In case the average cannot be calculated, output Undefined instead of Y. In case K is only 1, output The average of 1 number is Y instead.

### Sample Input 1:

```
7
5 -3.2 aaa 9999 2.3.4 7.123 2.35

```

### Sample Output 1:

```
ERROR: aaa is not a legal number
ERROR: 9999 is not a legal number
ERROR: 2.3.4 is not a legal number
ERROR: 7.123 is not a legal number
The average of 3 numbers is 1.38

```

### Sample Input 2:

```
2
aaa -9999

```

### Sample Output 2:

```
ERROR: aaa is not a legal number
ERROR: -9999 is not a legal number
The average of 0 numbers is Undefined

```

### 题目大意：

给定一些字符，寻找符合题目要求的数字，并求平均数。 要求：小数位数不超过两位；必须是数字；绝对值小于等于1000。

### 分析及思路:

本题使用sscanf和sprintf超级方便。 sscanf() – 从一个字符串中读进与指定格式相符的数据。 sprintf() – 字符串格式化命令，主要功能是把格式化的数据写入某个字符串中。

```
sscanf(s1, "%lf", &amp;temp); //若是数字，则把s1转换为double型赋值给temp

```

```
sprintf(s2, "%.2f", temp); //把temp变为有两位小数点的数字，并放入s2中

```

如果在s1的长度下s1==s2，则满足前两个要求。

### AC代码：

```
#include&lt;stdio.h&gt;
#include&lt;string.h&gt;

int main(){<!-- -->
	int n, cnt = 0;
	double sum = 0, temp = 0;
	scanf("%d", &amp;n);
	for(int i = 0; i &lt; n; i++){<!-- -->
		char s1[50], s2[50];
		int flag = 0;
		scanf("%s", s1);
		sscanf(s1, "%lf", &amp;temp);
		sprintf(s2, "%.2f", temp);
		for(int j = 0; j &lt; strlen(s1); j++){<!-- -->
			if(s1[j] != s2[j]) flag = 1;
		}
		if(flag || temp &lt; -1000 || temp &gt; 1000){<!-- -->
			printf("ERROR: %s is not a legal number\n", s1);
		}else{<!-- -->
			cnt++;
			sum += temp;
		}
	}
	if(cnt == 1) printf("The average of 1 number is %.2f\n", sum);
    else if(cnt &gt; 1) printf("The average of %d numbers is %.2f\n", cnt, sum/cnt);
	else printf("The average of 0 numbers is Undefined\n");
	return 0;
} 

```
