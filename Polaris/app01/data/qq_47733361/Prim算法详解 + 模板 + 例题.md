
--- 
title:  Prim算法详解 + 模板 + 例题 
tags: []
categories: [] 

---
>  
 普里姆算法（Prim算法），图论中的一种算法，可在加权连通图里搜索最小生成树。意即由此算法搜索到的边子集所构成的树中，不但包括了连通图里的所有顶点（英语：Vertex (graph theory)），且其所有边的权值之和亦为最小。该算法于1930年由捷克数学家沃伊捷赫·亚尔尼克（英语：Vojtěch Jarník）发现；并在1957年由美国计算机科学家罗伯特·普里姆（英语：Robert C. Prim）独立发现；1959年，艾兹格·迪科斯彻再次发现了该算法。因此，在某些场合，普里姆算法又被称为DJP算法、亚尔尼克算法或普里姆－亚尔尼克算法。 ——百度百科 


### 一、基本思想

（1）输入：一个加权连通图，顶点集V，边集E； （2）初始化：可选择任意结点**x**为起始点，将起始点x加入顶点集V1 = {x}，边集为空E1 = { }； （3）重复下列操作，直到所有顶点全部加入顶点集V1中，即V1 = V： a. 在集合E中寻找权值最小的边&lt;u, v&gt;，其中结点u在集合V1中，而结点v不在集合V1中，并且v∈V（如果存在多条符合要求的边，任选其一即可）； b. 将结点v加入顶点集V1中，将边&lt;u，v&gt;加入边集E1中； （4）输出：通过顶点集V1与边集E1打印最小生成树及其他相关操作。

### 二、时间复杂度

使用**邻接矩阵**存储图信息时间复杂度为：O(n^2) 使用**邻接表**存储图信息时间复杂度为：O(m*logn) 其中n为顶点数，m为图的边数。

### 三、图解

<img src="https://img-blog.csdnimg.cn/20201216090440146.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20201216090512882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20201216090542361.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 四、模板

prim算法需要用到两个主要数组：

>  
 int lowcost[N]; //lowcost[i]表示i到集合最近的距离 int mst[N]; //mst[i]表示对应i为终点的边的起点 


```
int Prim(){<!-- -->
	fill(lowcost, lowcost + N, INT_MAX);
	fill(mst, mst + N, 1);
	for(int i = 2; i &lt;= n; i++){<!-- -->
		lowcost[i] = v[1][i];
	}
	int u, minn, sum = 0;
	for(int i = 2; i &lt;= n; i++){<!-- -->
		minn = INT_MAX;
		for(int j = 2; j &lt;= n; j++){<!-- -->
			if(lowcost[j] != 0 &amp;&amp; minn &gt; lowcost[j]){<!-- -->
				minn = lowcost[j];
				u = j;
			}
		}
		sum += minn;
		lowcost[u] = 0;
		for(int k = 2; k &lt;= n; k++){<!-- -->
			if(v[u][k] &lt; lowcost[k]){<!-- -->
				lowcost[k] = v[u][k];
				mst[k] = u;
			}
		}
	}
	return sum;
}

```

### 五、例题

1、模板题  AC代码：

```
#include&lt;iostream&gt;
#include&lt;climits&gt;
#include&lt;algorithm&gt;

using namespace std;
const int N = 5010;
int n, m;
int v[N][N]; 
int lowcost[N];//存储距离集合最近的距离 
int mst[N];

int Prim(){<!-- -->
	fill(lowcost, lowcost + N, INT_MAX);
	fill(mst, mst + N, 1);
	for(int i = 2; i &lt;= n; i++){<!-- -->
		lowcost[i] = v[1][i];
	}
	int minn, u, sum = 0;
	for(int j = 2; j &lt;= n; j++){<!-- -->
		minn = INT_MAX;
		for(int i = 2; i &lt;= n; i++){<!-- -->
			if(lowcost[i] != 0 &amp;&amp; minn &gt; lowcost[i]){<!-- -->
				minn = lowcost[i];
				u = i;
			}
		}
		sum += minn;
		lowcost[u] = 0;
		for(int i = 2; i &lt;= n; i++){<!-- -->
			if(lowcost[i] &gt; v[u][i]){<!-- -->
				lowcost[i] = v[u][i];
				mst[i] = u;
			}
		}
	}
	return sum;
}
int main(){<!-- -->
	fill(v[0], v[0] + N*N, INT_MAX);
	cin &gt;&gt; n &gt;&gt; m;
	for(int i = 1; i &lt;= m; i++){<!-- -->
		int a, b, c;
		cin &gt;&gt; a &gt;&gt; b &gt;&gt; c;
		v[a][b] = v[b][a] = min(v[a][b], c);
	}
	int ans = Prim();
	cout &lt;&lt; ans &lt;&lt; endl;
	return 0;
} 

```
