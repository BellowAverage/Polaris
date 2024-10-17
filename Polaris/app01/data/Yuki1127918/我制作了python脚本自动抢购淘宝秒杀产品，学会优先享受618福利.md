
--- 
title:  我制作了python脚本自动抢购淘宝秒杀产品，学会优先享受618福利 
tags: []
categories: [] 

---
#### 这是本文的标题
- 前言- 第一步：- 第二步：- 第三步：- 第四步：<li> 
  <ul>- 零基础Python学习指南<li> 
    <ul><li> 
      <ul>- 👉Python学习路线汇总👈- 👉Python必备开发工具👈- 👉Python学习视频600合集👈- 👉实战案例👈- 👉100道Python练习题👈- 👉面试刷题👈- 👉资料领取👈
## 前言

每到618，各位男性朋友们就要大吐血了，万一女朋友想要的东西还没有抢到，就要更加…

所以我便创造了这个自动抢购的脚本，希望对你们有用

## 第一步：

思路很简单，就是让“程序”帮我们自动打开浏览器，进入淘宝，然后到购物车等待抢购时间，自动购买并支付。 <img src="https://img-blog.csdnimg.cn/c165d6b3d9f646eb9d1039a76dc939df.png#pic_center" alt="在这里插入图片描述">

## 第二步：

导入模块，我们需要一个时间模块，抢购的时间，还有一个Python的自动化操作。代码如下：

```

import datetime #模块
now = datetime.datetime.now().strftime('Y-m-d H:M:S.f')
import time
#全自动化Python代码操作
from selenium import webdriver


```

## 第三步：

根据我们的思路，首先需要程序帮我们打开谷歌浏览器，并输入“「http://www.taobao.com」”，然后点击登录，进入到购物车。代码如下：

```
times = "2021-11-04 21:00:00.00000000"
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
time.sleep(3)                               #点击
browser.find_element_by_link_text("亲，请登录").click()


```

不过这里有一个问题就是，我们不能把我们的账户、密码写在代码里边，这样很容易泄露，所以这里采取手动扫码登录

```
print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)


```

## 第四步：

进入购物车，等待抢购时间然后购买。

首先这个程序不能帮我们去挑选商品，所以我们得提前把商品加入到购物车里面。

等到了抢购时间，直接全选商品购买就可以了。

```
#是否全选购物车
while True:
    try:
        if browser.find_element_by_id("J_SelectAll1"):
            browser.find_element_by_id("J_SelectAll1").click()
            break
    except:
        print(f"找不到购买按钮")


while True:
    #获取电脑现在的时间,                      year month day
    now = datetime.datetime.now().strftime('Y-m-d H:M:S.f')
    # 对比时间，时间到的话就点击结算
    print(now)
    #判断是不是到了秒杀时间?
    if now &gt; times:
        # 点击结算按钮
        while True:
            try:
                if browser.find_element_by_link_text("结 算"):
                    print("here")
                    browser.find_element_by_link_text("结 算").click()
                    print(f"主人,程序锁定商品,结算成功")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element_by_link_text('提交订单'):
                    browser.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
            except:
                print(f"主人,我已帮你抢到商品啦,您来支付吧")
                break
        time.sleep(0.01)


```

### 完结

希望各位小哥哥不仅能买到自己想要的礼物，还可以省好多钱钱，

学会python爬虫，像这样嫖取资源的脚本还有很多，如果大家感兴趣的话可以参考以下学习资料：

### 零基础Python学习指南

##### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。 <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png" alt="">

##### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

##### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png" alt="">

##### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。 <img src="https://img-blog.csdnimg.cn/img_convert/c16d8e403066e409687f0f537c8f3a49.png" alt="">

##### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png" alt="">

##### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/7caaa5459a9bcd39c18f532ce8a30421.png" alt="">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
