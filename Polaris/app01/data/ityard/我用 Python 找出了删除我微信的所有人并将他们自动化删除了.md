
--- 
title:  我用 Python 找出了删除我微信的所有人并将他们自动化删除了 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/2020110813310160.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

### 1. 概述

不知你是否遇到过在微信上给通讯录中的某个人发消息，结果出现了这一幕：

<img src="https://img-blog.csdnimg.cn/20201108132602297.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

平时一直认为自己的心里素质过硬，不过遇到这种情况 …

<img src="https://img-blog.csdnimg.cn/20201108132619938.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">

在我缓了半个钟头（半分钟）之后，缓缓拿出了手机，打开微信，找到通讯录中的 `ABC`，默默地按下了删除按钮，此刻的我心如止水 …

<img src="https://img-blog.csdnimg.cn/20201108132635374.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">

好了，我们回到正题，为了避免再次出现上述情况，我决定把微信通讯录中删除了自己的人全部找出来并且删除，之前我已经在网上了解到检查自己的微信是否被删比较好的方式就是转账，通过转账我们可以实现无痕检测。

<img src="https://img-blog.csdnimg.cn/20201108132651256.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

下面我们通过两张图片直观的看一下微信被删前后给别人转账的效果：

<img src="https://img-blog.csdnimg.cn/20201108132705231.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400"> <img src="https://img-blog.csdnimg.cn/20201108132717447.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">

现在已经知道了检测方式，正在我准备挨个检测时，无意识的滑动了微信通讯录列表，100、200 … 500 …

<img src="https://img-blog.csdnimg.cn/20201108132738997.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">

我去！什么时候加了这么多人，滑动列表的同时我顺势扫了一眼微信名字：A卖保险、B办理信用卡、C游泳健身、D卖保健品 … 此刻我知道了微信通讯录中有这么多人的玄机，但是有个问题，这么多人我挨个手动执行转账还不累屎了 …

如果手动执行的方式行不通，那么可以通过编程的方式自动化执行吗？想到这里我陷入了沉思 …

<img src="https://img-blog.csdnimg.cn/2020110813275669.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">

突然我脑中闪了一下（不是抽筋哈），思绪渐明，前几天我不是写了一篇吗？用这个应该就可以实现，编程实现的基本思路如下：
-  获取微信通讯录列表中每个人的名字（备注）并记录，这个是不会有重复的，因为即使在之前加好友时有重复的，自己也会在备注时给改了 -  遍历获取到的通讯录列表，分别对每一个人执行转账操作，如果检测到是删除自己的人就对其执行删除操作，如果检测到不是删除自己的人则继续检测下一个人，依次往复循环 
### 2. 环境

因之前在模拟器上测试 Appium 模拟微信转账可能有点问题，因此本文使用真机实现。

先简单介绍一下真机环境，下面一起来看一下相应步骤。
-  从桌角下取出我的小米5s手机（MIUI10.2、Android8.0.0），擦擦灰尘后用数据线将其连到自己的电脑上 -  手机充了一会电之后开机，打开微信登录自己的微信号 -  在手机中依次执行（点击）：设置-&gt;我的设备-&gt;全部参数-&gt;MIUI版本（多次点击，开启开发者模式）-&gt;返回设置列表-&gt;更多设置-&gt;开发者选项-&gt;开启开发者选项并分别开启：USB调试、USB安装、USB调试（安全设置）选项，如图所示： 
<img src="https://img-blog.csdnimg.cn/20201108132851884.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">
- 此时手机上会弹出USB的用途弹框，我们选择传输文件（MTP）即可，如图所示：
<img src="https://img-blog.csdnimg.cn/20201108132907583.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="400">
-  在电脑 CMD 中执行 `adb devices` 命令，看是否能找到自己的手机，比如下图所示就是成功的结果了 <img src="https://img-blog.csdnimg.cn/20201108132921776.PNG#pic_center" alt=""> -  在上面步骤中你可能出现找不到手机的情况，通常这种情况是驱动问题，这里介绍一种简单的处理方式：下载一个驱动精灵，安装启动之后点击驱动管理，之后安装相应驱动即可解决，如图所示： 
<img src="https://img-blog.csdnimg.cn/20201108132940728.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="600"> <img src="https://img-blog.csdnimg.cn/20201108132954161.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="600">

