
--- 
title:  VSCode中设置Python语言自动格式化的方案 
tags: []
categories: [] 

---
**目录**

























## 安装Python扩展

在VSCode的扩展（Externsions）中使用下面命令检索Python扩展

>  
 @category:debuggers Python 


<img alt="" height="488" src="https://img-blog.csdnimg.cn/575212fd9bda4da49a8cae954d670b30.png" width="442">

 打开一个Python文件，可以在VSCode的右下角看到运行环境。

<img alt="" height="118" src="https://img-blog.csdnimg.cn/70fbead31db24658984b20b9ea61c56f.png" width="413">

## 安装PEP8

```
 python3.10 -m pip install -U autopep8
```

## 安装Flake8

```
python3.10 -m pip install -U flake8
```

 <img alt="" height="248" src="https://img-blog.csdnimg.cn/ba8258ecf6444af9bae70e855f3f4255.png" width="435">

安装完需要重启VSCode

## 修改配置

通过扩展中Python的设置按钮打开扩展的配置页面

<img alt="" height="541" src="https://img-blog.csdnimg.cn/7b999f9a0c10412c972a64340207b49c.png" width="682">

### 开启Flake8

在检索框输入flake8Enabled，注意加一个空格。

<img alt="" height="226" src="https://img-blog.csdnimg.cn/adbc6b9c7de44b0eb21f143cfd58da9d.png" width="757">

勾选以开启flake8。

关于Lint的相关配置如下

<img alt="" height="718" src="https://img-blog.csdnimg.cn/e8a7dd606e574917a64ff5b132f34d50.png" width="378">

## 效果

```
import datetime

def get_tomorrow():
    now_time=datetime.datetime.now()
    tomorrow_time = now_time + datetime.timedelta(days=+1)
    
    return tomorrow_time

if __name__ == '__main__':
    print(get_tomorrow())
```

 我们输入一段代码，可以看到已经有很多提示了。

<img alt="" height="173" src="https://img-blog.csdnimg.cn/79076c57d8c949f7a60377cba541d7e6.png" width="633">

 <img alt="" height="229" src="https://img-blog.csdnimg.cn/78a1f60f6d4c4edd82d1cd1738dc065e.png" width="558">

## 格式化代码

### 批量处理历史代码

安装Format Files扩展

<img alt="" height="215" src="https://img-blog.csdnimg.cn/89c8c6b85db243e48b4e35dc1a4da4d6.png" width="435">

 在需要处理的目录下，右击

<img alt="" height="157" src="https://img-blog.csdnimg.cn/88ada6a0545749458746e8188e071dda.png" width="382">

 <img alt="" height="130" src="https://img-blog.csdnimg.cn/2eebe3fd16f44b8a83aa7d80a4d8ceeb.png" width="631">

 这样历史代码就被格式化了

<img alt="" height="275" src="https://img-blog.csdnimg.cn/f8b4e8a8f0f74aaeb59d287832cfeda1.png" width="508">

### 保存时自动格式化

修改VSCode的配置

<img alt="" height="390" src="https://img-blog.csdnimg.cn/48c32ec14e69496cae366d165c4f0dac.png" width="365">

勾选Format On Save

<img alt="" height="468" src="https://img-blog.csdnimg.cn/5948e179e5414fbc9ddfc8ef36a843a6.png" width="1012">

这样我们在保存代码时，自动会进行格式化操作。

## 定制策略

假如我们希望某种问题不提示，则可以定制Flake8的配置。

比如下图就是忽略了E501错误。

<img alt="" height="434" src="https://img-blog.csdnimg.cn/70b5f87306174aa5a7345044a8c025cf.png" width="1200">

其他各种配置可以见




