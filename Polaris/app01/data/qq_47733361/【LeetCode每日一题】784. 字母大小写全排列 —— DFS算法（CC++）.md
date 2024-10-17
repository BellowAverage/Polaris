
--- 
title:  【LeetCode每日一题】784. 字母大小写全排列 —— DFS算法（C/C++） 
tags: []
categories: [] 

---
##### 写在前面：

大家好！我是一看就会(只是背下来了)一写就废的菜鸡，欢迎大家来与我一起进行刷题学习！！！下面先上鸡汤（本菜鸡），刷题前怎么能没有鸡汤与美女呢，嘎嘎嘎 ^ - ^

>  
 月亮在悄悄的变圆，事情在悄悄的变好！！！ 


### 题目：

给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。

### 示例 1：

>  
 输入：s = “a1b2” 输出：[“a1b2”, “a1B2”, “A1b2”, “A1B2”] 


### 示例 2:

>  
 输入: s = “3z4” 输出: [“3z4”,“3Z4”] 


### 提示:

1 &lt;= s.length &lt;= 12 s 由小写英文字母、大写英文字母和数字组成

### 思路：

更详细的DFS算法请看这篇：DFS详解 + 例题！！！ 若不明白 isdigit() 函数请看这篇：

本文是典型的DFS算法题，具体思路如下： 首先使用 isdigit() 函数判断，若为数字则直接进行递归，即不用管；若为字母则使用 tolower() 函数——变为小写，然后递归，再使用 toupper() 函数——变为大写，递归。

### 代码：

```
vector&lt;string&gt; ans; //记录最终结果

void DFS(int cur, string s){<!-- -->
	if(cur == s.size()){<!-- -->
		ans.push_back(s);
		return ;
	}
	
	if(isdigit(s[cur])){<!-- -->
		DFS(cur + 1, s); 
	}else{<!-- -->
		s[cur] = tolower(s[cur]);
		DFS(cur + 1, s);
		s[cur] = toupper(s[cur]);
		DFS(cur + 1, s); 
	}
} 

vector&lt;string&gt; letterCasePermutation(string s) {<!-- -->
	DFS(0, s);
	
	return ans; 
}

```

### 知识总结：

**tolower() 函数**：大写字母变为小写字母，小写字母不变；

**toupper() 函数**：小写字母变为大写字母，大写字母不变。

来源：力扣（LeetCode） 链接：
