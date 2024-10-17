
--- 
title:  Python 操作selenium 
tags: []
categories: [] 

---
#### 配置driver

下载浏览器对应的driver，连接Python和selenium，比如chrome需要使用chromedriver。

#### 下载selenium

```
pip install selenium

```

#### 配置一个测试环境（记录cookie用）

```
cd {你的chrome路径}
chrome.exe --remote-debugging-port=9222 --use-data-dir="{随便一个路径}"

```

#### 登陆获取cookie

#### 操作selenium获取连接

```
chrome_path = {<!-- -->你的软件安装路径}
config = webdriver.ChromeOptions()
config.add_experimental_option("debuggerAdress", "127.0.0.1:9222")

browser = webdriver.Chrome(executable_path = chrome_path, chrome_options=config)


```

登陆：

```
browser.get("{url}")

```

#### 获取Xpath

在Chrome浏览器中右键检查可以获取Xpath。执行Xpath以后即可登陆

对XPath进行操作：

```
browser.find_element(By.XPATH, {XPath}).send_keys

```
