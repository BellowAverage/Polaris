
--- 
title:  你需要知道的 Selenium4 新特性 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/17b79d7d951d4b13af8f0d85f49f9ddf.png#pic_center=1080x1920" alt="插入图片">

## 前言

>  
 最近又用到了**Selneium**，发现已经来到了 **4.9+** 版本了。本篇文章来介绍下它较比 **Selenium3** 的一些新特性。 


记录下，当是做笔记了。 最令人惊喜的是，**Selenium4** 会自动回收浏览器资源。

本文所使用的 **Selenium** 版本为 <font color="blackyellow" size="6"> 4.9.9</font>

## 知识点📖📖

|作用|链接
|------
|**WebDriver文档**|

**更新模块**
- 使用**Selenium4**，要求 **Python**版本为 **3.7** 或者更高。
```
pip install --upgrade selenium

```

## 新特性🧐🧐

>  
 这里只展示常用到的一些特性。具体的可以通过上面给出的官方文档去进行系统的学习。 


### 1. 定位语法

>  
 大体上一致，变化不大。但是 **Selenium4** 不支持 **Selenium3** 的这种定位方法。 


在Selenium3中，

```
driver.find_element_by_xpath('demo')
driver.find_elements_by_xpath('demo')

```

而在Selenium4中，

```
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, "demo")
driver.find_elements(By.XPATH, "demo")

```

### 2. 相对定位器

>  
 使用**JavaScript**函数 来确定页面上元素的大小和位置，并且可以使用此信息来定位相邻元素。 


>  
 **Selenium 4**引入了相对定位器。当不方便定位到一个元素，但却可以定位到该元素在空间上的其它元素。这个时候就可以使用相对位置去定位（用于辅助定位，还是很不错的。 


以下面的图片为例（共六个元素：
- 它们的标签属性值如下所示
|元素|TAG_NAME|ID
|------
|**Email Address**标签||lbl-email
|邮箱输入框|input|
|**Password**标签||lbl-password
|密码输入框|input|
|**Cancel**按钮|button|cancel
|**Sunmit**按钮|button|submit

<img src="https://img-blog.csdnimg.cn/e7d3602616c14e8d998da06311810c74.png" alt="在这里插入图片描述">

#### 导入模块

```
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

```

#### Above ☝

>  
 定位位于 Password标签上面的 **邮箱输入框** 


```
passwd_label = driver.find_element(By.ID, 'lbl-password')

element = driver.find_element(locate_with(By.TAG_NAME, 'input').above(passwd_label))

```

#### Below 👇

>  
 定位位于 Email Address标签下方的 **邮箱输入框** 


```
email_label = driver.find_element(By.ID, 'lbl-email')

element = driver.find_element(locate_with(By.TAG_NAME, 'input').above(email_label ))

```

#### Left of 👈

>  
 定位位于 **Submit按钮** 左边的 **Cancel按钮** 


```
btn_submit = driver.find_element(By.ID, 'submit')

element = driver.find_element(locate_with(By.TAG_NAME, 'button').to_left_of(btn_submit))


```

#### Right of👉

>  
 定位位于 **Cancel按钮** 右边的 **Submit按钮** 


```
btn_cancel = driver.find_element(By.ID, 'cancel')

element = driver.find_element(locate_with(By.TAG_NAME, 'button').to_right_of(btn_cancel))

```

#### Near 🤝

>  
 定位位于 **Cancel按钮** 旁边的 **Submit按钮** 


```
btn_cancel = driver.find_element(By.ID, 'cancel')

element = driver.find_element(locate_with(By.TAG_NAME, 'button').near(btn_cancel))

```

### 3. 弃用消息

#### 已弃用⚡

>  
 这里 `chromedriver.exe` 驱动文件与 **.py** 文件在用一个目录下， 


下面是 **Selenium3** 的创建一个浏览器的写法。

**Selenium3**

```
from selenium import webdriver

CHROMEDRIVER_PATH = './chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

```

这份代码在 **Selenium4** 执行，会有有一个弃用警告
- `DeprecationWarning: executable_path has been deprecated, please pass in a Service object`- 弃用警告: executable_path已弃用，请传入一个**Service** 对象
<img src="https://img-blog.csdnimg.cn/6de4515aff0b460e968a90c9cec73639.png" alt="在这里插入图片描述">

#### 新特性✨

所以在 <font color="inkblue">**Selenium4**</font> ，创建一个浏览器的写法如下：

**Selenium4**

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

CHROMEDRIVER_PATH = './chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

```

### 4. 自动回收浏览器资源

跟一下 **Selenium4** 的源码，可以看到以下：
- 在 程序运行结束之前，这里会停止 **Service** 服务，于是 浏览器资源就释放了~- 这跟我们手动调用 <font color="pink"> `driver.service.stop()` </font>是一样的。
<img src="https://img-blog.csdnimg.cn/546196fba5e9460ebff58022066daacf.png" alt="在这里插入图片描述">

#### 保持浏览器的打开状态✨

>  
 将 **detach** 参数设置为 **true** 将在驱动过程结束后保持浏览器的打开状态。 

- 将这一行代码添加到 **options** 中即可~
```
options.add_experimental_option("detach", True)

```

## 总结🐱‍🏍🐱‍🏍

本文章介绍了**Selenium 4**相对于**Selenium 3**的一些新特性和变化。
- **Selenium 4** 可以自动回收浏览器资源，不需要手动停止服务，使得代码更加简洁；- 定位语法方面，**Selenium 4**引入了新的定位方法，使用By类来替代之前的find_element_by系列方法；- **Selenium 4**还引入了相对定位器，通过使用JavaScript函数getBoundingClientRect()可以定位到页面上元素的相对位置，这对于辅助定位非常有用- 文章还介绍了一些已经弃用的特性，并给出了新的替代方法。
**Selenium4**挺好的，拥抱变化~

## 后话

本次分享到此结束， see you~~🏹🏹
