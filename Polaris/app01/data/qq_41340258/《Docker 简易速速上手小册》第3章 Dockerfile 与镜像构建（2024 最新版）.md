
--- 
title:  《Docker 简易速速上手小册》第3章 Dockerfile 与镜像构建（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/b3063ac18b2442bf9789dbccb2102b6d.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 3.1 编写 Dockerfile

Dockerfile 是 Docker 镜像构建的核心，它就像是制作美食的食谱，告诉 Docker 如何一步步构建出你需要的镜像。让我们深入了解 Dockerfile 的基础知识，并通过一些实际案例来展示它的强大功能。

### 3.1.1 重点基础知识

深入理解 Dockerfile 的构成和最佳实践对于高效创建和管理 Docker 镜像非常重要。以下是 Dockerfile 编写的一些关键概念和技巧：
<li> **精简基础镜像**: 
  1. 选择适当的基础镜像是关键。例如，对于 Python 应用，`python:3.8-slim` 或 `python:3.8-alpine` 是比 `python:3.8` 更轻量级的选择。 </li><li> **避免不必要的层**: 
  1. 每个 Dockerfile 指令都会创建一个新的镜像层。过多的层会增加镜像的大小。通过合并指令和清理不必要的文件，可以减少镜像层的数量。 </li><li> **使用 .dockerignore 文件**: 
  1. 类似于 `.gitignore`，`.dockerignore` 文件可以指定在构建过程中忽略的文件和目录，减少构建上下文的大小，加快构建速度。 </li><li> **多阶段构建**: 
  1. 多阶段构建允许你在一个 Dockerfile 中使用多个 FROM 指令，每个阶段可以使用不同的基础镜像。这对于优化镜像大小和构建速度非常有效。 </li><li> **利用缓存机制**: 
  1. Docker 会缓存每一步的结果，如果 Dockerfile 的某一部分没有更改，Docker 将重用这一部分的缓存。合理安排 Dockerfile 中指令的顺序，可以最大化地利用缓存。 </li><li> **参数化 Dockerfile**: 
  1. 使用 ARG 和 ENV 指令可以使 Dockerfile 更灵活。ARG 用于构建时设置变量，ENV 用于设置容器运行时的环境变量。 </li><li> **健康检查**: 
  1. 使用 HEALTHCHECK 指令可以让 Docker 定期检查容器的健康状态，这对于确保长时间运行的服务稳定性非常重要。 </li>- 每个 Dockerfile 指令都会创建一个新的镜像层。过多的层会增加镜像的大小。通过合并指令和清理不必要的文件，可以减少镜像层的数量。- 多阶段构建允许你在一个 Dockerfile 中使用多个 FROM 指令，每个阶段可以使用不同的基础镜像。这对于优化镜像大小和构建速度非常有效。- 使用 ARG 和 ENV 指令可以使 Dockerfile 更灵活。ARG 用于构建时设置变量，ENV 用于设置容器运行时的环境变量。
通过掌握这些基础知识，你将能够编写更高效、更专业的 Dockerfile，从而构建出性能更优、更安全且易于维护的 Docker 镜像。这些技巧对于任何使用 Docker 进行应用部署和管理的开发者或系统管理员来说都是非常宝贵的。

### 3.1.2 重点案例：创建简单 Python 应用的 Docker 镜像

让我们通过一个实际案例来学习如何为一个简单的 Python 应用创建 Docker 镜像。我们将从编写一个基本的 Python 脚本开始，然后创建一个 Dockerfile，并最终构建并运行该镜像。

**步骤 1**: 创建 Python 脚本

首先，我们需要一个简单的 Python 脚本作为我们应用的核心。在你的工作目录中，创建一个名为 `hello.py` 的文件，并添加以下内容：

```
# hello.py
def main():
    print("Hello, Docker World!")

if __name__ == "__main__":
    main()

```

这个脚本定义了一个打印欢迎信息的 `main` 函数。

**步骤 2**: 编写 Dockerfile

接下来，我们需要创建一个 Dockerfile 来定义如何在 Docker 容器中运行这个脚本。在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 使用官方 Python 运行时作为基础镜像
FROM python:3.8-slim

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录中的文件复制到容器的 /app 目录
COPY hello.py /app/

# 定义容器启动时执行的命令
CMD ["python", "./hello.py"]

```

这个 Dockerfile 从 Python 3.8 官方镜像开始，创建了一个工作目录 `/app`，然后将我们的 `hello.py` 脚本复制到这个目录中。最后，它定义了容器启动时执行的命令。

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建 Docker 镜像：

```
docker build -t hello-python-app .

