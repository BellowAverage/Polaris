
--- 
title:  【PyCharm中文教程  07】程序结束了如何继续调试 
tags: []
categories: [] 

---
假如我们在一个爬虫的项目中，会使用到 正则表达式 来匹配我们想要抓取的内容。正则这种东西，有几个人能够一步到位的呢，通常都需要经过很多次的调试才能按预期匹配。在我们改了一次正则后，运行了下，需要重新向网站抓取请求，才能发现没有匹配上，然后又改了一版，再次运行同样需要发起请求，结果还是发现还是没有匹配上，往往复复，正则不好的同学可能要进行几十次的尝试。

（上面这个例子可能不太贴切，毕竟是有很多种方法实现不用重新发请求，只是列举了一种很笨拙且低效的调试过程，你看看就好了）

而我们在这几十次的调试中，向同一网站发起请求都是没有意义的重复工作。如果在 Pycharm 中可以像 IPython Shell 和 Jupyter Notebook 那样，可以记住运行后所有的变量信息，可以在不需要重新运行项目或脚本，就可以通过执行命令表达式，来调整我们的代码，进行我们的正则调试。

答案当然是有。

假如我在调试如下几行简单的代码。在第 3 行处打了个断点。然后点击图示位置 `Show Python Prompt` 按钮。

<img src="https://img-blog.csdnimg.cn/20210305100413452.png" alt="">

就进入了 `Python Shell` 的界面，这个Shell 环境和我们当前运行的程序环境是打通的，变量之间可以互相访问，这下你可以轻松地进行调试了。

<img src="https://img-blog.csdnimg.cn/20210305100414101.png" alt="">

上面我们打了个断点，是为了方便说明这个效果。并不是说一定要打断点。如果不打断点，在脚本执行完成后，也仍然可以在这个界面查看并操作所有变量。

<img src="https://img-blog.csdnimg.cn/20210305100414525.png" alt="">

现在我们已经可以满足我们的调试的需求，但是每次运行脚本，都要手动点击 `Show Python Prompt` ，有点麻烦。嗯？其实这个有地方可以设置默认打开的。这个开关还比较隐秘，一般人还真发现不了。

你需要点击图示位置 `Edit Configurations` 处。

<img src="https://img-blog.csdnimg.cn/20210305100414874.png" alt="">

然后在这里打勾选中。

<img src="https://img-blog.csdnimg.cn/20210305100415527.png" alt="">

设置上之后，之后你每次运行后脚本后，都会默认为你存储所有变量的值，并为你打开 console 命令行调试界面。

除了上面这种方法，其实还有一种方法可以在调试过程中，执行命令表达式，而这种大家可能比较熟悉了，这边也提一下，就当是汇总一下。但是从功能上来说，是没有上面这种方法来得方便易用的。因为这种方法，必须要求你使用 debug 模式运行项目，并打断点。

使用方法就是，在你打了断点后，在图示位置处，点击右键使用 `Evaluate Expression`

<img src="https://img-blog.csdnimg.cn/20210305100415933.png" alt="">

就弹出了一个 `Evaluate Expression` 窗口，这里 可以运行命令表达式，直接操作变量。

<img src="https://img-blog.csdnimg.cn/20210305100416296.png" alt="">

文章最后给大家介绍三个我自己写的在线文档：

**第一个文档**：

花了两个多月的时间，整理了 100 个 PyCharm 的使用技巧，为了让新手能够直接上手，我花了很多的时间录制了上百张 GIF 动图，有兴趣的前往在线文档阅读。

<img src="https://img-blog.csdnimg.cn/20210305100419838.png" alt="">

**第二个文档**：

系统收录各种 Python 冷门知识，Python Shell 的多样玩法，令人疯狂的 Python 炫技操作，Python 的超详细进阶知识解读，非常实用的 Python 开发技巧等。

<img src="https://img-blog.csdnimg.cn/20210305100420580.png" alt="">

**第三个文档**：

花了三个月时间写的一本 适合零基础入门 Python 的全中文教程，搭配大量的代码案例，让初学者对 代码的运作效果有一个直观感受，教程既有深度又有广度，每篇文章都会标内容的难度，是基础还是进阶的，可供读者进行选择，是一本难得的 Python 中文电子教程。

<img src="https://img-blog.csdnimg.cn/20210305100421794.png" alt="">
