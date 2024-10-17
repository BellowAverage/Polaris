
--- 
title:  《Docker 简易速速上手小册》第1章 Docker 基础入门（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/fdbcf5755a33456487eb75db3fa558f4.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 1.1 Docker 简介与历史

欢迎来到 Docker 的世界！在这一节中，我们将从 Docker 的基础知识和历史开始，然后通过一些精彩的案例来深入探讨它的实用性和强大功能。让我们一起开启这趟知识之旅吧！

### 1.1.1 Docker 基础知识

要深入了解 Docker，我们首先需要掌握一些关键概念。Docker 是一个开源的容器化技术，它允许开发者和系统管理员在所谓的容器中打包、分发和运行应用。这些容器是轻量级的、可移植的、自给自足的包，它们包含了运行应用所需的一切：代码、运行时环境、库、环境变量和配置文件。

**容器 vs. 虚拟机**

容器经常被与虚拟机（VM）相比较。虽然它们都提供资源隔离和分配的功能，但容器更为轻量级。与虚拟机不同的是，容器共享主机系统的内核，不需要运行整个操作系统。这就意味着容器启动得更快，占用的资源更少。

**镜像**

Docker 镜像是容器的蓝本。它是一个轻量级的、不可变的、可执行的软件包，包含运行应用所需的所有内容——代码、运行时环境、库、环境变量和配置文件。通过 Dockerfile，一个简单的文本文件，可以定义如何构建镜像。

**Docker Hub 和仓库**

Docker Hub 是 Docker 的公共仓库，用户可以在此上传和下载镜像。除了 Docker Hub，用户还可以在私有仓库存储镜像。仓库可以被视为镜像的集合，它允许用户版本控制和分享。

**Dockerfile**

Dockerfile 是一个文本文件，包含了一系列的指令和参数，用于定义如何从基础镜像构建新的镜像。通过 Dockerfile，可以自动化创建镜像的过程，确保环境的一致性和可重复性。

**Docker Compose**

Docker Compose 是一个用于定义和运行多容器 Docker 应用的工具。通过一个 YAML 文件，可以配置应用服务的所有参数。这使得管理容器化应用更加容易，特别是在处理多个相互依赖的容器时。

**网络和数据存储**

Docker 容器可以通过网络进行通信，并可以使用卷（volume）来持久化和共享数据。Docker 网络功能允许容器之间的相互连接，以及容器与外部世界的通信。通过卷，可以将数据持久化存储在容器外部，确保数据的安全和持续性。

了解这些基本概念后，你就已经准备好进一步探索 Docker 的强大功能和实际应用了。在接下来的章节中，我们将通过实际案例，让你更深入地了解如何使用 Docker 来改善你的开发和运维工作。

### 1.1.2 重点案例：Python Web 应用的 Docker 化

在这个案例中，我们将创建一个简单的 Python Web 应用，并通过 Docker 容器化技术部署它。这个案例将向你展示如何将现代 Web 开发流程与 Docker 相结合，从而提高开发效率和应用的可移植性。

**步骤 1**: 创建 Flask 应用

我们的第一步是创建一个基本的 Python Flask 应用。Flask 是一个轻量级的 Web 应用框架，非常适合快速开发和原型设计。以下是我们的简单 Flask 应用代码：

```
# 文件名：app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

```

在这个应用中，我们定义了一个根路由 `/`，当访问这个路由时，它返回“Hello, Docker!”。

**步骤 2**: 编写 Dockerfile

接下来，我们需要创建一个 Dockerfile 来定义如何在 Docker 容器中运行我们的 Flask 应用。Dockerfile 是构建 Docker 镜像的蓝图，包含了必要的指令和步骤。

```
# Dockerfile

# 使用官方 Python 运行时作为父镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 安装 Flask
RUN pip install flask

# 使得端口 5000 可供此容器外的环境使用
EXPOSE 5000

# 定义环境变量
ENV NAME World

# 运行 app.py 时启动应用
CMD ["python", "./app.py"]

```

