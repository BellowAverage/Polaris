
--- 
title:  Python包管理：Conda和Pip常见命令一览 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/2d49ca3b43b946f0ba11230fd9a5b82a.png#pic_center" alt="在这里插入图片描述" width="600">

**摘要**：本篇博客介绍了 Python 中两大包管理工具 Conda 和 Pip 的基本使用方法。在 Conda 部分介绍了如何创建、管理和克隆环境，以及如何安装和管理跨语言包。在 Pip 部分，叙述了安装、升级和卸载 Python 包的命令，以及如何通过 `requirements.txt` 管理项目依赖，包括离线安装。为 Python 开发者提供一个简明实用的包和环境管理指南，帮助提升项目开发的效率和稳定性。



#### 文章目录
- - <ul><li>- - - - - - - - - - - - 


## Conda 常见命令详解

Conda 是一个强大的工具，用于包管理和环境管理。无论你是在进行数据科学、机器学习项目，还是日常的 Python 开发，掌握 Conda 的常用命令都是非常有帮助的。以下是 Conda 的一些最常见命令及其使用说明。

<img src="https://img-blog.csdnimg.cn/direct/301afadc31204a69960924e8f96f52db.png#pic_center" alt="在这里插入图片描述" width="400">

### 1. 环境管理

环境管理是 Conda 的一项核心功能，它允许你为不同的项目创建隔离的环境，以避免依赖冲突。
<li> **创建新环境**： <pre><code class="prism language-sh">conda create --name myenv python=3.8
</code></pre> 这将创建一个名为 `myenv` 的新环境。你可以通过指定 `python=3.x` 来为环境设置特定的 Python 版本。 </li><li> **激活环境**： <pre><code class="prism language-sh">conda activate myenv
</code></pre> 在开始工作前，你需要激活相应的环境。`myenv` 就是你想要激活的环境名称。 </li><li> **退出环境**： <pre><code class="prism language-sh">conda deactivate
</code></pre> 当你完成工作并希望返回到基本环境时，使用这个命令。 </li>
### 2. 包管理

包管理是 Conda 另一个重要功能，它让安装、更新和删除包变得简单快捷。
<li> **安装包**： <pre><code>conda install numpy
</code></pre> 这将在当前活动环境中安装最新版本的 NumPy 包。如果你想在特定环境中安装包，可以使用 `--name` 标志指定环境。 </li><li> **更新包**： <pre><code class="prism language-sh">conda update numpy
</code></pre> 这将更新当前环境中的 NumPy 包到最新版本。 </li><li> **移除包**： <pre><code class="prism language-sh">conda remove numpy
</code></pre> 这将从当前环境中移除 NumPy 包。 </li>
### 3. 环境列表和删除
<li> **列出所有环境**： <pre><code class="prism language-sh">conda env list
</code></pre> 或者使用 `conda info --envs`，这将显示所有可用的 Conda 环境及其路径。 </li><li> **删除环境**： <pre><code class="prism language-sh">conda remove -n myenv --all
</code></pre> 这个命令中 `-n myenv` 指定了环境的名称（在这个例子中是 `myenv`），而 `--all` 参数确保环境中的所有包和自身都会被删除。这样，Conda 就会移除整个环境，包括所有已安装的包和环境自身，确保没有任何剩余的文件或配置留下。 </li>
### 4. 环境导出和克隆
<li> **导出环境**： <pre><code class="prism language-sh">conda env export &gt; environment.yml
</code></pre> 这将当前环境的所有包及其版本导出到一个 `environment.yml` 文件中，非常适合共享或迁移环境。 </li><li> **克隆环境**： 使用以下命令克隆环境： <pre><code class="prism language-sh">conda create --clone myenv --name myclone
</code></pre> 这里，`myenv` 是你想要克隆的现有环境的名称，而 `myclone` 是新环境的名称。 当你执行克隆命令时，Conda 会复制 `myenv` 环境中的所有包和配置到新的 `myclone` 环境中。这意味着新环境将具有与原始环境相同的 Python 版本、库和依赖包，包括任何你可能已安装的非默认包。 </li>
## Pip常见命令

Pip 是 Python 的官方包管理工具，负责从 Python 包索引 (PyPI) 安装和管理包。自 Python 2.7.9 和 Python 3.4 以来，它成为了标准的包安装方法。Pip 使得查找、安装、升级甚至卸载 Python 包变得非常简单。

<img src="https://img-blog.csdnimg.cn/direct/63244aca64274c5a8ab7de31a061fc4d.png#pic_center" alt="在这里插入图片描述" width="400">

### 1. 安装包

要安装一个 Python 包，你可以使用 `install` 命令后跟包的名称：