```

这个命令会根据 Dockerfile 构建一个名为 `hello-python-app` 的镜像。

**步骤 4**: 运行 Docker 容器

一旦镜像构建完成，我们可以运行一个基于该镜像的容器：

```
docker run hello-python-app

```

执行这个命令后，Docker 会启动一个新的容器实例，容器会运行 `hello.py` 脚本，并在控制台输出 “Hello, Docker World!”。

通过这个案例，你学会了如何为一个简单的 Python 应用创建 Docker 镜像，并运行它。这个过程展示了从编写应用代码、创建 Dockerfile 到构建和运行 Docker 镜像的完整流程，是理解 Docker 容器化应用的基础。

### 3.1.3 拓展案例 1：Dockerfile 优化

在这个案例中，我们将通过优化一个现有的 Dockerfile 来减小 Python 应用的 Docker 镜像大小，并提高构建效率。这个过程是 Dockerfile 编写的重要部分，它可以确保你的镜像尽可能高效和轻量。

**步骤 1**: 创建初始 Python 应用

假设我们有一个简单的 Python 应用，它使用了几个外部库。在你的工作目录中，创建一个 `app.py` 和 `requirements.txt`：
<li> `app.py`: <pre><code class="prism language-python"># app.py
import flask
import pandas as pd

print("Hello, optimized Docker World!")
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
pandas
</code></pre> </li>
**步骤 2**: 编写初始 Dockerfile

创建一个初始的 Dockerfile，未进行优化：

```
# 初始 Dockerfile
FROM python:3.8

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "./app.py"]

```

**步骤 3**: 优化 Dockerfile

接下来，我们对 Dockerfile 进行优化，以减少镜像大小和提高构建速度：

```
# 优化后的 Dockerfile
FROM python:3.8-slim