这个 Dockerfile 从一个 Python 3.8 镜像开始，将我们的应用代码复制到镜像中，并安装 Flask。然后，它将容器的 5000 端口暴露出来，并指定了启动应用时运行的命令。

**步骤 3**: 构建和运行 Docker 容器

最后一步是构建我们的 Docker 镜像，并在容器中运行它。

首先，我们使用以下命令构建镜像：

```
docker build -t flask-app .

```

这个命令会读取 Dockerfile，并构建一个名为 `flask-app` 的镜像。

接下来，运行这个镜像：

```
docker run -p 5000:5000 flask-app

```

这个命令会启动一个新的容器实例，将本地的端口 5000 映射到容器的端口 5000，并在该容器中运行我们的 Flask 应用。

现在，打开浏览器并访问 `http://localhost:5000`，你应该能看到显示“Hello, Docker!”的页面。

通过这个简单的案例，你可以看到 Docker 如何帮助我们轻松地部署 Web 应用，并保证了在不同环境中的一致性和可移植性。这只是 Docker 众多强大功能中的一个简单示例。随着你对 Docker 的进一步学习，你将能够发现并利用更多高级功能来优化你的开发和部署流程。

### 1.1.3 拓展案例 1：使用 Docker 进行 Python 数据分析

在这个案例中，我们将通过 Docker 创建一个 Python 数据分析环境。这个环境将包括 Jupyter Notebook，这是一个非常受欢迎的工具，允许你在浏览器中编写和执行 Python 代码，并且能够可视化数据和分析结果。让我们一步一步来完成这个案例。

**步骤 1**: 创建 Dockerfile

首先，我们需要创建一个 Dockerfile 来定义我们的数据分析环境。这个环境将基于 Python 3，并安装 Jupyter Notebook 以及一些常用的数据分析库，如 Pandas 和 NumPy。

```
# Dockerfile

# 从 Python 官方镜像开始构建
FROM python:3.8-slim

# 安装 Jupyter Notebook
RUN pip install jupyter

# 安装常用的数据分析库
RUN pip install numpy pandas matplotlib seaborn

# 设置工作目录
WORKDIR /data

# 使得端口 8888 可供此容器外的环境使用
EXPOSE 8888

# 当容器启动时，启动 Jupyter Notebook
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]

```

这个 Dockerfile 从 Python 3.8 镜像开始，安装了 Jupyter Notebook 和几个常用的数据分析库。它还将容器的 8888 端口暴露出来，以便访问 Jupyter Notebook。

**步骤 2**: 构建 Docker 镜像

使用以下命令构建我们的 Docker 镜像：

```
docker build -t python-data-analysis .

```

这个命令会根据 Dockerfile 构建一个名为 `python-data-analysis` 的镜像。

**步骤 3**: 运行 Docker 容器

接下来，运行这个镜像：

```
docker run -p 8888:8888 python-data-analysis

```

这个命令启动了一个容器实例，将本地的 8888 端口映射到了容器的 8888 端口，并在该容器中启动了 Jupyter Notebook。

在容器启动后，你将看到一个 URL，其中包含一个 token。将这个 URL 复制到浏览器中，就可以开始使用 Jupyter Notebook 了。

**数据分析示例**

在 Jupyter Notebook 中，你可以开始编写 Python 代码进行数据分析。例如，你可以使用以下代码来创建一个简单的数据集，并用 Matplotlib 生成一个图表：

```
# 导入所需库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 创建一个简单的数据集
data = pd.DataFrame({<!-- -->
    'x': range(10),
    'y': np.random.randn(10)
})

# 绘制图表
plt.plot(data['x'], data['y'])
plt.show()

```

通过这个案例，你可以看到 Docker 如何帮助我们快速搭建一个完整的数据分析环境，无论你在哪里工作，都能保证环境的一致性和可移植性。使用 Docker，你可以专注于数据分析本身，而不是环境配置的问题。

