
--- 
title:  用 Python 将 QQ 好友头像生成祝福语 
tags: []
categories: [] 

---
本文我们来看一下如何使用 Python 将 QQ 好友头像拼成“五一快乐”四个字。我们可以将整个实现过程分为两步：爬取 QQ 好友头像、利用好友头像生成文字。

### 爬取头像

爬取 QQ 好友头像我们需要借助于 QQ 邮箱，首先我们从浏览器上登录 QQ 邮箱，之后按 `F12` 键打开开发者工具并用鼠标选中 `Network` 选项，如下图所示： <img src="https://img-blog.csdnimg.cn/20200502105958290.png" alt=""> 再接着我们按 `F5` 键刷新一下网页，然后在 `Filter` 中输入 `laddr_lastlist`，如下图所示： <img src="https://img-blog.csdnimg.cn/20200502110014626.png" alt=""> 我们再点 `Name` 下的链接，点击之后右侧会出现一个窗口，我们用鼠标选中 `Response` 项，如下图所示： <img src="https://img-blog.csdnimg.cn/20200502110032510.png" alt=""> 我们最后将 `Response` 下面出现的内容复制到 txt 文件。

获取了爬取需要用到的东西后我们就可以开始实现爬取了，我们使用 `requests` 库将头像图片爬取来下存到本地，代码实现如下所示：

```
# 获取头像
def get_head():
    file = codecs.open('qqfriends.txt', 'rb', 'utf-8')
    s = file.read()
    pattern = re.compile(r'\d+@qq.com')
    # 正则表达式匹配所有的 qq 号
    all_mail = pattern.findall(s)
    # 用于存储需要访问的链接
    all_link = []
    url = 'http://qlogo.store.qq.com/qzone/'
    for mail in all_mail:
        qq = mail.replace('@qq.com', '')
        l = url + qq + '/' + qq + '/100'
        all_link.append(l)
    # 初始化下载图片数量
    i = 0
    # 获取朋友头像数量
    friends_count = len(all_link)
    print('共{}个头像'.format(friends_count))
    # 遍历链接，下载头像
    for link in all_link:
        i += 1
        saveurl = 'head/' + str(i) + '.png'
        print('第 %d 个' % i, end=' ')
        sava2img(link, saveurl)
    return True

# 存储图片函数，picurl 是图片的 URL，saveurl 是本地存储位置
def sava2img(picurl, saveurl):
    try:
        start = time.time()
        response = requests.get(picurl, stream=True)
        # 下载图片到本地
        with open(saveurl, 'wb') as file:
            file.write(response.content)
            print('下载完成...', end=' ')
        end = time.time()
        time_ = end - start
        print('用时: %.2f秒' % (time_))
        return True
    except:
        print('出错了...')

```

### 生成文字

现在 QQ 头像图片已经有了，我们再看一下如何用这些图片生成文字，这里需要用到一下第三方库 `PIL`，安装使用 `pip install Pillow`，我们需要先将 “五一快乐” 四个字转化为汉字库的点阵数据再使用，现在看一下具体实现：

