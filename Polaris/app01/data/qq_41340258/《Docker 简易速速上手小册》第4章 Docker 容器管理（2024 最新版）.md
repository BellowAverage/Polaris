
--- 
title:  《Docker 简易速速上手小册》第4章 Docker 容器管理（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/209014f0a8544c10837d296a7abb0af5.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 4.1 容器生命周期管理

管理 Docker 容器的生命周期就像是驾驶宇宙飞船，你需要了解如何启动、停止，甚至是销毁这些飞船。这一节将带你穿梭在 Docker 容器的生命周期管理的浩瀚宇宙中。

### 4.1.1 重点基础知识

深入理解 Docker 容器的生命周期管理是掌握 Docker 使用的关键。下面是一些关于容器生命周期管理的进一步基础知识，它们将帮助你更好地管理你的 Docker 容器。
<li> **容器创建**: 
  1. 使用 `docker create` 创建一个容器但不启动它。这允许你先配置容器（例如，设置网络和卷），然后再用 `docker start` 命令启动。 </li><li> **容器状态检查**: 
  1. `docker inspect` 命令提供了关于容器配置和状态的详细信息，包括 IP 地址、使用的端口和挂载的卷。 </li><li> **容器资源限制**: 
  1. 在创建或运行容器时，可以通过各种选项限制其使用的资源，如 CPU、内存等。这对于确保容器不会消耗过多主机资源非常重要。 </li><li> **容器与主机间的数据拷贝**: 
  1. `docker cp` 命令可以在容器和主机间拷贝文件。这在需要快速复制日志文件或其他数据时非常有用。 </li><li> **容器内部运行命令**: 
  1. `docker exec` 命令允许你在运行中的容器内执行命令，这对于调试和管理操作非常方便。 </li><li> **容器日志管理**: 
  1. 了解如何查看和管理容器日志。`docker logs` 命令可以帮助你快速定位问题。 </li><li> **容器的优雅停止**: 
  1. 当使用 `docker stop` 命令时，Docker 会首先向容器发送 SIGTERM 信号，允许容器优雅地停止。如果在指定时间后容器仍未停止，Docker 会发送 SIGKILL 信号强制停止。 </li>- `docker inspect` 命令提供了关于容器配置和状态的详细信息，包括 IP 地址、使用的端口和挂载的卷。- `docker cp` 命令可以在容器和主机间拷贝文件。这在需要快速复制日志文件或其他数据时非常有用。- 了解如何查看和管理容器日志。`docker logs` 命令可以帮助你快速定位问题。
通过掌握这些高级技巧和知识，你将能够有效地管理 Docker 容器的生命周期，确保容器的稳定运行和高效管理。这些技能对于任何需要在生产环境中使用 Docker 的人员来说都是非常宝贵的。

### 4.1.2 重点案例：启动并管理 Python Flask 应用容器

让我们通过一个实际案例来学习如何启动并管理一个 Python Flask 应用的 Docker 容器。这个案例将覆盖从创建容器到管理其生命周期的各个阶段。

**步骤 1**: 准备 Flask 应用

首先，我们需要准备 Flask 应用。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Dockerized Flask App!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

接下来，编写一个 Dockerfile 用于构建 Flask 应用的镜像：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "app.py"]

```

**步骤 3**: 构建 Docker 镜像

在包含 Dockerfile 的目录中，运行以下命令来构建镜像：

```
docker build -t flask-app .

```

**步骤 4**: 启动 Flask 应用容器

使用以下命令启动 Flask 应用的 Docker 容器：

```
docker run -d -p 5000:5000 --name my-flask-app flask-app

```

这里 `-d` 参数让容器在后台运行，`-p` 参数映射了容器和主机的端口。

**步骤 5**: 查看容器日志

要查看 Flask 应用的输出，可以使用：

```
docker logs my-flask-app

```

**步骤 6**: 停止和重启容器

若需要停止容器，可以使用：

```
docker stop my-flask-app

```

要重启已停止的容器，使用：

```
docker start my-flask-app

```

**步骤 7**: 清理容器

使用完容器后，可以将其删除：

```
docker rm my-flask-app

