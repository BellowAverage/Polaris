
--- 
title:  1054 The Dominant Color (20分)——C/C++（map用法与Hash散列） 
tags: []
categories: [] 

---
Behind the scenes in the computer’s memory, color is always talked about as a series of 24 bits of information for each pixel. In an image, the color with the largest proportional area is called the dominant color. A strictly dominant color takes more than half of the total area. Now given an image of resolution M by N (for example, 800×600), you are supposed to point out the strictly dominant color.

### Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive numbers: M (≤800) and N (≤600) which are the resolutions of the image. Then N lines follow, each contains M digital colors in the range [0,224). It is guaranteed that the strictly dominant color exists for each input image. All the numbers in a line are separated by a space.

### Output Specification:

For each test case, simply print the dominant color in a line.

### Sample Input:

```
5 3
0 0 255 16777215 24
24 24 0 0 24
24 0 24 24 24

```

### Sample Output:

```
24

```

### 题目大意：

给定m*n个数，找到其中出现次数为一半以上的数字并输出。

### 思路及分析：

使用map可以不用考虑数组开的大小。用map记录数字出现的个数，然后在遍历一遍输入的数字，找到出现一半以上的数字输出即可。本质还是Hash散列。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;map&gt;
using namespace std;

int a[480010];
map&lt;int, int&gt; p;

int main(){<!-- -->
	int n, m;
	cin &gt;&gt; m &gt;&gt; n;
	for(int i = 0; i &lt; m*n; i++){<!-- -->
		cin &gt;&gt; a[i];
		p[a[i]]++;
	}
	for(int i = 0; i &lt; m*n; i++){<!-- -->
		if(p[a[i]] &gt;= m*n/2){<!-- -->
			cout &lt;&lt; a[i];
			break;
		}
	}
	return 0;
}

```
