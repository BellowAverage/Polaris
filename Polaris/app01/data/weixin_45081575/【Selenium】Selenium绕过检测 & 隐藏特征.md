
--- 
title:  【Selenium】Selenium绕过检测 & 隐藏特征 
tags: []
categories: [] 

---
## 前言

>  
 一文给你介绍的清清楚楚， 伪装Selenium特征的N种方式✨✨ 


在使用 Selenium 访问某些网站时候，会不成功。像很多url中带`gov` 字眼的，往往都无法正常打开。

因为网站检测到了 我们使用自动化工具，所以就给ban掉了，所以这篇文章就来说说怎么过掉它。

值得一提的是，这篇文章不针对任何一个网站，只用下面的这个网站来做参照~
- 
访问这个网站时候，可以看到它会检测很多项浏览器的信息。明显可以看到 正常浏览器 和 Selenium打开浏览器是有区别的~

<img src="https://img-blog.csdnimg.cn/aa8697ef55364fdebd64878266aa0df9.png" alt="">

输入 `window.navigator.webdriver` 时候，正常浏览器是 false，Selenium打开的是true

<img src="https://img-blog.csdnimg.cn/0280cb57762545b9ba4bbc424c9f54f1.png" alt="">

下面去看看怎么绕过检测 &amp; 隐藏特征。

## 三种方式

这里主要介绍三大类隐藏 **Selenium** 特征的方式，分别是以下：
1. 注入JS代码1. 中间人修改文件1. 接管已打开浏览器
### 1. 注入JS代码

>  
 在 **注入JS代码** 的大类中，分了三个方式来讲，大体上差别不是很大 


#### 1.1 执行cdp

**hide_features.py**

```
# -*- coding: utf-8 -*-
# Name:         hide_features.py
# Author:       小菜
# Date:         2022/8/29 2:43
# Description:

from selenium import webdriver


driver = webdriver.Chrome()

# 代码的关键所在
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {<!-- -->
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () =&gt; false
    })
  """
})


driver.get('https://bot.sannysoft.com/')


```

代码释义：
- driver.execute_cdp_cmd ：执行 `Chrome Devtools Protocol `命令- Page.addScriptToEvaluateOnNewDocument：在浏览器启动之前执行给定的JS脚本- Object.defineProperty：JS语法，直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，并返回此对象（代码中是将 `navigator.webdriver` 设置为 `undefined`
**CDP文档**：

<img src="https://img-blog.csdnimg.cn/e15b47dd188645e9958891bd05b202a5.png" alt="">

代码运行效果如下：
- 明明 `window.navigator.webdriver` 输出已经是 false 了，为啥还是不通过？
<img src="https://img-blog.csdnimg.cn/52ec74a94510427cb647b8f5bd96fc72.png" alt="">

看下图，差别在这里
- 注：有部分网站不会检测的这么深，在这一步其实就可以绕过检测了
<img src="https://img-blog.csdnimg.cn/1dfa228988a943bc8ac8945e61782f60.png" alt="">

继续讲如何更深入的绕过检测~

#### 1.2 执行cdp_2

>  
 这里分两步走，需要先获取 隐藏特征的JS文件，然后再将JS代码注入到Selenium中 


##### 1.2.1 获取隐藏特征文件

>  
 隐藏特征文件的官方文档： 


如果没有科学的话，生成一份还是比较耗时间的，所以我也准备了一份，点击即可下载 

隐藏特征文件的简介和获取如下图所示：
- 可以将最新的隐身规避从 `puppeteer-extra-stealth` 提取到一个js文件中。生成的JS文件可以用于纯CDP实现，也可以用于测试devtools中的规避。- 只要安装了`NodeJS`，就可以一行代码即可拿下~- 将在当前文件夹中创建一个 `stealth.min.js` 文件。
<img src="https://img-blog.csdnimg.cn/b6eaa29f9b434e15a55aeaaba5c10673.png" alt="">

在cmd窗口输入 `npx extract-stealth-evasions`，稍后便可以看到生成的 `stealth.min.js` 文件了。

<img src="https://img-blog.csdnimg.cn/277439926eb843c88be870a1773ab2d4.png" alt="在这里插入图片描述">

