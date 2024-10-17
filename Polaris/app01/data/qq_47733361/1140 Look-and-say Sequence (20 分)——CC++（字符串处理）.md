
--- 
title:  1140 Look-and-say Sequence (20 分)——C/C++（字符串处理） 
tags: []
categories: [] 

---
Look-and-say sequence is a sequence of integers as the following:

>  
 D, D1, D111, D113, D11231, D112213111, … 


where D is in [0, 9] except 1. The (n+1)st number is a kind of description of the nth number. For example, the 2nd number means that there is one D in the 1st number, and hence it is D1; the 2nd number consists of one D (corresponding to D1) and one 1 (corresponding to 11), therefore the 3rd number is D111; or since the 4th number is D113, it consists of one D, two 1’s, and one 3, so the next number must be D11231. This definition works for D = 1 as well. Now you are supposed to calculate the Nth number in a look-and-say sequence of a given digit D.

### Input Specification:

Each input file contains one test case, which gives D (in [0, 9]) and a positive integer N (≤ 40), separated by a space.

### Output Specification:

Print in a line the Nth number in a look-and-say sequence of D.

### Sample Input:

```
1 8

```

### Sample Output:

```
1123123111

```

### 题目大意：

首先给定一个数字D，为第一个数列；第二个数列为D1，他是由前一个数列而来，D在第一个数列中有1个，则第二个数列为D1；第三个数列为D111，含义为在上一个数列中D有1个，1有1个；以此类推。

### 分析及思路：

由于第一个数列给出，因此只需要循环n-1次。使用string开始记录每个序列，双重循环，外循环遍历上一序列，内循环找寻相等个数。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
using namespace std;

int main(){<!-- -->
	int n;
	string s;
	cin &gt;&gt; s &gt;&gt; n;
	n -= 1;
	while(n--){<!-- -->
		string s1 = "";
		for(int i = 0; i &lt; s.size();) {<!-- -->
			s1 += s[i];
			int j = i;
			while(j &lt; s.size() &amp;&amp; s[i] == s[j]) j++;
			s1 += to_string(j-i);
			i = j;
		}
		s = s1;
	}
	cout &lt;&lt; s &lt;&lt; endl;
	return 0;
} 

```