```
# 将字转化为汉字库的点阵数据
def char2bit(textStr):
    KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]
    target = []
    global count
    count = 0
    for x in range(len(textStr)):
        text = textStr[x]
        rect_list = [] * 16
        for i in range(16):
            rect_list.append([] * 16)
        gb2312 = text.encode('gb2312')
        hex_str = binascii.b2a_hex(gb2312)
        result = str(hex_str, encoding='utf-8')
        area = eval('0x' + result[:2]) - 0xA0
        index = eval('0x' + result[2:]) - 0xA0
        offset = (94 * (area-1) + (index-1)) * 32
        font_rect = None
        with open("HZK16", "rb") as f:
            f.seek(offset)
            font_rect = f.read(32)
        for k in range(len(font_rect) // 2):
            row_list = rect_list[k]
            for j in range(2):
                for i in range(8):
                    asc = font_rect[k * 2 + j]
                    flag = asc &amp; KEYS[i]
                    row_list.append(flag)
        output = []
        for row in rect_list:
            for i in row:
                if i:
                    output.append('1')
                    count+=1
                else:
                    output.append('0')
        target.append(''.join(output))
    return target

# 生成图片文字
def head2char(workspace,folder,self,outlist):
    # 将工作路径转移至头像文件夹
    os.chdir(folder)
    # 获取文件夹内头像列表
    imgList = os.listdir(folder)
    # 获取头像图片个数
    numImages = len(imgList)
    # 设置头像裁剪后尺寸
    eachSize = 100
    # 变量 n 用于循环遍历头像图片
    n=0
    # 变量 count 用于为最终生成的单字图片编号
    count = 0
    # 初始化颜色列表，用于背景着色
    colorlist = ['#FFFACD','#F0FFFF','#BFEFFF','#b7facd','#ffe7cc','#fbccff','#d1ffb8','#febec0','#E0EEE0']
    # index 用来改变不同字的背景颜色
    index = 0
    # 每个 item 对应不同字的点阵信息
    for item in outlist:
        # 将工作路径转到头像所在文件夹
        os.chdir(folder)
        # 新建一个带有背景色的画布，16 * 16点阵，每个点处填充 2 * 2 张头像图片，故长为 16 * 2 * 100
        canvas = Image.new('RGB', (3200, 3200), colorlist[index])  # 新建一块画布
        # index 变换，用于变换背景颜色
        index = (index+1)%9
        count += 1
        # 每个 16 * 16 点阵中的点，用四张 100 * 100 的头像来填充
        for i in range(16*16):
            # 点阵信息为 1，即代表此处要显示头像来组字
            if item[i] == "1":
                # 循环读取连续的四张头像图片
                x1 = n % len(imgList)
                x2 = (n+1) % len(imgList)
                x3 = (n+2) % len(imgList)
                x4 = (n+3) % len(imgList)
                # 以下四组 try,将读取到的四张头像填充到画板上对应的一个点位置
                # 点阵处左上角图片 1/4
                try:
                    # 打开图片
                    img = Image.open(imgList[x1])
                except IOError:
                    print("有1张图片读取失败，已使用备用图像替代")
                    img = Image.open(self)
                finally:
                    # 缩小图片
                    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)
                    # 拼接图片
                    canvas.paste(img, ((i % 16) * 2 * eachSize, (i // 16) * 2 * eachSize))
                # 点阵处右上角图片 2/4
                try:
                    img = Image.open(imgList[x2])
                except IOError:
                    print("有1张图片读取失败，已使用备用图像替代")
                    img = Image.open(self)
                finally:
                    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)
                    canvas.paste(img, (((i % 16) * 2 + 1) * eachSize, (i // 16) * 2 * eachSize))
                # 点阵处左下角图片 3/4
                try:
                    img = Image.open(imgList[x3])
                except IOError:
                    print("有1张图片读取失败，已使用备用图像替代")
                    img = Image.open(self)
                finally:
                    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)
                    canvas.paste(img, ((i % 16) * 2 * eachSize, ((i // 16) * 2 + 1 ) * eachSize))
                # 点阵处右下角图片 4/4
                try:
                    img = Image.open(imgList[x4])
                except IOError:
                    print("有1张图片读取失败，已使用备用图像替代")
                    img = Image.open(self)
                finally:
                    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)
                    canvas.paste(img, (((i % 16) * 2 + 1) * eachSize, ((i // 16) * 2 + 1) * eachSize))
                #调整 n 以读取后续图片
                n= (n+4) % len(imgList)
        os.chdir(workspace)
        # 创建文件夹用于存储输出结果
        if not os.path.exists('output'):
            os.mkdir('output')
        os.chdir('output')
        # 存储将拼接后的图片，quality 为图片质量，1 - 100，100 最高
        canvas.save('result%d.jpg'% count, quality=100)

```

看一下实现效果： <img src="https://img-blog.csdnimg.cn/20200502110054922.jpg" alt=""> 源码可在公号 **Python小二** 后台回复 200501 获取。
