
--- 
title:  1092 To Buy or Not to Buy (20分)——C/C++（Hash与map用法） 
tags: []
categories: [] 

---
Eva would like to make a string of beads with her favorite colors so she went to a small shop to buy some beads. There were many colorful strings of beads. However the owner of the shop would only sell the strings in whole pieces. Hence Eva must check whether a string in the shop contains all the beads she needs. She now comes to you for help: if the answer is Yes, please tell her the number of extra beads she has to buy; or if the answer is No, please tell her the number of beads missing from the string.

For the sake of simplicity, let’s use the characters in the ranges [0-9], [a-z], and [A-Z] to represent the colors. For example, the 3rd string in Figure 1 is the one that Eva would like to make. Then the 1st string is okay since it contains all the necessary beads with 8 extra ones; yet the 2nd one is not since there is no black bead and one less red bead. <img src="https://img-blog.csdnimg.cn/20210118210234394.png" alt="在这里插入图片描述">

figbuy.jpg

Figure 1

### Input Specification:

Each input file contains one test case. Each case gives in two lines the strings of no more than 1000 beads which belong to the shop owner and Eva, respectively.

### Output Specification:

For each test case, print your answer in one line. If the answer is Yes, then also output the number of extra beads Eva has to buy; or if the answer is No, then also output the number of beads missing from the string. There must be exactly 1 space between the answer and the number.

### Sample Input 1:

```
ppRYYGrrYBR2258
YrR8RrY

```

### Sample Output 1:

```
Yes 8

```

### Sample Input 2:

```
ppRYYGrrYB225
YrR8RrY

```

### Sample Output 2:

```
No 2

```

### 题目大意：

第一个字符串为商店中所有的颜色，第二个字符串是所需要的颜色，如果可以从商店中找到第二个字符串所有的颜色，则输出商店中多出的颜色的个数；否则输出缺少的颜色的个数。

### 思路及分析：

使用map标记第一个字符串s，统计所有字符个数；之后减去第二个字符串s1，即进行p[s1[i]]- - 操作；最后遍历第一个字符串，统计大于0的字符的个数，然后遍历s1统计小于0的字符的个数。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;map&gt;

using namespace std;
map&lt;char, int&gt; p;
int main(){<!-- -->
	int t = 0, t1 = 0;
	string s, s1;
	cin &gt;&gt; s &gt;&gt; s1;
	for(int i = 0; i &lt; s.size(); i++) p[s[i]]++;
	for(int i = 0; i &lt; s1.size(); i++) p[s1[i]]--;
	for(int i = 0; i &lt; s.size(); i++){<!-- -->
		if(p[s[i]] &gt; 0) t1 += p[s[i]], p[s[i]] = 0;
	}
	for(int i = 0; i &lt; s1.size(); i++){<!-- -->
		if(p[s1[i]] &lt; 0) t += p[s1[i]], p[s1[i]] = 0;
	}
	if(t != 0) {<!-- -->
		cout &lt;&lt; "No" &lt;&lt; ' ' &lt;&lt; abs(t) &lt;&lt; endl;
		return 0;
	}else{<!-- -->
		cout &lt;&lt; "Yes" &lt;&lt; ' ' &lt;&lt; t1 &lt;&lt; endl;
	}
	return 0;
} 

```
