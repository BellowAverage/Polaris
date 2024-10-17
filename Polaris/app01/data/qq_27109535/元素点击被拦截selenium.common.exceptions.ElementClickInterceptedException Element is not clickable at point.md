
--- 
title:  元素点击被拦截selenium.common.exceptions.ElementClickInterceptedException Element is not clickable at point 
tags: []
categories: [] 

---
元素点击被拦截异常 该元素不能被点击，本地点击将会被转移到其他元素上

```
selenium.common.exceptions.ElementClickInterceptedException Element is not clickable at point

```

## 点击登录按钮

```
element = driver.find_element(By.XPATH, '//button[@class="el-button el-button--default el-button--medium"]')
driver.execute_script("arguments[0].click();",element )

```
