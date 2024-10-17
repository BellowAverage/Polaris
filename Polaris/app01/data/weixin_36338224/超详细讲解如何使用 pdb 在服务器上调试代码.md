
--- 
title:  超详细讲解如何使用 pdb 在服务器上调试代码 
tags: []
categories: [] 

---
Pycharm 的图形化界面虽然好用，但是在某些场景中，是无法使用的。而 Python 本身已经给我们提供了一个调试神器 -- pdb，可能你还不知道它，为了讲解这个神器，我写了这篇文章来帮助你轻松的理解它。

### 1. 准备文件

在调试之前先将这两个文件准备好（做为演示用），并放在同级目录中。

`utils.py`

```
def sum(mylist):
    result = 0
    for item in mylist:
        result += item
    return result
```

`pdb_demo.py`

```
import utils

def myfunc(mylist):
    result = utils.sum(mylist)
    print(result)


if __name__ == '__main__':
    print("----start----")
    myfunc([1,2,3,4])
    print("----end-----")
```

### 2. 进入调试模式

主要有两种方法

做为脚本调用，方法很简单，就像正常执行python脚本一样，只是多加了`-m pdb`

```
ptyhon -m pdb pdb_demo.py
```

使用这个方式进入调试模式，会在脚本的第一行开始单步调试。

<img src="https://img-blog.csdnimg.cn/20201030111532118.png" alt="">

对于单文件的脚本并没有什么问题，如果是一个大型的项目，项目里有很多的文件，使用这种方式只能大大降低我们的效率。

一般情况下，都会直接在你需要的地方打一个断点，那如何打呢？

只需在你想要打断点的地方加上这两行。

```
import pdb
pdb.set_trace()
```

然后执行时，也不需要再指定`-m pdb`了，直接`python pdb_demo.py` ，就会直接在这个地方暂停。

<img src="https://img-blog.csdnimg.cn/20201030111533830.png" alt="">

<img src="https://img-blog.csdnimg.cn/20201030111536402.png" alt="">

### 3. 调试指令

熟悉 Pycharm 的人都知道，我们执行下一步，执行到下一个断点是

同样的，pdb 也需要你更多记这样的命令。

当你看到pdb模式的标识符 `(Pdb)`时，就可以输入这样的命令。

我在这里将这些指令按使用频度分为三个等级。

**最常用**

<th align="center">指令</th><th align="center">英文</th><th align="center">解释</th>
|------
<td align="center">n</td><td align="center">Next</td><td align="center">下一步</td>
<td align="center">l</td><td align="center">list</td><td align="center">列出当前断点处源码</td>
<td align="center">p</td><td align="center">print</td><td align="center">打印变量</td>
<td align="center">s</td><td align="center">step into</td><td align="center">执行当前行，可以进入函数</td>
<td align="center">r</td><td align="center">return</td><td align="center">运行完当前函数，返回结果</td>
<td align="center">c</td><td align="center">continue</td><td align="center">执行到下一断点或者结束</td>
<td align="center">b</td><td align="center">break</td><td align="center">设置断点</td>
<td align="center">q</td><td align="center">quit</td><td align="center">退出程序</td>

**有时使用**

<th align="center">指令</th><th align="center">英文</th><th align="center">解释</th>
|------
<td align="center">a</td><td align="center">args</td><td align="center">列出当前函数的参数</td>
<td align="center">pp</td><td align="center">pprint</td><td align="center">一种可视化更好的打印</td>
<td align="center">j</td><td align="center">jump</td><td align="center">跳到指定行</td>
<td align="center">cl</td><td align="center">clear</td><td align="center">清除断点</td>
<td align="center">w</td><td align="center">where</td><td align="center">打印当前堆栈</td>
<td align="center">u</td><td align="center">up</td><td align="center">执行跳转到当前堆栈的上一层</td>
<td align="center">unt</td><td align="center">until</td><td align="center">行数递增执行(忽略循环和函数)</td>
<td align="center">ll</td><td align="center">longlist</td><td align="center">列出更多的源码</td>
<td align="center">run/restart</td><td align="center">run</td><td align="center">重新启动 debug(-m pdb)</td>

**几乎不用**

<th align="center">指令</th><th align="center">英文</th><th align="center">解释</th>
|------
<td align="center">tbreak</td><td align="center">temporary break</td><td align="center">临时断点</td>
<td align="center">disable</td><td align="center"></td><td align="center">停用断点</td>
<td align="center">enable</td><td align="center"></td><td align="center">启用断点</td>
<td align="center">alias</td><td align="center"></td><td align="center">设置别名</td>
<td align="center">unalias</td><td align="center"></td><td align="center">删除别名</td>
<td align="center">whatis</td><td align="center"></td><td align="center">打印对象类型</td>
<td align="center">ignore</td><td align="center"></td><td align="center">设置忽略的断点</td>
<td align="center">source</td><td align="center"></td><td align="center">列出给定对象的源码</td>

其上全部是我翻译自官方文档，原文在这里：

其实你大可不必死记这些命令，忘记的时候，只要敲入`help`并回车，就可以看所有的指令了。

<img src="https://img-blog.csdnimg.cn/20201030111537235.png" alt="">

### 4. 开始调试

这里就几个最常用的指定，来演示一遍。

<img src="https://img-blog.csdnimg.cn/20201030111539454.png" alt="">

这个调试过程，我加了些注释，你应该能够很轻易地理解这种调试方式。

今天pdb的调试内容大概就是这些，你学会了吗？

看到上面截图的时间了吧？是的，又是一个深夜写的文章。希望对你会有所帮助。
