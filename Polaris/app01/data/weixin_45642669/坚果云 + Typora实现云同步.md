
--- 
title:  坚果云 + Typora实现云同步 
tags: []
categories: [] 

---
这个是自己整理 + 网上的一部分。

##### 申请一个坚果云

不用多说，就是一个zookeeper简化版（或者理解为自动pull的git）。

#### 下载Typora

这个也不需要多说。

新建一个文件夹作为markdown根文件夹。

在这个文件夹下面新建一个pic文件夹。 把新建的文件夹进行云同步。

#### 将Typora同步到坚果云

将Typora同步到坚果云，以后打开的时候可以直接点击typora，即可在本地查看写的带图片的markdown。在另外一台电脑进行编辑的时候也不会因为配置不同写到其他路径。

（因为不知道配置文件的位置）

这样的话就可以实现在所有的电脑都能保证图片可见。

为了保证所有图片都能在pic文件夹可见，需要 设置设置Typora图片为相对路径： <img src="https://img-blog.csdnimg.cn/d48cd104ca8c43099889e5f0daf5fbbb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-Od5hAmN2-1645281254804)(pic/image-20220219223040286.png)]"> 这样的话，即可自动复制图片到对应路径。 非图床，所以无法分享到互联网。复制的话会提示没有链接。