```
# -*- coding: utf-8 -*-
# Name:         hide_features.py
# Author:       小菜
# Date:         2022/8/29 122:43
# Description:

from selenium import webdriver

driver = webdriver.Chrome()

with open('stealth.min.js', mode='r') as f:
    js = f.read()


# 关键代码
driver.execute_cdp_cmd(
    cmd_args={<!-- -->'source': js},
    cmd="Page.addScriptToEvaluateOnNewDocument",
)

driver.get('https://bot.sannysoft.com/')


```

代码运行如下图所示：
- 现在，正常的浏览器和Selenium浏览器都一样了，都可以通过检测~- 虽然一个是 false 一个是undefined（但并不影响~
<img src="https://img-blog.csdnimg.cn/2a0b438bac9a4a818240f83d53cea197.png" alt="">

后续再访问任何网页都能成功隐藏Selenium 的特征了，但是只能在当前页面去操作~

值得注意的是：如果新开一个网页再去访问，那就没法隐藏特征了，看下图
- 所以这个方法也是不够完美的~
<img src="https://img-blog.csdnimg.cn/f34147910b264f43a26a20e0bcb58347.png" alt="">

#### 1.3 添加 ChromeOptions &amp; 修改默认参数

>  
 这个不算是注入JS的内容，是修改默认参数的，只是并到了一块儿； 到第三种方法了，这个只需要添加一个参数即可~ 


这个方法的出处在这里：

**代码**

```
# -*- coding: utf-8 -*-
# Name:         hide_features.py
# Author:       小菜
# Date:         2022/8/29 22:43
# Description:

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)


driver.get('https://bot.sannysoft.com/')


```

代码释义：
- `disable-blink-features=AutomationControlled`：禁用 blink 特征


<img src="https://img-blog.csdnimg.cn/72b884ea3d4c4ecaa93dbcd91eccd9bd.png" alt="在这里插入图片描述">

代码运行效果如下：
- 通过检测，且新开的窗口也同样可以通过检测 <img src="https://img-blog.csdnimg.cn/82b08ab3b8f24fae8b8e41c62370227d.png" alt="">
新开一个窗口 <img src="https://img-blog.csdnimg.cn/716214fa608f421898f584e80d14120d.png" alt="">

可见，这个操作是相对完美了。 因为没有做过详尽的测试，所以我无法保证这个方法是否能100%适用~ 如果网站检测的信息有很多，甚至检测 经纬度、ip代理等。那可能就会失效！

### 2：中间人抓包修改文件

>  
 一个思路，不属于是好方法的思路 


这个方法就介绍一下思路吧， 在可以找到网站检测代码的前提下，去替换检测代码的文件。 可以使用抓包工具，如 `Charles、fiddler、mitmproxy`等去监听检测文件，然后替换它 也可以使用 `Chrome浏览器 -&gt; 开发者工具 -&gt; Sources -&gt; Overrides` 去做替换 替换的方法有很多，

但我觉得这不是一个好方法，只是也是一种方法。

### 3. 接管已打开浏览器

>  
 这个网站没法检测出来，完美如斯。正常的浏览器是咋样的，这个就是咋样的 


接管已经打开的浏览器（强烈推荐

如何接管已经打开的浏览器，参考这两篇文章，这里不再赘述

<th align="left">标题</th>|链接
|------
<td align="left"></td>|https://blog.csdn.net/weixin_45081575/article/details/112621581
<td align="left"></td>|https://blog.csdn.net/weixin_45081575/article/details/126389273

**代码**

```
# -*- coding: utf-8 -*-
# Name:         hide_features.py
# Author:       小菜
# Date:         2022/8/29 22:43
# Description:

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    os.system(r'start chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    driver = webdriver.Chrome(options=options)
    driver.get('https://bot.sannysoft.com/')


```

代码运行如下：
- 无论打开多少个窗口，都是可以通过检测的
<img src="https://img-blog.csdnimg.cn/ad4091aec5e44ac7ac4e7a3110aaac03.png" alt="">

### 总结

上面介绍了三大类隐藏 **Selenium** 特征的方式，但是最好用是 第三种，即
- 接管已经打开的浏览器端口，不用担心被网站所检测到，因为它就是你正常使用的浏览器
使用起来也很简单，调用cmd命令去打开浏览器然后再使用 **Selenium** 去接管即可。

## 后话

自己动手，试验一番，岂不美哉~ see you🐱‍🏍🐱‍🏍
