
--- 
title:  Python办公神器：教你如何快速分拆、删页、合并PDF文件 
tags: []
categories: [] 

---
>  
 哈喽大家好，我是了不起，今天教你如何用Python快速分拆、删页、合并PDF文件 


<img src="https://img-blog.csdnimg.cn/img_convert/0661f53b93f577eb1cc6ce7009edba1b.png" alt="">

#### 介绍

有时我们可能需要对PDF文件进行一些处理，例如分拆、删页、合并等。这些操作在一些专业的PDF软件中可能比较容易实现，但是如果我们想要用Python来自动化或批量处理这些操作呢？有没有什么简单而强大的Python库可以帮助我们呢？

答案是肯定的。在Python中，有一个叫做`PyPDF2`的库，它可以让我们用简单的代码来处理PDF文件。

在这篇教程中，我们将学习如何使用`PyPDF2`库来快速分拆、删页、合并PDF文件。我们将通过一些实际的例子来演示这些操作，并介绍一些常用的API和参数。在开始之前，我们需要先安装`PyPDF2`库。

<img src="https://img-blog.csdnimg.cn/img_convert/e384019798708d6f5be6a88f09261adc.png" alt="">

#### 安装

要安装`PyPDF2`库，我们可以使用pip命令：

```
pip install PyPDF2   

```

安装完成后，我们就可以在Python中导入`PyPDF2`库了：

```
import PyPDF2   

```

#### 分拆

分拆（Split）是指将一个PDF文件分成多个小的PDF文件，每个小文件只包含原文件中的一部分页面。这样做的目的可能是为了方便管理或传输这些文件，或者只需要其中的某些页面。

要实现分拆操作，我们需要使用`PyPDF2.PdfReader`类来读取原始的PDF文件，并使用`PyPDF2.PdfWriter`类来创建新的PDF文件，并将需要的页面写入其中。下面是一个简单的例子：

```
# 读取原始的PDF文件
pdf_reader = PyPDF2.PdfReader("original.pdf")

# 获取原始文件中的总页数
total_pages = len(pdf_reader.pages)

# 创建一个空列表，用于存放新创建的PDF文件名
new_files = []

# 循环遍历每一页
for i in range(total_pages):
    # 创建一个新的PdfFileWriter对象
    pdf_writer = PyPDF2.PdfWriter()
    # 获取当前页对象
    page = pdf_reader.pages[i]
    # 将当前页对象添加到PdfFileWriter对象中
    pdf_writer.add_page(page)
    # 创建一个新的PDF文件名，格式为"original_页码.pdf"
    new_file = f"original_{<!-- -->i+1}.pdf"
    # 将新的PDF文件名添加到列表中
    new_files.append(new_file)
    # 打开一个新的PDF文件，以二进制写入模式
    with open(new_file, "wb") as f:
        # 将PdfFileWriter对象中的内容写入到新的PDF文件中
        pdf_writer.write(f)

# 打印出新创建的PDF文件名
print(new_files)

```

运行上面的代码，我们可以得到如下的输出：

```
['original_1.pdf', 'original_2.pdf', 'original_3.pdf', 'original_4.pdf', 'original_5.pdf']

```

这说明我们已经成功地将原始的PDF文件分拆成了5个小的PDF文件，每个文件只包含原始文件中的一 页。我们可以打开这些文件，查看它们的内容是否正确。

<img src="https://img-blog.csdnimg.cn/img_convert/13f3c9b8f00a910fb19b8b195132a731.png" alt="">

#### 删页

删页（Delete）是指将一个PDF文件中的某些页面删除，只保留需要的页面。这样做的目的可能是为了减少文件的大小或去除不相关的内容。

要实现删页操作，我们也需要使用`PyPDF2.PdfReader`类来读取原始的PDF文件，并使用`PyPDF2.PdfWriter`类来创建新的PDF文件，并将需要保留的页面写入其中。不同的是，我们需要指定要删除的页面的索引或范围，并在循环遍历每一页时跳过这些页面。下面是一个简单的例子：

```
# 读取原始的PDF文件
pdf_reader = PyPDF2.PdfReader("original.pdf")

# 获取原始文件中的总页数
total_pages = len(pdf_reader.pages)

# 指定要删除的页面索引或范围，从0开始计数
delete_pages = [0, 2, 4]

# 创建一个新的PdfFileWriter对象
pdf_writer = PyPDF2.PdfWriter()

# 循环遍历每一页
for i in range(total_pages):
    # 如果当前页索引不在要删除的页面列表中，则保留该页
    if i not in delete_pages:
        # 获取当前页对象
        page = pdf_reader.pages[i]
        # 将当前页对象添加到PdfFileWriter对象中
        pdf_writer.add_page(page)

# 创建一个新的PDF文件名，格式为"original_deleted.pdf"
new_file = "original_deleted.pdf"

# 打开一个新的PDF文件，以二进制写入模式
with open(new_file, "wb") as f:
    # 将PdfFileWriter对象中的内容写入到新的PDF文件中
    pdf_writer.write(f)

# 打印出新创建的PDF文件名
print(new_file)

```

运行上面的代码，我们可以得到如下的输出：

```
original_deleted.pdf   

```

这说明我们已经成功地将原始的PDF文件中的第1、3、5页删除，只保留了第2、4页。我们可以打开新创建的PDF文件，查看它们的内容是否正确。

#### 合并

合并（Merge）是指将多个PDF文件合并成一个大的PDF文件，包含所有原始文件中的所有页面。这样做的目的可能是为了整合或汇总相关的文档，或者方便查阅或打印。

要实现合并操作，我们需要使用`PyPDF2.PdfMerger`类来创建一个合并器对象，并使用它来添加和合并多个PDF文件。下面是一个简单的例子：

```
# 创建一个PdfMerger对象
pdf_merger = PyPDF2.PdfMerger()

# 创建一个空列表，用于存放要合并的PDF文件名
files_to_merge = []

# 循环遍历要合并的5个小文件
for i in range(5):
    # 获取当前小文件名，格式为"original_页码.pdf"
    file = f"original_{<!-- -->i+1}.pdf"
    # 将当前小文件名添加到列表中
    files_to_merge.append(file)
    # 用PdfFileReader对象打开当前小文件
    pdf_reader = PyPDF2.PdfReader(file)
    # 用PdfFileMerger对象添加当前小文件，append方法可以将所有页面添加到合并器中
    pdf_merger.append(pdf_reader)

# 创建一个新的PDF文件名，格式为"original_merged.pdf"
new_file = "original_merged.pdf"

# 打开一个新的PDF文件，以二进制写入模式
with open(new_file, "wb") as f:
    # 将PdfFileMerger对象中的内容写入到新的PDF文件中
    pdf_merger.write(f)

# 打印出新创建的PDF文件名
print(new_file)

```

运行上面的代码，我们可以得到如下的输出：

```
original_merged.pdf   

```

这说明我们已经成功地将5个小的PDF文件合并成了一个大的PDF文件，包含了原始文件中的所有页面。我们可以打开新创建的PDF文件，查看它们的内容是否正确。

#### 总结

在这篇教程中，我们学习了如何使用`PyPDF2`库来快速分拆、删页、合并PDF文件。我们通过一些实际的例子来演示了这些操作，并介绍了一些常用的API和参数。`PyPDF2`库还有很多其他的功能和特性，例如旋转、裁剪、加密、解密、提取文本等，感兴趣的读者可以自行探索和尝试。希望这篇教程对你有所帮助，让你成为Python自动化办公高手！

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
