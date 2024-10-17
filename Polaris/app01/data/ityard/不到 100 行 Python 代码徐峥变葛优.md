
--- 
title:  不到 100 行 Python 代码徐峥变葛优 
tags: []
categories: [] 

---
给照片换脸大家应该都见过，本文我们来介绍一下如何通过 Python 实现换脸。

### 1. 功能实现

实现换脸功能，我们大致可以分为两种：一种是所有功能都通过自己编码来实现，另一种是借助于第三方 API 来实现，第一种方式可能需要我们进行大量的编码才能实现，而第二种方式我们只需进行少量的编码即可实现。

本文我们使用更简单的第二种方式来实现，我们用到的 API 接口提供方是 Face++，首先我们需要到该网站注册一个自己的账号，注册地址为：`https://console.faceplusplus.com.cn/register`，打开后如下所示： <img src="https://img-blog.csdnimg.cn/20200428220811670.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们可以通过手机号和邮箱两种方式来注册，注册好账号之后，我们再到登录地址 `https://console.faceplusplus.com.cn/login` 进行登录，登录之后，我们会发现网站已经为我们创建好了应用，如下图所示： <img src="https://img-blog.csdnimg.cn/20200428220840447.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们需要用到的是上图中的 `API Key` 和 `API Secret` 的值，下面来看一下具体实现代码：

```
import requests, simplejson, json, base64

# 获取人脸关键点
def find_face(imgpath):
    print("正在查找……")
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    data = {<!-- -->"api_key": "自己的 api_key",
            "api_secret": "自己的 api_secret",
            "image_url": imgpath, "return_landmark":1}
    files = {<!-- -->"image_file": open(imgpath, "rb")}
    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    this_json = simplejson.dumps(req_dict)

    this_json2 = simplejson.loads(this_json)
    print(this_json2)
    faces = this_json2['faces']
    list0 = faces[0]
    rectangle = list0['face_rectangle']
    # print(rectangle)
    return rectangle


# 换脸，图片的大小应不超过 2M，number 表示换脸的相似度
def merge_face(image_url1, image_url2, image_url, number):
    ff1 = find_face(image_url1)
    ff2 = find_face(image_url2)

    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))
    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])
    print(rectangle2)
    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
    f1 = open(image_url1, 'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_url2, 'rb')
    f2_64 = base64.b64encode(f2.read())
    f2.close()

    data = {<!-- -->"api_key": "自己的 api_key",
            "api_secret": "自己的 api_secret",
            "template_base64": f1_64, "template_rectangle": rectangle1,
            "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}

    response = requests.post(url_add, data=data)
    req_con1 = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con1)
    result = req_dict['result']
    imgdata = base64.b64decode(result)
    file = open(image_url, 'wb')
    file.write(imgdata)
    file.close()

```

### 2. 效果展示

下面我们通过具体图片来看一下实现效果。

首先，我们使用两位男明星的图片进行效果展示，以徐峥和葛优为例，原图如下所示： <img src="https://img-blog.csdnimg.cn/20200428221045122.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> <img src="https://img-blog.csdnimg.cn/20200428221058307.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 换脸后的效果图如下所示： <img src="https://img-blog.csdnimg.cn/20200428221125653.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 接着，我们再使用两位女明星的图片进行效果展示，以贾玲和关晓彤为例，原图如下所示： <img src="https://img-blog.csdnimg.cn/20200428221143375.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> <img src="https://img-blog.csdnimg.cn/20200428221206270.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 换脸后的效果图如下所示： <img src="https://img-blog.csdnimg.cn/2020042822122688.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 是不是感觉有点意思，有兴趣的同学可以自己动手试试。
