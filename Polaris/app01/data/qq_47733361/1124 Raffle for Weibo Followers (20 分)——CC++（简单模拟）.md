
--- 
title:  1124 Raffle for Weibo Followers (20 分)——C/C++（简单模拟） 
tags: []
categories: [] 

---
John got a full mark on PAT. He was so happy that he decided to hold a raffle（抽奖） for his followers on Weibo – that is, he would select winners from every N followers who forwarded his post, and give away gifts. Now you are supposed to help him generate the list of winners.

```
Input Specification:

```

Each input file contains one test case. For each case, the first line gives three positive integers M (≤ 1000), N and S, being the total number of forwards, the skip number of winners, and the index of the first winner (the indices start from 1). Then M lines follow, each gives the nickname (a nonempty string of no more than 20 characters, with no white space or return) of a follower who has forwarded John’s post.

Note: it is possible that someone would forward more than once, but no one can win more than once. Hence if the current candidate of a winner has won before, we must skip him/her and consider the next one.

```
Output Specification:

```

For each case, print the list of winners in the same order as in the input, each nickname occupies a line. If there is no winner yet, print Keep going… instead.

```
Sample Input 1:

```

```
9 3 2
Imgonnawin!
PickMe
PickMeMeMeee
LookHere
Imgonnawin!
TryAgainAgain
TryAgainAgain
Imgonnawin!
TryAgainAgain

```

### Sample Output 1:

```
PickMe
Imgonnawin!
TryAgainAgain

```

### Sample Input 2:

```
2 3 5
Imgonnawin!
PickMe

```

### Sample Output 2:

```
Keep going...

```

### 题目大意：

给定一些字符串（有重复），起始为s，每隔n个位置输出一个字符串，若该字符串已经输出过，则顺位到下一位。若没有可输出的字符串则输出“Keep going…”。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;map&gt;
using namespace std;

string str[1010];
map&lt;string, int&gt; p;

int main(){<!-- -->
	int m, n, s;
	cin &gt;&gt; m &gt;&gt; n &gt;&gt; s;
	for(int i = 0; i &lt; m; i++) {<!-- -->
		cin &gt;&gt; str[i];
		p[str[i]] = 0;
	}
	if(n + s &gt; m) cout &lt;&lt; "Keep going..." &lt;&lt; endl;
	else{<!-- -->
		for(int i = s-1; i &lt; m; i += n){<!-- -->
			if(p[str[i]] == 0) {<!-- -->
				cout &lt;&lt; str[i] &lt;&lt; endl;
				p[str[i]] = 1;
			}
			else {<!-- -->
				while(p[str[i]] == 1) i++;
				cout &lt;&lt; str[i] &lt;&lt; endl;
				p[str[i]] = 1;
			}
		}
	}
	return 0;
} 

```
