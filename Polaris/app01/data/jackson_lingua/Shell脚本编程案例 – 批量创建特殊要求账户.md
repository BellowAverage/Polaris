
--- 
title:  Shell脚本编程案例 – 批量创建特殊要求账户 
tags: []
categories: [] 

---
## Shell脚本编程案例 – 批量创建特殊要求账户

### Shell Scripting Cases – Create a Bunch of accounts with special requests

By Jackson@ML

本文简要介绍批量执行Shell脚本命令的基本思路，以检验shell脚本知识掌握情况。希望对读者有所帮助。

>  
 案例要求： 
 - 需要批量创建20个系统账号（例如new_user001至new_user020），并进行密码设置（密码为随机值，要求是字母和数字混合的八位数）；- 把账号和密码保存到文本文档中作为备份以供查看；- 在操作过程中的提示被保存到文本文件中， 屏幕不输出任何提示信息，当全部用户创建完毕，并且加密完成后输出提示语。 


#### 一、分步实现

以下分步骤解释该课题的实现过程。

##### 1. 创建20个账户

###### 1） 方法一：用seq命令输出等宽且步长为1的序列；

命令：

```
seq -w 020

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/539261d85b8e432aa0cc806e56e07809.png" alt="在这里插入图片描述">

###### 2） 方法二：用echo命令直接输出

命令：

```
echo {<!-- -->001..020}

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/dd39b9fdc17747148aa7d60bed44313b.png" alt="在这里插入图片描述">

##### 2. 无交互地设置密码

此命令执行之前，必须先创建一个新用户（new_user）,然后再设置该用户的新密码（例如：八位数字），并用双引号包围。

命令：

```
useradd new_user
echo “89674523” | passwd --stdin new_user

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/a95b44d8ba8d4ce09aa718191954cfce.png" alt="在这里插入图片描述">

##### 3. 创建一个混合的随机八位密码

命令：

```
echo $RANDOM | md5sum | cut -c 8-15

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/c990ce746d254724905ae6f6b5e17050.png" alt="在这里插入图片描述"> 可以看到随即产生的密码为：f65951de

##### 4. 把账号密码备份到文档

命令：

```
echo -e “$user\t $password“ &gt;&gt; UserDetail.txt

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/6eeb068f1efa4d098f26d6b2549de076.png" alt="在这里插入图片描述">

同时，可以看到，密码备份文件UserDetail.txt位于当前目录/root。

##### 5. 仅输出最后提示。

#### 二、批量实现

接下来，将上述命令批量实现，集中到一个shell脚本文件(useradd.sh) 中，全部代码如下：

<img src="https://img-blog.csdnimg.cn/direct/02d372d7f7d04fc084e353e78c60fe83.png" alt="在这里插入图片描述"> 接下来，执行该脚本：

```
sh useradd.sh

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/160726e826b0469b9a1b6496c81ef69b.png" alt="在这里插入图片描述"> 查看日志文本文件：

```
cat UserLog.txt

```

<img src="https://img-blog.csdnimg.cn/direct/52f3ac5ce51547dabafbc8b89dd12d4d.png" alt="在这里插入图片描述"> 说明执行成功！

技术好文陆续推出，敬请关注。

喜欢就点赞哈，您的认可，我的动力！😊

#### 相关阅读：
1. 1. 1. 1. 1. 1. 