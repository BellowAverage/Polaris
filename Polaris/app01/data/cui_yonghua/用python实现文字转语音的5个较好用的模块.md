
--- 
title:  用python实现文字转语音的5个较好用的模块 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- - <ul><li>- - 


### 一. 用 gtts 模块

**参考文档**：

使用前需要先安装：`pip3 install gtts` ，样例如下：

```
# -*- encoding: utf-8 -*-
from gtts import gTTS

text = """
从前，有一座美丽的大森林，森林里住着许多小动物，它们每天过着无忧无虑的生活。有一天，森林里来了几个伐木工人，
他们拿着斧头和锯子，把一棵棵树给砍倒了。几天下来，裸露的土地不断扩大，森林里的树木不断减少。大象看了之后非常生气，
他和几个好朋友决定把这些伐木工人抓起来，送到动物法庭上。第二天，大象他们就把伐木工人给抓了起来，送到了动物法庭上。
许多旁观者都纷纷议论起来，猴法官说：“安静，安静，大象你们把这些人抓来是怎么回事?”大象说：“这些人乱砍树木，破坏我们的家园。
大象的好朋友小猴说：“对呀，他们把树给砍光了，我们就不能在树上荡秋千了。”小鸟也说：”猴法官，要是没有树木，我们就不能筑巢了。
长颈鹿说：“要是没有树木，我们就吃不到树叶了，我们会饿死的。”听到这里，猴法官对伐木工人说：“你们乱砍树木是不对的，
没有了树木，我们动物就无法生存，同样也会给你们人类带来灾难的。”听了这些话，伐木工人觉得很惭愧，知道自己错了，
他们保证以后不再乱砍树木破坏森林了，还在森林入口立了一块告示牌，上面写着：“保护森林，人人有责。”从此以后，人们不再破坏森林，
动物和人类和平相处，大家都过着幸福、快乐的生活。
"""

tts = gTTS(text=text, lang='zh-tw')
tts.save("XXX.mp3")

```

### 二. 用pyttsx3模块

**参考文档**：

**优势：** 1、完全脱机文本到语音转换，可以在系统中安装的不同语音中进行选择； 2、控制语音的速度/速率，调整音量； 3、将语音音频另存为文件； 4、简单、强大、直观的API。

使用前需要先安装：`pip3 install pyttsx3`

#### 基本使用

```
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

```

#### 直接朗读

```
import pyttsx3
pyttsx3.speak("I will speak this text")

```

#### 更改语音、速率和音量

```
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()


"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

```

### 三. baidu-aip

通过在百度开放开发者平台申请语音合成账号来生成音频文件。样例如下：

```
# 下载baidu-aip模块并导入
from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY) #配置百度语音客户端res=client.synthesis(text,lang,1,options={<!-- -->
spd:语速，取值0-9，默认为5中语速,
pit:音调，取值0-9，默认为5中语调,
vol:音量，取值0-15，默认为5中音量,
per:发音人选择, 0为女声，1为男声， 3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女})  
#配置个性化语音
with open('XX.mp3','wb') as f:  #打开文件流
    f.write(res)    #写入文件

```

### 四. pywin32

操作window dll的库，它可以实现很多功能，十分强大。不过经测试，对中文支持不太友好。

需要先安装：`pip install pywin32`

```
# -*- encoding: utf-8 -*-
from win32com import client

# 配置客户端接口
speaker = client.Dispatch("SAPI.SpVoice")

speaker.Speak("hello")

```

### 五. speech

也是一款强大的语音模块，依赖于pywin32，而且它最适合做语音启动程序了。

下载并导入：`pip install speech`

```
import speech
# 生成音频：
speech.say('hello')

```
