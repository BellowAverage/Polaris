
--- 
title:  使用 cflow 静态分析 C 语言并生成函数调用关系 
tags: []
categories: [] 

---
### cflow 安装

cflow 是一款静态分析 C 语言代码的工具，通过它可以生成函数的调用关系，并输出各种函数之间的依赖关系图。源码安装的方式都差不多，就不多说了。

```
wget https://ftp.gnu.org/gnu/cflow/cflow-1.6.tar.gz
```

源码安装：

### cflow 使用

随便拿一个 .c 文件来测试。

```
root@master ~/mysql# cflow -T -m main ./mysql-5.7.21/cmd-line-utils/libedit/np/fgetln.c &gt; main.txt

root@master ~/mysql# vim main.txt
+-main() &lt;int main (int argc, char *argv[]) at ./mysql-5.7.21/cmd-line-utils/libedit/np/fgetln.c:97&gt;
  +-fgetln() &lt;char *fgetln (FILE *fp, size_t *len) at ./mysql-5.7.21/cmd-line-utils/libedit/np/fgetln.c:49&gt;
  | +-malloc()
  | +-fgets()
  | +-strchr()
  | +-realloc()
  | +-free()
  | \-strlen()
  +-printf()
  \-free()
```

### tree2dotx 下载

```
wget https://github.com/tinyclub/linux-0.11-lab/blob/master/tools/tree2dotx
or
wget https://raw.githubusercontent.com/tinyclub/linux-0.11-lab/master/tools/tree2dotx
```

有可能用 wget 会直接下载不下来，不过目前可以从网页打开链接，将文件内容拷贝下来。

<img alt="" height="681" src="https://img-blog.csdnimg.cn/2021081716580691.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1184">

然后再对文件添加上可执行权限以后就可以直接用了： 

```
root@master ~/mysql# vim tree2dotx
root@master ~/mysql# chmod a+x tree2dotx
root@master ~/mysql# ll tree2dotx 
-rwxr-xr-x. 1 root root 6.0K Aug 17 15:43 tree2dotx*
root@master ~/mysql# cat main.txt | ./tree2dotx &gt; main.dot

root@master ~/mysql# vim main.dot
digraph G{
    rankdir=LR;
    size="1920,1080";
    node [fontsize=16,fontcolor=blue,style=filled,fillcolor=Wheat,shape=box];
    "main" -&gt; "fgetln ";
    "fgetln " -&gt; "malloc";
    "fgetln " -&gt; "fgets";
    "fgetln " -&gt; "strchr";
    "fgetln " -&gt; "realloc";
    "fgetln " -&gt; "free";
    "fgetln " -&gt; "strlen";
    "main" -&gt; "printf";
    "main" -&gt; "free";
}
```

### graphviz 安装

redhat 系统的话可以直接用 yum 进行安装。

```
root@master ~/mysql# yum install graphviz
```

安装好以后就可以直接使用了。 

```
root@master ~/mysql# dot -Tpng main.dot -q3 -o main.png
```

### 生成图片

                                                                         <img alt="" height="427" src="https://img-blog.csdnimg.cn/20210817170707753.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="341">

所以，在相关软件都安装好的情况下，主要就下面这三步就可以生成 .c 文件的调用关系图了。

```
cflow -T -m main fgetln.c &gt; main.txt
cat main.txt | ./tree2dotx &gt; main.dot
dot -Tpng main.dot -q3 -o main.png

```

当然，它还可以生成更复杂的关系图，可以先见识一下它的威力。

 <img alt="" height="1200" src="https://img-blog.csdnimg.cn/20210817172506592.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1200">


