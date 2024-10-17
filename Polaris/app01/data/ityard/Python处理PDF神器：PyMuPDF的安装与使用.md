
--- 
title:  Python处理PDF神器：PyMuPDF的安装与使用 
tags: []
categories: [] 

---
来源：网络

## 1、`PyMuPDF`简介

### 1. 介绍 

在介绍`PyMuPDF`之前，先来了解一下`MuPDF`，从命名形式中就可以看出，`PyMuPDF`是`MuPDF`的`Python`接口形式。

**MuPDF**

`MuPDF` 是一个轻量级的 `PDF、XPS`和电子书查看器。`MuPDF` 由软件库、命令行工具和各种平台的查看器组成。

`MuPDF` 中的渲染器专为高质量抗锯齿图形量身定制。它以精确到像素的几分之一内的度量和间距呈现文本，以在屏幕上再现打印页面的外观时获得最高保真度。

这个观察器很小，速度很快，但是很完整。它支持多种文档格式，如`PDF`、`XPS`、`OpenXPS`、`CBZ`、`EPUB`和`FictionBook 2`。您可以使用移动查看器对`PDF`文档进行注释和填写表单(这个功能很快也将应用于桌面查看器)。

命令行工具允许您注释、编辑文档，并将文档转换为其他格式，如`HTML、SVG、PDF`和`CBZ`。您还可以使用`Javascript`编写脚本来操作文档。

**PyMuPDF**`PyMuPDF`(当前版本1.18.17)是支持`MuPDF`(当前版本1.18.*)的Python绑定。

使用`PyMuPDF`，你可以访问扩展名为`“.pdf”、“.xps”、“.oxps”、“.cbz”、“.fb2”`或`“.epub”`。此外，大约10种流行的图像格式也可以像文档一样处理:`“.png”，“.jpg”，“.bmp”，“.tiff”`等。

### 2. 功能 

对于所有支持的文档类型可以：
- 解密文件- 访问元信息、链接和书签- 以栅格格式（`PNG`和其他格式）或矢量格式`SVG`呈现页面- 搜索文本- 提取文本和图像- 转换为其他格式：`PDF, (X)HTML, XML, JSON, text`对于`PDF`文档，存在大量的附加功能:它们可以**创建、合并或拆分**。页面可以通过多种方式**插入、删除、重新排列或修改**(包括注释和表单字段)。- 可以提取或插入图像和字体- 完全支持嵌入式文件- pdf文件可以重新格式化，以支持双面打印，色调分离，应用标志或水印- 完全支持密码保护:解密、加密、加密方法选择、权限级别和用户/所有者密码设置- 支持图像、文本和绘图的 PDF 可选内容概念- 可以访问和修改低级 PDF 结构<li>命令行模块`"python -m fitz…"`具有以下特性的多功能实用程序**新:布局保存文本提取!**脚本`fitzcliy .py`通过子命令`“gettext”`提供不同格式的文本提取。特别有趣的当然是布局保存，它生成的文本尽可能接近原始物理布局，周围有图像的区域，或者在表格和多列文本中复制文本。 
   <ul>- 加密/解密/优化- 创建子文档- 文档连接- 图像/字体提取- 完全支持嵌入式文件- 保存布局的文本提取(所有文档)
## 2、安装

`PyMuPDF`可以从源码安装，也可以从`wheels`安装。

对于`Windows, Linux`和`Mac OSX`平台，在`PyPI`的下载部分有`wheels`。这包括`Python 64位版本3.6到3.9`。Windows版本也有32位版本。从最近开始，Linux ARM架构也出现了一些问题——查找平台标签`manylinux2014_aarch64`。

除了标准库，它没有强制性的外部依赖项。只有在安装了某些包时，才会有一些不错的方法:
- `Pillow`：当使用`Pixmap.pil_save()`和 `Pixmap.pil_tobytes()`时需要- `fontTools`：当使用`Document.subset_fonts()`时需要- `pymupdf-fonts` 是一个不错的字体选择，可以用于文本输出方法
**使用`pip`安装命令**：

`pip install PyMuPDF`

**导入库：**

```
import fitz
```

### 关于命名`fitz`的说明 

这个库的标准`Python`导入语句是`import fitz`。这是有历史原因的:`MuPDF`的原始渲染库被称为`Libart`。

