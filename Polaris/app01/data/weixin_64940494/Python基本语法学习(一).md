
--- 
title:  Python基本语法学习(一) 
tags: []
categories: [] 

---
        Python的优点是简单、易学、易读和易维护，Python取消 " ; " 做结束符，同时也取消了很多的符号。Python采用强制缩进的方式使得代码具有较好可读性，取消了" {} " ，强制使用4个空格作层级关系。

### 1. Python内置数据类型
|文本类型：|str
|数值类型：|`int`, `float`, `complex`
|序列类型：|`list`, `tuple`, `range`
|映射类型：|`dict`
|集合类型：|`set`, `frozenset`
|布尔类型：|`bool`
|二进制类型：|`bytes`, `bytearray`, `memoryview`

### 2. Python注释

#### 2.1 单行注释

      使用 # 做单行注释，# 后面的内容将不会被执行。

>  
 # 这是python的单行注释，单行注释规范：#[一个空格]注释的内容 


#### 2.2 多行注释

使用一对三个双引号做多行注释。

>  
         """ 
                 这是python的多行注释，三引号也可以做单行注释，但是做单行注释时左边不 
                 要有等号赋值，不然注释的内容会被当成是字符串 
         """ 


### 3. Python变量

#### 3.1 变量的定义

>  
         变量名 = 变量值  


#### 3.2 变量命名规则
- 变量名必须以字母或下划线字符开头- 变量名称不能以数字开头- 变量名只能包含字母数字字符和下划线（A-z、0-9 和 _）- 变量名称区分大小写- 变量名称不能使用关键字，如：class 、True 、False... 等
#### 3.3 多个变量的定义

>  
 a1,a2,a3= "guangdong" , "hunan" , "hubei" 


### 4. Python运算符

#### 4.1 Python算术运算符

        基础运算符
<td style="text-align:center;width:107px;">运算符</td><td style="text-align:center;width:232px;">描述</td><td style="text-align:center;width:253px;">实例</td>
<td style="text-align:center;width:107px;">+ 、- 、* 、/</td><td style="width:232px;">数字基本的加、减、乘、除</td><td style="width:253px;"></td>
<td style="text-align:center;width:107px;">%</td><td style="width:232px;">除法后取余</td><td style="width:253px;"> x = 4,y = 2  x%y = 0  x = 5,y = 2  x%y = 1 </td>

x = 5,y = 2  x%y = 1
<td style="text-align:center;width:107px;">//</td><td style="width:232px;">除法后取结果的整数部分</td><td style="width:253px;"> x = 4,y = 2 x//y = 2 x = 5,y = 2 x//y = 2 </td>

x = 5,y = 2 x//y = 2
<td style="text-align:center;width:107px;">**</td><td style="width:232px;">幂次方</td><td style="width:253px;">x = 3 ,y=2 x**y = 3² = 9</td>

        复合赋值运算符，在基础运算符后拼接等于号，就是先运算后赋值，例如：x += 2 相当于 x = x + 2 。

#### 4.2 Python比较运算符

        比较运算符做判断，返回值为bool类型（True、False）。
<td style="text-align:center;width:90px;">运算符</td><td style="text-align:center;width:250px;">描述</td><td style="text-align:center;width:257px;">实例</td>
<td style="text-align:center;width:90px;">==</td><td style="width:250px;">判断是否相等</td><td style="width:257px;"> x = 10 , y = 10  x==y 返回 True x = 'hello' , y = 'word' x==y 返回False </td>

x = 'hello' , y = 'word' x==y 返回False
<td style="text-align:center;width:90px;">!=</td><td style="width:250px;">判断是否不相等</td><td style="width:257px;"> x = 10 , y = 10  x==y 返回 False x = 'hello' , y = 'word' x==y 返回True </td>

x = 'hello' , y = 'word' x==y 返回True
<td style="text-align:center;width:90px;">&gt; &lt;</td><td style="width:250px;">大于、小于判断</td><td style="width:257px;"> x = 10 , y = 20  x&gt;y 返回False x = 10 , y = 20  x&lt;y 返回True </td>

x = 10 , y = 20  x&lt;y 返回True
<td style="text-align:center;width:90px;"> &gt;= &lt;= </td><td style="width:250px;">大于等于、小于等于判断</td><td style="width:257px;"> x = 10 , y = 20  x&gt;=y 返回False x = 10 , y = 20  x&lt;=y 返回True </td>

&lt;=

x = 10 , y = 20  x&lt;=y 返回True

### 5. Python字符串

#### 5.1 字符串定义

        字符串定义使用英文的单引号、多引号或者三引号

        例如：

>  
    str = '你好' 
    str = "你好" 
    str = """你好""" 


          注意：之前提过Python多行注释也是使用三引号，区别在于如果有赋值变量接收那么就是字符串定义，如果没有赋值变量接收就是多行注释。

#### 5.2 字符串拼接

        字符串的拼接使用" + "进行拼接。

        例如："hello" + "word" 

        在字符串拼接是不允许拼接一个数字如果拼接一个数字的话会报错，如果要拼接一个数字需要将数字进行强制类型转换。

        例如："hello" + str(2)

#### 5.3 字符串占位拼接

**5.3.1 占位符拼接**
<td style="text-align:center;width:77px;">占位符</td><td style="text-align:center;width:243px;">描述</td><td style="text-align:center;width:290px;">实例</td>
<td style="text-align:center;width:77px;">%s</td><td style="width:243px;">将内容换成字符串，放入占位位置</td><td colspan="1" rowspan="3" style="width:290px;">"你好我叫%s,我的年龄是%d,我的身高是：%.2f" % ('码农'，30，175.5)</td>
<td style="text-align:center;width:77px;">%d</td><td style="width:243px;">将内容换成整数，放入占位位置</td>
<td style="text-align:center;width:77px;">%.nf</td><td style="width:243px;"> 将内容换成浮点数，放入占位位置， .n代表小数点几位，如果不设置默认是6位小数，%f代表不设置小数点 </td>

.n代表小数点几位，如果不设置默认是6位小数，%f代表不设置小数点

**5.3.2 使用 f 快速拼接**

    例如：f"你好我叫{'码农'}，我的年龄是{30}，我的身高是{175.5}"

<img alt="" height="169" src="https://img-blog.csdnimg.cn/d19d913bb31d414c96e947e792eee348.png" width="751">
