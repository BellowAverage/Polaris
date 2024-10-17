
--- 
title:  【LeetCode每日一题】206. 反转链表 —— 递归（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背了下来)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 人总是兴高采烈的去奔赴一场未知的喜剧！ 


### 题目：

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/94c0a502daed4292a42d8a79e4cfcf62.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 输入：head = [1,2,3,4,5] 输出：[5,4,3,2,1] 


### 示例 2：

<img src="https://img-blog.csdnimg.cn/246c8eff2dbf4828a24f737443f230a9.png" alt="在这里插入图片描述">

>  
 输入：head = [1,2] 输出：[2,1] 


### 示例 3：

>  
 输入：head = [] 输出：[] 


### 提示：

链表中节点的数目范围是 [0, 5000] -5000 &lt;= Node.val &lt;= 5000

### 进阶：

链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

### 思路：

反转链表，只要屁股连头，头连屁股就好啦 ^ - ^qaq；

在遍历列表时，将当前节点的 next 指针改为指向前一个元素。由于节点没有引用其上一个节点，因此必须事先存储其前一个元素。在更改引用之前，还需要另一个指针来存储下一个节点。不要忘记在最后返回新的头引用！

### 代码：

```
ListNode* reverseList(ListNode* head) {<!-- -->
    ListNode* q = nullptr;
    ListNode* p = head;
    
    while(p){<!-- -->
        ListNode* t = p-&gt;next;
        p-&gt;next = q;
        q = p;
        p = t;
    }
    return q;
}

```
