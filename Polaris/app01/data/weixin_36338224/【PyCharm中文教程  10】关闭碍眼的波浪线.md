
--- 
title:  【PyCharm中文教程  10】关闭碍眼的波浪线 
tags: []
categories: [] 

---
下面我先给出了一小段代码示例，思考一下，为什么name，my_name 不会有波浪线，而 myname 和 wangbm 会有波浪线呢？

<img src="https://img-blog.csdnimg.cn/20210309084054262.png" alt="">

Pycharm 本身会实时地对变量名进行检查，如果变量名不是一个已存在的英文单词，就会出现一条波浪线，当一个变量里有多个单词时，Python 推荐的写法是用下划线来分隔（其他语言可能会习惯使用`驼峰式命名法` ，但 Python 是使用下划线），所以在 Pycharm 看来 my_name 是规范的，而 myname 会被当成是一个单词对待，由于它在单词库里并没有它，所以 myname 是不规范的。

每个人的变量命名习惯不一样，如何你在项目里大量使用了 myname 这种风格的变量命名方法，像下面这样（随便找了一段 cloudinit 的代码），是让人挺不舒服的，总有一种代码有 bug 的错觉。

<img src="https://img-blog.csdnimg.cn/20210309084054599.png" alt="">

那么如何关闭这个非语法级别的波浪线呢？很简单，它的开关就在你的右下角那个像 人头像 一样的按钮

<img src="https://img-blog.csdnimg.cn/20210309084054825.png" alt="">

然后选择 `Syntax` 级别的即可。同样一段代码，效果如下，干净了很多。

<img src="https://img-blog.csdnimg.cn/2021030908405542.png" alt="">

文章最后给大家介绍三个我自己写的在线文档：

**第一个文档**：

花了两个多月的时间，整理了 100 个 PyCharm 的使用技巧，为了让新手能够直接上手，我花了很多的时间录制了上百张 GIF 动图，有兴趣的前往在线文档阅读。

<img src="https://img-blog.csdnimg.cn/20210309084055563.png" alt="">

**第二个文档**：

系统收录各种 Python 冷门知识，Python Shell 的多样玩法，令人疯狂的 Python 炫技操作，Python 的超详细进阶知识解读，非常实用的 Python 开发技巧等。

<img src="https://img-blog.csdnimg.cn/20210309084055904.png" alt="">

**第三个文档**：

花了三个月时间写的一本 适合零基础入门 Python 的全中文教程，搭配大量的代码案例，让初学者对 代码的运作效果有一个直观感受，教程既有深度又有广度，每篇文章都会标内容的难度，是基础还是进阶的，可供读者进行选择，是一本难得的 Python 中文电子教程。

<img src="https://img-blog.csdnimg.cn/20210309084056720.png" alt="">
