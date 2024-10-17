
--- 
title:  Python + Appium 自动化操作微信入门看这一篇就够了 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20201104203003388.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

### 1. 简介

Appium 是一个开源的自动化测试工具，支持 Android、iOS 平台上的原生应用，支持 Java、Python、PHP 等多种语言。

Appium 封装了 Selenium，能够为用户提供所有常见的 JSON 格式的 Selenium 命令以及额外的移动设备相关的控制命令，比如：多点触控手势、屏幕朝向等。

### 2. 环境

本文主要环境如下：
- Win7- JDK1.8- Appium- Python3.7- android-sdk- mumu 模拟器
#### JDK

下载地址：`https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html`，也可在文末直接获取

配置环境变量：
- 计算机（右键）-&gt;属性-&gt;高级系统设置-&gt;高级-&gt;环境变量-&gt;新建环境变量 `JAVA_HOME`，如图所示：
<img src="https://img-blog.csdnimg.cn/20201104202554129.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">
-  系统变量-&gt;找到 `Path` 变量-&gt;编辑-&gt;在变量值的末尾添加`;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;` -  新建 `CLASSPATH` 变量，变量值为：`.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar` 
#### android-sdk

下载地址：`https://www.androiddevtools.cn/`，也可在文末直接获取

配置环境变量：
-  与 JDK 配置类似，新建环境变量 `ANDROID_HOME`，变量值为 `android-sdk` 位置，比如：`D:\android-sdk-windows` -  在 `Path` 变量值的末尾添加 `;%ANDROID_HOME%\tools;%ANDROID_HOME%\build-tools\30.0.0-preview;%ANDROID_HOME%\platform-tools` 
#### Appium

下载地址：`https://github.com/appium/appium-desktop/releases/tag/v1.18.3`，也可在文末直接获取

安装 Python 库：`pip install appium-python-client`

Appium 安装完成启动后，点击编辑配置，配置 JDK 和 android-sdk，如图所示：

<img src="https://img-blog.csdnimg.cn/20201104202628299.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

#### mumu

下载地址：`http://www.51xiazai.cn/soft/584481.htm`，也可在文末直接获取

mumu 模拟器下载完后，除了根据自己需要更改一下安装路径，其他选项默认即可安装，装完后打开点击`应用中心`，搜一下微信，搜到之后安装一下，微信安装完成后再用自己的微信号登录一下。

因为我们是通过安卓的 `adb` 连接虚拟机的，因此需要在控制台执行 `adb connect 127.0.0.1:7555` 命令，让 `adb` 连接上虚拟机。

执行了上面连接模拟器的命令后，我们可以在 `cmd` 控制台输入 `adb devices` 查看当前连接的虚拟机。

### 3. 使用

首先启动 Appium 和 mumu，因为之前我们已经配置了 Appium，此时我们直接点击 Appium 的`启动服务器`按钮即可，如下图所示：

<img src="https://img-blog.csdnimg.cn/20201104202646497.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

启动之后如图所示：

<img src="https://img-blog.csdnimg.cn/20201104202701371.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

现在我们可以先通过 Python 来启动一下微信，代码实现如下：

```
desired_caps = {
        "platformName": "Android",  # 操作系统
        "deviceName": "emulator-5554",  # 设备 ID
        "platformVersion": "6.0.1",  # 设备版本号
        "appPackage": "com.tencent.mm",  # app 包名
        "appActivity": "com.tencent.mm.ui.LauncherUI",  # app 启动时主 Activity
        'noReset': True,  # 是否保留 session 信息，可以避免重新登录
        'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
        'resetKeyboard': True  # 将键盘给隐藏起来
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

```

执行上述代码之后，如果发现 mumu 模拟器中的微信已经启动了，就说明基本环境已经调通了；如果执行代码后发现调不到 mumu 模拟器中的微信，先在 `cmd` 中执行一下 `adb connect 127.0.0.1:7555` 命令，再执行程序即可。

#### 添加好友

我们先来使用 Appium 实现添加好友的操作，基本过程为：打开微信-&gt;点击⊕-&gt;选择添加朋友-&gt;在搜索框输入微信号-&gt;点击搜索-&gt;点击添加到通讯录，功能的代码实现如下：