```

通过这个案例，你不仅学会了如何为 Flask 应用创建和启动 Docker 容器，还掌握了如何管理容器的基本生命周期，包括查看日志、停止、重启和删除容器。这些技能对于任何使用 Docker 部署和管理 Web 应用的开发者来说都是非常有用的。

### 4.1.3 拓展案例 1：调试运行中的容器

在这个案例中，我们将探索如何进入一个正在运行的 Docker 容器以进行调试。这是一项非常实用的技能，特别是当你需要诊断或解决运行时问题时。

**步骤 1**: 运行 Flask 应用容器

首先，确保 Flask 应用的 Docker 容器正在运行。如果尚未运行，可以参考之前的案例来启动它。

**步骤 2**: 进入运行中的容器

使用 `docker exec` 命令进入正在运行的容器。这个命令允许你在容器内部启动一个新的交互式命令行会话：

```
docker exec -it my-flask-app /bin/bash

```

这里，`my-flask-app` 是你的容器名称，`/bin/bash` 是你想在容器内部运行的 shell。对于不包含 bash 的轻量级镜像，你可能需要使用 `/bin/sh` 或其他 shell。

**步骤 3**: 在容器内执行命令

一旦进入容器，你就可以像在普通 Linux 环境中一样执行命令了。例如，你可以查看当前目录的文件列表，检查环境变量或者安装额外的调试工具：

```
ls -l
printenv
apt-get update &amp;&amp; apt-get install -y curl

```

**步骤 4**: 退出容器

完成调试后，可以输入 `exit` 命令来离开容器。

**注意**：在容器内执行的任何更改（比如安装的额外软件包）都不会保存到镜像中，且只在当前容器实例中有效。

通过这个案例，你学会了如何进入正在运行的 Docker 容器并执行调试操作。这种能力对于快速定位和解决应用运行时的问题至关重要，是每位 Docker 用户必备的技能之一。

### 4.1.4 拓展案例 2：优雅地停止和清理容器

在这个案例中，我们将学习如何优雅地停止一个运行中的 Docker 容器，并在停止后清理容器实例。这是确保容器资源被妥善管理和释放的重要步骤。

**步骤 1**: 运行 Flask 应用容器

确保你的 Flask 应用容器正在运行。如果尚未启动，可以参考之前的指南来启动它。例如：

```
docker run -d -p 5000:5000 --name my-flask-app flask-app

```

**步骤 2**: 优雅地停止容器

当你需要停止容器时，使用 `docker stop` 命令。这个命令会向容器发送 SIGTERM 信号，提醒容器优雅地停止。默认情况下，Docker 会等待 10 秒让应用处理停止请求：

```
docker stop my-flask-app

```

**步骤 3**: 确认容器已停止

使用 `docker ps -a` 命令确认容器的状态。你会看到 `my-flask-app` 容器的状态为 `Exited`。

```
docker ps -a

```

**步骤 4**: 清理停止的容器

停止容器后，它仍然会占用磁盘空间。为了释放这些资源，可以使用 `docker rm` 命令来删除容器：

```
docker rm my-flask-app

