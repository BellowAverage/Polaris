
--- 
title:  1116 Come on! Let‘s C (20 分)——C/C++（数字处理） 
tags: []
categories: [] 

---
“Let’s C” is a popular and fun programming contest hosted by the College of Computer Science and Technology, Zhejiang University. Since the idea of the contest is for fun, the award rules are funny as the following:

0、 The Champion will receive a “Mystery Award” (such as a BIG collection of students’ research papers…). 1、 Those who ranked as a prime number will receive the best award – the Minions (小黄人)! 2、 Everyone else will receive chocolates. Given the final ranklist and a sequence of contestant ID’s, you are supposed to tell the corresponding awards.

### Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10^​4 ), the total number of contestants. Then N lines of the ranklist follow, each in order gives a contestant’s ID (a 4-digit number). After the ranklist, there is a positive integer K followed by K query ID’s.

### Output Specification:

For each query, print in a line ID: award where the award is Mystery Award, or Minion, or Chocolate. If the ID is not in the ranklist, print Are you kidding? instead. If the ID has been checked before, print ID: Checked.

### Sample Input:

```
6
1111
6666
8888
1234
5555
0001
6
8888
0001
1111
2222
8888
2222

```

### Sample Output:

```
8888: Minion
0001: Chocolate
1111: Mystery Award
2222: Are you kidding?
8888: Checked
2222: Are you kidding?

```

### 题目大意：

给定n个四位数ID（按排名），然后有k个查询，并按如下规则输出：
1. 第一名输出“Mystery Award”；1. 素数名次输出“Minion”；1. 其他名次输出“Chocolate”；1. 已经查询过的输出“Checked”；1. 没有该ID的输出“Are you kidding?”；
### 分析及思路：

使用map标记每个ID名次，然后按条件判断需要的内容，具体看代码，特别容易。

### AC代码：

```
#include&lt;iostream&gt;
#include&lt;string&gt;
#include&lt;map&gt;
#include&lt;cmath&gt;
using namespace std;

int Judge(int n){<!-- -->
	if(n &lt;= 1) return 0;
	for(int i = 2; i &lt;= sqrt((double)n); i++){<!-- -->
		if(n % i == 0) return 0;
	}
	return 1;
}

int main(){<!-- -->
	int n, k;
	cin &gt;&gt; n;
	map&lt;int, int&gt; p;
	for(int i = 1; i &lt;= n; i++){<!-- -->
		int temp;
		cin &gt;&gt; temp;
		p[temp] = i;
	}
	cin &gt;&gt; k;
	for(int i = 1; i &lt;= k; i++){<!-- -->
		int temp;
		cin &gt;&gt; temp;
		if(p[temp] == 1) {<!-- -->
			printf("%04d: Mystery Award\n", temp);
			p[temp] = -1;
		}else if(Judge(p[temp])) {<!-- -->
			printf("%04d: Minion\n", temp);
			p[temp] = -1;
		}else if(p[temp] == 0){<!-- -->
			printf("%04d: Are you kidding?\n", temp);
		}else if(p[temp] == -1){<!-- -->
			printf("%04d: Checked\n", temp);
		}else{<!-- -->
			printf("%04d: Chocolate\n", temp);
            p[temp] = -1;
		}
	}
	return 0;
} 

```
