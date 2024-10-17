
--- 
title:  找不到DNS地址的解决方案 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/ae71112ca0c14d0fb7be74fba2140835.png#pic_center" alt="在这里插入图片描述">



#### 找不到DNS地址的解决方案
- - - <ul><li>- 


## 第一种解决方案：刷新DNS缓存

<mark>`WIN+R`输入`cmd`回车输入命令输入命令 `ipconfig /flushdns` 并按回车键。将刷新DNS解析缓存</mark>

<img src="https://img-blog.csdnimg.cn/direct/f773d57428d44c22af61ef705dd4cc89.png#pic_center" alt="在这里插入图片描述">

## 第二种解决方案： 配置Internet协议版本4（TCP/IPv4）

<mark>按`WIN+I`快捷键打开Windows设置选择网络和Internet选项</mark>

<img src="https://img-blog.csdnimg.cn/direct/047d2861c6c94d3a8c33846a51b6936e.png" alt="在这里插入图片描述"> <mark>在左侧状态里点击`更改适配器选项`</mark>

<img src="https://img-blog.csdnimg.cn/direct/036f3d3dff244aab992b6742685f0e6c.png#pic_center" alt="在这里插入图片描述"> <mark>点击`WLAN选项`</mark>

<img src="https://img-blog.csdnimg.cn/direct/269f861541964dd18743ad6001843e97.png#pic_center" alt="在这里插入图片描述"> <mark>点击`属性`</mark>

<img src="https://img-blog.csdnimg.cn/direct/f0439959a64f4ed8be0f9e42787ce764.png#pic_center" alt="在这里插入图片描述"> <mark>点击`Internet协议版本4（TCP/IPv4）`</mark>

<img src="https://img-blog.csdnimg.cn/direct/9776d566219742e493edee142fbc5a15.png#pic_center" alt="在这里插入图片描述"> <mark>选择自动获得IP地址、使用下方的DNS服务器地址，输入8.8.8.8</mark> `下一部分会简单讲一下为何这样设置`

<img src="https://img-blog.csdnimg.cn/direct/40e49a7de7744540ab44020842718a30.png#pic_center" alt="在这里插入图片描述">

### 配置IP地址

<img src="https://img-blog.csdnimg.cn/direct/929d194f107549eb806d9b41fb1be7fa.png" alt="在这里插入图片描述">

>  
 选择自动获取 IP 地址（也称为 DHCP，Dynamic Host Configuration Protocol）通常是更为方便和推荐的做法，因为它使得网络配置更加灵活和自动化。DHCP 可以`自动为你的设备分配 IP 地址、子网掩码、默认网关和 DNS 服务器地址`，减少了手动配置的麻烦，特别是在移动设备或连接不同网络的情况下。 


使用自动获取 IP 地址的优势包括：
- 1.自动化配置： 系统会自动获取一个可用的 IP 地址，无需手动输入。- 2.避免IP冲突： DHCP 确保分配的 IP 地址在网络上是唯一的，避免了潜在的 IP 地址冲突问题。- 3.易于管理： 对于网络管理员来说，更容易集中管理和维护网络配置。
>  
 然而，在某些情况下，可能需要手动配置 IP 地址，例如： 
 - 特定网络要求： 某些网络可能需要手动配置特定的 IP 地址、子网掩码和 DNS 服务器地址。- 固定设备连接： 对于一些固定连接的设备，手动配置 IP 地址可以提供更为稳定的网络连接。 


综合考虑，大多数用户在日常使用中都会选择自动获取 IP 地址，因为它更方便、适用范围更广，并降低了网络配置的繁琐性。

### 配置DNS地址

<img src="https://img-blog.csdnimg.cn/direct/2273046b88ff400aa443c2734c7f4c41.png" alt="在这里插入图片描述">

>  
 选择自动获取 DNS 服务器地址（也称为 DHCP 分配 DNS）通常是更为推荐的选择。这允许你的设备从`网络服务提供商（ISP）或网络管理员自动获取 DNS 服务器地址`，并且在连接不同网络时更加方便。 


使用自动获取DNS服务器地址的优势包括：
- 1.自动更新： 自动获取 DNS 地址可确保你使用的是最新的、由 ISP 提供的 DNS 服务器地址。- 2.网络切换时更方便： 如果你经常连接到不同的网络，自动获取 DNS 服务器地址可以确保你无需手动更改，使得在不同网络间的切换更为无缝。
>  
 然而，有些情况下，手动设置 DNS 服务器地址可能会更合适，比如： 
 - 提高性能或隐私保护： 一些用户可能选择使用特定的第三方 DNS 服务器，博主使用的是Google的`8.8.8.8`，以获得更快的域名解析速度或增强隐私保护。- 网络访问控制： 在某些特定网络中，可能需要手动配置特定的 DNS 服务器地址，以便符合网络访问策略或限制。 


总体而言，对于大多数用户来说，选择自动获取 DNS 服务器地址通常是更加方便和实用的，因为它可以减少手动配置带来的麻烦，并确保设备始终使用有效的 DNS 服务器地址。然而，对于寻求更快速度或更严格隐私保护的用户，手动设置特定的 DNS 服务器地址也是一个可选的选择。

## 如何查看本机IPv4地址、子网掩码与默认网关

<mark>`WIN+R`输入`cmd`回车然后输入`ipconfig`命令即可查看IP配置，在里面即可查看</mark>

<img src="https://img-blog.csdnimg.cn/direct/897030fa92c54d1d8f13bab113ec71b2.png" alt="在这里插入图片描述">
