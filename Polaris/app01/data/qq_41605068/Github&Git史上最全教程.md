
--- 
title:  Github&Git史上最全教程 
tags: []
categories: [] 

---
## 一、注册账号：

####         注意:

            1.私有仓库是收费的，公共仓库就行；

            2.新注册的用户必须验证邮箱后才可以创建git仓库；

            3.为qq邮箱，当没有收到邮件时，要在qq邮箱中设置白名单。

## 二、目的: 借助github托管项目代码。

## 三、基本概念:

      仓库(Repository)：即项目；

      收藏(Star);

      复制克隆项目(Fork):当点击之后，别人的仓库里就多了这个项目，只不过这个项目是基于你的项目基础(本质上是在原有的项目基础上新建了一个分支），可以随便的去改进，不会影响原有项目的代码结构。

      发起请求(Pull Request):想把自己的改进合并到的原有的项目里，就可以发起一个PR，原有项目创建人就可以收到这个请      求，当创建人觉得ok，就会接受他的PR，这个时候他的改进在原有项目中就有了。

     关注(Watch):如果你W了这个项目，那么以后只要这个项目有任何更新，你都会在第一时间收到关于这个项目的通知提醒。

     事务卡片(lssue)：即bug,别人发现你的项目中有bug或者那些地方做的不好，他就可以给你提个lssue，这样你就可以逐一修    复，ok了就可以一个个的close掉。

## 四、Git安装与使用

     目的：通过Git管理GitHub项目(GitHub是一个面向开源及私有软件项目的托管平台，因为只支持Git作为唯一的版本库格式进                   行托管，故名命为:GitHub)

     下载:Git官网下载并安装  

     安装:

            <img alt="" class="has" height="345" src="https://img-blog.csdnimg.cn/20190710113827908.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="443">

            <img alt="" class="has" height="367" src="https://img-blog.csdnimg.cn/20190710113849877.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="471">

          查看是否安装成功:（桌面右单击）

           <img alt="" class="has" height="260" src="https://img-blog.csdnimg.cn/20190710114153341.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="466">

## 五.Git工作区域

     <img alt="" class="has" height="244" src="https://img-blog.csdnimg.cn/20190712142534709.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="507">

#### 5.1向仓库添加文件流程

      git status //查看一下此时工作区的状态(假设待上传文件都在工作区)

      git add 文件名  //从工作区到暂存区

      git status  //查看暂存区此时的工作状态

      git commit -m "提交描述"   //提交到仓库

      git status     //查看此时仓库的状态

## 六.Git基础设置

### 6.1Git安装完成后，需要进行一些基本信息的设置（该设置在GitHub仓库主页显示谁提交了该文件）

     1.设置用户名: git config --global user.name "用户名"

     2.设置用户邮箱: git config --global user.email "邮箱"

     3.查看设置:git config --list

### 6.2初始化一个新的Git仓库

####       1.创建文件夹：mkdir 文件名(test)

####       2.在文件内初始化git（创建git仓库）

            cd test

            git init   //此时会出现.git ，如果看不见，则设置电脑显示隐藏文件      

####       3.向仓库添加文件

           touch 文件名(a.html)    //1.创建文件

           git status       //查看此时区域状态(工作区)

           git add a.html      //2.添加到暂存区

           git commit -m "描述"    //3.将文件从暂存区提交到仓库 

####       4.修改文件    

           ls   //列出当前目录下的所有文件

           vi  a.html(待编辑的文件)   //编辑模式，vi命令详解  

           cat a.html     //保存

           git status       //查看状态

           git add a.html  //添加到暂存区

           git commit -m "描述"      //提交到仓库

           git status

####      5.删除仓库文件

           rm -rf  a.html   //删除文件(第一步)

           git rm a.html    //从git中删除文件(第二步)

           git commit -m "提交描述"     //提交操作 (第三步)

## 七.Git管理远程仓库

###  7.1使用远程仓库的目的：备份、实现代码共享集中化管理

###  7.2 由于本地Git仓库和Github仓库之间的传输是通过SSH加密的，所以连接时需要设置一下：

####      7.2.1创建SSH KEY。

         先看一下你C盘用户目录下有没有.ssh目录，有的话看下里面有没有id_rsa和id_rsa.pub这两个文件，有就跳到下一步，没有就通过下面命令创建：

         $  ssh-keygen -t rsa -C "youremail@example.com"

        <img alt="" class="has" height="176" src="https://img-blog.csdnimg.cn/20190717101735153.png" width="571">

    此时会发现:

          <img alt="" class="has" height="120" src="https://img-blog.csdnimg.cn/20190717101828570.png" width="498">

#### 7.2.2登录Github，设置

         找到右上角的图标，打开点进里面的Settings，再选中里面的SSH and GPG KEYS，点击右上角的New SSH key，然后Title里面随便填，再把刚才id_rsa.pub里面的内容复制到Title下面的Key内容框里面，最后点击Add SSH key，这样就完成了SSH Key的加密。

<img alt="" class="has" height="239" src="https://img-blog.csdnimg.cn/20190717102529271.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1134">

输入:

```
$ ssh -T git@github.com

```

<img alt="" class="has" height="61" src="https://img-blog.csdnimg.cn/2019071711173124.png" width="568">（输入：yes）

#### 7.2.3在GitHub上创建Git仓库，并关联本地git

  在Github上创建好Git仓库之后我们就可以和本地仓库进行关联了，赋值仓库地址：

<img alt="" class="has" height="103" src="https://img-blog.csdnimg.cn/20190717105521110.png" width="384">

关联：

```
 $  git remote add origin 地址.git
```

<img alt="" class="has" height="31" src="https://img-blog.csdnimg.cn/20190717105852559.png" width="496">

关联好之后我们就可以把本地库的所有内容推送到远程仓库（也就是Github）上了:

```
git push -u origin master  //因为第一次仓库是空的所有需要加-u参数

git push origin master     //当仓库有东西时，提交时，执行这个即可
```

<img alt="" class="has" height="286" src="https://img-blog.csdnimg.cn/20190717114604918.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="613">

报错:<img alt="" class="has" height="33" src="https://img-blog.csdnimg.cn/20190717114647190.png" width="563">

原因: 这是由于你新创建的那个仓库里面的README文件不在本地仓库目录中，这时我们可以通过以下命令先将内容合并以下

```
git pull --rebase origin master    //合并readme.txt
```

成功:

:<img alt="" class="has" height="174" src="https://img-blog.csdnimg.cn/20190717122615222.png" width="511">

再次提交：

<img alt="" class="has" height="168" src="https://img-blog.csdnimg.cn/20190717122807318.png" width="513">

#### 7.3Git克隆操作

      目的：将远程仓库(github对应的项目)复制到本地

      命令：git clone 仓库链接地址

## 遇到的坑：

### 1.ssh连接不上服务器,把之前的ssh删除，重新生成一下

<img alt="" class="has" height="74" src="https://img-blog.csdnimg.cn/20190717111955943.png" width="548">

解决方法：7.2.2

#### 思考:为什么无法同步?

答案：私有项目，没有权限，输入用户名密码，或者远程地址采用这种类型:

         vi .git/config

         将[remote "origin"]

              url = https://github.com/用户名/仓库名.git

         修改为:

          [remote "origin"]

                url = https://用户名:密码@github.com/用户名/仓库名.git

## 8.其它命令

### 8.1分支

```
--当前仓库的所有分支
git  branch   
--创建一个叫 new 的分支
git branch  new
--切换分支
git  checkout  new
--合并过来
git  merge  new
--将暂存区的文件保存到另外一个地方(堆栈)
git stash
git stash pop

--删除分支
git branch -d new


git remote remove  new
--查看所有仓库
git remote
--查看所有仓库的信息
git remote -v
--添加一个仓库
git remote add new http:******
```

 
