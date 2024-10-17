
--- 
title:  【腾讯云 Cloud Studio 实战训练营】Claude GPT+Cloud Studio快速完成Excel工资自动核算 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li>- - - - - - - - 


## 一、Cloud Studio介绍

### 1. Cloud Studio是什么？

Cloud Studio是一款在线的集成开发环境（IDE），旨在提供一个集中的平台，使开发人员能够在云端进行软件开发。它具有丰富的功能和工具，可以支持多种编程语言和框架，包括Java、Python、JavaScript等。Cloud Studio提供了代码编辑器、调试器、版本控制、自动化构建等功能，使开发人员可以方便地编写、测试和部署他们的应用程序。此外，Cloud Studio还支持与其他开发者的协作，可以轻松地共享代码和项目，并进行实时的协同编辑。总之，Cloud Studio是一个强大的云端开发工具，可以提高开发效率，简化开发流程，并促进团队协作。

### 2. 登录注册

（1）打开Cloud Studio官网，点击注册：

<img src="https://img-blog.csdnimg.cn/42dd13758fc14a65a2abaab42fd9622f.png" alt="在这里插入图片描述">

（2）注册完成后出现这个界面说明登录成功： <img src="https://img-blog.csdnimg.cn/b2064a160ec54547be26074e1483c5fd.png" alt="在这里插入图片描述">

## 二、GPT工具 Claude 介绍

<img src="https://img-blog.csdnimg.cn/681a0bbc306e416498bd00b0d1a89717.png" alt="在这里插入图片描述">

### 1. 背景介绍

是由Anthropic创建的（Anthropic是一家由对公司不满意的前 OpenAI 工程师创立的初创公司），它的功能尚未像 GPT 那样全面，但无需搜索网络即可响应。它的优势包括消化、总结财务文件和研究论文。Claude 得到了 Google、Zoom 和 Slack 的支持。

Claude 是Anthropic的人工智能助手，可通过聊天界面或 API 访问。它能够进行对话和文本处理。用例包括摘要、搜索、创意和协作写作、制定问答和一些基本编码。由前 OpenAI 员工开发，它的研究起点也是GPT-3，相同的团队背景、技术线路和应用方向。现在用户可以通过Quora的Poe应用程序以及其他两个聊天机器人访问 Claude。

它可以快速响应客户服务请求，并可以在需要时将任务交给人工。Claude特别擅长编辑、重写、总结、分类和提取结构化数据。它还可以遵循基本指令和逻辑场景，根据年度报告分析战略风险和机遇，评估立法的利弊并识别法律文件中的风险。

### 2. 接入方式

Claude的官网在国内虽然不太好访问，但是这个并不影响我们使用它，相信在网上有很多如何接入 Claude 的方法，这里我也介绍一下，前面背景介绍里说过了，Slack 也在支持 Claude，我们只需要在 Slack 插件中加入它即可。关于 Slack 如何去创建一个组织大家可以自行搜索查询，这里我们为了各位实验的便利性，创建了一个临时的 Slack 组织，在手册中点击  即可加入我们临时的 Slack 组织 <img src="https://img-blog.csdnimg.cn/37152b47843245cb94b29ae6a6813aec.png" alt="在这里插入图片描述"> 加入组织后，你们可以看到 Slack 的面板，Claude 应用我们已经添加到组织中了，大家可以随时启用： <img src="https://img-blog.csdnimg.cn/83827f7597cf499298d45ae1e57deb38.png" alt="在这里插入图片描述">

## 三、Excel工资自动核算实战

### 1. 案例介绍

Excel数据表如下： <img src="https://img-blog.csdnimg.cn/a35b53a9eaad4015b681b09562f0717d.png" alt="在这里插入图片描述">

**规则如下**：当前表格中，考勤扣除金额、个税扣除、实发工资目前是空缺的，最终生成的数据需要将上述三列的数据分别根据以下规则填充。

**1、迟到次数核算方法：**
- 3次以内不扣除- 3次以上每多1次扣除100（也就是第4次开始）
**2、个税扣除核算方法：**

个税扣除 = 基础工资 - 五险一金扣除 - 考勤扣除金额，然后进行以下方式核算：
- 不考虑个税起征点。- 收入中不超过3000元的按3%税率缴纳个税。- 3000元-12000元的按10%税率缴纳个税。- 超过12000元不高于25000元的按税率20%计算。- 25000元-35000元的按税率25%计算。- 35000元-55000元的按税率30%计算。- 55000元-80000元的按税率35%计算。
**3、将算出的结果填充到salary.xlsx表中**
- 考前扣除金额填充至原文件中。- 个税扣除填充至原文件中。- 实发工资填充至原文件中。
**4、新建一个文件将表格中的数据在Cloud Studio终端中输出**

### 2. 创建项目

（1）Excel工资自动核算用Python更加方便，这里先创建Python项目环境： <img src="https://img-blog.csdnimg.cn/91b27b52f1094eadb2089b16cb7bc149.png" alt="在这里插入图片描述">

（2）这里可以实名认证领取免费时长： <img src="https://img-blog.csdnimg.cn/e4207cd317e54b8da2568caffa25ba32.png" alt="在这里插入图片描述">

（3）点击创建后一分钟左右Python环境就给我们创建好了： <img src="https://img-blog.csdnimg.cn/33997617458149f19d11c34f0f407065.png" alt="在这里插入图片描述"> （4）启动成功后进入了下面的界面： <img src="https://img-blog.csdnimg.cn/37835ad6404f4830aaa209d0a5c7e9a5.png" alt="在这里插入图片描述"> （5）查看一下Python的版本，可以看到这里是Python3.11没有问题：

