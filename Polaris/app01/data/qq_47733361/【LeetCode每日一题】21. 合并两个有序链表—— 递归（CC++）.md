
--- 
title:  【LeetCode每日一题】21. 合并两个有序链表—— 递归（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背了下来)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 时间从来不说话，却回答了所有问题！ 


### 题目：

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/7e7a6f42b7cf414ab24cf65182bb59fe.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 输入：l1 = [1,2,4], l2 = [1,3,4] 输出：[1,1,2,3,4,4] 


### 示例 2：

>  
 输入：l1 = [], l2 = [] 输出：[] 


### 示例 3：

>  
 输入：l1 = [], l2 = [0] 输出：[0] 


### 提示：

两个链表的节点数目范围是 [0, 50] -100 &lt;= Node.val &lt;= 100 list1 和 list2 均按 非递减顺序 排列

### 思路：

我们直接将以上递归过程建模，同时需要考虑边界情况。

如果 list1 或者 list2 一开始就是空链表 ，那么没有任何操作需要合并，所以我们只需要返回非空链表。否则，我们要判断 list1 和 list2 哪一个链表的头节点的值更小，然后递归地决定下一个添加到结果里的节点。如果两个链表有一个为空，递归结束。

### 代码：

```
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {<!-- -->
    if(list1 == nullptr){<!-- -->
        return list2;
    }else if(list2 == nullptr){<!-- -->
        return list1;
    }else if(list1-&gt;val &gt; list2-&gt;val){<!-- -->
        list2-&gt;next = mergeTwoLists(list1, list2-&gt;next);
        return list2;
    }else{<!-- -->
        list1-&gt;next = mergeTwoLists(list1-&gt;next, list2);
        return list1;
    }
}

```

来源：力扣（LeetCode） 链接：
