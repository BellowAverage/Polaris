
--- 
title:  MarkDown语法 
tags: []
categories: [] 

---
## MarkDown语法

在程序员们编写代码时，肯定少不了一个编辑器记录自己的学习、工作等。

有很多同学都喜欢将自己的知识分享，帮助大家学习，理解等，他们一般都会发布博客到相关的博客网站、论坛等。比如：博客园、

csdn、掘金，语雀等。

他们发博客那肯定少不了文档编辑，这里推荐一款好用的Markdown编辑器：typora。

好了，废话不多说，现在教大家在日常编程中常用到的Markdown语法吧。

Markdown官方教程：



### 1、Markdown是什么？

Markdown 是一种轻量级的标记语言，可用于在纯文本文档中添加格式化元素。Markdown 由 John Gruber 于 2004 年创建，如今已成为世界上最受欢迎的标记语言之一。

**特点**：
1. 专注于文字内容；1. 纯文本，易读易写，可以方便地纳入版本控制；1. 语法简单，没有什么学习成本，能轻松在码字的同时做出美观大方的排版。
### 2、为什么要使用Markdown呢？
- Markdown 无处不在。StackOverflow、CSDN、掘金、简书、GitBook、有道云笔记、V2EX、光谷社区等。主流的代码托管平台，如 GitHub、GitLab、BitBucket、Coding、Gitee 等等，都支持 Markdown 语法，很多开源项目的 README、开发文档、帮助文档、Wiki 等都用 Markdown 写作。- Markdown 是纯文本可移植的。几乎可以使用任何应用程序打开包含 Markdown 格式的文本文件。如果你不喜欢当前使用的 Markdown 应用程序了，则可以将 Markdown 文件导入另一个 Markdown 应用程序中。这与 Microsoft Word 等文字处理应用程序形成了鲜明的对比，Microsoft Word 将你的内容锁定在专有文件格式中。- Markdown 是独立于平台的。你可以在运行任何操作系统的任何设备上创建 Markdown 格式的文本。- Markdown 能适应未来的变化。即使你正在使用的应用程序将来会在某个时候不能使用了，你仍然可以使用文本编辑器读取 Markdown 格式的文本。
### 3、Markdown 格式如何转换为 HTML 呢？
1. 使用文本编辑器或 Markdown 专用的应用程序创建 Markdown 文件。该文件应带有 `.md` 或 `.markdown` 扩展名。1. 在 Markdown 应用程序中打开 Markdown 文件。1. 使用 Markdown 应用程序将 Markdown 文件转换为 HTML 文档。1. 在 web 浏览器中查看 HTML 文件，或使用 Markdown 应用程序将其转换为其他文件格式，例如 PDF。
这是我推荐的一些Markdown文档创作工具：
- 现代编辑器 VSCode / Atom- 传统编辑器 Vim / Emacs / Sublime Text / Notepad++- IDE 自带编辑器 IntelliJ IDEA / Android Studio / WebStorm- 专用编辑器 Ulysses / Mou / Typora / Markpad- 在线编辑器 各种支持 Markdown 的网站都提供了
### 4、基本语法

|元素|Markdown 语法
|------
||`# H1 ## H2 ### H3`
||`**bold text**`
||`*italicized text*`
||`&gt; blockquote`
||`1. First item` `2. Second item` `3. Third item`
||`- First item - Second item - Third item` (+，*，-都可以是)
||`code`
||`---` ( ***、___、— 三个都可以)
||`[title](https://www.example.com)`
||`![alt text](image.jpg)`
|链接图片|`[![沙漠](/img/shiprock.jpg "Shiprock")](https://markdown.com.cn)`
|代码块|`code `(三个 ```或者 ~ ~ ~) (想要什么语言高亮显示，就在后面接啥语言，如：~ ~ ~json)
|脚注|`[^1]`
|删除线|`~~删除线 ~~`
|换行|`&lt;br&gt;`
|转义字符|`\`
|标记文本|`==标记==`
|下角标|`H~2~O 是液体。`
|上角标|`2^10^=1024 运算结果是 1024`
|计划任务|`- [ ] 计划任务&lt;br/&gt;- [x] 完成任务`

### 5、复制和粘贴表情符号

在大多数情况下，您可以简单地从  等来源复制表情符号并将其粘贴到文档中。许多Markdown应用程序会自动以Markdown格式的文本显示表情符号。从Markdown应用程序导出的HTML和PDF文件应显示表情符号。

去露营了！⛺很快回来。

真好笑！😂

### 6、禁用自动URL链接

如果您不希望自动链接URL，则可以通过将URL表示为带反引号的代码来删除该链接。

```
`www.baidu.com`

```

呈现的输出如下所示：

`http://www.example.com`

<mark>今天的课上到这里，好啦，下课。你要永远相信光啊！！！😂</mark>
- <input type="checkbox" class="task-list-item-checkbox" disabled> 计划任务- <input type="checkbox" class="task-list-item-checkbox" checked disabled> 计划任务