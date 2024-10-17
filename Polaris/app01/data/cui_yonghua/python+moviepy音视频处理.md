
--- 
title:  python+moviepy音视频处理 
tags: []
categories: [] 

---
### 一. moviepy概述

中文网站：

官网：

github地址：

安装方式：`pip install moviepy`

其中： moviepy.editor模块类

>  
 <mark>VideoFileClip</mark>：最常用的视频剪辑类, 用于导入视频文件(mp4、avi等格式皆可) <mark>ImageClip</mark>：常用的剪辑类, 用于导入图片文件(png、jpg等格式皆可) <mark>ColorClip</mark>：ImageClip的子类，比较少用, 可以把它当作是单一颜色的图片 <mark>TextClip</mark>：常用的剪辑类, 文字剪辑, 常用于给视频加字幕、水印、标题等 <mark>CompositeVideoClip</mark>：最常用剪辑类, 组合剪辑, 用于组合以上各种视频剪辑类CompositeVideoClip().to_videofile(‘file_name’) <mark>AudioClip</mark>:最常用音频剪辑类, 与VideoFileClip类似, 用于导入音频文件(mp3, m4a等) <mark>CompositeAudioClip</mark>:与CompositeVideoClip类似, 是最常用的音频组合剪辑类 


### 二. 视频处理

#### 2.1 视频加载和输出

1、视频加载：调用`VideoFileClip(文件名)`即可将视频加载进来，可以支持不同格式的视频文件。VideoFileClip类的构造函数参数如下：

filename：视频文件名，一般常见格式都支持； has_mask：是否包含遮罩； audio：是否加载音频； audio_buffersize：音频缓冲区大小； target_resolution：加载后需要变换到的分辨率； resize_algorithm：调整分辨率的算法，默认是 bicubic，可以设置为 bilinear，fast_bilinear； audio_fps：声音的采样频率； audio_nbytes：采样的位数； verbose：是否输出处理信息。

2、视频输出：write_videofile或to_videofile方法用于视频输出，可以将处理之后的视频写入本地。

#### 2.2 视频转换gif

```
from moviepy.editor import VideoFileClip
clip = VideoFileClip('./21.mp4')
clip.write_gif('21.gif')
# fps设置每秒的帧数，这将直接影响gif文件的大小(帧数越小，文件越小)，不设置的时候，默认取视频的原帧数
# clip.write_gif('21.gif', fps=1)  

```

gif缩放：视频分辨率往往比较高，直接转化为Gif，比较大，不利于网络传播，所以可以使用resize，来进行缩放

```
clip = (VideoFileClip("21.mp4").subclip(1, 3).resize(0.5))  # 宽度和高度乘以0.1
clip.write_gif("Video.gif")

```

#### 2.3 视频裁剪

用 subclip 这个方法就可以实现视频的截取，添加参数传入起始时间和结束时间即可截取视频中的指定部分。subclip(t_start,t_end) 方法中的时间参数：

t_start默认为开始0秒，t_end 的默认值就是视频的长度(最后时间)，可支持负数，表示结束前N时间点 以秒表示： (t_start=10) 表示从开始时间的10s开始裁剪到最后。 以分秒表示： (t_start=(1,20)) 表示从开始时间的1分20秒开始裁剪到最后。 以时分秒表示： (t_start=(1,1,20)) 或者 (t_start=(01:01:20))表示从开始时间的1小时1分20秒开始裁剪到最后

```
clip = VideoFileClip(video_path)
video_clip = clip.subclip
```
