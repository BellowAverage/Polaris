
--- 
title:  朋友欠钱老拖着不给？这个Python小工具让他立马还钱！ 
tags: []
categories: [] 

---
相信大家身边都有遇到过欠钱你不问他要，他就会忘记给，最近我一个朋友就借了我一些钱，一个多月了还没给我，不知道他是不是忘记这回事了，所以我决定做个一个小工具，来提醒他记得要还钱！（建议收藏，指不定哪天用得到呢）

<img src="https://img-blog.csdnimg.cn/img_convert/cedb94163e7e61d227629d2606ce60f7.png" height="533" width="976">

## 工具

这里用到了PIP工具，Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。

pip 是一个现代的，通用的 Python 包管理工具。提供了对 Python 包的查找、下载、安装、卸载的功能。

<img src="https://img-blog.csdnimg.cn/img_convert/fdd0873e89fd0689149c3f096ed770e1.png" height="346" width="732">

## 源码

```
import win32api,win32con,time


from apscheduler.schedulers.blocking import BlockingScheduler


def DrunkWater():


    win32api.MessageBox(0, "你的欠款已逾期，为了不影响朋友间的感情，请尽快结清！", "还钱小助手",win32con.MB_OK)


# BlockingScheduler


scheduler = BlockingScheduler()


scheduler.add_job(DrunkWater, 'interval', minutes=1)


if __name__ == '__main__':


    while True:


        scheduler.start()


        time.sleep(1)

```

## 效果

这里我们设置半 个小时提醒一次。

<img src="https://img-blog.csdnimg.cn/img_convert/327e5fa107e3795a4c64c0197aaac2f3.png" height="274" width="378"> 

## 可执行文件

打包工具选择：pyinstaller  弹窗提醒选择：pywin3

## 安装 pyinstaller &amp; pywin32

pip install pyinstaller

pip install pywin32

## 打包命令

直接在 py 文件所在路径下执行：pyinstaller -F -w demp.py即可。

-F：意为将代码打包成一个独立的可执行文件。-w：意为以 noconsole 模式运行，即没有 cmd 黑框。

## 结果

<img src="https://img-blog.csdnimg.cn/img_convert/478c94ef1c4b937095a69103b718f782.png" height="220" width="222">

到这我们就可以大功告成了，如上图，`dist` 中的文件就是我们打包后的可执行文件，其能够实现和 `demo.py` 一样的功能。 

## 结语

如果小伙伴以后遇到这种情况，别忘记了还有这种应对方式，感谢您的阅读，如果有喜欢我的文章的小伙伴可以**点赞**、**在看**哦！我会不断的努力更新更优质的内容！

### 

### 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

https://blog.csdn.net/m0_60173255/article/details/119110877

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/5ae97459cfa02de46416bc71255a25ac.gif">

微信扫码关注，了解更多内容
