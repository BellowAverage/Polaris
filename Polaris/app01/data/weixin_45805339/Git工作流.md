
--- 
title:  Git工作流 
tags: []
categories: [] 

---
## Git工作流

Gitflow工作流通过为功能开发、发布准备和维护分配独立的分支，让发布迭代过程更流畅。严格的分支模型也为大型项目提供了一些非常必要的结构。 <img src="https://img-blog.csdnimg.cn/20200108170356411.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### Gitflow工作流

Gitflow工作流定义了一个围绕项目发布的严格分支模型。虽然比功能分支工作流复杂几分，但提供了用于一个健壮的用于管理大型项目的框架。

Gitflow工作流没有用超出功能分支工作流的概念和命令，而是为不同的分支分配一个明确的角色，并定义分支之间如何和什么时候进行交互。 除了使用功能分支，在做准备、维护和记录发布时，也定义了各自的分支。 当然你可以用上功能分支工作流所有的好处：Pull Requests、隔离实验性开发和更高效的协作。

#### 1 工作方式

Gitflow工作流仍然用中央仓库作为所有开发者的交互中心。和其它的工作流一样，开发者在本地工作并push分支到要中央仓库中。

#### 2 历史分支

相对于使用仅有的一个master分支，Gitflow工作流使用两个分支来记录项目的历史。master分支存储了正式发布的历史，而develop分支作为功能的集成分支。 这样也方便master分支上的所有提交分配一个版本号。 <img src="https://img-blog.csdnimg.cn/20200108173126227.png" alt="在这里插入图片描述">

#### 3 功能分支

每个新功能位于一个自己的分支，这样可以push到中央仓库以备份和协作。 但功能分支不是从master分支上拉出新分支，而是使用develop分支作为父分支。当新功能完成时，合并回develop分支。 新功能提交应该从不直接与master分支交互。 <img src="https://img-blog.csdnimg.cn/20200108173236625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 注意，从各种含义和目的上来看，功能分支加上develop分支就是功能分支工作流的用法。但Gitflow工作流没有在这里止步。

#### 4 发布分支

<img src="https://img-blog.csdnimg.cn/20200108173307824.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 一旦develop分支上有了做一次发布（或者说快到了既定的发布日）的足够功能，就从develop分支上checkout一个发布分支。 新建的分支用于开始发布循环，所以从这个时间点开始之后新的功能不能再加到这个分支上—— 这个分支只应该做Bug修复、文档生成和其它面向发布任务。 一旦对外发布的工作都完成了，发布分支合并到master分支并分配一个版本号打好Tag。 另外，这些从新建发布分支以来的做的修改要合并回develop分支。

使用一个用于发布准备的专门分支，使得一个团队可以在完善当前的发布版本的同时，另一个团队可以继续开发下个版本的功能。 这也打造定义良好的开发阶段（比如，可以很轻松地说，『这周我们要做准备发布版本4.0』，并且在仓库的目录结构中可以实际看到）。

常用的分支约定：

```
用于新建发布分支的分支: develop
用于合并的分支: master
分支命名: release-* 或 release/*

```

#### 5 维护分支

<img src="https://img-blog.csdnimg.cn/20200108173640870.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

#### 6 示例

下面的示例演示本工作流如何用于管理单个发布循环。假设你已经创建了一个中央仓库。

**创建开发分支** <img src="https://img-blog.csdnimg.cn/20200108173805261.png" alt="在这里插入图片描述"> 第一步为master分支配套一个develop分支。简单来做可以本地创建一个空的develop分支，push到服务器上：

```
git branch develop
git push -u origin develop

```

以后这个分支将会包含了项目的全部历史，而master分支将只包含了部分历史。其它开发者这时应该克隆中央仓库，建好develop分支的跟踪分支：

```
git clone ssh://user@host/path/to/repo.git
git checkout -b develop origin/develop

```

现在每个开发都有了这些历史分支的本地拷贝。

**小华和小李开始开发新功能** <img src="https://img-blog.csdnimg.cn/20200108175532656.png" alt="在这里插入图片描述"> 这个示例中，小红和小明开始各自的功能开发。他们需要为各自的功能创建相应的分支。新分支不是基于master分支，而是应该基于develop分支：

```
git checkout -b some-feature develop

```

