
--- 
title:  Eolink如何解决API测试痛点 
tags: []
categories: [] 

---


#### 文章目录
- - - - <ul><li>- - - - - - - - - - - 


## 前言

>  
 一个搞测试的粉丝最近遇到一些测试的头痛的事情，跑来找我帮忙，本文将分享关于API测试相关痛点和解决方法 


## 一、API测试的痛点
- 1、需求发布前需要对项目进行回归测试，传统测试方式的覆盖面窄、效率低下。- 2、产品需求变动/代码改动后，测试人员无法确定测试范围。- 3、传统测试方式的周期长，无法每天、每小时、24小时随时执行测试，并且依赖于人的专业性，测试效果不可靠。- 4、传统测试团队成员之间缺乏协作，互相不清楚各自编写的测试用例、测试脚本、测试结果等，导致重复劳动。由于所处的立场不同，测试人员与研发人员发生冲突的情况很多。简单举例下，研发人员认为测试人员提出的BUG有问题，不予修复，测试人员则认为研发人员应该修复这个BUG，双方僵持不下，类似的场景非常多
## 二、eolink可以解决什么？

### 2.1 Eolink是什么？

一站式 API 生产力工具：结合 API 设计、文档管理、自动化测试、监控、研发管理和团队协作的一站式 API 生产平台，从个人开发者到跨国企业用户，Eolink帮助全球超过30万开发者和数万家企业更快、更好且更安全地开发和使用 API。测试团队使用 Eolinker API 自动化测试平台日常维护 API 自动化测试用例后，可有效解决上述问题，帮助测试团队提高测试能力和效率。 

### 2.2 Eolink可以解决什么？
1. 后端、前端、测试团队可以同步开始工作，而不需要互相等待;1. 使用基于API的自动Mock、代码自动生成和自动化测试工具,大幅提升开发效率;开发的各个角色都会获得更好的工作体验;1. API可以在不同的项目中重复使用,提高开发效率;1. 新人更容易熟悉项目，方便团队规模的扩大;1. 与外部团队的协作也更加顺畅。 
## 三、环境安装以及实践操作

### 3. 1 下载安装

官网下载地址（免费下载使用）： 

<img src="https://img-blog.csdnimg.cn/a6b925b6a3cb494aba85c21ef3730e18.png" alt="在这里插入图片描述">

### 3.2 创建项目

（1）API管理主界面点击，并输入项目名称：  <img src="https://img-blog.csdnimg.cn/a949e53c5f6a4c8c9be8fb9d9f72eddf.png" alt="在这里插入图片描述"> （2）添加项目负责人： <img src="https://img-blog.csdnimg.cn/b6a91ad73c2440e790b51e6870bf103e.png" alt="在这里插入图片描述">

（3）创建API项目之后，接着创建API接口文档，点击添加API即可：  <img src="https://img-blog.csdnimg.cn/e95b675534ea49f0938a379ddc02822d.png" alt="在这里插入图片描述">  （4）新建接口，主要填写**接口地址，请求方式，请求体，请求参数等信息**：  <img src="https://img-blog.csdnimg.cn/8299069f07d5436ca41de69b94104c0d.png" alt="在这里插入图片描述"> 

## 四、支持所有自动化接口测试场景

### 4.1 单API接口测试

单自动化接口测试用例中，支持执行顺序排序，参数传递，结果判断条件，参数快速加解密等。 

<img src="https://img-blog.csdnimg.cn/d5c199066dad4e71aa7d4673fe76d32f.png" alt="在这里插入图片描述">

设置参数值，点击发送：  <img src="https://img-blog.csdnimg.cn/335ee70d8a17474f9c2ab1a450e6d4d3.png" alt="在这里插入图片描述"> 正常登录情况下拿到token值：  <img src="https://img-blog.csdnimg.cn/1fdf4cd2261b487f9356165c0c0b5837.png" alt="在这里插入图片描述">

### 4.2 API变更智能通知

许多用户在维护API时，经常遇到API文档变更了，但是前端和测试人员却不知道的问题。为了解决这个痛点，API研发管理平台提供了变更通知功能，当API发生变化时通过邮件和站内信自动通知相关成员，并且显示变更的内容: 当API状态变为“开发”时，通知后端开发 当API变为“对接”时，通知前端进行对 当API变为“测试”时，通知测试人员进行测试  <img src="https://img-blog.csdnimg.cn/bb3f3ceb071749a4baca18296259bb12.png" alt="在这里插入图片描述">

### 4.3 API历史版本对比与恢复功能