```

**步骤 5**: 验证容器已被删除

再次运行 `docker ps -a` 命令确认容器已被删除。你不应该再看到 `my-flask-app` 容器。

通过这个案例，你可以看到如何优雅地停止并清理 Docker 容器。这不仅是良好的资源管理实践，也是维护 Docker 环境整洁的关键步骤。掌握这些技巧可以帮助你高效地管理容器资源，保持你的 Docker 环境的清洁和有序。

通过这些案例的学习，你将能够有效地管理 Docker 容器的生命周期，从容器的诞生到退休，每一个环节都能游刃有余。掌握这些技能，你将成为 Docker 宇宙中的优秀飞行员！

## 4.2 容器数据管理与持久化

在 Docker 世界中，数据管理和持久化是一项至关重要的技能。它就像是给你的容器建造一个记忆盒子，即使容器消失了，记忆仍然留存。让我们深入了解如何在 Docker 中管理数据，并保证它的持久性。

### 4.2.1 重点基础知识

深入理解 Docker 容器的数据管理与持久化是保证数据安全和高效使用 Docker 的关键。以下是关于容器数据管理与持久化的更多基础知识，帮助你更好地理解和应用这些概念。
<li> **卷（Volumes）的高级管理**: 
  1. 可以在 Docker 主机上全局管理卷，包括创建、列出、删除未使用的卷等。这有助于更好地组织和清理数据。1. 卷可以在容器之间或者在 Dockerfile 中使用，为应用提供灵活性和可重用性。 </li><li> **绑定挂载的路径和权限**: 
  1. 绑定挂载时，可以指定路径和权限，例如只读挂载，以确保容器内的应用不会意外修改宿主机上的数据。1. 路径可以是相对的或绝对的，这在进行本地开发和测试时特别有用。 </li><li> **使用 Docker Compose 管理卷和挂载**: 
  1. Docker Compose 允许你在 `docker-compose.yml` 文件中定义和管理卷及挂载，这对于复杂应用的数据管理更加直观和方便。 </li><li> **卷驱动的选择**: 
  1. Docker 提供了不同的卷驱动，支持各种存储需求，例如本地存储、网络存储等。根据应用的具体需求选择合适的卷驱动非常重要。 </li><li> **备份和迁移数据**: 
  1. 了解如何备份和迁移 Docker 卷中的数据是确保数据安全的关键。这包括将卷数据导出到文件系统，或者迁移到其他 Docker 主机上。 </li><li> **数据持久化的策略**: 
  1. 根据应用的特点和需求，制定合适的数据持久化策略。例如，对于数据库应用，可能需要频繁备份和高可用性的存储解决方案。 </li>- 绑定挂载时，可以指定路径和权限，例如只读挂载，以确保容器内的应用不会意外修改宿主机上的数据。- 路径可以是相对的或绝对的，这在进行本地开发和测试时特别有用。- Docker 提供了不同的卷驱动，支持各种存储需求，例如本地存储、网络存储等。根据应用的具体需求选择合适的卷驱动非常重要。- 根据应用的特点和需求，制定合适的数据持久化策略。例如，对于数据库应用，可能需要频繁备份和高可用性的存储解决方案。
通过掌握这些高级知识，你将能够更有效地管理 Docker 容器中的数据，并确保数据的持久化和安全。这些技能对于任何需要在 Docker 环境中处理和存储重要数据的开发者或管理员来说都是非常宝贵的。

### 4.2.2 重点案例：使用卷存储 Python 应用数据

在这个案例中，我们将创建一个 Python Flask 应用，并使用 Docker 卷来持久化存储应用数据。这是一个常见的场景，特别是当你的应用需要保存状态或用户数据时。

**步骤 1**: 创建 Flask 应用

首先，我们需要准备 Flask 应用。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open('/data/count.txt', 'a+') as file:
        file.seek(0)
        count = file.read() or '0'
        count = int(count) + 1
        file.seek(0)
        file.write(str(count))
        file.truncate()
    return f'Hello, Dockerized Flask! This page has been visited {<!-- -->count} times.'

if __name__ == '__main__':
    if not os.path.exists('/data'):
        os.makedirs('/data')
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

编写一个 Dockerfile 用于构建 Flask 应用的镜像：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "app.py"]

```

**步骤 3**: 构建 Docker 镜像

在包含 Dockerfile 的目录中，运行以下命令来构建镜像：

```
docker build -t flask-app-with-volume .

```

**步骤 4**: 创建并启动容器，绑定卷

使用以下命令启动 Flask 应用的 Docker 容器，并绑定一个卷来持久化 `count.txt` 文件：

```
docker run -d -p 5000:5000 --name my-flask-app -v flask-data:/data flask-app-with-volume

```

这里，`flask-data` 是一个 Docker 卷，`/data` 是容器内的路径。

**步骤 5**: 访问和测试应用

访问 `http://localhost:5000` 并多次刷新页面，你将看到访问次数的增加。即使容器重启，计数也不会丢失，因为它被保存在 Docker 卷中。

通过这个案例，你学会了如何使用 Docker 卷为 Python Flask 应用提供持久化数据存储。这样即使容器被删除，卷中的数据仍然安全。这是管理涉及状态或需要持久化存储的容器化应用时的一个关键技巧。

### 4.2.3 拓展案例 1：使用绑定挂载进行数据持久化

