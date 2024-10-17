
--- 
title:  git pull 时每次都要输入账号和密码的解决办法 
tags: []
categories: [] 

---
如果我们 git clone 下载代码的时候是连接的 https:// （就是 git remote -v 显示的那个 url）

```
root@master ~/xxx# git remote -v
origin	https://gitee.com/account/repo.git (fetch)
origin	https://gitee.com/account/repo.git (push)
```

而不是 git@git (ssh) 的形式，当我们操作 git pull/push 到远程的时候，总是提示我们输入账号和密码才能操作成功，频繁的输入账号和密码会很麻烦。

### 解决办法1：

把原创仓库地址写成用 git@git 的形式（记得添加机器的 ssh 公钥到远端仓库哟！！！）：

```
root@master ~/xxx# git remote rm origin
root@master ~/xxx# git remote add origin git@gitee.com:account/repo.git
root@master ~/xxx# git remote -v
origin	git@gitee.com:account/repo.git (fetch)
origin	git@gitee.com:account/repo.git (push)

```

### 解决办法2（常用）：

cd xxx 进入你的项目目录，输入：

git config --global credential.helper store

输入以上指令后，下面文件的最后会多出以下内容：

```
root@master ~/xxx# cat ~/.gitconfig 
[user]
	name = looking
	email = looking@qq.com
[credential]
	helper = store
```

然后你使用上述的命令配置好之后，再操作一次 git pull，然后它会提示你输入账号密码，这一次之后就不需要再次输入密码了。

```
root@master ~/xxx# git pull
Username for 'https://gitee.com': 
Password for 'https://account@gitee.com': 
From https://gitee.com/account/repo
 * [new branch]      database   -&gt; origin/database
 * [new branch]      master     -&gt; origin/master
There is no tracking information for the current branch.
Please specify which branch you want to rebase against.
See git-pull(1) for details.

    git pull &lt;remote&gt; &lt;branch&gt;

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/&lt;branch&gt; master

```

关联分支：

```
root@master ~/xxx# git branch --set-upstream-to=origin/master
Branch 'master' set up to track remote branch 'master' from 'origin'.

```

 同时在与 .gitconfig  相同目录下会存在一个 .git-credentials 文件，上边就已经记录了你刚才输入的账号和密码，之后操作就不用再输入密码了。

```
root@master ~/insight-tool# cat ~/.git-credentials 
https://account:passwd@gitee.com

```

 

  