他们用老套路添加提交到各自功能分支上：编辑、暂存、提交：

```
git status
git add 
&lt;
some-file
&gt;

git commit

```

**小红完成功能开发** <img src="https://img-blog.csdnimg.cn/20200108180051704.png" alt="在这里插入图片描述"> 添加了提交后，小红觉得她的功能OK了。如果团队使用Pull Requests，这时候可以发起一个用于合并到develop分支。 否则她可以直接合并到她本地的develop分支后push到中央仓库：

```
git pull origin develop
git checkout develop
git merge some-feature
git push
git branch -d some-feature

```

第一条命令在合并功能前确保develop分支是最新的。注意，功能决不应该直接合并到master分支。 冲突解决方法和集中式工作流一样。

**小华开始准备发布** <img src="https://img-blog.csdnimg.cn/20200108180127621.png" alt="在这里插入图片描述"> 这个时候小明正在实现他的功能，小红开始准备她的第一个项目正式发布。 像功能开发一样，她用一个新的分支来做发布准备。这一步也确定了发布的版本号：

```
git checkout -b release-0.1 develop

```

这个分支是清理发布、执行所有测试、更新文档和其它为下个发布做准备操作的地方，像是一个专门用于改善发布的功能分支。

只要小红创建这个分支并push到中央仓库，这个发布就是功能冻结的。任何不在develop分支中的新功能都推到下个发布循环中。 **小红完成发布** <img src="https://img-blog.csdnimg.cn/20200108180248742.png" alt="在这里插入图片描述"> 一旦准备好了对外发布，小红合并修改到master分支和develop分支上，删除发布分支。合并回develop分支很重要，因为在发布分支中已经提交的更新需要在后面的新功能中也要是可用的。 另外，如果小红的团队要求Code Review，这是一个发起Pull Request的理想时机。

```
git checkout master
git merge release-0.1
git push
git checkout develop
git merge release-0.1
git push
git branch -d release-0.1

```

发布分支是作为功能开发（develop分支）和对外发布（master分支）间的缓冲。只要有合并到master分支，就应该打好Tag以方便跟踪。

```
git tag -a 0.1 -m "Initial public release" master
git push --tags

```

Git有提供各种勾子（hook），即仓库有事件发生时触发执行的脚本。 可以配置一个勾子，在你push中央仓库的master分支时，自动构建好版本，并对外发布。

**最终用户发现Bug** <img src="https://img-blog.csdnimg.cn/20200108180438320.png" alt="在这里插入图片描述"> 对外版本发布后，小红小明一起开发下一版本的新功能，直到有最终用户开了一个Ticket抱怨当前版本的一个Bug。 为了处理Bug，小红（或小明）从master分支上拉出了一个维护分支，提交修改以解决问题，然后直接合并回master分支：

```
git checkout -b issue-#001 master
# Fix the bug
git checkout master
git merge issue-#001
git push

```

就像发布分支，维护分支中新加这些重要修改需要包含到develop分支中，所以小红要执行一个合并操作。然后就可以安全地删除这个分支了：

```
git checkout develop
git merge issue-#001
git push
git branch -d issue-#001

```

## Git总结

### 1 Gitflow工作流分支

<th align="left">分支</th><th align="left">作用</th>
|------
<td align="left">master</td><td align="left">迭代历史分支</td>
<td align="left">dev</td><td align="left">集成最新开发特性的活跃分支</td>
<td align="left">f_xxx</td><td align="left">feature 功能特性开发分支</td>
<td align="left">b_xxx</td><td align="left">bug修复分支</td>
<td align="left">r_xxx</td><td align="left">release 版本发包分支</td>

### 2 Confict冲突解决
<li> 方式一 
  <ol><li> 获取最新代码 <pre><code>git fetch
</code></pre> </li><li> 对比代码 <pre><code>git diff origin/dev
</code></pre> </li>-  修改冲突地方后提交并推送代码 -  发起合并请求 </ol> </li><li> 方式二 
  <ol><li> 拉取并合并最新代码 <pre><code>git pull origin dev
</code></pre> </li><li> 查看冲突代码 <pre><code>git status
</code></pre> </li>-  修改冲突代码后提交并推送代码 -  发起合并请求 </ol> </li>