
--- 
title:  1136 A Delayed Palindrome (20 分)——C/C++（高精度算法） 
tags: []
categories: [] 

---
Consider a positive integer N written in standard notation with k+1 digits ai as ak…a1a0 with 0 &lt;= ai &lt; 10 for all i and ak &gt; 0. Then N is palindromic if and only if ai = ak-i for all i. Zero is written 0 and is also palindromic by definition.

Non-palindromic numbers can be paired with palindromic ones via a series of operations. First, the non-palindromic number is reversed and the result is added to the original number. If the result is not a palindromic number, this is repeated until it gives a palindromic number. Such number is called a delayed palindrome. (Quoted from https://en.wikipedia.org/wiki/Palindromic_number)

Given any positive integer, you are supposed to find its paired palindromic number.

### Input Specification:

Each input file contains one test case which gives a positive integer no more than 1000 digits.

### Output Specification:

For each test case, print line by line the process of finding the palindromic number. The format of each line is the following: A + B = C where A is the original number, B is the reversed A, and C is their sum. A starts being the input number, and this process ends until C becomes a palindromic number — in this case we print in the last line “C is a palindromic number.”; or if a palindromic number cannot be found in 10 iterations, print “Not found in 10 iterations.” instead.

### Sample Input 1:

```
97152
Sample Output 1:
97152 + 25179 = 122331
122331 + 133221 = 255552
255552 is a palindromic number.

```

### Sample Input 2:

```
196

```

### Sample Output 2:

```
196 + 691 = 887
887 + 788 = 1675
1675 + 5761 = 7436
7436 + 6347 = 13783
13783 + 38731 = 52514
52514 + 41525 = 94039
94039 + 93049 = 187088
187088 + 880781 = 1067869
1067869 + 9687601 = 10755470
10755470 + 07455701 = 18211171
Not found in 10 iterations.

```

### 题目大意：

给定一个数字n，把该数字与其倒置相加求和，若和为回文数，则输出“n is a palindromic number.”；否则继续把和赋值给n，继续以上规则求和，直到10次之后还没有回文数，输出“Not found in 10 iterations.”。

### 分析及思路：

若该数等于其倒置数，则其为回文数； 倒置可用reverse()函数直接翻转； 由于是不超过1000位的正整数，则应使用高精度算法。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;algorithm&gt;
#include&lt;string&gt;

using namespace std;

string add(string n, string n1){<!-- -->
	string sum;
	int carry = 0;//标记是否进位 
	for(int i = 0; i &lt; n.size(); i++){<!-- -->
		int num = n[i] - '0' + n1[i] - '0' + carry;
		carry = 0;
		if(num &gt;= 10){<!-- -->
			carry = 1;
			num %= 10;
		} 
		sum += num + '0';
	}
	if(carry == 1) sum += '1';
	reverse(sum.begin(), sum.end());
	return sum;
}
int main(){<!-- -->
	int i = 0;
	string n, sum = "";
	cin &gt;&gt; n;
	while(i &lt; 10){<!-- -->
        sum.clear();
		string n1 = n;
		reverse(n1.begin(), n1.end());
		if(n == n1) break;
		sum = add(n, n1);
		cout &lt;&lt; n &lt;&lt; " + " &lt;&lt; n1 &lt;&lt; " = " &lt;&lt; sum &lt;&lt; endl;
		n = sum;
		i++;
	}
	if(i &lt; 10) cout &lt;&lt; n &lt;&lt; " is a palindromic number." &lt;&lt; endl;
	else cout &lt;&lt; "Not found in 10 iterations." &lt;&lt; endl;
	return 0;
} 

```
