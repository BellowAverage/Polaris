
--- 
title:  海康摄像头在线播放(H5+Flash) 
tags: []
categories: [] 

---
 <img alt="" height="430" src="https://img-blog.csdnimg.cn/20201230142718189.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

<img alt="" height="764" src="https://img-blog.csdnimg.cn/2020123014291879.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

一、后端

```
&lt;dependency&gt;
      &lt;groupId&gt;org.bytedeco&lt;/groupId&gt;
      &lt;artifactId&gt;javacv-platform&lt;/artifactId&gt;
      &lt;version&gt;1.4.4&lt;/version&gt;
&lt;/dependency&gt;
```

```
public static void main(String[] args) throws FrameGrabber.Exception, FrameRecorder.Exception, NoSuchFieldException, IllegalAccessException {
        final int captureWidth = 1280;
        final int captureHeight = 720;
        final FFmpegFrameGrabber grabber = new FFmpegFrameGrabber("rtsp://账号:密码@ip:端口");
        grabber.setImageWidth(captureWidth);
        grabber.setImageHeight(captureHeight);
        // rtsp格式一般添加TCP配置，否则丢帧会比较严重
        // Brick在测试过程发现，该参数改成udp可以解决部分电脑出现的下列报警，但是丢帧比较严重
        // av_interleaved_write_frame() error -22 while writing interleaved video packet.
        grabber.setOption("rtsp_transport", "tcp");
        grabber.start();
        // 最后一个参数是AudioChannels，建议通过grabber获取
        final FFmpegFrameRecorder recorder = new FFmpegFrameRecorder("rtmp://127.0.0.1:1935/live", captureWidth, captureHeight, 1);
        recorder.setInterleaved(true);
        // 降低编码延时
        recorder.setVideoOption("tune", "zerolatency");
        // 提升编码速度
        recorder.setVideoOption("preset", "ultrafast");
        // 视频质量参数(详见 https://trac.ffmpeg.org/wiki/Encode/H.264)
        recorder.setVideoOption("crf", "28");
        // 分辨率
        recorder.setVideoBitrate(2000000);
        // 视频编码格式
        recorder.setVideoCodec(avcodec.AV_CODEC_ID_H264);
        // 视频格式
        recorder.setFormat("flv");
        // 视频帧率
        recorder.setFrameRate(15);
        recorder.setGopSize(60);
        recorder.setAudioOption("crf", "0");
        recorder.setAudioQuality(0);
        recorder.setAudioBitrate(192000);
        recorder.setSampleRate(44100);
        // 建议从grabber获取AudioChannels
        recorder.setAudioChannels(1);
        recorder.setAudioCodec(avcodec.AV_CODEC_ID_AAC);
        recorder.start();

        // 解决音视频同步导致的延时问题
        Field field = recorder.getClass().getDeclaredField("oc");
        field.setAccessible(true);
        avformat.AVFormatContext oc = (avformat.AVFormatContext) field.get(recorder);
        oc.max_interleave_delta(100);

        // 用来测试的frame窗口
        final CanvasFrame cFrame = new CanvasFrame("frame");
        Frame capturedFrame = null;

        // 有些时候，程序执行回报下列错误，添加一行代码解决此问题
        // av_interleaved_write_frame() error -22 while writing interleaved video packet.
        grabber.flush();

        while ((capturedFrame = grabber.grab()) != null) {
            if (cFrame.isVisible()) {
                cFrame.showImage(capturedFrame);
            }
            System.out.println(grabber.getFrameNumber() + "--" + capturedFrame.timestamp);
            recorder.setTimestamp(capturedFrame.timestamp);
            recorder.record(capturedFrame);
        }
        cFrame.dispose();
        recorder.close();
        grabber.close();

    }
```

 

 

二、前端

>  
  