### 1.1.4 拓展案例 2：Docker 中的 Python 机器学习环境

在这个案例中，我们将展示如何使用 Docker 搭建一个 Python 机器学习环境。这个环境将包括 Python 的机器学习库，如 scikit-learn 和 TensorFlow，使得机器学习项目的开发和部署更加容易和一致。

**步骤 1**: 创建 Dockerfile

首先，我们需要创建一个 Dockerfile，以定义我们的机器学习环境。这个环境将基于 Python 3，并安装 scikit-learn 和 TensorFlow 这两个流行的机器学习库。

```
# Dockerfile

# 从 Python 官方镜像开始构建
FROM python:3.8-slim

# 安装 scikit-learn 和 TensorFlow
RUN pip install scikit-learn tensorflow

# 设置工作目录
WORKDIR /ml

# 运行时，保持容器运行
CMD ["tail", "-f", "/dev/null"]

```

这个 Dockerfile 从 Python 3.8 镜像开始，安装了 scikit-learn 和 TensorFlow。它还设置了工作目录，并使用 `tail` 命令来保持容器运行。

**步骤 2**: 构建 Docker 镜像

使用以下命令来构建我们的 Docker 镜像：

```
docker build -t python-ml .

```

这个命令会根据 Dockerfile 构建一个名为 `python-ml` 的镜像。

**步骤 3**: 运行 Docker 容器

接下来，运行这个镜像：

```
docker run -it --name ml-container python-ml

```

这个命令启动了一个名为 `ml-container` 的容器实例，并进入交互式模式。

**机器学习示例**

在这个容器中，你可以开始使用 Python 进行机器学习实验。例如，你可以使用以下代码来训练一个简单的线性模型：

```
# 导入所需库
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
import pandas as pd

# 加载数据集
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target, columns=["MEDV"])

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建并训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 测试模型
score = model.score(X_test, y_test)
print(f"Model Accuracy: {<!-- -->score}")

```

通过这个案例，你可以看到 Docker 如何帮助我们快速搭建一个包含必要机器学习库的环境，使得在不同环境中的机器学习开发和部署变得更加容易和一致。使用 Docker，你可以专注于机器学习模型的构建和训练，而无需担心环境配置问题。

通过以上案例，你不仅能够理解 Docker 的基本概念和历史背景，还能深入学习如何在实际工作中应用 Docker 来提升 Python 开发和数据科学项目的效率和一致性。这些案例旨在提供实用性强且贴近实际生产的应用场景，帮助你更好地理解和运用 Docker 技术。

## 1.2 安装与配置 Docker

在这一节中，我们将详细讲解 Docker 的安装和配置过程，重点关注在不同操作系统上的安装步骤。随后，我们将通过一些实用的 Python 应用案例，展示如何在 Docker 环境中运行和管理 Python 应用。

### 1.2.1 重点基础知识

