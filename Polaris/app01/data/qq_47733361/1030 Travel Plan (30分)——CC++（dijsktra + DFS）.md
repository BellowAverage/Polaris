
--- 
title:  1030 Travel Plan (30分)——C/C++（dijsktra + DFS） 
tags: []
categories: [] 

---
A traveler’s map gives the distances between cities along the highways, together with the cost of each highway. Now you are supposed to write a program to help a traveler to decide the shortest path between his/her starting city and the destination. If such a shortest path is not unique, you are supposed to output the one with the minimum cost, which is guaranteed to be unique.

### Input Specification:

Each input file contains one test case. Each case starts with a line containing 4 positive integers N, M, S, and D, where N (≤500) is the number of cities (and hence the cities are numbered from 0 to N−1); M is the number of highways; S and D are the starting and the destination cities, respectively. Then M lines follow, each provides the information of a highway, in the format:

>  
 City1 City2 Distance Cost 


where the numbers are all integers no more than 500, and are separated by a space.

### Output Specification:

For each test case, print in one line the cities along the shortest path from the starting point to the destination, followed by the total distance and the total cost of the path. The numbers must be separated by a space and there must be no extra space at the end of output.

### Sample Input:

```
4 5 0 3
0 1 1 20
1 3 2 30
0 3 4 10
0 2 2 20
2 3 1 20

```

### Sample Output:

```
0 2 3 3 40

```

### 题目大意：

给定城市个数N、城市之间的道路数量M、起点S和终点D；输出最短路径所经过的结点、最短距离及其花费，如果最短距离有相同就输出最小花费，这个必然是不同的。

### 思路：

为求单元最短路径的算法。本题使用dijkstra算法存储路径在pre[][]数组中，并寻找最短距离。使用DFS搜索最短路径的结点及最小花费。 dijkstra算法详解+模板+例题请。

### 代码：

```
#include&lt;cstdio&gt;
#include&lt;iostream&gt;
#include&lt;climits&gt;
#include&lt;vector&gt;
using namespace std;

int N, M, S, D;
int dist[510];//dist[i]存储S到i结点的最短距离 
int book[510];//标记i结点是否访问 
int v[510][510];//存储图信息 
int cost[510][510];//存储花费信息 
vector &lt;int&gt; pre[510];//存储最短路径所经过的结点 
vector &lt;int&gt; path, temppath;
int mincost = INT_MAX;

void dijkstra(){<!-- -->
	fill(dist, dist+510, INT_MAX-1);
	int u, minx;
	pre[S].push_back(S);
	dist[S] = 0;
	for(int i = 0; i &lt; N; i++){<!-- -->
		minx = INT_MAX;
		for(int j = 0; j &lt; N; j++){<!-- -->//寻找没有被标记并且最短的路径，并记录此结点 
			if(!book[j] &amp;&amp; minx &gt; dist[j]){<!-- -->
				minx = dist[j];
				u = j;
			} 
		}
		book[u] = 1;
		for(int k = 0; k &lt; N; k++){<!-- -->
			if(!book[k] &amp;&amp; v[u][k] != INT_MAX){<!-- -->
				if(dist[k] &gt; dist[u]+v[u][k]){<!-- -->
					dist[k] = dist[u]+v[u][k];
					pre[k].clear();
					pre[k].push_back(u);
				} 
				else if(dist[k] == dist[u]+v[u][k]){<!-- -->
					pre[k].push_back(u);
				}
			}
		}
	}
}
void dfs(int v){<!-- -->
	temppath.push_back(v);
	if(S == v){<!-- -->
		int tempcost = 0;
		for(int i = temppath.size()-1; i &gt;= 1; i--){<!-- -->
			int id = temppath[i], id1 = temppath[i-1];
			tempcost += cost[id][id1];
		}
		if(mincost &gt; tempcost){<!-- -->
			mincost = tempcost;
			path = temppath;
		}
		temppath.pop_back();
		return;
	}
	for(int i = 0; i &lt; pre[v].size(); i++){<!-- -->
		dfs(pre[v][i]);
	}
	temppath.pop_back();
}
int main(){<!-- -->
	scanf("%d %d %d %d", &amp;N, &amp;M, &amp;S, &amp;D);
	fill(v[0], v[0]+510*510, INT_MAX-1);
	for(int i = 0; i &lt; M; i++){<!-- -->
		int a, b, c, d;
		scanf("%d %d %d %d", &amp;a, &amp;b, &amp;c, &amp;d);
		v[a][b] = v[b][a] = min(v[a][b], c);
		cost[a][b] = cost[b][a] = d;
	}
	dijkstra();
	dfs(D);
	for(int i = path.size()-1; i &gt;= 0; i--){<!-- -->
		printf("%d ", path[i]);
	}
	printf("%d %d", dist[D], mincost);
	return 0;
}

```