# 安装依赖时一并清理缓存，减少镜像层大小
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt &amp;&amp; \
    rm -rf /var/lib/apt/lists/*

# 仅复制所需文件
COPY app.py .

CMD ["python", "./app.py"]

```

在这个优化后的 Dockerfile 中，我们做了以下几点改进：
- 切换到更轻量级的基础镜像 `python:3.8-slim`。- 在安装依赖后清理不必要的文件，如 APT 缓存。- 确保仅复制所需的文件到镜像中。
**步骤 4**: 重新构建并运行优化后的镜像

使用以下命令重新构建镜像，并观察大小的变化：

```
docker build -t optimized-python-app .

```

运行优化后的镜像：

```
docker run optimized-python-app

```

通过这个案例，你可以看到 Dockerfile 优化的重要性，以及如何通过简单的调整减小镜像大小并提升构建效率。这种优化对于提升应用的部署和运行效率至关重要，尤其是在生产环境中。

### 3.1.4 拓展案例 2：多阶段构建

在这个案例中，我们将使用 Docker 的多阶段构建来优化一个稍微复杂的 Python 应用的 Docker 镜像。多阶段构建可以帮助我们构建出更小、更安全的生产级镜像。

**步骤 1**: 准备 Python 应用

假设我们有一个 Python 应用，它不仅需要运行时依赖，还需要编译时依赖。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
import pandas as pd

print("Hello from a multi-stage Dockerized Python App!")
</code></pre> </li><li> `requirements.txt`: <pre><code>pandas
</code></pre> </li>
**步骤 2**: 编写多阶段 Dockerfile

我们将创建一个 Dockerfile，它包含两个阶段：构建阶段和最终阶段。

```
# 第一阶段：构建阶段
FROM python:3.8 as builder

WORKDIR /app

COPY requirements.txt .

# 安装所有依赖
RUN pip install --user -r requirements.txt

# 第二阶段：最终阶段
FROM python:3.8-slim

WORKDIR /app

# 从构建阶段复制已安装的 Python 依赖
COPY --from=builder /root/.local /root/.local

COPY app.py .

# 确保在运行时使用的是用户安装的库
ENV PATH=/root/.local:$PATH

CMD ["python", "./app.py"]

```

在这个 Dockerfile 中，第一阶段使用了完整的 Python 镜像来安装所有依赖。第二阶段则基于更轻量级的 `python:3.8-slim` 镜像，并从第一阶段复制了已安装的依赖。

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建 Docker 镜像：

```
docker build -t multi-stage-python-app .

```

这个命令会根据多阶段 Dockerfile 构建一个名为 `multi-stage-python-app` 的镜像。

**步骤 4**: 运行 Docker 容器

运行以下命令来启动 Python 应用：

```
docker run multi-stage-python-app

```

这个命令启动了一个基于新构建的镜像的容器。

通过这个案例，你可以看到多阶段构建在优化 Docker 镜像大小方面的巨大优势。这对于减少生产环境中的资源占用、加快镜像下载和部署速度非常关键。同时，它也提高了安全性，因为最终的镜像中不包含仅用于构建阶段的工具和文件。

通过这些案例，你不仅会学会编写基本的 Dockerfile，还会掌握如何优化和提高 Docker 镜像的效率，这对于提高应用的部署速度和安全性至关重要。

## 3.2 构建流程深入解析

探究 Docker 镜像构建流程的细节不仅是一项技术挑战，更像是解开神秘盒子的过程。在这一节中，我们将深入探索 Docker 镜像构建的内在机制，从而有效地掌握和优化构建过程。

### 3.2.1 重点基础知识

深入了解 Docker 镜像构建流程的细节对于有效地创建高质量的 Docker 镜像至关重要。下面是一些关于 Docker 镜像构建过程的进一步基础知识：
<li> **Dockerfile 指令详解**: 
  1. `FROM`: 指定基础镜像，是构建过程的起点。1. `RUN`: 执行命令并创建新的镜像层，用于安装软件、修改配置等。1. `COPY` 和 `ADD`: 用于将文件从宿主机复制到镜像。`ADD` 具有自动解压缩功能，但通常推荐使用更简单的 `COPY`。1. `CMD` 和 `ENTRYPOINT`: 指定容器启动时默认执行的命令。`CMD` 可被 `docker run` 后的命令行参数覆盖，而 `ENTRYPOINT` 则不会。 </li><li> **层的合并与优化**: 
  1. 虽然每个指令都会创建一个新的层，但 Docker 在最终镜像中会尽可能合并层来减少总大小。1. 通过合并多个 `RUN` 指令来减少层的数量，例如使用 `&amp;&amp;` 连接多个命令。 </li><li> **利用 ONBUILD 指令**: 
  1. `ONBUILD` 指令用于设置当镜像作为另一个构建的基础时将执行的操作。这对于创建基础镜像非常有用。 </li><li> **避免安装不必要的包**: 
  1. 只安装应用运行所必需的包和库，避免不必要的额外安装，可以显著减少镜像大小。 </li><li> **使用 ARG 和 ENV**: 
  1. `ARG` 用于定义构建阶段的变量，而 `ENV` 用于设置容器环境变量。适当使用这些指令可以增加 Dockerfile 的灵活性和可配置性。 </li>- 虽然每个指令都会创建一个新的层，但 Docker 在最终镜像中会尽可能合并层来减少总大小。- 通过合并多个 `RUN` 指令来减少层的数量，例如使用 `&amp;&amp;` 连接多个命令。- 只安装应用运行所必需的包和库，避免不必要的额外安装，可以显著减少镜像大小。
通过掌握这些高级技巧和最佳实践，你将能够创建出更加高效、安全且易于维护的 Docker 镜像。这些知识不仅有助于优化你的开发和部署流程，还能提升整个团队的工作效率和产品质量。

### 3.2.2 重点案例：构建 Python 应用的 Docker 镜像

让我们通过一个具体的案例来学习如何为一个 Python 应用构建 Docker 镜像。我们将从编写一个简单的 Python 应用开始，然后创建一个 Dockerfile，并最终构建并运行该镜像。

**步骤 1**: 创建 Python 应用

首先，我们创建一个 Python 应用。在你的工作目录中，创建一个名为 `app.py` 的文件，并添加以下内容：

```
# app.py
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Dockerized World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

这段代码创建了一个简单的 Flask 应用，它在根 URL (`/`) 上返回一条欢迎消息。

**步骤 2**: 编写 Dockerfile

接下来，创建一个 Dockerfile 来定义如何在 Docker 容器中运行这个 Flask 应用。在你的工作目录中，创建一个名为 `Dockerfile` 的文件，并添加以下内容：

```
# 使用官方 Python 镜像作为基础镜像
FROM python:3.8-slim

# 将工作目录设置为 /app
WORKDIR /app

# 复制 requirements.txt 文件，并安装 Python 依赖
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 将当前目录中的文件复制到容器的 /app 目录
COPY . /app

# 定义容器启动时执行的命令
CMD ["python", "app.py"]

```

在 `requirements.txt` 文件中，添加 Flask 的依赖：

```
flask

```

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建 Docker 镜像：

```
docker build -t python-flask-app .

```

这个命令会根据 Dockerfile 构建一个名为 `python-flask-app` 的镜像。

**步骤 4**: 运行 Docker 容器

一旦镜像构建完成，我们可以运行一个基于该镜像的容器：

```
docker run -p 5000:5000 python-flask-app

```

执行这个命令后，Docker 会启动一个新的容器实例，容器会运行 Flask 应用，并在端口 5000 上侦听。

通过访问 `http://localhost:5000`，你可以看到 Flask 应用的输出。

通过这个案例，你学会了如何为一个 Python Flask 应用创建 Docker 镜像，并运行它。这个过程展示了从编写应用代码、创建 Dockerfile 到构建和运行 Docker 镜像的完整流程。这种技能在现代软件开发中极为重要，尤其是在构建和部署微服务架构时。

### 3.2.3 拓展案例 1：优化 Docker 构建上下文

在这个案例中，我们将探讨如何优化 Docker 构建上下文，以加快 Python 应用的 Docker 镜像构建速度。优化构建上下文是提高 Docker 镜像构建效率的关键步骤之一。

**步骤 1**: 准备 Python 应用

假设我们的 Python 应用包含多个文件，其中一些文件对构建镜像并不必要。在你的工作目录中，创建以下文件：
- `app.py` (必需)- `requirements.txt` (必需)- `test.py` (不必要的测试脚本)- `data.csv` (大型数据文件，构建时不需要)
`app.py` 和 `requirements.txt` 文件的内容同前面案例。

**步骤 2**: 创建初始 Dockerfile

编写一个简单的 Dockerfile：

```
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]

```

**步骤 3**: 添加 .dockerignore 文件

创建 `.dockerignore` 文件来排除不必要的文件，减少构建上下文的大小：

```
test.py
data.csv

```

**步骤 4**: 重新构建 Docker 镜像

使用优化后的构建上下文重新构建 Docker 镜像：

```
docker build -t optimized-context-python-app .

```

**步骤 5**: 观察构建速度的变化

比较使用 `.dockerignore` 前后的构建速度。你会发现排除了不必要的文件后，构建速度有了明显的提升。

通过这个案例，你可以看到优化 Docker 构建上下文对提高构建效率的重要性。在实际开发中，通过精心管理构建上下文，可以显著减少构建时间，尤其是在持续集成/持续部署（CI/CD）的环境中。

### 3.2.4 拓展案例 2：利用多阶段构建优化镜像

在这个案例中，我们将演示如何使用 Docker 的多阶段构建来优化一个 Python 应用的 Docker 镜像。多阶段构建是一种有效的方法，可以帮助我们构建更小、更安全的镜像，特别适合于需要编译或有复杂依赖的应用。

**步骤 1**: 准备 Python 应用

假设我们的 Python 应用需要一些编译工作。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
import pandas as pd

print("Hello from a multi-stage Dockerized Python App!")
</code></pre> </li><li> `requirements.txt`: <pre><code>pandas
</code></pre> </li>
**步骤 2**: 编写多阶段 Dockerfile

我们将创建一个包含两个阶段的 Dockerfile，其中第一阶段用于安装和编译依赖，第二阶段用于创建最终的运行时镜像。

```
# 第一阶段：构建阶段
FROM python:3.8 as builder

WORKDIR /app

COPY requirements.txt .

# 安装依赖
RUN pip install --user -r requirements.txt

# 第二阶段：运行阶段
FROM python:3.8-slim

WORKDIR /app

# 从构建阶段复制已安装的 Python 依赖
COPY --from=builder /root/.local /root/.local

COPY app.py .

# 确保在运行时使用的是用户安装的库
ENV PATH=/root/.local:$PATH

CMD ["python", "./app.py"]

```

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建 Docker 镜像：

```
docker build -t multi-stage-optimized-python-app .

```

这个命令会根据多阶段 Dockerfile 构建一个名为 `multi-stage-optimized-python-app` 的镜像。

**步骤 4**: 运行 Docker 容器

运行以下命令来启动 Python 应用：

```
docker run multi-stage-optimized-python-app

```

这个命令启动了一个基于新构建的镜像的容器。

通过这个案例，你可以看到多阶段构建如何帮助我们创建了一个更加精简且功能完整的 Docker 镜像。这种方法对于减少生产环境中的资源占用、加快镜像下载和部署速度具有重要意义。同时，它也增加了安全性，因为最终的镜像中不包含仅用于构建阶段的工具和文件。

通过深入了解 Docker 构建流程的这些知识和案例，你将能够更有效地构建高质量的 Docker 镜像，优化构建过程，提高开发效率。掌握这些技能，你将在 Docker 镜像构建方面更加游刃有余。

## 3.3 镜像构建的最佳实践

在 Docker 镜像构建中遵循最佳实践是确保镜像高效、安全且易于维护的关键。让我们深入了解这些实践，并通过具体案例加深理解。

### 3.3.1 重点基础知识

在 Docker 镜像构建过程中，遵循一系列最佳实践可以帮助你创建出更高效、更安全且易于维护的镜像。这些实践不仅适用于简单的应用，也适用于复杂的生产级应用。让我们进一步深入这些最佳实践。
<li> **使用特定版本的基础镜像**: 
  1. 指定基础镜像的具体版本，而不是使用标签如 `latest`，以确保构建的一致性和可预测性。 </li><li> **利用 Docker 缓存机制**: 
  1. 将不经常变更的指令放在 Dockerfile 的顶部，如安装软件包，以最大化利用 Docker 的层缓存。 </li><li> **避免在运行时使用 root 用户**: 
  1. 出于安全考虑，创建并使用非 root 用户运行你的应用。这可以减少容器内部发生的潜在安全风险。 </li><li> **使用 COPY 而非 ADD**: 
  1. 除非需要自动解压缩功能，否则优先使用 `COPY`。`COPY` 更简单、更透明。 </li><li> **精简命令和层**: 
  1. 尽量使用链式命令和逻辑运算符（如 `&amp;&amp;`）来合并 `RUN` 指令，减少镜像层的数量。 </li><li> **避免安装不必要的软件**: 
  1. 仅安装运行应用所必需的软件包，避免增加不必要的额外负担。 </li><li> **定期更新和维护**: 
  1. 定期更新镜像以包含安全修复和更新。及时删除不再使用的旧镜像和层，以节省存储空间。 </li><li> **多阶段构建中的目标阶段**: 
  1. 在多阶段构建中，明确标记目标阶段，以便只构建最终所需的镜像部分，减少构建时间和资源消耗。 </li>- 将不经常变更的指令放在 Dockerfile 的顶部，如安装软件包，以最大化利用 Docker 的层缓存。- 除非需要自动解压缩功能，否则优先使用 `COPY`。`COPY` 更简单、更透明。- 仅安装运行应用所必需的软件包，避免增加不必要的额外负担。- 在多阶段构建中，明确标记目标阶段，以便只构建最终所需的镜像部分，减少构建时间和资源消耗。
遵循这些高级技巧和最佳实践，将帮助你构建出更优质的 Docker 镜像。这些实践不仅提高了镜像的性能和安全性，还确保了你的镜像在部署和维护过程中更加高效和可靠。

### 3.3.2 重点案例：构建轻量级的 Python Web 应用镜像

在这个案例中，我们将构建一个轻量级的 Python Flask Web 应用的 Docker 镜像。我们将应用 Docker 镜像构建的最佳实践，以创建一个高效且易于维护的镜像。

**步骤 1**: 创建 Flask 应用

首先，我们需要创建 Flask 应用的基本代码。在你的工作目录中，创建一个名为 `app.py` 的文件，并添加以下内容：

```
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Dockerized Flask!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

```

同时，创建一个 `requirements.txt` 文件，包含 Flask 依赖：

```
flask

```

**步骤 2**: 编写 Dockerfile

接下来，我们编写 Dockerfile 来优化镜像大小和构建速度：

```
# 使用官方 Python Slim 镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 复制仅构建所需的文件
COPY requirements.txt /app/

# 安装依赖，利用 Docker 层缓存
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py /app/

# 指定非 root 用户运行容器
RUN useradd appuser &amp;&amp; chown -R appuser /app
USER appuser

# 定义容器启动时执行的命令
CMD ["python", "app.py"]

```

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建 Docker 镜像：

```
docker build -t lightweight-python-flask-app .

```

**步骤 4**: 运行 Docker 容器

一旦镜像构建完成，我们可以运行一个基于该镜像的容器：

```
docker run -p 5000:5000 lightweight-python-flask-app

```

这个命令启动了一个基于新构建镜像的容器，并将容器的 5000 端口映射到了你的主机的 5000 端口。

通过访问 `http://localhost:5000`，你可以看到 Flask 应用的输出。

通过这个案例，你学会了如何构建一个轻量级的 Python Flask Web 应用的 Docker 镜像。这种方法不仅优化了镜像的大小，还提高了构建速度和安全性。这对于在生产环境中部署 Web 应用是非常重要的。

### 3.3.3 拓展案例 1：优化 Dockerfile 结构

在这个案例中，我们将优化一个 Python 应用的 Dockerfile 结构，以提高构建效率和提升安全性。我们的目标是优化构建过程，并确保应用在容器中以非 root 用户运行。

**步骤 1**: 准备 Python 应用

假设我们已有一个基本的 Python Flask 应用。在你的工作目录中，创建 `app.py` 和 `requirements.txt`：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Optimized Docker World!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写初始 Dockerfile

创建一个未优化的 Dockerfile：

```
FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

```

**步骤 3**: 优化 Dockerfile

现在，我们将对 Dockerfile 进行优化，包括重新排序命令以利用 Docker 缓存，使用 `python:3.8-slim` 作为基础镜像，并设置非 root 用户运行：

```
# 使用更轻量级的基础镜像
FROM python:3.8-slim

# 先复制 requirements.txt 文件并安装依赖
# 这一步可以利用 Docker 缓存，如果依赖没有变更，不需要重新安装
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# 然后复制应用代码
COPY . /app

# 创建非 root 用户并切换，提升容器安全性
RUN useradd -m appuser
USER appuser

CMD ["python", "app.py"]

```

**步骤 4**: 重新构建 Docker 镜像

使用优化后的 Dockerfile 重新构建 Docker 镜像：

```
docker build -t optimized-structure-python-app .

```

**步骤 5**: 运行 Docker 容器

运行优化后的容器：

```
docker run -p 5000:5000 optimized-structure-python-app

```

通过这个案例，你可以看到 Dockerfile 结构的优化如何影响构建效率和容器的安全性。通过合理地组织 Dockerfile 指令和使用轻量级的基础镜像，我们不仅提高了镜像的构建速度，还增强了应用的安全性。

### 3.3.4 拓展案例 2：多阶段构建的复杂 Python 应用

在这个案例中，我们将展示如何使用 Docker 的多阶段构建为一个包含复杂依赖的 Python 应用创建优化的 Docker 镜像。这种方法特别适用于那些需要编译步骤或具有多个依赖层的应用。

**步骤 1**: 准备 Python 应用

我们的 Python 应用将使用 Pandas 库进行数据处理。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
import pandas as pd

def main():
    print("Pandas version:", pd.__version__)
    print("Hello from a multi-stage Dockerized Python App!")

if __name__ == "__main__":
    main()
</code></pre> </li><li> `requirements.txt`: <pre><code>pandas
</code></pre> </li>
**步骤 2**: 编写多阶段 Dockerfile

为了优化镜像大小和构建时间，我们使用多阶段构建：

```
# 第一阶段：构建阶段
FROM python:3.8 as builder

WORKDIR /app

COPY requirements.txt .

# 安装依赖
RUN pip install --user -r requirements.txt

# 第二阶段：运行阶段
FROM python:3.8-slim

WORKDIR /app

# 从构建阶段复制已安装的 Python 依赖
COPY --from=builder /root/.local /root/.local

# 复制应用代码
COPY app.py .

# 确保在运行时使用的是用户安装的库
ENV PATH=/root/.local:$PATH

CMD ["python", "./app.py"]

```

**步骤 3**: 构建 Docker 镜像

使用以下命令来构建多阶段的 Docker 镜像：

```
docker build -t multi-stage-complex-python-app .

```

**步骤 4**: 运行 Docker 容器

运行以下命令来启动 Python 应用：

```
docker run multi-stage-complex-python-app

```

这个命令启动了一个基于新构建的镜像的容器。

通过这个案例，你可以看到多阶段构建如何帮助创建一个更小、更高效的 Docker 镜像，尤其是对于那些依赖较重的应用。多阶段构建使得我们可以在构建阶段安装和准备一切所需，而在最终的镜像中只包含运行应用所必需的组件，这样既优化了镜像大小，也提升了安全性。

遵循这些最佳实践可以显著提高 Docker 镜像的质量，使其更适合在生产环境中使用。这些技巧不仅有助于提高开发和部署的效率，还能增强应用的安全性。