在深入探讨如何使用 Docker 运行 Python 应用之前，了解 Docker 的基本安装和配置步骤是非常重要的。以下是一些关键的基础知识点：
<li> **下载 Docker**: 
  1. **Windows** 和 **MacOS**: 对于 Windows 和 MacOS 用户，推荐使用 Docker Desktop。它提供一个直观的用户界面，并包含了 Docker Engine、Docker CLI 客户端、Docker Compose 等工具。您可以从 Docker 的官方网站下载对应的安装程序。1. **Linux**: Linux 用户需要通过命令行安装 Docker。不同的 Linux 发行版（如 Ubuntu、Fedora、Debian）有着不同的安装命令。例如，在 Ubuntu 上，你可以使用 `sudo apt-get install docker.io` 来安装 Docker。 </li><li> **安装 Docker**: 
  1. 在 Windows 或 MacOS 上，双击下载的安装包并遵循安装向导的指示完成安装。1. 在 Linux 上，通常需要使用特定的包管理器进行安装，并可能需要配置 Docker 以便非 root 用户也能运行 Docker 命令。 </li><li> **启动 Docker**: 
  1. 在 Windows 或 MacOS 上，安装完成后，Docker 将作为一个应用程序出现。你只需点击它来启动 Docker。1. 在 Linux 上，你可能需要使用命令 `sudo systemctl start docker` 来启动 Docker 服务。 </li><li> **验证 Docker 安装**: 
  1. 无论在哪个平台上，都可以通过在终端或命令行中运行 `docker --version` 来检查 Docker 是否安装成功。这将显示 Docker 的版本信息。 </li><li> **运行 Docker 的 Hello World**: 
  1. 为了验证 Docker 是否被正确安装和配置，可以运行 Docker 的 Hello World 示例。在命令行中输入 `docker run hello-world`。这将从 Docker Hub 下载一个测试镜像，并在一个容器中运行它。如果一切顺利，你将在终端中看到一条欢迎消息。 </li><li> **Docker 用户组**: 
  1. 在 Linux 上，建议将用户添加到 Docker 用户组中。这允许非 root 用户执行 Docker 命令。可以通过 `sudo usermod -aG docker $USER` 命令来实现。 </li><li> **配置 Docker**: 
  1. Docker 提供了多种配置选项，包括网络设置、存储选项等。这些配置可以通过修改 `/etc/docker/daemon.json` 文件（在 Linux 上）或通过 Docker Desktop 应用程序（在 Windows 和 MacOS 上）进行。 </li>- 在 Windows 或 MacOS 上，双击下载的安装包并遵循安装向导的指示完成安装。- 在 Linux 上，通常需要使用特定的包管理器进行安装，并可能需要配置 Docker 以便非 root 用户也能运行 Docker 命令。- 无论在哪个平台上，都可以通过在终端或命令行中运行 `docker --version` 来检查 Docker 是否安装成功。这将显示 Docker 的版本信息。- 在 Linux 上，建议将用户添加到 Docker 用户组中。这允许非 root 用户执行 Docker 命令。可以通过 `sudo usermod -aG docker $USER` 命令来实现。
通过掌握这些基础知识，您将为使用 Docker 创建和运行容器应用打下坚实的基础。接下来的案例将指导您如何在这个设置中运行 Python 应用，无论是简单的脚本还是复杂的 Web 应用。

### 1.2.2 重点案例：使用 Docker 运行 Python 脚本

在这个案例中，我们将演示如何使用 Docker 来运行一个简单的 Python 脚本。这将帮助你理解如何在 Docker 容器中运行 Python 程序，从而为更复杂的项目打下基础。

**步骤 1**: 创建 Python 脚本

首先，我们需要创建一个 Python 脚本。让我们编写一个简单的脚本，它会输出一条欢迎信息。在你的工作目录中，创建一个名为 `hello.py` 的文件，并添加以下内容：

```
# hello.py
print("Hello from Docker!")

```

这个脚本非常简单，只是打印出一条消息。

**步骤 2**: 编写 Dockerfile

接下来，我们需要创建一个 Dockerfile 来定义如何在 Docker 容器中运行这个脚本。Dockerfile 是一个文本文件，包含了一系列的指令，用于告诉 Docker 如何构建镜像。

在你的工作目录中，创建一个名为 `Dockerfile` 的文件（无文件扩展名），并添加以下内容：

```
# 使用官方 Python 运行时作为父镜像
FROM python:3.8

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录中的文件复制到容器的 /app 目录
COPY . /app

# 运行 hello.py 脚本时，调用 Python 解释器
CMD ["python", "./hello.py"]

```

这个 Dockerfile 从一个 Python 3.8 镜像开始，将工作目录设置为 `/app`，将当前目录下的文件复制到这个位置，然后定义了运行容器时要执行的命令。

**步骤 3**: 构建 Docker 镜像

现在，我们可以使用以下命令来构建我们的 Docker 镜像：

