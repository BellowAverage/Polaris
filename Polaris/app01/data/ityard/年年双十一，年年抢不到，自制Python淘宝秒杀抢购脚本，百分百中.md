
--- 
title:  年年双十一，年年抢不到，自制Python淘宝秒杀抢购脚本，百分百中 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/909c750120d013d471ba3e3e8aae421c.png" alt="909c750120d013d471ba3e3e8aae421c.png">

### 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/weixin_41556756/article/details/121182499

事情是这个样子的，前几天不是双十一预购秒杀嘛。

由于我女朋友比较笨，手速比较慢，就一直抢不到，她没抢到特价商品就不开心。

<img src="https://img-blog.csdnimg.cn/img_convert/07e9d88c96fcab6d020794466fb7f0c4.png" alt="07e9d88c96fcab6d020794466fb7f0c4.png">

她不开心，我也就不能跟着开心，就别提看6号的全球总决赛了。

<img src="https://img-blog.csdnimg.cn/img_convert/99bc564c51eee02a97bee94a0d3eac2e.png" alt="99bc564c51eee02a97bee94a0d3eac2e.png">

为了解决这个问题，就决定写一个自动定时抢购的脚本。

## **第一步**

首先我的思路很简单，就是让“程序”帮我们自动打开浏览器，进入淘宝，然后到购物车等待抢购时间，自动购买并支付。<img src="https://img-blog.csdnimg.cn/img_convert/da7cc082f96599373a56a90b9ae9fbbd.png" alt="da7cc082f96599373a56a90b9ae9fbbd.png">

## **第二步**

导入模块，我们需要一个时间模块，抢购的时间，还有一个Python的自动化操作。

代码如下：

```
import datetime #模块
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
import time
#全自动化Python代码操作
from selenium import webdriver
```

## **第三步**

根据我们的思路，首先需要程序帮我们打开谷歌浏览器，并输入：www.taobao.com，然后点击登录，进入到购物车。

##### 代码如下：

```
times = "2021-11-04 21:00:00.00000000"
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
time.sleep(3)                               #点击
browser.find_element_by_link_text("亲，请登录").click()
```

不过这里有一个问题就是，我们不能把我们的账户、密码写在代码里边，这样很容易泄露，所以这里采取手动扫码登录。

```
print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)
```

## **第四步**

进入购物车，等待抢购时间然后购买。

首先这个程序不能帮我们去挑选商品，所以我们得提前把商品加入到购物车里面。

等到了抢购时间，直接全选商品购买就可以了。

```
# 是否全选购物车
while True:
    try:
        if browser.find_element_by_id("J_SelectAll1"):
            browser.find_element_by_id("J_SelectAll1").click()
            break
    except:
        print(f"找不到购买按钮")




while True:
    #获取电脑现在的时间,                      year month day
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
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
