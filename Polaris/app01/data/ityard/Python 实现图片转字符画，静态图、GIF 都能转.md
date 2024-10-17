
--- 
title:  Python 实现图片转字符画，静态图、GIF 都能转 
tags: []
categories: [] 

---
字符画是一种由字母、标点或其他字符组成的图画，它产生于互联网时代，在聊天软件中使用较多，本文我们看一下如何将自己喜欢的图片转成字符画。

### 静态图片

首先，我们来演示将静态图片转为字符画，功能实现主要用到的 Python 库为 OpenCV，安装使用 `pip install opencv-python` 命令即可。

功能实现的基本思路为：利用聚类将像素信息聚为 3 或 5 类，颜色最深的一类用数字密集度表示，阴影的一类用横杠（-）表示，明亮部分用空白表示。

主要代码实现如下：

```
def img2strimg(frame, K=5):   
    if type(frame) != np.ndarray:
        frame = np.array(frame)
    height, width, *_ = frame.shape  
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_array = np.float32(frame_gray.reshape(-1))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    # 得到 labels(类别)、centroids(矩心)
    compactness, labels, centroids = cv2.kmeans(frame_array, K, None, criteria, 10, flags)
    centroids = np.uint8(centroids)
    # labels 的数个矩心以随机顺序排列，所以需要简单处理矩心
    centroids = centroids.flatten()
    centroids_sorted = sorted(centroids)
    # 获得不同 centroids 的明暗程度，0 为最暗
    centroids_index = np.array([centroids_sorted.index(value) for value in centroids])
    bright = [abs((3 * i - 2 * K) / (3 * K)) for i in range(1, 1 + K)]
    bright_bound = bright.index(np.min(bright))
    shadow = [abs((3 * i - K) / (3 * K)) for i in range(1, 1 + K)]
    shadow_bound = shadow.index(np.min(shadow))
    labels = labels.flatten()
    # 将 labels 转变为实际的明暗程度列表
    labels = centroids_index[labels]
    # 解析列表
    labels_picked = [labels[rows * width:(rows + 1) * width:2] for rows in range(0, height, 2)]
    canvas = np.zeros((3 * height, 3 * width, 3), np.uint8)
	# 创建长宽为原图三倍的白色画布
    canvas.fill(255)
    y = 8
    for rows in labels_picked:
        x = 0
        for cols in rows:
            if cols &lt;= shadow_bound:
                cv2.putText(canvas, str(random.randint(2, 9)),
                            (x, y), cv2.FONT_HERSHEY_PLAIN, 0.45, 1)
            elif cols &lt;= bright_bound:
                cv2.putText(canvas, "-", (x, y),
                            cv2.FONT_HERSHEY_PLAIN, 0.4, 0, 1)
            x += 6
        y += 6
    return canvas

```

原图如下： <img src="https://img-blog.csdnimg.cn/img_convert/776d5a002c0f1c3482b9621e8062c7ae.png" alt="" width="300"> 效果图如下： <img src="https://img-blog.csdnimg.cn/img_convert/22dd9ec1391b3cc248683ad701d311f0.png" alt="" width="300">

### GIF 动图

接下来我们演示将 GIF 转为字符画，功能实现主要用到的 Python 库为 imageio、Pillow，安装使用 `pip install imageio/Pillow` 命令即可。

功能实现的基本思路如下：
- 将 gif 图片的每一帧拆分为静态图片- 将所有静态图片变为字符画- 将所有字符画重新合成 gif
主要代码实现如下：

```
# 拆分 gif 将每一帧处理成字符画
def gif2pic(file, ascii_chars, isgray, font, scale):
    '''
    file: gif 文件
    ascii_chars: 灰度值对应的字符串
    isgray: 是否黑白
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
            # 将每一帧处理为字符画
            img2ascii(name, ascii_chars, isgray, font, scale)
            # 继续处理下一帧
            im.seek(current+1)
    except:
        os.chdir(path)

# 将不同的灰度值映射为 ASCII 字符
def get_char(ascii_chars, r, g, b):
    length = len(ascii_chars)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_chars[int(gray/(256/length))]


# 将图片处理成字符画
def img2ascii(img, ascii_chars, isgray, font, scale):
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
    img_txt = Image.new('RGB', (raw_width, raw_height), (255, 255, 255))
    # 创建 ImageDraw 对象以写入 ASCII
    draw = ImageDraw.Draw(img_txt)
    for j in range(len(txts)):
        for i in range(len(txts[0])):
            if isgray:
                draw.text((i * block_x, j * block_y), txts[j][i], (119,136,153))
            else:
                draw.text((i * block_x, j * block_y), txts[j][i], colors[j][i])
    img_txt.save(img)

# 读取 tmp 目录下文件合成 gif
def pic2gif(dir_name, out_name, duration):
    path = os.getcwd()
    os.chdir(dir_name)
    dirs = os.listdir()
    images = []
    num = 0
    for d in dirs:
        images.append(imageio.imread(d))
        num += 1
    os.chdir(path)
    imageio.mimsave(out_name + '_ascii.gif',images,duration = duration)

```

原图如下： <img src="https://img-blog.csdnimg.cn/img_convert/3d6c54893d5ad97b7e8b9cb7d0c8e4a6.gif" alt=""> 黑白效果图如下： <img src="https://img-blog.csdnimg.cn/img_convert/d4a6aee96983380e9e9e0431fb389b40.gif" alt=""> 彩色效果图如下： <img src="https://img-blog.csdnimg.cn/img_convert/e26b2cd99beb29f0229444351f18e984.gif" alt="">

### 总结

本文我们利用 Python 演示了将静态图和 GIF 转为字符画的方法，大家如果有兴趣的话，可以将自己喜欢的图转一下，如果对转换效果不满意，还可以修改代码，改成自己满意的效果。

源码在公众号 **Python小二** 后台回复 **字符画** 获取。

>  
 本文非首发于个人号 

