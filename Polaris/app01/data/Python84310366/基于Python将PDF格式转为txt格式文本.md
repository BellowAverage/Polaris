
--- 
title:  基于Python将PDF格式转为txt格式文本 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/0f79348530f4e0a218602e15803982d1.png" alt="">

我们的工作内容是对上市公司的定期公告进行分析。

其中一环节是对大量的pdf格式的文件进行文本处理。

此次的示例，是随机选中的文本内容，共计344个pdf格式文件。

分析过程中对图片图表的需求并不大，将pdf批量转换成txt文本内容已经满足。如果考虑格式以及图片的读取，可以使用Python将pdf转csv、Word。

<img src="https://img-blog.csdnimg.cn/img_convert/bc699e39813505ec73113cc28f5b1a4b.png" alt="">

使用Python调用pdfplumber库，将将PDF格式转为txt格式文本。

首先安装pdfplumber库：

```
pip install pdfplumber

```

使用以下Python脚本来遍历指定文件夹中的所有PDF文件，将它们转换为TXT格式，并保存在一个新的文件夹：

```
import os
import pdfplumber

# 源文件夹路径
source_folder = "D:\\daku\\东鹏\\pdf"
# 目标文件夹路径，用于保存TXT文件
target_folder = "D:\\daku\\东鹏\\txt_exports"

# 如果目标文件夹不存在，则创建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith(".pdf"):
        # 构建完整的文件路径
        file_path = os.path.join(source_folder, filename)

        # 使用pdfplumber打开PDF文件
        with pdfplumber.open(file_path) as pdf:
            # 初始化一个空字符串来保存文本内容
            text = ""

            # 遍历PDF中的每一页
            for page in pdf.pages:
                # 提取页面的文本并添加到text变量中
                text += page.extract_text()
                text += "\n\n"  # 添加换行符以分隔不同页面的内容

        # 构建目标TXT文件的路径，文件名保持不变，只是扩展名改为.txt
        txt_file_path = os.path.join(target_folder, filename.replace(".pdf", ".txt"))

        # 将文本内容写入TXT文件
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

        print(f"已转换文件: {<!-- -->filename} -&gt; {<!-- -->txt_file_path}")

```

<img src="https://img-blog.csdnimg.cn/img_convert/fba120a6829b965a7dab78add105e902.jpeg" alt="">

344个pdf文件很迅速就可以转为txt文本

<img src="https://img-blog.csdnimg.cn/img_convert/ca78dfecd41951ebb1d5118b11d80d42.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/a251a4b0dcc65eaa89d59a11098cb90a.png" alt="">

工作导向不同，工作流程会存在差异，需要读取pdf文件中的图片，相关Python库可以使用将图像中的文字识别为文本进行导出。

```
 # 关于Python学习指南

```

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
