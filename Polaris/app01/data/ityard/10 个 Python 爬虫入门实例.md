
--- 
title:  10 个 Python 爬虫入门实例 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/b86f79dcea46fee29fcd09fe8dd49a1a.png">

来源：cnblogs.com/h3zh1/p/12548946.html

带伙伴们学习python爬虫，准备了几个简单的入门实例，分享给大家。

>  
  涉及主要知识点: 
  - web是如何交互的- requests库的get、post函数的应用- response对象的相关函数，属性- python文件的打开，保存 
 

代码中给出了注释，并且可以直接运行哦

如何安装requests库(安装好python的朋友可以直接参考，没有的，建议先装一哈python环境)

#### windows用户，Linux用户几乎一样:打开cmd输入以下命令即可，如果python的环境在C盘的目录，会提示权限不够，只需以管理员方式运行cmd窗口

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

```

Linux用户类似(ubantu为例): 权限不够的话在命令前加入sudo即可

```
sudo pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

```

#### 

#### **1. 爬取强大的BD页面，打印页面信息**

```
# 第一个爬虫示例,爬取百度页面


import requests #导入爬虫的库，不然调用不了爬虫的函数


response = requests.get("http://www.baidu.com")  #生成一个response对象


response.encoding = response.apparent_encoding #设置编码格式


print("状态码:"+ str( response.status_code ) ) #打印状态码


print(response.text)#输出爬取的信息

```

#### 

#### **2. 常用方法之get方法实例，下面还有传参实例**

```
# 第二个get方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


response = requests.get("http://httpbin.org/get")  #get方法


print( response.status_code ) #状态码


print( response.text )

```

#### 

#### 

#### **3. 常用方法之post方法实例，下面还有传参实例**

```
# 第三个 post方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


response = requests.post("http://httpbin.org/post")  #post方法访问


print( response.status_code ) #状态码


print( response.text )

```

#### 

#### **4. put方法实例**

```
# 第四个 put方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


response = requests.put("http://httpbin.org/put")  # put方法访问


print( response.status_code ) #状态码


print( response.text )

```

#### 

#### **5. 常用方法之get方法传参实例(1)**

如果需要传多个参数只需要用&amp;符号连接即可如下：

```
# 第五个 get传参方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


response = requests.get("http://httpbin.org/get?name=hezhi&amp;age=20")  # get传参


print( response.status_code ) #状态码


print( response.text )

```

#### 

#### **6. 常用方法之get方法传参实例(2)**

params用字典可以传多个

```
# 第六个 get传参方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


data = {
  "name":"hezhi",
  "age":20
}
response = requests.get( "http://httpbin.org/get" , params=data )  # get传参


print( response.status_code ) #状态码


print( response.text )

```

#### 

#### **7. 常用方法之post方法传参实例(2) 和上一个有没有很像**

```
# 第七个 post传参方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


data = {
  "name":"hezhi",
  "age":20
}
response = requests.post( "http://httpbin.org/post" , params=data )  # post传参


print( response.status_code ) #状态码


print( response.text )

```

#### 

#### **8. 关于绕过反爬机制，以zh爸爸为例**

```
# 第好几个方法实例


import requests #先导入爬虫的库，不然调用不了爬虫的函数


response = requests.get( "http://www.zhihu.com")  #第一次访问知乎，不设置头部信息


print( "第一次,不设头部信息,状态码:"+response.status_code )# 没写headers，不能正常爬取，状态码不是 200


#下面是可以正常爬取的区别，更改了User-Agent字段


headers = {


    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"


}#设置头部信息,伪装浏览器


response = requests.get( "http://www.zhihu.com" , headers=headers )  #get方法访问,传入headers参数，


print( response.status_code ) # 200！访问成功的状态码


print( response.text )

```

#### 

#### **9. 爬取信息并保存到本地**

#### 因为目录关系，在D盘建立了一个叫做爬虫的文件夹，然后保存信息

注意文件保存时的encoding设置

```
# 爬取一个html并保存


import requests


url = "http://www.baidu.com"


response = requests.get( url )


response.encoding = "utf-8" #设置接收编码格式


print("\nr的类型" + str( type(response) ) )


print("\n状态码是:" + str( response.status_code ) )


print("\n头部信息:" + str( response.headers ) )


print( "\n响应内容:" )


print( response.text )


#保存文件
file = open("D:\\爬虫\\baidu.html","w",encoding="utf")  #打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制


file.write( response.text )


file.close()

```

#### 

#### **10. 爬取图片，保存到本地**

```
#保存百度图片到本地


import requests #先导入爬虫的库，不然调用不了爬虫的函数


response = requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")  #get方法的到图片响应


file = open("D:\\爬虫\\baidu_logo.gif","wb") #打开一个文件,wb表示以二进制格式打开一个文件只用于写入


file.write(response.content) #写入文件


file.close()#关闭操作，运行完毕后去你的目录看一眼有没有保存成功

```

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/71a47e9fac1e44f43f4d8ffeac423076.gif">

微信扫码关注，了解更多内容
