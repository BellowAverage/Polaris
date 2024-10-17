
--- 
title:  解决Selenium中用find_elements_by_xpath()无法获取属性值问题 
tags: []
categories: [] 

---
解决Selenium中用find_elements_by_xpath()无法获取属性值问题

```
yanzhengma_image=driver.find_elements(by=By.XPATH, value='/html/body/form[1]/div[4]/div[4]/img/@src')

```

结果出现错误:大概意思是说列表存放的是element而不是object。

```
yanzhengma_image=driver.find_elements(by=By.XPATH, value='/html/body/form[1]/div[4]/div[4]/img')
yanzhengma_image=yanzhengma_image[0].get_attribute("src")#这里的[0],是提取列表的第一个元素
print(yanzhengma_image)

```

```
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div')


```
