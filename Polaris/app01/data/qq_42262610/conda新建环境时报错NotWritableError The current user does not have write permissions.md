
--- 
title:  conda新建环境时报错NotWritableError: The current user does not have write permissions 
tags: []
categories: [] 

---


在使用

```
conda create -n environment_name
```

命令新建环境时，遇到错误：

>  
 Solving environment: failed NotWritableError: The curren user does not have write permissions to a required path.   path: /home/user_name/.conda/pkgs/urls.txt   uid: 1021   gid: 1021 
 If you feel that permissions on this path are set incorrectly, you can manually change them by executing 
   $ sudo chown 1021:1021 /home/user_name/.conda/pkgs/urls.txt 
 In general, it's not advisable to use 'sudo conda'. 


#### 2、问题原因

也许是安装Anaconda的时候，使用了**sudo** sh Ana...造成的多余问题。

安装Anaconda的时候使用了root权限，所以现在非root用户没有对anaconda3文件夹的读写权限。

#### 3、解决方案

方案一：

>  
 'cd' 到 'annoconda3' 文件夹所在位置，运行以下命令： 
 <pre>`sudo chown -R username anaconda3    #username为自己的用户名`</pre> 


方案二：

>  
 按照他给出的提示操作无果，于是使用下面的命令改变conda相关文件夹的权限，-r递归应用于子文件夹 
 sudo chmod 777 -R ~/anaconda3/ sudo chmod 777 -R ~/.conda/ 


#### 4、测试

使用方案一对我的问题无效，但是有网友说是可行的。

方案二成功地解决了我的问题，可以新建环境了。

Solving environment: done


