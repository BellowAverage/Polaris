
--- 
title:  VMWare Workstation 17 Pro虚拟机加载网卡失败的解决办法 
tags: []
categories: [] 

---
## VMWare Workstation 17 Pro虚拟机加载网卡失败的解决办法

一般来说，安装好了VMWare Workstation 17 Pro, 应该在每次打开虚拟机和客户机操作系统Red Hat Enterprise Linux时没有问题。

>  
 **故障描述**：通常启动Linux客户机操作系统时没出现问题，但是运行SSH远程登录时，突然发现无法连通；同时在Linux客户机操作系统，用ifconfig也找不到网络接口卡与IP地址绑定的信息。** 


现在，让我们一起，分步骤查找和排除上述问题引起的这个故障。

#### 1. 首先，在VMWare Workstation虚拟机上查看虚拟网络适配器信息。

打开虚拟网络编辑器对话框，看到采用NAT模式，绑定的网卡VMNet8的子网IP为192.168.85.0, 子网掩码为255.255.255.0. <img src="https://img-blog.csdnimg.cn/39272b143ce24add8721fb084a631a57.png" alt="在这里插入图片描述"> 点击右侧按钮“NAT设置”，则弹出新的对话框，显示对应的子网网关为192.168.85.2。 <img src="https://img-blog.csdnimg.cn/c97341afd6dc4ef8a2892f699bcb577b.png" alt="在这里插入图片描述"> 这些参数留在后续配置中使用。

#### 2. 接下来，查看VMWare相关的Windows服务是否启动。

打开Windows服务管理器，启动所有跟VMWare相关的服务： <img src="https://img-blog.csdnimg.cn/6b4b8ee404ec4b348be21088e5814db5.png" alt="在这里插入图片描述"> 于是，查看配置文件。按照常规方法，设置虚拟网络适配器，用以下命令编辑配置文件。

```
vi /etc/sysconfig/network-scripts/ifcfg-ens33

```

修改默认的DHCP，为静态地址。将

```
BOOTPROTO=”dchp”

```

修改为：

```
BOOTPROTO=”static”

```

修改（或保持）以下语句：

```
ONBOOT=”yes”

```

之后，添加以下几行到配置文件中去：

```
IPADDR=”192.168.85.222”  (因为虚拟网络适配器默认主机是192.168.85.0)
GATEWAY=”192.168.85.2”  (由虚拟网络适配器默认定义)
NETMASK=”255.255.255.0” （子网掩码，通用默认值）
DNS=”61.129.66.79”       (中国电信上海DNS服务器之一)

```

编辑完配置文件，按ESC退出，同时以：wq保存并退出该配置文件。 此时，再用cat命令查看以下刚才编辑的配置文件，如下图：

<img src="https://img-blog.csdnimg.cn/30ea411827af40e8b44e77b11095c353.png" alt="在这里插入图片描述">

#### 3. 其次，依次运行几个网络命令验证如下：

```
```bash
systemctl stop NetworkManager  （系统初始化时停止NetworkManager服务）
disable NetworkManager         （禁用NetworkManager服务）
service network start          （启动网络服务）
ifup ens33                     （重新挂载网络接口卡）

```

之后，再次查看IP地址

```
ip addr

```

<img src="https://img-blog.csdnimg.cn/af3f1062df7a466fa5b7a1b9d812ce80.png" alt="在这里插入图片描述">

可以看到，ens33设备成功绑定IP地址192.168.85.222! 使用以下命令，确认网络配置。

```
ifconfig

```

<img src="https://img-blog.csdnimg.cn/cb4e331ded12465eb5b8d14f4ac1be90.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/46ff71ac324045ff818dc999f5638f7b.png" alt="在这里插入图片描述">

点击**接受并保存**，启动远程连接成功！

<img src="https://img-blog.csdnimg.cn/7208e51d6cca45aca4416a51b1f2642b.png" alt="在这里插入图片描述">

输入**root**用户及密码，尝试登陆。 ``<img src="https://img-blog.csdnimg.cn/4d147f1f011944deb39898ab200bfe67.png" alt="在这里插入图片描述">

连接成功！如下图。

<img src="https://img-blog.csdnimg.cn/d66c83fae9414ce1a79bd7d9e869d2cd.png" alt="在这里插入图片描述">

已经由**root**超级用户登陆成功！

接下来，可在**Xshell**上尝试使用各种命令操作，也可以大刀阔斧地开展运维工作啦！
