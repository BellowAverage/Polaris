
--- 
title:  【LeetCode每日一题】542. 01 矩阵 —— BFS算法（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 我写了三行字，爱要藏在哪里才合适，你又能否一眼便知。 


### 题目：

给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/42fe3df927da42d3af33cb486f6c31c6.png#pic_center" alt="在这里插入图片描述">

>  
 输入：mat = [[0,0,0],[0,1,0],[0,0,0]] 输出：[[0,0,0],[0,1,0],[0,0,0]] 


### 示例 2：

<img src="https://img-blog.csdnimg.cn/ec6ead5a83c3471aa09b70f7648580fe.png#pic_center" alt="在这里插入图片描述">

>  
 输入：mat = [[0,0,0],[0,1,0],[1,1,1]] 输出：[[0,0,0],[0,1,0],[1,2,1]] 


### 提示：

n == mat.length m == mat[i].length 1 &lt;= m, n &lt;= 10^4 1 &lt;= m * n &lt;= 10^4 mat[i][j] is either 0 or 1. mat 中至少有一个 0

### 思路：

对于矩阵中的每一个元素，如果它的值为 0，那么离它最近的 0 就是它自己。如果它的值为 1，那么我们就需要找出离它最近的 0，并且返回这个距离值。 我们可以从 0 的位置开始进行 广度优先搜索。广度优先搜索可以找到从起点到其余所有点的 最短距离，因此如果我们从 0 开始搜索，每次搜索到一个 1，就可以得到 0 到这个 1 的最短距离，也就离这个 1 最近的 0 的距离了（因为矩阵中只有一个 0）。

### 代码：

```
struct xy{<!-- -->  //存位置
    int x;
    int y;
}node, top;

vector&lt;vector&lt;int&gt;&gt; updateMatrix(vector&lt;vector&lt;int&gt;&gt;&amp; mat) {<!-- -->
    int n = mat.size(), m = mat[0].size(); 
    vector&lt;vector&lt;int&gt;&gt; a(n, vector&lt;int&gt; (m));  //记录变换后的数组
    vector&lt;vector&lt;int&gt;&gt; book(n, vector&lt;int&gt; (m)); //标记是否被访问
    int tx[4] = {<!-- -->0, 1, 0, -1};  //进行方向上的操作
    int ty[4] = {<!-- -->-1, 0, 1, 0};
    queue&lt;xy&gt; q;
    
    for(int i = 0; i &lt; n; i++){<!-- -->  //先将所有0填入数组
        for(int j = 0; j &lt; m; j++){<!-- -->
            if(mat[i][j] == 0){<!-- -->
                node.x = i;
                node.y = j;
                q.push(node);
                book[i][j] = 1;
            }
        }
    }
    
    while(!q.empty()){<!-- -->  //bfs模板
        top = q.front();
        q.pop();
        
        for(int t = 0; t &lt; 4; t++){<!-- -->
            int x1 = top.x + tx[t];
            int y1 = top.y + ty[t];
            
            if(x1 &gt;= 0 &amp;&amp; x1 &lt; n &amp;&amp; y1 &gt;=0 &amp;&amp; y1 &lt; m &amp;&amp; !book[x1][y1]){<!-- -->
                a[x1][y1] = a[top.x][top.y] + 1;
                node.x = x1;
                node.y = y1;
                q.push(node);
                book[x1][y1] = 1;
            }
        }
    }
    return a;
}

```

来源：力扣（LeetCode） 链接：
