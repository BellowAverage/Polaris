
--- 
title:  《 Python程序设计项目案例》— 用Python开发的基于TCP通讯协议的私人聊天室 (期末大作业、结课作业、课程设计、毕业设计) 
tags: []
categories: [] 

---
## 基于Python与TCP协议的私人聊天室（GUI交互界面，用户注册、用户登录、实时聊天，文件上传与下载）

## 用Python开发的基于TCP通讯协议的实时聊天通讯和文件共享应用



#### 目录
- - - - - - <ul><li>- - <ul><li>- - - - <ul><li>- - - - 


## 1、项目概述：

　　在如今的大数据时代，科技飞速发展，人们的生活逐渐变得便利快捷，大家都更喜欢简单方便快捷的东西，从以前的车马很慢，到现在的实时通讯沟通，让言语不拘于距离，不止于步伐。为了满足工作生活的的需求，提高工作效率，学习效率，而又不在拘泥于距离。

　　针对以上问题，本项目以Python为开发语言，采用轻量tkinter作为前GUI端页面对每个单元功能板块进行设计，多线程进行各个功能实时并行，人性化美观的人机交互界面，数据以json格式TCP协议为基础，自定协议进行响应传输，利用mysql对用户数据进行存储修改，为了和现在的信息时代的特点个性符合，同时也具备严密的登录和注册功能，实现在线聊天和文件共享。

## 2、项目背景和意义

　　通信产业有强劲的生命力，依然处在蓬勃发展阶段之中，各种新的技术日新月异，层出不穷。但是蓬勃的发展中也有一些亟待解决的问题，这些都是现代通信的不足。日新月异，通讯不止于书信，不止于电话，现代最方便最快捷的就是线上实时聊天通讯，能有效便捷的沟通，工作学习都将得到进一步的快速提升。

## 3、项目组成及核心原理

### 3.1 项目总体框架

(1).用户注册

(2).用户登录

(3).进入聊天实时通讯

(4).上传共享文件

(5).下载共享文件

### 3.2 项目核心算法设计

#### 3.2.1 用户信息表

用户信息表utf8编码，主键为uid1

```
drop table user;
create table user (
uid1 int unsigned auto\_increment,
username varchar(20) not null unique,
password char(32) not null,
phone char(11) not null,
email char(32),
primary key(uid1)
)engine=InnoDB auto\_increment=1001 default charset=utf8;

```

Uid1: 用户id，唯一且不为空，自增长型，从1001开始增长。

Username:用户名，字符型，唯一且不为空。

Password:用户密码，字符型，不能为空。

Phone:用户手机号，字符型，可为空。

Email:用户邮箱，字符型，可为空。

#### 3.2.2 文件存储表

文件存储表utf8编码，uid为主键

```
drop table file;
create table file (
uid int unsigned auto\_increment,
fliename varchar(20) not null,
own char(36) not null,
data char(50) not null,
lx char(32),
primary key(uid)
 )engine=InnoDB auto\_increment=1 default charset=utf8;

```

Uid：文件id，自增长，从1开始。 Filename：文件名字，字符型，不可为空。 Own：上传文件的用户名称，字符型，不可为空。 Data：上传时间，字符型，不可为空。 Lx文件类型，字符型，可为空。

## 4、项目详细设计

### 4.1 基于TCP的自拟通讯协议

**tcp特点** 　　面向连接：通信双方必须先建立连接才能进行数据的传输，双方都必须为该连接分配必要的系统内核资源，以管理连接的状态和连接上的传输。双方间的数据传输都可以通过这一个连接进行。完成数据交换后，双方必须断开此连接，以释放系统资源。这种连接是一对一的，因此TCP不适用于广播的应用程序，基于广播的应用程序请使用UDP协议。

　　可靠传输：TCP采用发送应答机制，TCP发送的每个报文段都必须得到接收方的应答才认为这个TCP报文段传输成功，超时重传发送端发出一个报文段之后就启动定时器，如果在定时时间内没有收到应答就重新发送这个报文段。

　　错误校验由发送端计算,然后由接收端验证,其目的是为了检测数据在发送端到接收端之间是否有改动,如果接收方检测到校验和有差错，则直接丢弃这个数据包。

（1）. 基于TCP通信 （2）. 定长包头 （3）. json数据格式发 （4）. 客户端主动发送请求，服务端回应请求 （5）. 采用三个服务端，处理用户请求 （6）. 验证注册服务端，聊天发送接收服务端，文件上传下载服务端

### 4.2 通信格式