```
docker build -t hello-python .

```

这条命令告诉 Docker 构建一个新的镜像，并将这个镜像标记（tag）为 `hello-python`。`.` 指的是当前目录，Docker 会在这里查找 Dockerfile。

**步骤 4**: 运行 Docker 容器

一旦镜像构建完成，我们就可以运行一个基于该镜像的容器了：

```
docker run hello-python

```

当这个命令执行时，它会启动一个新的容器实例，容器会运行 `hello.py` 脚本，并显示输出。你应该会在命令行中看到 “Hello from Docker!” 的消息。

通过这个简单的案例，你已经学会了如何将 Python 脚本容器化，并在 Docker 中运行它。这是理解 Docker 容器如何工作的基础，并且是向更复杂的应用迈进的第一步。

### 1.2.3 拓展案例 1：使用 Docker 部署 Flask Web 应用

在这个案例中，我们将演示如何使用 Docker 来部署一个简单的 Flask Web 应用。Flask 是一个轻量级的 Python Web 框架，非常适合快速开发。通过 Docker 化 Flask 应用，你可以确保你的 Web 应用在任何环境中都能以相同的方式运行。

**步骤 1**: 创建 Flask 应用

首先，我们创建一个基本的 Flask 应用。在你的工作目录中，创建两个文件：`app.py` 和 `requirements.txt`。
<li> `app.py` - Flask 应用的主要文件： <pre><code class="prism language-python"># app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
</code></pre> </li><li> `requirements.txt` - 列出所需的 Python 包： <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

接下来，我们需要创建一个 Dockerfile 来定义如何在 Docker 容器中运行我们的 Flask 应用。

在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 使用官方 Python 镜像
FROM python:3.8

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录中的文件复制到容器的 /app 目录
COPY . /app

# 安装 requirements.txt 中的所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 让世界可以访问你的应用
EXPOSE 5000

# 定义环境变量
ENV FLASK_APP=app.py

# 运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]

```

这个 Dockerfile 从 Python 3.8 镜像开始，设置工作目录，复制文件，并安装依赖。它还将容器的 5000 端口暴露出来，并定义了运行 Flask 应用的命令。

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建我们的 Flask 应用的 Docker 镜像：

```
docker build -t flask-app .

```

这条命令会创建一个名为 `flask-app` 的镜像。

**步骤 4**: 运行 Docker 容器

构建完镜像后，使用以下命令运行容器：

```
docker run -p 5000:5000 flask-app

```

这个命令启动了一个容器实例，将你的机器的 5000 端口映射到容器的 5000 端口。

现在，你的 Flask 应用应该在 Docker 容器中运行了。在浏览器中访问 `http://localhost:5000`，你应该能看到 “Hello, Docker!” 的消息。

通过这个案例，你已经成功地使用 Docker 部署了一个 Flask Web 应用。这个案例演示了 Docker 如何帮助你保证应用在不同环境中的一致性，同时也展示了 Docker 在现代 Web 开发中的应用。

### 1.2.4 拓展案例 2：在 Docker 中运行 Python 数据分析环境

在这个案例中，我们将通过 Docker 创建一个 Python 数据分析环境。这个环境将包括 Jupyter Notebook 和常用的数据分析库，如 Pandas、NumPy 和 Matplotlib。这种方法非常适合数据科学家和分析师，因为它提供了一个一致且易于共享的工作环境。

**步骤 1**: 创建 Dockerfile

首先，我们需要创建一个 Dockerfile 来定义我们的数据分析环境。在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 从官方 Python 镜像开始构建
FROM python:3.8-slim

# 安装 Jupyter 和常见的数据分析库
RUN pip install jupyter pandas numpy matplotlib seaborn

# 设置工作目录，用于在容器内部运行 Jupyter Notebook
WORKDIR /data

# 暴露 Jupyter Notebook 运行的端口
EXPOSE 8888

# 启动 Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

