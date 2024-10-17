
--- 
title:  Python中的8种运算符 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/92b6f8a7e4c34feba8b20fb5583de221.gif#pic_center" alt="在这里插入图片描述"> 

#### Python中的5种运算符
- - <ul><li>- - - - - - - 


## Python运算符(持续更新中)

### 算术运算符

✅算术运算符是处理四则运算的符号，数字处理应用方面最多，在Python中，常用的算术运算符如下表所示

|运算符|描述
|------
|+|加
|-|减
|*|乘
|/|除
|%|取摸-返回除法的余数
|**|幂-返回x的y次方
|//|取整数-返回商的整数部分

<font color="red" size="4"> 详解算术运算符</font>
- `+`运算符 +运算符用于两个数相加 `实例`：将x和y的值相加
```
x = 10
y = 7
print("两个数相加:", x + y)

```

<img src="https://img-blog.csdnimg.cn/c3d118af6d6746b79c557409ebaec2c7.png" alt="在这里插入图片描述">
- `-`运算符 -运算符用于将两个数相减 `实例`：将x和y的值相减
```
x = 10
y = 7
print("两个数相减:", x - y)

```

<img src="https://img-blog.csdnimg.cn/550cc346c6c24921b1174f279c6f90bd.png" alt="在这里插入图片描述">
- `*`乘运算符 *乘运算符用于将两个数相乘 `实例`：将x和y的值相乘
```
x = 10
y = 7
print("两个数相乘:", x * y)

```

<img src="https://img-blog.csdnimg.cn/fa7cb5cefb134347ac3d39d3016ff895.png" alt="在这里插入图片描述">
- `/`除运算符 /运算符用于将两个数相除 `实例`：将x和y的值相除
```
x = 10
y = 7
print("两个数相乘:", x / y)

```

<img src="https://img-blog.csdnimg.cn/f514432eceed4d17966f94b0ba39955c.png" alt="在这里插入图片描述">
- `%`取模运算符(返回除法的余数) %取模运算符用于将两数进行取模运算 `实例`：将x和y的值进行取模，返回余数
```
x = 10
y = 7
print("两个数相除:", x / y)
print("两个数取整除:", x // y)

```

<img src="https://img-blog.csdnimg.cn/1a0e4063ea4e40f9a6679a06003149d1.png" alt="在这里插入图片描述">
- `//`取整除运算符(返回商的整数部分) //取整除运算符用于将两数进行取整除运算(默认保留小数点后16位) `实例`：将x和y的值进行取整除，返回商的整数部分 返回商的整数部分是指返回整数，例如10与7相除约等于1.4285714285714286，取商的整数部分即取1
```
x = 10
y = 7
print("两个数相除:", x / y)
print("两个数取整除:", x // y)

```

<img src="https://img-blog.csdnimg.cn/116c9b942edb4201b3a1d1fd48c73dd6.png" alt="在这里插入图片描述">
- `**`幂运算符(返回x的y次方) **幂运算符用于将两数进行乘方运算符 `实例`：将x和y的值进行幂运算(例如2的2次等于4)
```
x = 2
y = 2
print("两数取幂:", x ** y)

```

<img src="https://img-blog.csdnimg.cn/d8e83f8a170f461eb102fb13b02b2832.png" alt="在这里插入图片描述">

### 赋值运算符

✅赋值运算符主要用于为变量等赋值，可以直接把简单赋值运算符右边的值直接赋值给左边的变量，也可以进行某种运算后再赋值给左边的变量。在Python中，常用的赋值运算符如下表所示

|运算符|描述
|------
|=|简单的赋值运算符
|+=|加法赋值运算符
|-=|减法赋值运算符
|*=|乘法赋值运算符
|/=|除法赋值运算符
|%=|取模赋值运算符
|**=|幂赋值运算符
|//=|取整除赋值运算符

<font color="red" size="4"> 详解赋值运算符</font>
- =简单的赋值运算符 把结果赋值给给一个变量 `实例`：将x的值赋值给y输出y的值
```
x = 777
y = x
print("y的值:", y)

```

