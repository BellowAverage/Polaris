
--- 
title:  【LeetCode每日一题】2. 两数相加 —— 模拟 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 人生如路，只要有耐心。走着走着，便会出现繁华的风景。 


### 题目：

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

### 示例 1：

<img src="https://img-blog.csdnimg.cn/40d1272c136b444dbedf4af789599e9a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAMjHlsoHooqvov6vnp4PlpLQ=,size_13,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 输入：l1 = [2,4,3], l2 = [5,6,4] 输出：[7,0,8] 解释：342 + 465 = 807. 


### 示例 2：

>  
 输入：l1 = [0], l2 = [0] 输出：[0] 


### 示例 3：

>  
 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] 输出：[8,9,9,9,0,0,0,1] 


### 提示：

每个链表中的节点数在范围 [1, 100] 内 0 &lt;= Node.val &lt;= 9 题目数据保证列表表示的数字不含前导零

### 思路：

由于输入的两个链表都是逆序存储数字的位数的，因此两个链表中同一位置的数字可以直接相加。

我们同时遍历两个链表，逐位计算它们的和，并与当前位置的进位值相加。好啦，具体看代码，本题注释非常详细！！！

### 代码：

```
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {<!-- -->
    ListNode* h = nullptr, *t = nullptr;
    int x = 0;
    
    while(l1 != nullptr || l2 != nullptr){<!-- -->
        int x1 = l1 ? l1-&gt;val : 0;
        int x2 = l2 ? l2-&gt;val : 0;
        x = x1 + x2 + x;
        if(h == nullptr){<!-- --> //头结点为空 
            h = t = new ListNode(x % 10); //新建结点并赋值 
        }else{<!-- -->
            t-&gt;next = new ListNode(x % 10); //新建结点并赋值
            t = t-&gt;next;
        }
        if(l1) l1 = l1-&gt;next; //l1不为空结点指针后移 
        if(l2) l2 = l2-&gt;next; //l2不为空结点指针后移
        x = x / 10; 
    }
    if(x &gt; 0){<!-- -->//说明最后一个结点数值相加大于10，需要进位 
        t-&gt;next = new ListNode(x);
        t = t-&gt;next;
    }
    return h;
}

```
