
--- 
title:  1077 Kuchiguse (20分)——C/C++（字符串处理） 
tags: []
categories: [] 

---
The Japanese language is notorious for its sentence ending particles. Personal preference of such particles can be considered as a reflection of the speaker’s personality. Such a preference is called “Kuchiguse” and is often exaggerated artistically in Anime and Manga. For example, the artificial sentence ending particle “nyan~” is often used as a stereotype for characters with a cat-like personality:

Itai nyan~ (It hurts, nyan~) Ninjin wa iyada nyan~ (I hate carrots, nyan~) Now given a few lines spoken by the same character, can you find her Kuchiguse?

### Input Specification:

Each input file contains one test case. For each case, the first line is an integer N (2&lt;=N&lt;=100). Following are N file lines of 0~256 (inclusive) characters in length, each representing a character’s spoken line. The spoken lines are case sensitive.

### Output Specification:

For each test case, print in one line the kuchiguse of the character, i.e., the longest common suffix of all N lines. If there is no such suffix, write “nai”.

### Sample Input 1:

```
3
Itai nyan~
Ninjin wa iyadanyan~
uhhh nyan~

```

### Sample Output 1:

```
nyan~

```

### Sample Input 2:

```
3
Itai!
Ninjinnwaiyada T_T
T_T

```

### Sample Output 2:

```
nai

```

### 题目大意：

给定n个字符串，输出n个字符串的最长的公共后缀，若没有公共后缀，则输出“nai”。

### 思路及分析：

若忘记了下面函数可点击。 由于是寻找后缀，因此使用reverse反转后就非常容易操作。 把第一个字符串赋值给ans并反转，然后循环判断，并在每一次循环中反转判断，把一样的字符用assign()赋值给ans，最后把ans反转输出即可。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;algorithm&gt;
using namespace std;

string s, ans;
int main(){<!-- -->
	int n, i, flag = 0;
	cin &gt;&gt; n;
	getchar();
	getline(cin, ans);
	reverse(ans.begin(), ans.end());
	for(i = 1; i &lt; n; i++){<!-- -->
		getline(cin, s);
		reverse(s.begin(), s.end());
		for(int j = 0; j &lt; s.size() &amp;&amp; j &lt; ans.size(); j++){<!-- -->
			if(s[j] != ans[j]){<!-- -->
				ans.assign(s, 0, j);
				break;
			}
		}
	}
	reverse(ans.begin(), ans.end());
	int len = ans.length();
	if(len == 0) cout &lt;&lt; "nai" &lt;&lt; endl;
	else cout &lt;&lt; ans &lt;&lt; endl;
	return 0;
} 

```