#### 4.2.1 用户登录
1. 客户端用户登录校验 ​ 示例：
```
 {
op:0,
 args:{
 user\_name:152xxxxxx89
 user\_pwd:

 }

```
1. 服务端发送: test:0表示校验成功，1表示校验失败 op:0表示用户登录 ​ 示例
```
{
op:0,
test:0
}

```

#### 4.2.2 用户发送验证码

1.用户端发送 示例：

```
 {
 op:0,
 test:0
 }

```

2.服务端响应 test:0表示成功，3表示手机号已存在,1表示网络问题,2表示手机号有问题 示例： {<!-- --> op:1, test:0 }

### 4.3 用户注册

#### 4.3.1 手机号验证

　　用户注册模块使用了第三方库requests用于调用手机号发送验证码API接口，第三方平台为网易云信，用于验证手机号码，requests是使用Apache2 licensed 许可证的HTTP库。在python内置模块的基础上进行了高度的封装，从而使得python进行网络请求时，变得人性化，使用Requests可以轻而易举的完成浏览器可有的任何操作。现代，国际化，友好。requests会自动实现持久连接keep-alive。

#### 4.3.2 正则验证

此外对于注册的每一个字段，都使用了正则表达式。

```
def test\_name(user\_name):
	if re.match(&amp;quot;^\S{<!-- -->1,6}$&amp;quot;,user\_name):
		a = True
	else:
		a = False
	return a

def test\_pwd(user\_pwd):
	if re.match(&amp;quot;^\s\*?$&amp;quot;,user\_pwd) or re.match(&amp;quot;^[a-z]\*?$&amp;quot;,user\_pwd) or re.match(&amp;quot;^[0-9]\*?$&amp;quot;,user\_pwd) or len(user\_pwd)\&amp;gt;16 or len(user\_pwd)\&amp;lt;12:
		a=False
	else:
		a = True
	return a

def test\_email(user\_email):
	if re.match(&amp;quot;^.\*?@.\*?\.([a-z]\*?)$&amp;quot;,user\_email):
		a = True
	else:
		a =False
	return a

def test\_phone(user\_phone):
	if re.match(&amp;quot;^1\d{<!-- -->10}$&amp;quot;,user\_phone):
		a = True
	else:
		a = False
	return a

```

　　有着较为严密的标准，用户密码至少由数字和字母组合，最低6位，最高16位，用户名为任意非空字符，最短为1，最长为6的限制，以确保存入数据库的数据合法准确。

#### 4.3.3 密码加密存储

　　对存入的密码采用了md5加密方法，以确用户的重要隐私，不会泄露。Md5全称: message-digest algorithm 5翻译过来就是: 信息 摘要 算法5

<img src="https://img-blog.csdnimg.cn/fd306b61b4cc4fe4be2c4ec556192e13.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMui0sOi_m-WItg==,size_20,color_222FFF,t_70,g_se,x_16" alt="在这里插入图片描述">

在用户注册时，会将密码进行md5加密，存到数据库中。这样可以防止那些可以看到数据库数据的人，恶意操作了。

### 4.4 用户登录

　　用户登录模块采用动态页面和特效使用了PIL第三方库，PIL(Python Image Library)是python的第三方图像处理库，但是由于其强大的功能与众多的使用人数，几乎已经被认为是python官方图像处理库了。其官方主页为:。

　　PIL历史悠久，原来是只支持python2.x的版本的，后来出现了移植到python3的库,pillow号称是`friendly fork for PIL`,其功能和PIL差不多，但是支持python3。 　　标题按钮，利用threading做了颜色动态变换的特效，

