
--- 
title:  如何用 Python 生成炫酷二维码及解析 
tags: []
categories: [] 

---
如今二维码可以说遍及了我们生活的各个角落，基本上我们的衣食住行都会见到二维码的身影。Python 用于生成及解析二维码的库为：qrcode、myqr 和 zxing，安装通过 `pip install qrcode/myqr/zxing` 即可。

### 生成

生成二维码的 Python 库为：qrcode、myqr，接下来我们通过示例来看一下。

##### 1. 方式一

qrcode 库可以生成一些相对简单的二维码，优势是速度快、占用空间小，便于在线生成，以扫描二维码跳转某地址为例来看一下。

```
import qrcode
​
# 二维码内容（链接地址或文字）
data = 'https://www.baidu.com/'
# 生成二维码
img = qrcode.make(data=data)
# 显示二维码
img.show()
# 保存二维码
# img.save('qr.jpg')

```

效果如下： <img src="https://img-blog.csdnimg.cn/img_convert/3c03300d8ef4717a147aea71bb1bf094.png#pic_center" alt="在这里插入图片描述" width="300">

我们可以看出上面的是最基本的二维码，下面我们对它进行一下简单的美化。

```
import qrcode
​
'''
version：二维码的格子矩阵大小，可以是 1 到 40，1 最小为 21*21，40 是 177*177
error_correction：二维码错误容许率，默认 ERROR_CORRECT_M，容许小于 15% 的错误率
box_size：二维码每个小格子包含的像素数量
border：二维码到图片边框的小格子数，默认值为 4
'''
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=3,
)
# 二维码内容
data = 'https://www.baidu.com/'
qr.add_data(data=data)
# 启用二维码颜色设置
qr.make(fit=True)
img = qr.make_image(fill_color='blue', back_color='white')
# 显示二维码
img.show()

```

效果如下： <img src="https://img-blog.csdnimg.cn/img_convert/d01e979e6244f53dd1c6db94c4f67032.png#pic_center" alt="在这里插入图片描述" width="300">

##### 2. 方式二

如果我们想要生成更加炫酷的二维码可以使用 myqr 库，但它同样有缺点，就是不适合在线使用。

**普通样式**

我们先生成一个基本二维码。

```
from MyQR import myqr
​
'''
words：内容
version：容错率
save_name：保存的名字
'''
myqr.run(words='https://www.baidu.com/',
         version=1,
        save_name='myqr.png')

```

效果如下： <img src="https://img-blog.csdnimg.cn/img_convert/0b03fd5de86fc5216ab17f04b93d7e7d.png#pic_center" alt="在这里插入图片描述" width="300"> **带图样式**

我们接着生成一个带图二维码。

```
from MyQR import myqr
​
'''
picture：生成二维码用到的图片
colorized：False 为黑白，True 为彩色
'''
myqr.run(words='https://www.baidu.com/',
         version=1,
         picture='bg.jpg',
         colorized=True,
         save_name='pmyqr.png')

```

效果如下： <img src="https://img-blog.csdnimg.cn/img_convert/ee95bfd92a0406a6812de867fee9461d.png#pic_center" alt="在这里插入图片描述" width="300"> **动态样式**

最后我们生成一个动态二维码。

```
from MyQR import myqr
​
myqr.run(words='https://www.baidu.com/',
         version=1,
         picture='my.gif',
         colorized=True,
         save_name='myqr.gif')

```

效果如下： <img src="https://img-blog.csdnimg.cn/img_convert/763d1600220715d7f475d439a67da071.gif#pic_center" alt="在这里插入图片描述" width="300">

### 解析

zxing 库是用来解析二维码的，我们通过示例来看一下。

```
import zxing
​
reader = zxing.BarCodeReader()
barcode = reader.decode('myqr.gif')
print(barcode.parsed)

```

如果我们需要对现有二维码进行美化，只需如下两步即可。
- 对现有二维码进行解析获取解析内容- 利用解析的内容生成新的二维码
比如以如下二维码为例，我们对其解析并生成新的二维码。 <img src="https://img-blog.csdnimg.cn/img_convert/f848d7a9057588b499d776849874e0b1.png#pic_center" alt="在这里插入图片描述" width="300">

```
import zxing
from MyQR import myqr
​
reader = zxing.BarCodeReader()
barcode = reader.decode('gzh.jpg')
myqr.run(words=str(barcode.parsed),
         version=1,
         picture='my.gif',
         colorized=True,
	 save_name='gmyqr.gif')

```

效果如下： <img src="https://img-blog.csdnimg.cn/20210320080150329.gif#pic_center" alt="在这里插入图片描述" width="300">

这样我们会发现扫描原二维码与新生成的二维码具体相同的效果。

在公众号 **Python小二** 后台回复 **qrcode** 获取源码
