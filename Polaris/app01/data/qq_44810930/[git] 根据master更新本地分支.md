
--- 
title:  [git] 根据master更新本地分支 
tags: []
categories: [] 

---
`git` 当前分支 t1
- 拉取远程master分支, 并更新- 将master分支合并到当前分支t1
```
git fetch origin master
git merge origin/master t1

```

第一行命令 `git fetch origin master` 会从远程仓库中获取最新的 `master` 分支代码，将其保存到本地的 `origin/master` 分支。

第二行命令 `git merge origin/master t1` 则将 `origin/master` 分支与当前分支 `t1` 合并，从而实现将远程 `master` 分支合并到本地 `t1` 分支的操作。

## 查看更新了哪些文件

要查看刚刚合并（merge）的内容，你可以使用以下 Git 命令来查看合并提交的详细信息：

```
git log --merges --first-parent

```

这个命令将列出所有合并提交，并且只显示合并提交的第一个父提交（通常是合并到的分支）。通过查看合并提交的详细信息，你可以了解到哪些内容在刚刚的合并中被包含进来。

如果你只想查看最近一次的合并提交，可以使用以下命令：

```
git show

```

要查看刚刚合并（merge）所包含的内容和哪些代码更新了，你可以使用以下 Git 命令来查看合并提交引入的变化：

```
git log -p -m --first-parent

```

这个命令将列出所有合并提交，并显示每个合并提交的详细变更内容。通过 `-p` 参数，你可以查看具体的代码变更，了解哪些文件被修改以及实际的代码更改是什么。

另外，`--first-parent` 参数指定只显示直接合并到当前分支的提交，以避免显示从其他分支合并过来的提交。

## commit时写错了

要修改上一个 commit 的信息，可以使用以下 Git 命令结合修改提交信息的操作：

```
git commit --amend

```

执行该命令后，Git 会打开一个文本编辑器（通常是默认的编辑器），让你修改上一个 commit 的提交信息。你可以修改提交信息后保存并关闭编辑器，Git 将会更新该 commit 的信息。

请注意，如果你已经将修改推送到远程仓库，修改提交信息后需要使用 `--force` 参数强制推送到远程分支：

```
git push --force

```

这样才能使远程仓库中的提交信息同步更新。记得谨慎使用 `--force`，因为可能会影响其他协作者的工作。
