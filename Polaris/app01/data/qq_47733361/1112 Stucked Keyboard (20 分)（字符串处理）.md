
--- 
title:  1112 Stucked Keyboard (20 分)（字符串处理） 
tags: []
categories: [] 

---
On a broken keyboard, some of the keys are always stucked. So when you type some sentences, the characters corresponding to those keys will appear repeatedly on screen for k times.

Now given a resulting string on screen, you are supposed to list all the possible stucked keys, and the original string.

Notice that there might be some characters that are typed repeatedly. The stucked key will always repeat output for a fixed k times whenever it is pressed. For example, when k=3, from the string thiiis iiisss a teeeeeest we know that the keys i and e might be stucked, but s is not even though it appears repeatedly sometimes. The original string could be this isss a teest.

### Input Specification:

Each input file contains one test case. For each case, the 1st line gives a positive integer k (1&lt;k≤100) which is the output repeating times of a stucked key. The 2nd line contains the resulting string on screen, which consists of no more than 1000 characters from {a-z}, {0-9} and _. It is guaranteed that the string is non-empty.

### Output Specification:

For each test case, print in one line the possible stucked keys, in the order of being detected. Make sure that each key is printed once only. Then in the next line print the original string. It is guaranteed that there is at least one stucked key.

### Sample Input:

```
3
caseee1__thiiis_iiisss_a_teeeeeest

```

### Sample Output:

```
ei
case1__this_isss_a_teest

```

### 题目大意：

键盘坏了，有一些键按一次该字符会出现3次，找出坏的键并按输入的字符串的顺序输出，最后并输出正确的字符串。

### 思路：

遍历字符串，使用map标记该字符对应的键位的好坏。 使用cnt标记一个字符连续出现的次数，若cnt % k == 0，则该键损坏。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;set&gt;
#include&lt;map&gt;
using namespace std;

bool book[256]; // 标记键的好坏 
int main(){<!-- -->
	int k, cnt = 0;
	string s, s1;
	set&lt;char&gt; a;
	map&lt;char, bool&gt; m;
	cin &gt;&gt; k &gt;&gt; s;
    char str = ' ';//初始化
	s += ' ';
	for(int i = 0; i &lt; s.length(); i++){<!-- -->
		if(s[i] == str) cnt++;
		else{<!-- -->
			if(cnt % k != 0) {<!-- -->
				book[str] = true; //若不等于0，则键为好键 
			} 
			cnt = 1;
		}
		if(i != s.length()-1) m[s[i]] = (cnt % k == 0);
        str = s[i];
	}
	for(int i = 0; i &lt; s.length()-1; i++){<!-- -->
		if(book[s[i]] == true) m[s[i]] = false;
	}
	for(int i = 0; i &lt; s.length()-1; i++){<!-- -->
		if(m[s[i]] &amp;&amp; a.find(s[i]) == a.end()){<!-- -->
			cout &lt;&lt; s[i];
			a.insert(s[i]);
		}
	}
	cout &lt;&lt; endl;
	for(int i = 0; i &lt; s.length()-1; i++){<!-- -->
		cout &lt;&lt; s[i];
		if(m[s[i]]) i = i + k - 1;
	}
	return 0;
}

```
