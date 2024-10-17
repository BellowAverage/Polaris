
--- 
title:  git 本地仓添加多个远端仓库 
tags: []
categories: [] 

---
知其然，知其所以然！

一般不涉及团队协作开发的话，添加一个远端仓库就够了，也就是你从 gitee 或者 github 上对应的 origin 克隆的那个仓库，比如：

```
[root@master GitTest]# git remote -v
origin	git@gitee.com:L2392863668/GitTest.git (fetch)
origin	git@gitee.com:L2392863668/GitTest.git (push)

```

添加远端仓库的命令其实并不复杂，关键是为什么要添加多个远程仓库呢？或者说，添加多个远端仓库以后，需要怎么去用起来？

```
git remote add &lt;upstream&gt; &lt;url&gt;
```

当然，既然放出来了这个问题，首先要分析一下原因，一般添加多个远程仓库的实用场景如下：

**你有一个本地仓 local、一个远端个人仓 origin（可自由 pull 和 push） 和一个远端主仓 upstream（一般来说只可以 pull ，没有直接 push 的权限），且远端个人仓是 fork 的远端主仓（通过 fork 关系关联）。本地代码则是先推送到远端个人仓，然后再提交 pr 到远端主仓，Committer 审核 pr 以后再合并到主仓。由于主仓的代码是多人协作的，难免可能会出现冲突的情况，所以你一般需要从远端主仓拉取最新代码到本地（强制拉取覆盖本地或者手动处理合并冲突），然后在此基础上再进行开发，以此来减少代码提交时的冲突。**

虽然现在像 gitee 等都是支持直接从远端主仓 upstream 强制更新代码到远端个人仓 origin 的，不过你还得再从远端个人仓 origin 拉取代码到本地 local，显然多绕了一圈路。

如果有配置多个远端仓库（origin 和 upstream）的话，代码的拉取和提交就要方便得多了。本文以主分支 maser 为例，实际操作时根据需要进行变更。

### 克隆远端个人仓

克隆远端个人仓以后，你的远端 origin 默认就添加上了。

```
[root@master test]# git clone git@gitee.com:L2392863668/GitTest.git
Cloning into 'GitTest'...
remote: Enumerating objects: 247, done.
remote: Total 247 (delta 0), reused 0 (delta 0), pack-reused 247
Receiving objects: 100% (247/247), 1.27 MiB | 626.00 KiB/s, done.
Resolving deltas: 100% (96/96), done.
[root@master test]# ll
total 0
drwxr-xr-x. 4 root root 165 Dec 15 20:57 GitTest
[root@master test]# cd GitTest/
[root@master GitTest]# git remote -v
origin	git@gitee.com:L2392863668/GitTest.git (fetch)
origin	git@gitee.com:L2392863668/GitTest.git (push)

```

### 本地添加远端主仓

一般也称为上游仓库（upstream）

```
[root@master GitTest]# git remote add upstream git@github.com:2392863668/GitTest.git
[root@master GitTest]# git remote -v
origin	git@gitee.com:L2392863668/GitTest.git (fetch)
origin	git@gitee.com:L2392863668/GitTest.git (push)
upstream	git@github.com:2392863668/GitTest.git (fetch)
upstream	git@github.com:2392863668/GitTest.git (push)

```

### 从主仓拉取代码到本地

#### 完全以远端主仓为准

由于你的个人仓 origin 可能会和远端主仓 upstream 的代码冲突（比如其他协作者的 pr 先你一步合并到主仓了，导致你自己的 pr 合并不进去），这时候你可以选择直接丢弃掉本地修改，完全以主仓为准：

```
[root@master GitTest]# git fetch upstream master; git reset --hard upstream/master
From github.com:2392863668/GitTest
 * branch            master     -&gt; FETCH_HEAD
HEAD is now at 1912baa deal merge conflict in hello.txt

```

#### 与本地修改进行合并

如果你要保留本地已经做过的修改，请从主仓拉取代码并进行合并（如果有冲突的话，注意处理合并冲突）：

```
[root@master GitTest]# git pull upstream master
remote: Enumerating objects: 26, done.
remote: Counting objects: 100% (26/26), done.
remote: Compressing objects: 100% (19/19), done.
Unpacking objects: 100% (26/26), 3.82 KiB | 279.00 KiB/s, done.
remote: Total 26 (delta 7), reused 19 (delta 5), pack-reused 0
From github.com:2392863668/GitTest
 * branch            master     -&gt; FETCH_HEAD
 * [new branch]      master     -&gt; upstream/master
Merge made by the 'recursive' strategy.
 hello.txt   |  3 +--
 looking.txt |  1 +
 readme.txt  | 13 +------------
 world.txt   |  1 +
 4 files changed, 4 insertions(+), 14 deletions(-)

```

### 本地推送到远端个人仓

#### 直接强制推送 

由于之前你的本地仓 local 和远端个人仓 origin 的代码是一致的，如果你是强制从远端主仓 upstream 更新的话，推送到远端个人仓的时候也需要强制推送。

```
[root@master GitTest]# git push -f origin master
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.2]
To gitee.com:L2392863668/GitTest.git
 + 7710a4c...1912baa master -&gt; master (forced update)

```

#### 合并后推送

如果你已经处理过合并冲突的话，推送到个人仓的时候就不会再冲突了。

```
[root@master GitTest]# git push origin master
Enumerating objects: 38, done.
Counting objects: 100% (34/34), done.
Delta compression using up to 4 threads
Compressing objects: 100% (26/26), done.
Writing objects: 100% (28/28), 3.95 KiB | 252.00 KiB/s, done.
Total 28 (delta 9), reused 0 (delta 0), pack-reused 0
remote: Powered by GITEE.COM [GNK-6.2]
To gitee.com:L2392863668/GitTest.git
   b65b892..7710a4c  master -&gt; master

```

### 在个人仓提交 pr

提交 pr 合并请求这个我就不啰嗦了，需要了解的话请看我的另外一篇博客：
