
--- 
title:  Visual Studio Code 插件的开发、调试及发布完整详细教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：Vscode的拓展插件，从环境安装到生成项目文件再到调试及部署发布的完整开发教程。 日期：2023年5月10日 vscode 1.78.1 


### 一、准备node环境及安装yo

项目初始化，优先安装yo、再通过yo创建code及插件项目。

#### 基础条件

需要先安装node，且node环境已经正确安装（包括环境变量、npm），且npm为最新版本 执行命令：`npm install -g yo` <img src="https://img-blog.csdnimg.cn/46ccd3bfe7dd4e1492bc8c36f20fd38b.png" alt="在这里插入图片描述">

#### 安装code

说明：必须要通过cmd进行，再vscode中会提示错误。 <img src="https://img-blog.csdnimg.cn/3b99f0ad23a3471480663635b1172f98.png" alt="在这里插入图片描述">

### 二、项目初始化

#### 步骤一、选择语言

<img src="https://img-blog.csdnimg.cn/63060696470048f9adf7e590881a1154.png" alt="在这里插入图片描述"> 操作：上下键选择，enter确认。

#### 步骤二、填写基础插件的信息


