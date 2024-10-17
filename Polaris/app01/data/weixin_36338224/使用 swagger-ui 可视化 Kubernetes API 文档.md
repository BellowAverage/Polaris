
--- 
title:  使用 swagger-ui 可视化 Kubernetes API 文档 
tags: []
categories: [] 

---
在工作中，你可能需要基于 Kubernetes 提供的 API 进行开发，比如开发适合自己的控制台，Kubernetes 官方提供的 API 文档，有两个问题：
1. 非常的不直观，这个问题其实还好，自己克服一下也不是大问题1. 只有 K8S api-server 的接口，这个就难办了，假如有新的 CRD 资源，比如 kubevirt ，又要去找 kubevirt 的 api 文档，关键是找不着
今天明哥给大家介绍一个工具，可以帮你解决这个问题。

这个工具叫 swagger-ui，可以把 k8s 暴露的 http 接口文档以 UI 界面呈现给你，你甚至还可以在上面进行调试，生成 curl 的请求命令。

### 1. 如何部署 swagger-ui

打开两个 ssh 连接到你的 K8S 集群中。

进入第一个窗口，执行如下命令建立一个反向代理

```
kubectl proxy --port=8080
```

进入第二个窗口，执行如下命令建立获取 k8s的 api 文档信息，输出到一个 `k8s-swagger.json` 文件中

```
curl localhost:8080/openapi/v2 &gt; k8s-swagger.json
```

获取到后，第一个窗口就可以关闭了。

然后任选一个窗口，执行如下命令运行一个容器

```
docker run \
    --rm \
    -d \
    -p 80:8080 \
    -e SWAGGER_JSON=/k8s-swagger.json \
    -v $(pwd)/k8s-swagger.json:/k8s-swagger.json \
    swaggerapi/swagger-ui
```

### 2. 使用 swagger-ui

此时，你在浏览器上输入 `http://ip` 就可以看到一个经过可视化的 api 文档界面，其中包括安装在集群上的所有自定义资源的模型和路径！

<img src="https://img-blog.csdnimg.cn/20211028075216878.png" alt="">

里面的 api 非常多，你用得上的，用不上的，这里都有。 不仅有 api-server 的 API ，​其他所有你另外安装的 CRD 资源也都有。

比如我自己安装的 VirtualMachineInstance 资源，根据关键字，立马就找到 KubeVirt 创建虚拟机的 API 

<img src="https://img-blog.csdnimg.cn/20211028075217179.png" alt="">

点击上面的 `Try it out` 可以修改请求体的参数，请生成一个 curl 命令，方便你进行调试。

### 絮叨一下

我在 CSDN 上写过很多的 Python 相关文章，其中包括 Python 实用工具，Python 高效技巧，PyCharm 使用技巧，很高兴得到了很多知乎朋友的认可和支持。

在他们的鼓励之下，我将过往文章分门别类整理成三本 PDF 电子书

**PyCharm 中文指南**

《PyCharm 中文指南》使用 300 多张 GIF 动态图的形式，详细讲解了最贴合实际开发的 105个 PyCharm 高效使用技巧，内容通俗易懂，适合所有 Python 开发者。

在线体验地址：

<img src="https://img-blog.csdnimg.cn/20211028075217462.png" alt="">

**Python 黑魔法指南**

《Python黑魔法指南》目前迎来了 v3.0 的版本，囊集了 100 多个开发小技巧，非常适合在闲时进行碎片阅读。

在线体验地址：

<img src="https://img-blog.csdnimg.cn/20211028075217667.png" alt="">

**Python 中文指南**

学 Python 最好的学习资料永远是 Python 官方文档，可惜现在的官方文档大都是英文，虽然有中文的翻译版了，但是进度实在堪忧。为了照顾英文不好的同学，我自己写了一份 面向零基础的朋友 的在线 Python 文档 -- 《Python中文指南》

在线体验地址：

<img src="https://img-blog.csdnimg.cn/20211028075217936.png" alt="">

**有帮助的话，记得帮我**  **点个赞哟~**
