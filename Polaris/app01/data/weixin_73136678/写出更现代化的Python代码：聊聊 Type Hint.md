
--- 
title:  写出更现代化的Python代码：聊聊 Type Hint 
tags: []
categories: [] 

---
`Type Hint`是 Python 3.5 新增的支持，中文可以译为 `类型提示`。屏幕前的你或许听过，又或许没有。所以今天，让我们一起了解了解。**本文基于 `Python 3.10.4`，部分代码需要在 `Python 3.10.0` 及以上运行，原因在后续文章中会有说明****本文的代码编辑器为 VS Code ，您可以选择其他现代编辑器/IDE以体验**

#### 为什么需要 Type Hint

简而言之，按我的理解，`type hint`的目的是**写给“别人”看**。这个“别人”，就包括`代码编辑器`、`其他阅读代码的人`和`几天后的你自己`。 废话不多说，Show You My Code!

#### 开始写代码

现在我们假设，你想写一个函数，用处是**统计给定字符串中某个字符出现的次数**，于是你大手一挥，写下了这样的代码：

```
def count_char(text, char):
    return text.啥来着？？？
复制代码
```

尴尬的是，你记得`str`类有这个方法，但却忘记了这个方法叫啥了，看看编辑器的自动提示？

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/76fdff9af48c084dfbdf8fa6e3ee114d.webp?x-oss-process=image/format,png">

遗憾的是，编辑器不知道你的text是啥类型的，自然没法帮你补全。那我们能不能告诉它：这是个`str`呢？可以，给参数名后面加个`: str`就好了 **（这个空格不是必须的，只是为了好看）**

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/3cb4b90e9f1193eaf0affbdd0945f48b.webp?x-oss-process=image/format,png">

这就是`Type Hint`的作用，通过**显示指明类型告诉调用者和编辑器：我需要什么类型**。这能帮助你充分利用现代编辑器的自动提示功能，并让你写出的代码更加易于阅读和维护。

#### 一个注意点

在继续下面内容之前，我们得明确一件事：**Type Hint只是手动指明我们需要的类型，但它不是强制的**。举个栗子，对于这个函数，正确的使用如下：

```
def count_char(text: str, char):
    return text.count(char)

# text 参数为 str
print(count_char("Hello World", "e"))
复制代码
```

但如果我们给`text`传了个别的类型，比如`int`，会发生什么？答案是仍然能编译通过，只是执行时报错而已。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/4d6430b12e0542eae195dbb2d9dd0fed.webp?x-oss-process=image/format,png">

这就是为什么它叫`Type Hint`：只是提示，并非强制。 当然，我们也可以借助其他手段来实现强制的类型限定，比如借助 `mypy`

mypy

安装`mypy`很容易，只需要`pip install `
