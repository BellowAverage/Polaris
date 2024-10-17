
--- 
title:  【LeetCode每日一题】994. 腐烂的橘子 —— BFS算法（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 “我见众生皆无意，唯有见你动了情 ” 


### 题目：

在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
- 值 0 代表空单元格；- 值 1 代表新鲜橘子；- 值 2 代表腐烂的橘子。- 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/c823018d34e14130a4117f1452670f40.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

输入：grid = [[2,1,1],[1,1,0],[0,1,1]] 输出：4

### 示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]] 输出：-1 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

### 示例 3：

输入：grid = [[0,2]] 输出：0 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

### 提示：

m == grid.length n == grid[i].length 1 &lt;= m, n &lt;= 10 grid[i][j] 仅为 0、1 或 2

### 思路：

由题目我们可以知道每分钟每个腐烂的橘子都会使上下左右相邻的新鲜橘子腐烂，这其实是一个**模拟广度优先搜索的过程**。所谓广度优先搜索，就是从起点出发，**每次都尝试访问同一层的节点**，如果同一层都访问完了，再访问下一层，最后广度优先搜索找到的路径就是从起点开始的最短合法路径。 观察到对于所有的腐烂橘子，其实它们在广度优先搜索上是等价于同一层的节点的。

假设这些腐烂橘子刚开始是新鲜的，而有一个腐烂橘子会在下一秒把这些橘子都变腐烂，而这个腐烂橘子刚开始在的时间是 −1 ，那么按照广度优先搜索的算法，下一分钟也就是第 0 分钟的时候，这个腐烂橘子会把它们都变成腐烂橘子，然后继续向外拓展，所以其实这些腐烂橘子是同一层的节点。那么在广度优先搜索的时候，我们将这些腐烂橘子都放进队列里进行广度优先搜索即可，最后每个新鲜橘子被腐烂的最短时间其实是以这个超级源点的腐烂橘子为起点的广度优先搜索得到的结果。

### 代码：

```
struct xy{<!-- -->  //记录结点
    int x;
    int y;
}node, top;

int orangesRotting(vector&lt;vector&lt;int&gt;&gt;&amp; grid) {<!-- -->
    int m = grid.size(), n = grid[0].size();
    vector&lt;vector&lt;int&gt;&gt; book(m, vector&lt;int&gt; (n)); //标记是否被访问
    int ans = 0, cnt = 0; // cnt统计好橘子的个数 
    int tx[4] = {<!-- -->0, 1, 0, -1};
    int ty[4] = {<!-- -->-1, 0, 1, 0};
    queue&lt;xy&gt; q;
    
    for(int i = 0; i &lt; m; i++){<!-- --> //将所有坏橘子放入队列
        for(int j = 0; j &lt; n; j++){<!-- -->
            if(grid[i][j] == 2){<!-- -->
                node.x = i;
                node.y = j;
                q.push(node);
                book[i][j] = 1;
            }else if(grid[i][j] == 1){<!-- -->
                cnt++;
            }
        }
    }
    
    while(!q.empty() &amp;&amp; cnt &gt; 0){<!-- -->
        int size = q.size();
        int cnt1 = 0;
        ans++;
        
        for(int i = 0; i &lt; size; i++){<!-- --> //层次遍历
            top = q.front();
            q.pop();
            
            for(int t = 0; t &lt; 4; t++){<!-- --> //访问四个方向
                int x1 = top.x + tx[t];
                int y1 = top.y + ty[t];
                
                if(x1 &gt;= 0 &amp;&amp; x1 &lt; m &amp;&amp; y1 &gt;=0 &amp;&amp; y1 &lt; n &amp;&amp; !book[x1][y1]){<!-- -->
                    if(grid[x1][y1] == 1){<!-- -->
                        grid[x1][y1] = 2; 
                        node.x = x1;
                        node.y = y1;
                        q.push(node);
                        book[x1][y1] = 1;
                        cnt1++;
                    }
                }
            }
        }
        cnt -= cnt1;
    }
    if(cnt != 0) return -1;
 else return ans;
}

```

链接：
