
--- 
title:  【LeetCode每日一题】557. 反转字符串中的单词 III——reverse应用（C/C++） 
tags: []
categories: [] 

---
>  
 若青春有张不老的脸，愿岁月待我们如初见 


### 题目：

给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

### 示例 1：

输入：s = “Let’s take LeetCode contest” 输出：“s’teL ekat edoCteeL tsetnoc”

### 示例 2:

输入： s = “God Ding” 输出：“doG gniD”

### 提示：

1 &lt;= s.length &lt;= 5 * 10^4 s 包含可打印的 ASCII 字符。 s 不包含任何开头或结尾空格。 s 里 至少 有一个词。 s 中的所有单词都用一个空格隔开。

### 思路：

不知你是否知道在反转字符串时，有一个特别强大的函数 **reverse() 函数**，引用这个函数可直接实现字符串的反转； 嘿嘿，下面来说下思路：可以对字符串进行遍历，标记开始位置，当**找到空格**时，使用**substr函数**截取，然后使用**reverse函数**进行反转，并加入另一字符串。

### 代码：

```
string reverseWords(string s) {<!-- -->
    string s1, str;
    int j = 0;
    for(int i = 0; i &lt; s.size(); i++){<!-- -->
        if(s[i] == ' '){<!-- -->
            s1 = s.substr(j, i - j);
            reverse(s1.begin(), s1.end());
            str = str + s1 + ' ';
            j = i + 1;
        }
        if(i == s.size() - 1){<!-- -->
            s1 = s.substr(j);
            reverse(s1.begin(), s1.end());
            str += s1;
        } 
    }
    return str;
}

```

来源：力扣（LeetCode） 链接：
