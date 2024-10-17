
--- 
title:  初识 Markdown编辑器 
tags: []
categories: [] 

---


#### 这里写自定义目录标题
- - <ul><li>- - - - - - - - <ul><li>- - - 


## 欢迎使用Markdown编辑器

你好！ 这是你第一次使用 **Markdown编辑器** 所展示的欢迎页。如果你想学习如何使用Markdown编辑器, 可以仔细阅读这篇文章，了解一下Markdown的基本语法知识。

### 新的改变

我们对Markdown编辑器进行了一些功能拓展与语法支持，除了标准的Markdown编辑器功能，我们增加了如下几点新功能，帮助你用它写博客：
1. **全新的界面设计** ，将会带来全新的写作体验；1. 在创作中心设置你喜爱的代码高亮样式，Markdown **将代码片显示选择的高亮样式** 进行展示；1. 增加了 **图片拖拽** 功能，你可以将本地的图片直接拖拽到编辑区域直接展示；1. 全新的 **KaTeX数学公式** 语法；1. 增加了支持**甘特图的mermaid语法<sup class="footnote-ref"></sup>** 功能；1. 增加了 **多屏幕编辑** Markdown文章功能；1. 增加了 **焦点写作模式、预览模式、简洁写作模式、左右区域同步滚轮设置** 等功能，功能按钮位于编辑区域与预览区域中间；1. 增加了 **检查列表** 功能。
### 功能快捷键

撤销：<kbd>Ctrl/Command</kbd> + <kbd>Z</kbd> 重做：<kbd>Ctrl/Command</kbd> + <kbd>Y</kbd> 加粗：<kbd>Ctrl/Command</kbd> + <kbd>B</kbd> 斜体：<kbd>Ctrl/Command</kbd> + <kbd>I</kbd> 标题：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>H</kbd> 无序列表：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd> 有序列表：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> 检查列表：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd> 插入代码：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd> 插入链接：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>L</kbd> 插入图片：<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> 查找：<kbd>Ctrl/Command</kbd> + <kbd>F</kbd> 替换：<kbd>Ctrl/Command</kbd> + <kbd>G</kbd>

### 合理的创建标题，有助于目录的生成

直接输入1次<kbd>#</kbd>，并按下<kbd>space</kbd>后，将生成1级标题。 输入2次<kbd>#</kbd>，并按下<kbd>space</kbd>后，将生成2级标题。 以此类推，我们支持6级标题。有助于使用`TOC`语法后生成一个完美的目录。

### 如何改变文本的样式

**强调文本** **强调文本**

**加粗文本** **加粗文本**

<mark>标记文本</mark>

<s>删除文本</s>

>  
 引用文本 


H<sub>2</sub>O is是液体。

2<sup>10</sup> 运算结果是 1024.

### 插入链接与图片

链接: .

图片: <img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw" alt="Alt">

带尺寸的图片: <img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw" alt="Alt" width="30" height="30">

居中的图片: <img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw#pic_center" alt="Alt">

居中并且带尺寸的图片: <img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw#pic_center" alt="Alt" width="30" height="30">

当然，我们为了让用户更加便捷，我们增加了图片拖拽功能。

### 如何插入一段漂亮的代码片

去页面，选择一款你喜欢的代码片高亮样式，下面展示同样高亮的 `代码片`.

```
// An highlighted block
var foo = 'bar';

```

### 生成一个适合你的列表
<li>项目 
  <ul><li>项目 
    <ul>- 项目1. 项目11. 项目21. 项目3- <input type="checkbox" class="task-list-item-checkbox" disabled> 计划任务- <input type="checkbox" class="task-list-item-checkbox" checked disabled> 完成任务
### 创建一个表格

一个简单的表格是这么创建的：

|项目|Value
|------
|电脑|$1600
|手机|$12
|导管|$1

#### 设定内容居中、居左、居右

使用`:---------:`居中 使用`:----------`居左 使用`----------:`居右

<th align="center">第一列</th><th align="right">第二列</th><th align="left">第三列</th>
|------
<td align="center">第一列文本居中</td><td align="right">第二列文本居右</td><td align="left">第三列文本居左</td>

#### SmartyPants

SmartyPants将ASCII标点字符转换为“智能”印刷标点HTML实体。例如：

|TYPE|ASCII|<abbr title="超文本标记语言">HTML</abbr>
|------
|Single backticks|`'Isn't this fun?'`|‘Isn’t this fun?’
|Quotes|`"Isn't this fun?"`|“Isn’t this fun?”
|Dashes|`-- is en-dash, --- is em-dash`|– is en-dash, — is em-dash

### 创建一个自定义列表

### 如何创建一个注脚

一个具有注脚的文本。<sup class="footnote-ref"></sup>

### 注释也是必不可少的

Markdown将文本转换为 <abbr title="超文本标记语言">HTML</abbr>。

### KaTeX数学公式

您可以使用渲染LaTeX数学表达式 :

Gamma公式展示  
     
      
       
       
         Γ 
        
       
         ( 
        
       
         n 
        
       
         ) 
        
       
         = 
        
       
         ( 
        
       
         n 
        
       
         − 
        
       
         1 
        
       
         ) 
        
       
         ! 
        
        
       
         ∀ 
        
       
         n 
        
       
         ∈ 
        
       
         N 
        
       
      
        \Gamma(n) = (n-1)!\quad\forall n\in\mathbb N 
       
      
    Γ(n)=(n−1)!∀n∈N 是通过欧拉积分

 
      
       
        
        
          Γ 
         
        
          ( 
         
        
          z 
         
        
          ) 
         
        
          = 
         
         
         
           ∫ 
          
         
           0 
          
         
           ∞ 
          
         
         
         
           t 
          
          
          
            z 
           
          
            − 
           
          
            1 
           
          
         
         
         
           e 
          
          
          
            − 
           
          
            t 
           
          
         
        
          d 
         
        
          t 
          
        
          . 
         
        
       
         \Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,. 
        
       
     Γ(z)=∫0∞​tz−1e−tdt.

>  
 你可以找到更多关于的信息 **LaTeX** 数学表达式. 


### 新的甘特图功能，丰富你的文章
- 关于 **甘特图** 语法，参考 ,
### UML 图表

可以使用UML图表进行渲染。 . 例如下面产生的一个序列图：

这将产生一个流程图。:
- 关于 **Mermaid** 语法，参考 ,
### FLowchart流程图

我们依旧会支持flowchart的流程图：
- 关于 **Flowchart流程图** 语法，参考 .
### 导出与导入

#### 导出

如果你想尝试使用此编辑器, 你可以在此篇文章任意编辑。当你完成了一篇文章的写作, 在上方工具栏找到 **文章导出** ，生成一个.md文件或者.html文件进行本地保存。

#### 导入

如果你想加载一篇你写过的.md文件，在上方工具栏可以选择导入功能进行对应扩展名的文件导入， 继续你的创作。
1.   1. 注脚的解释  