```

这个 Dockerfile 从 Python 3.8 镜像开始，安装了 Jupyter Notebook 和几个常用的数据分析库。它还设置了工作目录并暴露了运行 Jupyter Notebook 所需的端口。

**步骤 2**: 构建 Docker 镜像

接下来，我们可以使用以下命令来构建我们的 Docker 镜像：

```
docker build -t python-data-analysis .

```

这个命令会根据 Dockerfile 构建一个名为 `python-data-analysis` 的镜像。

**步骤 3**: 运行 Docker 容器

现在，我们可以运行这个镜像了：

```
docker run -p 8888:8888 python-data-analysis

```

这个命令会启动一个 Docker 容器，并将本地机器的 8888 端口映射到容器的 8888 端口。当容器启动后，它将运行 Jupyter Notebook。

在容器运行后，你会在命令行中看到一个 URL，其中包含了访问 Jupyter Notebook 的 token。复制并粘贴这个 URL 到浏览器中，你就可以开始在 Jupyter Notebook 中进行数据分析了。

**数据分析示例**

在 Jupyter Notebook 中，你可以执行各种数据分析任务。例如，你可以使用 Pandas 来加载和分析数据，使用 Matplotlib 和 Seaborn 来进行数据可视化。以下是一个简单的示例：

```
# 导入所需的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 创建一个简单的数据集
data = pd.DataFrame({<!-- -->
    'x': range(1, 11),
    'y': np.random.rand(10),
})

# 使用 Seaborn 画一个散点图
sns.scatterplot(x='x', y='y', data=data)
plt.show()

```

通过这个案例，你可以看到如何快速地在 Docker 中搭建一个完整的数据分析环境，这个环境可以在不同机器上轻松复制和共享。这为数据分析和科学研究提供了极大的便利，特别是在协作和远程工作的场景中。

通过这些案例，你将能够掌握在 Docker 中安装、配置和运行 Python 应用的基本技巧，这些技巧在实际的生产和工作环境中非常有用。这些案例不仅提供了一个实用的起点，也帮助你理解 Docker 在不同应用场景中的灵活性和强大功能。

## 1.3 Docker 的基本命令

掌握 Docker 的基本命令对于有效使用 Docker 来说至关重要。这一节将详细介绍 Docker 的一些核心命令，并通过实用的 Python 案例来展示这些命令的使用。

### 1.3.1 重点基础知识

为了有效地使用 Docker，了解其核心命令是至关重要的。这些命令涉及到容器的创建、运行、管理和镜像的处理。以下是 Docker 常用命令的详细讲解：
1.  **docker run**: 这是启动新容器的基本命令。例如，`docker run -d -p 5000:5000 flask-app` 会在后台运行一个 Flask 应用，并将容器的端口 5000 映射到主机的端口 5000。 1.  **docker build**: 此命令用于从 Dockerfile 创建一个新的镜像。例如，`docker build -t my-image-name .` 会根据当前目录的 Dockerfile 构建一个名为 `my-image-name` 的镜像。 1.  **docker images**: 用来列出本地所有的 Docker 镜像。这有助于查看已有的镜像及其标签和大小。 1.  **docker ps**: 列出当前运行的容器。使用 `docker ps -a` 可以查看所有容器，包括未运行的。 1.  **docker stop**: 用于停止一个或多个正在运行的容器。例如，`docker stop container_id` 会停止指定的容器。 1.  **docker rm**: 删除一个或多个容器。需要注意的是，只有停止的容器才能被删除。例如，`docker rm container_id` 会删除指定的容器。 1.  **docker rmi**: 删除一个或多个镜像。这是管理本地镜像空间的重要命令。例如，`docker rmi image_id` 会删除指定的镜像。 1.  **docker logs**: 查看容器的日志输出。这对于调试和了解容器的行为非常有用。例如，`docker logs container_id` 会显示指定容器的日志。 1.  **docker exec**: 在运行中的容器内执行命令。这常用于调试或修改容器内的设置。例如，`docker exec -it container_id bash` 会在指定的容器内启动一个交互式 bash shell。 1.  **docker pull**: 从 Docker Hub 或其他 Docker 仓库拉取（下载）镜像。例如，`docker pull ubuntu` 会从 Docker Hub 下载最新的 Ubuntu 镜像。 1.  **docker push**: 将本地镜像推送到 Docker Hub 或其他 Docker 仓库。在执行此命令之前，需要先登录到 Docker Hub。例如，`docker push my-username/my-image`。 
通过理解和实践这些基本命令，你将能够有效地管理 Docker 容器和镜像，为构建和部署应用提供坚实的基础。

### 1.3.2 重点案例：使用 Docker 运行 Python 脚本

在这个案例中，我们将展示如何使用 Docker 来运行一个简单的 Python 脚本。这个脚本会打印出当前的日期和时间，演示了如何在 Docker 容器中执行 Python 代码。

**步骤 1**: 创建 Python 脚本

首先，我们需要编写一个 Python 脚本。在你的工作目录中，创建一个名为 `date_time_script.py` 的文件，并添加以下内容：

```
# date_time_script.py
from datetime import datetime

