
--- 
title:  成功解决Server responded “algorithms negotiation failed. “Key exchange with the remote host failed. This 
tags: []
categories: [] 

---
成功解决Server responded "algorithms negotiation failed. "Key exchange with the remote host failed. This can happen for example if the remote host computer does not support the selected algorithms.





**目录**





















## **解决问题**

Server responded "algorithms negotiation failed. "Key exchange with the remote host failed. This can happen for example if the remote host computer does not support the selected algorithms.



## **解决思路**

这个错误信息表明，在尝试建立SSH连接时，密钥交换阶段出现了问题。通常，这种问题是由于远程主机和本地主机之间支持的加密算法不匹配或协商失败引起的。



## **解决方法**

这个错误信息表明，在尝试建立SSH连接时，密钥交换阶段出现了问题。通常，这种问题是由于远程主机和本地主机之间支持的加密算法不匹配或协商失败引起的。以下是一些可能的解决方法：



### **<strong><strong>T1、更改SSH算法设置：**</strong></strong>

在本地SSH客户端（例如OpenSSH）的配置文件中，尝试明确指定支持的算法。您可以编辑 sshd_config 文件，以确保服务器端支持您所需的算法，或者编辑 ssh_config 文件以确保客户端选择适当的算法。

例如，您可以在SSH客户端的配置文件中指定强制使用较旧的算法，如下所示：

Host your_remote_host

  KexAlgorithms +diffie-hellman-group1-sha1

  Ciphers +aes128-cbc

请注意，这可能会牺牲安全性，因此仅在必要时使用。



### **<strong><strong>T2、更新SSH软件：**</strong></strong>

确保您的SSH客户端和服务器端都是最新版本。有时，问题可能会在旧版本的软件中出现，而新版本可能已解决了这些问题。

联系远程主机管理员：

如果您没有控制远程主机的配置，可以尝试联系远程主机的管理员，让他们检查并修复算法协商问题。



### **<strong><strong>T3、尝试不同的SSH客户端：**</strong></strong>

如果使用的是一个SSH客户端，尝试使用另一个不同的SSH客户端（例如PuTTY）来连接到远程主机，以查看是否有不同的结果。





### **<strong><strong>T4、检查防火墙和网络问题：**</strong></strong>

有时，防火墙或网络问题可能导致密钥交换失败。确保网络连接正常，没有防火墙规则干扰了SSH连接。










