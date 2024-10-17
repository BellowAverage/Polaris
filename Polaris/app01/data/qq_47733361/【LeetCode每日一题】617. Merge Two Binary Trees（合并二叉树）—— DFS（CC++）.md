
--- 
title:  【LeetCode每日一题】617. Merge Two Binary Trees（合并二叉树）—— DFS（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了感觉会)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 这世界最美的风景，不过你可爱的模样！！！ 


### 题目：

给你两棵二叉树： **root1** 和 **root2** 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，**不为** null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

**注意**: 合并过程必须从两个树的根节点开始。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/34a992a9d7304734a209241bc9bd8f38.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] 输出：[3,4,5,5,4,null,7]

### 示例 2：

输入：root1 = [1], root2 = [1,2] 输出：[2,2]

### 提示：

两棵树中的节点数目在范围 [0, 2000] 内 -10^4 &lt;= Node.val &lt;= 10^4

### 思路：

可以使用**深度优先搜索**合并两个二叉树。从根节点开始同时遍历两个二叉树，并将对应的节点进行合并。 两个二叉树的对应节点可能存在以下三种情况，对于每种情况使用不同的合并方式。
- 如果两个二叉树的对应节点都为空，则合并后的二叉树的对应节点也为空；- 如果两个二叉树的对应节点只有一个为空，则合并后的二叉树的对应节点为其中的非空节点；- 如果两个二叉树的对应节点都不为空，则合并后的二叉树的对应节点的值为两个二叉树的对应节点的值之和，此时需要显性合并两个节点。
对一个节点进行合并之后，还要对该节点的左右子树分别进行合并。这是一个递归的过程。

### 代码：

```
TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {<!-- -->
    if(root1 == nullptr) return root2;
    if(root2 == nullptr) return root1;
    
    auto node = new TreeNode(root1-&gt;val + root2-&gt;val);
    
    node-&gt;left = mergeTrees(root1-&gt;left, root2-&gt;left);
    node-&gt;right = mergeTrees(root1-&gt;right, root2-&gt;right);
    
    return node;
}

```

### 知识总结：

##### 一、auto关键字

1、auto是c++程序设计语言的关键字。用于两种情况： （1）声明变量时根据初始化表达式自动推断该变量的类型 （2）声明函数时函数返回值的占位符

2、简要理解 auto可以在声明变量时根据变量初始值的类型自动为此变量选择匹配的类型。 举例：对于值x=1；既可以声明： int x=1 或 long x=1，也可以直接声明 auto x=1

##### 二、null与nullptr的区别

NULL在C++中就是0，这是因为在C++中void* 类型是不允许隐式转换成其他类型的，所以之前C++中用0来代表空指针，但是在重载整形的情况下，会出现上述的问题。所以，C++11加入了nullptr，可以保证在任何情况下都代表空指针，而不会出现上述的情况，因此，建议以后还是都用nullptr替代NULL吧，而NULL就当做0使用。

来源：力扣（LeetCode） 链接：
