
--- 
title:  linux上yum安装Jenkins 
tags: []
categories: [] 

---
## linux上yum安装Jenkins

>  
 你可以在 Red Hat Enterprise Linux、CentOS 和其他基于 Red Hat 的发行版上安装 Jenkins。 


### 1、选择一个LTS（稳定版，长期支持）版本：

```
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

#这里可能会报错：
--2022-07-8 09:44:17--  https://pkg.jenkins.io/redhat-stable/jenkins.repo
正在解析主机 pkg.jenkins.io (pkg.jenkins.io)... 151.101.74.133, 2a04:4e42:1a::645
正在连接 pkg.jenkins.io (pkg.jenkins.io)|151.101.74.133|:443... 已连接。
错误: 无法验证 pkg.jenkins.io 的由 “/C=US/O=Let's Encrypt/CN=R3” 颁发的证书:
  颁发的证书已经过期。
要以不安全的方式连接至 pkg.jenkins.io，使用“--no-check-certificate”。

#解决：yum install -y ca-certificates &amp;&gt;/dev/null

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum install -y epel-release
#为jenkins包添加所需的依赖项
sudo yum install java-11-openjdk
sudo yum install jenkins

```

### 2、启动Jenkins：

```
#开机自启
sudo systemctl enable jenkins
#启动Jenkins
sudo systemctl start jenkins
#检查 Jenkins 服务的状态：
sudo systemctl status jenkins
#关闭Jenkins服务：
sudo systemctl stop jenkins

#查看服务
netstat -anp |grep 8080

```

>  
 如果你安装、开启了防火墙，你需要在防火墙添加Jenkins端口： 


```
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload

```

这里Jenkins默认的端口是8080，如果有端口冲突的话，可以在配置文件中修改端口：

```
vi /etc/syscofig/jenkins
#修改内容如下：
JENKINS_USER="root"   #这里Jenkins默认的用户名是Jenkins，需要的也可以自行更改
JENKINS_PORT="8888"

#修改完端口后，重启Jenkins
sudo systemctl restart jenkins

```

>  
 查看jenkins的配置文件，定义了home、JAVA_CMD、user、port等基础配置，保持默认即可#（cat /etc/sysconfig/jenkins） 


### 3、解锁Jenkins：

>  
 浏览到（或安装时为 Jenkins 配置的任何端口），然后等待**“解锁 Jenkins**”页面出现。`http://localhost:8888` 


<img src="https://img-blog.csdnimg.cn/28bfee53840644f4a431e395827aa5d7.png#pic_center" alt="在这里插入图片描述">

这里的密码是一个加密的形式显示的：

```
#查看管理员密码
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

#如果您使用官方镜像在 Docker 中运行 Jenkins，则可以使用在控制台中打印密码，而无需执行到容器中。
jenkins/jenkinssudo docker exec ${CONTAINER_ID or CONTAINER_NAME} cat /var/jenkins_home/secrets/initialAdminPassword

#破解管理员密码
[root@zhaohuaizhe admin_8837323664593734073]# pwd
/var/lib/jenkins/users/admin_8837323664593734073

[root@zhaohuaizhe admin_8837323664593734073]# cat config.xml
&lt;passwordHash&gt;#jbcrypt:$2a$10$cNCnS.RHqF7.wpQeb25IcevJuZppNAN18JWwKvUv6edClEP1O5Nju&lt;/passwordHash&gt;

```

>  
 在“解锁 Jenkins”页面上，将此密码粘贴到“管理员密码”字段中，然后单击“继续”。 


接下来就可以愉快的使用Jenkins了。😁
