
--- 
title:  git clone和git push操作流程 
tags: []
categories: [] 

---
## 生成personal access token

直接使用git push命令或者用HTTPS进行git clone时会报错，错误信息如下所示：

>  
 报错：remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead. remote: Please see  for more information. fatal: unable to access '': The requested URL returned error: 403 


或者出现下图所示情况，即输入命令后，会出现一个窗口，上面提示用浏览器登录或密码登录，若点击浏览器登录会出来一个灰色小窗口，依次输入用户名与密码，但登录成功后，git黑窗口却出现fatal:已取消一个任务；若点击密码登录，会出现一串验证码，并跳转到网页窗口，将方才出现的验证码输入进去后，网页上将出现如图所示 Congratulations,you are all set!字样，但git黑窗口依然会出现fatal:已取消一个任务。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/af628cebf65b5e5247263293fbd34598.webp?x-oss-process=image/format,png">

造成其二者报错信息的原因：自2021年8月13日起，github不再支持使用密码push的方式。

>  
 解决方案：两种 一、 使用SSH 二、使用Personal access token 


#### 法一：使用SSH



#### 法二：使用Personal access token

首先，需要获取token

1.点击你的GitHub头像 -&gt; 设置 -&gt; 开发者设置 -&gt; Personal access tokens -&gt; Generate new token

2.生成token

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6d3f3b2640c29f8c5a806f0a07312f50.webp?x-oss-process=image/format,png">

3.复制token 4.使用token进行push、pull、clone等操作（pull和clone等操作原理同push，只需替换push为pull或其他相应的命令即可） 使用token的方式其实原理在于将原来明文密码换为token，说白了就是token&gt;=password，之所以我这里写了&gt;号，是因为token的功能远大于原来的password，相比password，token具有很多其没有的用法。

### token使用方法

#### token法一：直接push

此方法每次push都需要输一遍token

```
   # git push https://你的token@你的仓库链接，我这里是我的仓库链接你要改成你的
   git push https://你的token@github.com/sober-orange/study.git
复制代码
```

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/0a70cc8bd5da3f24ce3c614fa3e30655.webp?x-oss-process=image/format,png">

#### token法二：修改remote别名

这种方式在push的时候直接指明别名就可 如果你已经设置过remote别名，使用如下命令

```
# 我这里的别名是origin
# git remote set-url 你的remote别名 https://你的token@你的仓库地址
# git remote set-url origin https://【用户名】:【token】@github.com/用户名/项目名.git

git remote set-url origin https://你的token@github.com/sober-orange/study.git
# 提交代码
git push -u origin master
复制代码
```

如果你未设置过别名，使用如下命令添加别名

```
 # git remote add 别名 https://你的token@你的仓库地址
 git remote add origin https://你的token@github.com/sober-orange/study.git
 # 提交代码
 git push -u origin master
复制代码
```

#### token法三：使用Git Credential Manager Core (GCM Core) 记住token

```
git push
Username: 你的用户名
Password: 你的token
# 记住token
git config credential.helper store
复制代码
```

#### toekn法四：使用Windows的凭据管理器
1. 打开凭据管理器 -&gt; windows凭据1. 找到“git:”的条目，编辑它1. 用token替换你以前的密码
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/53b85173acdca06059cefd8e6589d103.webp?x-oss-process=image/format,png">

### push命令详细说明

git push命令用于将本地分支的更新，推送到远程主机。它的格式与git pull命令相仿。

```
git push &lt;远程主机名&gt; &lt;本地分支名&gt;:&lt;远程分支名&gt;
复制代码
```

注意：这里的:前后是必须没有空格的。\colorbox{cyan}{注意：这里的:前后是必须没有空格的。}注意：这里的:前后是必须没有空格的。​

注意，分支推送顺序的写法是&lt;来源地&gt;:&lt;目的地&gt;， 所以git pull是&lt;远程分支&gt;:&lt;本地分支&gt;， 而git push 是&lt;本地分支&gt;:&lt;远程分支&gt;。

如果省略远程分支名，则表示将本地分支推送与之存在"追踪关系"的远程分支（通常两者同名），如果该远程分支不存在，则会被新建。

```
git push origin master
复制代码
```

上面命令表示，将本地的master分支推送到origin主机的master分支。如果后者不存在，则会被新建。（在本地需要上传的文件夹上打开git后，使用git init命令生成.git文件后，该文件夹默认为master分支）

如果省略本地分支名，则表示删除指定的远程分支，因为这等同于推送一个空的本地分支到远程分支。

```
git push origin :master
# 等同于
git push origin --delete master
复制代码
```

上面命令表示删除origin主机的master分支。

如果当前分支与远程分支之间存在追踪关系，则本地分支和远程分支都可以省略。

```
git push origin
复制代码
```

上面命令表示，将当前分支推送到origin主机的对应分支。

如果当前分支只有一个追踪分支，那么主机名都可以省略。

```
git push
复制代码
```

如果当前分支与多个主机存在追踪关系，则可以使用-u选项指定一个默认主机，这样后面就可以不加任何参数使用git push。

```
git push -u origin master
复制代码
```

上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了。

### git push操作流程

```
# 1、（先进入项目文件夹）通过命令 git init 把这个目录变成git可以管理的仓库
    git init
# 2、把文件添加到版本库中，使用命令 git add .添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文件夹下的所有文件
   git add .
# 3、用命令 git commit告诉Git，把文件提交到仓库。引号内为提交说明
   git commit -m 'first commit'
# 4、关联到远程库 即使用如下命令添加别名
　 git remote add origin 你的远程库地址
# 5、使用token登录
   git remote set-url origin https://【用户名】:【token】@github.com/用户名/项目名.git
# 6、把本地库的内容推送到远程，使用 git push命令，实际上是把当前分支master推送到远程。执行此命令后会要求输入用户名、密码，验证通过后即开始上传。
 git push -u origin master:远程分支名
复制代码
```

注意： git使用commit命令后显示Author identity unknown 报错如下：

```
*** Please tell me who you are.
Run  
git config --global user.email "you@example.com"  
git config --global user.name "Your Name" to set your account's default identity.
Omit --global to set the identity only in this repository. fatal:
unable to auto-detect email address (got 'Zero@zero.(none)')
复制代码
```

在git命令行中重新输入命令： 先输入：git config --global user.name “你的名字” 回车后， 再输入：git config --global user.email “你的邮箱地址” 完成后再提交就没问题了。

### git clone 流程

```
git clone https://access_token@github.com/username/xxx.git
复制代码
```

### git相关命令

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/a1d8af6614d99f5d2afd295d4112ad9a.webp?x-oss-process=image/format,png">
