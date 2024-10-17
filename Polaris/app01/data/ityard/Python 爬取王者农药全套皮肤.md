
--- 
title:  Python 爬取王者农药全套皮肤 
tags: []
categories: [] 

---
>  
  作者：toofelix 
  来源：http://suo.im/6pj3Zp 
 

## 

## 一、分析需要爬取的网站

#### ①、打开官方王者荣耀壁纸网站
- 网站地址：https://pvp.qq.com/web201605/wallpaper.shtml
#### ②、快捷键F12，调出控制台进行抓包

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNVpmVG03SEw0VHFPME5nZmp3cFdqVVlNb3dmcW1ESUVGOXZWV0J0ZnEzS3pBRGU1czVWMGljMncvNjQw?x-oss-process=image/format,png">

#### ③、找到正确的链接并分析

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNU5XZmpoU25WVkppY0JMYVlQaFBkaWFWcDNqS3o0aWJ3Nks1MkxMd2lhRmhhaWFQUkhzZ2RjWHNvUzFnLzY0MA?x-oss-process=image/format,png">

#### ④、查看返回数据格式

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNVllNjZCR2ozT2RPNWQzUHBIaWE0WXdaeEs1RXpPOHA2a096OFZWcUY4WUhMOVVYaWM4bEgweXpBLzY0MA?x-oss-process=image/format,png">

#### ⑤、解析url链接

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNW9DQmJSemg5TDVYeExheWVxZnJCQWtPTGNqOGlheVhuN3V0OXJncHd1NGlhamljbmUyblJ5TUVNdy82NDA?x-oss-process=image/format,png">

#### ⑥、查看url内容是否是所需图片，发现其实是缩略图

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNVRlSWM0bVR6QmwwejIzSW02UnZIa3JYb1NGTlp6ZnBpYzJySWlhZ2VOb3pJcDFiRUE3eWdUT0N3LzY0MA?x-oss-process=image/format,png">

#### ⑦、那就去分析网站，随便点开一张壁纸，查看指定格式的链接

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNXFPQjRsZ0RmOWliZDBuVWhmbFNINUNSYThTY0VpYzJocnM5OXRUTWNmMGlhb2FmZzlPOVVUNDY1QS82NDA?x-oss-process=image/format,png">

#### ⑧、找到目标地址

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNTBwS2dZNUM0WTJWcVVWMTFTelR4QWJoMHdLVEFhN2hrYmRGczNENXd6NmdDckx2dmNyeDRVQS82NDA?x-oss-process=image/format,png">

#### ⑨、分析目标链接和缩略图的链接区别
- 缩略图：http://shp.qpic.cn/ishow/2735090714/1599460171_84828260_8311_sProdImgNo_6.jpg/200- 目标图：http://shp.qpic.cn/ishow/2735090714/1599460171_84828260_8311_sProdImgNo_6.jpg/0- 可以知道，将指定格式的缩略图地址后面200替换成0就是目标真实图片
## 二、爬虫代码

#### ①、至此，爬虫分析完成，爬虫完整代码如下

```
#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 王者荣耀壁纸下载
#
#                   @File Name    : main.py
#
#                   @Programmer   : Felix
#
#                   @Start Date   : 2020/7/30 14:42
#
#                   @Last Update  : 2020/7/30 14:42
#
#-------------------------------------------------------------------
'''
import os, time, requests, json, re
from retrying import retry
from urllib import parse
 
class HonorOfKings:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self, save_path='./heros'):
        self.save_path = save_path
        self.time = str(time.time()).split('.')
        self.url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&amp;sVerifyCode=ABCD&amp;sDataType=JSON&amp;iListNum=20&amp;totalpage=0&amp;page={}&amp;iOrder=0&amp;iSortNumClose=1&amp;iAMSActivityId=51991&amp;_everyRead=true&amp;iTypeId=2&amp;iFlowId=267733&amp;iActId=2735&amp;iModuleId=2735&amp;_=%s' % self.time[0]
 
    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print("*" * 50)
        print(' ' * 18 + '王者荣耀壁纸下载')
        print(' ' * 5 + '作者: Felix  Date: 2020-05-20 13:14')
        print("*" * 50)
        return self
 
    def run(self):
        '''
        The program entry
        '''
        print('↓' * 20 + ' 格式选择: ' + '↓' * 20)
        print('1.缩略图 2.1024x768 3.1280x720 4.1280x1024 5.1440x900 6.1920x1080 7.1920x1200 8.1920x1440')
        size = input('请输入您想下载的格式序号，默认6：')
        size = size if size and int(size) in [1,2,3,4,5,6,7,8] else 6
 
        print('---下载开始...')
        page = 0
        offset = 0
        total_response = self.request(self.url.format(page)).text
        total_res = json.loads(total_response)
        total_page = --int(total_res['iTotalPages'])
        print('---总共 {} 页...' . format(total_page))
        while True:
            if offset &gt; total_page:
                break
            url = self.url.format(offset)
            response = self.request(url).text
            result = json.loads(response)
            now = 0
            for item in result["List"]:
                now += 1
                hero_name = parse.unquote(item['sProdName']).split('-')[0]
                hero_name = re.sub(r'[【】:.&lt;&gt;|·@#$%^&amp;() ]', '', hero_name)
                print('---正在下载第 {} 页 {} 英雄 进度{}/{}...' . format(offset, hero_name, now, len(result["List"])))
                hero_url = parse.unquote(item['sProdImgNo_{}'.format(str(size))])
                save_path = self.save_path + '/' + hero_name
                save_name = save_path + '/' + hero_url.split('/')[-2]
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                if not os.path.exists(save_name):
                    with open(save_name, 'wb') as f:
                        response_content = self.request(hero_url.replace("/200", "/0")).content
                        f.write(response_content)
            offset += 1
        print('---下载完成...')
 
    @retry(stop_max_attempt_number=3)
    def request(self, url):
        '''
        Send a request
        :param url: the url of request
        :param timeout: the time of request
        :return: the result of request
        '''
        response = requests.get(url, timeout=10)
        assert response.status_code == 200
        return response
 
if __name__ == "__main__":
    HonorOfKings().hello().run()

```

