
--- 
title:  使用Python的Selenium进行网络自动化的入门教程 
tags: []
categories: [] 

---


## 使用Python的Selenium进行网络自动化入门

自动化可以被看作是在使用电子机器或机器人来执行任务的过程中去除人力的过程。

在这篇文章中，我们将研究网络流程的自动化。

让软件机器人在网络上自动执行流程和任务的能力被称为网络自动化。

使用网络自动化，我们可以做很多事情，例如。
- 搜索网络。- 删除电子邮件。- 填写表格。- 登录网站。
在现代社会中，对执行重复性任务的速度的需求是必须的，这使得自动化成为必要。

Selenium是一个框架，用于网络应用程序测试、自动化软件测试和刮擦网络。

在python中，Selenium可以被看作是一套帮助开发者与网络互动的库，以实现网络流程的自动化。

当涉及到与网络浏览器的交互时，Selenium是一个非常强大的工具，它支持所有现代的网络浏览器，可以用各种编程语言进行编码，如Java、Python、C#等。

在本指南中，我们将研究如何使用Selenium来编写脚本，用Python来自动完成基本的网络任务。

#### 前提条件

要理解本指南，读者必须熟悉。
- HTML标签、元素、ID和类。- Python编程语言的基础知识
#### 目标

在本指南中，我们将专注于建立两个Python自动化脚本。

一个将根据关键词 "大学 "进行谷歌搜索，另一个将自动登录。

在本指南的最后，读者将能够写出能够的python脚本。
- 在浏览器中查找元素。- 在浏览器中向表格区域插入文本。- 点击浏览器中的按钮。
预期的结果将是。



#### <img alt="" height="509" src="https://img-blog.csdnimg.cn/5dd9f95f973a45dd99a17237f786b4f1.png" width="899">设置环境

 

首先，我们需要在Python中创建一个虚拟环境。

为了与selenium一起工作，我们将不得不安装selenium。要安装，使用下面的命令。 

```
pip install selenium
复制代码
```

我们还必须安装一个网络驱动器（网络自动化所需的工具）。网络驱动程序帮助我们与浏览器进行交互。

如果你使用的是Windows，我们将使用一个被称为`chocolatey` 的windows软件包管理器来安装网络驱动程序。

要安装，我们将使用下面的命令。

```
choco install chromedriver
复制代码
```

如果你使用的是macOS，我们将使用下面的命令。

```
brew cask install chromedriver
复制代码
```

`chromedriver` 的版本应该与你的浏览器版本兼容。

如果你遇到兼容性错误，那么下载基于你的浏览器版本的驱动程序。

#### 自动进行谷歌搜索

创建一个文件`app.py` ，并添加以下代码。

```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
复制代码
```

上面的代码片段用于打开浏览器并请求一个网页`url` 。

第一行代码从Selenium导入web驱动。第二行打开chrome的web驱动`driver` 。

>  
 注意：不同的浏览器有不同的网络驱动。如果你喜欢使用不同的浏览器，请在互联网上浏览该驱动程序的名称。 


例如，我们会使用`firefoxDriver` ，用于Firefox浏览器。

在第三行，我们使用`driver` ，向浏览器发送请求，要求使用`url` 。

你可以使用下面的命令运行该代码。

```
python app.py
复制代码
```

上述代码打开了Chrome浏览器，如下图所示。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ce61b69520b06e4144b90d1845b74df8.png">

接下来，我们将在谷歌网站的搜索栏中输入一个`search` 关键词。要做到这一点，我们将不得不通过检查页面来获得搜索字段的元素。

要检查该页面，请在谷歌网站页面上点击右键，然后点击`Inspect element` 。

浏览器将打开一个窗口，如下图所示。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/fe039ecf6dae61c908a8660d7fbef3cb.png">

在继续之前，我们需要了解什么是Selenium中的定位器。

**定位器**是我们可以在网页上识别网络元素的方法。它们帮助我们找到网页上的任何元素。

我们可以用不同类型的定位器来识别网页上的元素。它们包括 -`id`,`class`,`name`, 和`xpath` 。

我们使用它们，如下图所示。
- `find_element_by_id`.- `find_element_by_name`.- `find_element_by_className`.- `find_element_by_xpath`.
从上面的`id`,`name`, 和`className` 是HTML属性，用于在HTML标签内控制其行为。

`xpath` 代表可扩展标记语言路径**（XML path**）是一种在网页上寻找元素的语法。

要获得该元素，请在`div` 标签上悬停，并不断打开突出搜索栏的标签，直到找到只突出搜索栏的标签。

然后，右击该标签，点击复制`xpath` 。接下来，粘贴`xpath` ，如图所示。

```
searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchField.send_keys('university')

searchField.submit()
复制代码
```

从上面的代码片断来看。
- 我们用复制的`xpath` 的值初始化了变量`searchField` 。- `send_keys()` 是用来在 对象中插入文本的。`searchField`- `searchField.send_keys('university')` 在搜索框中插入值 。`university`- `searchField.submit()` 提交搜索请求。
>  
 注意：如果网页上有这样的元素，你也可以搜索`submit` 按钮，并对其使用`click()` 方法。但是，`submit()` 方法使它更容易。 


你的完整代码将看起来像下面的片段。

```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchField.send_keys('university')

searchField.submit()
复制代码
```

如果你运行你的代码，它将打开浏览器，请求谷歌网页，在搜索框中输入`university` 值，并自动提交。

#### 自动登录到一个网站

利用我们从前面的例子中学到的东西，让我们尝试登录Quora网站。要做到这一点，让我们在我们的项目目录中创建一个新文件，名称为`main.py` 。将下面的代码粘贴或输入到该文件中。

```
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.quora.com/') # Open Quora website

emailField = driver.find_element_by_xpath('//*[@id="email"]') # HTML tag element for email field
emailField.send_keys('YourEmail') # Login user name

passwordField = driver.find_element_by_xpath('//*[@id="password"]') # HTML tag element for password field
passwordField.send_keys('YourPassword') # Login password

button = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button/div/div/div') # HTML tag element for button

button.click() # onClick event handler for HTML button
复制代码
```

从上面的代码片段来看。
- 首先，我们从`selenium` 中导入`webdriver` 。- 为了避免多次使用`webdriver.Chrome()` ，我们将它们存储在一个变量中`driver` 。- `driver.get('https://www.quora.com/')` 向发送一个请求。- `emailField = driver.find_element_by_xpath('//*[@id="email"]')` 通过 找到 字段。`xpath` `email`- `emailField.send_keys('YourEmail')` 将电子邮件地址插入到 字段中。`email`- `passwordField = driver.find_element_by_xpath('//*[@id="password"]')` 通过 找到密码字段。`xpath`- `passwordField.send_keys('YourPassword')` 将密码插入到 字段中。`password`- `button = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button/div/div/div')`，通过`xpath` 找到`login` 按钮。- `button.click()` 点击 按钮。`login`
当你运行该应用程序时，Chrome浏览器会打开，向Quora网站发送请求，填写登录细节，并将你登录到你的Quora账户。

#### 结论

总之，我们能够编写两个Python脚本，进行谷歌搜索并登录Quora。

理解了上面的两个例子，你就会明白如何使用selenium来。
- 直接到任何URL。- 查找任何HTML元素。- 填写和提交任何表格。