
--- 
title:  python--生成器generator_python代码自动生成器 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- - - - - - - - - - - - 


## 前言

### 1.生成器是什么？

在Python中，生成器（generator）是一种特殊的迭代器，它是通过函数来实现的。生成器函数在执行过程中可以暂停和继续执行，可以动态地生成一系列值，而不需要一次性生成所有值，从而节省了内存空间和计算资源。
-  可以由生成器表达式得到。 -  可以使用yield关键字得到一个生成器函数，再通过调用这个函数得到一个生成器对象，包含yield语句的生成器函数调用生成生成器对象的时候，生成器函数的函数体不会立即执行。 -  生成器(对象)可以使用next方法，next(generator) 会从函数的当前位置向后执行到之后碰到的第一个yield语句，会中断函数执行，并返回yield表达式的值，再次调用next函数，从上一次的中断点恢复执行，继续调用next函数，生成器函数如果结束执行了（显式或隐式调用了return语句），会抛出StopIteration异常。 -  next()方法超限会直接报错，如果不是有特别需求，一般推荐使用for循环遍历。 -  生成器对象只能逐次遍历一遍，不能再回头读取。 
### 2.生成器函数和普通函数的区别

生成器函数与普通函数的区别在于，生成器函数中使用了yield语句来产生值，而不是使用return语句返回值。当生成器函数被调用时，它会返回一个生成器对象，而不是直接执行函数体中的代码。**当生成器对象被迭代时，生成器函数中的代码会逐行执行，直到遇到yield语句，此时会暂停执行并将yield后面的值作为迭代器的下一个值返回。下一次迭代时，生成器函数会从yield语句后面的代码继续执行，直到再次遇到yield语句**，以此类推。

### 3.以下是一个简单的生成器函数的示例

它生成了从0开始的自然数序列：

return

numbers = natural_numbers()

难到numbers不应该等于函数natural_numbers的返回值None吗？

虽然有显式return语句（可以没有return），但是当python编译是执行到yield语句时，就会给函数natural_numbers打上生成器标签，于是调用该生成器函数natural_numbers可以返回一个生成器对象存到numbers。

```
def natural_numbers():
    n = 0
    while True:
        yield n
        n += 1
    return
numbers = natural_numbers()

```

通过迭代器的方式—next()方法依次获取序列中的值：

yield、return都不是生成器函数的返回值，只有当我对生成器对象使用nexth函数的时候，才会开始运行生成器函数本体

```
print(next(numbers))  # 输出：0
print(next(numbers))  # 输出：1
print(next(numbers))  # 输出：2


```

由于生成器对象是一种迭代器，因此可以在**for循环**中使用，例如：

```
for n in natural_numbers():
    if n &gt; 10:
        break
    print(n)


```

### 4.生成器函数执行逻辑
- 同一个生成器函数中yield语句可以有多个。
```
for i in range(5):
    yield i  #执行了5次yield语句。

```
- 遍历生成器函数对象时，函数执行到yield语句会中断执行，并返回yield表达式的值。- 再次遍历该对象时，函数从上一个yield断点位置继续执行，并执行到下一个yield语句。- 重复上一步，直到函数正常结束，或者遇到return语句。- return语句依然可以终止函数运行，但return语句的返回值不能被获取到。- return会导致当前函数返回，无法继续执行。生成器对象至此已经没有可迭代深度。- 继续使用next()方法，抛出StopIteration异常。- 如果函数没有显式的return语句，如果生成器函数执行到结尾（相当于执行了return None），一样会抛出StopIteration异常。
```
    def gen():
        print('line 1')
        yield 1
        print('line 2')
        yield 2
        print('line 3')
        return 3
        yield 4

```

### 5.next()
- 如果直接用next()方法调用生成器函数本身，那么每次都会重新生成一个生成器对象，也就无法对某一个生成器对象持续向下遍历。
```
    next(gen()) # line 1
    next(gen()) # line 1
    
    ```
    ```
    line 1
    1
    line 1
    1   
    

```
- 因此需要使用一个变量接收gen()返回的生成器对象。
```
    g = gen()
    print(g)
    
    ```
    ```
    &lt;generator object gen at 0x000001C19302C228&gt;
    

```
- 用next方法，逐次遍历该生成器对象，可以正常输出。
```
    print(next(g)) # line 1
    print(next(g)) # line 2
    

```

```
   line 1
   1
   line 2
   2
   

```
- 但是如果再继续用next()遍历，解释器会报错，StopIteration ，说明遍历超限了，函数已经在 return 3 处返回，不会执行到之后的yield
```
    print(next(g)) # StopIteration
    

```

```
   line 3
   
   ---------------------------------------------------------------------------
   
       StopIteration                             Traceback (most recent call last)
       &lt;ipython-input-91-9757af9844f9&gt; in &lt;module&gt;
       ----&gt; 1 print(next(g)) # StopIteration
       
       StopIteration: 3
       
       StopIteration: 3
   

```

### 6.作用
- 生成器可以用于处理大数据集，减少了内存的占用。此外，生成器还可以用于惰性计算，即仅在需要时才计算，从而提高程序的效率。- 生成器函数可以作为中断循环体的执行的隔断，每次调用生成器对象时，函数循环体才会继续运行一次。- 无限循环：
```
def counter():
	i = 0
	while True:
		i += 1
		yield i
def inc(c):
	return next(c)
c = counter()
print(inc(c))


```
- 计数器：
```
def inc():
	def counter():
		i = 0
		while True:
			i += 1
			yield i
	c = counter()
	return lambda : next(c)
foo = inc()
print(foo()) # 1
print(foo()) # 2
print(foo()) # 3


```
- 处理递归问题：原本的死循环递归，会引起解释器超过最大递归深度报错，但是插入yield语句之后，循环体被卡主了，被生成器对象调用一次才函数循环体会执行一次。
```
def fib():
	x = 0
	y = 1
	while True:
		yield y
		x, y = y, x+y
foo = fib()
for _ in range(5):
	print(next(foo))	


```

### 7.生成器函数语法糖-yield from
-  yield from是Python 3.3出现的新的语法 -  yield from iterable 是 for item in iterable: yield item 形式的语法糖 
```
def inc():
	for x in range(1000):
		yield x

def inc(): 
	yield from range(1000)  ## 解释器优化的语法糖



```

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>上述这份完整版的Python全套学习资料已经上传CSDN官方，朋友们如果需要可以微信扫描下方CSDN官方认证二维码 即可领取↓↓↓</mark>

<img src="https://img-blog.csdnimg.cn/267b263b1a904df391a976f922ec2b8e.png#pic_center" alt="在这里插入图片描述">