#### ②、详细分析链接
- 其实前端发送的是jsonp请求，这样的数据在python不好处理，因为不是标准的json格式- 因为其前面JQuery1710418919222这个字符串，而知道jsonp的请求的都知道，有这个前缀，必然请求链接中有相同的callback参数，将其删除即可- 因此我python代码中是删除了这个参数的- 这个链接还有很多参数，其实我觉得很多都可以删除，但是我懒得慢慢去试- 这个请求链接中最重要的一个参数必然就是页码数，也就是page这个参数，iListNum=20&amp;totalpage=0&amp;page={}- 上面的三个参数是可用的，一个是20，指每页的数量，totalpage估计没啥用，page抓包发现是从0开始的，这个需要注意一下，因为下面代码需要将总页数减1
```
self.url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&amp;sVerifyCode=ABCD&amp;sDataType=JSON&amp;iListNum=20&amp;totalpage=0&amp;page={}&amp;iOrder=0&amp;iSortNumClose=1&amp;iAMSActivityId=51991&amp;_everyRead=true&amp;iTypeId=2&amp;iFlowId=267733&amp;iActId=2735&amp;iModuleId=2735&amp;_=%s' % self.time[0]

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNVllNjZCR2ozT2RPNWQzUHBIaWE0WXdaeEs1RXpPOHA2a096OFZWcUY4WUhMOVVYaWM4bEgweXpBLzY0MA?x-oss-process=image/format,png">

#### ③、格式选择
- 开始运行时，让你选择想下载格式的序号，为什么是8个格式呢，看原网页就知道了，8种不同分辨率的- 看上面的图片，缩略图链接有1-8，对应了8中分辨率的缩略图，那么原图必然也是8种- 这里我默认1920*1080的，一般电脑用这个分辨率的都可以- 其中1的原图，你自己试下，其实也是一个缩略图，所以一般下载选择2-8
```
print('↓' * 20 + ' 格式选择: ' + '↓' * 20)
print('1.缩略图 2.1024x768 3.1280x720 4.1280x1024 5.1440x900 6.1920x1080 7.1920x1200 8.1920x1440')
size = input('请输入您想下载的格式序号，默认6：')
size = size if size and int(size) in [1,2,3,4,5,6,7,8] else 6

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNXFPQjRsZ0RmOWliZDBuVWhmbFNINUNSYThTY0VpYzJocnM5OXRUTWNmMGlhb2FmZzlPOVVUNDY1QS82NDA?x-oss-process=image/format,png">

#### ④、下载代码分析
- 第一次请求主要是为了获取总页数，但是请求是从0开始为第一页，所以需要减去1- while true中就是开始从0循环去请求地址，先找到缩略图地址，然后将缩略图的地址链接200替换成0就是目标图片地址了- 如果名字中有特殊字符，就将其用正则去除，不然可能会影响路径的查找
```
print('---下载开始...')
page = 0
offset = 0
total_response = self.request(self.url.format(page)).text
total_res = json.loads(total_response)
total_page = --int(total_res['iTotalPages'])
print('---总共 {} 页...' . format(total_page))
while True:
    if offset &gt; total_page:
        break
    url = self.url.format(offset)
    response = self.request(url).text
    result = json.loads(response)
    now = 0
    for item in result["List"]:
        now += 1
        hero_name = parse.unquote(item['sProdName']).split('-')[0]
        hero_name = re.sub(r'[【】:.&lt;&gt;|·@#$%^&amp;() ]', '', hero_name)
        print('---正在下载第 {} 页 {} 英雄 进度{}/{}...' . format(offset, hero_name, now, len(result["List"])))
        hero_url = parse.unquote(item['sProdImgNo_{}'.format(str(size))])
        save_path = self.save_path + '/' + hero_name
        save_name = save_path + '/' + hero_url.split('/')[-2]
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        if not os.path.exists(save_name):
            with open(save_name, 'wb') as f:
                response_content = self.request(hero_url.replace("/200", "/0")).content
                f.write(response_content)
    offset += 1
print('---下载完成...')

```

#### ⑤、爬虫运行的结果，相同名字的放在同一个文件夹下

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNTBMektqSjNJRjN4c1VEVFRUaWNTRTMxWVV2dDZqSTFVUjM1Q3ViUFp3TVljaWFyY3JUbEhaaWI5dy82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhnU043aWFsOHpDUkN4T1lqc05pYWVsNTBUZUwzUXJZY2ZrbnVmZlB1TDJHUUxhdVlKY3R1V3pNU0dvQ3l0V1dpY0RxbTNHSHFncjl2NmcvNjQw?x-oss-process=image/format,png">

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
