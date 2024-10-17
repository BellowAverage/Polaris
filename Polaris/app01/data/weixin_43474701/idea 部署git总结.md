
--- 
title:  idea 部署git总结 
tags: []
categories: [] 

---


#### idea 部署git总结
- <ul><li>- - - - - 


### github密匙快捷获取方法

简单的步骤就不记录了，记录几个问题 <img src="https://img-blog.csdnimg.cn/5b0ba78a25254b05a714baaf38984d15.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/abe935477e0e4e15a1bfa33457cfb691.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c560820ce34a4412a63d3eca912ab025.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/0a7767ca7ae047aaad786ae79a900af6.png" alt="在这里插入图片描述">

### idea将本地项目上传到远程仓库GitHub

idea里面使用命令行，直接上传本地项目到远程仓库， 命令行入口 <img src="https://img-blog.csdnimg.cn/221f51c19aeb481d8e132cae17da15d6.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/dfe14d03bf004238a5e7d20a29882f42.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8873f95ec7ec408f8ae813f6864ebc90.png" alt="在这里插入图片描述"> 中途会有弹窗可以输入密码或者网页认证 <img src="https://img-blog.csdnimg.cn/1e769c9d838e4d9a9c2ecff1528522fa.png" alt="在这里插入图片描述">

<font color="red" size="5">WiFi如果上传不了就连手机热点</font>

>  
 从命令行创建一个仓库 touch READNE.md git init git add README.md git comit -m “fist commit” git remote add origin 仓库地址 git push -u origin master 


### <font color="red">报错-》error: src refspec master does not match any.</font>

利用git add xxx.py 指令，将所有的文件全部都添加，然后再进行git commit -m "init"将所有的文件commit,

git commit -m “init”

git remote add origin xxxxxxxx.git

### Everything up-to-date

<img src="https://img-blog.csdnimg.cn/b8c9466d5c5a4dc495dcb5a49822cffc.png" alt="在这里插入图片描述"> push之前必须要写commit。 git commit -m “wiki”

### specify commit message

<img src="https://img-blog.csdnimg.cn/4f4f87088658403c84f616454291e5fa.png" alt="在这里插入图片描述"> 在红框里面写上描述就行了，比如这是我第一次提交文件，再点击Commit就可以了

### hint: Updates were rejected because the tip of your current branch is behind

强制推送并且覆盖远程git仓库：git push -f origin master
