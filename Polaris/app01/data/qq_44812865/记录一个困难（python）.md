
--- 
title:  记录一个困难（python） 
tags: []
categories: [] 

---
在从一个网页跳转另一个网页（该网页是登录页面） 采用python的selenium库对网页进行自动化登录

```
import time
from selenium import webdriver
path ='chromedriver.exe'
driver =webdriver.Chrome(path)
driver.get("url")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys("username")#利用xpath找到用户输入框，并输入
driver.find_element_by_id("password").send_keys("password")#密码
driver.find_element_by_id("login_submit").click()#点击登录按钮

```

问题出现在

```
driver.find_element_by_xpath('//*[@id="username"]').send_keys("username")#利用xpath找到用户输入框，并输入

```

错误提示：

>  
 selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {“method”:“xpath”,“selector”:“//*[@id=“username”]”} (Session info: chrome=118.0.5993.71) 伪解决办法 省去跳转过程直接get登录页面的url。 


但是问题一直在，网上的解决办法俩种一种加入等待时间一种是ifame嵌入，都被排除。 ———————————————— 待解决问题！！
