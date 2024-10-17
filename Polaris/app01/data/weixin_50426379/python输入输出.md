
--- 
title:  python输入输出 
tags: []
categories: [] 

---
### 一、input输入函数

**help(input)**: Read a string from standard input.–&gt;从标准输入(键盘)读取一个字符串

#### 案例：

##### 1.用户名密码输入------&gt;接收用户输入，并将结果输出

```
username = input("请输入用户名：") 
passwd = input("请输入密码：") 
print("用户名：",username) 
print("密码：",passwd) 
print("变量类型：",type(username),type(passwd))
print("变量长度：",len(username),len(passwd))             

```

<img src="https://img-blog.csdnimg.cn/img_convert/fef0d1d46c96675e59ffd906eb48248d.png#pic_center" alt="在这里插入图片描述">

###### 1.1*print函数里面用 “,” 连接和用 “+” 连接的区别：用“,”连接会产生一个空格，因为用’,'连接代表是多个值，print函数里面值与值之间默认的分隔符是空格，而用‘+’是字符串拼接，代表一个值（后面会提到print输出函数的用法）**

```
 username = input("请输入用户名：")
 passwd = input("请输入密码：")
 print("用户名："+username)
 print("密码：",passwd)       

```

##### 2.案例1的用户名密码输入，优化：将密码隐藏

```
import getpass
username = input("请输入用户名：")
passwd = getpass.getpass("请输入密码：") 
print("用户名："+username) 
print("密码：",passwd) 
print("变量类型：",type(username),type(passwd))
print("变量长度：",len(username),len(passwd))   

```

###### 2.2getpass.getpass–&gt;getpass模块中的getpass函数，需要在终端（Terminal）运行看到效果

<img src="https://img-blog.csdnimg.cn/img_convert/e001cff0c09a994383e036448345e3ef.png#pic_center" alt="在这里插入图片描述">

### 二、print输出函数

**help(print)**

<img src="https://img-blog.csdnimg.cn/img_convert/a9e858222c5f7ef3b27c711a618ccaf2.png#pic_center" alt="在这里插入图片描述">

##### 1.**sep指定分割符**，在值与值之间插入字符串，默认为空格

# print(‘a’,‘b’,‘c’,7, sep="&amp;&amp;&amp;")

<img src="https://img-blog.csdnimg.cn/img_convert/4653ec4e1acf438293c3cef5e909fce0.png" alt="image.png">

##### 2.end: 指定追加符，默认情况下是换行输出

# print(1, end = “%”)

# print(2, end = “%”)

# print(3)

<img src="https://img-blog.csdnimg.cn/img_convert/38858931c26a58937eedac556eca7a04.png" alt="image.png">

##### 3.file指定输出到哪里， 默认输出到屏幕

#还可以输出到文件

#以读写的形式打开文件file.txt

f = open(“file.txt”, ‘w+’)

print(“a”, “b”, “c”, file=f)

##### 4.flush：是否强制刷新流

```
import time
for i in range(20):
    print('#', end='',flush=True) #每隔0.2秒输出一个'#'，实时更新输出
    time.sleep(0.2)

```

### 总结案例

##### 1.输入用户名和密码，在文件中输出xxx用户，欢迎您！（也是在终端运行）

```
import getpass
username = input("请输入用户名：")
passwd = getpass.getpass("请输入密码：")
filename = open('./2022-03--5/test.txt', 'w+')
print(username, '用户,欢迎您！', sep='', file=filename)

```
