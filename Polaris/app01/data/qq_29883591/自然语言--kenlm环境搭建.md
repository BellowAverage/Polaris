
--- 
title:  自然语言--kenlm环境搭建 
tags: []
categories: [] 

---
      这篇博客主要是分享下小象学院自然语言课程（主讲：史兴）第二讲中示例中kenlm环境搭建的过程，同时也当给自己留个存档。

      对于这个环境的搭建，我是在ubuntu16.04的虚拟机中进行的，下面直接进入正题：

1、首先看一下此课程中搭建需要用的东西，如下图所示。在运行环境处，对于anaconda和NLTK是很简单的，这里就不多做解释了，如果有需要的可以留言交流。

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162152667" alt="">

2、直接进入KenLM环境的搭建，首先进入kenlm的github网址，然后会进入到kenlm的界面，如下：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162200386" alt="">

3、使用命令：wget -O - http://kheafield.com/code/kenlm.tar.gz |tar xz 对kenlm库进行下载，如下所示：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162206958" alt="">

（4）在刚刚kenlm的github官网中可以看到编译的方法：



<img src="https://img-blog.csdn.net/20180505162216649" alt="">

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt="">

对于提示的没有安装cmake，那么进行cmake的安装：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162225271" alt="">

继续执行我们的编译，会看到如下的错误：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162240907" alt="">

对于上图中的错误，谷歌了一下，得到了一个方法，使用命令apt install libboost-dev libboost-test-dev安装boost，如下：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162254185" alt="">

再次尝试编译，如下所示，可以看出是有效果的，然而好像boost的包还是不全面，这就说明我们刚刚没有下载全：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162301966" alt="">

又在网上找了个安装全部库的命令：sudo apt-get install libboost-all-dev（由于此前没截图，此处省略），直接展示执行完后的效果如下：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162312340" alt="">

如图所示，boost的问题解决了，然后按照提示解决Eigen3的问题，最后我们继续cmake：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/201805051623209" alt="">

至此，cmake问题解决。

（5）执行命令：make -j 4，如下所示：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162330413" alt="">

<img src="http://write.blog.csdn.net/postedit/80205917" alt="">

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162344175" alt="">

至此，kenlm环境搭建完毕。

（6）执行训练模型的脚本，如下所示，可以看出，好像我们的环境还没有搭建完全，提示的是lmplz不存在，然后build_binary不存在：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162352912" alt="">

（7）谷歌查找了一些资料后，发现自己的bin文件夹中是有这些文件的，那么唯一的问题就是我们的系统中没有为它们设置环境变量，将kenlm的路径添加进去即可，这个路径依据自己的机器上的具体路径为准，我的如下图中箭头所示：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162400893" alt="">

保存上述文件，然后执行source .profile，使环境变量生效。

（8）重新执行下训练脚本，如下所示，成功了：

<img src="http://write.blog.csdn.net/postedit/80205917" alt=""><img src="https://img-blog.csdn.net/20180505162409831" alt="">

<img src="http://write.blog.csdn.net/postedit/80205917" alt="">

       至此，kenlm环境已经搭建成功了，此次分享就到这里，有什么不对的地方欢迎大家交流指正。

关键词：CMake Warning at /usr/share/cmake-3.5/Modules/FindBoost.cmake:725 (message):  Imported targets not available for Boost versiontrain.sh.UNK: line 1: lmplz: command not foundtrain.sh.UNK: line 2: build_binar
