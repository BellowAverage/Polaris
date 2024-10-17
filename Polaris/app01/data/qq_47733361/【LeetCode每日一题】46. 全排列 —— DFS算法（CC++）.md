
--- 
title:  【LeetCode每日一题】46. 全排列 —— DFS算法（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背了下来)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 时间从来不说话，却回答了所有问题！ 


### 题目：

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

### 示例 1：

>  
 输入：nums = [1,2,3] 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 


### 示例 2：

>  
 输入：nums = [0,1] 输出：[[0,1],[1,0]] 


### 示例 3：

>  
 输入：nums = [1] 输出：[[1]] 


### 提示：

1 &lt;= nums.length &lt;= 6 -10 &lt;= nums[i] &lt;= 10 nums 中的所有整数 互不相同

### 思路：

更详细的DFS算法请看这篇：DFS详解 + 例题！！！

本文是典型的**DFS模板题**，并且是最具代表性的例题之一**排列组合类型**，没错，就是高中学的排列组合；

下面说说具体思路：首先定义几个数组，具体含义如下

>  
 vector&lt;vector&gt; ans; //记录答案 vector a; // 记录每次排列 map&lt;int, int&gt; book; //标记是否被访问 


然后循环，当 nums[i] 没有被访问过时，加入数组a，并标记已经被访问，之后进行DFS递归操作，在递归结束后要释放被访问的元素，并弹出数组a。

### 代码：

```
vector&lt;vector&lt;int&gt;&gt; ans; //记录答案
vector&lt;int&gt; a; // 记录每次排列 
map&lt;int, int&gt; book; //标记是否被访问 

void DFS(int cur, int n, vector&lt;int&gt;&amp; nums){<!-- -->
    if(cur == n){<!-- -->
        ans.push_back(a);
        return ;
    }
    for(int i = 0; i &lt; n; i++){<!-- -->
        if(book[nums[i]] == 0){<!-- -->
            a.push_back(nums[i]);
            book[nums[i]] = 1;
            DFS(cur + 1, n, nums);
            book[nums[i]] = 0;
            a.pop_back();
        }
    }
}

vector&lt;vector&lt;int&gt;&gt; permute(vector&lt;int&gt;&amp; nums) {<!-- -->
    int n = nums.size();
    DFS(0, n, nums);
    
    return ans; 
}

```

来源：力扣（LeetCode） 链接：
