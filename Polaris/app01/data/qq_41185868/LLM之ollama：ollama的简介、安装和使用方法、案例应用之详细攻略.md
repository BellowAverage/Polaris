
--- 
title:  LLM之ollama：ollama的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLM之ollama：ollama的简介、安装和使用方法、案例应用之详细攻略





**目录**







































































## **ollama****的简介**

ollama是一款可以开始使用本地的大型语言模型。启动并运行大型语言模型。运行Llama 2、Code Llama和其他模型。自定义并创建您自己的模型。

官网：

GitHub地址：







### **<strong><strong>1、模型库**</strong></strong>

Ollama 支持 ollama.com/library 上可用的一系列模型。

注意：运行 7B 模型时，您应至少有 8GB 的可用 RAM，运行 13B 模型时需要 16GB，运行 33B 模型时需要 32GB。

以下是一些可下载的示例模型：









## **ollama****的安装和使用方法**

### **<strong><strong>1、下载**</strong></strong>

#### **<strong><strong>macOS、Windows、Linux**</strong></strong>

macOS：

Windows：

Linux：

curl -fsSL https://ollama.com/install.sh | sh



手动安装说明：





#### **<strong><strong>Docker**</strong></strong>

Ollama 官方 Docker 镜像 ollama/ollama 已在 Docker Hub 上可用。







#### **<strong><strong>相关库**</strong></strong>

ollama-python

ollama-js





### **<strong><strong>2、快速入门**</strong></strong>

要运行并与 Llama 2 聊天：

ollama run llama2





### **<strong><strong>3、自定义模型**</strong></strong>

#### **<strong><strong>从 GGUF 导入**</strong></strong>

Ollama 支持在 Modelfile 中导入 GGUF 模型：

创建一个名为 Modelfile 的文件，其中包含一个 FROM 指令，指向要导入的模型的本地文件路径。

FROM ./vicuna-33b.Q4_0.gguf



在 Ollama 中创建模型

ollama create example -f Modelfile



运行模型

ollama run example



#### **<strong><strong>从 PyTorch 或 Safetensors 导入**</strong></strong>

有关导入模型的指南，请参阅指南。







#### **<strong><strong>自定义提示**</strong></strong>

##### **<strong><strong>可以使用提示来定制 Ollama 库中的模型。例如，要定制 llama2 模型：**</strong></strong>

ollama pull llama2



##### **<strong><strong>创建一个 Modelfile：**</strong></strong>

FROM llama2



# set the temperature to 1 [higher is more creative, lower is more coherent]

PARAMETER temperature 1  将温度设置为 1 [较高为更具创造性，较低为更连贯]



# set the system message设置系统消息

SYSTEM """

You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.

"""

FROM llama2



##### **<strong><strong>接下来，创建并运行模型：**</strong></strong>

ollama create mario -f ./Modelfile

ollama run mario

&gt;&gt;&gt; hi

Hello! It's your friend Mario.

有关更多示例，请参阅示例目录。有关使用 Modelfile 的更多信息，请参阅 Modelfile 文档。





### **<strong><strong>4、CLI 参考**</strong></strong>

#### **<strong><strong>创建模型**</strong></strong>

使用 Modelfile 创建模型的命令是 ollama create。

ollama create mymodel -f ./Modelfile

#### **<strong><strong>拉取模型**</strong></strong>

ollama pull llama2

此命令还可用于更新本地模型。只会拉取差异。



#### **<strong><strong>删除模型**</strong></strong>

ollama rm llama2

#### **<strong><strong>复制模型**</strong></strong>

ollama cp llama2 my-llama2



#### **<strong><strong>多行输入**</strong></strong>

对于多行输入，可以使用"""

&gt;&gt;&gt; """Hello,

... world!

... """

I'm a basic program that prints the famous "Hello, world!" message to the console.



#### **<strong><strong>多模态模型**</strong></strong>

&gt;&gt;&gt; What's in this image? /Users/jmorgan/Desktop/smile.png

The image features a yellow smiley face, which is likely the central focus of the picture.



#### **<strong><strong>将prompt作为参数传递**</strong></strong>

$ ollama run llama2 "Summarize this file: $(cat README.md)"

 Ollama is a lightweight, extensible framework for building and running language models on the local machine. It provides a simple API for creating, running, and managing models, as well as a library of pre-built models that can be easily used in a variety of applications.



#### **<strong><strong>列出计算机上的型号**</strong></strong>

ollama list



#### **<strong><strong>开始Ollama**</strong></strong>

在不运行桌面应用程序的情况下启动Ollama时使用Ollama服务。

ollama serve





### **<strong><strong>5、构建**</strong></strong>

安装 cmake 和 go：

brew install cmake go



然后生成依赖项：

go generate ./...



然后构建二进制文件：

go build .

有关更详细的说明，请参阅开发人员指南



#### **<strong><strong>运行本地构建**</strong></strong>

接下来，启动服务器：

./ollama serve



最后，在另一个 shell 中，运行一个模型：

./ollama run llama2



### **<strong><strong>6、REST API**</strong></strong>

Ollama 具有用于运行和管理模型的 REST API。

#### **<strong><strong>生成响应**</strong></strong>

curl http://localhost:11434/api/generate -d '{<!-- -->

"model": "llama2",

"prompt":"天空为什么是蓝色？"

}'

#### **<strong><strong>与模型聊天**</strong></strong>

curl http://localhost:11434/api/chat -d '{<!-- -->

"model": "mistral",

"messages": [

{ "role": "user", "content": "天空为什么是蓝色？" }

]

}'

有关所有端点的 API 文档，请参阅 API 文档。





## **ollama****的案例应用**

持续更新中……






