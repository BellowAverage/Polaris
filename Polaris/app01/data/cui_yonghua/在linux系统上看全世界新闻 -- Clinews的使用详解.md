
--- 
title:  在linux系统上看全世界新闻 -- Clinews的使用详解 
tags: []
categories: [] 

---
#### 一. Clinews介绍

Clinews 和 InstantNews 类似，都是 Linux 命令行下的新闻客户端，安装及配置 Clinews 后就可以在 Linux 命令行下阅读新闻及头条新闻了， 当然还有博客新闻，不需要安装 GUI 应用或移动应用，轻松在 Linux 终端中阅读到世界上发生的重大新闻，Clinews 采用 NodeJS 编写，是一款开源的软件。

Clinews 从 News API(newsapi.org) 中检索所有新闻标题。News API 是一个简单易用的 API，它返回当前在一系列新闻源和博客上发布的头条的 JSON 元数据。

它目前提供来自 128 个热门源的实时头条，包括 Ars Technica、BBC、Blooberg、CNN、每日邮报、Engadget、ESPN、金融时报、谷歌新闻、hacker News，IGN、Mashable、国家地理、Reddit r/all、路透社、 Speigel Online、Techcrunch、The Guardian、The Hindu、赫芬顿邮报、纽约时报、The Next Web、华尔街日报，今日美国和等等。

#### 二. Clinews安装

步骤一：由于 Clinews 是使用 NodeJS 编写的，因此你可以使用 NPM 包管理器安装。如果尚未安装 NodeJS，请按照以下链接中的说明进行安装。

安装 node 后，运行以下命令安装 Clinews：`npm i -g clinews`

步骤二：需要 News API 的 API 密钥。进入 https://newsapi.org/register 并注册一个免费帐户来获取 API 密钥。

从 News API 获得 API 密钥后࿰
