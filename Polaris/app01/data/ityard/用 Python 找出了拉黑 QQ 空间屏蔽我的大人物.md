
--- 
title:  用 Python 找出了拉黑 QQ 空间屏蔽我的大人物 
tags: []
categories: [] 

---
### **前景提要**

最近发现有人QQ空间对我展开了屏蔽，咱们也不知道怎么惹到人家了，一气之下写了一个小爬虫看看到底谁把我屏蔽了。写小本本记下来！！！

#### 

### **准备工作**

```
python环境：
python3.7.4


第三方库环境：
requests
lxml
threadpool
selenium
```

#### 

### **利用selenium模拟登陆获取cookie并保存到本地**

```
def search_cookie(): # 先检测一下是否运行过
    if not __import__('os').path.exists('cookie_dict.txt'):
        get_cookie_json()
    with open('cookie_dict.txt', 'r') as f:
        cookie=json.load(f)
    return cookie


def get_cookie_json(): # 无头selenium登陆
  qq_number = input('请输入qq号:')
    password = __import__('getpass').getpass('请输入qq密码:')
    from selenium import webdriver
    login_url = 'https://i.qq.com/'
    chrome_options =Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(login_url)
    driver.switch_to_frame('login_frame')
    driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="u"]').send_keys(qq_number)
    driver.find_element_by_xpath('//*[@id="p"]').send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login_button"]').click()
    time.sleep(1)
    cookie_list = driver.get_cookies()
    cookie_dict = {}
    for cookie in cookie_list:
        if 'name' in cookie and 'value' in cookie:
            cookie_dict[cookie['name']] = cookie['value']
    with open('cookie_dict.txt', 'w') as f:
        json.dump(cookie_dict, f)
    return True
```

#### 

### **找到查看好友的接口**

进入我的空间，点击 F12 检查界面，将 Network 清空后点击好友界面。<img src="https://img-blog.csdnimg.cn/img_convert/b1efd451388a6f21a98244b39cb31da8.png" alt="b1efd451388a6f21a98244b39cb31da8.png">首选盲猜好友列表含有friend字段。直接选择搜索发现出来一些数据，挨个查找之后发现好友字段。保存当前获得的 url 供日后查询。<img src="https://img-blog.csdnimg.cn/img_convert/6cc25231d3b74d6599a7a99e33898d57.png" alt="6cc25231d3b74d6599a7a99e33898d57.png">

### **破解data里面的加密参数**

<img src="https://img-blog.csdnimg.cn/img_convert/f46c5251b555bea65b1b3d59821b7208.png" alt="f46c5251b555bea65b1b3d59821b7208.png">看到只有一个 g_tk 加密参数就很激动，就一个加密！

去 Sources 里面搜索 g_tk 取值到底是什么加密，发现是个函数点进去看后发现是个简单的小加密。可以写 python 代码。

<img src="https://img-blog.csdnimg.cn/img_convert/8778a186cb49125fd3ed9d9f6defdf03.png" alt="8778a186cb49125fd3ed9d9f6defdf03.png">

<img src="https://img-blog.csdnimg.cn/img_convert/62e85295eebac4bcd29f42c9b9a64d40.png" alt="62e85295eebac4bcd29f42c9b9a64d40.png">

Python代码如下：

```
def get_g_tk(): # QQ空间的加密算法
    p_skey = cookie['p_skey']
    h = 5381
    for i in p_skey:
        h += (h &lt;&lt; 5) + ord(i)
        g_tk = h &amp; 2147483647
    return g_tk
```

#### 

### **在QQ空间好友栏获取好友列表**

拿到加密参数后，接下来我们就只需要进刚才所说的空间好友栏页面将所有的好友的QQ号抓下来，用urllib.parse.urlencode(data)将参数转成我们常见的url后面缀了一长串&amp;&amp;&amp;的形式与原始链接拼接，然后就可以带上cookies发送请求获取json数据。

