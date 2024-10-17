
--- 
title:  git的使用 
tags: []
categories: [] 

---
## git的使用

代码托管中心是基于网络服务器的远程代码仓库，一般我们简单称为远程库。

局域网：
- gitlab
互联网：
- github- gitee 码云
官网地址： https://git-scm.com/

#### 常用命令：

查看版本：

```
git --version
git config --global user.name 用户名    #设置用户签名
git config --global user.email 邮箱   #设置用户签名


git init     #初始化本地库

git status   #查看本地库状态

git add 文件名  #添加到暂存区

git commit -m "日志信息" 文件名     #提交到本地库

git reflog  #查看版本信息
git log     #查看版本详细信息

git reset --hard 版本号    #版本穿梭

```

新增文件：

```
vim hello.txt

```

#### Git分支操作：

<img src="https://img-blog.csdnimg.cn/img_convert/4b51e26f7a0a7500a5595721426ee5c0.png" alt="img">
- 在版本控制过程中，同时推进多个任务，为每个任务，我们就可以创建每个任务的单独
分支。
- 分支可以简单理解为副本，一个分支就是一个单独的副本。（分支底层其实也是指针的引用）- 同时并行推进多个功能开发，提高开发效率。- 各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响。失败的分支删除重新开始即可。
分支操作：

```
# 查看分支
git branch -v 

# 创建分支
git branch 分支名

# 切换分支
git checkout 分支名

# 合并分支
git merge 分支名

```

产生冲突：

```
冲突产生的表现：后面状态为 MERGING
Layne@LAPTOP-Layne MINGW64 /d/Git-Space/SH0720 (master|MERGING)

解决冲突：
编辑有冲突的文件，删除特殊符号，决定要使用的内容
特殊符号：&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD 当前分支的代码 ======= 合并过来的代码 &gt;&gt;&gt;&gt;&gt;&gt;&gt; hot-fix

```

#### 远程仓库操作：

```
git remote -v    # 查看当前所有远程地址别名
git remote add 别名 远程地址    # 起别名
git push 别名 分支    # 推送本地分支上的内容到远程仓库
git clone 远程地址    # 将远程仓库的内容克隆到本地
git pull 远程库地址别名 远程分支名    # 将远程仓库对于分支最新内容拉下来后与当前本地分支直接合并

```

#### 创建github账号及库：

```
git remote -v    # 查看当前所有远程地址别名

# 给远程库起别名，方便记忆（尽量与远程库同名）
git remote add 别名 远程地址
git remote add git-demo https://github.com/swltp/git-demo.git

# push代码到远程库
git push git-demo master

# pull远程库的代码到本地
git pull git-demo master

# 克隆远程库的内容到本地,(这里不需要登录就可以克隆)
git clone https://github.com/swltp/git-demo.git

```

克隆会进行三部操作：
- 拉取代码- 初始化本地仓库- 创建别名