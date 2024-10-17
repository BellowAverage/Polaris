
--- 
title:  1073 Scientific Notation (20分)——C/C++（字符串处理） 
tags: []
categories: [] 

---
Scientific notation is the way that scientists easily handle very large numbers or very small numbers. The notation matches the regular expression [±][1-9]”.”[0-9]+E[±][0-9]+ which means that the integer portion has exactly one digit, there is at least one digit in the fractional portion, and the number and its exponent’s signs are always provided even when they are positive.

Now given a real number A in scientific notation, you are supposed to print A in the conventional notation while keeping all the significant figures.

### Input Specification:

Each input file contains one test case. For each case, there is one line containing the real number A in scientific notation. The number is no more than 9999 bytes in length and the exponent’s absolute value is no more than 9999.

### Output Specification:

For each test case, print in one line the input number A in the conventional notation, with all the significant figures kept, including trailing zeros,

### Sample Input 1:

```
+1.23400E-03

```

### Sample Output 1:

```
0.00123400

```

### Sample Input 2:

```
-1.2E+10

```

### Sample Output 2:

```
-12000000000

```

### 题目大意：

给定用科学计数法的格式的数字A，要求输出普通数字表示法的A，并保证所有有效位都被保留，包括末尾的0。

### 思路即分析：

在字符串处理方面string是如此的强大，忘记string的同学，可。 s1存储E之前的部分，s2存储E之后的部分，即指数部分；此时s2[0]若是‘+’，则小数点后移；s2[0]若是‘-’，则小数点前移；最后判断小数点位置即可完成。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;

using namespace std;

int main(){<!-- -->
	int i = 0;
	string s;
	cin &gt;&gt; s;
	while(s[i] != 'E'){<!-- -->
		i++;
	}
	if(s[0] == '-' )cout &lt;&lt; s[0];
	string s1 = s.substr(1, i-1);
	string s2 = s.substr(i+1);
	int len = abs(stoi(s2));
	if(s2[0] == '-'){<!-- -->
		cout &lt;&lt; "0.";
		for(int j = 0; j &lt; len-1; j++) cout &lt;&lt; 0;
		for(int j = 0; j &lt; s1.size(); j++){<!-- -->
			if(s1[j] != '.') cout &lt;&lt; s1[j];
		}
	}else{<!-- -->
		if(len &lt; s1.size()-2){<!-- -->
			int j;
			for(j = 0; j &lt; len+2; j++){<!-- -->
				if(s1[j] != '.') cout &lt;&lt; s1[j];
			}
			cout &lt;&lt; '.';
			cout &lt;&lt; s1.substr(j);
		}else{<!-- -->
			for(int j = 0; j &lt; s1.size(); j++){<!-- -->
				if(s1[j] != '.') cout &lt;&lt; s1[j];
			}
			for(int j = 0; j &lt; len-s1.size()+2; j++) cout &lt;&lt; 0;
		}
	}
} 

```
