
--- 
title:  年轻人不讲武德，用Python自动化抢红包，耗子尾汁 
tags: []
categories: [] 

---
### 1. 概述

刚刚收到了两个消息，一个好消息，一个坏消息。

先说好消息，好消息就是微信群里有人要发红包，开心~

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXVTaWNrZUpxeGliOUQ2aWFNOVI1RUxyek1MNWVMUjlKa29VTEdpYlVIaHhhQWlhQXBZRHN6S1VLaG5Udy82NDA?x-oss-process=image/format,png">

不过转念一想，前几次的红包一个都没抢到，这次？？？不由自主的叹了一口气 ...

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXU5ajlnVlRYeHpjOEdwT0p0NkVYTmhKNFIyN25GMTNYQmliZmliUG9XdFRuSUMyYk9QeEg1N0dNQS82NDA?x-oss-process=image/format,png">

过了一会，内心的情绪逐渐平复了。

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXVGZXpJdmljaWNJVzJub0k1OW1GUkpSMnhtRXRTcmNTVTVQaWJES0tsY3BZemljRThzRUpVZzl2SEpBLzY0MA?x-oss-process=image/format,png">

心想：“难道就这么放弃了吗？晚饭还吃泡面（泡面感觉有被冒犯到<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXU1U0dvOWJZd0t4RFV2aWI0VkYxTWlhQUc0ZkVRQUk5d1N1enRYZVlEaWFSVndxWjR0RHNHQk4zWmcvNjQw?x-oss-process=image/format,png">）？但是手动抢肯定没戏，毕竟手can谁也没办法！那就只能试试能不能通过编程的方式实现自动化抢红包了！”

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXVZNWlhSG1uSGdwSlVZR1ZkeThvd2hVclhtV3dReVhFOGs2Tnc4VkJ6aWJMbURpYjJmaWNBSG5pYnhSZy82NDA?x-oss-process=image/format,png">

现在捋一下思路，微信群发红包的基本情况是：每一次发红包都会与上一次有一些时间间隔，实现自动化抢红包的基本思路如下：
-  手动清空之前微信群中的红包记录 -  执行自动化抢红包程序，进入发红包的微信群（可以暂时将其顶置），循环检测群中是否有红包，发现红包则点击红包 -  检测红包是否被领取（判断点击后的红包是否出现开字），如果红包未被领取，则点击开字领取红包，再返回群聊界面删除已被领取的红包记录；如果红包已被领取，则返回群聊界面删除已被领取的红包记录，之后以此类推 
### 2. 环境

本文主要环境如下：
-  Win7 -  小米5s -  Python3.7 -  Appium1.5 -  微信7.0.20 
如果对环境搭建不熟悉的话，可以看一下： 和 。

### 3. 实现

接下来我们开始手动敲代码，下面一起来看一下具体实现。

首先看一下配置信息，代码实现如下：

```
desired_caps = {
    "platformName": "Android", # 系统
    "platformVersion": "8.0.0", # 系统版本号
    "deviceName": "m5s", # 设备名
    "appPackage": "com.tencent.mm", # 包名
    "appActivity": ".ui.LauncherUI", # app 启动时主 Activity
    'unicodeKeyboard': True, # 使用自带输入法
    'noReset': True # 保留 session 信息，可以避免重新登录
}

```

因为点击红包后需要判断点击后的红包是否被领取，即是否有开字，如图所示：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXUwMWNjTmljQkUxeHVsSUZPVzZJVEZFVU8wQld3cVdzMTd2NE5LWHFFM0xpYkRLOERDWFVsNHB3Zy82NDA?x-oss-process=image/format,png">

所以我们定义一个判断元素是否存在的方法，代码实现如下：

```
# 判断元素是否存在
def is_element_exist(driver, by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:
        return False
    else:
        return True

```

因为红包无论是被自己领取还是被他人领取，之后都要删除领取后的红包记录，所以我们再来定义一个删除已领取红包的方法，代码实现如下：

```
# 删除领取后的红包记录
def del_red_envelope(wait, driver):
    # 长按领取过的红包
    r8 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/r8")))
    TouchAction(driver).long_press(r8).perform()
    # 点击长按后显示的删除
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/gam"))).click()
    # 点击弹出框的删除选项
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/doz"))).click()

```

长按领取后红包的效果图如下：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXVrcGF2NUUxNk81aWEzeTBnRG9kSmljVE9SSnlUY2VLdmZxbmVzM3JQeGRoS3h1SkhYUmFpYmliV3pnLzY0MA?x-oss-process=image/format,png">

点击长按后显示的删除项之后的效果图如下：

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2g5VGJ3czlxVXpiMmJFaWFtMENsZXV2MTZaSVB1cHUyd0pkeVpNWDBpY0o2dkh1Z0VONFRZT0tpYWZSQktZM3ZTeFFUR0t6NzdVbDVudy82NDA?x-oss-process=image/format,png">

我们接着来看一下进入红包群后的主程序实现，代码如下：

```
while True:
    # 有红包则点击
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/r8"))).click()
    print("点击了红包")
    # 判断红包是否被领取
    is_open = is_element_exist(driver, "id", "com.tencent.mm:id/den");
    print("红包是否被领取：", is_open)
    if is_open == True:
        # 红包未被领取，打开红包
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/den"))).click()
        # 返回群聊
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/dm"))).click()
        # 删除领取过的红包记录
        del_red_envelope(wait, driver)
    else:
        # 返回群聊
        driver.keyevent(4)
        # 删除领取过的红包记录
        del_red_envelope(wait, driver)

```

最后，我们通过视频来看一下整体效果：



源码在公号 Python小二 后台回复 201123 获取。

原创不易，如果觉得有一些帮助，希望大家给个分享、在看、赞。

&lt; END &gt;

<img alt="" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">
