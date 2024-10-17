
--- 
title:  Python学习笔记第二天(Python基本语句) 
tags: []
categories: [] 

---


#### Python学习笔记第二天
- - - - <ul><li>- - - - <ul><li>- 


## 行与缩进

        python最具特色的就是使用缩进来表示代码块。

正确写法：

```
# 实例 1
if True:
    print("True")
else:
    print("False")    

```

        若没有缩进则报错，或者缩进不规范也容易没有产生值。

错误写法：

```
# 实例 2
if True:
print("True")
else:
print("False")    

```

## 关键字

        关键字指的是具有特殊功能的标识符。

关键字有：

```
False      class      finally    is         return

None       continue   for        lambda     try

True       def        from       nonlocal   while

and        del        global     not        with 

as         elif       if         or         yield

assert     else       import     pass

break      except     in         raise

```

        跟java等语言一样，在python中有33个关键字，注意在python中，False、None和True的首字母大写，其他关键字全部小写。

## 数据类型

        python的数据类型有：字符串、整型、列表、元组、字典、布尔型等等。数据类型是编程语言必备的属性，只有给数据赋予明确的数据类型，计算机才能对数据进行处理运算。

### 整数类型（int）简称整型，它用于表示整数。

        接下来看看整型是怎么表示的

```
# 实例 3      两种写法均可
counter = 100 # 赋值整型变量
counter = int(100)# 赋值整型变量

```

### 浮点型（Float）数学中的小数，用于表示实数。

        接下来看看浮点型是怎么表示的

```
# 实例 4      两种写法均可
miles = 1000.0 # 赋值浮点型变量
miles = float(100)# 赋值浮点型变量

```

### 字符串型（str）可以理解为中文

        比如"123"是**一二三**不是整型的**一百二十三**，接下来看看字符串型是怎么表示的

```
# 实例 5      三种写法均可
name = '100' # 赋值字符串型变量
name = "100" # 赋值字符串型变量
name = str(100)# 赋值字符串型变量

```

"“与’‘区别：         ""优先级比’'大也可以理解为”"里面用’’

```
# 实例 6      
name = "'中国'+'中华'"

```

### 布尔型是整型的子类型，布尔型数据只有两个取值：True和False，分别对应整型的1和0。

#### 比较运算：
1. 等于 == 不等于 ！=1. 小于等于 &lt;= 大于等于&gt;=1. 大于 &gt; 小于 &lt;
#### 逻辑运算：
1. 与运算 and 一假则假1. 或运算 or 一真则真1. 非运算 not 真假倒转
```
# 实例 6      
a = True
print(a and 0 or 99) # ==&gt; 99

```

## 结束语

今天学习的是Python基本语句，学会了吗。 今天学习内容总结一下：
1. 行与缩进1. 关键字1. 数据类型