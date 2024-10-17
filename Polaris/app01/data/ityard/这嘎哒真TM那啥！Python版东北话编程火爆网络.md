
--- 
title:  这嘎哒真TM那啥！Python版东北话编程火爆网络 
tags: []
categories: [] 

---
>  
  开源最前线（ID：OpenSourceTop） 猿妹综合整理 
 

还记得12月份刷爆朋友圈的那个文言文编程语言么？

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X2pwZy9rT1ROa2ljNWdWQkYwR0ZOVVdDU05DaWJzVzZGOXBQRnZVcFA3TTI3MzYyNXQyYUE3ZHBYZGljZDBXSGQ2ekljMWRPWjRCamNnYWlhdUFVWkZ2enFwN3A5RUEvNjQw?x-oss-process=image/format,png">

这个项目是一位名为Huang Lingdong的大四学生创建的，当时，就连中科院计算所研究员、机器翻译领域知名专家刘群老师都赞叹道：后生可畏

近日，Github上一个名叫dongbei的开源编程项目，再一次引起大家关注，这是一个以东北方言词汇为基本关键字的编程语言——dongbei。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9rT1ROa2ljNWdWQkZTbWNlQ0FpYVVzZUZjdWg3UFlCN3hMb251RHFJM1RGSnd3aWFCdUFnVkZta1FHM2ZEdmVaVmRTTkt4VHVQd0k2cWx4MWZLSnNrVU43US82NDA?x-oss-process=image/format,png">

该项目作者是一位 Google 的高级软件工程师/技术主管，同时也是 Google C++测试框架 googletest 以及 googlemock 的原作者。

根据项目作者介绍：

>  
  dongbei可是填补了世界方言编程地图上的一大片儿空地啊！这么说吧，谁要是看了 dongbei 程序能憋住了不笑，我敬他是纯爷们儿！ 
  那它有啥特点咧？多了去了： 
  简单啊！小学文化程度就行。您能看懂春晚不？能？那就没问题。 
  好读啊！看着看着包您不由自主地念出声儿来。 
  开心啊！呃，做人嘛，最重要的是要开心。 
  开源啊！不但不要钱，而且不要脸 -- 随时随地欢迎东北话高手打脸指正。 
  总而言之，dongbei 语言具有极高的娱技比（娱乐精 
 

dongbei 编程语言的开发采用了业界领先的 TDD（TreeNewBee-Driven Development） 方式。 具体地说，就是每个功能都是先把文案写好，八字没一撇牛皮就吹起来了，然后根据牛皮写测试案例，最后再实现功能让牛皮不被吹破。 这样做有两大好处：第一每个功能都是有的放矢，不值得 tree new bee 的功能一概没有。 第二确保了每个功能都有文案负责吹嘘，开发者绝对不会养在深闺无人识。

再来就是系统支持的问题了，donbei只需要保证开发环境有**Python 3** ，直接下载GitHub项目，跑src/dongbei.py，这事儿就成了。

我们还是先来个东北味儿的hello World程序吧：

```
唠唠：“唉呀，这嘎哒真他妈那啥！”。

```

用 utf-8 编码保存。要是编辑器因为编码错误埋汰你，那就把文件内容改成：

```
# -*- coding: utf-8 -*-

唠唠：“唉呀，这嘎哒真他妈那啥！”。

```

再试，应该就成了。然后在命令行窗口运行：

```
src/dongbei.py hello-world.dongbei

```

你应该看到执行结果：

```
唉呀，这嘎哒真他妈那啥！

```

**语法规则**

学习一门语言，先得了解它的词法、语法和语义，下面我们就一点一点来了解一下：

**词法**

**字符串常量**

一行代码当中，要是出现配对的中文全角双引号，比如

```
...“我是一个字符串”...

```

那么引号当中的内容（我是一个字符串）会被当成一个字符串常量。

**常数**