```
cc = ["#FFB6C1",'#FFC0CB', '#DC143C', '#FFF0F5', '#DB7093', '#FF69B4', '#FF1493', '#C71585', '#DA70D6', '#D8BFD8', '#DDA0DD', '#EE82EE', '#FF00FF', '#FF00FF', '#8B008B', '#800080', '#BA55D3', '#9400D3', '#9932CC', '#4B0082', '#8A2BE2', '#9370DB', '#7B68EE', '#6A5ACD', '#483D8B', '#E6E6FA', '#F8F8FF', '#0000FF', '#0000CD', '#191970', '#00008B', '#000080', '#4169E1', '#6495ED', '#B0C4DE', '#778899', '#708090', '#1E90FF', '#F0F8FF', '#4682B4', '#87CEFA', '#87CEEB', '#00BFFF', '#ADD8E6', '#B0E0E6', '#5F9EA0', '#F0FFFF', '#E0FFFF', '#AFEEEE', '#00FFFF', '#00FFFF', '#00CED1', '#2F4F4F', '#008B8B', '#008080', '#48D1CC', '#20B2AA', '#40E0D0', '#7FFFD4', '#66CDAA', '#00FA9A', '#F5FFFA', '#00FF7F', '#3CB371', '#2E8B57', '#F0FFF0', '#90EE90', '#98FB98', '#8FBC8F', '#32CD32','#00FF00', '#228B22', '#008000', '#006400', '#7FFF00', '#7CFC00', '#ADFF2F', '#556B2F', '#9ACD32', '#6B8E23', '#F5F5DC', '#FAFAD2', '#FFFFF0', '#FFFFE0', '#FFFF00', '#808000', '#BDB76B', '#FFFACD', '#EEE8AA', '#F0E68C', '#FFD700', '#FFF8DC', '#DAA520', '#B8860B', '#FFFAF0', '#FDF5E6', '#F5DEB3', '#FFE4B5', '#FFA500', '#FFEFD5', '#FFEBCD', '#FFDEAD', '#FAEBD7', '#D2B48C', '#DEB887', '#FFE4C4', '#FF8C00', '#FAF0E6', '#CD853F', '#FFDAB9', '#F4A460', '#D2691E', '#8B4513', '#FFF5EE', '#A0522D', '#FFA07A', '#FF7F50', '#FF4500', '#E9967A', '#FF6347', '#FFE4E1', '#FA8072', '#FFFAFA', '#F08080', '#BC8F8F', '#CD5C5C', '#FF0000', '#A52A2A', '#B22222', '#8B0000', '#800000', '#FFFFFF', '#F5F5F5', '#DCDCDC', '#D3D3D3', '#C0C0C0', '#A9A9A9', '#808080', '#696969', '#000000']


```

　　将各种颜色代码存入列表，再使用random对其进行随机变换。

### 4.5 聊天界面

　　此功能实现主要运用了多线程以及以上基于TCP自拟的通讯协议进行实时聊天，为了严谨性每次发消息都会对用户身份进行识别鉴定。整体界面简洁且高效。

### 4.6 文件共享

　　这部分整体都是基于TCP，整体问题都是因为TCP的特性，TCP:英文全拼(Transmission Control Protocol)简称传输控制协议，它是一种面向连接的、可靠的、基于字节流的传输层通信协议.TCP通信需要经过创建连接、数据传送、终止连接三个步骤。TCP通信模型中，在通信开始之前，一定要先建立相关的链接，才能发送数据，类似于生活中，打电话。

　　Tcp最大的缺点，是传输速度过慢，但不是这一功能模块面对的问题，主要问题是数据流传输的形式会出现粘包，导致传输的文件不正确，这里我采用定长包头的方式，先发送文件大小，定长接收，根据文件大小计算接收次数，最后使用md5校对文件是否正确。

## 5、界面效果图

登录界面，背景以及颜色皆为动态，截图不能展现动态效果： <img src="https://img-blog.csdnimg.cn/c588afb93277484eabf3039678baaca8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMui0sOi_m-WItg==,size_30,color_110000,t_70,g_se,x_16" alt="在这里插入图片描述">

　　注册界面截图，需输入用户名、密码、手机号、验证码以及邮箱 <img src="https://img-blog.csdnimg.cn/c1b011c0f52b4edaba7ab9e3d9f9c295.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMui0sOi_m-WItg==,size_30,color_222FFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 　　聊天界面截图，支持多人聊天，类似于多人聊天群组或私密聊天室 <img src="https://img-blog.csdnimg.cn/6184269a0a2547e2a924cfb2783b31d4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMui0sOi_m-WItg==,size_30,color_222FFF,t_70,g_se,x_16" alt="在这里插入图片描述">

　　文件上传界面截图，可浏览文件或文件夹，完成上传 <img src="https://img-blog.csdnimg.cn/e24369065f4d4cfeb592bd7b017a918c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAMui0sOi_m-WItg==,size_30,color_222FFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 6、总结

　　某信某q虽然好用，但是在这个信息时代隐私俨然已经成了问题，所以重要的工作和谈话使用自制的软件，还是比较具有隐秘性。

## 7、项目代码

　　通过下面的链接地址，关注 **2贰进制** ，并回复关键词，具体关键词可在下面链接地址对照列表查看：  https://mp.weixin.qq.com/s/ynG-dNNqO8kjIdf6ZFiZbg

## 更多内容

 https://blog.csdn.net/meenr/article/details/121452685 简书地址： 
