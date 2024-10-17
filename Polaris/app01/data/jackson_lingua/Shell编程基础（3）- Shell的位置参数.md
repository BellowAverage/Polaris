
--- 
title:  Shell编程基础（3）- Shell的位置参数 
tags: []
categories: [] 

---
## Shell编程基础（3）- Shell的位置参数

### Shell Scripting Essentials (3) – Locative Parameters of Shell Scripting

前文介绍过shell变量。当声明shell变量时，只需要在代码行写出变量名称即可;在输入行用read命令要求用户输入，在语句末尾加上变量name, 如下所示：

```
read -p “Enter your name: “ name

```

而当引用一个变量时，需要在变量名之前添加一个美元符号( $ ，例如: $ name),这样做是为了获取变量的值，而不是变量名本身。

```
echo “Welcome, Mr.$name.”

```

## 1. 位置参数

Shell提供了一些特殊变量，最常用的一组变量成为位置参数（或者命令行参数），取名为 **$0, $1, $2, $3… $n.**

其中，$0比较特殊，表示被调用脚本的名称；而其它位置参数则被赋予命令行传递而来的参数值（按照在命令行出现的顺序赋值）。

我们看以下这个脚本文件(theScript.sh)：

```
# A Script to output command-line arguments by echo
echo “The first argument is $1, the second one is $2.”
echo “The command line itself is called $0.”
echo “There are $# parameters on your command line.”
echo “Here are all the arguments $@”

```

运行下面这个脚本（后跟四个命令行参数）

```
sh theScript.sh TaylorSwift LadyGaga EdSheen EltonJohn

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/a1bb1a24df6a454aa616c9195a71a993.png" alt="在这里插入图片描述">

如你所见，位置参数 **$0** 为theScript的完整路径或相对路径：

```
The command itself is called theScript.sh

```

其他位置参数中，$1 为TaylorSwift, $2 为LadyGaga, $3 为EdSheeran, $4 为EltonJohn.

此外，还可以使用 $ # 获取脚本被赋予的参数数量；在上述示例中，$ #为4；而$@变量则保存了命令行中输入的所有四个参数。

#### 2. $?的使用

另一个非常有用的变量是$?, 它接受最后一条被执行命令的退出状态。一般来说，0值意味着命令成功退出；而非0值则表示某一种类型的错误。

#### 3. 读取参数

Linux系统通过read命令，可以提示用户输入信息，并存储该信息，以便日后在脚本中使用，接下列列举一个使用了read命令的脚本示例(脚本文件名为perfectScript.sh)：

```
#!/bin/bash
Read -p “Type an adjective, noun and verb (past tense):” adj1 noun1 verb1
Echo “He signed and $verb1 to the elixir, then he ate the $adj1 $noun1.”

```

编辑脚本及执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/b8ec970815d244dda2566846e9a5cc9c.png" alt="在这里插入图片描述">

位置参数可以灵活的添加到脚本中，并且在执行shell脚本时进行交互；$开头的参数以数字从小到大排列； $ #用来获取脚本被赋予的参数数量，而 $@将保存了命令输入的所有参数。

技术好文不断推出，敬请关注。 喜欢就点赞哈! 😃
