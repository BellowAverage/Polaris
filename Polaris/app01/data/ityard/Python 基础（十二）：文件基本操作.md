
--- 
title:  Python 基础（十二）：文件基本操作 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - - - 


## 1 简介

<img src="https://img-blog.csdnimg.cn/20191223200746155.jpg#pic_center" alt="" height="300">

在编程工作中文件操作还是比较常见的，基本文件操作包括：创建、读、写、关闭等，Python 中内置了一些文件操作函数，我们使用 Python 操作文件还是很方便的。

## 2 基本操作

### 2.1 创建

Python 使用 `open()` 函数创建或打开文件，语法格式如下所示：

```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

```

参数说明如下所示：
-  **file**：表示将要打开的文件的路径，也可以是要被封装的整数类型文件描述符。 -  **mode**：是一个可选字符串，用于指定打开文件的模式，默认值是 `'r'`（以文本模式打开并读取）。可选模式如下： 
<th align="left">模式</th><th align="left">描述</th>
|------
<td align="left">r</td><td align="left">读取（默认）</td>
<td align="left">w</td><td align="left">写入，并先截断文件</td>
<td align="left">x</td><td align="left">排它性创建，如果文件已存在则失败</td>
<td align="left">a</td><td align="left">写入，如果文件存在则在末尾追加</td>
<td align="left">b</td><td align="left">二进制模式</td>
<td align="left">t</td><td align="left">文本模式（默认）</td>
<td align="left">+</td><td align="left">更新磁盘文件（读取并写入）</td>
-  **buffering**：是一个可选的整数，用于设置缓冲策略。 -  **encoding**：用于解码或编码文件的编码的名称。 -  **errors**：是一个可选的字符串，用于指定如何处理编码和解码错误（不能在二进制模式下使用）。 -  **newline**：区分换行符。 -  **closefd**：如果 closefd 为 False 并且给出了文件描述符而不是文件名，那么当文件关闭时，底层文件描述符将保持打开状态；如果给出文件名，closefd 为 True （默认值），否则将引发错误。 -  **opener**：可以通过传递可调用的 opener 来使用自定义开启器。 
以 txt 格式文件为例，我们不手动创建文件，通过代码方式来创建，如下所示：

```
open('test.txt', mode='w',encoding='utf-8')

```

执行完上述代码，就为我们创建好了 test.txt 文件。

### 2.2 写入

上面我们创建的文件 test.txt 没有任何内容，我们向这个文件中写入一些信息，对于写操作，Python 文件对象提供了两个函数，如下所示：

<th align="left">函数</th><th align="left">描述</th>
|------
<td align="left">write(str)</td><td align="left">将字符串写入文件，返回写入字符长度</td>
<td align="left">writelines(s)</td><td align="left">向文件写入一个字符串列表</td>

我们使用这两个函数向文件中写入一些信息，如下所示：

```
wf = open('test.txt', 'w', encoding='utf-8')
wf.write('Tom\n')
wf.writelines(['Hello\n', 'Python'])
# 关闭
wf.close()

```

上面我们使用了 close() 函数进行关闭操作，如果打开的文件忘记了关闭，可能会对程序造成一些隐患，为了避免这个问题的出现，可以使用 `with as` 语句，通过这种方式，程序执行完成后会自动关闭已经打开的文件。如下所示：

```
with open('test.txt', 'w', encoding='utf-8') as wf:
    wf.write('Tom\n')
    wf.writelines(['Hello\n', 'Python'])

```

### 2.3 读取

之前我们已经向文件中写入了一些内容，现在我们读取一下，对于文件的读操作，Python 文件对象提供了三个函数，如下所示：

<th align="left">函数</th><th align="left">描述</th>
|------
<td align="left">read(size)</td><td align="left">读取指定的字节数，参数可选，无参或参数为负时读取所有</td>
<td align="left">readline()</td><td align="left">读取一行</td>
<td align="left">readlines()</td><td align="left">读取所有行并返回列表</td>

我们使用上面三个函数读取一下之前写入的内容，如下所示：

```
with open('test.txt', 'r', encoding='utf-8') as rf:
    print('readline--&gt;', rf.readline())
    print('read--&gt;', rf.read(6))
    print('readlines--&gt;', rf.readlines())

```

### 2.4 定位

Python 提供了两个与文件对象位置相关的函数，如下所示：

<th align="left">函数</th><th align="left">描述</th>
|------
<td align="left">tell()</td><td align="left">返回文件对象在文件中的当前位置</td>
<td align="left">file.seek(offset[, whence])</td><td align="left">将文件对象移动到指定的位置；offset 表示移动的偏移量；whence 为可选参数，值为 0 表示从文件开头起算（默认值）、值为 1 表示使用当前文件位置、值为 2 表示使用文件末尾作为参考点</td>

下面通过示例对上述函数作进一步了解，如下所示：

```
with open('test.txt', 'rb+') as f:
    f.write(b'123456789')
    # 文件对象位置
    print(f.tell())
    # 移动到文件的第四个字节
    f.seek(3)
    # 读取一个字节，文件对象向后移动一位
    print(f.read(1))
    print(f.tell())
    # 移动到倒数第二个字节
    f.seek(-2, 2)
    print(f.tell())
    print(f.read(1))

```

### 2.5 其他

除了上面那些函数，Python 文件对象还有一些其他方法，如：isatty() 和 truncate()，但它们的出场率较低，没什么存在感。

<img src="https://img-blog.csdnimg.cn/2019122421030477.jpeg#pic_center" alt="" height="300">

直接通过示例简单了解一下，如下所示：

```
with open('test.txt', 'r+') as f:
    # 检测文件对象是否连接到终端设备
    print(f.isatty())
    # 截取两个字节
    f.truncate(2)
    print(f.read())

```

参考： 

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">