通过上面的一系列操作，我们已经处理好了真机环境了。

Appium 的环境本文就不说了，如果不清楚的话，可以看一下：。

### 3. 实现

下面我们开始手动敲代码，如果对 Appium 基本代码操作不了解的话，还是可以去看一下我之前写的这篇：。

首先看一下相应参数配置，代码实现如下：

```
desired_caps = {<!-- -->
    "platformName": "Android", # 系统
    "platformVersion": "8.0.0", # 系统本号
    "deviceName": "m5s", # 设备名
    "appPackage": "com.tencent.mm", # 包名
    "appActivity": ".ui.LauncherUI", # app 启动时主 Activity
    'unicodeKeyboard': True, # 使用自带输入法
    'noReset': True # 保留 session 信息，可以避免重新登录
}

```

接着看一下如何获取微信通讯录名字（备注）列表？代码实现如下：

```
# 获取通讯录列表
def get_address_list():
    driver.find_elements_by_id('com.tencent.mm:id/cn_')[1].click()
    # 获取昵称（备注）
    address_list = driver.find_elements_by_id('com.tencent.mm:id/dy5')
    remarks = []
    for address in address_list:
        remark = address.get_attribute("content-desc")
        # 排除自己和微信官方号
        if remark != "自己的微信名" and "微信" not in remark:
            remarks.append(remark)
    return remarks

```

取到了微信通讯录列表之后，我们就可以对其进行遍历检测了，下面看一下如何实现检测自己的微信是否被删，代码实现如下：

```
# 判断是否被删
def is_delete(remark, count):
    if count == "1":
        time.sleep(2)
        print('点击微信搜索框')
        driver.find_element_by_id('com.tencent.mm:id/cn1').click()
    time.sleep(2)
    print('在搜索框输入搜索信息')
    driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(remark)
    time.sleep(2)
    print('点击搜索到的好友')
    driver.find_element_by_id('com.tencent.mm:id/tm').click()
    time.sleep(2)
    # 转账
    driver.find_element_by_id('com.tencent.mm:id/aks').click()
    time.sleep(2)
    driver.find_elements_by_id('com.tencent.mm:id/pa')[5].click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/cx_').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/cxi').click()
    time.sleep(5)
    # 判断是否被删
    is_exist = is_element_exist('com.tencent.mm:id/jh')
    if is_exist is True:
        return remark
    else:
        return False

```

上述方法中，如果检测到是删了自己微信的人就返回那个人的微信名（备注），然后我们将这些人记录起来；如果检测到不是删除自己微信的人就返回 False。

上述过程执行完了之后，我们就可以获取到所有删了自己微信的人了，接下来我们就可以将这些人都从自己微信通讯录中删除了，删除实现的代码如下：

```
# 删除把自己删除的人
def del_person(nicks):
    for inx, val in enumerate(nicks):
        time.sleep(2)
        if inx == 0:
            print('在搜索框输入搜索信息')
            driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(val)
        else:
            time.sleep(2)
            print('点击微信搜索框')
            driver.find_element_by_id('com.tencent.mm:id/cn1').click()
            print('在搜索框输入搜索信息')
            time.sleep(1)
            driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(val)
        time.sleep(2)
        print('点击搜索到的人')
        driver.find_element_by_id('com.tencent.mm:id/tm').click()
        time.sleep(2)
        print('点击聊天对话框右上角...')
        driver.find_element_by_id('com.tencent.mm:id/cj').click()
        time.sleep(2)
        print('点击头像')
        driver.find_element_by_id('com.tencent.mm:id/f3y').click()
        time.sleep(2)
        print('点击联系人右上角...')
        driver.find_element_by_id('com.tencent.mm:id/cj').click()
        time.sleep(2)
        print('点击删除按钮')
        driver.find_element_by_id('com.tencent.mm:id/g6f').click()
        time.sleep(2)
        print('点击弹出框中的删除')
        driver.find_element_by_id('com.tencent.mm:id/doz').click()

```

至此，我们就利用 Python + Appium 实现了自动化找出微信中删除自己的人并将其删除的工作了。
