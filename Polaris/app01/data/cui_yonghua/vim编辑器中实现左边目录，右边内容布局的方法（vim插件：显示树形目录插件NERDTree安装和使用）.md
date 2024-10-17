
--- 
title:  vim编辑器中实现左边目录，右边内容布局的方法（vim插件：显示树形目录插件NERDTree安装和使用） 
tags: []
categories: [] 

---
**NERDTree**：是Vim编辑器的文件系统资源管理器。使用此插件，用户可以直观地浏览复杂的目录层次结构，快速打开文件进行读取或编辑，并执行基本的文件系统操作。

它允许轻松浏览文件，并在不离开vim的情况下执行一些基本操作，如创建或移动文件。

可以与Git集成：用于显示哪个文件被修改了

github地址：

效果如下图： <img src="https://img-blog.csdnimg.cn/6ab9ebd161d44ab5b5ede1b1c8b30a27.png" alt="在这里插入图片描述">

### 一. 安装方法

#### 1、终端下载压缩文件

`wget http://www.vim.org/scripts/download_script.php?src_id=17123 -O nerdtree.zip`

#### 2、解压

`unzip nerdtree.zip`

#### 3、在家目录下创建.vim/{plugin,doc}

`mkdir -p ~/.vim/{plugin,doc}`

#### 4、复制两个文件

```
cp plugin/NERD_tree.vim ~/.vim/plugin/
cp doc/NERD_tree.txt ~/.vim/doc/

```

安装好后，打开vim，在