除了用阿拉伯数字表示的十进制整数（比如 2、42、250，等等），0 到 10 的常数也可以用中文表达：

```
零一二三四五六七八九十

```

二也可以写成两或者俩。三也可以写成仨。

**语句**

一个 dongbei 程序是由一串语句组成的。每个语句以句号（。）结束。为了表达程序员炽热的感情，也可以用感叹号（！）结束，意思和句号是一样一样的。请大家根据自己的心情任选使用。

**1、变量**

dongbei 语言允许使用任何字符串做变量名。定义变量如下：

```
老王是活雷锋。

```

**2、给变量赋值**

dongbei 语言不整“赋值”这种文绉绉的词儿。咱们叫“装”。比如：

```
老王装二。

```

可以理解为 C 语言的

```
lao_wang = 2;

```

要把一个活雷锋的值清空回到原始状态，可以用削：

```
削老王。

```

过后老王就啥也不是了。

**3、增减变量**

活雷锋除了会装，加加减减也是常见的操作。按没病走两步的规矩，这些操作的名字叫做：走走、稍稍、走X步、稍X步。比如：

```
老张装二。  # 现在老张等于2
老张走走。  # 现在老张等于3
老张走两步。  # 现在老张等于5
老张稍稍。  # 现在老张等于4
老张稍五步。  # 现在老张等于-1

```

**4、输出**

要输出信息，咱们得说“唠唠”。假定要说的信息是 YY，就得写

```
唠唠：YY。

```

**5、循环**

磨叽，就是一遍一遍循环。 所以，在 dongbei 语言里循环的写法是：

```
老王从一到五磨叽：  # 老王从1走到5。
  唠唠：老王！  # 打印老王的当前值。
磨叽完了！  # 循环结束。

```

运行结果如下：

```
1
2
3
4
5

```

**6、条件**

虽然 dongbei 人都是活雷锋，干活的时候该讲条件还是要讲条件的。寻思是一项很有用的技能！比如有件事情（不妨叫做 XXX）只想在某个条件（不妨叫 CCC）成立的时候再做，就写：

```
寻思：CCC ？
要行咧就 XXX

```

要是 CCC 不成立的时候俺们有另外一件事情 YYY 要做，那就写：

```
寻思：CCC ？
要行咧就 XXX
要不行咧就 YYY
```

**7、套路**

“套路”这名字听着吓人，其实就是给一串常用的组合拳取一个名字，定义套路用这个格式：

```
套路名字 咋整：
  ...  # 爱做的事儿
整完了。

```

下面定义一个叫“写九九表”的套路。注意定义套路本身不会让这个套路真的跑起来。所以下面这段程序跑的结果是啥也不做。

```
写九九表咋整：  # 定义套路 写九九表。
  老王从1到9磨叽：
    老张从老王到9磨叽：
      唠唠：老王、“*”、老张、“=”、老王乘老张。  # 打印 X*Y=Z
    磨叽完了。
    唠唠：“”。  # 空一行。
  磨叽完了。
整完了。  # 结束套路定义。

```

想把上面的套路跑一遍，你得写：

```
整写九九表。

```

然后，你就可以输出一份九九乘法表啦：

```
1*1=1
1*2=2
1*3=3
...

8*8=64
8*9=72

9*9=81

```

项目的issue上，更是好多热心网友给出建议：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9rT1ROa2ljNWdWQkZTbWNlQ0FpYVVzZUZjdWg3UFlCN3hMaWFQSEY1S2g4ZzRYTFhsSFBsb1l6TGdmdFBpYWliWlJzV3JJMHNkaWF5Vnp6Nzkzc3dOaWJIemljQjJnLzY0MA?x-oss-process=image/format,png">

你觉得这门东北方言的编程语言好不好使呢？如果你也对它感兴趣，可以去Github上下载下来好好研究研究。

最后附上Github地址：https://github.com/zhanyong-wan/dongbei

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
