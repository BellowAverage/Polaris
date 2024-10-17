
--- 
title:  Dockerfile中的CMD (❁´◡`❁) 和 ENTRYPOINT (●ˇ∀ˇ●) 
tags: []
categories: [] 

---
## 带你了解Dockerfile中CMD和ENTRYPOINT

此篇博客只为用于学习，大家喜欢的话还请关注一下原作者哦！

转载地址：https://www.cnblogs.com/sparkdev/p/8461576.html

作者：

出处：http://www.cnblogs.com/sparkdev/

CMD 和 ENTRYPOINT 指令都是用来指定容器启动时运行的命令。单从功能上来看，这两个命令几乎是重复的。单独使用其中的一个就可以实现绝大多数的用例。但是既然 doker 同时提供了它们，为了在使用中不至于混淆，本文试图把它们的用法理清楚。

## exec 模式和 shell 模式

CMD 和 ENTRYPOINT 指令都支持 exec 模式和 shell 模式的写法，所以要理解 CMD 和 ENTRYPOINT 指令的用法，就得先区分 exec 模式和 shell 模式。这两种模式主要用来指定容器中的不同进程为 1 号进程。了解 linux 的朋友应该清楚 1 号进程在系统中的重要地位。笔者也在《》一文中介绍过 1 号进程对容器中信号处理的重要性，感兴趣的朋友可以移步进行了解。下面我们通过 CMD 指令来学习 exec 模式和 shell 模式的特点。

**exec 模式**

使用 exec 模式时，容器中的任务进程就是容器内的 1 号进程，看下面的例子：

把上面的代码保存到 test1 目录的 Dockerfile 中，然后进入 test1 目录构建镜像并启动一个容器：

然后查看容器中的进程 ID：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223130211589-1153779778.png" alt="" class="medium-zoom-image">

从图中我们看到运行 top 命令的进程 ID 为 1。exec 模式是建议的使用模式，因为当运行任务的进程作为容器中的 1 号进程时，我们可以通过 docker 的 stop 命令优雅的结束容器(详情请参考《》)。

**exec 模式的特点是不会通过 shell 执行相关的命令，所以像 $HOME 这样的环境变量是取不到的**：

把上面的代码保存到 test1 目录的 Dockerfile 中，然后进入 test1 目录构建镜像并启动一个容器：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223130421899-425658453.png" alt="" class="medium-zoom-image">

通过 exec 模式执行 shell 可以获得环境变量：

把上面的代码保存到 test1 目录的 Dockerfile 中，然后进入 test1 目录构建镜像并启动一个容器：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223130529482-988600776.png" alt="" class="medium-zoom-image">

这次正确取到了 $HOME 环境变量的值。

**shell 模式**

使用 shell 模式时，docker 会以 /bin/sh -c "task command" 的方式执行任务命令。也就是说容器中的 1 号进程不是任务进程而是 bash 进程，看下面的例子：

把上面的代码保存到 test2 目录的 Dockerfile 中，然后进入 test2 目录构建镜像并启动一个容器：

然后查看容器中的进程 ID：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223130735006-594451977.png" alt="" class="medium-zoom-image">

1 号进程执行的命令居然是 /bin/sh -c top。而我们指定的 top 命令的进程 ID 为 7。这是由 docker 内部决定的，目的是让我们执行的命令或者脚本可以取到环境变量。

## CMD 指令

CMD 指令的目的是：为容器提供默认的执行命令。CMD 指令有三种使用方式，其中的一种是为 ENTRYPOINT 提供默认的参数：**CMD ["param1","param2"]**另外两种使用方式分别是 exec 模式和 shell 模式：**CMD ["executable","param1","param2"]**    // 这是 exec 模式的写法，注意需要使用双引号。**CMD command param1 param2**                  // 这是 shell 模式的写法。注意命令行参数可以覆盖 CMD 指令的设置，但是只能是重写，却不能给 CMD 中的命令通过命令行传递参数。一般的镜像都会提供容器启动时的默认命令，但是有些场景中用户并不想执行默认的命令。用户可以通过命令行参数的方式覆盖 CMD 指令提供的默认命令。比如通过下面命令创建的镜像：

在启动容器时我们通过命令行指定参数 ps aux 覆盖默认的 top 命令：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223130944593-1511091543.png" alt="" class="medium-zoom-image">

从上图可以看到，命令行上指定的 ps aux 命令覆盖了 Dockerfile 中的 CMD [ "top" ]。实际上，命令行上的命令同样会覆盖 shell 模式的 CMD 指令。

## ENTRYPOINT 指令

ENTRYPOINT 指令的目的也是为容器指定默认执行的任务。ENTRYPOINT 指令有两种使用方式，就是我们前面介绍的 exec 模式和 shell 模式：**ENTRYPOINT ["executable", "param1", "param2"]**   // 这是 exec 模式的写法，注意需要使用双引号。**ENTRYPOINT command param1 param2**                   // 这是 shell 模式的写法。exec 模式和 shell 模式的基本用法和 CMD 指令是一样的，下面我们介绍一些比较特殊的用法。

**指定 ENTRYPOINT  指令为 exec 模式时，命令行上指定的参数会作为参数添加到 ENTRYPOINT 指定命令的参数列表中。**用下面的代码构建镜像 test1：

运行下面的命令：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131125462-1226384921.png" alt="" class="medium-zoom-image">

我们在命令行上添加的参数被追加到了 top 命令的参数列表中。

**由 CMD 指令指定默认的可选参数：**

使用这段代码构建镜像 test2 并不带命令行参数启动容器：

这时容器中运行的命令为：top -b -c。如果我们指定命令行参数：

-n 1 会覆盖 通过 CMD [ "-c" ] 指定的参数，容器执行的命令为：top -b -n 1

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131251202-140384117.png" alt="" class="medium-zoom-image">

注意上图的输出显示 -c 参数被覆盖了。

**指定 ENTRYPOINT  指令为 shell 模式时，会完全忽略命令行参数：**

把上面的代码编译成镜像 test2，分别不带命令行参数和使用命令行参数 ls 执行命令：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131407554-1561884995.png" alt="" class="medium-zoom-image">

我们看到 ls 命令没有被执行，这说明命令行参数被 ENTRYPOINT  指令的 shell 模式忽略了。

**覆盖默认的 ENTRYPOINT 指令：**ENTRYPOINT 指令也是可以被命令行覆盖的，只不过不是默认的命令行参数，而是需要显式的指定 --entrypoint 参数。比如我们通过下面的方式覆盖上面镜像中的 echo $HOME 命令：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131500161-1384881659.png" alt="" class="medium-zoom-image">

这里我们使用 hostname 命令覆盖了默认的 echo $HOME 命令。

## Dockerfile 中至少要有一个

如果镜像中既没有指定 CMD 也没有指定 ENTRYPOINT 那么在启动容器时会报错。这不算是什么问题，因为现在能见到的绝大多数镜像都默认添加了 CMD 或 ENTRYPOINT 指令。

## 指定任意一个，效果差不多

从结果上看，CMD 和 ENTRYPOINT 是一样的，我们可以通过它们实现相同的目的。下面我们分别用 CMD 和 ENTRYPOINT 设置 top -b 命令，然后观察容器运行时的 metadata 信息：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131618500-870134564.png" alt="">

或者：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131645158-1706317623.png" alt="">

虽然实现方式不同，但最终容器运行的命令是一样的。

## 同时使用 CMD 和 ENTRYPOINT 的情况

对于 CMD 和 ENTRYPOINT 的设计而言，多数情况下它们应该是单独使用的。当然，有一个例外是 CMD 为 ENTRYPOINT 提供默认的可选参数。我们大概可以总结出下面几条规律：    • 如果 ENTRYPOINT 使用了 shell 模式，CMD 指令会被忽略。    • 如果 ENTRYPOINT 使用了 exec 模式，CMD 指定的内容被追加为 ENTRYPOINT 指定命令的参数。    • 如果 ENTRYPOINT 使用了 exec 模式，CMD 也应该使用 exec 模式。真实的情况要远比这三条规律复杂，好在 docker 给出了官方的解释，如下图所示：

<img src="https://images2018.cnblogs.com/blog/952033/201802/952033-20180223131745112-1674454515.png" alt="" class="medium-zoom-image">

当我们无法理解容器中运行命令的行为时，说不定通过这个表格可以解开疑惑！

## 总结

对于 Dockerfile 来说，CMD 和 ENTRYPOINT 是非常重要的指令。它们不是在构建镜像的过程中执行，而是在启动容器时执行，所以主要用来指定容器默认执行的命令。但是提供两个功能类似的指令，必然会给用户带来理解上的困惑和使用中的混淆。希望本文能够帮助大家理解二者的区别与联系，并更好的使用二者。
