
--- 
title:  YYDS！一行Python代码即可实现数据可视化大屏 
tags: []
categories: [] 

---
今天分享一个 Python 可视化大屏项目，GitHub 地址：`https://github.com/TurboWay/big_screen`，项目结构简单使用方便，直接传数据就可以实现数据可视化大屏。

### 安装

项目依赖第三方模块 `flask`，因此我们需要先进行依赖安装，安装命令：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask`。

### 运行

首先，我们从 GitHub 上将项目下载到本地，当然也可以在公众号`Python小二`后台回复`big_screen`直接获取。

项目下载好后，我们进入项目根路径，如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/65360f9512791ed488e3d792eb978534.png" alt="65360f9512791ed488e3d792eb978534.png">

然后，按住`Shift`点`鼠标右键`，接着选择`在此处打开命令窗口(W)`，命令窗口打开后输入命令：`python app.py`启动项目。

项目启动之后，我们直接在浏览器输入地址即可访问，下面看一下示例。

大数据可视化展板通用模板：`http://127.0.0.1:5000`，如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/f5cf8b47eea08ce0bf15ef972182fb3a.png" alt="f5cf8b47eea08ce0bf15ef972182fb3a.png">

4600 万企业数据大屏可视化：`http://127.0.0.1:5000/corp`，如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/c301aa081a613d6517e51092f779e874.png" alt="c301aa081a613d6517e51092f779e874.png">

厦门 10 万招聘数据(2020-09)大屏可视化：`http://127.0.0.1:5000/job`，如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/6ccc27553dbbb6a8476071dd896c55a6.png" alt="6ccc27553dbbb6a8476071dd896c55a6.png">

### 使用
- 编辑 data.py 中的 SourceData 类(或者新增类，新增的话需要编辑 app.py 增加路由，请参考 CorpData/JobData)- 从任何地方读取你的数据，按照 SourceDataDemo 的数据格式，填充到 SourceData 类- 运行 python app.py 查看数据变更后的效果
推荐阅读  点击标题可跳转
- - - - - - - - 