
--- 
title:  常用adb命令 
tags: []
categories: [] 

---
###### 1、禁用APP

adb shell pm disable-user ‘包名’

###### 2、解禁APP

adb shell pm enable ‘包名’

###### 3、指定连接设备

adb -s 设备名 shell

###### 4、安装apk

adb install 包名—

说明install后可加-r -t -s -d -p等关键字

-r：替换已存在应用

-t：测试package标识

-s：将应用安装到adcard

-d：忽略版本号

-p：部分安装apk标志

使用命令安装deb文件

sudo dpkg -i 文件.deb

或

sudo apt install 文件.deb

###### 5、卸载应用

adb uninstall 包名

###### 6、卸载APP，但保存数据和缓存文件

adb uninstall -k 包名

###### 7、adb 命令更改日期

adb shell date 0822216202021.00

###### 8、查看手机所有包名

adb shell pm list packages

###### 9、查看所有三方APP包名

adb shell pm list packages -3

删除所有第三方APP:

adb shell pm list packages -3|cut -d: -f2|grep -E “[\w.]”|xargs -t -i adb uninstall {}

###### 命令解释：

adb shell pm list packages -3 //表示列出第三方可卸载app软件 | cut -d :-f2 //表示通过“:” 冒号分割取第二位程序 | grep -E “[\w.]” //表示找出符合条件的字符串(\w表示字母、数字及下划线，.表示点号)正则匹配出来 | xargs -t -i // xargs命令是给其他命令传递参数的一个过滤器 。-i 选项告诉 xargs 用每项的名称替换 {}。-t 选项指示 xargs 先打印命令，然后再执行 adb uninstall {} // 依次卸载列出的第三方app 原文链接：https://blog.csdn.net/moakey/article/details/105415884

###### 10、清除应用数据和缓存信息

adb shell pm clear 包名

###### 11、adb 命令修改时间

adb root;adb shell date 080816202021.00

###### 12、 将手机卡中的某个文件复制到电脑

输入: adb pull 手机存储路径 电脑路径

###### 13、从电脑端向手机复制文件

输入: adb push 电脑路径 手机存储路径

###### 14、repo 更新代码

repo sync -d --prune --force-sync --no-tags -f -j6

###### 15、压缩与解压缩

解压tar文件：tar zxvf 文件名

压缩：zip -r name.zip 文件名

解压zip文件：unzip name.zip --解压到当前目录下

unzip -o -d /home name.zip

-o ：不提示并且覆盖文件

-d：指明文件解压到目录下

###### 16、只查看Activity包名（过滤）

以下命令可以查看手机中当前界面是哪个Activity。

```
adb shell dumpsys activity top | grep ACTIVITY

```

如果未安装 grep for window.exe，请分开执行：

```
adb shell
然后再输入
dumpsys activity top | grep ACTIVITY

```

说明： 1、部分手机查出的Activity可能有多个。一般会包括手机桌面Activity什么的。 2、grep是linux下一个正则匹配工具，adb shell自带。 3、top表示位于栈顶。

例如

1、微信主界面Activity和朋友圈Activity：

```
com.tencent.mm/.ui.LauncherUI
com.tencent.mm/.plugin.sns.ui.SnsTimeLineUI

```

2、UC浏览器主界面Activity：

```
com.UCMobile/com.uc.browser.InnerUCMobile

```

3、QQ聊天主界面和QQ空间Activity：

```
com.tencent.mobileqq/.activity.SplashActivity
com.tencent.mobileqq/cooperation.qzone.QzoneFeedsPluginProxyActivity

```

4、支付宝首页Activity：

```
com.eg.android.AlipayGphone/.AlipayLogin

```

5、淘宝底部菜单对应的首页、微淘、消息、购物车、我的淘宝不是同一个Activity，它们依次是：

```
首页com.taobao.taobao/com.taobao.tao.homepage.MainActivity3
微淘com.taobao.taobao/com.taobao.wetao.home.WeTaoMainActivity
消息com.taobao.taobao/com.taobao.message.category.MsgCenterCategoryTabActivity
购物车com.taobao.taobao/com.taobao.android.trade.cart.CartTabActivity
我的淘宝com.taobao.taobao/com.taobao.tao.mytaobao.MyTaoBaoActivity

```

###### 17、查看 Activity 所有信息，包括fragment，view

结果信息存到手机存储卡根目录的a.txt文件：

```
dumpsys activity top &gt;/storage/emulated/0/a.txt

```

存到D盘：

```
dumpsys activity top &gt;D:/a.txt

```

说明 `&gt;` 表示控制台输出。文件不存在则创建，再输出。覆盖式写入。 如果需要追加，应使用 `&gt;&gt;a.txt`
