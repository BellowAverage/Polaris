
--- 
title:  【LeetCode每日一题】283. 移动零——vector用法（C/C++） 
tags: []
categories: [] 

---
>  
 没有谁会踏雾而来，喜欢的风景自己去看！！！ 


### 题目：

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

### 示例 1:

输入: nums = [0,1,0,3,12] 输出: [1,3,12,0,0]

### 示例 2:

输入: nums = [0] 输出: [0]

### 提示:

1 &lt;= nums.length &lt;= 10^4 -2^31 &lt;= nums[i] &lt;= 2^31 - 1

进阶：你能尽量减少完成的操作次数吗？

### 思路：

两个方法，任你选择！！！！ 方法一：纯 vector 容器运用，看到题目说要让操作步数尽可能少，自然想到了能不能先把数组里的0全部删了，再在最后把0补回来； 那么显然是可以哒，主要利用到了remove和erase两个函数； 那么具体的做法是：先用remove删掉0，再用erase删掉容器中的无用元素，最后再压入0的个数就ok啦。

方法二：此方法就是请注意中的赋值数组方法，哈哈哈，当时没注意看，写完才发现，那也要放上呀！嘿嘿，讲思路：定义一个数组 a 复制数组nums，然后循环 **if(a[i] != 0)** 就压入nums，否则 **t++ ——统计0的个数**，最后循环压入t个0。

### 代码：

方法一：

```
void moveZeroes(vector&lt;int&gt;&amp; nums) {<!-- -->
	int n = nums.size(), t = 0;
	for(int i = 0; i &lt; n; i++){<!-- -->
		if(nums[i] == 0) t++;
	}
	remove(nums.begin(),nums.end(),0);
	nums.erase(nums.begin() + (n - t), nums.end());
	while(t--){<!-- -->
		nums.push_back(0);
	}
}

```

方法二：

```
void moveZeroes(vector&lt;int&gt;&amp; nums) {<!-- -->
	vector&lt;int&gt; a(nums);
	int t = 0;
	nums.erase(nums.begin(), nums.end());
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		if(a[i] != 0){<!-- -->
			nums.push_back(a[i]);
		} 
		else t++;
	}
	while(t--){<!-- -->
		nums.push_back(0);
	}
}

```

### 知识总结：

**remove函数:** 这个函数的作用是删除vector容器中与某个值相等的量，最后返回指向最后一个元素的迭代器。 但是执行remove之后，vector的大小和容量并不会改变！！

**erase函数：** erase可以删去容器中指定位置的元素，容器的size（大小）会改变，但是容器的容量不变。

来源：力扣（LeetCode） 链接：
