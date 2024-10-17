
--- 
title:  python 实现与企业微信群机器人信息交互 
tags: []
categories: [] 

---
### 1 企业微信群添加机器人

#### 1.1 在群聊里穿件机器人

右键群聊，如下图： <img src="https://img-blog.csdnimg.cn/01308b95548d42f5899e751be339058a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Ziz5YWJX-S9oOWlvQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 1.2 查看群聊机器人信息

创建完机器人，在群聊右侧群成员下面，就能看见我们创建的群机器人。右键机器人查看其信息，我们要把Webhook地址复制下来，这个很重要，我们稍后回用到，如下图： <img src="https://img-blog.csdnimg.cn/c023a53b3ead40069ec18439929db0c4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Ziz5YWJX-S9oOWlvQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 我们假设，我的群聊机器人Webhook地址为：https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=slkjflsjlfjsljs-sjsjl9028508-isjfrwruiou-sjkfjkjsl92849

### 2 用python 编写发送消息函数

首先，我们用python3写一个发送post请求的方法：

```
def send_msg(msg):
	"""
	msg:要往群里发送的消息
	"""
    headers = {<!-- -->"Content-Type": "application/json"} # 请求头
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=slkjflsjlfjsljs-sjsjl9028508-isjfrwruiou-sjkfjkjsl92849"  # Webhook地址，即机器人地址
    json = {<!-- -->
        "msgtype": "markdown",
        "markdown": {<!-- -->"content": msg}
    }
    r1 = requests.post(url=url, json=json, headers=headers)
    print(r1.text)
    json_text = {<!-- -->
        "msgtype": "text",
        "text": {<!-- -->
            "content": "",
            "mentioned_list": ["xiaoming",  "@all"]
            "mentioned_mobile_list":["19999999999","@all"]
        }
    }
    r2 = requests.post(url=url, json=json_text, headers=headers)
    print(r2.text)

```

该函数实现了两种格式数据的发送：文本格式，markdown格式

### 3 消息格式类型

消息类型格式有：文本格式，markdown格式，图片类型，文件类型

#### 3.1 文本类型

json格式：

```
{<!-- -->
    "msgtype": "text",
    "text": {<!-- -->
        "content": "早会还有十分钟进行，大家准备一下",
        "mentioned_list":["张三","@all"],
        "mentioned_mobile_list":["19999999999","@all"]
    }
}

```

|参数|是否必填|说明
|------
|msgtype|是|消息类型，此时固定为text
|content|是|文本内容，最长不超过2048个字节，必须是utf8编码
|mentioned_list|否|userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
|mentioned_mobile_list|否|手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人

#### 3.2 markdown类型

json格式：

```
{<!-- -->
    "msgtype": "markdown",
    "markdown": {<!-- -->
        "content": "早会出席情况：&lt;font color="yellow"&gt;90人&lt;/font&gt;，请大家注意。\n
         &gt;研发部:&lt;font color="black"&gt;120人&lt;/font&gt;
         &gt;产品部:&lt;font color="black&gt;24人&lt;/font&gt;
         &gt;测试组:&lt;font color="black"&gt;15人&lt;/font&gt;"
    }
}

```



#### 3.3 图片格式

json格式：

```
{<!-- -->
    "msgtype": "image",
    "image": {<!-- -->
        "base64": "DATA",
        "md5": "MD5"
    }
}

```

|参数|是否必填|说明
|------
|msgtype|是|消息类型，此时固定为image
|base64|是|图片内容的base64编码
|md5|是|图片内容（base64编码前）的md5值

>  
 注：图片（base64编码前）最大不能超过2M，支持JPG,PNG格式 <img src="https://img-blog.csdnimg.cn/4705a361046742e79eb26ec089afbf2d.png#pic_center" alt="在这里插入图片描述"> 


#### 文件格式

json格式：

```
{<!-- -->
    "msgtype": "file",
    "file": {<!-- -->
         "media_id": "3a8asd892asd8asd"
    }
}

```

|参数|是否必填|说明
|------
|msgtype|是|消息类型，此时固定为file
|media_id|是|文件id，通过下文的文件上传接口获取

<img src="https://img-blog.csdnimg.cn/img_convert/2e59375b10259fb82aefe59063a4ab89.png" alt="img">

>  
 注：上传的文件限制：要求文件大小在5B~20M之间 