```
def get_friends_uin(g_tk): # 获得好友的QQ号信息
    yurl = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?'
    data = {
            'uin': cookie['ptui_loginuin'],
            'do': 1,
            'g_tk': g_tk
            }
    url = yurl + urllib.parse.urlencode(data)
    res=requests.get(url, headers = headers, cookies = cookie)
    r = res.text.split('(')[1].split(')')[0]
    friends_list=json.loads(r)['data']['items_list']
    friends_uin=[]
    for f in friends_list:
        friends_uin.append(f['uin'])
    return friends_uin
```

#### 

### **找到屏蔽我的狠人**

拿到好友的QQ号之后，咱们就能直接访问好友的空间了，但是好友设置了拒绝访问，一定要拿小本本记下来！

<img src="https://img-blog.csdnimg.cn/img_convert/9ce402f40cfe8e93f65cb914f149caf0.png" alt="9ce402f40cfe8e93f65cb914f149caf0.png">

```
def get_blacklist(friends): # 查询被挡好友的QQ号，用小本本记下来!
    access_denied=[] # 拉黑笔记，小本本记下来！
    yurl = 'https://user.qzone.qq.com/'
    for friend in friends:
        print("开始检查:"+str(friend))
        url = yurl + str(friend)
        res = requests.get(url,headers=headers,cookies=cookie)
        tip = etree.HTML(res.text).xpath('/html/body/div/div/div[1]/p/text()')
        if len(tip) &gt; 0:
            #if tip[0][:7] == "主人设置了权限":
            print(str(friend)+"把我拉黑了!")
            access_denied.append(friend)
    return access_denied
```

#### 

### **秃然好心寒**

其实看到这，我就有点心寒了。。。。

<img src="https://img-blog.csdnimg.cn/img_convert/b83af50ac00fd784f3a77e9407b0f32f.png" alt="b83af50ac00fd784f3a77e9407b0f32f.png">

### **拉黑这帮重色轻友的人！**

进入自己心灵想进去的地方，拉黑他们！<img src="https://img-blog.csdnimg.cn/img_convert/735624cad6d49160e0bf013bda5d7445.png" alt="735624cad6d49160e0bf013bda5d7445.png">发现只有一个 post 请求，那应该就只能是这个了。<img src="https://img-blog.csdnimg.cn/img_convert/657159b1d749b77c8a933781b1f03620.png" alt="657159b1d749b77c8a933781b1f03620.png">看了眼所需要的参数，自己的号，拉黑的号，自己的空间，加上一个无用参数和刚才所获得加密参数。<img src="https://img-blog.csdnimg.cn/img_convert/5dd445114714977414b08b9b8e524e70.png" alt="5dd445114714977414b08b9b8e524e70.png">越想越气，写代码！

```
def pull_black(): # 拉黑，必须拉黑！
    global cookie
    cookie = search_cookie()
    with open('access_denied.txt', 'r') as f:
        access_denied = f.readlines()
    for fake_friend in access_denied:
        fake_friend = fake_friend.split('\n')[0]
        yurl = "https://user.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/right/cgi_black_action_new?"
        g_tk = get_g_tk()
        url_data = {'g_tk': g_tk}
        data = {
            'uin': cookie['ptui_loginuin'],
            'action': '1',
            'act_uin': fake_friend,
            'fupdate': '1',
            'qzreferrer': 'https://user.qzone.qq.com/1223411083'
        }
        url = yurl + urllib.parse.urlencode(url_data)
        res=requests.post(url, headers = headers, data=data, cookies = cookie)
        print(str(fake_friend)+"已被您拉黑")
    print("都拉黑了！解气！！")
```

### 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/qq_45414559/article/details/107733745

### ****

### **全部代码**

#### 

如果对本文内容感兴趣，可以添加小二微信：**ityard**，备注**QQ**

免费获取本文源码****

<img src="https://img-blog.csdnimg.cn/img_convert/86d78a8e4d210d2c3365e58b5688baa6.png" alt="86d78a8e4d210d2c3365e58b5688baa6.png">

******长按识别上方********<img src="https://img-blog.csdnimg.cn/img_convert/2fa4745126814efb0db82d4c283b7993.png" alt="2fa4745126814efb0db82d4c283b7993.png">二维码添加小二微信**
