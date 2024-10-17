
--- 
title:  1148 Werewolf - Simple Version (20 分)——C/C++（枚举） 
tags: []
categories: [] 

---
Werewolf（狼人杀） is a game in which the players are partitioned into two parties: the werewolves and the human beings. Suppose that in a game,
1. player #1 said: “Player #2 is a werewolf.”;1. player #2 said: “Player#3 is a human.”;1. player #3 said: “Player #4 is a werewolf.”;1. player #4 said: “Player #5 is a human.”;1. player #5 said: “Player #4 is a human.”.
Given that there were 2 werewolves among them, at least one but not all the werewolves were lying, and there were exactly 2 liars. Can you point out the werewolves?

Now you are asked to solve a harder version of this problem: given that there were N players, with 2 werewolves among them, at least one but not all the werewolves were lying, and there were exactly 2 liars. You are supposed to point out the werewolves.

Input Specification: Each input file contains one test case. For each case, the first line gives a positive integer N (5≤N≤100). Then N lines follow and the i-th line gives the statement of the i-th player (1≤i≤N), which is represented by the index of the player with a positive sign for a human and a negative sign for a werewolf.

Output Specification: If a solution exists, print in a line in ascending order the indices of the two werewolves. The numbers must be separated by exactly one space with no extra spaces at the beginning or the end of the line. If there are more than one solution, you must output the smallest solution sequence – that is, for two sequences A=a[1],…,a[M] and B=b[1],…,b[M], if there exists 0≤k&lt;M such that a[i]=b[i] (i≤k) and a[k+1]&lt;b[k+1], then A is said to be smaller than B. In case there is no solution, simply print No Solution.

### Sample Input 1:

```
5
-2
+3
-4
+5
+4

```

### Sample Output 1:

```
1 4

```

### Sample Input 2:

```
6
+6
+3
+1
-5
-2
+4

```

### Sample Output 2 (the solution is not unique):

```
1 5

```

### Sample Input 3:

```
5
-2
-3
-4
-5
-1

```

### Sample Output 3:

```
No Solution

```

### 题目大意：

简单版狼人杀，虽然我没有感觉出哪里简单，哈哈哈 ~ _ ~ 本题主要意思是在给定的n个玩家中，有两个狼人，需要找出这两个狼人，并输出序号。每个玩家说一条语句，在这n个玩家中有2个人说谎，即一个狼人与一个农民；在上面输入中用正整数表示农民，负整数表示狼人。如果有解，在一行中按递增顺序输出 2 个狼人的编号；如果解不唯一，则输出最小序列解；若无解则输出 No Solution。

### 分析及思路：

使用v向量保存每个人说的数字（语句）；假设i，j为狼人，双重循环，i从1到n，j从i+1到n；定义lie向量保存说谎的人的下标，a向量标记是狼人还是农民，初始化为农民‘1’；k从1到n遍历v，若 **v[k] * a[abs(v[k])] &lt; 0** 说明第k个人说谎，把k放入lie向量中；遍历结束后判断，若**lie.size() == 2**（两个人说谎）且**a[lie[0]] + a[lie[1]] == 0**（一个为狼人，一个为农民）说明符合条件，输出i与j。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;cmath&gt;
#include&lt;vector&gt;
using namespace std;

int main(){<!-- -->
	int n;
	cin &gt;&gt; n;
	vector&lt;int&gt; v(n+1);//定义一个n+1长度的向量 
	for(int i = 1; i &lt;= n; i++) cin &gt;&gt; v[i];
	for(int i = 1; i &lt;= n; i++){<!-- -->
		for(int j = i + 1; j &lt;= n; j++){<!-- -->
			vector&lt;int&gt; lie, a(n + 1, 1);//a为定义一个n+1长度且值为1的向量 
			a[i] = a[j] = -1;//假设i，j为狼
			for(int k = 1; k &lt;= n; k++){<!-- -->
				if(v[k] * a[abs(v[k])] &lt; 0) lie.push_back(k);
			} 
			if(lie.size() == 2 &amp;&amp; a[lie[0]] + a[lie[1]] == 0){<!-- -->
				cout &lt;&lt; i &lt;&lt; ' ' &lt;&lt; j;
				return 0;
			}
		}
	}
	cout &lt;&lt; "No Solution";
    return 0;
} 

```

注：参考柳神思路（https://blog.csdn.net/liuchuo/article/details/82560876）
