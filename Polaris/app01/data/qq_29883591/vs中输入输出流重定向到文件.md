
--- 
title:  vs中输入输出流重定向到文件 
tags: []
categories: [] 

---
在vs中，有的时候我们在输入的时候需要输入很多东西，然后输出结果后，发现出现问题了，之后调试又得输入大量的东西，这是很让人头疼的事情，为此我们可以将输入重定向到文件中，将我们需要的输入存储到一个文件中，在运行vs时会自动读取文件里的东西取代dos窗口的输入，这样就为我们省去了很多的麻烦。

下面看一具体的过程（很简单的过程）：

在vs的窗口中，点击项目-》属性，如下图所示：

<img src="https://img-blog.csdn.net/20170404202408314?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

点击属性后，在命令参数中填写“&lt;data.txt”,注意，其中“&lt;”是不可变的，后面的data.txt是文件名，存放输入的数据。

<img src="https://img-blog.csdn.net/20170404202515416?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

在点击确定后，然后运行相应的程序，便可以成功从文件中读取数据了。

对于将cmd窗口中的输出数据重定向到文件也是一样的道理，只需要将命令参数修改为“&gt;data.txt”，如下图：

<img src="https://img-blog.csdn.net/20170406210039416?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

好了，这是一个使用的小技巧，就讲到这里了。
