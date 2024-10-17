
--- 
title:  SSL_connect returned=1 errno=0 state=error: certificate verify failed 
tags: []
categories: [] 

---
### 起因

起因是这样的，我昨天使用 gem 安装 irb 的时候出现了下面这个错误：

```
[root@master ~]# gem install irb
ERROR:  Could not find a valid gem 'irb' (&gt;= 0), here is why:
          Unable to download data from https://rubygems.org/ - SSL_connect returned=1 errno=0 state=error: certificate verify failed (https://api.rubygems.org/specs.4.8.gz)

```

其实 ruby 安装后是自带 irb 的，但是为什么还要安装 irb 呢？主要是旧版 irb 太拉跨了，退出以后再进入的话，历史记录都没有了，只有一些基本的功能。新版的 irb 就酷炫很多了，自动提示之类的用起来很方便。原因明确了，所以修复目标也就很明确了！

### 下载证书

可以使用 wget 下载或者直接在网页下载

```
https://curl.se/ca/cacert.pem
```

有时候由于 great wall 的原因，可能下载不下来，所以我下载后放到云盘了：

链接：https://pan.baidu.com/s/1XwOsh9去掉我V7Hd3gzn8x0F2YJA?pwd=mhmx  提取码：mhmx 

### 设置环境变量

```
[root@master ~]# vim /etc/profile
export SSL_CERT_FILE=/root/cacert.pem

[root@master ~]# source /etc/profile
```

### 再次安装

没有设置国内镜像的话可能会比较慢

```
[root@master ~]# gem install irb
Successfully installed irb-1.4.1
Parsing documentation for irb-1.4.1
Done installing documentation for irb after 0 seconds
1 gem installed

```

### 新版展示

```
root@master ~]# irb
irb(main):001:0&gt; a = [1, 2, 3]
=&gt; [1, 2, 3]
irb(main):002:0&gt; a.f
                 a.fetch                            
                 a.filter!                          
                 a.fill                             
                 a.flatten                          
                 a.flatten!                         
                 a.find_index                       
                 a.filter                           
                 a.first                            
                 a.find                             
                 a.find_all                         
                 a.filter_map                       
                 a.flat_map                         
                 a.frozen?                          
                 a.freeze        
```

<img alt="" height="286" src="https://img-blog.csdnimg.cn/a73362b7abe9493bb572a4cf4d0f1b0b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_14,color_FFFFFF,t_70,g_se,x_16" width="440">


