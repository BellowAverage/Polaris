
--- 
title:  吊打jd_seckill，Go语言版免配置抢茅台程序，实力接盘~ 
tags: []
categories: [] 

---
大家好，我是明哥。

在12月29日那天，我发布了一篇文章『』，介绍了一个非常热门的开源项目 `jd_seckill`，利用这个脚本项目可以实现在京东上自动预约，自动抢茅台。只要抢到一瓶，就可以净赚将近 1000 块钱，真的是天上掉钱的事儿，这波用一句话来说就是，技术造福人类啊~

这个项目连续几天登上了 Github 的榜首，短短几天时间收获了8000多的star，简直火得一塌糊涂。可惜好景不长，就在昨天，作者 `红头土豆` 就收到了京东安全的警告邮件，在重重的压力之下，红头土豆最后一次更新仓库，发表删库声明，并删除了 master 分支。

<img src="https://img-blog.csdnimg.cn/img_convert/c8a34e341280ccd92a61eb5b57e18df6.png" alt="">

`红头土豆` 的 `jd_seckill` 是基于 Python 编写的，整个流程操作下来呢，分为如下几步：
1. 安装 Python3 并下载源码1. 从 requirements.txt 里安装项目依赖包1. 手动打开PC端 京东商城，下单后获取 eid 和 fp 参数，填入配置文件 config.ini1. 修改抢购时间，一定要是未来的时间。1. 执行 `python main.py` 然后输入 1，进行预约1. 执行 `python main.py` 然后输入 2，进行抢购
从这个流程来看，有非常多需要人工来操作的步骤来搭建脚本的运行环境，在我那篇文章火了后，有上百个人添加我的微信来问我如何搭建环境之类的基础问题，对于毫无编程经验的纯小白来说，要想使用这个脚本是有很大的门槛的。

如果从产品的角度来看，这个项目的改进空间非常大。

说巧不巧，前脚 `jd_seckill` 刚被叫停正式下架，后面就有一个使用 `Golang` 编写的抢茅台项目 `mtSeckill` 又站了起来（https://github.com/zqjzqj/mtSecKill）。

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-xToO0c7n-1610068170640)(http://image.iswbm.com/image-20210107221409507.png)]

我试着把这个 `mtSeckill` 项目编译了下，跑了起来，发现之前的 `jd_seckill` 的体验真的是一言难尽啊，整个过程无比流畅。

你只要执行下面这条命令

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-v9fGzzgk-1610068170642)(http://image.iswbm.com/image-20210107214318091.png)]

其中的参数非常的直观
- **sku**：你抢购的端口的 sku_id，下面这个id是茅台的- **num**：抢购数量，茅台最多 2瓶，设置为2- **works**：开启多少个浏览器窗口抢购- **time**：抢购时间，注意不是日期，而是时间，时间会自动取未来最近一天的时间。
执行完成后就会自动打开一个 chrome 浏览器，访问京东并让你扫码登陆。

<img src="https://img-blog.csdnimg.cn/img_convert/0d9f1d0f8ebf6735c51b538dccb0d75a.png" alt="">

登陆之后，程序会自动感知，去获取 eid 和 fp 参数，注意这个过程是完全自动的，不像之前 `jd_seckill` 需要手动获取，真的是太贴心了。

<img src="https://img-blog.csdnimg.cn/img_convert/6c3e75415778651c2543c153356bb646.png" alt="">

获取到 eid 和 fp 后，就会自动打开 6 个窗口（就是你之前传入的 work 参数）等待抢购时间的到达~

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-9Ui2Xtnx-1610068170652)(http://image.iswbm.com/image-20210107214616168.png)]

是不是非常的简单而且流畅？这体验，完全吊打之前的 `jd_seckill` ，只要某个懂点 Go 的程序员把项目编译成可执行文件，就算是一个完全不懂编程的小白，也可以直接使用，简单太方便了。

我已经将整个项目编译好了，并打包在一起，有 Windows 版本的，也有 Mac 版本的，如果你想在抢两瓶茅台回家过个好年，可以直接点这个链接直接下载使用：https://wws.lanzous.com/iSHCXk5e1mh

<img src="https://img-blog.csdnimg.cn/img_convert/86aaade31990346afb68fdbf2da65f3e.png" alt="">

即便操作过是如此简单，为了照顾纯小白，有两点我需要额外说明下（免得一直有人问）：
1. 无论你使用 win 还是 mac，电脑都需要有安装chrome浏览器1. 若是 win 用户，直接双击 exe 文件即可1. 若是mac用户，下载后需到终端执行该条命令赋予执行权限 `chmod +x mtSeckill.mac` ，然后再执行命令 `./mtSeckill.mac` 运行。