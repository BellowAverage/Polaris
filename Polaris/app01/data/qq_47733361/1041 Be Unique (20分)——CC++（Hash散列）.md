
--- 
title:  1041 Be Unique (20分)——C/C++（Hash散列） 
tags: []
categories: [] 

---
Being unique is so important to people on Mars that even their lottery is designed in a unique way. The rule of winning is simple: one bets on a number chosen from [1, 104]. The first one who bets on a unique number wins. For example, if there are 7 people betting on 5 31 5 88 67 88 17, then the second one who bets on 31 wins.

### Input Specification:

Each input file contains one test case. Each case contains a line which begins with a positive integer N (&lt;=105) and then followed by N bets. The numbers are separated by a space.

### Output Specification:

For each test case, print the winning number in a line. If there is no winner, print “None” instead.

### Sample Input 1:

```
7 5 31 5 88 67 88 17

```

### Sample Output 1:

```
31

```

### Sample Input 2:

```
5 888 666 666 888 888

```

### Sample Output 2:

```
None

```

### 题目大意：

给定一个数列，寻找有且只有一个并且第一个符合此要求的数并输出；如果没有则输出“None”。

### 分析思路：

定义一个数组存储数列，另一个数组book记录数的个数；最后再遍历一遍数列，看是否有符合要求的大数字。

### AC代码：

```
#include&lt;iostream&gt;

using namespace std;

int a[100010];
int book[10010];

int main(){<!-- -->
	int n, i;
	cin &gt;&gt; n;
	for(i = 0; i &lt; n; i++){<!-- -->
		cin &gt;&gt; a[i];
		book[a[i]]++;
	}
	for(i = 0; i &lt; n; i++){<!-- -->
		if(book[a[i]] == 1) {<!-- -->
			cout &lt;&lt; a[i] &lt;&lt; endl;
			break;
		}
	}
	if(i &gt;= n) cout &lt;&lt; "None" &lt;&lt; endl;
	return 0;
} 

```
