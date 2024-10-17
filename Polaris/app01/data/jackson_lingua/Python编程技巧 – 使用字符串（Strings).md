
--- 
title:  Python编程技巧 – 使用字符串（Strings) 
tags: []
categories: [] 

---
## Python编程技巧 – 使用字符串（Strings)

### Python Programming Essentials – Using Strings

本文简要介绍如何使用字符串，来进行Python编程。字符串有很多用途，包括输出结果、反馈状态、数据处理以及切片和文本筛选等

#### 1. 字符串

字符串(String)就是一系列字符组成的集合。Python 中的字符串用单引号或双引号括起来。因此，‘hello’与“hello”相同。 在开发第一个Python应用程序时，”Hello, world!”就是一个字符串，当执行打印输出时，程序语句如下：

```
print(“Hello, world!”)
print(‘Hello, world!’)

```

这说明，您可以在需要的时候，使用 print（） 函数输出显示字符串文字。

#### 2. 字符串变量

将字符串分配给变量是用变量名称后跟等号和字符串来完成的，例如下面代码：

```
s = “Hello”
print(s)

```

#### 3. 多行字符串

当字符串很长的时候，可以在多行表达遮掩的字符串，而包含字符串的是三引号“”“，而不仅仅是双引号“”。

```
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

```

以上的例子，也可以用三个单引号’’’来包含长字符串。

```
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

```

#### 4. 字符串数组

Python表示的字符串，也是包含在unicode字符范围的字节数组；这就意味着，也能够用方括号[ ]来访问每个字符串的元素。示例代码如下，要是想得到字符H，需要获取位置为1的字符：

```
s = "Hello, World!"
print(s[1])

```

Python不像JavaScript语言，没有包含char字符的数据类型，单个字符仅仅是长度为1的字符串。

#### 5. 遍历字符串

既然，字符串是数组，那么每个字符作为一个元素，可以被访问，当然也可以被遍历。请看一下下方代码：

```
s = “fantastic”
x = 0
for x in s:
  print(x)

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/b641ed4a93eb4e8c9cfeefbf4a72824e.png" alt="在这里插入图片描述">

#### 6. 字符串长度

len( ) 函数可以返回一个字符串的长度。同样，遍历字符串的字符，也可以用这个长度来实现。

##### 代码一：返回字符串的长度

```
str = “Welcome to New York! We have schedule a trip for you.”
print(len(str))

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/1e7454baae2644d3b5755e4b49be2bae.png" alt="在这里插入图片描述">

#### 7. 检查字符串

如果需要检查某个字符串中是否包含了特定的短语或字符，可以使用关键字in，如下代码：

```
txt = “The best thins in life are free. Free time can be important.”
print(“free” in txt)

```

执行代码如下图所示： <img src="https://img-blog.csdnimg.cn/8e8e7437fa4842dbb221ea34bb139829.png" alt="在这里插入图片描述">

#### 8. 合并字符串

当需要合并两个字符串时，运用+运算符或者格式合并即可，如下代码：

```
fname = input(“Enter your first name: “)
lname = input(“Enter your last name: “)
print(f“Your full name is: {<!-- -->fname} {<!-- -->lname}”)

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/8c08300c3afc4d8c8b25d953e3d30ea4.png" alt="在这里插入图片描述"> 分别要求输入first name, last name, 结果是full name等于 first name 和last name组成的全名Bruce Lee。执行成功！

字符串就简单讲述到此。后续还有更多的技术好文，敬请关注。

喜欢请点赞/收藏哈，这也是我不断创作的源泉。😊

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 