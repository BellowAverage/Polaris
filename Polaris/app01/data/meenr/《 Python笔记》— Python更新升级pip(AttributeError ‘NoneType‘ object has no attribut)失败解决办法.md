
--- 
title:  《 Python笔记》— Python更新升级pip(AttributeError: ‘NoneType‘ object has no attribut)失败解决办法 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - 


### 1 更新命令

pip更新常用命令

```
python -m pip install -U pip
python -m pip install --upgrade pip 

```

### 2 报错信息

升级失败，提示如下信息

```
pip install -U pip==23.0.1 AttributeError: 'NoneType' object has no attribut

```

<img src="https://img-blog.csdnimg.cn/549ae78e27b443d58ec056d7a1f76c57.png" alt="在这里插入图片描述">

### 3 解决办法

使用如下命令更新pip

```
easy_install -U pip

```

<img src="https://img-blog.csdnimg.cn/0ff2c746b05a4edf8bec5bf3a4b62a3b.png" alt="在这里插入图片描述"> 提示如上图信息，成功更新完成
