
--- 
title:  tar 命令高频使用方式+详解 
tags: []
categories: [] 

---
将tar压缩文件解压到指定的目录下的命令是：

tar -xvf  压缩文件 -C  /指定目录

例：#tar -xvf openstack_test.tar -C /tmp

说明：把根目录下的openstack_test.tar解压到/tmp下。

扩展资料：

tar命令是Unix/Linux系统中备份文件的可靠方法，几乎可以工作于任何环境中，它的使用权限是所有用户。

解压参数说明：

-x : --extract，--get 解开tar文件。

-v : --verbose 列出每一步处理涉及的文件的信息，只用一个“v”时，仅列出文件名，使用两个“v”时，列出权限、所有者、大小、时间、文件名等信息。

-f : --file [主机名:]文件名 指定要处理的文件名。可以用“-”代表标准输出或标准输入。

-C,--directory DIR   转到指定的目录.

参考来源资料：百度百科-Tar（Linux系统命令）

一、解压.tar.gz格式到指定的目录下：

命令格式为：tar -zxvf 【压缩包文件名.tar.gz】 -C  【路径】/

例如：tar -zxvf japan.tar.gz -C /tmp/

二、解压.tar.bz2格式到指定的目录下：

命令格式：tar -jxvf 【压缩包文件名.tar.bz2】 -C  【路径】/

例如：tar -zxvf japan.tar.bz2 -C /tmp/

三、压缩.tar.gz格式到指定目录下

命令格式：tar -zcvf 【目录】/ 【压缩包文件名.tar.gz】【源文件】

例如：tar -zcvf /tmp/test.tar.gz japan/

注意：一次压缩多个文件直接在源文件后用空格格开即可

四、压缩.tar.bz2格式到指定目录下

命令格式：tar -jcvf 【目录】/ 【压缩包文件名.tar.gz】【源文件】

例如：tar -jcvf /tmp/test.tar.bz2 japan/

注意：一次压缩多个文件直接在源文件后用空格格开即可

扩展资料

每条选项以及命令直接的空格一定要打，Linux严格区分大小写，输入时注意大小写。

tar在Linux上是常用的打包、压缩、加压缩工具，他的参数很多，常用的压缩与解压缩参数有：

-c ：create 建立压缩档案的参数；

-x ： 解压缩压缩档案的参数；

-z ： 是否需要用gzip压缩；

-v： 压缩的过程中显示档案；

-f： 置顶文档名，在f后面立即接文件名，不能再加参数

 Linux下的tar压缩解压缩命令详解 tar

-c: 建立压缩档案 -x：解压 -t：查看内容 -r：向压缩归档文件末尾追加文件 -u：更新原压缩包中的文件

这五个是独立的命令，压缩解压都要用到其中一个，可以和别的命令连用但只能用其中一个。下面的参数是根据需要在压缩或解压档案时可选的。

-z：有gzip属性的 -j：有bz2属性的 -Z：有compress属性的 -v：显示所有过程 -O：将文件解开到标准输出

下面的参数-f是必须的

-f: 使用档案名字，切记，这个参数是最后一个参数，后面只能接档案名。

# tar -cf all.tar *.jpg 这条命令是将所有.jpg的文件打成一个名为all.tar的包。-c是表示产生新的包，-f指定包的文件名。

# tar -rf all.tar *.gif 这条命令是将所有.gif的文件增加到all.tar的包里面去。-r是表示增加文件的意思。

# tar -uf all.tar logo.gif 这条命令是更新原来tar包all.tar中logo.gif文件，-u是表示更新文件的意思。

# tar -tf all.tar 这条命令是列出all.tar包中所有文件，-t是列出文件的意思

# tar -xf all.tar 这条命令是解出all.tar包中所有文件，-t是解开的意思

压缩

tar -cvf jpg.tar *.jpg //将目录里所有jpg文件打包成jpg.tar

tar -czf jpg.tar.gz *.jpg   //将目录里所有jpg文件打包成jpg.tar后，并且将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz

 tar -cjf jpg.tar.bz2 *.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用bzip2压缩，生成一个bzip2压缩过的包，命名为jpg.tar.bz2

tar -cZf jpg.tar.Z *.jpg   //将目录里所有jpg文件打包成jpg.tar后，并且将其用compress压缩，生成一个umcompress压缩过的包，命名为jpg.tar.Z

rar a jpg.rar *.jpg //rar格式的压缩，需要先下载rar for linux

zip jpg.zip *.jpg //zip格式的压缩，需要先下载zip for linux

解压

tar -xvf file.tar //解压 tar包

tar -xzvf file.tar.gz //解压tar.gz

tar -xjvf file.tar.bz2   //解压 tar.bz2

tar -xZvf file.tar.Z   //解压tar.Z

unrar e file.rar //解压rar

unzip file.zip //解压zip

总结

1、*.tar 用 tar -xvf 解压

2、*.gz 用 gzip -d或者gunzip 解压

3、*.tar.gz和*.tgz 用 tar -xzf 解压

4、*.bz2 用 bzip2 -d或者用bunzip2 解压

5、*.tar.bz2用tar -xjf 解压

6、*.Z 用 uncompress 解压

7、*.tar.Z 用tar -xZf 解压

8、*.rar 用 unrar e解压

9、*.zip 用 unzip 解压
