
--- 
title:  【Python】基于Python的电话簿（Phonebook project）设计【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Python phonebook project design【基于Python的电话簿（Phonebook project）设计（代码详解）】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - - <ul><li>- - - - - - - -  
  </li></ul> 
  
  


## 一. 原文要求

The Phonebook project is a classic business case study in miniature. You are given a skeleton program to complete and must use all of the code given to ensure that you shall demonstrate a clear understanding of Unit 3’s lessons by completing it. In this version of a command line interface (text based) program you shall be handling five lists in parallel. The application simulates keeping a digital address book consisting of a person’s name, address, postal code and phone number.

Your Programmer’s Journal is a vital tool of communicating your knowledge and understanding of the programming process. Each day you should carefully mark down what you accomplished and learned while coding the project. Include the date of each entry, resources you used while exploring the solution, and problems you encountered.

**Ministry Expectations** o Demonstrate the ability to use different data types o Use proper code maintenance techniques o Use a variety of problem-solving strategies o Design algorithms according to specifications o Apply a software development life-cycle model (design-code-test-repeat) o Demonstrate an understanding of the software development process

**Steps**
1. Run the code attached to this project: Unit3_PhoneBook.py1. Understand the given skeleton program and how it works1. Plan your changes to the existing code – set milestones1. Generate flow-charts or pseudocode of your changes (add to your journal)1. Use step-wise-refinement to test your code at each milestone (comment in your journal)1. Update your programmer’s journal at every stage **1. Complete the Phonebook project as a complete working project including text file IO.1. Ensure that existing code is preserved as much as possible1. Comment all internal blocks of code as required (replacing teacher comments where needed)1. Submit your project file, the program’s contact.txt file and programmer’s journal.
<img src="https://img-blog.csdnimg.cn/c5d4ee68b3c24859af8801f8145ee593.png" alt="在这里插入图片描述">

## 二. 中文翻译

电话簿项目是一个微型的经典商业案例研究。你会得到一个需要完成的骨架程序，并且必须使用所有给定的代码，以确保你通过完成它来清晰地展示对第三单元课程内容的理解。在这个基于文本的命令行界面程序版本中，你将同时处理五个列表。该应用模拟了一个包含人的姓名、地址、邮政编码和电话号码的数字地址簿。

你的程序员日志是一个传达你对编程过程知识和理解的重要工具。每天，你应该仔细记录在编码项目过程中完成和学到了什么。包括每个条目的日期、在探索解决方案时使用的资源，以及遇到的问题。

**预期** o 展示使用不同数据类型的能力 o 使用正确的代码维护技巧 o 使用多种解决问题的策略 o 根据规格设计算法 o 应用软件开发生命周期模型（设计-代码-测试-重复） o 展示对软件开发过程的理解

**步骤**
1. 运行附加到这个项目的代码：Unit3_PhoneBook.py1. 理解给定的骨架程序以及其工作原理1. 计划对现有代码的更改 – 设置里程碑1. 生成你的更改的流程图或伪代码（添加到你的日志中）1. 使用分步细化来在每个里程碑处测试你的代码（在你的日志中添加注释）1. 在每个阶段更新你的程序员日志**1. 完成电话簿项目作为一个包括文本文件IO的完整工作项目1. 尽量保留现有代码1. 根据需要注释所有内部代码块（替换教师的注释）1. 提交你的项目文件、程序的contact.txt文件和程序员日志。
## 三、代码详解

### 1. 帮助功能

**获取帮助**：如果不清楚怎么使用，可以输入 `h`、`H` 或 `help` 来获取可用命令的列表。 <img src="https://img-blog.csdnimg.cn/da2750942b6b45fdbf99e1b817eb2b8a.png" alt="在这里插入图片描述">

### 2. 添加联系人

**添加新联系人**：输入 `newContact John Doe 1234567890 Address 12345`（用空格分隔开各个字段）来添加一个新的联系人。 **列出所有联系人**：输入 `listAll`，程序会显示所有联系人的信息。

<img src="https://img-blog.csdnimg.cn/61e2a8a3ae554f9488784e040bf49a06.png" alt="在这里插入图片描述">

### 3. 查找联系人

**查找联系人**：输入 `findContact John first` 来根据名字查找联系人。同样，也可以用 `last`, `phone`, `postal` 来指定不同的查找字段。

<img src="https://img-blog.csdnimg.cn/07950760b2ba45baba1e60cf48e46006.png" alt="在这里插入图片描述">

### 4. 修改联系人

**更新联系人信息**：输入 `updateContact John Doe`，程序会提示你输入新的信息以更新该联系人。

<img src="https://img-blog.csdnimg.cn/63184702855f4c74af4797741116d907.png" alt="在这里插入图片描述">

### 5. 显示联系人

**按姓氏首字母列出联系人**：输入 `listContacts A`（其中 `A` 是姓氏的首字母），程序会列出所有姓氏以 `A` 开头的联系人。

<img src="https://img-blog.csdnimg.cn/c7a082a895b54ad381a8ccbd4716203a.png" alt="在这里插入图片描述">

### 6. 删除联系人

**删除联系人**：输入 `deleteContact John Doe`（用空格分隔开姓和名）来删除一个联系人。

<img src="https://img-blog.csdnimg.cn/15fcfcf6063f4302ab148fe1a62ed6cc.png" alt="在这里插入图片描述">

### 7. 退出

<img src="https://img-blog.csdnimg.cn/99df14ee090d4749a2b708d6df5bcc3e.png" alt="在这里插入图片描述">

### 四、部分代码

部分代码如下：

<img src="https://img-blog.csdnimg.cn/e6c13ff6c57142e0989254e208959af0.png" alt="在这里插入图片描述">

### 👇👇👇关注公众号，回复 “Python电话簿” 获取源码👇👇👇
