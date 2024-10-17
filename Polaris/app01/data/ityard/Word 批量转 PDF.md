
--- 
title:  Word 批量转 PDF 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200504111209452.png" alt=""> 现实中我们大多数人都做过将 Word 文件转成 PDF 文件的工作，如果需要转换的文件较少时，我们自己手动转没什么问题，但如果需要转换的文件比较多时，手动转起来也是一个不小的工作量，这时我们就需要找一个更加便利、高效的方式了。

我们使用 Python 就能实现将 Word 文件批量转成 PDF 文件，因此，当我们需要转换的文件比较多时，就可以考虑使用这种方式了。

转换功能的实现需要用到第三方库 `comtypes`，安装使用 `pip install comtypes` 即可，实现的基本思路是：我们将需要转换的 Word 文件放在一个目录下，通过 Python 实现对文件的遍历、转换工作。

转换功能的代码实现也比较简单，如下所示：

```
def get_file(input_path, output_path):
    # 获取所有文件名的列表
    filename_list = os.listdir(input_path)
    # 获取所有 Word 文件名列表
    wordname_list = [filename for filename in filename_list \
                     if filename.endswith((".doc", ".docx"))]
    for wordname in wordname_list:
        # 分离 Word 文件名称和后缀，转化为 PDF 名称
        pdfname = os.path.splitext(wordname)[0] + ".pdf"
        # 如果当前 Word 文件对应的 PDF 文件存在，则不转化
        if pdfname in filename_list:
            continue
        # 拼接路径和文件名
        wordpath = os.path.join(input_path, wordname)
        pdfpath = os.path.join(output_path, pdfname)
        # 生成器
        yield wordpath, pdfpath

def word2pdf(input_path, output_path):
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = 0
    for wordpath, pdfpath in get_file(input_path, output_path):
        newpdf = word.Documents.Open(wordpath)
        newpdf.SaveAs(pdfpath, FileFormat=17)
        newpdf.Close()


```

我们看一下效果，Word 文件内容如下所示： <img src="https://img-blog.csdnimg.cn/20200504111425448.png" alt=""> 看一下转换后的 PDF 文件： <img src="https://img-blog.csdnimg.cn/2020050411145410.png" alt=""> 我们可以看到，无论是文字样式还是图片，转换的效果都比较好。

源码可在公众号 **Python小二** 后台回复 **200504** 获取。
