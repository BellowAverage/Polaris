
--- 
title:  git的使用 
tags: []
categories: [] 

---
### 一、了解git

#### 1.集中化版本控制系统和分布式版本控制系统的特点

（**git属于分布式版本控制系统**）

<img src="https://img-blog.csdnimg.cn/img_convert/f9ffc83deea5a7b9041bc2995ddd1741.png" alt="image.png">

<img src="https://img-blog.csdnimg.cn/img_convert/d227b154ffdc086e06eb2ee20ad4ea98.png#pic_center" alt="在这里插入图片描述">

#### 2.git的三个区域及三种状态：

<img src="https://img-blog.csdnimg.cn/img_convert/d8a4b03560da9d63f6c4bad470520e54.png#pic_center" alt="在这里插入图片描述">

### 二、git的使用

#### **实现自己在web建的仓库与本地仓库进行信息更新**

<img src="https://img-blog.csdnimg.cn/img_convert/308cf775dc92231b69d5ece7cff40b0a.png" alt="image.png">

<img src="https://img-blog.csdnimg.cn/img_convert/1563e99850a939923118aabba46b819f.png" alt="image.png">

#### 步骤：

##### 1.在web界面新建仓库

<img src="https://img-blog.csdnimg.cn/img_convert/6624eff909cdc8fca71c9ac313c62ced.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/img_convert/7b480ee690ee78f78ecab616fb587af3.png#pic_center" alt="在这里插入图片描述">

##### 2.把web界面的新建的远程仓库克隆到本地仓库

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码 
$ git clone https://gitee.com/weihong1117/python-test.git

```

##### 3.进入仓库目录（所有与具体项目/仓库相关的操作一定要先进入仓库目录再进行操作）

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码
$ cd python-test/    

```

##### 4.修改文件

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ echo 'xxx' &gt;&gt; README.md   

```

##### 5.把修改文件放入暂存区

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git add README.md          

```

##### 6.提交文件

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git commit -m '添加了一个README.md文件' 
[master a107f57] 添加了一个README.md文件 1 file changed, 1 insertion(+) create mode 100644 README.md        

```

##### 7.把文件推上远程仓库

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git push origin master   #origin--&gt;自己的仓库的别名映射，master--&gt;仓库下面的分支   

```

###### 可用 git remote -v 命令查看别名映射

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/pirate-king-2022/20220306-git及python起步/homework/weihong (master)
$ git remote -v 
origin  https://gitee.com/weihong1117/pirate-king-2022.git (fetch) 
origin  https://gitee.com/weihong1117/pirate-king-2022.git (push) 
teacher https://gitee.com/vaster/pirate-king-2022.git (fetch) 
teacher https://gitee.com/vaster/pirate-king-2022.git (push)  

```

#### 仓库分支：

##### 1.查看当前仓库的分支

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git branch -a 
master 
remotes/origin/HEAD -&gt; origin/master remotes/origin/master           

```

##### 2.创建分支

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git branch test1 
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git branch -a 
master 
test1
remotes/origin/HEAD -&gt; origin/master remotes/origin/maste            

```

##### 3.切换分支

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (master) 
$ git checkout test1 
Switched to branch 'test1'             

```

##### 4.创建并进入分支

```
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (test1) 
$ git checkout -b test2 
Switched to a new branch 'test2' 
Lenovo@LAPTOP-CEL1ETIO MINGW64 /h/三创学习资料/python学习软件/海贼王-代码/python-test (test2)
 $ git branch -a
master
test1 
test2
remotes/origin/HEAD -&gt; origin/master 
remotes/origin/master    

```

​

​