```
pip install package_name

```

默认情况下，这个命令会从 Python 官方包索引 (PyPI) 下载并安装指定的 `package_name`。PyPI 的默认 URL 是：

```
https://pypi.org/simple

```

在某些情况下，由于网络问题或者其他原因，你可能需要使用镜像源。中国地区常见的镜像源包括：
<li>**清华大学镜像源**：<pre><code class="prism language-sh">https://pypi.tuna.tsinghua.edu.cn/simple
</code></pre> </li><li>**阿里云镜像源**：<pre><code class="prism language-sh">https://mirrors.aliyun.com/pypi/simple/
</code></pre> </li><li>**豆瓣镜像源**：<pre><code class="prism language-sh">http://pypi.douban.com/simple/
</code></pre> </li><li>**中国科技大学镜像源**：<pre><code class="prism language-sh">https://pypi.mirrors.ustc.edu.cn/simple/
</code></pre> </li>
要使用这些镜像源之一安装包，可以在安装命令中使用 `-i` 选项：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name

```

例如，使用清华大学镜像源安装 `requests` 包，你可以这样做：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

```

这个命令会从清华大学的 PyPI 镜像下载并安装 `requests` 包，这通常能提供更快的下载速度。

通过指定 `-i` 选项和选择合适的镜像源，你可以根据网络状况和地理位置优化包的安装过程。

### 2. 升级包

当包的新版本发布时，你可以使用 `install` 命令和 `--upgrade`（或 `-U`）标志来升级到最新版本：

```
pip install --upgrade package_name

```

使用 `--upgrade` 或 `-U` 选项，Pip 会检查 `package_name` 的最新版本，如果本地安装的版本不是最新的，则进行升级。这保证了你使用的包总是最新的。

例如，升级 `requests` 包：

```
pip install --upgrade requests

```

### 3. 卸载包

如果你不再需要某个包，可以使用 `uninstall` 命令将其卸载：

```
pip uninstall package_name

```

此命令用于卸载已安装的包。执行后，Pip 通常会要求你确认卸载操作。如果你想跳过确认，可以添加 `-y` 选项。

### 4. 列出已安装的包

Pip 允许你快速查看已安装的包及其版本，使用 `list` 命令：

```
pip list

```

`list` 命令显示了所有已安装包及其版本。你可以添加 `--outdated` 选项来查看有更新版本的包，或使用 `--uptodate` 仅查看已是最新版本的包。

### 5. 查找包

尽管查找包通常是通过 PyPI 网站完成的，但你也可以使用 `search` 命令在命令行中搜索：

```
pip search package_name

```

此命令用于在 PyPI 上搜索包。它会返回与搜索词相关的所有包的简短描述。需要注意的是，此命令的功能可能受到 PyPI API 更改的影响，建议直接在 PyPI 网站上进行搜索。

### 6. 查看包信息

要获取有关已安装包的更多信息，可以使用 `show` 命令：

```
pip show package_name

```

`show` 命令显示指定包的详细信息，包括版本、安装位置、依赖项、主页等。

### 7. 生成依赖文件

在项目中，经常需要记录所有依赖项的准确版本，以保证环境的一致性。`freeze` 命令可以帮助你生成一个包含所有已安装包及其版本的列表：

```
pip freeze &gt; requirements.txt

```

`freeze` 命令生成一个包含所有已安装包及其精确版本的列表，并将其输出到 `requirements.txt` 文件中。这对于共享环境或在不同环境中重建相同环境非常有用。

### 8. 从依赖文件安装包

`requirements.txt` 文件是 Python 项目中的标准方式，用于记录项目的所有依赖。要安装这些依赖，可以使用以下命令：

```
pip install -r requirements.txt

```

此命令根据 `requirements.txt` 文件中列出的依赖关系安装包。这在确保项目在不同开发环境中的一致性方面非常重要。

### 9. 从离线依赖包文件夹安装

如果你有一个包含所有依赖包的本地文件夹（例如，你预先下载了所有必要的包以便离线安装），可以通过指定该文件夹路径来安装这些包：

```
pip install --no-index --find-links=path/to/folder -r requirements.txt

```

这里，`path/to/folder` 是存储下载包的本地文件夹路径。`--no-index` 告诉 Pip 不从 PyPI 检索包，而 `--find-links` 指定包的本地路径。

例如，如果你的依赖包存储在 `/path/to/packages` 文件夹中，命令将是：

```
pip install --no-index --find-links=/path/to/packages -r requirements.txt

```

这种方法特别适合于没有互联网访问或希望从特定源安装包的情况，确保了即使在离线环境下也能保持项目依赖的一致性和可复现性。
