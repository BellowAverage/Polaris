
--- 
title:  【LeetCode每日一题】35. 搜索插入位置——二分算法（C/C++） 
tags: []
categories: [] 

---
### 题目：

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

### 示例 1:

输入: nums = [1,3,5,6], target = 5 输出: 2

### 示例 2:

输入: nums = [1,3,5,6], target = 2 输出: 1

### 示例 3:

输入: nums = [1,3,5,6], target = 7 输出: 4

### 提示:

1 &lt;= nums.length &lt;= 104 -104 &lt;= nums[i] &lt;= 104 nums 为 无重复元素 的 升序 排列数组 -104 &lt;= target &lt;= 104

### 思路：

**二分算法**的模板题； mid = (right - left) / 2 + left; 当 nums[i] == target 时，返回下标mid； 当 nums[i] &gt; target 时，变换左边边界，left = left + 1； 当 nums[i] &lt; target 时，变换右边边界，right = right - 1。

当没有时返回插入位置，即**左边界就是要插入的位置**。

### 代码：

```
int searchInsert(vector&lt;int&gt;&amp; nums, int target) {<!-- -->
	int l = 0, r = nums.size() - 1;
	while(l &lt;= r){<!-- -->
		int mid = (r - l) / 2 + l; 
		if(nums[mid] == target) return mid;
		else if(nums[mid] &gt; target) r = mid - 1;
		else l = mid + 1;
	}
	return l;
}

```

来源：力扣（LeetCode） 链接：
