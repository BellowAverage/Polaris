
--- 
title:  1061 Dating (20分)——C/C++（字符串处理） 
tags: []
categories: [] 

---
Sherlock Holmes received a note with some strange strings: “Let’s date! 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&amp;hgsfdk d&amp;Hyscvnm”. It took him only a minute to figure out that those strange strings are actually referring to the coded time “Thursday 14:04” — since the first common capital English letter (case sensitive) shared by the first two strings is the 4th capital letter ‘D’, representing the 4th day in a week; the second common character is the 5th capital letter ‘E’, representing the 14th hour (hence the hours from 0 to 23 in a day are represented by the numbers from 0 to 9 and the capital letters from A to N, respectively); and the English letter shared by the last two strings is ‘s’ at the 4th position, representing the 4th minute. Now given two pairs of strings, you are supposed to help Sherlock decode the dating time.

### Input Specification:

Each input file contains one test case. Each case gives 4 non-empty strings of no more than 60 characters without white space in 4 lines.

### Output Specification:

For each test case, print the decoded time in one line, in the format “DAY HH:MM”, where “DAY” is a 3-character abbreviation for the days in a week — that is, “MON” for Monday, “TUE” for Tuesday, “WED” for Wednesday, “THU” for Thursday, “FRI” for Friday, “SAT” for Saturday, and “SUN” for Sunday. It is guaranteed that the result is unique for each case.

### Sample Input:

```
3485djDkxh4hhGE 
2984akDfkkkkggEdsb 
s&amp;hgsfdk 
d&amp;Hyscvnm

```

### Sample Output:

```
THU 14:04

```

### 题目大意：

福尔摩斯收到一张字条，上面有一些奇怪的字串：我们约会吧！3485DJDKXH4HGE 2984AKDFKKKGGEDSB s&amp;hgsfdk d&amp;Hyscvnm。他只花了一分钟就发现那些奇怪的字符串实际上是指编码时间星期四14:04——因为前两个字符串共享的第一个常用大写英文字母（区分大小写）是第四个大写字母D，代表一周中的第四天；第二个常用字符是第五个大写字母E，表示第14个小时（因此，一天中从0到23的小时分别由0到9的数字和从a到N的大写字母表示）；最后两个字符串共享的英文字母在第4个位置是s，表示第4分钟。现在给两对字符串，你应该帮助夏洛克解码约会时间。以DAY HH:MM格式将解码后的时间打印在一行中，其中DAY是一周中天数的3个字符的缩写，即MON表示周一，TUE表示周二，WED表示周三，THU表示周四，FRI表示周五，SAT表示周六，SUN表示周日。

### 思路及分析：

挺简单的，遍历字符串按要求找到所需要的字母，进行转换即可，具体看代码。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;algorithm&gt;
using namespace std;

int main(){<!-- -->
	string s[8] = {<!-- -->"MON","TUE","WED","THU","FRI","SAT","SUN"};
	int day, i, hour, minute;
	string s1, s2, s3, s4;
	cin &gt;&gt; s1 &gt;&gt; s2 &gt;&gt; s3 &gt;&gt; s4;
	int len = min(s1.length(), s2.length());
	for(i = 0; i &lt; len; i++){<!-- -->
		if(s1[i] == s2[i] &amp;&amp; s1[i] &gt;= 'A' &amp;&amp; s1[i] &lt;= 'G'){<!-- -->
			day = s1[i] - 'A';
			break;
		} 
	}
	for(i = i+1; i &lt; len; i++){<!-- -->
		if(s1[i] == s2[i]){<!-- -->
			if(s1[i] &gt;= 'A' &amp;&amp; s1[i] &lt;= 'N'){<!-- -->
				hour = s1[i] - 'A' + 10;
				break;
			}
			if(s1[i] &gt;= '0' &amp;&amp; s1[i] &lt;= '9'){<!-- -->
				hour = s1[i] - '0';
				break;
			}
		} 
	}
	len = min(s3.size(), s4.size());
	for(i = 0; i &lt; len; i++){<!-- -->
		if(s3[i] == s4[i] &amp;&amp; (s3[i] &gt;= 'a' &amp;&amp; s3[i] &lt;= 'z' || s3[i] &gt;= 'A' &amp;&amp; s3[i] &lt;= 'Z')) {<!-- -->
			minute = i;	
			break;
		}
	}
	cout &lt;&lt; s[day] &lt;&lt; ' ';
	printf("%02d:%02d", hour,minute);
	return 0;
	
} 

```
