
--- 
title:  1084 Broken Keyboard (20分)——C/C++(Hash散列) 
tags: []
categories: [] 

---
On a broken keyboard, some of the keys are worn out. So when you type some sentences, the characters corresponding to those keys will not appear on screen.

Now given a string that you are supposed to type, and the string that you actually type out, please list those keys which are for sure worn out.

### Input Specification:

Each input file contains one test case. For each case, the 1st line contains the original string, and the 2nd line contains the typed-out string. Each string contains no more than 80 characters which are either English letters [A-Z] (case insensitive), digital numbers [0-9], or _ (representing the space). It is guaranteed that both strings are non-empty.

### Output Specification:

For each test case, print in one line the keys that are worn out, in the order of being detected. The English letters must be capitalized. Each worn out key must be printed once only. It is guaranteed that there is at least one worn out key.

### Sample Input:

```
7_This_is_a_test
_hs_s_a_es

```

### Sample Output:

```
7TI

```

### 题目大意：

给定两个字符串，找到没有在第二个字符串中出现的字符，并按输入顺序输出没有出现的字符。

### 思路及分析：

本质为Hash散列。使用map标记第二个字符串中的字符，然后遍历第一个字符串，把没有在第二个字符串中出现的字符放入ans中，然后遍历ans输出不重复的字符。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;map&gt;
using namespace std;

map&lt;char, int&gt; p, p1;

int main(){<!-- -->
	string s, s1, ans;
	cin &gt;&gt; s &gt;&gt; s1;
	for(int i = 0; i &lt; s1.length(); i++){<!-- -->
		p[s1[i]]++;
	}
	for(int i = 0; i &lt; s.length(); i++){<!-- -->
		if(p[s[i]] == 0) ans += s[i];
	}
	for(int i = 0; i &lt; ans.length(); i++){<!-- -->
		if(ans[i] &gt;= 'a' &amp;&amp; ans[i] &lt;= 'z') ans[i] -= 32;
		if(p1[ans[i]]) continue;
		cout &lt;&lt; ans[i];
		p1[ans[i]]++;
	}
	return 0;
}

```