Eolink还提供了非常强大的API版本管理功能，可以比较版本修改的差异，还可以随时回滚到任意一次APl文档版本。

（1）差异对比功能，修改的地方会显示蓝框：  <img src="https://img-blog.csdnimg.cn/d87d088cf63a46a3a508e97c90e68ffd.png" alt="在这里插入图片描述"> （2）恢复历史版本功能，这个功能10分好评，有了自动备份和回滚任意版本功能，一旦接口有问题可以恢复到指定版本去：

<img src="https://img-blog.csdnimg.cn/678a9ffdbfd94bd68fa53f71811d8529.png" alt="在这里插入图片描述">

### 4.4 API文档评论功能

测试人员与研发人员发生冲突的情况很多，往往是由于沟通不到位导致的，而这个评论功能的所有沟通内容都会跟随版本保留下来，效果的降低了沟通成本和记录成本，这个功能实在太香了 <img src="https://img-blog.csdnimg.cn/4e280e4dd24f4079b20bae16a2d7df62.png" alt="在这里插入图片描述">

### 4.5 API一键批量测试

回归测试是版本系统测试中必经的一个测试阶段。回归测试到底由缺陷提交人员回归自己提交的缺陷呢？还是由其他人回归呢？回归测试到底是仅仅回归缺陷本身，还是围绕缺陷和修正代码展开更多的测试？这里面的测试策略非常多。我觉得我们要结合测试资源、项目实际情况、测试流程和机制等综合决策如何更好的展开回归测试。 eolink支持多自动化接口测试用例批量测试，测试人员可以**一键批量测试**，可以减少很多重复工作。 

<img src="https://img-blog.csdnimg.cn/ea1a08ff3c024a82a5198768f7936c50.png" alt="在这里插入图片描述"> 

### 4.6 用例模板

可以将重复的测试步骤添加到测试模板库中，并且在测试用例中引用测试模板来实现复用测试步骤的目的，大大减少重复工作

（1） 新建模块：  <img src="https://img-blog.csdnimg.cn/a33ebed94c7c415c93bdbbb66cd3ac1e.png" alt="在这里插入图片描述">

（2）填写名字和分组  <img src="https://img-blog.csdnimg.cn/e2208fe78c3044fda461d18900a0b7f9.png" alt="在这里插入图片描述">

（3） 引用模板：  <img src="https://img-blog.csdnimg.cn/57c5a20f11aa4535868b36b83479faf9.png" alt="在这里插入图片描述">  （4） 勾选所需的模板：  <img src="https://img-blog.csdnimg.cn/ebf61de524dd47ccafc39282fb033a07.png" alt="在这里插入图片描述">  （5） 执行测试：  <img src="https://img-blog.csdnimg.cn/78a0631a72cc4ede86af7f0ca56da4f5.png" alt="在这里插入图片描述">  （6） 选择数据集，点击下一步：

<img src="https://img-blog.csdnimg.cn/366ce128a1694d2f8a9eebae649008d1.png" alt="在这里插入图片描述">  （7） 生成测试结果：  <img src="https://img-blog.csdnimg.cn/359b19943b7244c98bffa350eed1d77b.png" alt="在这里插入图片描述">

### 4.7 定时测试任务

API自动化测试可以设置定时任务，实现项目在无人值守的情况下自动测试并且发送报告给相应的邮箱，监控项目监控情况。

（1） 添加定时任务

<img src="https://img-blog.csdnimg.cn/fbdb162b24f64a3c8f038ff0c959331e.png" alt="在这里插入图片描述">  （2）在新页面中设置定时任务的详细情况：  <img src="https://img-blog.csdnimg.cn/3c6d779cc7254487ae3f4595b3eb1dbc.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/1be287e21a514468b2f4d934b08719b4.png" alt="在这里插入图片描述">

### 4.8 查看测试报告

（1） 查看定时测试历史 <img src="https://img-blog.csdnimg.cn/c824e88227b047d783aec1a7eb228a98.png" alt="在这里插入图片描述"> 

（2） 可以查看详情或者下载导出：  <img src="https://img-blog.csdnimg.cn/772d5fe0563543ca8d2889e7d6fa5be0.png" alt="在这里插入图片描述">

## 五、总结

eolink支持所有自动化接口测试场景，无论是单自动化接口测试还是多自动化接口测试用例批量测试，效果解决了传统测试效率低的问题；历史版本对比功能可以有效帮助测试人员确定测试范围；API文档评论功能够及时的沟通和记录，大大降低了测试人员与研发人员发生冲突的情况，提高团队协作沟通能力；