在这个案例中，我们将展示如何通过绑定挂载（bind mounts）在 Docker 容器中实现数据持久化。绑定挂载是一种直接映射宿主机文件系统到容器的方式，非常适合开发环境中的快速数据共享和测试。

**步骤 1**: 创建 Flask 应用

首先，准备 Flask 应用。在你的工作目录中，创建 `app.py` 和 `requirements.txt`：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    filepath = '/mnt/data/count.txt'
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write('0')
    
    with open(filepath, 'r+') as file:
        count = int(file.read()) + 1
        file.seek(0)
        file.write(str(count))
        file.truncate()
    
    return f'This page has been visited {<!-- -->count} times.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

创建一个 Dockerfile 用于构建 Flask 应用的镜像：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "app.py"]

```

**步骤 3**: 构建 Docker 镜像

在包含 Dockerfile 的目录中，运行以下命令来构建镜像：

```
docker build -t flask-app-bind-mount .

```

**步骤 4**: 创建宿主机目录并启动容器

在宿主机上创建一个目录用于挂载：

```
mkdir /path/to/local/data

```

使用以下命令启动 Flask 应用的 Docker 容器，并通过绑定挂载连接到刚刚创建的宿主机目录：

```
docker run -d -p 5000:5000 --name my-flask-app -v /path/to/local/data:/mnt/data flask-app-bind-mount

```

**步骤 5**: 访问和测试应用

访问 `http://localhost:5000` 并多次刷新页面。检查 `/path/to/local/data/count.txt` 文件，你会发现页面访问次数被正确记录。

通过这个案例，你学会了如何使用绑定挂载在 Docker 容器中实现数据的持久化。这种方法对于开发环境特别有用，因为它允许你直接在宿主机上访问和修改容器内的文件，从而实现快速的开发和测试。

### 4.2.4 拓展案例 2：使用临时存储管理敏感数据

在这个案例中，我们将通过使用 Docker 的临时存储（tmpfs 挂载）来处理和管理敏感数据。这种方法特别适用于处理需要在容器运行时保留但不应该持久化到硬盘的敏感信息。

**步骤 1**: 创建 Flask 应用

创建一个简单的 Flask 应用，它会生成并存储一些敏感数据。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    sensitive_path = '/tmp/sensitive_data.txt'
    with open(sensitive_path, 'a+') as file:
        file.write("Very sensitive information\n")
    return 'Sensitive data written to temporary storage.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

编写 Dockerfile 来构建 Flask 应用的镜像：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "app.py"]

```

**步骤 3**: 构建 Docker 镜像

运行以下命令来构建 Flask 应用的 Docker 镜像：

```
docker build -t flask-app-tmpfs .

```

**步骤 4**: 启动 Flask 应用容器，使用 tmpfs

启动 Flask 应用的 Docker 容器，并使用 tmpfs 挂载来创建临时存储区：

```
docker run -d -p 5000:5000 --name my-flask-app --tmpfs /tmp flask-app-tmpfs

```

这个命令会创建一个名为 `/tmp` 的 tmpfs 挂载点，所有写入该路径的数据都只会存储在内存中。

**步骤 5**: 访问应用并验证临时存储

访问 `http://localhost:5000`，应用会写入敏感数据到临时存储中。尽管数据写入了 `/tmp/sensitive_data.txt`，但由于使用了 tmpfs，这些数据仅在内存中存在，并不会持久化到硬盘。

通过这个案例，你学会了如何在 Docker 容器中使用临时存储来处理敏感数据。这种方法在处理需要高度保密性的数据时非常有用，确保了数据的安全性，同时便于在应用重启或容器销毁时自动清理这些数据。

通过这些案例，你将能够掌握 Docker 容器中数据的管理和持久化。无论是将数据永久保存还是仅在容器运行时保留，你都有了相应的工具和知识来处理这些情况。这在构建可靠且安全的 Docker 应用时非常重要。

## 4.3 容器网络配置

欢迎来到 Docker 容器网络的世界！在这一章中，我们将像网络专家一样探索 Docker 容器网络的奥秘。了解容器如何通信、如何配置网络，可以帮助你更好地管理和部署容器应用。

### 4.3.1 重点基础知识

