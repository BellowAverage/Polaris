
--- 
title:  git 合并多次提交记录（commit） 
tags: []
categories: [] 

---
### 一、应用场景

在开发过程中，对于一个完整的功能可能会先后进行多次提交。这种及提交方式不利于与代码走查时或者后期回顾功能点影响范围。为此，应该将多次提交合并为一次提交。

### 二、git rebase合并提交

例如当前提交如下：

```
[root@node2 test]# git log
commit 91bfbb8f599fa0129f28f9c4fd85e9feeca335be
Author: licc &lt;2719540156@qq.com&gt;
Date:   Wed Oct 18 06:20:41 2023 +0000

    功能：提交DockerFile

commit 56f27c0cd2f6e0c4d60b4b36526ea352ad7da5b8
Author: licc &lt;2719540156@qq.com&gt;
Date:   Wed Oct 18 06:16:53 2023 +0000

    功能：提交DockerFile

commit 7dbba7b7b46aa47bb57d109cd6c4dac3f3485a0a
Author: licc &lt;2719540156@qq.com&gt;
Date:   Wed Oct 18 05:28:38 2023 +0000

    功能：提交DockerFile与构建脚本、日志类型输出字符串

commit ae459d7a16e878276e6bb391c16ad4b4d0d23a47
Author: licc &lt;2719540156@qq.com&gt;
Date:   Fri Oct 13 09:09:06 2023 +0000

    功能：增加选项--no-web-service 关闭webService
    

```

若我想合并前3次提交即从91bfbb8f599fa0129f28f9c4fd85e9feeca335be到7dbba7b7b46aa47bb57d109cd6c4dac3f3485a0a的提交，以下为操作步骤：

##### 1、找到需要合并的提交记录的前一次commit id

这里是ae459d7a16e878276e6bb391c16ad4b4d0d23a47（增加选项–no-web-service 关闭webService）；

##### 2、使用git rebase -i &lt;的前一次commit id&gt; 开始合并：

```
git rebase -i ae459d7a16e878276e6bb391c16ad4b4d0d23a47

```

或

```
# 3表示合并前3次提交
git rebase -i HEAD~3

```

##### 3、此时弹出交互框，列出了需要合并的所有提交：

```
pick 7dbba7b 功能：提交DockerFile与构建脚本、日志类型输出字符串
pick 56f27c0 功能：提交DockerFile
pick 91bfbb8 功能：提交DockerFile

# 变基 ae459d7..0d23a47 到 ae459d7（3 个提交）
#
# 命令:
# p, pick &lt;提交&gt; = 使用提交
# r, reword &lt;提交&gt; = 使用提交，但修改提交说明
# e, edit &lt;提交&gt; = 使用提交，进入 shell 以便进行提交修补
# s, squash &lt;提交&gt; = 使用提交，但融合到前一个提交
# f, fixup &lt;提交&gt; = 类似于 "squash"，但丢弃提交说明日志
# x, exec &lt;命令&gt; = 使用 shell 运行命令（此行剩余部分）
# b, break = 在此处停止（使用 'git rebase --continue' 继续变基）
# d, drop &lt;提交&gt; = 删除提交
# l, label &lt;label&gt; = 为当前 HEAD 打上标记
# t, reset &lt;label&gt; = 重置 HEAD 到该标记
# m, merge [-C &lt;commit&gt; | -c &lt;commit&gt;] &lt;label&gt; [# &lt;oneline&gt;]
# .       创建一个合并提交，并使用原始的合并提交说明（如果没有指定
# .       原始提交，使用注释部分的 oneline 作为提交说明）。使用
# .       -c &lt;提交&gt; 可以编辑提交说明。
#
# 可以对这些行重新排序，将从上至下执行。
#
# 如果您在这里删除一行，对应的提交将会丢失。
#
# 然而，如果您删除全部内容，变基操作将会终止。
#

```

修改commit之前的单词，第一个commit保留为pick，后续的commit修改为s，

```
pick 7dbba7b 功能：提交DockerFile与构建脚本、日志类型输出字符串
s 56f27c0 功能：提交DockerFile
s 91bfbb8 功能：提交DockerFile

# 省略

```

修改完后，保存并退出（交互式框是vi编辑框，保存并退出的方法与vi操作相同）

##### 4、此时会再次弹出交互式对话框，用于设置提交的消息：

```
# 这是一个 3 个提交的组合。
# 这是第一个提交说明：

功能：提交DockerFile与构建脚本、日志类型输出字符串

# 这是提交说明 #2：

功能：提交DockerFile

# 这是提交说明 #3：

功能：提交DockerFile

# 请为您的变更输入提交说明。以 '#' 开始的行将被忽略，而一个空的提交
# 省略 ......

```

若需要修改提交消息增应将上面删除然后修改，例如修改如下：

```

功能：提交DockerFile与构建脚本、日志类型输出字符串

# 请为您的变更输入提交说明。以 '#' 开始的行将被忽略，而一个空的提交
# 省略 ......

```

修改完后，保存并退出（交互式框是vi编辑框，保存并退出的方法与vi操作相同）

##### 5、此时完成了本地仓库中commit的合并，可以通过git log查看合并后的效果

```
[root@node2 test]# git log
commit e66a398f3ae8889ec39ffae51cf1ddf773098dac
Author: licc &lt;2719540156@qq.com&gt;
Date:   Wed Oct 18 05:28:38 2023 +0000

    功能：提交DockerFile与构建脚本、日志类型输出字符串

commit ae459d7a16e878276e6bb391c16ad4b4d0d23a47
Author: licc &lt;2719540156@qq.com&gt;
Date:   Fri Oct 13 09:09:06 2023 +0000

    功能：增加选项--no-web-service 关闭webService
    

```

##### 6、如果之前的提交已经同步到git服务器，可以使用git push -f 强制将本地仓库同步至git服务器（可选）
