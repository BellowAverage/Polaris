
--- 
title:  Selenium get_attribute()方法获取元素信息（文本和属性） 
tags: []
categories: [] 

---
### 获取文本

```
fangwuyongtu=browser.find_elements(by=By.XPATH,value='/html/body/div[1]/div/div/table[2]/tbody/tr[2]/td[2]')
fangwuyongtu =fangwuyongtu[0].get_attribute("textContent").strip()

```

### 获取属性

```
fangwuyongtu=browser.find_elements(by=By.XPATH,value='/html/body/div[1]/div/div/table[2]/tbody/tr[2]/td[2]')
fangwuyongtu =fangwuyongtu[0].get_attribute("class")

```
