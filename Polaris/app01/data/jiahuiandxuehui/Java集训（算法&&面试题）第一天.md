
--- 
title:  Java集训（算法&&面试题）第一天 
tags: []
categories: [] 

---


#### 目录标题
- - - - 


## 导读

<img src="https://img-blog.csdnimg.cn/15ba3ac46ad2468a9baf91404491b97b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6IKl5a2m,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

在刚刚结束的 **每日算法&amp;面试题，大厂特训二十八天** 和 **冲刺大厂每日算法&amp;面试题，动态规划21天** 的训练中我们一起**打卡**走了过来。但是学习不能停呀，从今天开始我们开始**Java集训（算法&amp;&amp;面试题）第一天**接着卷起来。

**特别介绍**

>  
 📣小白练手专栏，适合刚入手的新人欢迎订阅 


>  
 📣python有趣练手项目里面包括了像《机器人尬聊》《恶搞程序》这样的有趣文章，可以让你快乐学python 


>  
 📣另外想学JavaWeb进厂的同学可以看看这个专栏： 


>  
 📣这是个冲刺大厂面试专栏还有算法比赛练习我们一起加油  


## 算法特训二十八天

>  
 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。 
 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。 


<img src="https://img-blog.csdnimg.cn/7fcf20df3bf0486f8194ffbb096240f9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IKl5a2m,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

```

```
示例  2：

输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8

```

```
示例 3：

输入：mat = [[5]]
输出：5

```

>  
 思路 遍历整个矩阵，如果当前坐标 (i, j)(i,j) 满足 i = ji=j 或者 i + j = n - 1i+j=n−1，就把当前的数字加入到答案中。 


```
class Solution {<!-- -->
    public int diagonalSum(int[][] mat) {<!-- -->
        int n = mat.length, sum = 0;
        for (int i = 0; i &lt; n; ++i) {<!-- -->
            for (int j = 0; j &lt; n; ++j) {<!-- -->
                if (i == j || i + j == n - 1) {<!-- -->
                    sum += mat[i][j];
                }
            }
        }
        return sum;
    }
}



```

>  
 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。 
 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。 
 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。 
 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵 <img src="https://img-blog.csdnimg.cn/870f92bb2fab4740b0abbd827eaffb0b.png" alt="在这里插入图片描述"> 


```
示例 1：


输入：mat = [[1,2],[3,4]], r = 1, c = 4
输出：[[1,2,3,4]]

```

<img src="https://img-blog.csdnimg.cn/4d5384c1e82142ff8d4fde829896fd53.png" alt="在这里插入图片描述">

```
示例 2：


输入：mat = [[1,2],[3,4]], r = 2, c = 4
输出：[[1,2],[3,4]]

```

```
class Solution {<!-- -->
    public int[][] matrixReshape(int[][] nums, int r, int c) {<!-- -->
        int m = nums.length;
        int n = nums[0].length;
        if (m * n != r * c) {<!-- -->
            return nums;
        }

        int[][] ans = new int[r][c];
        for (int x = 0; x &lt; m * n; ++x) {<!-- -->
            ans[x / c][x % c] = nums[x / n][x % n];
        }
        return ans;
    }
}



```

## 面试题

```
虚拟内存是什么，虚拟内存的原理是什么？
虚拟内存是计算机系统内存管理的一种技术。
虚拟内存有以下两个优点：
 虚拟内存地址空间是连续的，没有碎片。
 虚拟内存的最大空间就是 cup 的最大寻址空间，不受内存大小的限制，能提供比内存更
大的地址空间。
当每个进程创建的时候，内核会为每个进程分配虚拟内存，这个时候数据和代码还在磁盘上，
当运行到对应的程序时，进程去寻找页表，如果发现页表中地址没有存放在物理内存上，而是
在磁盘上，于是发生缺页异常，于是将磁盘上的数据拷贝到物理内存中并更新页表，下次再访
问该虚拟地址时就能命中了。




MySQL 为什么 InnoDB 是默认引擎
聚集索引是指数据库表行中数据的物理顺序与键值的逻辑（索引）顺序相同。一个表只能有一
个聚簇索引，因为一个表的物理顺序只有一种情况，所以，对应的聚簇索引只能有一个。聚簇
索引的叶子节点就是数据节点，既存储索引值，又在叶子节点存储行数据。
Innodb 创建表后生成的文件有：
frm:创建表的语句
idb:表里面的数据+索引文件

```

## <font color="red" size="6">点击直接资料领取</font>

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
