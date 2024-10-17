
--- 
title:  【ubuntu】 Linux(ubuntu)创建python的虚拟环境 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Linux(ubuntu)创建python的虚拟环境</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - <ul><li>-  
  </li></ul> 
  
  


在 Linux 上使用 Python 创建虚拟环境非常简单。常用的工具是 `venv`（Python 3.3 之后内置）和 `virtualenv`。以下是使用这两种方法创建虚拟环境的步骤：

### 方法1. 使用 `venv`:
<li> **安装 `venv`**: 如果你的 Python 版本大于等于 3.3，那么 `venv` 已经内置，不需要额外安装。如果由于某种原因你没有 `venv`，你可以使用 `apt` 安装它（针对 Debian/Ubuntu）： <pre><code class="prism language-bash">sudo apt-get install python3-venv
</code></pre> </li><li> **创建虚拟环境**: <pre><code class="prism language-bash">python3 -m venv myenv
</code></pre> 这将在当前目录下创建一个名为 `myenv` 的文件夹，其中包含了虚拟环境。 </li><li> **激活虚拟环境**: <pre><code class="prism language-bash">source myenv/bin/activate
</code></pre> 一旦激活，你的命令提示符将显示虚拟环境的名称，表示你正在使用该虚拟环境。 </li><li> **退出虚拟环境**: <pre><code class="prism language-bash">deactivate
</code></pre> </li>
### 方法 2. 使用 `virtualenv`:
<li> **安装 `virtualenv`**: <pre><code class="prism language-bash">pip install virtualenv
</code></pre> </li><li> **创建虚拟环境**: <pre><code class="prism language-bash">virtualenv myenv
</code></pre> 这也将在当前目录下创建一个名为 `myenv` 的文件夹。 </li><li> **激活虚拟环境**: <pre><code class="prism language-bash">source myenv/bin/activate
</code></pre> </li><li> **退出虚拟环境**: <pre><code class="prism language-bash">deactivate
</code></pre> </li>
选择哪种方法取决于你的需求。对于大多数用途，`venv` 足够好了，但 `virtualenv` 提供了一些额外的功能和选项。无论选择哪种方法，使用虚拟环境都是 Python 项目的最佳实践，因为它可以隔离项目的依赖性，使得项目管理更加简单和干净。
