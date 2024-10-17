
--- 
title:  用 Python 写个简单但强大的人脸识别系统 
tags: []
categories: [] 

---
`face_recognition`是一个强大、简单、易上手的人脸识别开源项目，并且配备了完整的开发文档和应用案例，特别是兼容树莓派系统。 `face_recognition`一经开源发布就得到的广泛的热捧，使用简单，功能强大成为其非常显著的标签。`face_recognition`对于公司或者是一些工程实践性的应用场景来说是非常好用好上手的利器，不需要你有太多的理论基础就可以比较轻松地去完成一个识别项目，所以今天我们专门来讲解一下。

首先，`face_recognition`项目开源地址在这里：

https://github.com/ageitgey/face_recognition

<img src="https://img-blog.csdnimg.cn/img_convert/72ceda6e7ed1108af7f8591cf92f2ae2.png">

网上有比较完整的API说明以及实例应用，我这里就不多去说明了。首先，使用face_recognition需要安装，可以通过 pip 完成。如果安装遇到报错可参考：

https://yishuihancheng.blog.csdn.net/article/details/102679177

安装完成后就可以使用了，在编码前可以通过简单的测试来检验是否安装成功，如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/5c1d8357ab9f0b31b0d6ae0639365978.png">

成功安装后，就可以进入使用了。

**1、定位图像中的人脸**

```
def demoFunc():
    '''
    在一张包含人脸的图片中圈出来人脸
    '''
    image = face_recognition.load_image_file("test.jpg")
    face_locations = face_recognition.face_locations(image)
    for one in face_locations:   
        y0, x1, y1, x0=one
        cv2.rectangle(image, pt1=(x0, y0), pt2=(x1, y1), color=(0, 0, 255), thickness=3)
    cv2.imshow('aaa', image)
    if cv2.waitKey(0) &amp; 0xFF == ord('q'):
        cv2.destroyAllWindows()

```

从网上随便找了一张图片，如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/0cfa8f549920bbeb2e5866e227569028.png">

定位结果如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/49819e6b4328207a652c768a66c96cbb.png">

感觉还是很强大的，当然了，在我实践的过程中也发现了部分图像识别检测人脸失败的问题，这个毕竟不是一个百分之百的问题，face_recognition更像是一个基础框架，帮助我们更加高效地去构建自己的人脸识别的相关应用。

**2、切割图像中的每个人脸保存本地**

```
def demoFunc():
    '''
    图片中人脸截图保存
    '''
    img = cv2.imread("test.jpg")
    image = face_recognition.load_image_file("test.jpg")
    face_locations = face_recognition.face_locations(image)  #(top, right, bottom, left)
    for i in range(len(face_locations)):
        y0, x1, y1, x0 = face_locations[i]
        cropped = img.crop((x0,y0,x1,y1))  # (left, upper, right, lower)  左上角  右下角
        cropped.save(str(i)+"_.jpg")
        cropped.show()

```

使用的原始图像同上，结果如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/285d1f60f76fd8de5be0e38985befdd6.png">

五张人脸都检测成功，并且保存成功，这里主要是要注意一些face_locations这个函数的返回结果，返回的子列表中每个子列表包含4个元素，分别是单张人脸图像的左上顶点和右下顶点坐标，主要需要注意的是这四个参数的顺序，我给出来的结果中(x0,y0)表示左上顶点的坐标，(x1,y1)表示右下顶点的坐标。

**3、将图像中的每个人脸编码成一个128维的向量**

```
def demoFunc():
    '''
    将图片中的每张人脸编码成一个128维长度的向量
    '''
    image = face_recognition.load_image_file("cl.jpg")
    face_locations = face_recognition.face_locations(image)  #(top, right, bottom, left) 
    face_encodings = face_recognition.face_encodings(image, face_locations)  #将单个人脸数据转化为一个128维的向量
    for one in face_encodings:
        print('one: ',one)

```

进行到这里就不得不去讲一下`face_recognition`的一些应用原理，下面是我的一些总结，如有不当欢迎指教。

face_recognition模块人脸识别应用实现的原理：

(１) 给定想要识别的人脸的图片并对其进行编码（每个人只需要一张），并将这些不同的人脸编码构建成一个列表。编码其实就是将人脸图片映射成一个１２８维的特征向量。

(２) 计算图像向量之间的相似度根据阈值或者是容错度来决定是否是同一个人

(３) 输出识别结果标签。

毫不夸张地说，`face_recognition`整个的核心就在于这一块的向量化处理中，输入的每一张人脸图像都会被转化为一个128维的特征向量进行存储，128维特征向量的生成也是一个算法在里面的感兴趣的话可以去查一下深入了解一下，我这里就不展开了，之后的人脸识别就转化为了两个人脸图像之间向量相似度的问题了。

这里使用一张成龙大哥的图像来进行测试，原始图像如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/8630adb87f3f6ee687d0601ed020b93c.png">

向量化结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/f393d4300b7f5fd7bdaa7c06afd1ebbb.png">

