
--- 
title:  VLFeat、pydot配置 
tags: []
categories: [] 

---


#### 文章目录
- - 


## VLFeat配置

下载地址：http://www.vlfeat.org/download/ 建议下载此版本 <img src="https://img-blog.csdnimg.cn/20190316132347278." alt="在这里插入图片描述"> 最新的版本对sift处理中的X.sift文件为空的情况下会报错。

下载好后解压 方法一： 将所在文件配置到环境变量Path中 D:\Program Files (x86)\VLFeat\vlfeat-0.9.20-bin\vlfeat-0.9.20\bin\win64 <img src="https://img-blog.csdnimg.cn/20190316132559364.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 方法二： 将文件所在位置中的（我是D:\Program Files (x86)\VLFeat\vlfeat-0.9.20-bin\vlfeat-0.9.20\bin\win64) sift.exe和vl.dll 拷到运行所在目录下面，亲测可用

## pydot配置

根据网上经验帖：https://blog.csdn.net/sinat_37998852/article/details/80507536?utm_source=blogxgwz2 PS：参考博客中的每一步基本上我都有做

**安装顺序：** graphviz-&gt;grapphviz软件本身-&gt;pydot 首先要在python中安装graphviz：pip install graphviz； 然后下载graphviz这个软件，直接下载镜像文件安装就好，要记得安装路径，并将路径添加到系统path中； grapphviz软件下载地址：http://www.graphviz.org/download/ https://graphviz.gitlab.io/_pages/Download/Download_windows.html <img src="https://img-blog.csdnimg.cn/20190316134957232." alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190316134004608.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 最后，pip install pydot

python库文件 https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml 但是只有和pyrhon27 匹配的 pygraphviz cp27

因此，直接下载 pygraphviz-1.5.zip 下载地址https://pypi.org/project/pygraphviz/#files 解压后放到运行文件的根目录下 （但这步好像不是很必要，运行时好像没有调用到这个包）

pip install pydot

最后成功运行（哪些步骤是关键的我也不是很清楚，但是都做好后可以使用）

**测试代码**

```
import pydot

g = pydot.Dot(graph_type='graph')

g.add_node(pydot.Node(str(0), fontcolor='transparent'))
for i in range(5):
  g.add_node(pydot.Node(str(i + 1)))
  g.add_edge(pydot.Edge(str(0), str(i + 1)))
  for j in range(5):
    g.add_node(pydot.Node(str(j + 1) + '0' + str(i + 1)))
    g.add_edge(pydot.Edge(str(j + 1) + '0' + str(i + 1), str(j + 1)))
g.write_png('../images/ch02/ch02_fig2-9_graph.png', prog='neato')

```

生成图片 <img src="https://img-blog.csdnimg.cn/20190316134813721.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> ps whl下载地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/

<img src="https://img-blog.csdnimg.cn/2019033122572095." alt="在这里插入图片描述">谢谢观看。
