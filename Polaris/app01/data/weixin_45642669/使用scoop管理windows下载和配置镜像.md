
--- 
title:  使用scoop管理windows下载和配置镜像 
tags: []
categories: [] 

---
在powershell执行：

```
# 允许通过shell安装
set-executionpolicy remotesigned -s cu

```

然后：

```
iex (new-object net.webclient).downloadstring('https://gitee.com/glsnames/scoop-installer')

```

如果失效的话，可以直接
- 百度gitee- 搜索scoop- 然后把项目地址http路径写入path。
执行scoop，按照提示即可下载，用过yum的都懂

Q-dir：分屏软件

Python3.7

redis：内存用数据库

git：代码拉取工具

everything：搜索工具

pycharm：

ditto：剪贴板监控软件

corretto8-jdk

winpython：python全家桶

quicklook：预览文件
