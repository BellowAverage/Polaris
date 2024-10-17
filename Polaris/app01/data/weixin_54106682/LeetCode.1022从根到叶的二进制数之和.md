
--- 
title:  LeetCode.1022从根到叶的二进制数之和 
tags: []
categories: [] 

---
## 

**目录**













## **一、题目**

给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。

例如，如果路径为 0 -&gt; 1 -&gt; 1 -&gt; 0 -&gt; 1，那么它表示二进制数 01101，也就是 13 。 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 32 位 整数。

示例 1：

输入：root = [1,0,1,0,1,0,1] 输出：22 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22 示例 2：

输入：root = [0] 输出：0

提示：

树中的节点数在 [1, 1000] 范围内 Node.val 仅为 0 或 1 

## **二、解题思路**

二叉树问题首先应该想到递归思想；

从根节点开始遍历，递归遍历根节点的左孩子节点，根节点的右孩子节点；接着把根节点的左孩子节点看成根节点，依次递归遍历当前根节点的左孩子节点和右孩子节点；直至所有节点都被遍历完，遍历过程中，设置presum变量保存当前一条路经的数值，并设置res全局变量保存所有路径数值之和，因此当遍历至叶子节点时，res+=val；

<img alt="" height="1085" src="https://img-blog.csdnimg.cn/21d3a63df1434ff9a02b638727850f80.png" width="1200">



```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int res=0;
public:
    void dfs(TreeNode* root,int presum)
    {
        if(!root){
            return;
        }
        presum=presum*2+root-&gt;val;
        if(root-&gt;left==nullptr &amp;&amp; root-&gt;right==nullptr){
            res+=presum;
        }
        dfs(root-&gt;left,presum);
        dfs(root-&gt;right,presum);
    }
    int sumRootToLeaf(TreeNode* root) {
        dfs(root,0);
        return res;
    }
};
```

## <img alt="" height="261" src="https://img-blog.csdnimg.cn/bda83f41dc2b48d6aaba47afdc28d100.png" width="972">

 复杂度
- 时间复杂度：O(N)O(N)，NN是二叉树节点个数。- 空间复杂度：O(N)O(N)，递归使用的栈空间。
## 三、知识总结

### 1.移位运算符

presum = (val &lt;&lt; 1) | root-&gt;val等价于presum=presum*2+root-&gt;val;

移位运算符：&lt;&lt;左移运算符，相当于乘2；&gt;&gt;右移运算符，相当于除以2；

### 2.二叉树后序遍历

```
class Solution {
public:
    void postorder(TreeNode *root, vector&lt;int&gt; &amp;res) {
        if (root == nullptr) {
            return;
        }
        postorder(root-&gt;left, res);
        postorder(root-&gt;right, res);
        res.push_back(root-&gt;val);
    }

    vector&lt;int&gt; postorderTraversal(TreeNode *root) {
        vector&lt;int&gt; res;
        postorder(root, res);
        return res;
    }
};
```

## 四、总结

二叉树问题应联想到递归思想解决。
