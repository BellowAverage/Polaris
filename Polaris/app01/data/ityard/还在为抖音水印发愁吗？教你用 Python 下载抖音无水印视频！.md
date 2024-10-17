
--- 
title:  还在为抖音水印发愁吗？教你用 Python 下载抖音无水印视频！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200607071939216.jpg#pic_center" alt="" width="800"> 说起抖音，大家或多或少应该都接触过，如果大家在上面下载过视频，一定知道我们下载的视频是带有水印的，那么我们有什么方式下载不带水印的视频呢？其实用 Python 就可以做到，下面我们来看一下。

首先，我们打开抖音随意找一个视频，如下图所示： <img src="https://img-blog.csdnimg.cn/20200607072019744.PNG" alt=""> 然后点击分享按钮，找到复制链接选项，如下图所示： <img src="https://img-blog.csdnimg.cn/20200607072037241.PNG" alt=""> 接着，我们点击按钮复制链接，比如我复制的链接为：`https://v.douyin.com/JePfx5f/`，然后我们将链接复制到谷歌浏览器上，按 F12 打开开发者工具，再切换到移动设备，选择 Network，如下图所示： <img src="https://img-blog.csdnimg.cn/20200607072051388.PNG" alt=""> 我们接着按回车键进行访问，然后在 Filter 中输入 item，进而我们可以找到 item_ids 和 dykt，如下图所示： <img src="https://img-blog.csdnimg.cn/20200607072102665.PNG" alt=""> 再切换到 Preview，我们可以发现有一个 play_addr，如下图所示： <img src="https://img-blog.csdnimg.cn/20200607072120627.PNG" alt=""> 我们通过 play_addr 就可以下载无水印视频了。

看一下主要实现代码：

```
share_url = "https://v.douyin.com/JePfx5f/"
# 获取 itemId、dytk
get = requests.get(share_url, headers=headers)
html = get.content
itemId = re.findall(r"(?&lt;=itemId:\s\")\d+", str(html))
dytk = re.findall(r"(?&lt;=dytk:\s\")(.*?)(?=\")", str(html))
# 组装视频长链接
long_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="+itemId[0]+"&amp;dytk="+dytk[0]
# 请求长链接，获取 play_addr
video_open = requests.get(long_url, headers=headers)
vhtml = video_open.text
uri = re.findall(r'(?&lt;=\"uri\":\")\w{32}(?=\")', str(vhtml))
# video_id 是长链接唯一变动的，提取出 uri 进行组装得到最终链接
play_addr = "https://aweme.snssdk.com/aweme/v1/play/?video_id="+uri[0]+\
            "&amp;line=0&amp;ratio=540p&amp;media_type=4&amp;vr_type=0&amp;improve_bitrate=0&amp;is_play_url=1&amp;is_support_h265=0&amp;source=PackSourceEnum_PUBLISH"
# 保存短视频
video = requests.get(url=play_addr, headers=headers)
with open("download.mp4", "wb") as file:
    file.write(video.content)
    file.close()
    print("抖音无水印视频下载完成！")

```

我将下载的视频上传到了百度网盘，我们可以点击看一下，我们可以看到视频中并未有水印，说明我们已经成功的利用 Python 下载了抖音无水印的视频了。

>  
 作者：程序员野客 公号：Python小二 链接： 

