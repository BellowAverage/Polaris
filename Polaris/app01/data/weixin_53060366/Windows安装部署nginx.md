
--- 
title:  Windows安装部署nginx 
tags: []
categories: [] 

---
## Windows安装部署nginx

### 1、官网下载安装包：

官网地址：

<img src="https://img-blog.csdnimg.cn/f54a100c5b4f461eb0fd92421db44a8d.png#pic_center" alt="在这里插入图片描述">

下载好后，解压即可：

<img src="https://img-blog.csdnimg.cn/6adacead688040cfa1f79fc0081c7f2e.png#pic_center" alt="在这里插入图片描述">

### 2、启动nginx：

启动nginx时，运行cmd，使用命令进行操作；不要直接双击nginx.exe，不要直接双击nginx.exe，不要直接双击nginx.exe。

打开命令提示符，用管理员运行。

<img src="https://img-blog.csdnimg.cn/92fcba388e484fa6ac62d3e16108ac26.png#pic_center" alt="在这里插入图片描述">

也可以nginx根目录下直接输：cmd

<img src="https://img-blog.csdnimg.cn/5a8fc88900a141e1a0d0de031d7f0746.png#pic_center" alt="在这里插入图片描述">
- 启动nginx：start nginx.exe- 停止nginx：nginx.exe -s stop- 重载nginx配置：nginx.exe -s reload- 检测配置文件：nginx.exe -t -c conf/nginx.conf- 查看nginx版本：nginx.exe -V
如果不想输命令的话，也可以使用下面的启动脚本：

### 3、nginx启动脚本：

1）启动nginx：

```
chcp 65001
@echo off
d:
cd D:\nginx\nginx-1.22.1\
start nginx.exe
echo 启动成功......
exit

```

2）停止nginx：

```
chcp 65001
@echo off
d:
cd D:\nginx\nginx-1.22.1\
nginx.exe -s stop
echo 已停止nginx.....
exit

```

如果需要全部的功能脚本，请跳转至文末。

启动直接双击 start.bat即可：

<img src="https://img-blog.csdnimg.cn/ba617b825bcb4edebf8db1bf0b5809d8.png#pic_center" alt="在这里插入图片描述">

### 4、设置开机自启：

#### 1）下载WinSW工具：



<img src="https://img-blog.csdnimg.cn/eb27ac11e8c445cfaadc88777e8062f7.png#pic_center" alt="在这里插入图片描述">

根据不同的系统架构，下载不同的版本。

#### 2）安装工具：
- 下载后将该工具放入Nginx的安装目录下，并且将其重命名为 nginx-service.exe- 在nginx安装目录下新建服务日志文件夹server-logs文件夹，用来存放nginx服务相关日志。- 在该目录下新建 nginx-service.xml 文件，写入配置信息，配置好了之后就可以通过这个将Nginx注册为Windows服务了。
<img src="https://img-blog.csdnimg.cn/447c49b0540c479987a90d4ea5094b77.png#pic_center" alt="在这里插入图片描述">

nginx-service.xml的内容如下：

```
&lt;!-- nginx-service.xml --&gt;
&lt;service&gt;
    &lt;id&gt;nginx&lt;/id&gt;
    &lt;name&gt;nginx&lt;/name&gt;
    &lt;description&gt;nginx&lt;/description&gt;
    &lt;logpath&gt;D:\nginx\nginx-1.22.1\server-logs\&lt;/logpath&gt;
    &lt;logmode&gt;roll&lt;/logmode&gt;
    &lt;depend&gt;&lt;/depend&gt;
    &lt;executable&gt;D:\nginx\nginx-1.22.1\nginx.exe&lt;/executable&gt;
    &lt;stopexecutable&gt;D:\nginx\nginx-1.22.1\nginx.exe -s stop&lt;/stopexecutable&gt;
&lt;/service&gt;

```

#### 3）、编写启用脚本：

```
chcp 65001
@echo off
d:
cd D:\nginx\nginx-1.22.1\
nginx-service.exe install
echo 开机自启动设置成功。
exit

```

需要开机自启时，只需要双击 nginx-enable.bat 即可：

<img src="https://img-blog.csdnimg.cn/5a2094e8867c4126bdeddb21fbb8e9b0.png#pic_center" alt="在这里插入图片描述">

查看是否成功将其注册为Windows服务。

<img src="https://img-blog.csdnimg.cn/7c10679645ac40ff887bc7ea3b03fa39.png#pic_center" alt="在这里插入图片描述">

>  
 其他命令： 注册系统服务命令 nginx-service.exe install 删除已注册的系统服务命令 nginx-service.exe uninstall 停止对应的系统服务命令 nginx-service.exe stop 启动对应的系统服务命令 nginx-service.exe start 


### 5、解决 Windows 中 BAT 脚本中文乱码问题：
-  使用 UTF-8 编码：将 BAT 脚本保存为 UTF-8 编码格式，然后在命令行窗口中运行该脚本。 -  设置代码页：在 BAT 脚本开头添加代码页设置命令，例如：chcp 65001，其中 65001 是 UTF-8 的代码页。 -  使用第三方工具：使用第三方工具如 Notepad++ 等编辑器打开 BAT 脚本，在其中添加中文输出，然后保存为 UTF-8 编码格式并运行。 