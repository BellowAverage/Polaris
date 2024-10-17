
--- 
title:  1042 Shuffling Machine (20分)——C/C++（简单模拟） 
tags: []
categories: [] 

---
Shuffling is a procedure used to randomize a deck of playing cards. Because standard shuffling techniques are seen as weak, and in order to avoid “inside jobs” where employees collaborate with gamblers by performing inadequate shuffles, many casinos employ automatic shuffling machines. Your task is to simulate a shuffling machine.

The machine shuffles a deck of 54 cards according to a given random order and repeats for a given number of times. It is assumed that the initial status of a card deck is in the following order:

>  
 S1, S2, …, S13, H1, H2, …, H13, C1, C2, …, C13, D1, D2, …, D13, J1, J2 


where “S” stands for “Spade”, “H” for “Heart”, “C” for “Club”, “D” for “Diamond”, and “J” for “Joker”. A given order is a permutation of distinct integers in [1, 54]. If the number at the i-th position is j, it means to move the card from position i to position j. For example, suppose we only have 5 cards: S3, H5, C1, D13 and J2. Given a shuffling order {4, 2, 5, 3, 1}, the result will be: J2, H5, D13, S3, C1. If we are to repeat the shuffling again, the result will be: C1, H5, S3, J2, D13.

### Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer K (&lt;= 20) which is the number of repeat times. Then the next line contains the given order. All the numbers in a line are separated by a space.

### Output Specification:

For each test case, print the shuffling results in one line. All the cards are separated by a space, and there must be no extra space at the end of the line.

### Sample Input:

```
2
36 52 37 38 3 39 40 53 54 41 11 12 13 42 43 44 2 4 23 24 25 26 27 6 7 8 48 49 50 51 9 10 14 15 16 5 17 18 19 1 20 21 22 28 29 30 31 32 33 34 35 45 46 47

```

### Sample Output:

```
S7 C11 C10 C12 S1 H7 H8 H9 D8 D9 S11 S12 S13 D10 D11 D12 S3 S4 S6 S10 H1 H2 C13 D2 D3 D4 H6 H3 D13 J1 J2 C1 C2 C3 C4 D1 S5 H5 H11 H12 C6 C7 C8 C9 S2 S8 S9 H10 D5 D6 D7 H4 H13 C5

```

### 题目大意：

初始字符串在题目中已给出。给定转换次数k，与需要转换的位置，输出k次转换后的字符串。

### 分析：

本题为简单模拟。定义一个二维数组初始化为初始字符串；然后使用双重循环，外循环为转换次数，内循环经过**s1[a[i]] = s1[i]**；变换，s1数组即为变换后的字符串。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
using namespace std;

int a[54];
int main(){<!-- -->
	string s[55] = {<!-- -->"",
		"S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13",
	    "H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13",
		"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13",
		"D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13",
		"J1","J2"};
	int k;
	cin &gt;&gt; k;
	for(int i = 1; i &lt;= 54; i++){<!-- -->
		cin &gt;&gt; a[i];
	}
	for(int j = 1; j &lt;= k; j++){<!-- -->
		string s1[100] = {<!-- -->""};
		for(int i = 1; i &lt;= 54; i++){<!-- -->
			s1[a[i]] = s[i];
		}
		for(int i = 1; i &lt;= 54; i++){<!-- -->
			s[i] = s1[i];
		}
	}
	for(int i = 1; i &lt;= 53; i++){<!-- -->
		cout &lt;&lt; s[i] &lt;&lt; ' ';
	}
	cout &lt;&lt; s[54] &lt;&lt; endl;
	return 0;
}

```
