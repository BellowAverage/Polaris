
--- 
title:  jenkins与django的持续集成 
tags: []
categories: [] 

---
### 背景

持续集成是敏捷开发的一项重要环节，传统的集成方式较为繁琐，需要利用一些CI/CD工具进行集成工作。笔者尝试采用jenkins进行django项目的集成部署。

### jenkins安装与配置

#### 安装

jenkins的安装比较简单，分为两步安装java运行环境和jenkins软件即可。另外，官网还推荐使用docker进行安装。笔者在ubuntu系统上采用传统方式进行后续的流程。安装步骤为：
- 安装java `apt install openjdk-8-jre`- 安装Jenkins
```
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ &gt; /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins

```

#### 配置

##### 端口

首次安装jenkins可能会出现无法启动的情况，其中一个原因可是能系统的8080端口被占用，我们需要修改`/etc/default/jenkins`的`HTTP_PORT=8080`为其他空闲端口即可。之后重启服务`service jenkins restart`

##### 账户权限

jenkins会为安装jenkins软件的linux系统生成一个jenkins账户进行后续操作。但是笔者想采用超级管理员权限进行后续的操作。
- 将jenkins账户加到root分组中，`gpasswd -a root jenkins`- 修改配置文件`/etc/default/jenkins`
```
JENKINS_USER=root
JENKINS_GROUP=root

```
- 重启服务`service jenkins restart`
##### 插件

笔者试用了blue ocean的插件，看起来比较美观。我们仅需要到系统管理-&gt;插件配置进行添加即可。 <img src="https://img-blog.csdnimg.cn/20190414173219624.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

#### 创建持续集成项目

项目创建有多种方案，最常用的是任意风格和流水线。笔者先介绍默认任意风格的方案，pipeline方案日后补上。

##### 任意风格

<img src="https://img-blog.csdnimg.cn/20190414163838291.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

###### 项目配置

一个简单django集成部署的步骤，需要包含：
- 从代码仓库(git/github等)拉取代码- 指定python运行环境- 创建或激活虚拟环境- 安装依赖- 数据库迁移- 静态文件收集- 配置环境变量- 杀死旧程序- 启动新程序
其中从代码仓库拉取代码可以利用配置完成： <img src="https://img-blog.csdnimg.cn/20190414172823935.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 剩余步骤，我们可以编写一个shell去完成这一系列的步骤：

```
# !/bin/bash
cd project_path

PROCESS=`ps -e | grep gunicorn | awk '{printf "%d\n", $1}'`
for i in $PROCESS
do
    echo "Kill the gunicorn process [ $i ]"
    kill -9 $i
done

CPROCESS=`ps -e | grep celery | awk '{printf "%d\n", $1}'`
for i in $CPROCESS
do
    echo "Kill the celery process [ $i ]"
    kill -9 $i
done

echo "finish kill"

~/.pyenv/bin/pyenv local 3.7.2
pipenv --python 3.7.2

export BUILD_ID=dontKillMe
. `pipenv --venv`/bin/activate
pip install -r requirements.txt
pip install gunicorn==19.9.0

python manage.py collectstatic --noinput
python manage.py migrate

nohup gunicorn -w 3 -b localhost:9003 imageprocessing.wsgi:application &gt; django.out 2&gt;&amp;1 &amp;

sleep 10s

nohup celery -A imageprocessing worker -l info -P eventlet -c 1 &gt; celery.out 2&gt;&amp;1 &amp;

sleep 10s

exit 0

```

其中有几个比较需要注意的点是：
- 笔者的python环境管理采用pyenv进行管理，但是在jenkins的脚本中，不知道出于什么原因直接调用pyenv是会报command not found的，需要指定绝对路径`~/.pyenv/bin/pyenv`才行。- 另外，jenkins当脚本完成之后会杀死所有的后台进程，所以直接使用nohup挂进程的话是没有效果的，需要在脚本中声明一个环境变量`export BUILD_ID=dontKillMe`才可以达到目的。 <img src="https://img-blog.csdnimg.cn/20190414173002569.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 保存过后点击执行即可。
如果安装了blue ocean最终的效果： <img src="https://img-blog.csdnimg.cn/20190414173336459.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/201904141735530.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
