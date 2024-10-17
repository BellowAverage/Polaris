
--- 
title:  我每天使用的5个Python自动化脚本 
tags: []
categories: [] 

---
### 介绍

Python是一种功能强大的编程语言，可用于自动执行各种任务。无论您是开发小型项目还是大型企业应用程序，Python 都可以帮助您节省时间并简化您的工作流程。

Python是一种伟大的语言，因为它的语法非常简单。10行Python代码完成的工作，在Javascript或C++这样的语言中，需要20行代码。下面是一个简单的 Web 请求的示例：

```
import requests 
r = requests.get("https://www.python.org") 
print(r.status_code)
print(r.text)

```

下面是完成相同功能的Javascript代码：

```
fetch(“https://www.python.org")
.then(res =&gt; {<!-- -->
  if(res.ok) {<!-- -->
    return res.text();
  } else {<!-- -->
    throw new Error(“HTTP error, status = “ + res.status);
  }
})
.then(text =&gt; {<!-- -->
  console.log(text);
})
.catch(error =&gt; {<!-- -->
  console.log(error);
});

```

如您所见，Python 代码比 Javascript 代码更容易理解，这使其成为自动执行重复性任务的理想选择，例如 Web 抓取、数据收集或翻译。以下是我最常做的五个重复性任务，我用 Python 来完成它们。

### 网址缩短器

```
importpyshorteners

s = pyshorteners.Shortener(api_key="YOUR_KEY")
long_url =input("Enter the URL to shorten: ")
short_url = s.bitly.short(long_url)
print("The shortened URL is: "+ short_url)

```

在URL缩短方面，Pyshorteners库是我最喜欢的库之一，可用于各种项目。大多数链接缩短器都需要一个 API 密钥，但除非您预计会有数十万个请求，否则它们通常是免费的。我发现像 Bit.ly，Adf.ly 和Tinyurl这样的API非常适合SaaS应用程序和Telegram机器人。

### 创建伪信息

```
import pandas as pd
from faker import Faker

# Create object
fake = Faker()

# Generate data
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=5)

# Dataframe creation
fakeDataframe = pd.DataFrame({<!-- -->‘date’:[fake.date() for i in range(5)],
 ‘name’:[fake.name() for i in range(5)],
 ‘email’:[fake.email() for i in range(5)],
 ‘text’:[fake.text() for i in range(5)]})
print(fakeDataframe)

```

如果您需要创建一个假人（伪造的角色），这个伪造者库为您提供了一个伪造者类，可以自动生成整个假人。此脚本创建几个不同的人并将他们存储在数据Frame中，这是一个稍微复杂的概念。如果我不得不向不太信任的网站提供信息，或者如果我不想其他人追溯到我的任何信息，我会使用这些假人信息。

### 优酷视频下载器

```
from pytube import YouTube

link = input("Enter a youtube video's URL") # i.e. https://youtu.be/dQw4w9WgXcQ

yt = Youtube(link)
yt.streams.first().download()

print("downloaded", link)

```

很简单。它使用 pytube 库将您提供的任何链接转换为文件，然后下载它。使用五行代码且没有 API 速率限制，您可以将其与另一个脚本结合使用来转录视频并使用情绪分析来确定视频包含的内容类型。

### 北约音标加密器

```
def encrypt_message(message):
   nato_alphabet = {<!-- -->
   ‘A’: ‘Alfa’, ‘B’: ‘Bravo’, ‘C’: ‘Charlie’, ‘D’: ‘Delta’,
   ‘E’: ‘Echo’, ‘F’: ‘Foxtrot’, ‘G’: ‘Golf’, ‘H’: ‘Hotel’,
   ‘I’: ‘India’, ‘J’: ‘Juliet’, ‘K’: ‘Kilo’, ‘L’: ‘Lima’,
   ‘M’: ‘Mike’, ’N’: ‘November’, ‘O’: ‘Oscar’, ‘P’: ‘Papa’,
   ‘Q’: ‘Quebec’, ‘R’: ‘Romeo’, ‘S’: ‘Sierra’, ‘T’: ‘Tango’,
   ‘U’: ‘Uniform’, ‘V’: ‘Victor’, ‘W’: ‘Whiskey’, ‘X’: ‘Xray’,
   ‘Y’: ‘Yankee’, ‘Z’: ‘Zulu’
   }

   encrypted_message = “”

# Iterate through each letter in the message
   for letter in message:

  # If the letter is in the dictionary, add the corresponding codeword to the encrypted message
     if letter.upper() in nato_alphabet:
     encrypted_message += nato_alphabet[letter.upper()] + “ “

  # If the letter is not in the dictionary, add the original letter to the encrypted message
     else:
     encrypted_message += letter

  return encrypted_message


message = "Hello World"
encrypted_message = encrypt_message(message)
print("Encrypted message: ", encrypted_message)

```

此函数对传递到其输入参数的任何消息进行编码，并输出相应的 NATO 字序列。这工作正常，因为它检查每个字符是否在 nato_alphabet 字典中，如果是，它将被附加到加密邮件中。如果在字典中找不到该字符（如果是空格、冒号或任何不是 a-z 的内容），则会在没有任何特殊编码的情况下追加该字符。因此，“Hello World”变成了“利马回声酒店利马奥斯卡”“威士忌奥斯卡罗密欧利马三角洲”。

### 社交媒体登录自动化

```
from selenium import webdriver

driver = webdriver.Firefox()
driver.get(“https://www.facebook.com/")

# Find the email or phone field and enter the email or phone number
email_field = driver.find_element_by_id(“email”)
email_field.send_keys(“your_email_or_phone”)

# Find the password field and enter the password
password_field = driver.find_element_by_id(“pass”)
password_field.send_keys(“your_password”)

# Find the login button and click it
login_button = driver.find_element_by_id(“loginbutton”)
login_button.click()

```

此代码利用 Selenium，一个流行的 Web 自动化库。它打开一个 Web 浏览器，并根据代码中给出的各种命令进行导航。在这个特定的代码块中，浏览器将跳转到Facebook，并在网页上找到要修改的特定元素。在这里，我们在电子邮件和密码字段中输入某些字符，然后单击“登录”按钮。如果提供了有效的凭据，这将自动登录用户。

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以找到适合自己的学习方案 


包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！

## 零基础Python学习资源介绍

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）** <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
