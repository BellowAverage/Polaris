
--- 
title:  git 忽略文件 mode 变化 
tags: []
categories: [] 

---
最近刚好碰到了，所以稍微写一下。

### 起因

我原来的电脑坏了，所以换了一个电脑。但是由于远端的仓库比较大，所以准备先用 xftp 从虚拟机把里边的仓库下载下来。git pull 后看到也是最新的。

```
lukaiyi@LAPTOP-73GH1NT7 MINGW64 /c/Project/zddiv3 (dev-3.16)
$ git pull
Already up to date.

```

但是 git status 的时候，可以看到一大堆 modified 文件：

```
lukaiyi@LAPTOP-73GH1NT7 MINGW64 /c/Project/zddiv3 (dev-3.16)
$ git status
On branch dev-3.16
Your branch is up to date with 'origin/dev-3.16'.

Changes not staged for commit:
  (use "git add &lt;file&gt;..." to update what will be committed)
  (use "git restore &lt;file&gt;..." to discard changes in working directory)
        modified:   bin/msgmgr_service/msgmgr_service.rb
        modified:   bin/register_service/public/css/chosen/chosen.css
        modified:   bin/register_service/public/css/common.css
...
```

git diff 查看的时候，**可以看到文件内容并没有改变，只是文件 mode 发生了变化（**因为 Linux 和 Windows 文件系统不一样的缘故，导致了拷贝以后文件的权限发生了变化，而这种变化刚好又被 git 捕捉到了）。

```
lukaiyi@LAPTOP-73GH1NT7 MINGW64 /c/Project/zddiv3 (dev-3.16)
$ git diff
diff --git a/bin/msgmgr_service/msgmgr_service.rb b/bin/msgmgr_service/msgmgr_service.rb
old mode 100755
new mode 100644
...
```

虽然并没有什么太大影响，但是强迫症受不了。

### 修复

```
git config --add core.filemode false
```

```
lukaiyi@LAPTOP-73GH1NT7 MINGW64 /c/Project/zddiv3 (dev-3.16)
$ git config --add core.filemode false

lukaiyi@LAPTOP-73GH1NT7 MINGW64 /c/Project/zddiv3 (dev-3.16)
$ git diff

```

**有时候，设置以后，需要重新再进入一下项目目录才生效。**
