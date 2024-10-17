
--- 
title:  1031 Hello World for U (20分)——C/C++（字符串处理） 
tags: []
categories: [] 

---
Given any string of N (&gt;=5) characters, you are asked to form the characters into the shape of U. For example, “helloworld” can be printed as: h d e l l r lowo That is, the characters must be printed in the original order, starting top-down from the left vertical line with n1 characters, then left to right along the bottom line with n2 characters, and finally bottom-up along the vertical line with n3 characters. And more, we would like U to be as squared as possible — that is, it must be satisfied that n1 = n3 = max { k| k &lt;= n2 for all 3 &lt;= n2 &lt;= N } with n1 + n2 + n3 – 2 = N.

### Input Specification:

Each input file contains one test case. Each case contains one string with no less than 5 and no more than 80 characters in a line. The string contains no white space.

### Output Specification:

For each test case, print the input string in the shape of U as specified in the description.

### Sample Input:

```
helloworld!

```

### Sample Output:

```
h   !
e   d
l   l
lowor

```

### 题目大意：

给定一个字符串，输出漂亮的“U”型，左侧从上到下为n1，底部从最左边到最右边为n2，右侧从最下边到最上面为n3；并且要满足**n2 &gt;= n1 == n3**和**n1 + n2 + n3 = N + 2**，其中N为输入的字符串的长度。

### 思路及分析：

首先分情况讨论：设n = N + 2；即n1 + n2 + n3 = n;
1. 当n % 3 == 0 时，n1 = n2 = n3 = n / 3；1. 当n % 3 != 0 时，n1 = n3 = n / 3，n2 = n / 3 + n % 3。
找到n1，n2的值后循环输出U型格式（具体看代码）。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;

using namespace std;

int main(){<!-- -->
	int n1, n2;
	string s;
	cin &gt;&gt; s;
	int n = s.length() + 2;
	n1 = n / 3;
	n2 = n / 3 + n % 3;
	for(int i = 0; i &lt; n1-1; i++){<!-- -->
		cout &lt;&lt; s[i];
		for(int j = 0; j &lt; n2-2; j++){<!-- -->
			cout &lt;&lt; ' ';
		}
		cout &lt;&lt; s[s.length()-i-1] &lt;&lt; endl;
	}
	for(int i = n1-1; i &lt; s.length()-n1+1; i++){<!-- -->
		cout &lt;&lt; s[i];
	}
	return 0;
}

```
