
--- 
title:  1120 Friend Numbers (20 分)——C/C++（set用法） 
tags: []
categories: [] 

---
Two integers are called “friend numbers” if they share the same sum of their digits, and the sum is their “friend ID”. For example, 123 and 51 are friend numbers since 1+2+3 = 5+1 = 6, and 6 is their friend ID. Given some numbers, you are supposed to count the number of different friend ID’s among them.

### Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N. Then N positive integers are given in the next line, separated by spaces. All the numbers are less than 10^4 .

### Output Specification:

For each case, print in the first line the number of different frind ID’s among the given integers. Then in the second line, output the friend ID’s in increasing order. The numbers must be separated by exactly one space and there must be no extra space at the end of the line.

### Sample Input:

```
8
123 899 51 998 27 33 36 12

```

### Sample Output:

```
4
3 6 9 26

```

### 题目大意：

给定n个数字，并把每位数字相加的和按从小到大的顺序输出，重复的输出一个。

### 分析及思路：

使用set集合，set会自动把集合中的数据从小到大排列，并且不会有重复数字。但set中能用迭代器遍历，这样最后一个空格会非常不好掌握，可用数组中转一下。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;set&gt;
using namespace std;

int a[10010];

int main(){<!-- -->
	int n, i = 0;
	cin &gt;&gt; n;
	set&lt;int&gt; ss;
	for(int i = 0; i &lt; n; i++){<!-- -->
		int temp, sum = 0;
		cin &gt;&gt; temp;
		while(temp &gt; 0){<!-- -->
			sum += temp % 10;
			temp /= 10; 
		}
		ss.insert(sum);
	}
	cout &lt;&lt; ss.size() &lt;&lt; endl;
	set&lt;int&gt;::iterator it;              
    for(it = ss.begin(); it != ss.end(); it++) a[i++] = *it;
    for(i = 0; i &lt; ss.size() - 1; i++) cout &lt;&lt; a[i] &lt;&lt; ' ';
    cout &lt;&lt; a[i] &lt;&lt; endl;
	return 0;
}

```
