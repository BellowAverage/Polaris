
--- 
title:  LLM之FreeAskInternet：FreeAskInternet的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLM之FreeAskInternet：FreeAskInternet的简介、安装和使用方法、案例应用之详细攻略





**目录**



























## **FreeAskInternet****的简介**

2024年4月5日发布，FreeAskInternet 是一个完全免费、私密且在本地运行的搜索聚合器和答案生成器，使用 LLM，无需 GPU。用户可以提出问题，系统将使用 searxng 进行多引擎搜索，并将搜索结果与 ChatGPT3.5 LLM 结合，基于搜索结果生成答案。所有过程均在本地运行，不需要 GPU 或 OpenAI 或 Google API 密钥。

**<strong>GitHub地址**</strong>：







### **<strong><strong>1、特点**</strong></strong>

&gt;&gt; 完全免费（无需任何 API 密钥）&gt;&gt;完全本地（无需 GPU，任何计算机均可运行）&gt;&gt;完全私密（所有事情均在本地运行）&gt;&gt;无需 LLM 硬件运行（无需 GPU！）&gt;&gt;使用免费的 ChatGPT3.5 API（无需 API 密钥！感谢 OpenAI）&gt;&gt;使用 Docker Compose 快速轻松部署&gt;&gt;网页和移动设备友好的界面，可从任何设备轻松访问（感谢 ChatGPT-Next-Web）



### **<strong><strong>2、工作原理**</strong></strong>

系统在 ChatGPT-Next-Web（本地运行）中获取用户输入的问题，并调用 searxng（本地运行）在多个搜索引擎上进行搜索。爬取搜索结果链接内容并传递给 ChatGPT3.5（使用 OpenAI ChatGPT3.5，通过本地运行的 FreeGPT35），请求 ChatGPT3.5 根据这些内容作为参考来回答用户问题。将答案流式传输到 ChatGPT-Next-Web 聊天界面。





### **<strong><strong>3、状态**</strong></strong>

该项目仍处于早期阶段。请期待一些错误。











## **FreeAskInternet****的安装和使用方法**

### **<strong><strong>1、运行最新版本**</strong></strong>

```
git clone https://github.com/nashsu/FreeAskInternet.git
cd ./FreeAskInternet
docker-compose up -d 
```

现在您应该能够在 http://localhost:3000 上打开 Web 界面。默认情况下不暴露任何其他内容。



### **<strong><strong>2、如何更新到最新版本**</strong></strong>

```
cd ./FreeAskInternet
git pull
docker compose rm backend
docker image rm nashsu/free_ask_internet
docker-compose up -d
```







## **FreeAskInternet****的案例应用**

持续更新中……