```
desired_caps = {
        "platformName": "Android",  # 操作系统
        "deviceName": "emulator-5554",  # 设备 ID
        "platformVersion": "6.0.1",  # 设备版本号
        "appPackage": "com.tencent.mm",  # app 包名
        "appActivity": "com.tencent.mm.ui.LauncherUI",  # app 启动时主 Activity
        'noReset': True,  # 是否保留 session 信息，可以避免重新登录
        'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
        'resetKeyboard': True  # 将键盘给隐藏起来
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
print('点击+号')
driver.find_element_by_id('com.tencent.mm:id/ef9').click()
time.sleep(5)
print('选择添加朋友')
driver.find_elements_by_id('com.tencent.mm:id/gam')[1].click()
time.sleep(5)
print('点击搜索框')
driver.find_element_by_id('com.tencent.mm:id/fcn').click()
time.sleep(5)
print('在搜索框输入微信号')
driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys('ityard')
time.sleep(3)
print('点击搜索')
driver.find_element_by_id('com.tencent.mm:id/ga1').click()
time.sleep(3)
print('点击添加到通讯录')
driver.find_element_by_id('com.tencent.mm:id/g6f').click()

```

简单说一下，在代码中我们通过 `driver.find_element_by_id('com.tencent.mm:id/xx')` 来获取微信上的元素，如果有重复的，则可以使用 `driver.find_elements_by_id('com.tencent.mm:id/xx')[n]` 来取，通过 `send_keys('xx')` 实现信息的输入，通过 `click()` 实现点击操作。

上面我们说了通过 `find_element(s)_by_id('com.tencent.mm:id/xx')` 来获取元素，那么如何来确定 `xx` 呢？下面来一起看一下。

首先我们点击 Appium 中的放大镜位置，如下图所示：

<img src="https://img-blog.csdnimg.cn/20201104202721298.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

点击之后会进到如下界面：

<img src="https://img-blog.csdnimg.cn/20201104202733921.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

我们在图中`所需功能`下方将代码中的 `desired_caps` 信息配置进去，配置好后点击`启动会话`按钮，启动之后我们会发现 Appium 中与 mumu 中的微信效果不一致，如下图所示：

<img src="https://img-blog.csdnimg.cn/20201104202746586.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

此时只需点击一下上图中红框圈起来的刷新按钮即可，现在我们就可以确定元素的值了（也就是上面说的 `xx`），比如：我们来确定微信中添加位置 `⊕` 的值，用鼠标点击 `⊕` 即可查看，如下图所示：

<img src="https://img-blog.csdnimg.cn/2020110420280075.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

我们接着点击 `⊕`，操作步骤为：先到 mumu 模拟器中点击微信中的 `⊕`，如下图所示：

<img src="https://img-blog.csdnimg.cn/20201104202814281.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

点击之后再到 Appium 中点击刷新按钮，如下图所示：

<img src="https://img-blog.csdnimg.cn/20201104202829548.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从图中我们可以看列表中每个选项的值都是 `com.tencent.mm:id/gam`，此时代码中我们就是用的 `driver.find_elements_by_id('com.tencent.mm:id/gam')[1]` 来取的，通过上面的介绍相信大家对 Appium 的使用已经基本了解了。

#### 发送消息

发送消息我们模拟的基本流程是：打开微信-&gt;点击搜索的放大镜-&gt;在搜索框输入好友昵称-&gt;点击搜索到的好友-&gt;发送文字+表情，代码实现如下：

```
desired_caps = {
        "platformName": "Android",  # 操作系统
        "deviceName": "emulator-5554",  # 设备 ID
        "platformVersion": "6.0.1",  # 设备版本号
        "appPackage": "com.tencent.mm",  # app 包名
        "appActivity": "com.tencent.mm.ui.LauncherUI",  # app 启动时主 Activity
        'noReset': True,  # 是否保留 session 信息，可以避免重新登录
        'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
        'resetKeyboard': True  # 将键盘给隐藏起来
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
print('点击微信搜索框')
driver.find_element_by_id('com.tencent.mm:id/f8y').click()
time.sleep(10)
print('在搜索框输入搜索信息')
driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys('Python小二')
time.sleep(3)
print('点击搜索到的好友')
driver.find_element_by_id('com.tencent.mm:id/tm').click()
time.sleep(3)
# 输入文字
driver.find_element_by_id('com.tencent.mm:id/al_').send_keys('hello')
time.sleep(3)
# 输入表情
driver.find_element_by_id('com.tencent.mm:id/anz').click()
time.sleep(3)
driver.find_element_by_id('com.tencent.mm:id/rv').click()
# 点击发送按钮发送信息
driver.find_element_by_id('com.tencent.mm:id/anv').click()
# 退出
driver.quit()

```

最后说一点，因模拟器反应可能会慢一些，如果程序执行时出错，可以将中间的等待时间 `time.sleep(x)` 设置大一些。

软件及代码在公号 **Python小二** 后台回复 **201104** 获取。