```
python -v

```

<img src="https://img-blog.csdnimg.cn/30d91dd368694b27b5c772e2e0d35cbb.png" alt="在这里插入图片描述"> （6）安装需要的Python模块：

```
pip install pandas
pip install openpyxl


```

<img src="https://img-blog.csdnimg.cn/26b0f85c5e5d4e399dea4c45ef1c6384.png" alt="在这里插入图片描述">

（7）右击找到新建文件： <img src="https://img-blog.csdnimg.cn/fd1e5c6d45d14457a8cc8b02fcd79d54.png" alt="在这里插入图片描述">

（8）新建一个Python文件，取名为`test.py：` <img src="https://img-blog.csdnimg.cn/24d0f66918e4448d8ce6610a6ff2978c.png" alt="在这里插入图片描述">

### 3. 上传数据

（1）点击下载测试数据：

<img src="https://img-blog.csdnimg.cn/25a9069d07184347a3b9e59287926f66.png" alt="在这里插入图片描述">

（2）下载完毕后，我们将它上传至Cloud Studio的 Python环境的根目录中去，右击空白处找到上传：

<img src="https://img-blog.csdnimg.cn/4278be496598440aa53ac847539541c7.png" alt="在这里插入图片描述">

（3）选择我们下载的Excel文件，点击打开： <img src="https://img-blog.csdnimg.cn/87d736e7e3414933a6b58e7151107163.png" alt="在这里插入图片描述">

（4）上传成功： <img src="https://img-blog.csdnimg.cn/e7036385c1934af293d1d283e50211a7.png" alt="在这里插入图片描述">

### 4. 开始使用GPT辅助编程

（1）读文件，并将数据存储至Excel中，最后打印输出： <img src="https://img-blog.csdnimg.cn/a59df878d4594f96a766d4fe971f6cbb.png" alt="在这里插入图片描述">

（2）将完整代码复制进test.py文件运行：

```
import pandas as pd
df = pd.read_excel('salary.xlsx')

# 考勤扣除金额计算
df['考勤扣除金额'] = (df['迟到次数'] - 3).clip(lower=0) * 100

# 个税扣除金额计算
df['个税扣除'] = 0
taxable_income = df['工资基数'] - df['五险一金扣除'] - df['考勤扣除金额']
df.loc[taxable_income &lt;= 3000, '个税扣除'] = taxable_income * 0.03
df.loc[(taxable_income &gt; 3000) &amp; (taxable_income &lt;= 12000), '个税扣除'] = taxable_income * 0.1
df.loc[(taxable_income &gt; 12000) &amp; (taxable_income &lt;= 25000), '个税扣除'] = taxable_income * 0.2
df.loc[(taxable_income &gt; 25000) &amp; (taxable_income &lt;= 35000), '个税扣除'] = taxable_income * 0.25
df.loc[(taxable_income &gt; 35000) &amp; (taxable_income &lt;= 55000), '个税扣除'] = taxable_income * 0.3
df.loc[(taxable_income &gt; 55000) &amp; (taxable_income &lt;= 80000), '个税扣除'] = taxable_income * 0.35
df.loc[taxable_income &gt; 80000, '个税扣除'] = taxable_income * 0.45

# 实发工资计算 
df['实发工资'] = df['工资基数'] - df['五险一金扣除'] - df['考勤扣除金额'] - df['个税扣除']

print(df)

# 将计算结果写入Excel
df.to_excel('salary_output.xlsx', index=False)

print('计算结果已写入Excel表格salary_output.xlsx') 

```

<img src="https://img-blog.csdnimg.cn/4b0b0a67c30a423eb6cb8d5605cce03b.png" alt="在这里插入图片描述">

（3）运行结果生成新的Excel表格： <img src="https://img-blog.csdnimg.cn/e006e05e4d9c436d8d48db96cfd4f1c9.png" alt="在这里插入图片描述">

### 5. 停止空间

直接关闭浏览器窗口，是无法关闭我们的空间状态的，所以需要到模版中**“停止空间”**

再次进入官网： <img src="https://img-blog.csdnimg.cn/1969b85967c549e38a797178d0fd6dde.png" alt="在这里插入图片描述">

## 四、总结

在腾讯云 Cloud Studio 实战训练营中，我学习了如何利用Claude GPT和Cloud Studio快速完成Excel工资自动核算。通过这个训练营，我深入了解了如何利用人工智能技术来简化繁琐的工作流程。

首先，Claude GPT是一种强大的自然语言处理模型，能够理解并生成人类语言。在这个训练营中，我们学习了如何使用Claude GPT来解析和理解Excel表格中的工资数据。通过编写简单的代码，我们能够让Claude GPT自动提取工资数据并进行计算，大大提高了工作效率。

而Cloud Studio作为一个云端开发环境，为我们提供了强大的计算资源和便捷的开发工具。在这个训练营中，我们学习了如何在Cloud Studio中搭建和运行我们的代码。通过Cloud Studio，我们可以轻松地管理和处理大量的Excel文件，实现自动化的工资核算。

总的来说，腾讯云 Cloud Studio 实战训练营为我提供了一个全面的学习和实践平台，让我学会了如何利用Claude GPT和Cloud Studio快速完成Excel工资自动核算。这个训练营不仅提升了我的技术能力，还让我在日常工作中更加高效地处理和管理数据。我非常感谢这个训练营给予我的宝贵经验和知识，我相信这将对我的职业发展产生积极的影响。
