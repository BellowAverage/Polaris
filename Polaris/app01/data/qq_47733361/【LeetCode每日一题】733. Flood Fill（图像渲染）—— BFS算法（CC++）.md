
--- 
title:  【LeetCode每日一题】733. Flood Fill（图像渲染）—— BFS算法（C/C++） 
tags: []
categories: [] 

---
>  
 与其喜欢深夜的梦，不如爱上凌晨的风！ 


### 题目：

有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。

你也被给予三个整数 sr , sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。

为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。

最后返回 经过上色渲染后的图像 。

### 示例 1:

<img src="https://img-blog.csdnimg.cn/46833227ffed438a872f4368942a296a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2 输出: [[2,2,2],[2,2,0],[2,0,1]] 解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。 注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。

### 示例 2:

输入: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2 输出: [[2,2,2],[2,2,2]]

### 提示:

m == image.length n == image[i].length 1 &lt;= m, n &lt;= 50 0 &lt;= image[i][j], newColor &lt; 2^16 0 &lt;= sr &lt; m 0 &lt;= sc &lt; n

### 思路：

典型BFS模板题呀，套模板就ok了！ 浅说一下思路：^ - ^我们从给定的起点开始，进行广度优先搜索。每次搜索到一个方格时，如果其与初始位置的方格颜色相同，就将该方格加入队列，并将该方格的颜色更新，以防止重复入队。

注：因为初始位置的颜色会被修改，所以我们需要保存初始位置的颜色，以便于之后的更新操作。

### 代码：

```
struct xy{<!-- -->
	int x;
	int y;
}node, top;

vector&lt;vector&lt;int&gt;&gt; floodFill(vector&lt;vector&lt;int&gt;&gt;&amp; image, int sr, int sc, int newColor) {<!-- -->
    int book[100][100] = {<!-- -->0};
    int tx[4] = {<!-- -->0, 1, 0, -1};
    int ty[4] = {<!-- -->-1, 0, 1, 0};
    int flag = image[sr][sc];
    book[sr][sc] = 1;
    image[sr][sc] = newColor;
    queue&lt;xy&gt; q;
    node.x = sr;
    node.y = sc;
    q.push(node);
    
    while(!q.empty()){<!-- -->
        top = q.front();
        q.pop();
        
        for(int i = 0; i &lt; 4; i++){<!-- -->
            int x1 = top.x + tx[i];
            int y1 = top.y + ty[i];
            
            if(x1 &lt; 0 || x1 &gt;= image.size() || y1 &lt; 0 || y1 &gt;= image[0].size() || book[x1][y1] == 1) continue;
            
            if(image[x1][y1] == flag){<!-- -->
                node.x = x1;
                node.y = y1;
                q.push(node);
                image[x1][y1] = newColor;
                book[x1][y1] = 1;
            }
        }
    }
    return image;
}

```

链接：
