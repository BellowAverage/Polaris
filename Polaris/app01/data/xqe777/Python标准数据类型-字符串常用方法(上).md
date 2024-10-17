
--- 
title:  Python标准数据类型-字符串常用方法(上) 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待 


<img src="https://img-blog.csdnimg.cn/bda67eea8ec641869e3c0abd5ebafe95.gif#pic_center" alt="在这里插入图片描述"> 

#### 字符串常用方法
- - <ul><li>- - - - - - - - - - - - - - - - 


## ✨字符串常用方法

Python中的字符串是不可变的序列对象，提供了许多方法来操作和处理字符串。下面是一些常用的字符串方法(`可根据目录找到自己的想要的方法，方便学习查看`)

### 拼接字符串`+`

使用+运算符可以拼接多个字符串并产生一个字符串对象 `示例代码`：

```
demo = "人生苦短我用Python"
demo1 = "Life is short I use Python"
print(demo + ":" + demo1)

```

✅在上面示例代码中，我们定义了两个列表demo和demo1，使用+将两个列表拼接在一起打印

<img src="https://img-blog.csdnimg.cn/830e163fb3e94af1a2f9f00e4353b027.png" alt="在这里插入图片描述">

`注意事项`：

字符串不允许直接与其他数据类型的数据进行拼接

`实例`：将以下字符串类型的数据与int类型的数据进行拼接

```
demo = "我今天一共走了"
num = 777
demo1 = "步"
print(demo + num + demo1)

```

运行以后就会报以下异常

`TypeError: can only concatenate str (not "int") to str` 类型错误：只能将字符串与字符串进行`concatenate`（连接）

<img src="https://img-blog.csdnimg.cn/dbbf5ec0102c4692840a4fff370480dc.png" alt="在这里插入图片描述"> `解决方法如下`：
-  第一种方法：将num的int类型强转为str类型 `num = str(777)` -  第二种方法：在打印时将num的值进行强转 `print(demo + str(num) + demo1)` 
<img src="https://img-blog.csdnimg.cn/2cdfa6b13b754c1e951ad609a57dfb07.png" alt="在这里插入图片描述">

### 字符串首字母大写`title()`

`title()`方法将字符串首字母转为大写

title()方法语法格式：`str.title()`

参数说明如下：
- `str`：要进行转换的字符串
`实例`：将"hello world"字符串首字母大写

```
demo = "hello world"
res = demo.title()
print("首字母大写:" + res)
print("原字符串:" + demo)

```

<img src="https://img-blog.csdnimg.cn/794f40d4f8a14edb979aefe86fd58ac7.png" alt="在这里插入图片描述">

### 字符串首字母大写`capitalize()`
- capitalize()方法与title()方法类似，都是将字符串首字母大写- 但使用capitalize()方法只有首字母大写，其他字母变小写
capitalize()方法语法格式：`str.capitalize()`

`实例`：将"hEllOworLd"字符串首字母大写

```
demo = "hEllOworLd"
res = demo.capitalize()
print("首字母大写:" + res)
print("原字符串:" + demo)

```

<img src="https://img-blog.csdnimg.cn/3e58b34b826c43569a160cb5fc6ea27e.png" alt="在这里插入图片描述">

### 字符串转大写`upper()`

`upper()`方法将字符串中的字母全部转大写

upper()方法语法格式：`str.upper()`

参数说明如下：
- `str`：要进行转换的字符串
`实例`：将"helloworld"字符串转大写

```
demo = "helloworld"
res = demo.upper()
print("字符串转大写:" + res)
print("原字符串:" + demo)

```

<img src="https://img-blog.csdnimg.cn/19c6c9aab8f9466e8de7e53eb206c05f.png" alt="在这里插入图片描述">

### 字符串转小写`lower()`

`lower()`方法将字符串中的字母全部转小写

lower()方法语法格式：`str.lower()`

参数说明如下：
- `str`：要进行转换的字符串
`实例`：将"HELLOWORLD"字符串转小写

```
demo = "HELLOWORLD"
res = demo.lower()
print("字符串转小写:" + res)
print("原字符串:" + demo)

```

<img src="https://img-blog.csdnimg.cn/00ee2d12325c402893f335bc7c0db57f.png" alt="在这里插入图片描述">

### 检索字符串中最小字母min()

`min()`方法检索字符串中最小字母 min()方法语法格式：`min(str)`

`实例`：检索"hacker"字符串中最小字母

```
demo = "hacker"
print(min(demo))

```

<img src="https://img-blog.csdnimg.cn/d481b1b35ec740be8a2a362d7bebbef2.png" alt="在这里插入图片描述">

### 检索字符串中最大字母max()

`max()`方法检索字符串中最小字母 max()方法语法格式：`max(str)`

`实例`：检索"hacker"字符串中最大字母

```
demo = "hacker"
print(max(demo))

```

<img src="https://img-blog.csdnimg.cn/c656bdf2820944c1bab2a00ad95f325f.png" alt="在这里插入图片描述">

### 计算字符串长度`len()`
- 要计算字符串的长度，首先要了解各字符所占的字节数。- 在Python中，数字、英文、小数点、下划线和空格占一个字节；- 一个汉字可能占2~4个字节，占几个字节取决于采用的编码。汉字在`GBK/GBK2312`编码中占2个字节，在`UTF-8`编码中一般占用3个字节。
在python中，使用`len()`函数计算字符串长度。

len()方法语法格式：`len(string)`

参数说明如下：
- `string`：要进行长度统计的字符串
`实例`：定义一个字符串，内容为"但行好事，莫问前程"，用len()函数计算该字符串长度并输出。

