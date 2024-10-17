
--- 
title:  vscode中配置latex 
tags: []
categories: [] 

---
**目录**











## 一、下载texlive

下载链接：

点击链接，进入texlive官网，如图所示，点击download from a nearby CTAN mirror

<img alt="" height="808" src="https://img-blog.csdnimg.cn/43a214f814054e2ba34f63056e832f30.png" width="1200">​

进入后，选择所需texlive版本，我选择的是2023版：

<img alt="" height="666" src="https://img-blog.csdnimg.cn/13005d227a7945bdb9ffbc36461e81af.png" width="1200">​ 这里下载可能比较慢，建议科学上网，或者参考该镜像网站：

##  二、安装texlive

下载完成后，打开texlive,点击install-tl-windows

<img alt="" height="1005" src="https://img-blog.csdnimg.cn/a347aa99d1ff4ca394be71daadd38ac9.png" width="1200">​

 运行该文件后，在弹出界面修改安装路径至D盘

<img alt="" height="709" src="https://img-blog.csdnimg.cn/301913a0741e4da6a77aed9310ad51aa.png" width="1200">​

 修改完毕，点击安装等待完成即可。

<img alt="" height="773" src="https://img-blog.csdnimg.cn/b0cac80fb0ec4875af90cb64ebaacaf3.png" width="1194">

完成标志：

<img alt="" height="773" src="https://img-blog.csdnimg.cn/7a1d3137a1194639bbb730a218751c1a.png" width="1194"> 打开cmd命令行，输入xelatex -v命令，输出如下则表示安装成功：

<img alt="" height="997" src="https://img-blog.csdnimg.cn/2b9fb32476ae48ab8cec82890c5102f9.png" width="1200">

## 三、vscode中配置latex

这里默认已安装vscode,若未安装，点击该链接，进行安装即可。

安装成功后，点击vscode侧边栏扩展选项，搜索latex workshop，点击安装。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/09aa5a20117e468d8fadb7f610af5e3b.png" width="1200">

 安装完毕后，进行latex配置。

点击左下角设置，后点击右上角，切换至settings.json

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/8afc88b941a14989b5807d246c83ac4f.png" width="1200"> 配置信息如下，粘贴至settings.json即可。

```
"latex-workshop.latex.tools": [	
    {
        "name": "pdflatex",
        "command": "pdflatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOCFILE%"
        ]
    },
    {
        "name": "xelatex",
        "command": "xelatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOCFILE%"
        ]
    },
    {
        "name": "bibtex",
        "command": "bibtex",
        "args": [
            "%DOCFILE%"
        ]
    }
],
"latex-workshop.latex.recipes": [
    {
        "name": "xelatex",
        "tools": [
            "xelatex"
        ],
    },
    {
        "name": "pdflatex",
        "tools": [
            "pdflatex"
        ]
    },
    {
        "name": "xe-&gt;bib-&gt;xe-&gt;xe",
        "tools": [
            "xelatex",
            "bibtex",
            "xelatex",
            "xelatex"
        ]
    },
    {
        "name": "pdf-&gt;bib-&gt;pdf-&gt;pdf",
        "tools": [
            "pdflatex",
            "bibtex",
            "pdflatex",
            "pdflatex"
        ]
    }
],
"latex-workshop.latex.clean.fileTypes": [
    "*.aux",
    "*.bbl",
    "*.blg",
    "*.idx",
    "*.ind",
    "*.lof",
    "*.lot",
    "*.out",
    "*.toc",
    "*.acn",
    "*.acr",
    "*.alg",
    "*.glg",
    "*.glo",
    "*.gls",
    "*.ist",
    "*.fls",
    "*.log",
    "*.fdb_latexmk"
],
//tex文件浏览器，可选项为"none" "browser" "tab" "external"
"latex-workshop.view.pdf.viewer": "tab",
//自动编译tex文件
"latex-workshop.latex.autoBuild.run": "onFileChange",
//显示内容菜单：（1）编译文件；（2）定位游标
"latex-workshop.showContextMenu": true,
//显示错误
"latex-workshop.message.error.show": false,
//显示警告
"latex-workshop.message.warning.show": false,
//从使用的包中自动补全命令和环境
"latex-workshop.intellisense.package.enabled": true,
//设置为never，为不清除辅助文件
"latex-workshop.latex.autoClean.run": "never",
//设置vscode编译tex文档时的默认编译链
"latex-workshop.latex.recipe.default": "lastUsed",
// 用于反向同步的内部查看器的键绑定。ctrl/cmd +点击(默认)或双击
"latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",

```

配置信息中的命令详解，可参考如下两篇文章：





## 四、测试

我从github上下载了一个latex模板：

解压缩后，用vscode打开，点击Build Latex project，若底部出现对勾，表示编译成功，否则，检查出错：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/d46d203923504c10aabae9b9f41751cf.png" width="1200">

 编译成功后，点击view latex PDF，如图所示：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/b1651996e88d44e79e7ba1156d5dbfa0.png" width="1200">

 至此，就大功告成啦~
