
--- 
title:  接口测试神器Apifox究竟有多香？ 
tags: []
categories: [] 

---
前言 这篇文章介绍一款协作的工具**Apifox**，官方对Apifox的定位是Apifox = Postman +Swagger + Mack +JMeter。 Apifox的强大之处可想而知。小伙伴们快来体验一下吧 

<img src="https://img-blog.csdnimg.cn/3861001de7f341848ba95a0c1d7fca4f.png" alt="在这里插入图片描述">



#### 接口测试神器Apifox
- - - - - - - - - - - 


## Apifox的功能

Apifox到底有哪些功能,来看看官方对Apifox功能的描述就知道了 <img src="https://img-blog.csdnimg.cn/42abf79355f04ccca20091c6748b3dd7.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/4ab095bdd5ce4a8ea70b07bf7f1b776d.png" alt="在这里插入图片描述">

## Apifox的优势

<mark>1</mark> 避免了代码和文档不同步的问题（自动将swagger同步到文档中） <mark>2</mark> 避免重复劳动（swagger写好后，一键同步，文档、调试、Mock、测试 的数据全部自动生成） <mark>3</mark> 开发效率高（功能很强大。比如：可以在自测时指定全局的token）

## 安装Apifox

访问Apifox的官网  Apifox覆盖的版本相当之全面(Windows、Mac、Linux) <img src="https://img-blog.csdnimg.cn/f40f28db507744ca9e5bdc80d8821bf8.png" alt="在这里插入图片描述"> 这里下载的是Windows64位版本（安装直接一路Next即可,十分方便）

<img src="https://img-blog.csdnimg.cn/40ba7ef106e545ff999cc55a03e3be97.png" alt="在这里插入图片描述"> 下载完登陆进去即可，这里官方考虑到我们第一次接触Apifox，贴心的准备了一个小demo（宠物店） 供我们参考

<img src="https://img-blog.csdnimg.cn/9554bc910c5a49d1b990c1e9b85577be.png" alt="在这里插入图片描述">

## 使用场景

Apifox 是接口管理、开发、测试全流程集成工具，使用受众为整个研发技术团队，主要使用者为前端开发、后端开发和测试人员。 **前端开发** 💬接口文档管理 💬接口数据Mock 💬接口调试 💬前端代码生成 **后端开发** 💬接口文档管理 💬接口数据Mock 💬接口调试 💬后端代码生成 **测试人员** 💬接口调试 💬接口自动化测试

## 智能mock

这里我们来新建一个接口感受一下智能mock的使用

<img src="https://img-blog.csdnimg.cn/8ad6e0befaec4f8da7ab52f2f821c2e2.png" alt="在这里插入图片描述"> 我们发现当写好接口下面的参数就自动生成了，还是很智能的

<img src="https://img-blog.csdnimg.cn/d00f157558b148998c1867fc5654e9da.png" alt="在这里插入图片描述"> 这里我们新建两个返回的字段

<img src="https://img-blog.csdnimg.cn/cfac78581f514278baae56a87ff7b343.png" alt="在这里插入图片描述"> 点击添加示例，这里有个很神奇的事情就是当我们点击自动生成时我们会发现每一次生成的数据都是随机的

<img src="https://img-blog.csdnimg.cn/4b98772f8e84481182981ef9a90035e2.png" alt="在这里插入图片描述"> 然后我们点击保存就会生成以下接口数据

<img src="https://img-blog.csdnimg.cn/a9182f9ee6fe492a83f0589298c6579a.png" alt="在这里插入图片描述"> 当我们把url复制到浏览器打开时，我们会发现神奇的事情又发生了。。。

<img src="https://img-blog.csdnimg.cn/1c1f3d4afa3c45f4892329c0403092f4.png" alt="在这里插入图片描述"> 智能mock很大程度的方便了我们前端的工作，简直就是前端开发者的福音

## 最佳实践

<mark>1</mark> 前端(或后端)在 Apifox 上定好接口文档初稿。 <mark>2</mark> 前后端 一起评审、完善接口文档，定好接口用例。 <mark>3</mark> 前端 使用系统根据接口文档自动生成的 Mock 数据进入开发，无需手写 mock 规则。 <mark>4</mark> 后端 使用接口用例 调试开发中接口，只要所有接口用例调试通过，接口就开发完成了。如开发过中接口有变化，调试的时候就自动更新了文档，零成本的保障了接口维护的及时性。 <mark>5</mark> 后端 每次调试完一个功能就保存为一个接口用例。 <mark>6</mark> 测试人员 直接使用接口用例测试接口。 <mark>7</mark> 所有接口开发完成后，测试人员(也可以是后端)使用集合测试功能进行多接口集成测试，完整测试整个接口调用流程。 <mark>8</mark> 前后端 都开发完，前端从Mock 数据切换到正式数据，联调通常都会非常顺利，因为前后端双方都完全遵守了接口定义的规范。

## 团队协作

Apifox可以和其他小伙伴共同开发项目，这里创建一个项目

<img src="https://img-blog.csdnimg.cn/64f2022c741e4f0490bd6a0bbcfd4aa6.png" alt="在这里插入图片描述"> 创建完毕在这里可以邀请其他成员共同完成项目，可以给他们设置使用权限。

<img src="https://img-blog.csdnimg.cn/b7baef4e8c7f4b47bd4ba24666041793.png" alt="在这里插入图片描述">

## 环境变量

我们可以通过Apifox自定义环境，做到开发环境、测试环境、生成环境区分测试，使我们能够更高效，更方便使用api

<img src="https://img-blog.csdnimg.cn/618d9b471ca84b2ebe68811234759768.png" alt="在这里插入图片描述">

## 项目概览

这里我们使用官方贴心准备的小demo做讲解，直接上图🔥🔥🔥

**接口概览页**

<img src="https://img-blog.csdnimg.cn/151014811cb74b25a47d73888ef3cb7b.png" alt="在这里插入图片描述">

**接口设计界面**

<img src="https://img-blog.csdnimg.cn/d069c9d3e54d45e28e43ee6855adbcb4.png" alt="在这里插入图片描述">

**接口运行界面**

<img src="https://img-blog.csdnimg.cn/313f6d76b70c4beca9053705680928cf.png" alt="在这里插入图片描述">

## 后续功能规划

💬接口性能测试支持(类似JMeter)。 💬支持插件市场，可以自己开发插件。 💬支持更多接口协议，如GraphQL、websocket等。 💬支持离线使用，项目可选择在线同步（团队协作）还是仅本地存储（单机离线使用）

## 写在最后

介绍了这么多Apifox的功能以及使用，你是否心动了呢？ 快点击链接下载使用一番吧 

<img src="https://img-blog.csdnimg.cn/04c7184d3eb4479e869f0dfbc3ebd60d.png" alt="在这里插入图片描述">