print(f"Current date and time: {<!-- -->datetime.now()}")

```

这个脚本简单地输出当前的日期和时间。

**步骤 2**: 编写 Dockerfile

接下来，我们需要创建一个 Dockerfile 来定义如何在 Docker 容器中运行这个脚本。在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 使用官方 Python 运行时作为父镜像
FROM python:3.8

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录中的文件复制到容器的 /app 目录
COPY date_time_script.py /app/

# 运行 date_time_script.py 脚本时，调用 Python 解释器
CMD ["python", "./date_time_script.py"]

```

这个 Dockerfile 使用 Python 3.8 官方镜像作为基础，设置工作目录，并将我们的脚本复制到容器中。最后，它指定了容器启动时执行的命令。

**步骤 3**: 构建 Docker 镜像

现在，我们可以使用以下命令来构建我们的 Docker 镜像：

```
docker build -t datetime-python .

```

这个命令会根据 Dockerfile 构建一个名为 `datetime-python` 的镜像。

**步骤 4**: 运行 Docker 容器

一旦镜像构建完成，我们就可以运行一个基于该镜像的容器了：

```
docker run datetime-python

```

当这个命令执行时，它会启动一个新的容器实例，容器会运行 `date_time_script.py` 脚本，并显示输出。你应该会在命令行中看到类似 “Current date and time: 2023-02-24 15:30:00.123456” 的消息。

通过这个案例，你学会了如何使用 Docker 构建一个 Python 应用的运行环境，并且理解了 Docker 容器如何运行 Python 脚本。这为使用 Docker 处理更复杂的 Python 应用提供了基础。

### 1.3.3 拓展案例 1：Docker 中的 Flask 应用

在这个案例中，我们将通过 Docker 容器来部署一个简单的 Flask Web 应用。这个案例展示了如何使用 Docker 来封装和运行一个基于 Python 的 Web 应用，确保应用在不同环境下的一致性。

**步骤 1**: 创建 Flask 应用

首先，我们需要创建 Flask 应用的基础代码。在你的工作目录中，创建一个名为 `app.py` 的文件，并添加以下内容：

```
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Dockerized Flask!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

```

此代码创建了一个简单的 Flask 应用，它在根 URL (`/`) 上返回一条消息。

**步骤 2**: 添加依赖文件

接下来，创建一个名为 `requirements.txt` 的文件，列出 Flask 应用的依赖：

```
flask

```

**步骤 3**: 编写 Dockerfile

现在，我们编写一个 Dockerfile 来定义 Flask 应用的容器化。在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 使用官方 Python 运行时作为父镜像
FROM python:3.8

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录中的文件复制到容器的 /app 目录
COPY . /app

