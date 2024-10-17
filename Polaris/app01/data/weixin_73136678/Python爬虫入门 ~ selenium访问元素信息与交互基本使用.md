
--- 
title:  Python爬虫入门 ~ selenium访问元素信息与交互基本使用 
tags: []
categories: [] 

---
### 访问元素信息

前面我们成功定位到了页面的标签元素，那接下来就该轮到获取元素的信息了，常用的函数有以下几种:

 - get_attribute
 - text
 - tag_name

#### 前置准备

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

path = 'chromedriver.exe'
browser = webdriver.Chrome(service=Service(path), options=options)

url = 'https://www.baidu.com/'
browser.get(url)
复制代码
```

#### **get_attribute**

获取元素属性，通过`get_attribute`函数，指定我们所需要的标签属性，即可得到对应的属性值。

```
obj = browser.find_element(By.ID, "su")
print(obj.get_attribute("class"))
复制代码
```


