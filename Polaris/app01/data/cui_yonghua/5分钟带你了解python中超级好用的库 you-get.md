
--- 
title:  5分钟带你了解python中超级好用的库 you-get 
tags: []
categories: [] 

---
#### 一. you-get概述

you-get是一个小型的命令行实用程序，用于从Web下载媒体内容（视频，音频，图像）。

官方网址：

源码地址：

命令行安装：`pip3 install you-get` (需要先按照python环境)

更新：`pip install --upgrade you-get`

#### 二. you-get主要参数

选项和说明 **`-i`**： 显示资源信息，比如说格式、清晰度、大小等（常用）； **`-c`**： 使用cookie，加载cookies.txt 或者cookies.sqlite。即下载会员资源需要会员的信息（常用）； **`-o`**：设置输出文件夹，即保存路径，若不指定，则保存在当前工作目录（常用）； **`-u`**： 指定下载或查看的url，有时候可以省略-u直接加上url； **`-O`**： 设置文件名，可采用默认文件名 **`-f`**： 强制覆盖已存在的文件 **`-l`**： 优先下载整个列表 **`-P`**： 使用密码（若访问视频需要密码） **`-t`**： 设置超时时间，单位是秒

#### 三. you-get命令用法

```
# 最简单的下载
you-get '视频链接' 

# # 列出视频信息，可以看到该网页提供的视频的信息
you-get -i '视频链接'

# 下载指定质量的视频，国内网站一般默认就是最高清的，但是国外的还有更高清的
you-get --itag=127 '视频链接'   

# 设置http代理
you-get -x 127.0.0.1:8118 '视频链接'   

```

#### 四. python代码中使用

python3代码中简单使用：

```
# -*- encoding: utf-8 -*-
# 可以获取到各个网站的下载器
from you_get.extractor import download_urls

url_list = ['https://www.bilibili.com/video/BV1sf4y1x7MS?spm_id_from=333.999.0.0&amp;vd_source=2b9d1ec775e1a5ff6537f2f5ec814470']
resp = download_urls(urls=url_list, title='myvideo', ext='mp4', total_size=0)

```

#### 五. 附：截至目前you-get支持下载的网站

<th align="center">Site</th><th align="left">URL</th><th align="center">Videos?</th><th align="center">Images?</th><th align="center">Audios?</th>
|------
<td align="center">**YouTube**</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**Twitter**</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">VK</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">Vine</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Vimeo</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Veoh</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**Tumblr**</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td>
<td align="center">TED</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">SoundCloud</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">SHOWROOM</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Pinterest</td><td align="left"></td><td align="center"></td><td align="center">✓</td><td align="center"></td>
<td align="center">MTV81</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Mixcloud</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">Metacafe</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Magisto</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Khan Academy</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Internet Archive</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**Instagram**</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">InfoQ</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Imgur</td><td align="left"></td><td align="center"></td><td align="center">✓</td><td align="center"></td>
<td align="center">Heavy Music Archive</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">Freesound</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">Flickr</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">FC2 Video</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Facebook</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">eHow</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Dailymotion</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Coub</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">CBS</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Bandcamp</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">AliveThai</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">interest.me</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**755ナナゴーゴー**</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">**niconicoニコニコ動画**</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**163网易视频网易云音乐**</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center">✓</td>
<td align="center">56网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**AcFun**</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**Baidu百度贴吧**</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">爆米花网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**bilibili哔哩哔哩**</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center">✓</td>
<td align="center">豆瓣</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center">✓</td>
<td align="center">斗鱼</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">凤凰视频</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">风行网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">iQIYI爱奇艺</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">激动网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">酷6网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">酷狗音乐</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">酷我音乐</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">乐视网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">荔枝FM</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">懒人听书</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">秒拍</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">MioMio弹幕网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">MissEvan猫耳FM</td><td align="left"></td><td align="center"></td><td align="center"></td><td align="center">✓</td>
<td align="center">痞客邦</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">PPTV聚力</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">齐鲁网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">QQ腾讯视频</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">企鹅直播</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Sina新浪视频微博秒拍视频</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Sohu搜狐视频</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**Tudou土豆**</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">阳光卫视</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">**Youku优酷**</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">战旗TV</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">央视网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">Naver네이버</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">芒果TV</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">火猫TV</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">阳光宽频网</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">西瓜视频</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">新片场</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">快手</td><td align="left"></td><td align="center">✓</td><td align="center">✓</td><td align="center"></td>
<td align="center">抖音</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">TikTok</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">中国体育(TV)</td><td align="left"> </td><td align="center">✓</td><td align="center"></td><td align="center"></td>
<td align="center">知乎</td><td align="left"></td><td align="center">✓</td><td align="center"></td><td align="center"></td>

就像you-get所说的，侵权问题与本人无关，怎么用是你自己的事。

觉得该工具有用的话，可以收藏起来哦
