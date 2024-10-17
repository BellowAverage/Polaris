
--- 
title:  Python 基础（二）：基本语句 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - - 


## 1 条件语句

在进行逻辑判断时，我们需要用到条件语句，Python 提供了 `if`、`elif`、`else` 来进行逻辑判断。格式如下所示：

```
if 判断条件1:
    执行语句1...
elif 判断条件2:
    执行语句2...
elif 判断条件3:
    执行语句3...
else:
    执行语句4...

```

## 2 循环语句

当需要多次重复执行时，我们要用到循环语句，Python 提供了 for 循环和 while 循环。

### 2.1 for 循环

for 循环可以遍历任何序列，比如：字符串。如下所示：

```
str = 'Python'
for s in str:
    print(s)

```

输出结果：

```
P
y
t
h
o
n

```

### 2.2 while 循环

while 循环，满足条件时进行循环，不满足条件时退出循环。如下所示：

```
sum = 0
m = 10
while m &gt; 0:
    sum = sum + m
    m = m - 1
print(sum)

```

输出结果：

```
55

```

### 2.3 break

break 用在 for 循环和 while 循环语句中，用来终止整个循环。如下所示：

```
str = 'Python'
for s in str:
    if s == 'o':
        break
    print(s)

```

输出结果：

```
P
y
t
h

```

### 2.4 continue

continue 用在 for 循环和 while 循环语句中，用来终止本次循环。如下所示：

```
str = 'Python'
for s in str:
    if s == 'o':
        continue
    print(s)

```

输出结果：

```
P
y
t
h
n

```

## 3 pass 语句

pass 是空语句，它不做任何事情，一般用做占位语句，作用是保持程序结构的完整性。如下所示：

```
if True:
    pass

```

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="340">
