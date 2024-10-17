
--- 
title:  【LeetCode每日一题】704. 二分查找 
tags: []
categories: [] 

---
### 题目：

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

### 示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9 输出: 4 解释: 9 出现在 nums 中并且下标为 4

### 示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2 输出: -1 解释: 2 不存在 nums 中因此返回 -1

### 提示：

你可以假设 nums 中的所有元素是不重复的。 n 将在 [1, 10000]之间。 nums 的每个元素都将在 [-9999, 9999]之间。

### 思路：

二分算法的模板题； mid = (right - left) / 2 + left; 当 nums[i] == target 时，返回下标mid； 当 nums[i] &gt; target 时，变换左边边界，left = left + 1； 当 nums[i] &lt; target 时，变换右边边界，right = right - 1。

### 代码：

```
int search(vector&lt;int&gt;&amp; nums, int target) {<!-- -->
	int l = 0, r = nums.size() - 1;
	while(l &lt;= r){<!-- -->
		int mid = (r - l) / 2 + l; 
		if(nums[mid] == target) return mid;
		else if(nums[mid] &gt; target) r = mid - 1;
		else l = mid + 1;
	}
	return -1;
}

```

题目链接：