在Artifex软件获得`MuPDF`项目后，开发的重点转移到编写一种新的现代图形图书馆称为`“Fitz”`。`Fitz`最初是作为一个研发项目，以取代老化的`Ghostscript`图形库，但却成为了MuPDF的渲染引擎(引用自维基百科)。

## 3、使用方法

### 1. 导入库，查看版本 

```
import fitz
print(fitz.__doc__)
PyMuPDF 1.18.16: Python bindings for the MuPDF 1.18.0 library.
Version date: 2021-08-05 00:00:01.
Built for Python 3.8 on linux (64-bit).
```

### 2. 打开文档 

```
doc = fitz.open(filename)
```

这将创建`Document`对象`doc`。文件名必须是一个已经存在的文件的python字符串。也可以从**内存数据**打开文档，或创建新的空PDF。您还可以将文档用作上下文管理器。

### 3. Document的方法和属性 

示例：

```
&gt;&gt;&gt; doc.count_page
1
&gt;&gt;&gt; doc.metadata
{'format': 'PDF 1.7',
 'title': '',
 'author': '',
 'subject': '',
 'keywords': '',
 'creator': '',
 'producer': '福昕阅读器PDF打印机 版本 10.0.130.3456',
 'creationDate': "D:20210810173328+08'00'",
 'modDate': "D:20210810173328+08'00'",
 'trapped': '',
 'encryption': None}
```

### 4. 获取元数据 

`PyMuPDF`完全支持标准元数据。`Document.metadata`是一个具有以下键的**Python字典**。它适用于所有文档类型，但并非所有条目都始终包含数据。元数据字段为字符串，如果未另行指示，则为无。还要注意的是，并非所有数据都始终包含有意义的数据——即使它们不是一个都没有。

### 5. 获取目标大纲 

```
toc = doc.get_toc()
```

### 6. 页面(`Page`) 

页面处理是`MuPDF`功能的核心。• 您可以将页面呈现为光栅或矢量（`SVG`）图像，可以选择缩放、旋转、移动或剪切页面。• 您可以提取**多种格式**的页面文本和图像，并搜索文本字符串。• 对于`PDF`文档，可以使用更多的方法向页面添加文本或图像。

首先，必须创建一个页面`Page`。这是`Document`的一种方法：

```
page = doc.load_page(pno) # loads page number 'pno' of the document (0-based)
page = doc[pno] # the short form
```

这里可以使用任何整数`-inf&lt;pno&lt;page_count`。负数从末尾开始倒数，所以`doc[-1]`是最后一页，就像Python序列一样。

更高级的方法是将文档用作页面的迭代器：

```
for page in doc:
    # do something with 'page'
    
# ... or read backwards
for page in reversed(doc):
    # do something with 'page'
    
# ... or even use 'slicing'
for page in doc.pages(start, stop, step):
    # do something with 'page'
```

>  
  接下来，主要介绍`Page`的常用操作！ 
 

#### a. 检查页面的链接、批注或表单字段

使用某些查看器软件显示文档时，链接显示为==“热点区域”==。如果您在光标显示**手形符号**时单击，您通常会被带到该热点区域中编码的标记。以下是如何获取所有链接：

```
# get all links on a page
links = page.get_links()
```

`links`是一个`Python`**字典**列表。

还可以作为迭代器使用：

```
for link in page.links():
    # do something with 'link'
```

如果处理PDF文档页面，还可能存在注释（`Annot`）或表单字段（`Widget`），每个字段都有自己的迭代器：

```
for annot in page.annots():
    # do something with 'annot'
    
for field in page.widgets():
    # do something with 'field'
```

#### b. 呈现页面

此示例创建页面内容的光栅图像：

```
pix = page.get_pixmap()
```

`pix`是一个`Pixmap`对象，它（在本例中）包含页面的RGB图像，可用于多种用途。

方法`Page.get_pixmap()`提供了许多用于控制图像的变体：分辨率、颜色空间（例如，生成灰度图像或具有减色方案的图像）、透明度、旋转、镜像、移位、剪切等。

例如：创建RGBA图像（即，包含alpha通道），指定`pix=page.get_pixmap（alpha=True）`。\

`Pixmap`包含以下引用的许多方法和属性。其中包括整数**宽度**、**高度**（每个像素）和**跨距**（一个水平图像行的字节数）。属性示例表示表示图像数据的**矩形字节区域**（Python字节对象）。

还可以使用`page.get_svg_image()`创建页面的矢量图像。

#### c. 将页面图像保存到文件中