```
demo = "但行好事莫问前程"
length = len(demo)
print("原字符串:" + demo)
print("字符串长度:" + str(length))

```

<img src="https://img-blog.csdnimg.cn/1a6fd1067b7e499eac1776bc877c4664.png" alt="在这里插入图片描述"> 从上面输出的结果可以看出，通过len()函数计算字符串长度，所有字符都是按照1个字符计算。 但在实际开发中，有时候我们需要获取字符串实际所占的字节数，这时可以采用encode()方法进行编码后再进行获取。

`实例`：采用UTF-8编码后获取上方实例中字符串长度。

```
demo = "但行好事莫问前程"
length = len(demo.encode())
print("原字符串:" + demo)
print("字符串长度:" + str(length))

```

<img src="https://img-blog.csdnimg.cn/e4812fbb8fc94e04aa28b5ef59cfb773.png" alt="在这里插入图片描述">

### 检测字符串是否只由字母和数字组成`isalnum()`

`isalnum()`方法检测字符串是否只由字母和数字组成 是返回True，不是返回False isalnum()方法语法格式：`str.isalnum()`

`实例`：检测"hacker707"字符串是否有字母和数字组成

```
demo = "hacker707"
print(demo.isalnum())

```

<img src="https://img-blog.csdnimg.cn/4c0a32641a6249c18974fb01e120a652.png" alt="在这里插入图片描述">

### 检测字符串是否只由字母或文字组成`isalpha()`

`isalpha()`方法检测字符串是否由只字母或文字组成 如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False isalpha()方法语法格式：`str.isalpha()`

`实例`：检测"hacker嘎嘎宠粉"字符串是否只由字母或文字组成

```
demo = "hacker嘎嘎宠粉"
print(demo.isalpha())

```

<img src="https://img-blog.csdnimg.cn/72d7ff8580644eb081c69af9040d5f47.png" alt="在这里插入图片描述">

### 检测字符串是否只由数字组成`isdigit()`

`isdigit()`方法检测字符串是否由数字组成 是返回true，不是返回false isdigit()方法语法格式：`str.isdigit()`

`实例`：检测"hacker707“字符串是否只由数字组成

```
demo = "hacker707"
print(demo.isdigit())

```

<img src="https://img-blog.csdnimg.cn/e4b98578b8d54170883b7863342e8d0f.png" alt="在这里插入图片描述">

### 检测字符串是否由小写字母组成`islower()`

`islower()`方法检测字符串是否由小写字母组成 是返回true，不是返回false islower()方法语法格式：`str.islower()`

`实例`：检测"hacker"字符串是否由小写字母组成

```
demo = "hacker"
print(demo.islower())

```

<img src="https://img-blog.csdnimg.cn/2eb3c732537e4ff4b12e9f66201d67b2.png" alt="在这里插入图片描述">

### 检测字符串是否由大写字母组成`isupper()`

`isupper()`方法检测字符串是否由小写字母组成 是返回true，不是返回false islower()方法语法格式：`str.isupper()`

`实例`：检测"HACKER"是否由大写字母组成

```
demo = "HACKER"
print(demo.isupper())

```

<img src="https://img-blog.csdnimg.cn/467382798fbc4d349b8afe930aadf44a.png" alt="在这里插入图片描述">

### 检测字符串是否只由数字组成`isnumeric()`

`isnumeric()`方法检测字符串是否只由数字组成 是返回true，不是返回false isnumeric()方法语法格式：`str.isnumeric()`

`实例`：检测"777"字符串是否只由数字组成

```
demo = "777"
print(demo.isnumeric())

```

<img src="https://img-blog.csdnimg.cn/6e6f602521b6438586c3c56954dea7d8.png" alt="在这里插入图片描述">

### 检测字符串是否只包含十进制字符`isdecimal()`

`isdecimal()`检测字符串是否只包含十进制字符 是返回ture，不是返回false isdecimal()方法语法格式：`str.isdecimal()`

`实例`：检测"hacker707"字符串是否只包含十进制字符

```
demo = "hacker707"
print(demo.isdecimal())

```

<img src="https://img-blog.csdnimg.cn/769a95f7ffd042068d00276f1e9a7f4d.png" alt="在这里插入图片描述">

### 检测字符串是否只由空白字符组成`isspace()`

`isspace()`方法检测字符串是否只由空白字符组成 是返回true，不是返回false isspace()方法语法格式：`str.isspace()`

`实例`：检测" "是否只由空白字符组成

```
demo = "            "
print(demo.isspace())

```

<img src="https://img-blog.csdnimg.cn/ad7a76b5c54846ffb27b16186ee21b8f.png" alt="在这里插入图片描述">

### 检测字符串所有单词首字母是否大写`istitle()`

istitle()方法检测字符串所有单词首字母是否大写 是返回true，不是返回false istitle()方法语法格式：`str.istitle()`

`实例`：检测"I Use Python"字符串所有单词首字母是否大写

```
demo = "I Use Python"
print(demo.istitle())

```

<img src="https://img-blog.csdnimg.cn/623efed6dc36442ba89834ce65c1aa96.png" alt="在这里插入图片描述">

## 结束语🥇

>  
 以上就是Python基础入门篇之Python标准数据类型-字符串常用方法(上) 
 - `欢迎大家订阅系列专栏:`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


>  
 感谢大家一直以来对hacker的支持 你们的支持就是博主无尽创作的动力💖💖💖 


<img src="https://img-blog.csdnimg.cn/bdd237d869be4fee9ba4de0f100e35a8.gif#pic_center" alt="在这里插入图片描述">
