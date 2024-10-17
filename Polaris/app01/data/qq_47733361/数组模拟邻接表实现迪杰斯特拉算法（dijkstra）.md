
--- 
title:  数组模拟邻接表实现迪杰斯特拉算法（dijkstra） 
tags: []
categories: [] 

---
以题为例子来描述邻接表实现dijkstra算法。



### 题目描述

如题，给出一个有向图，请输出从某一点出发到所有点的最短路径长度。

### 输入输出样例

输入 ：

```
4 6 1
1 2 2
2 3 2
2 4 1
1 3 5
3 4 3
1 4 4

```

输出 ：

```
0 2 4 3

```

### 题目分析：

该题用邻接矩阵存储数据会导致超出内存，因此需要用邻接表存储数据。 数组模拟邻接表： head[i]表示该条边是从i开始的第head[i]条边； edge结构体存储该条边的第二个结点to，权值w，下一条边next。

### 代码：

```
#include&lt;cstdio&gt;
#include&lt;iostream&gt;
#include&lt;climits&gt;
using namespace std;
struct Edge{<!-- -->
	int to, w, next;
}edge[1000010];

int dist[10010];
int head[10010];
int book[10010];
int n, m, s, idx = 1;

void add(int a, int b, int c){<!-- -->
	edge[idx].to = b;
	edge[idx].w = c;
	edge[idx].next = head[a];
	head[a] = idx++; 
}
void dijkstra(){<!-- -->
	fill(dist, dist + 10010, INT_MAX);
	dist[s] = 0;
	int temp = s;
	while(!book[temp]){<!-- -->
		book[temp] = 1;
		for(int i = head[temp]; i != -1; i = edge[i].next){<!-- -->
			if(!book[edge[i].to] &amp;&amp; dist[edge[i].to] &gt; dist[temp] + edge[i].w){<!-- -->
				dist[edge[i].to] = dist[temp] + edge[i].w;
			}
		}
		int minn = INT_MAX;
		for(int i = 1; i &lt;= n; i++){<!-- -->
			if(!book[i] &amp;&amp; minn &gt; dist[i]){<!-- -->
				minn = dist[i];
				temp = i;
			}
		}
	}
}
int main(){<!-- -->
	fill(head, head + 10010, -1);
	scanf("%d %d %d", &amp;n, &amp;m, &amp;s);
	for(int i = 0; i &lt; m; i++){<!-- -->
		int a, b, c;
		scanf("%d %d %d", &amp;a, &amp;b, &amp;c);
		add(a, b, c);
	}
	dijkstra();
	for(int i = 1; i &lt;= n; i++){<!-- -->
		if(i &lt; n)
			printf("%d ", dist[i]);
		else
			printf("%d", dist[i]);
	}
	
	return 0;
} 

```
