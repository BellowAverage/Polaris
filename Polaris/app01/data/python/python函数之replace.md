
--- 
title:  python函数之replace 
tags: []
categories: [] 

---
**在python3中，replace用于对字符串中的元素进行替换，返回一个新的字符串，不会对原有字符串进行更改。因为字符串是不可变类型。**

语法：

```
String.replece(old, new, count)
```

参数
- old : 需要被替换的字符- new：新的字符- count ：最多替换几次
返回值
-         返回一个新的字符串
实例：

```
s = 'abcabcabc'
new_s = s.replace('a', 'b', 2)
print(s.replace('a', 'b', 2))
print(s)

# 结果
bbcbbcabc
abcabcabc
```


