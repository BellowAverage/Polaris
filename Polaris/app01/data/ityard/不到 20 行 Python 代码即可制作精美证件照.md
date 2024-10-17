
--- 
title:  不到 20 行 Python 代码即可制作精美证件照 
tags: []
categories: [] 

---
无论是我们上学时还之后的工作中，基本都需要用到电子证件照片，这类照片基本都对照片尺寸、背景色有要求，本文我们来看一下如何只用不到 20 行 Python 代码完成证件照片的制作。

## 简介

制作证件照我们主要有两个工作：修改照片背景和修改照片尺寸，修改背景我们需要用到第三方库 `removebg`，修改照片尺寸需要用到 `PIL` 库，这两个库的安装使用 `pip install removebg` 和 `pip install Pillow` 即可。

使用 `removebg` 时，我们还需要一个 API 密钥，获取方式为：首先，我们打开链接地址 `https://accounts.kaleido.ai/users/sign_up` 注册一个账户，打开后如下图所示： <img src="https://img-blog.csdnimg.cn/20200424063156397.PNG" alt=""> 我们填写邮箱和密码再勾选同意协议后提交，之后该网站会给我们刚刚填写的邮箱发送一条验证信息，我们进到自己的邮箱点击验证链接完成验证之后即完成了账号的注册工作。

账号注册好之后，我们接着打开 `https://www.remove.bg/zh/profile#api-key` 地址登录自己的账号，即可进入到下图位置： <img src="https://img-blog.csdnimg.cn/20200424063246368.PNG" alt=""> 我们点击上图中的显示按钮，就可以拿到秘钥了。

## 代码实现

代码实现也比较简单，还是我们之前说的思路：使用 `removebg` 库修改照片背景色，使用 `PIL` 库修改照片尺寸，具体实现如下所示：

```
from PIL import Image
from removebg import RemoveBg

# 修改照片背景色
def change_bgcolor(file_in, file_out, api_key, color):
    rmbg = RemoveBg(api_key, 'error.log')
    rmbg.remove_background_from_img_file(file_in)
    no_bg_image = Image.open(file_in)
    x, y = no_bg_image.size
    new_image = Image.new('RGBA', no_bg_image.size, color=color)
    new_image.paste(no_bg_image, (0, 0, x, y), no_bg_image)
    new_image.save(file_out)

# 修改照片尺寸
def change_size(file_in, file_out, width, height):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

```

我们可以看出整个实现过程只用了不到 20 行代码。

## 效果展示

最后我们来看一下实现效果：

<img src="https://img-blog.csdnimg.cn/20200424063354335.jpg" alt=""> <img src="https://img-blog.csdnimg.cn/20200424063413372.jpg" alt=""> 源码可在公号后台回复 **200424** 获取。

<img src="https://img-blog.csdnimg.cn/20200424063728608.png#pic_center" alt=""> <img src="https://img-blog.csdnimg.cn/20200424064031758.PNG?#pic_center" alt="" width="500">
