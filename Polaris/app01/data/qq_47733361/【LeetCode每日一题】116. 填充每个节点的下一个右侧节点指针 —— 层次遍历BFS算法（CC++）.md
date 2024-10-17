
--- 
title:  【LeetCode每日一题】116. 填充每个节点的下一个右侧节点指针 —— 层次遍历BFS算法（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 我的喜欢写在云里，从此整个世界都是你！！！ 


### 题目：

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

```
struct Node {<!-- -->
    int val;
    Node *left;
    Node *right;
    Node *next;
}

```

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/3b843b613e9242b08377533f73c80d0f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

输入：root = [1,2,3,4,5,6,7] 输出：[1,#,2,3,#,4,5,6,7,#] 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，‘#’ 标志着每一层的结束。

### 示例 2:

输入：root = [] 输出：[]

### 提示：

树中节点的数量在 [0, 2^12 - 1] 范围内 -1000 &lt;= node.val &lt;= 1000

### 进阶：

你只能使用常量级额外空间。 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

### 思路：

题目本身希望我们将二叉树的每一层节点都连接起来形成一个链表。因此直观的做法我们可以对二叉树进行层次遍历，在层次遍历的过程中将我们将二叉树每一层的节点拿出来遍历并连接。

**层次遍历基于广度优先搜索**，它与广度优先搜索的不同之处在于，广度优先搜索每次只会取出一个节点来拓展，而层次遍历会每次将队列中的所有元素都拿出来拓展，这样能保证每次从队列中拿出来遍历的元素都是属于同一层的，因此我们可以在遍历的过程中修改每个节点的 **next** 指针，同时拓展下一层的新队列。

### 代码：

```
Node* connect(Node* root) {<!-- -->
    if(root == nullptr) return root;
    
    queue&lt;Node*&gt; q;
    q.push(root);
    
    while(!q.empty()){<!-- -->
        int size = q.size();
        
        for(int i = 0; i &lt; size; i++){<!-- -->
            Node* t = q.front();
            q.pop();
            
            if(i &lt; size - 1) t-&gt;next = q.front();
            
            if(t-&gt;left != nullptr) q.push(t-&gt;left);
            if(t-&gt;right != nullptr) q.push(t-&gt;right);
        }
    }
    return root;
}

```

来源：力扣（LeetCode） 链接：
