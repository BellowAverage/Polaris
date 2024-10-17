
--- 
title:  Windows 10 上安装 CentOS7（Linux） 系统 
tags: []
categories: [] 

---
开启WSL windows10 上开启 WSL，以管理员身份运行 Powershell，并输入以下命令，稍等片刻，会提示是否立即重启计算机。输入“Y”回车重启系统。

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

```

<img src="https://img-blog.csdnimg.cn/direct/326e0bc4f45b4887bbb8a20b65889858.png" alt="在这里插入图片描述">

## 安装centos7

下载一个可用于 WSL 的 CentOS 镜像

https://github.com/mishamosher/CentOS-WSL/releases/tag/7.9-2009

网络不好的可以下载

https://download.csdn.net/download/qq_44810930/89030459

下载回来的是 zip 文件。解压缩至任意不包含中文字符的目录下

进入其目录，右键单击 CentOS7.exe 文件，以管理员身份运行。

稍等片刻，安装完毕

### 启动

再次右击单击，并以管理员身份运行 CentOS.exe

### 更新 (可选)

```
yum update

```

注意：如果发现不能更新系统，很有可能是没有设置 DNS 导致的域名无法解析。

执行如下命令设置 nameserver

```
cat &gt; /etc/resolv.conf &lt;&lt;EOF
nameserver 8.8.8.8
nameserver 8.8.4.4
EOF

```
