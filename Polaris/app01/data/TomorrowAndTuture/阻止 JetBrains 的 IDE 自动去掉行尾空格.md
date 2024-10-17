
--- 
title:  阻止 JetBrains 的 IDE 自动去掉行尾空格 
tags: []
categories: [] 

---
### 起因

最近换了电脑，然后重新装了一堆堆 IDE，包括 Pycharm、RubyMine 和 GoLand等，发现 RubyMine 修改某一行的代码后，Ctrl + S 保存，**结果 IDE 将文件的所有行末尾的空格都自动给去掉了！！！**

但是这样就会有一个问题，本来我可能就修改了一个地方，结果 Ctrl + K 进行 commit 的时候，却看到一大堆改动点，结果弄得我自己都不知道我真正修改的是哪些地方。虽然我理解 IDE 这样做完全是出于好心，但是对于一个程序猿来说，不可以自己控制到底提交哪些改动，这是坚决不能忍的！！！

### 修复

设置方式如下：

File -&gt; Settings -&gt; Editor -&gt; General -&gt; 去掉勾选标记处：

<img alt="" height="720" src="https://img-blog.csdnimg.cn/04d552b5939849ffba5cae113f6d5ee7.png" width="998">

旧版的可能在 Other 的选项里边。

我自己设置以后，还在 Code Style 里边 Disabled 了一个什么东东（就是叹号！那个提示），然后才生效的。

<img alt="" height="1032" src="https://img-blog.csdnimg.cn/0ae239b437234afdb882521bee611c2d.png" width="1200">

 
