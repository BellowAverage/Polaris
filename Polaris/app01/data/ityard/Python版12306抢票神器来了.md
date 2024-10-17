
--- 
title:  Python版12306抢票神器来了 
tags: []
categories: [] 

---
项目：testerSunshine，智能刷票&amp;订票

耗费时长：不详

难易度：10



环境准备

Python 3.6 - 3.7.4



实现步骤

**项目依****赖库：**

验证码目前可以本地识别，需要下载模型，放于项目根目录，感兴趣的可以点击下方卡片在公众号**Python小二**后台回复**12306**领取

自托管云打码服务器搭建：12306_code_server如果大家有空闲的服务器，可搭建之后在这个 issues 里面填入自己的服务器（请注意服务器安全！)项目依赖 requirements.txt

**安装方法<strong>：**</strong>

```
x:root用户(避免多python环境产生问题): pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
非root用户（避免安装和运行时使用了不同环境）: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

许多windows的用户装不了tensorflow的话，可以适当降低版本或者升高版本都是可以的
- tensorflow的兼容版本 1.14.0rc\1.14.0rc\1.15.0\1.15.0rc 以上版本都测试无问题  - 如果pip代理的清华源无法下载，可以更换其他源解决此问题
**服务器启动:**

修改配置文件，可以配置邮箱,配置邮箱的格式在配置里面可以看到ex，配置配置文件的时候，需注意空格和遵循python语法格式

```
# 测试邮箱和server酱是否可用， server酱测试的前提是server酱开关开启
# 可以配置server酱提醒（推荐）[配置教程](https://www.jianshu.com/p/8d10b5b9c4e3)
# 用python3 还是python 完全取决于安装的时候配置的环境变量是否为python3,以下启动默认环境变量为python3
python3 run.py t
```

启动前请先筛选cdn，这点很重要
- <pre class="has">`python3 run.py c`</pre>
启动服务
- <pre class="has">`python3 run.py r`</pre>
如果你不知道如何操作，下面的命令可能会帮助你
<li><pre class="has"><code class="language-properties">python3 run.py -h


——————————————————————————
sage: run.py [-h] operate


positional arguments:
  operate     r: 运行抢票程序, c: 过滤cdn, t: 测试邮箱和server酱，server酱</code></pre></li><li>如果你的服务器安装了docker与docker-compose, 那么你可以忽略上面的所有步骤，直接按以下步骤操作，即可开始抢票： 
   <ul>- 开始抢票：`docker-compose up --build -d`- 停止抢票：`docker-compose down`- 查看抢票log: `docker logs --follow ticket`- 请确认你安装的docker版本为18.09及以上: `docker -v`- 请确认你安装的docker-compose版本为1.23.2及以上: `docker-compose -v`- 请根据自己需要修改好配置文件:`TickerConfig.py`- 请修改配置文件`TickerConfig.py`中的变量`AUTO_CODE_TYPE`和`HOST`，`AUTO_CODE_TYPE`改为`3`, HOST改为`"captcha:80"`（这里很重要，这是本地打码服务器的配置）- 前提条件- 运行命令


获取方式

因为涉及到很多说明和特殊步骤，建议跟随项目说明进行查看，否则就算有压缩包也不一定可以成功执行！所以请前往项目源地址进行查看，暂不提供现成压缩包。<img src="https://img-blog.csdnimg.cn/img_convert/eb7c80b822d926bde11c8665b3b28691.webp?x-oss-process=image/format,png" alt="format,png"><img src="https://img-blog.csdnimg.cn/img_convert/8f51f44dffe023026e94a625529d4abe.webp?x-oss-process=image/format,png" alt="format,png"><img src="https://img-blog.csdnimg.cn/img_convert/4091d5bd6b6365b39bf0f43ca0a01766.webp?x-oss-process=image/format,png" alt="format,png"><img src="https://img-blog.csdnimg.cn/img_convert/9735450a34de066061708350a674c3db.webp?x-oss-process=image/format,png" alt="format,png">