<img src="https://img-blog.csdnimg.cn/9274b42a3c5942cf9ce0ec2cc5f6d00b.png" alt="在这里插入图片描述">
- `+=`加法赋值运算符 x+=y相当于x=x+y(将x+y的值重新赋值给x） `实例`：将x与y进行加法赋值运算
```
x = 10
x += 7
print("加法赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/e2b8af167ebd498794676509bc6946ac.png" alt="在这里插入图片描述">
- `-=`减法赋值运算符 x-=y相当于x=x-y(将x-y的值重新赋值给x) `实例`：将x与y进行减法赋值运算
```
x = 10
x -= 7
print("减法赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/f2e00e9c6cf64c4d93c649493c5cfba0.png" alt="在这里插入图片描述">
- `*=`乘法赋值运算符 x*=y相当于x=x * y(将x * y的值重新赋值给x) 实例：将x与y进行乘法赋值运算
```
x = 10
x *= 7
print("乘法赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/fc53ab0430c44d698c98706a894cd754.png" alt="在这里插入图片描述">
- `/=`除法赋值运算符 x/=y相当于x=x / y(将x / y的值重新赋值给x) `实例`：将x与y进行除法赋值运算
```
x = 10
x /= 7
print("除法赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/ef72ac9b704245b894b249270aa6bae7.png" alt="在这里插入图片描述">
- `%=`取模赋值运算符 x%=y相当于x=x % y(将x % y的值重新赋值给x) `实例`：将x与y进行取模赋值运算
```
x = 10
x %= 7
print("取模赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/2fd6de11fd0d4ed3b81b627068718206.png" alt="在这里插入图片描述">
- `**/`幂赋值运算符 x**=y相当于x=x ** y(将x ** y的值重新赋值给x) `实例`：将x与y进行幂赋值运算
```
x = 2
x **= 2
print("幂赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/cb124e75045d477ca4a7d1db9ffeda8e.png" alt="在这里插入图片描述">
- `//=`取整除赋值运算符 x//=y相当于x=x // y(将x // y的值重新赋值给x) `实例`：将x与y进行取整除赋值运算
```
x = 10
x //= 7
print("取整除赋值:", x)

```

<img src="https://img-blog.csdnimg.cn/b476f48f2af447148c4a7b590065f6fc.png" alt="在这里插入图片描述">

### 比较(关系)运算符

✅比较运算符又称关系运算符，用于对变量或者表达式的结果进行大小，真假等比较，如果比较结果为真返回True，反之返回False。在Python中，常用的比较运算符如下表所示

|运算符|描述
|------
|==|等于(比较两个对象是否相等
|!=|不等于(比较两个对象是否不相等
|&gt;|大于(返回x是否大于y)
|&lt;|小于(返回x是否小于y)
|&gt;=|大于等于(返回x是否大于等于y
|&lt;=|小于等于(返回x是否小于等于y

<font color="red" size="4"> 详解比较(关系)运算符</font>
- `==`等于 比较两个对象是否相等 如果相等返回True，反之返回False `实例`：比较x与y是否相等
```
x = 10
y = 10
print("x是否等于y:", x == y)

```

<img src="https://img-blog.csdnimg.cn/9cb53fc24a2544f0bdde9ac115e19522.png" alt="在这里插入图片描述">
- `!=`不等于 比较两个对象是否不相等 如果不相等返回True，反之返回False `实例`：比较x与y是否不相等
```
x = 10
y = 7
print("x是否不等于y:", x != y)

```

<img src="https://img-blog.csdnimg.cn/ac53db9d982048a4a26b2d2320dcb69e.png" alt="在这里插入图片描述">
- `&gt;`大于(返回x是否大于y) 如果x大于y返回True，反之返回False `实例`：比较x是否大于y
```
x = 10
y = 7
print("x是否大于y:", x &gt; y)

```

<img src="https://img-blog.csdnimg.cn/434c0b19e2534ecaaf14f63877baee5a.png" alt="在这里插入图片描述">
- `&lt;`小于(返回x是否小于y) 如果x大于y返回True，反之返回False `实例`：比较x是否小于y
```
x = 10
y = 7
print("x是否小于y:", x &lt; y)

```

<img src="https://img-blog.csdnimg.cn/fb697fc554b44bed9505a56c9edab34c.png" alt="在这里插入图片描述">
- `&gt;=`大于等于(返回x是否大于等于y) 如果x大于y返回True，反之返回False `实例`：比较x是否大于等于y
```
x = 10
y = 7
print("x是否大于等于y:", x &gt;= y)

```

<img src="https://img-blog.csdnimg.cn/b4213a18cb554d4baf75ce402a1c0b76.png" alt="在这里插入图片描述">
- `&lt;=`小于等于(返回x是否小于等于y) 如果x大于y返回True，反之返回False `实例`：比较x是否小于等于y
```
x = 10
y = 7
print("x是否小于等于y:", x &lt;= y)


```

<img src="https://img-blog.csdnimg.cn/99fb98364fe749688c3b0cb3d11fe910.png" alt="在这里插入图片描述">

### 逻辑运算符

✅逻辑运算符是对真假两种布尔值进行运算，运算的结果仍是一个布尔值。在Python中，常用的逻辑运算符如下表所示

|运算符|描述
|------
|and|逻辑与
|or|逻辑或
|not|逻辑非

<font color="red" size="4"> 详解逻辑运算符</font>
- `and`逻辑与运算符 如果x为False，x and y返回x的值，反之返回y的值 `实例`：计算x and y的运算
```
x = 0
y = 20
print("x为False:", x and y)

```

<img src="https://img-blog.csdnimg.cn/17529edd2a5248aa82284894b6682de0.png" alt="在这里插入图片描述">
- `or`逻辑或运算符 如果x为True，x or y返回x的值，反之返回y的值 `实例`：x or y的运算
```
x = 10
y = 7
print("x为True:", x or y)

```

<img src="https://img-blog.csdnimg.cn/668eadf7e3b74016a2133f43d559cbb8.png" alt="在这里插入图片描述">
- `not`逻辑非运算符 如果x为True返回False 如果x为False返回True
```
x = 10
print("x为True:", not x)

```

<img src="https://img-blog.csdnimg.cn/6f11d501e4344603a63756ae0a1f6b48.png" alt="在这里插入图片描述">

### 位运算符(了解即可)

✅位运算符是把数字看作二进制数进行计算，需要先将要参与运算的数据转换为二进制然后进行计算(不常用，仅作了解即可)
- `&amp;`按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0- `|`按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。- `^` 按位异或运算符：当两对应的二进位相异时，结果为1- `~`按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。- `&lt;&lt;`左移动运算符：运算数的各二进位全部左移若干位，由"&lt;&lt;"右边的数指定移动的位数，高位丢弃，低位补0。- `&gt;&gt;`右移动运算符：把"&gt;&gt;“左边的运算数的各二进位全部右移若干位，”&gt;&gt;"右边的数指定移动的位数
### 成员运算符

✅成员运算符用于判断在指定序列里是否找到值，返回的结果为布尔类型的True或False。在Python中常用的成员运算符如下表所示

|运算符|描述
|------
|in|在指定序列里找到值返回True，否则返回False
|not in|在指定序列里没找到值返回True，否则返回False

<font color="red" size="4"> 详解成员运算符</font>
- in(找到值返回True) `实例`：判断x是否在指定序列中
```
x = 7
demo = [1, 2, 3, 4, 5, 6, 7]
print("x是否在demo列表里:", x in demo)

```

<img src="https://img-blog.csdnimg.cn/9a67e07c2ad64df184068eb850bb1b46.png" alt="在这里插入图片描述">
- not in(没找到值返回True) `实例`：判断x是否在指定序列中
```
x = "python"
demo = ["python", "java", "javascript"]
print("x是否不在demo字符串里:", x not in demo)

```

<img src="https://img-blog.csdnimg.cn/893a9193b28f4330a1bcba99ac74e8a7.png" alt="在这里插入图片描述">

### 身份运算符

身份运算符用于判断是否引自同一对象，返回值为布尔类型的True或False。在Python中，常用的身份运算符如下表所示

|运算符|描述
|------
|is|判断两个标识符是不是引用自一个对象
|is not|判断两个标识符是不是引用自不同对象

<font color="red" size="4"> 详解身份运算符</font>
- `is`身份运算符 如果引自同一对象返回True，反之返回False 实例：判断x与y是否引自同一对象
```
x = 10
y = 10
print(x is y)

```

<img src="https://img-blog.csdnimg.cn/f6124b5ec470443fb9c3472acff55823.png" alt="在这里插入图片描述">
- `is not`身份运算符 如果引自不同对象返回True，反之返回False 实例：判断x与y是否引自不同对象
```
x = 10
y = 10.0
print(x is y)

```

<img src="https://img-blog.csdnimg.cn/96351b378d14419ab639200739a40008.png" alt="在这里插入图片描述">

✅`is和==的区别`： is是判断是否引自同一个对象 ==是判断值是否相等

```
x = 10
y = 10.0
print("x的内存地址:", id(x))
print("y的内存地址:", id(y))
print("x is y:", x is y)
print("x == y:", x == y)

```

<img src="https://img-blog.csdnimg.cn/98563e65bd684fef9e06f208e5675482.png" alt="在这里插入图片描述">

### 三目运算符

三目运算符通常用于简化条件判断语句 例如：我们想输出两数之间最大的那一个，可以用if else 语句

```
x = 7
y = 10
if x &gt; y:
    print("max:", x)
else:
    print("max:", y)

```

<img src="https://img-blog.csdnimg.cn/450b4465532549f99aec9b6cee79446d.png" alt="在这里插入图片描述"> 可以将以上代码用三目运算符进行简化

三目运算符语法格式：`True_statements if expression else False_statements`

如果expression为真值，执行True_statements，并将其结果作为整个表达式的结果，反之为假执行False_statements，并将其结果作为整个表达式的结果

```
x = 7
y = 10
print("max:", x if x &gt; y else y)

```

<img src="https://img-blog.csdnimg.cn/8299037e9514408d97df30662e6f800b.png" alt="在这里插入图片描述">

## 运算符优先级

✅仅列举常用的运算符的优先顺序（1最高依次降低)

|优先级顺序|运算符|描述
|------
|1|**|幂
|2|* / % //|乘、除、取模、取整除
|3|+ -|加、减
|4|== != &lt; &gt; &lt;= &gt;=|比较运算符
|5|= %= /= //= -= += *= **=|赋值运算符
|6|is is not|身份运算符
|7|in not in|成员运算符
|8|not or and|逻辑运算符

## 结束语🥇

>  
 以上就是Python基础入门篇之Python中的8种运算符 
 - `欢迎大家订阅系列专栏:`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


>  
 感谢大家一直以来对hacker的支持 你们的支持就是博主无尽创作的动力💖💖💖 


<img src="https://img-blog.csdnimg.cn/bdd237d869be4fee9ba4de0f100e35a8.gif#pic_center" alt="在这里插入图片描述">
