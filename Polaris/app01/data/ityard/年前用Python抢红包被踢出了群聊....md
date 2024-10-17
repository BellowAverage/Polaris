
--- 
title:  年前用Python抢红包被踢出了群聊... 
tags: []
categories: [] 

---
### 1. 概述

快过年了，刚刚收到了两个消息，一个好消息，一个坏消息。

先说好消息，好消息就是微信群里有人要发红包，开心~

<img src="https://img-blog.csdnimg.cn/img_convert/7efaf0fab8b97bf4b3e11abe6a374078.jpeg" alt="7efaf0fab8b97bf4b3e11abe6a374078.jpeg">

不过转念一想，前几次的红包一个都没抢到，这次？？？不由自主的叹了一口气 ...

<img src="https://img-blog.csdnimg.cn/img_convert/c88de1661fbab2696030bc1f6d0f2c1d.jpeg" alt="c88de1661fbab2696030bc1f6d0f2c1d.jpeg">

过了一会，内心的情绪逐渐平复了。

<img src="https://img-blog.csdnimg.cn/img_convert/c9a48a011bae96d3111a4904b4708095.jpeg" alt="c9a48a011bae96d3111a4904b4708095.jpeg">

心想：“难道就这么放弃了吗？晚饭还吃泡面（泡面感觉有被冒犯到<img src="https://img-blog.csdnimg.cn/img_convert/bdd86fe30e936d1833525e84f8b72db6.png" alt="bdd86fe30e936d1833525e84f8b72db6.png">）？但是手动抢肯定没戏，毕竟手can谁也没办法！那就只能试试能不能通过编程的方式实现自动化抢红包了！”

<img src="https://img-blog.csdnimg.cn/img_convert/8368b8f296bccb9d12094260ad8f836f.jpeg" alt="8368b8f296bccb9d12094260ad8f836f.jpeg">

现在捋一下思路，微信群发红包的基本情况是：每一次发红包都会与上一次有一些时间间隔，实现自动化抢红包的基本思路如下：
- 手动清空之前微信群中的红包记录- 执行自动化抢红包程序，进入发红包的微信群（可以暂时将其顶置），循环检测群中是否有红包，发现红包则点击红包- 检测红包是否被领取（判断点击后的红包是否出现开字），如果红包未被领取，则点击开字领取红包，再返回群聊界面删除已被领取的红包记录；如果红包已被领取，则返回群聊界面删除已被领取的红包记录，之后以此类推
### 2. 环境

本文主要环境如下：
- Win7- 小米5s- Python3.7- Appium1.5- 微信7.0.20
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

<img src="https://img-blog.csdnimg.cn/img_convert/ed9a95500281773d09bc8f501eb34b3e.png" alt="ed9a95500281773d09bc8f501eb34b3e.png">

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

<img src="https://img-blog.csdnimg.cn/img_convert/3a152cca03c6d8aa0615e22e218e4d9b.png" alt="3a152cca03c6d8aa0615e22e218e4d9b.png">

点击长按后显示的删除项之后的效果图如下：

<img src="https://img-blog.csdnimg.cn/img_convert/271adb0fde851e725437b0f400ad706a.png" alt="271adb0fde851e725437b0f400ad706a.png">

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

源码在👇公众号 Python小二 后台回复 201123 获取。
- - - - - - - 