如果自己想要构建自己的个性化应用的话一般会选择在这里进行改造，首先就是需要保存这里的特征向量。

**4、输入两张人脸图像，判断是否是同一个人**

```
def demoFunc(one_pic='c1.jpg',two_pic='c2.jpg'):
    '''
    给定两张图片，判断是否是同一个人
    '''
    chenglong = face_recognition.load_image_file(one_pic)
    unknown_image = face_recognition.load_image_file(two_pic)
    biden_encoding = face_recognition.face_encodings(chenglong)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    print('results: ',results)
    return results[0]

```

这里其实跟上面第三部分的有点相似，这部分是建立在第三部分基础上的只不过是自带了compare_faces这个相似度计算接口，这里其实可以自己去实现替换的。

同样，使用了两张成龙大哥的图像来进行测试，原始图像如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/c623090917259aab7c0f9018575bf6d0.png">

<img src="https://img-blog.csdnimg.cn/img_convert/0d7e1d72e685e527491ab8df71f9447d.png">

测试结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/54db078cc92fd4e8d53e9362e51c9349.png">

**5、脸部关键点识别和标注**

```
def demoFunc(pic_path='cl.jpg'):
    '''
    脸部关键点识别、标注
    '''
    image = face_recognition.load_image_file(pic_path)
    face_landmarks_list = face_recognition.face_landmarks(image)
    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)
    for face_landmarks in face_landmarks_list:
        for facial_feature in face_landmarks.keys():
            print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
        for facial_feature in face_landmarks.keys():
            d.line(face_landmarks[facial_feature], width=5)
    pil_image.show()

```

脸部的关键点包括：鼻子、嘴巴、眼睛、眉毛等，这里还是用的上面成龙大哥的图片，下面的结果输出：

<img src="https://img-blog.csdnimg.cn/img_convert/f21915899ce3760270185131b5b4decb.png">

<img src="https://img-blog.csdnimg.cn/img_convert/66b6dc624cb0c159cf19afa815a75abe.png">

**6、化妆**

这部分是建立在第五部分基础上的，得到的面部的特征以后就可以进行自动化妆了，下面是具体的实现：

```
def demoFunc(pic_path="haiwang.jpg"):
    '''
    化妆
    '''
    image = face_recognition.load_image_file(pic_path)
    face_landmarks_list = face_recognition.face_landmarks(image)
    pil_image = Image.fromarray(image)
    for face_landmarks in face_landmarks_list:
        demo = ImageDraw.Draw(pil_image, 'RGBA')
        demo.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
        demo.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
        demo.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=2)
        demo.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=2)
        demo.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
        demo.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
        demo.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=2)
        demo.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=2)
        demo.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
        demo.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))
        demo.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=2)
        demo.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=2)
        pil_image.show()

```

这里使用海王的一张图片来进行测试，原始图像如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/eca489901253092dae3e2e83641fe212.png">

处理后结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/fd7a40e0f239ffece599219a7efed2d9.png">

还可以是这样的：

<img src="https://img-blog.csdnimg.cn/img_convert/5a6ad411d6dd5e0a10d73d385ee0b3df.png">

**7、基于face_recognition构建自己的简单人脸识别应用**

上面介绍了很多face_recognition的应用，这里才是最重要的内容我觉得是这样的，基于已有的功能来实现我们自己的个性化应用，我这里只是简单的抛砖引玉，给出来自己的最最简单的实现：

```
def faceRecognitionDemo(picDir='data/', test_pic='test.png'):
    '''
    基于 face_recognition 构建人脸识别模块
    '''
    pic_list=os.listdir(picDir)
    for one_pic in pic_list:
        one_pic_path=picDir+one_pic
        one_res=demo6(one_pic=one_pic_path,two_pic=test_pic)
        one_name=one_pic.split('.')[0].strip()
        if one_res:
            print('This Person is: ', one_name)
            break
        else:
            print('This Person is not: ', one_name)

```

data文件夹数据截图如下：

<img src="https://img-blog.csdnimg.cn/img_convert/deecb84f9527289b32c27354fbe6b53c.png">

test.png内容如下：

<img src="https://img-blog.csdnimg.cn/img_convert/84cc02a7b467c547735d1d80d67c36e1.png">

结果输出如下：

<img src="https://img-blog.csdnimg.cn/img_convert/661074d4a77ad0219e10489793f148a4.png">

当然了，实时计算肯定当前的计算方式不能满足的，这个只是一个最简单的应用而已，只想在这里抛砖引玉，这里是通过调用了face_recognition接口的形式来完成相似判定的工作的，还有一种非常常见的办法就是在得到人脸图像的128维特征向量之后就可以将人脸识别问题转化为基于机器学习模型的一个简单分类问题了，比如：SVM、RF、GBDT等都可以非常出色地完成上面的任务。

好了本文就到这里结束了，欢迎交流！

版权声明：本文为CSDN博主「Together_CZ」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。原文链接：

https://yishuihancheng.blog.csdn.net/article/details/102831117

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/3e66b1a787efb826d2b9647b83be23dc.gif">

微信扫码关注，了解更多内容
