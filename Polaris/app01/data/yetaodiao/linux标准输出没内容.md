
--- 
title:  linux标准输出没内容 
tags: []
categories: [] 

---
linux标准输入是文件描述符0。它是命令的输入，缺省是键盘，也可以是文件或其他命令的输出。

linux标准输出是文件描述符1。它是命令的输出，缺省是屏幕，也可以是文件。

linux标准错误是文件描述符2。这是命令错误的输出，缺省是屏幕，同样也可以是文件。

重定向的使用有如下规律：

1）标准输入0、输出1、错误2需要分别重定向，一个重定向只能改变它们中的一个。

2）标准输入0和标准输出1可以省略。（当其出现重定向符号左侧时）

3）文件描述符在重定向符号左侧时直接写即可，在右侧时前面加&amp;。

4）文件描述符与重定向符号之间不能有空格！

command &lt; filename                         把标准输入重定向到filename文件中

command 0&lt; filename                       把标准输入重定向到filename文件中



command &gt; filename                         把标准输出重定向到filename文件中(覆盖)

command 1&gt; fielname                       把标准输出重定向到filename文件中(覆盖)



command &gt;&gt; filename                       把标准输出重定向到filename文件中(追加)

command 1&gt;&gt; filename                     把标准输出重定向到filename文件中(追加)



command 2&gt; filename                       把标准错误重定向到filename文件中(覆盖)

command 2&gt;&gt; filename                     把标准输出重定向到filename文件中(追加)



command &gt; filename 2&gt;&amp;1               把标准输出和标准错误一起重定向到filename文件中(覆盖)

command &gt;&gt; filename 2&gt;&amp;1             把标准输出和标准错误一起重定向到filename文件中(追加)



command &lt; filename &gt;filename2        把标准输入重定向到filename文件中，把标准输出重定向

                                                        到filename2文件中

command 0&lt; filename 1&gt; filename2   把标准输入重定向到filename文件中，把标准输出重定向

                                                        到filename2文件中



下面还几种不常见的用法：

n&lt;&amp;- 表示将 n 号输入关闭

&lt;&amp;- 表示关闭标准输入（键盘）

n&gt;&amp;- 表示将 n 号输出关闭

&gt;&amp;- 表示将标准输出关闭 