掌握 Docker 容器网络配置是确保容器应用顺利运行的关键。了解不同网络类型、如何连接容器以及如何隔离容器是非常重要的。以下是容器网络配置的更多基础知识，帮助你深入理解 Docker 网络的工作原理。
<li> **网络类型详解**: 
  1. `bridge`：默认网络类型，适用于单机上的容器通信。1. `host`：移除了网络隔离，容器直接使用宿主机的网络。1. `overlay`：用于跨多个 Docker 主机的容器通信，常用于 Docker Swarm。1. `none`：禁用所有网络。 </li><li> **网络隔离和安全**: 
  1. Docker 网络提供了隔离机制，增强了容器之间的安全性。1. 了解如何配置网络策略，可以更有效地控制容器间的通信权限。 </li><li> **服务发现与 DNS**: 
  1. 在自定义网络中，Docker 提供了内建的 DNS 服务，容器可以通过服务名称互相发现和通信。1. 这消除了容器间通信中硬编码 IP 地址的需要。 </li><li> **网络命令行工具**: 
  1. Docker 提供了一系列命令行工具来管理网络，如 `docker network create`、`docker network ls`、`docker network inspect` 等。1. 这些工具对于诊断网络问题、审查网络配置等非常有用。 </li><li> **端口映射与暴露**: 
  1. 除了使用 `-p` 参数进行端口映射，还可以使用 `EXPOSE` 指令在 Dockerfile 中声明容器监听的端口，增加文档化和清晰度。 </li><li> **容器连接的最佳实践**: 
  1. 使用自定义网络而非旧式的 `--link` 方法来连接容器。1. 在复杂应用中，考虑使用 Docker Compose 来管理容器和网络，简化部署和配置。 </li>- Docker 网络提供了隔离机制，增强了容器之间的安全性。- 了解如何配置网络策略，可以更有效地控制容器间的通信权限。- Docker 提供了一系列命令行工具来管理网络，如 `docker network create`、`docker network ls`、`docker network inspect` 等。- 这些工具对于诊断网络问题、审查网络配置等非常有用。- 使用自定义网络而非旧式的 `--link` 方法来连接容器。- 在复杂应用中，考虑使用 Docker Compose 来管理容器和网络，简化部署和配置。
通过掌握这些高级知识，你将能够更加精确地控制你的 Docker 容器网络，提升应用的连通性和安全性。这对于构建可扩展和安全的容器化应用至关重要。

### 4.3.2 重点案例：配置 Python Flask 应用的网络

在这个案例中，我们将通过配置网络来部署一个 Python Flask 应用。这个过程不仅包括容器的创建和运行，还涉及到如何通过 Docker 网络让应用能够被外界访问。

**步骤 1**: 准备 Flask 应用

首先，创建 Flask 应用。在你的工作目录中，创建 `app.py` 和 `requirements.txt`：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Dockerized Flask App accessible from outside!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

接下来，编写 Dockerfile 来构建 Flask 应用的镜像：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 5000
CMD ["python", "app.py"]

```

这里的 `EXPOSE 5000` 命令是用于文档化，表明容器会在 5000 端口上监听连接。

**步骤 3**: 构建 Docker 镜像

在包含 Dockerfile 的目录中，运行以下命令来构建镜像：

```
docker build -t flask-app-network .

```

**步骤 4**: 启动 Flask 应用容器，并映射端口

使用以下命令启动 Flask 应用的 Docker 容器，并映射端口以使应用可从外部访问：

```
docker run -d -p 8000:5000 --name my-flask-app flask-app-network

```

这里，我们将容器的 5000 端口映射到宿主机的 8000 端口。

**步骤 5**: 访问 Flask 应用

现在，你可以通过访问 `http://localhost:8000` 来查看 Flask 应用。你应该能看到欢迎消息。

通过这个案例，你学会了如何为 Flask 应用配置 Docker 网络，使得应用不仅在容器内运行，还能被外部网络访问。这是部署 Web 应用时的一个常见需求，了解如何配置和管理 Docker 网络对于确保应用的可访问性至关重要。

### 4.3.3 拓展案例 1：容器间通信

在这个案例中，我们将演示如何使两个 Docker 容器之间进行通信。我们将部署两个 Flask 应用，一个作为前端服务，另一个作为后端 API，演示它们如何在 Docker 中相互通信。

