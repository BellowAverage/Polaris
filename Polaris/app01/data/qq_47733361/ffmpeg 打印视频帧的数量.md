
--- 
title:  ffmpeg 打印视频帧的数量 
tags: []
categories: [] 

---
### 命令：

可以使用 ffprobe 工具：

```
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 input.ts

```

上面命令含义为：
- -v error：设置输出日志级别为 error，只输出错误信息。- -count_frames：计算帧数。- -select_streams v:0：选择第一个视频流进行操作。- -show_entries stream=nb_read_frames：显示视频流的已读取帧数。- -of default=nokey=1:noprint_wrappers=1：设置输出格式为不显示键名，不显示外层包装。
这个命令的作用是分析视频文件，并输出已读取帧数，以及可能的错误信息。通过这些信息，可以更好地了解视频文件的特性和内容。

### 结果：

```
[root@storm03 cctv5+3000]# ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 cctv5+_3000kb.ts 
[hevc @ 0x3feefc0] PPS id out of range: 0
    Last message repeated 39 times
[hevc @ 0x3ff1540] Could not find ref with POC 27
[hevc @ 0x3ff1540] Could not find ref with POC 24
29886
29886


```
