
--- 
title:  【LeetCode每日一题】567. Permutation in String (字符串的排列) —— 滑动窗口 (C/C++) 
tags: []
categories: [] 

---
>  
 人总是兴高采烈的去奔赴一场未知的喜剧！ 


### 题目：

给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

### 示例 1：

输入：s1 = “ab” s2 = “eidbaooo” 输出：true 解释：s2 包含 s1 的排列之一 (“ba”).

### 示例 2：

输入：s1= “ab” s2 = “eidboaoo” 输出：false

### 提示：

1 &lt;= s1.length, s2.length &lt;= 10^4 s1 和 s2 仅包含小写字母

### 思路：

先解释两个概念：子串与子序列 子串：**必须连续** 子序列：**可以不连续** 本题是说s1 的排列之一是 s2 的 子串 ；这样的话若s1的长度大于s2错误，返回false； 由于排列不会改变字符串中每个字符的个数，所以只有当两个字符串每个字符的个数均相等时，一个字符串才是另一个字符串的排列； 我们可以定义两个数组a与b，分别用来记录s1与s2中字符的个数； 由于需要遍历的子串长度均为 s1的长度n，我们可以使用一个固定长度为n的**滑动窗口**来维护记录s2字符个数的数组b：滑动窗口每向右滑动一次，就多统计一次进入窗口的字符，少统计一次离开窗口的字符。然后，判断 数组a与b是否相等，若相等说明s1是s2的子串之一。

### 代码：

```
bool checkInclusion(string s1, string s2) {<!-- -->
	int n = s1.size();
	if(n &gt; s2.size()) return false;
	
	vector&lt;int&gt; a(26), b(26);
	
	for(int i = 0; i &lt; n; i++){<!-- -->
		a[s1[i] - 'a']++;
		b[s2[i] - 'a']++;
	}
	
	if(a == b){<!-- -->
		return true;
	}
	
    for(int i = n; i &lt; s2.size(); i++){<!-- -->
    	b[s2[i] - 'a']++;
    	b[s2[i - n] - 'a']--;
    	if(a == b){<!-- -->
    		return true;
		}
	}
	return false;
}

```

来源：力扣（LeetCode） 链接：