# 安装 requirements.txt 中的所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 使得端口 5000 可供此容器外的环境使用
EXPOSE 5000

# 定义环境变量
ENV FLASK_APP=app.py

# 运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]

```

**步骤 4**: 构建 Docker 镜像

使用以下命令来构建 Docker 镜像：

```
docker build -t flask-app .

```

这个命令会根据 Dockerfile 构建一个名为 `flask-app` 的镜像。

**步骤 5**: 运行 Docker 容器

构建完镜像后，使用以下命令运行容器：

```
docker run -p 5000:5000 flask-app

```

这个命令会启动一个基于 `flask-app` 镜像的容器，并将容器的 5000 端口映射到主机的 5000 端口。

现在，Flask 应用已在 Docker 容器中运行。在浏览器中访问 `http://localhost:5000`，你应该能看到 “Hello, Dockerized Flask!” 的消息。

通过这个案例，你可以看到 Docker 如何帮助我们轻松地部署一个 Flask Web 应用，并保证应用在不同环境中的一致性。这种方法不仅适用于开发和测试环境，也适用于生产环境，使得部署变得更加简单和可靠。

### 1.3.4 拓展案例 2：Docker 中的 Jupyter Notebook

在这个案例中，我们将演示如何使用 Docker 容器来部署 Jupyter Notebook，这是一个广泛使用的工具，用于数据分析和科学计算。Docker 化 Jupyter Notebook 可以确保在任何环境中都能以相同的方式运行，方便共享和协作。

**步骤 1**: 编写 Dockerfile

我们从创建 Dockerfile 开始，该文件定义了 Jupyter Notebook 运行所需的环境。在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 从官方 Python 镜像开始构建
FROM python:3.8-slim

# 安装 Jupyter Notebook
RUN pip install notebook

# 设置工作目录
WORKDIR /workspace

# 暴露 Jupyter Notebook 运行的端口
EXPOSE 8888

# 启动 Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

```

这个 Dockerfile 使用 Python 3.8 官方镜像作为基础，安装 Jupyter Notebook，并设置工作目录。它还暴露了运行 Jupyter Notebook 所需的端口，并定义了容器启动时执行的命令。

**步骤 2**: 构建 Docker 镜像

接下来，使用以下命令来构建 Docker 镜像：

```
docker build -t jupyter-notebook .

```

这个命令会根据 Dockerfile 构建一个名为 `jupyter-notebook` 的镜像。

**步骤 3**: 运行 Docker 容器

现在，我们可以运行这个镜像了：

```
docker run -p 8888:8888 jupyter-notebook

```

这个命令启动了一个 Docker 容器，将本地机器的 8888 端口映射到容器的 8888 端口。当容器启动后，它将运行 Jupyter Notebook。

在容器运行后，你会在命令行中看到一个 URL，其中包含了访问 Jupyter Notebook 的 token。复制并粘贴这个 URL 到浏览器中，你就可以开始在 Jupyter Notebook 中工作了。

**使用 Jupyter Notebook**

在 Jupyter Notebook 中，你可以创建新的笔记本来写 Python 代码，进行数据分析和可视化。例如，你可以导入数据分析和科学计算的库，如 Pandas、NumPy 和 Matplotlib，来分析数据集并绘制图表。

通过这个案例，你可以看到 Docker 如何帮助我们快速搭建一个数据分析环境。这个环境可以在不同机器上轻松复制和共享，非常适合团队合作和远程工作。使用 Docker 化的 Jupyter Notebook，数据科学家和分析师可以保证在任何地方都能以一致的方式工作，无需担心环境配置的不一致性。

这些案例展示了 Docker 在不同 Python 应用场景中的实用性，从简单脚本的执行到复杂的 Web 应用和数据分析环境的部署，反映了 Docker 在现代软件开发和数据科学中的广泛应用。通过这些案例，你可以更好地理解和掌握 Docker 的基本命令及其在实际生产环境中的应用。
