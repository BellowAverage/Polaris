
--- 
title:  浏览器端可以直接运行Python了 
tags: []
categories: [] 

---
来源 | OSC开源社区（ID：oschina2013)

知名 Python 发行版 Anaconda 开发商近日宣布了可在浏览器端运行的 Python —— PyScript。

<img src="https://img-blog.csdnimg.cn/img_convert/4a9222fccd66f1e134a142fecec309b7.png" alt="4a9222fccd66f1e134a142fecec309b7.png">

根据官方的介绍，PyScript 是一个开发框架，为开发者提供了在标准 HTML 中嵌入编写 Python 代码的能力、使用 Python 调用 JavaScript 函数库，以及创建 Python Web 应用。PyScript 旨在提供“一等公民(first-class)”的编程语言，它具有一致的风格化规则、更具表现力且更易于学习。

**PyScript 示例代码**

```
&lt;py-script&gt;
"Hello World"
&lt;/py-script&gt;
```

```
&lt;py-script src="/my_own_file.py"&gt;&lt;/py-script&gt;
```

```
&lt;py-env&gt;
- bokeh
- numpy
- paths:
  - /utils.py
  &lt;/py-env&gt;
```

**PyScript 核心特性**
- Python in the browser：启用 drop-in content、外部文件托管（基于 Pyodide 项目），以及不依赖服务器端配置的应用程序托管- Python 生态：提供流行的 Python 和科学计算软件包（例如 numpy, pandas, scikit-learn 等）- Python with JavaScript：在 Python 和 JavaScript 对象和命名空间之间进行双向通信- 环境管理：开发者可定义要引入哪些包和文件，以便页面代码的运行- 可视化应用开发：开发者可使用现成的 UI 组件，如按钮、容器、文本框等- 灵活的框架：开发者可以利用它在 Python 中直接创建和分享新的可插拔和可扩展的组件
**PyScript 目标**
- 提供干净简单的 API- 支持标准 HTML- 扩展 HTML 以读取稳定且可靠的自定义组件- 提供可插拔、可扩展的组件系统
PyScript 基于 Pyodide 构建，Pyodide 由编译成 WebAssembly 的 CPython 3.8 解释器组成，允许在网页浏览器中运行 Python。Pyodide 可以安装来自 PyPi 的任何 Python 包。Pyodide 还包括一个外部函数接口，可以将 Python 包暴露给 JavaScript，并将浏览器 UI，包括 DOM，暴露给 Python。

<img src="https://img-blog.csdnimg.cn/img_convert/ccc51a476ce9d606d5af698777e86641.png" alt="ccc51a476ce9d606d5af698777e86641.png">

关于 PyScript 运行原理的更多信息查看：https://engineering.anaconda.com/2022/04/welcome-pyscript.html

目前 PyScript 处于 alpha 测试阶段，下载和安装地址：https://pyscript.net/

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/a935bb9da74cae9f0c4d84290e43d517.gif" alt="a935bb9da74cae9f0c4d84290e43d517.gif">
