
--- 
title:  python mp3获取帧率，总时长 
tags: []
categories: [] 

---


### python mp3获取帧率，总时长



方法1

```
from pydub import AudioSegment

if __name__ == '__main__':
    mp3_file_path = r"E:\20240326\output\airuhuo_T4_w\airuhuo_T4_w.MP3"
    wav_file_path = r"E:\20240326\output\airuhuo_T4_w\airuhuo.wav"

    # 加载 MP3 文件
    audio = AudioSegment.from_mp3(mp3_file_path)

    # 导出为 WAV 格式
    audio.export(wav_file_path, format='wav')

    frame_rate = audio.frame_rate
    print("帧率（采样率）:", frame_rate, "Hz")

    # 获取总时长（以毫秒为单位）
    duration_ms = len(audio)
    print("总时长:", duration_ms, "毫秒")

    # 如果需要以秒为单位的时长，可以进行转换
    duration_seconds = duration_ms / 1000.0
    print("总时长:", duration_seconds, "秒")

```



方法2

```
from mutagen.mp3 import MP3
from pydub import AudioSegment

if __name__ == '__main__':
    mp3_file_path = r"E:\20240326\output\airuhuo_T4_w\airuhuo_T4_w.MP3"
    wav_file_path = r"E:\20240326\output\airuhuo_T4_w\airuhuo.wav"

    # 加载 MP3 文件
    audio = AudioSegment.from_mp3(mp3_file_path)

    # 导出为 WAV 格式
    audio.export(wav_file_path, format='wav')


    # 定义 MP3 文件的路径


    # 加载 MP3 文件
    audio = MP3(mp3_file_path)

    # 获取时长（以秒为单位）
    duration = audio.info.length
    print(f"时长: {duration} 秒")

    # 获取比特率（以 kbps 为单位）
    bitrate = audio.info.bitrate / 1000
    print(f"比特率: {bitrate} kbps")

    # 计算帧数
    # MP3 文件的帧长度通常为 26 毫秒
    # 这个值可能因编码方式的不同而有所变化
    frame_length_ms = 26
    frame_count = duration * 1000 / frame_length_ms
    print(f"帧数: {int(frame_count)} 帧")
```


