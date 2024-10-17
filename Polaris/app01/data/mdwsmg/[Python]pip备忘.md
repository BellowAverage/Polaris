
--- 
title:  [Python]pip备忘 
tags: []
categories: [] 

---


#### pip初始化备忘
- - - <ul><li>- 


## 1、 查看当前pip版本

pip为python带的，安装的时候一直next应该就有，安装记得点add path

```
pip --version

```

## 2、常规安装命令

后面-i -t不指定则为默认源与默认安装位置

```
pip install &lt;package_name&gt; -i &lt;index_url&gt; -t &lt;target_dir&gt;

```

```
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple -t /home/user/myproject

```

### 2.1、查看修改pip源

查看当前源

```
pip config get global.index-url

```

查看源列表

```
pip config list

```

添加、修改源。这个可以配置文件，也可以命令行，命令行如下：

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

```

国内源推荐如下：

```
pypi 清华大学源：https://pypi.tuna.tsinghua.edu.cn/simple
pypi 腾讯源：http://mirrors.cloud.tencent.com/pypi/simple
pypi 阿里源：https://mirrors.aliyun.com/pypi/simple/
pypi 豆瓣源 ：http://pypi.douban.com/simple/

```

### 2.1、修改pip默认安装地址

关于怎么修改pip默认安装地址，网上说法太多且不一样了，所以才写的这个。 python安装好后，在lib目录下有site.py文件，里面可以指定默认安装地址。 找到大概87~88行的位置，修改下面两项

```
USER_SITE = "F:\ProgrammingLanguages\Python\Lib\site-packages"
USER_BASE = "F:\ProgrammingLanguages\Python\Scripts"

```

查看当前pip安装地址配置

```
python -m site

```
