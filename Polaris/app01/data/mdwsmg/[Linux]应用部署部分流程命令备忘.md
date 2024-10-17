
--- 
title:  [Linux]应用部署部分流程命令备忘 
tags: []
categories: [] 

---
备忘一下常用的Linxu应用部署命令，Java应用版。 

#### 目录
- - <ul><li>- - <ul><li>- - 


## 1、环境查询

### 1.1、端口占用查询

lsof -i 命令

```
lsof -i:端口号

```

示例:lsof -i:8001 <img src="https://img-blog.csdnimg.cn/b380f9fa8b224915af6323fe973e0246.png" alt="在这里插入图片描述">

若无权限则使用

```
netstat -tunlp | grep 端口号

```

<img src="https://img-blog.csdnimg.cn/5967b6c8efc54b248225d2e5b4dde25d.png" alt="在这里插入图片描述">

### 1.2、环境变量查询与设置

经常能在各种配置脚本中看到诸如 $LOGPATH之类的字样，使用echo ${LOGPATH}命令输出，echo $LOGPATH也可以输出，printenv LOGPATH也可以

```
echo $LOGPATH
echo ${LOGPATH}
printenv LOGPATH

```

直接使用printenv可以查看所有环境变量。

#### 设置局部用户定义变量

```
my_variable="Hello World";
echo $my_variable;

```

#### 设置全局环境变量

只在当前会话有效，关闭会话后失效。如果想永久生效，可把这句命令拷贝到linux启动脚本中。

```
export my_variable; 

```

#### 删除环境变量

```
unset my_variable;

```

## 2、执行命令保存日志并查看

将sh脚本的执行结果输出到文件，然后查看文件，可以做到命令执行即查看命令执行过程

```
sh yoursh.sh  &gt; temp.log &amp;&amp; tail -f temp.log

```

## 3、查看java应用内存使用情况

可以使用jamp命令查看堆内对象示例的统计信息、查看 ClassLoader 的信息以及 finalizer 队列，以及生成dump文件。

```
jamp -heap pid

```

jamp -heap pid可以查看当前进程堆详细信息 <img src="https://img-blog.csdnimg.cn/19fdd97703134af58f5e27042ae3e314.png" alt="在这里插入图片描述"> jmap -histo 显示堆中对象的统计信息 pid是进程号，20表示排名前二十，instances表示实例数量，bytes表示占用内存大小（1M=1024KB,1KB=1024Bytes）

```
 jmap -histo pid | head -n 20

```

<img src="https://img-blog.csdnimg.cn/0b76985eee6946fd99bebf5171a85b32.png" alt="在这里插入图片描述"> 更多命令推荐大佬的文章 
