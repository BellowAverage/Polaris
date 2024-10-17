
--- 
title:  【Python】Windows：Python 3.9.2 下载和安装 
tags: []
categories: [] 

---
**目录**









## 一、Python 下载

>  
 官网下载地址： 


<img alt="" height="470" src="https://img-blog.csdnimg.cn/2021022817183575.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="643">

<img alt="" height="399" src="https://img-blog.csdnimg.cn/20210228172125576.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="884">

## 二、Python 安装

（1）找到已经下载好的 exe 安装包，双击运行，如图，有两个注意事项：

>  
 ① 底部先注意勾选上：Add Python 3.9 to PATH 
 ② 点击选择安装方式： 
      【不推荐】默认安装：点击 install now ，则会默认装在 C 盘，不建议使用此种安装方式，因为会占用 C 盘空间，不方便以后查找卸载更新： 
      **【推荐】**自定义安装：点击 customize installation ，然后自己选择要安装的目录路径，示例安装步骤如下： 


<img alt="" height="109" src="https://img-blog.csdnimg.cn/20210228173106603.png" width="786">

<img alt="" height="410" src="https://img-blog.csdnimg.cn/20210228184138608.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="664">

（2）先自定义勾选第 1 页 Optional Features 的可选功能，然后点击 next：

>  
 **Documentation : 文献资料安装【（可选可不选）主要做参考资料】** 
 Installs the Python documentation files ：安装 Python 文档文件 


>  
 **pip ：pip 安装 【（必选）之后安装必要库时会用到】** 
 Installs pip,which can download an install other Python packages ：安装 pip，可以下载并安装其他 Python 软件包 


>  
 **tcl/tk and IDLE 【（可选可不选）开发常用】** 
 Installs tkinter and the IDLE development environment ：安装 tkinter 和 IDLE 开发环境 
 **备注可参考  写的博文：** 


>  
 **Python test suite ：Python 测试套件 【（可选可不选）测试常用】** 
 Installs the standard library test suite ：安装标准库测试套件 


>  
 **Python launcher ：Python 启动器【（必选）常用】** 
 **for all user (require elevation) ：对于所有用户（需要提升） 【（可选可不选）对于本机上所有用户账号登录后的配置】** 
 Installs the global 'py' launcher to make it easier to start Python ：安装全局的 'py' 启动器以更轻松地启动 Python 


<img alt="" height="406" src="https://img-blog.csdnimg.cn/2021022821300122.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="663">

（3）继续自定义勾选第 2 页 Optional Features 的可选功能，再点击 Browse，选择自己想安装的目录位置，点击 install：

>  
 **Install for all users ：为所有用户安装 【（可选可不选）对于本机上所有用户账号登录后的配置】** 


>  
 **Associate files with Python require the py launcher ：将文件与 Python 关联需要 py 启动器 【（必选）】** 


>  
 **Create shortcuts for Installed application ：为已安装的应用程序创建快捷方式【（必选）】** 


>  
 **Add Python to environment variables ：将 Python 添加到环境变量【（必选）】** 


>  
 **Precompile standard library ：预编译标准库****【（可选可不选）为了方便还是选】** 


>  
 **Download debugging symbol ：下载调试符号****【（可选可不选）为了方便还是选】** 


>  
 **Download debug binaries(require VS 2017 or later) ：下载调试二进制文件（需要VS 2017或更高版本）【（可选可不选）为了方便还是选】** 


<img alt="" height="415" src="https://img-blog.csdnimg.cn/20210228213423492.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="1037">

<img alt="" height="410" src="https://img-blog.csdnimg.cn/20210228213511545.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="668">

（4）等待安装成功后，点击 Close 关闭弹框：

<img alt="" height="408" src="https://img-blog.csdnimg.cn/2021022821365099.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="665">

<img alt="" height="406" src="https://img-blog.csdnimg.cn/20210228214442495.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="665">

## 三、Python 配置

>  
 **检查安装时是否成功配置了系统环境变量 “path” ，新增 2 个路径如下：** 
 ① Python 的安装路径 
 ② Python 的 Scripts 目录路径 【这是为了使用 Python 默认的 pip 工具】 


<img alt="" height="717" src="https://img-blog.csdnimg.cn/20210228214635831.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="393">

<img alt="" height="592" src="https://img-blog.csdnimg.cn/20210228214736633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="477">

<img alt="" height="655" src="https://img-blog.csdnimg.cn/20210228214847119.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="618">

<img alt="" height="560" src="https://img-blog.csdnimg.cn/20210228215210363.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="528">

<img alt="" height="656" src="https://img-blog.csdnimg.cn/20210228215237321.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="613">

<img alt="" height="588" src="https://img-blog.csdnimg.cn/20210228215434830.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="469">

## 四、Python 验证

>  
 打开 cmd，输入版本命令，然后输入语言测试输出；回车，可以看到版本号和输出成功，则安装成功。 
 **注意：3.* 之后的版本和 3.* 之前的版本语法略有不同。** 


（1）检查 python 的安装版本号，示例校验安装成功如下：

```
python -V
```

 <img alt="" height="191" src="https://img-blog.csdnimg.cn/20210228220346635.png" width="443">

（2）3.* 之前的版本语法：

```
python
print "hello world"
```

>  
 **3.* 之后的版本，输入错误语法命令，会出现以下报错： ** 


<img alt="" height="293" src="https://img-blog.csdnimg.cn/20210228215858517.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="796">

（3）3.* 之后的版本语法：

```
python
print ('hello world')
```

>  
 **3.* 之后的版本，输入正确语法，安装成功输出如下：** 


<img alt="" height="306" src="https://img-blog.csdnimg.cn/20210228220500647.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NzIwMjQ5,size_16,color_FFFFFF,t_70" width="679">
