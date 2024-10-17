
--- 
title:  用 Python 将神龙大侠搞怪 GIF 转为字符动画 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20191229150432261.png" alt=""> **谁是神龙大侠？**

动画电影《功夫熊猫》相信很多人都看过，主角是一只武功高强又经常搞怪名字叫阿宝的熊猫，在选拔神龙大侠的比武中，阿宝成为神龙大侠，所以现在的神龙大侠就是熊猫阿宝。

### 运行环境
- 系统：Windows- Python 版本：3.6- 模块：os、imageio、PIL
第三方模块的安装使用 `pip install ...` 即可。

### 基本思路
- 将 gif 图片的每一帧拆分为静态图片- 将所有静态图片变为字符画- 将所有字符画重新合成 gif
### 主要实现

**1. 将 gif 每一帧拆分为静态图片**

```
def gif2pic(file, ascii_chars, font, scale):
    '''
    file: gif 文件
    ascii_chars: 灰度值对应的字符串
    font: ImageFont 对象
    scale: 缩放比例
    '''
    im = Image.open(file)
    path = os.getcwd()
    if(not os.path.exists(path+"/tmp")):
        os.mkdir(path+"/tmp")
    os.chdir(path+"/tmp")
    # 清空 tmp 目录下内容
    for f in os.listdir(path+"/tmp"):
        os.remove(f)
    try:
        while 1:
            current = im.tell()
            name = file.split('.')[0]+'_tmp_'+str(current)+'.png'
            # 保存每一帧图片
            im.save(name)
            # 继续处理下一帧
            im.seek(current+1)
    except:
        os.chdir(path)

```

**2. 将静态图片变成字符画**

```
def img2ascii(img, ascii_chars, font, scale):
    scale = scale
    # 将图片转换为 RGB 模式
    im = Image.open(img).convert('RGB')
    # 设定处理后的字符画大小
    raw_width = int(im.width * scale)
    raw_height = int(im.height * scale)
    # 获取设定的字体的尺寸
    font_x, font_y = font.getsize(' ')
    # 确定单元的大小
    block_x = int(font_x * scale)
    block_y = int(font_y * scale)
    # 确定长宽各有几个单元
    w = int(raw_width/block_x)
    h = int(raw_height/block_y)
    # 将每个单元缩小为一个像素
    im = im.resize((w, h), Image.NEAREST)
    # txts 和 colors 分别存储对应块的 ASCII 字符和 RGB 值
    txts = []
    colors = []
    for i in range(h):
        line = ''
        lineColor = []
        for j in range(w):
            pixel = im.getpixel((j, i))
            lineColor.append((pixel[0], pixel[1], pixel[2]))
            line += get_char(ascii_chars, pixel[0], pixel[1], pixel[2])
        txts.append(line)
        colors.append(lineColor)
    # 创建新画布
    img_txt = Image.new("RGB", (raw_width, raw_height), (255, 255, 255))
    # 创建 ImageDraw 对象以写入 ASCII
    draw = ImageDraw.Draw(img_txt)
    for j in range(len(txts)):
        for i in range(len(txts[0])):
            draw.text((i*block_x, j*block_y), txts[j][i], colors[j][i])
        img_txt.save(img)

def get_char(ascii_chars, r, g, b):
    length = len(ascii_chars)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_chars[int(gray/(256/length))]

```

**3. 将所有字符画合成 gif**

```
def pic2gif(dir_name, duration):
    path = os.getcwd()
    os.chdir(dir_name)
    dirs = os.listdir()
    images = []
    num = 0
    for d in dirs:
        images.append(imageio.imread(d))
        num += 1
    os.chdir(path)
    imageio.mimsave(d.split('_')[0]+'_char.gif',images,duration = duration)

```

### 效果展示

我们找两张神龙大侠搞怪 gif 图片，如下所示：

<img src="https://img-blog.csdnimg.cn/20191229160013281.gif" alt="原图1">

<img src="https://img-blog.csdnimg.cn/20191229160039627.gif" alt="原图2">

看一下处理后的效果图：

<img src="https://img-blog.csdnimg.cn/20191229160220759.gif" alt="">

<img src="https://img-blog.csdnimg.cn/20191229160245843.gif" alt="">

**完整代码**请关注文末公众号，后台回复 **GIF** 免费获取。

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">
