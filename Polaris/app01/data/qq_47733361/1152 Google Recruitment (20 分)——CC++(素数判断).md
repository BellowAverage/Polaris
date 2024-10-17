
--- 
title:  1152 Google Recruitment (20 分)——C/C++(素数判断) 
tags: []
categories: [] 

---
In July 2004, Google posted on a giant billboard along Highway 101 in Silicon Valley (shown in the picture below) for recruitment. The content is super-simple, a URL consisting of the first 10-digit prime found in consecutive digits of the natural constant e. The person who could find this prime number could go to the next step in Google’s hiring process by visiting this website.

<img src="https://img-blog.csdnimg.cn/20210313175026749.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

The natural constant e is a well known transcendental number（超越数）. The first several digits are: e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921… where the 10 digits in bold are the answer to Google’s question.

Now you are asked to solve a more general problem: find the first K-digit prime in consecutive digits of any given L-digit number.

### Input Specification:

Each input file contains one test case. Each case first gives in a line two positive integers: L (≤ 1,000) and K (&lt; 10), which are the numbers of digits of the given number and the prime to be found, respectively. Then the L-digit number N is given in the next line.

### Output Specification:

For each test case, print in a line the first K-digit prime in consecutive digits of N. If such a number does not exist, output 404 instead. Note: the leading zeroes must also be counted as part of the K digits. For example, to find the 4-digit prime in 200236, 0023 is a solution. However the first digit 2 must not be treated as a solution 0002 since the leading zeroes are not in the original number.

### Sample Input 1:

```
20 5
23654987725541023819

```

### Sample Output 1:

```
49877

```

### Sample Input 2:

```
10 3
2468024680

```

### Sample Output 2:

```
404

```

### 题目大意：

给定一串n位的数字，从中找到一个k（k &lt; 10）位的数字，该数字为顺序的k位组成。

### 分析及思路：

使用string存储n位数字，遍历字符串，使用substr每次取k个字符，判断。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;cmath&gt;
using namespace std;

bool Judge(string t){<!-- -->
	int x = stoi(t);
	if(x == 0 || x == 1) return false;
	for(int i = 2; i &lt;= sqrt((double)x); i++){<!-- -->
		if(x % i == 0) return false;
	}
	return true;
}
int main(){<!-- -->
	int n, k;
	string s;
	cin &gt;&gt; n &gt;&gt; k &gt;&gt; s;
	for(int i = 0; i &lt;= n - k; i++){<!-- -->
		string t = s.substr(i, k);
		if(Judge(t)) {<!-- -->
			cout &lt;&lt; t;
			return 0;
		}
	}
	cout &lt;&lt; "404";
	return 0;
} 

```
