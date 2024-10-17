
--- 
title:  1050 String Subtraction (20分)——C/C++（字符串处理或Hash散列） 
tags: []
categories: [] 

---
Given two strings S1 and S2, S = S1 - S2 is defined to be the remaining string after taking all the characters in S2 from S1. Your task is simply to calculate S1 - S2 for any given strings. However, it might not be that simple to do it fast.

### Input Specification:

Each input file contains one test case. Each case consists of two lines which gives S1 and S2, respectively. The string lengths of both strings are no more than 104. It is guaranteed that all the characters are visible ASCII codes and white space, and a new line character signals the end of a string.

### Output Specification:

For each test case, print S1 - S2 in one line.

### Sample Input:

```
They are students.
aeiou

```

### Sample Output:

```
Thy r stdnts.

```

### 题目大意：

给定两个字符串s1与s2，输出s1中不包含s2的部分。

### 思路及分析：

两种方法，总有一种适合你，爆搜与Hash。 方法一：字符串长度不超过10^4，所以可以直接暴力搜索，双重循环找到不在s2中的字母，加入字符串s中；时间复杂度较高为n的平方。 方法二：Hash散列，使用map标记s2，然后遍历s1，把不属于s2中的字符存入s中；时间复杂度为n。

### AC代码：

方法一：爆搜

```
#include&lt;iostream&gt;
#include&lt;string&gt;

using namespace std;

int main(){<!-- -->
	int t = 0;
	string s1, s2, s;
	getline(cin, s1);
	getline(cin, s2);
	for(int i = 0; i &lt; s1.length(); i++){<!-- -->
		int flag = 0;
		for(int j = 0; j &lt; s2.length(); j++){<!-- -->
			if(s1[i] == s2[j]){<!-- -->
				flag = 1;
				break;
			}
		}
		if(flag == 0) s = s + s1[i];
	}
	cout &lt;&lt; s &lt;&lt; endl;
	return 0;
}

```

方法二：Hash散列

```
#include&lt;iostream&gt;
#include&lt;map&gt;
#include&lt;string&gt;
using namespace std;

map&lt;char, int&gt; p;
int main(){<!-- -->
	int t = 0;
	string s1, s2, s;
	getline(cin, s1);
	getline(cin, s2);
	for(int i = 0; i &lt; s2.length(); i++){<!-- -->
		p[s2[i]] = 1;
	}
	for(int i = 0; i &lt; s1.length(); i++){<!-- -->
		if(p[s1[i]] == 0) s = s + s1[i];
	}
	cout &lt;&lt; s;
	return 0;
}

```
