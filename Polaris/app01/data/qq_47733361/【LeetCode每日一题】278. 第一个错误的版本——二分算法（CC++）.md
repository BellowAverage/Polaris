
--- 
title:  【LeetCode每日一题】278. 第一个错误的版本——二分算法（C/C++） 
tags: []
categories: [] 

---
### 题目：

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, …, n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

### 示例 1：

输入：n = 5, bad = 4 输出：4 解释： 调用 isBadVersion(3) -&gt; false 调用 isBadVersion(5) -&gt; true 调用 isBadVersion(4) -&gt; true 所以，4 是第一个错误的版本。

### 示例 2：

输入：n = 1, bad = 1 输出：1

### 提示：

1 &lt;= bad &lt;= n &lt;= 2^31 - 1

### 思路：

二分算法的模板题； mid = (right - left) / 2 + left； 如果 !isBadVersion(mid-1) &amp;&amp; isBadVersion(mid)，返回下标mid； 如果 !isBadVersion(mid) ，变换左边边界，left = left + 1； 如果 isBadVersion(mid) ，变换右边边界，right = right - 1。

### 代码：

```
int firstBadVersion(int n) {<!-- -->
   int l = 1, r = n;
   while(l &lt;= r){<!-- -->
       int mid = (r - l) / 2 + l;
       if(!isBadVersion(mid-1) &amp;&amp; isBadVersion(mid)) return mid;
       if(!isBadVersion(mid)) l = mid + 1;
       else r = mid - 1;
   }
   return 0;
}

```

来源：力扣（LeetCode） 链接：
