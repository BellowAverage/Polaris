
--- 
title:  【LeetCode每日一题】977. 有序数组的平方——Sort排序 
tags: []
categories: [] 

---
### 题目：

给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

### 示例 1：

输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100] 排序后，数组变为 [0,1,9,16,100]

### 示例 2：

输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]

### 提示：

1 &lt;= nums.length &lt;= 10^4 -10^4 &lt;= nums[i] &lt;= 10 ^4 nums 已按 非递减顺序 排序

### 思路：

首先定义一个数组，使用循环进行开平方，然后调用Sort函数进行排序，最后返回数组；

注：若不会使用 **sort函数** 可以看这篇 。

### 代码：

```
vector&lt;int&gt; sortedSquares(vector&lt;int&gt;&amp; nums) {<!-- -->
	vector&lt;int&gt; a;
	for(int i = 0; i &lt; nums.size(); i++){<!-- -->
		int temp = pow(nums[i], 2);
		a.push_back(temp);
	}
	sort(a.begin(), a.end());
	return a;
}

```

来源：力扣（LeetCode） 链接：