**步骤 1**: 创建前端 Flask 应用

首先，创建一个前端 Flask 应用。在你的工作目录中，创建 `frontend.py` 和 `requirements.txt`：
<li> `frontend.py`: <pre><code class="prism language-python"># frontend.py
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("http://backend:5000/api")
    return f'Frontend calling backend: {<!-- -->response.text}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
requests
</code></pre> </li>
**步骤 2**: 创建后端 Flask API

创建一个后端 Flask 应用。在你的工作目录中，创建 `backend.py`：
<li> `backend.py`: <pre><code class="prism language-python"># backend.py
from flask import Flask

app = Flask(__name__)

@app.route('/api')
def api():
    return 'Hello from Backend!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li>
**步骤 3**: 创建 Dockerfile

对于前端和后端，可以使用相同的 Dockerfile：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "frontend.py"]

```

**步骤 4**: 构建 Docker 镜像

分别为前端和后端构建 Docker 镜像：

```
docker build -t flask-frontend-app -f Dockerfile .
docker build -t flask-backend-app -f Dockerfile .

```

**步骤 5**: 创建自定义网络

创建一个 Docker 自定义网络来实现容器间通信：

```
docker network create flask-network

```

**步骤 6**: 启动 Flask 容器

在创建的网络中启动两个 Flask 容器：

```
docker run -d --name frontend --network flask-network -p 8000:5000 flask-frontend-app
docker run -d --name backend --network flask-network flask-backend-app

```

**步骤 7**: 访问前端服务

现在，你可以通过访问 `http://localhost:8000` 来测试前端服务是否能成功调用后端 API。

通过这个案例，你学会了如何在 Docker 中创建自定义网络，并在此网络下运行多个容器以实现容器间的通信。这种方法对于部署由多个服务组成的应用非常有效，能够保证服务之间的高效通信。

### 4.3.4 拓展案例 2：使用 Docker Compose 管理网络

在这个案例中，我们将使用 Docker Compose 来管理一个包含 Flask 应用和数据库服务的网络。Docker Compose 是一个工具，用于定义和运行多容器 Docker 应用。通过一个 YAML 文件，可以配置应用服务、网络和卷等资源。

**步骤 1**: 创建 Flask 应用

首先，创建一个 Flask 应用。在你的工作目录中，创建以下文件：
<li> `app.py`: <pre><code class="prism language-python"># app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({<!-- -->"message": "Hello from Flask App!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
</code></pre> </li><li> `requirements.txt`: <pre><code>flask
</code></pre> </li>
**步骤 2**: 编写 Dockerfile

创建 Dockerfile 来构建 Flask 应用的镜像：

```
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "app.py"]

```

**步骤 3**: 创建 Docker Compose 文件

编写 `docker-compose.yml` 文件来定义 Flask 应用和数据库服务：

```
version: '3'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    networks:
      - app-network

  db:
    image: postgres
    environment:
      POSTGRES_DB: exampledb
      POSTGRES_USER: exampleuser
      POSTGRES_PASSWORD: examplepass
    networks:
      - app-network

networks:
  app-network:

```

这里，我们定义了两个服务：`web`（Flask 应用）和 `db`（Postgres 数据库）。它们都连接到一个名为 `app-network` 的自定义网络。

**步骤 4**: 使用 Docker Compose 启动服务

运行以下命令来构建镜像并启动服务：

```
docker-compose up

```

这个命令会根据 `docker-compose.yml` 文件的定义来启动 Flask 应用和数据库服务。

**步骤 5**: 访问 Flask 应用

现在，你可以通过访问 `http://localhost:5000` 来测试 Flask 应用。它应该能正常响应，尽管它目前还未与数据库交互。

通过这个案例，你学会了如何使用 Docker Compose 来管理包含多个服务的应用。Docker Compose 不仅简化了容器和网络的管理，还使得整个部署过程更加清晰和一致。这对于开发和测试复杂的多容器应用非常有用。

通过这些案例，你将了解 Docker 容器网络的配置和管理，掌握如何在容器化环境中有效地实现服务间的通信。无论是简单的单容器应用还是复杂的多容器部署，合理的网络配置都是保证容器正常工作的关键。
