
--- 
title:  【LeetCode每日一题】695. 岛屿的最大面积 —— BFS算法（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了感觉会)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 若青春有张不老的脸，愿岁月待我们如初见 。 


### 题目：

给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/0f94b7eb073f48cabdc00d410e7c4484.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]] 输出：6 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

### 示例 2：

输入：grid = [[0,0,0,0,0,0,0,0]] 输出：0

### 提示：

n == grid.length m == grid[i].length 1 &lt;= m, n &lt;= 50 grid[i][j] 为 0 或 1

### 思路：

我们想知道网格中每个连通形状的面积，然后取最大值。 如果我们在一个土地上，以 44 个方向探索与之相连的每一个土地（以及与这些土地相连的土地），那么探索过的土地总数将是该连通形状的面积。 为了确保每个土地访问不超过一次，我们每次经过一块土地时，将这块土地的值置为 00。这样我们就不会多次访问同一土地。

### 代码：

```
struct xy{<!-- -->
    int x;
    int y;
}node, top;

int maxAreaOfIsland(vector&lt;vector&lt;int&gt;&gt;&amp; grid) {<!-- -->
    int ans = 0;
    int book[60][60] = {<!-- -->0};  //标记是否访问
    int tx[4] = {<!-- -->0, 1, 0, -1};
    int ty[4] = {<!-- -->-1, 0, 1, 0};
    queue&lt;xy&gt; q;
    
    for(int i = 0; i &lt; grid.size();i++){<!-- -->
        for(int j = 0; j &lt; grid[0].size(); j++){<!-- -->
            if(grid[i][j] == 1 &amp;&amp; book[i][j] == 0){<!-- -->
                int temp = 1;
                node.x = i;
                node.y = j;
                q.push(node);
                book[i][j] = 1;
                while(!q.empty()){<!-- -->
                    top = q.front();
                    q.pop();
                    
                    for(int i = 0; i &lt; 4; i++){<!-- -->
                        int x1 = top.x + tx[i];
                        int y1 = top.y + ty[i];
                        
                        if(x1 &lt; 0 || x1 &gt;= grid.size() || y1 &lt; 0 || y1 &gt;= grid[0].size() || book[x1][y1] == 1) continue;
                        
                        if(grid[x1][y1] == 1){<!-- -->
                            book[x1][y1] = 1;
                            node.x = x1;
                            node.y = y1;
                            q.push(node);
                            temp++;
                        } 
                    }
                }
                if(temp &gt; ans) ans = temp;
            }
        }
    }
    return ans;
}

```
