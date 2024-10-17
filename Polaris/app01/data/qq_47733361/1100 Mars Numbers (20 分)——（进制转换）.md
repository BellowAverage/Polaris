
--- 
title:  1100 Mars Numbers (20 分)——（进制转换） 
tags: []
categories: [] 

---
People on Mars count their numbers with base 13:

Zero on Earth is called “tret” on Mars. The numbers 1 to 12 on Earth is called “jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec” on Mars, respectively. For the next higher digit, Mars people name the 12 numbers as “tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou”, respectively. For examples, the number 29 on Earth is called “hel mar” on Mars; and “elo nov” on Mars corresponds to 115 on Earth. In order to help communication between people from these two planets, you are supposed to write a program for mutual translation between Earth and Mars number systems.

### Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (&lt;100). Then N lines follow, each contains a number in [0, 169), given either in the form of an Earth number, or that of Mars.

### Output Specification:

For each number, print in a line the corresponding number in the other language.

### Sample Input:

```
4
29
5
elo nov
tam

```

### Sample Output:

```
hel mar
may
115
13

```

### 题目大意：

把十进制数转换为火星上的13进制，把13进制转换为10进制。

### 思路及分析：

先判断输入的数字是是10进制，还是13进制，然后分情况讨论转换，具体看代码。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
using namespace std;

int main(){<!-- -->
	string s[13] = {<!-- -->"tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"};
	string s1[13] = {<!-- -->"","tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"}; 
	int n;
	cin &gt;&gt; n;
	getchar();
	for(int i = 0; i &lt; n; i++){<!-- -->
		int t;
		if(scanf("%d", &amp;t) == 1){<!-- -->
			if(t &lt; 13) cout &lt;&lt; s[t] &lt;&lt; endl;
			else if(t % 13 == 0) cout &lt;&lt; s1[t/13] &lt;&lt; endl;
			else cout &lt;&lt; s1[t/13] &lt;&lt; ' ' &lt;&lt; s[t%13] &lt;&lt; endl; 
		}else{<!-- -->
			string str;
			getline(cin, str);
			int j = 0, ans = 0;
			while(str[j] != ' ' &amp;&amp; j != str.size()) j++;
			if(j != str.size()) {<!-- -->
				string t = str.substr(0, j);
				string t1 = str.substr(j+1);
				for(j = 1; j &lt;= 13; j++) {<!-- -->
					if(t == s1[j]) {<!-- -->
						ans = j * 13;
						break;
					}
				}
				for(j = 1; j &lt;= 13; j++){<!-- -->
					if(t1 == s[j]) {<!-- -->
						ans += j;
						break;
					}
				}
			}else{<!-- -->
				for(j = 0; j &lt;= 13; j++){<!-- -->
					if(str == s[j]) {<!-- -->
						ans = j;
						break;
					}
				}
				for(j = 1; j &lt;= 13; j++){<!-- -->
	            	if(str == s1[j]){<!-- -->
	            		ans = j*13;
	            		break;
					}
				}
			}
			cout &lt;&lt; ans &lt;&lt; endl;
		}
	}
	return 0;
}

```