我们可以简单地将图像存储在`PNG`文件中：

```
pix.save("page-%i.png" % page.number)
```

#### d. 提取文本和图像

我们还可以以多种不同的形式和细节级别提取页面的所有文本、图像和其他信息：

```
text = page.get_text(opt)
```

对`opt`使用以下字符串之一以获取不同的格式：
- `"text"`：（默认）带换行符的纯文本。无格式、无文字位置详细信息、无图像- `"blocks"`：生成文本块（段落）的列表- `"words"`：生成单词列表（不包含空格的字符串）- `"html"`：创建页面的完整视觉版本，包括任何图像。这可以通过internet浏览器显示- `"dict"/"json"`：与`HTML`相同的信息级别，但作为Python字典或`resp.JSON`字符串。- `"rawdict"/"rawjson"`：`"dict"/"json"`的超级集合。它还提供诸如`XML`之类的字符详细信息。- `"xhtml"`：文本信息级别与文本版本相同，但包含图像。- `"xml"`：不包含图像，但包含每个文本字符的**完整位置和字体信息**。使用`XML`模块进行解释。
#### e. 搜索文本

您可以找到某个文本字符串在页面上的确切位置：

```
areas = page.search_for("mupdf")
```

这将提供一个**矩形列表**，每个矩形都包含一个字符串`“mupdf”`（不区分大小写）。您可以使用此信息来突出显示这些区域（仅限PDF）或创建文档的交叉引用。

### 7. PDF操作 

`PDF`是唯一可以使用`PyMuPDF`**修改**的文档类型。其他文件类型是只读的。

但是，您可以将任何文档（包括图像）**转换为PDF**，然后将所有`PyMuPDF`功能应用于转换结果,`Document.convert_to_pdf()`。

`Document.save()`始终将PDF以其当前（可能已修改）状态存储在磁盘上。

通常，您可以选择是保存到新文件，还是仅将修改附加到现有文件（“增量保存”），这通常要快得多。

下面介绍如何操作PDF文档。

#### a. 修改、创建、重新排列和删除页面

有几种方法可以操作所谓页面树（描述所有页面的结构）：
- `PDF:Document.delete_page()`和`Document.delete_pages()`删除页面- `Document.copy_page()`、`Document.fullcopy_page()`和`Document.move_page()`将页面**复制或移动**到同一文档中的其他位置。<li>`Document.select()`将PDF压缩到选定页面，参数是要保留的页码序列。这些整数都必须在`0&lt;=i&lt;page_ count`范围内。执行时，此列表中缺少的所有页面都将被删除。剩余的页面将按顺序出现，次数相同（！）正如您所指定的那样。因此，您可以轻松地使用创建新的PDF：保存的新文档将包含仍然有效的链接、注释和书签（i.a.w.指向所选页面或某些外部资源）。 
   <ul>- 第一页或最后10页- 仅奇数页或偶数页（用于双面打印）- 包含或不包含给定文本的页- 颠倒页面顺序
`Document.insert_page()`和`Document.new_page()`插入新页面。此外，页面本身可以通过一系列方法进行修改（例如页面旋转、注释和链接维护、文本和图像插入）。

#### b. 连接和拆分PDF文档

方法`Document.insert_pdf()`在不同的pdf文档之间复制页面。下面是一个简单的`joiner`示例（doc1和doc2在PDF中打开）：

```
# append complete doc2 to the end of doc1
doc1.insert_pdf(doc2)
```

下面是一个**拆分doc1**的片段。它将创建第一页和最后10页的新文档：

```
doc2 = fitz.open() # new empty PDF
doc2.insert_pdf(doc1, to_page = 9) # first 10 pages
doc2.insert_pdf(doc1, from_page = len(doc1) - 10) # last 10 pages
doc2.save("first-and-last-10.pdf")
```

#### c. 保存

`Document.save()`将始终以当前状态保存文档。

您可以通过指定选项`incremental=True`将更改写回原始PDF。这个过程（通常）非常快，因为更改会**附加**到原始文件，而不会完全重写它。

#### d. 关闭

在程序继续运行时，通常需要“关闭”文档以将底层文件的控制权交给操作系统。

这可以通过`Document.close()`方法实现。除了关闭基础文件外，还将释放与文档关联的缓冲区。

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/bc4875ddab406041021e34b4d4d6dc29.gif" alt="bc4875ddab406041021e34b4d4d6dc29.gif">
