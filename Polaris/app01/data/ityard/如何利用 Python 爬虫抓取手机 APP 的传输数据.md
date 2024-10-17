
--- 
title:  如何利用 Python 爬虫抓取手机 APP 的传输数据 
tags: []
categories: [] 

---
大多数APP里面返回的是json格式数据，或者一堆加密过的数据 。这里以超级课程表APP为例，抓取超级课程表里用户发的话题。

**1、抓取APP数据包**

表单：

<img src="https://img-blog.csdnimg.cn/img_convert/f0d55eadcde82545ffa12c90fa3d5ae5.png" alt="f0d55eadcde82545ffa12c90fa3d5ae5.png">

表单中包括了用户名和密码，当然都是加密过了的，还有一个设备信息，直接post过去就是。

另外必须加header,一开始我没有加header得到的是登录错误，所以要带上header信息。

<img src="https://img-blog.csdnimg.cn/img_convert/7a40b5100afce18f177db8b5a8769f2c.png" alt="7a40b5100afce18f177db8b5a8769f2c.png">

**2、登录**

登录代码：

```
import urllib2
from cookielib import CookieJar
loginUrl = 'http://120.55.151.61/V2/StudentSkip/loginCheckV4.action'
headers = {
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; M040 Build/JRO03H)',
'Host': '120.55.151.61',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'Content-Length': '207',
}
loginData = 'phoneBrand=Meizu&amp;platform=1&amp;deviceCode=868033014919494&amp;account=FCF030E1F2F6341C1C93BE5BBC422A3D&amp;phoneVersion=16&amp;password=A55B48BB75C79200379D82A18C5F47D6&amp;channel=MXMarket&amp;phoneModel=M040&amp;versionNumber=7.2.1&amp;'
cookieJar = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
req = urllib2.Request(loginUrl, loginData, headers)
loginResult = opener.open(req).read()
print loginResult
```

登录成功 会返回一串账号信息的json数据

<img src="https://img-blog.csdnimg.cn/img_convert/ce9a51b755ba0246d67b54a6bb946d72.png" alt="ce9a51b755ba0246d67b54a6bb946d72.png">

和抓包时返回数据一样，证明登录成功

<img src="https://img-blog.csdnimg.cn/img_convert/36f799d68a73c0eca07d59248a207a63.png" alt="36f799d68a73c0eca07d59248a207a63.png">

**3、抓取数据**

用同样方法得到话题的url和post参数

下见最终代码，有主页获取和下拉加载更新。可以无限加载话题内容。

```
#!/usr/local/bin/python2.7
# -*- coding: utf8 -*-
"""
超级课程表话题抓取
"""
import urllib2
from cookielib import CookieJar
import json
''' 读Json数据 '''
def fetch_data(json_data):
data = json_data['data']
timestampLong = data['timestampLong']
messageBO = data['messageBOs']
topicList = []
for each in messageBO:
topicDict = {}
if each.get('content', False):
topicDict['content'] = each['content']
topicDict['schoolName'] = each['schoolName']
topicDict['messageId'] = each['messageId']
topicDict['gender'] = each['studentBO']['gender']
topicDict['time'] = each['issueTime']
print each['schoolName'],each['content']
topicList.append(topicDict)
return timestampLong, topicList
''' 加载更多 '''
def load(timestamp, headers, url):
headers['Content-Length'] = '159'
loadData = 'timestamp=%s&amp;phoneBrand=Meizu&amp;platform=1&amp;genderType=-1&amp;topicId=19&amp;phoneVersion=16&amp;selectType=3&amp;channel=MXMarket&amp;phoneModel=M040&amp;versionNumber=7.2.1&amp;' % timestamp
req = urllib2.Request(url, loadData, headers)
loadResult = opener.open(req).read()
loginStatus = json.loads(loadResult).get('status', False)
if loginStatus == 1:
print 'load successful!'
timestamp, topicList = fetch_data(json.loads(loadResult))
load(timestamp, headers, url)
else:
print 'load fail'
print loadResult
return False
loginUrl = 'http://120.55.151.61/V2/StudentSkip/loginCheckV4.action'
topicUrl = 'http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV3.action'
headers = {
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; M040 Build/JRO03H)',
'Host': '120.55.151.61',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'Content-Length': '207',
}
''' ---登录部分--- '''
loginData = 'phoneBrand=Meizu&amp;platform=1&amp;deviceCode=868033014919494&amp;account=FCF030E1F2F6341C1C93BE5BBC422A3D&amp;phoneVersion=16&amp;password=A55B48BB75C79200379D82A18C5F47D6&amp;channel=MXMarket&amp;phoneModel=M040&amp;versionNumber=7.2.1&amp;'
cookieJar = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
req = urllib2.Request(loginUrl, loginData, headers)
loginResult = opener.open(req).read()
loginStatus = json.loads(loginResult).get('data', False)
if loginResult:
print 'login successful!'
else:
print 'login fail'
print loginResult
''' ---获取话题--- '''
topicData = 'timestamp=0&amp;phoneBrand=Meizu&amp;platform=1&amp;genderType=-1&amp;topicId=19&amp;phoneVersion=16&amp;selectType=3&amp;channel=MXMarket&amp;phoneModel=M040&amp;versionNumber=7.2.1&amp;'
headers['Content-Length'] = '147'
topicRequest = urllib2.Request(topicUrl, topicData, headers)
topicHtml = opener.open(topicRequest).read()
topicJson = json.loads(topicHtml)
topicStatus = topicJson.get('status', False)
print topicJson
if topicStatus == 1:
print 'fetch topic success!'
timestamp, topicList = fetch_data(topicJson)
load(timestamp, headers, topicUrl)
```

结果：

<img src="https://img-blog.csdnimg.cn/img_convert/c2d14e6ada741e65c3e2b2d8548e4e63.png" alt="c2d14e6ada741e65c3e2b2d8548e4e63.png">声明：本文于网络整理，版权归原作者所有，如来源信息有误或侵犯权益，请联系我们删除或授权

<img src="https://img-blog.csdnimg.cn/img_convert/6b50ff68049bbffbff06aaf0fb12f206.png" alt="6b50ff68049bbffbff06aaf0fb12f206.png">
