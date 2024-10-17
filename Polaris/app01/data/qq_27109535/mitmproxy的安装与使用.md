
--- 
title:  mitmproxy的安装与使用 
tags: []
categories: [] 

---
### mitmproxy的安装与使用

查看 Windows IP 地址

```
ipconfig

```

windows下面是不支持mitmproxy的，但是安装mitmproxy的时候回同时安装3个库，分别是：mitmproxy、mitmdump、mitmweb。 

mitmproxy有三种启动命令： (1) mitmweb – 提供一个web界面； – 代理端口：绑定了 *:8080作为代理端口； – 交互界面地址：localhost:8081； (2) mitmproxy – 提供命令行界面； – 可以通过命令过滤请求； (3) mitmdump – 【TODO】 和python交互

### 1. 安装第三方库

三种安装方法

```
pip install mitmproxy

```

```
pip install mitmproxy==5.0.1

```

```
pip install pipx
pipx install mitmproxy


```

### 2. 设置代理

<img src="https://img-blog.csdnimg.cn/36c558da3558419eadf8b32901dfcc84.png" alt="在这里插入图片描述">

chrome设置代理（omega） <img src="https://img-blog.csdnimg.cn/99e13b6ce09f4df9ab061b6c6bb3ea6e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ae8fad5fc0a04da89e2a89e02ab46b7e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ab5a0295e41b49c48389dc56934d5e9b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e7ce64fe02eb43ec88697edcea462b7b.png" alt="在这里插入图片描述">

### 3. 安装证书

要抓取https请求，需要安装证书： 方法一： <img src="https://img-blog.csdnimg.cn/bd51a16465d348a885cb94d352ecd237.png" alt="在这里插入图片描述">

方法二 mitmproxy设置浏览器的代理，在浏览器中输入mitm.it，

```
mitm.it

```

2 选择操作系统，会自动下载证书； <img src="https://img-blog.csdnimg.cn/3e712b37b14241f2a0af3f68e9c749c6.png" alt="在这里插入图片描述">

3 双击证书，一直下一步，即可完成安装。

### 4. 应用

mitmproxy 工具有以下三部分组成

mitmproxy -&gt; 命令行工具（win不支持） mitmdump -&gt; 加载 python 脚本 mitmweb -&gt; web 界面工具

#### 1. mitmweb

命令行执行mitmweb -p 9999，-p可指定端口

```


```

```
mitmweb -p 9999

```

<img src="https://img-blog.csdnimg.cn/1e60a0b1162848a787ad7fbf512f356a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b2ed3bf9a4bc4ec78473ff32768902a1.png" alt="在这里插入图片描述">

```



```

<img src="https://img-blog.csdnimg.cn/1ecf604e79a140e783402c21d57c6347.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ae51b374f8a148cba1f827e5b8e11b26.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f8d6a1ee7c684bdb9538cfbb521a2a8e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4985b95bdd6148f98ae101348fa27458.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f31961041a384d7d9c978ad2ae763c9b.png" alt="在这里插入图片描述">

#### 2. mitmdump

```
录制与回放

录制：mitmdump -w 文件名
过滤：mitmdump -nr 文件名 -w 文件名2 “~s hogwarts”
回放：mitmdump -nC 文件名

```

参数

```
-s “script.py --bar” # 执行脚本，通过双引号来添加参数
-n 不启动代理
-r 读取文件内容
-w 写入文件
~s 过滤响应数据
~q 过滤请求数据

```

更多参数见：https://docs.mitmproxy.org/stable/concepts-filters/ 例1：监听9999端口，并录制请求数据，保存到baidu.txt文件

```
mitmdump -p 9999 -w baidu.txt

```

打开百度搜索，依次搜索mitmproxy、mitmweb、mitmdump，然后结束录制。录制结束后，会在当前目录下生成二进制录制文件baudu.txt 例2：过滤上面录制的请求，只保存搜索mitmdump的数据

```
mitmdump -nr baidu.txt -w mitmdump.txt "~s mitmdump"

```

回放mitmdump.txt 文件接口.

```
mitmdump -nC mitmdump.txt


```

#### 3. mitmdump

```
mitmdump -p [端口号] -s python脚本
 
例：
mitmdump -p 8889

```

### 5. mitmproxy常用命令

```
1、搜索返回不是200的请求
!(~c 200)

2、POST请求+URL里包含baidu.com的数据包
~m post ~u baidu.com
~m post &amp; ~u baidu.com

3、拦截百度的GET包
~d baidu.com ~m get
~d baidu.com &amp; ~m get

4、拦截baidu.com包
~d baidu.com
``


```
