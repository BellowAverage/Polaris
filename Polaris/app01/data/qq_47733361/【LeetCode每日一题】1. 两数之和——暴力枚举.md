
--- 
title:  【LeetCode每日一题】1. 两数之和——暴力枚举 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 因为有悔，所以披星戴月;因为有梦，所以奋不顾身。 


### 题目：

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

### 示例 1：

>  
 输入：nums = [2,7,11,15], target = 9 输出：[0,1] 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。 


### 示例 2：

>  
 输入：nums = [3,2,4], target = 6 输出：[1,2] 


### 示例 3：

>  
 输入：nums = [3,3], target = 6 输出：[0,1] 


### 提示：

2 &lt;= nums.length &lt;= 10<sup>4</sup> -10<sup>9</sup>&lt;= nums[i] &lt;= 10<sup>9</sup> -10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup> 只会存在一个有效答案

### 思路：

最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。

当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配。而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。

### 代码：

```
vector&lt;int&gt; twoSum(vector&lt;int&gt;&amp; nums, int target) {<!-- -->
    vector&lt;int&gt; a;
    for(int i = 0; i &lt; nums.size(); i++){<!-- -->
        for(int j = i + 1; j &lt; nums.size(); j++){<!-- -->
            if(nums[i] + nums[j] == target){<!-- -->
                a.push_back(i);
                a.push_back(j);
                return a;
            }
        }
    }
    return a;
}

```

来源：力扣（LeetCode） 链接：
