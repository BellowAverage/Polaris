
--- 
title:  用 Python 修改微信（支付宝）运动步数，轻松 TOP1 
tags: []
categories: [] 

---
>  
  作者：Tsubasa_Ou 
  https://blog.csdn.net/jiangfan2017/article/details/108984940 
 

## 项目意义

如果你想在支付宝蚂蚁森林收集很多能量种树，为环境绿化出一份力量，又或者是想每天称霸微信运动排行榜装逼，却不想出门走路，那么该python脚本可以帮你实现。

## 实现方法

手机安装第三方软件乐心健康，注册账号登录，将运动数据同步到微信和支付宝。用python脚本远程修改乐心健康当前登录账号的步数即可。

第一步：在手机上安装乐心健康app。

安卓版下载地址：`http://app.mi.com/details?id=gz.lifesense.weidong`

苹果版下载地址：`https://apps.apple.com/us/app/lifesense-health/id1479525632`

第二步：注册账号登录，并设置登录密码。

第三步：完成第三方同步，将运动数据同步到微信和支付宝。

第四步：运行python脚本，修改乐心健康步数。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcXJ2R01rYjdNRVF5Sm9RTUNDOERnSDR6dkR4aWJtN3MzYWVWTXdDOTZ2ZG1Nc0FnZFJXaE50VXJpYlFRRTdVRXdJMTZVWUZ0TEJvaWJMZy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcXJ2R01rYjdNRVF5Sm9RTUNDOERnSHBrOUlJWjR3b1NxNGs1U1k5SkpGaWJCV0JpYkM5TjJsRGQ3VFNEaWNWUTluN2lheXE1MFc4S1Z5SkEvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcXJ2R01rYjdNRVF5Sm9RTUNDOERnSHNuWXJYU3Q4UkN3TXl5WkxkdkxYU0dFVUVSQ1RzZUxtdGtJSFZiTHQwam1XZzVGQVpjaWJtV1EvNjQw?x-oss-process=image/format,png">

## python代码

程序设定是每天7点自动修改步数，在下面脚本对应的位置替换填入乐心健康账号、乐心健康密码、修改步数，然后运行程序。修改步数推荐设置范围是30000至90000，步数值太大会导致修改不成功。如果想改变第二天自动修改步数的时间，请修改图示位置的25200，+25200代表第二天0点后加上的秒数，也就是7x60x60，即7小时，根据自己的需要修改即可。如果每天都要修改步数，那么让程序一直保持运行即可。注意：运行程序会立刻修改当天的步数，自动修改步数是从程序保持运行的第二天开始。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcXJ2R01rYjdNRVF5Sm9RTUNDOERnSHViTDJ3c0VKdzZ3c29Eek9LN2lhSFZ5V25rNjBjWHVOb2liRzBqc2tDS1JCWUVqdGlhS3JHWUtMUS82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcXJ2R01rYjdNRVF5Sm9RTUNDOERnSE12THNmdE5pYklLRDMwS0VZTGljanliY2lhS3ZCMlRVanFKaHNXbjhISUhWR2liU3V5Y2ljMW1qTlpRLzY0MA?x-oss-process=image/format,png">change_step.py

```
# -*- coding: utf-8 -*-
import requests
import json
import hashlib
import time
import datetime


class LexinSport:
    def __init__(self, username, password, step):
        self.username = username
        self.password = password
        self.step = step

    # 登录
    def login(self):
        url = 'https://sports.lifesense.com/sessions_service/login?systemType=2&amp;version=4.6.7'
        data = {'loginName': self.username, 'password': hashlib.md5(self.password.encode('utf8')).hexdigest(),
                'clientId': '49a41c9727ee49dda3b190dc907850cc', 'roleType': 0, 'appType': 6}
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/LIO-AN00)'
        }
        response_result = requests.post(url, data=json.dumps(data), headers=headers)
        status_code = response_result.status_code
        response_text = response_result.text
        # print('登录状态码：%s' % status_code)
        # print('登录返回数据：%s' % response_text)
        if status_code == 200:
            response_text = json.loads(response_text)
            user_id = response_text['data']['userId']
            access_token = response_text['data']['accessToken']
            return user_id, access_token
        else:
            return '登录失败'

    # 修改步数
    def change_step(self):
        # 登录结果
        login_result = self.login()
        if login_result == '登录失败':
            return '登录失败'
        else:
            url = 'https://sports.lifesense.com/sport_service/sport/sport/uploadMobileStepV2?systemType=2&amp;version=4.6.7'
            data = {'list': [{'DataSource': 2, 'active': 1, 'calories': int(self.step/4), 'dataSource': 2,
                              'deviceId': 'M_NULL', 'distance': int(self.step/3), 'exerciseTime': 0, 'isUpload': 0,
                              'measurementTime': time.strftime('%Y-%m-%d %H:%M:%S'), 'priority': 0, 'step': self.step,
                              'type': 2, 'updated': int(round(time.time() * 1000)), 'userId': login_result[0]}]}
            headers = {
                'Content-Type': 'application/json; charset=utf-8',
                'Cookie': 'accessToken=%s' % login_result[1]
            }
            response_result = requests.post(url, data=json.dumps(data), headers=headers)
            status_code = response_result.status_code
            # response_text = response_result.text
            # print('修改步数状态码：%s' % status_code)
            # print('修改步数返回数据：%s' % response_text)
            if status_code == 200:
                return '修改步数为【%s】成功' % self.step
            else:
                return '修改步数失败'


# 睡眠到第二天执行修改步数的时间
def get_sleep_time():
    # 第二天日期
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    # 第二天7点时间戳
    tomorrow_run_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) + 25200
    # print(tomorrow_run_time)
    # 当前时间戳
    current_time = int(time.time())
    # print(current_time)
    return tomorrow_run_time - current_time


if __name__ == "__main__":
    # 最大运行出错次数
    fail_num = 3
    while 1:
        while fail_num &gt; 0:
            try:
                # 修改步数结果
                result = LexinSport('乐心健康账号', '乐心健康密码', 修改步数).change_step()
                print(result)
                break
            except Exception as e:
                print('运行出错，原因：%s' % e)
                fail_num -= 1
                if fail_num == 0:
                    print('修改步数失败')
        # 重置运行出错次数
        fail_num = 3
        # 获取睡眠时间
        sleep_time = get_sleep_time()
        time.sleep(sleep_time)


```

源码及相关文件在公众号后台回复 `步数` 获取。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
