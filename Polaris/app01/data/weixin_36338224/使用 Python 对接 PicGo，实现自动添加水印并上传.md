
--- 
title:  使用 Python 对接 PicGo，实现自动添加水印并上传 
tags: []
categories: [] 

---
### 1. 天下苦搬运党久矣

对于我这样经常需要写点文章的技术自媒体来说，很经常早上我才在公众号首发了原创文章，中午就有人同步到了知乎、今日头条等外部平台，并且拿到了该篇文章在这些平台的首发。 <img src="https://img-blog.csdnimg.cn/20210308091032477.png" alt="">

平台的首发很重要，以微信的公众号平台来说，一篇文章能否在公众号标原创，就是通过检测是否在公众号平台上首发，如果公众号的文章库里没有搜索到与你文章相似度较高的文章，那么你就可以标原创了。

为了解决了首发的问题，我付费使用了 OpenWrite 这个平台，每个月 20 块钱的费用，一键就可以分发各大平台，非常的省心~

**首发固然重要，但有时候也没那么重要。**

因为有专门的培训机构（这里就不点名，避免给他们反向营销）就是拿你的文章去给自己的帐号堆干货，吸引关注，他们才不在乎原创不原创，只要文章能发布就行了。

这种人在知乎这种没有原创检测机制的平台，可以活得很好。

之前有一无良培训机构在知乎上生产了10几个号，批量搬运我以及一些朋友的原创文章。那时候，我每天都可以举报好多。

<img src="https://img-blog.csdnimg.cn/20210308091032936.png" alt="">

渐渐地，我累了，自己写了几百篇的文章，如果一篇一篇去检查，那我这一天基本啥事都做不了，违权成本实在太高了。

考虑到我的文章都有非常多的图片，为了让这些人在白嫖我文章的同时，也能给我带来点收益（当然人家是不可能付费的，但至少能给我的公众号打打广告也是非常奈斯的）。

于是我就想啊，是不是可以自己写个工具，给自己的每张配图上都加上自己的水印，看他们还盗不盗。。

### 2. 目前的图床管理工具

在开始讲如何利用 Python 来实现我的需求之前 ，我有必要介绍下我的图床管理工具。

我在写文章的时候，主要用到三款工具：
- `Typora` ：Markdown 文案的编辑- `Snipaste`：非常好用的截图工具- `PicGo`：非常人性的图床管理工具
<img src="https://img-blog.csdnimg.cn/20210308091033141.png" alt="">

其中今天的要参与的主角是 `PicGo`

<img src="https://img-blog.csdnimg.cn/20210308091033396.png" alt="">

它对当下主流的图床平台都提供了很好的支持

<img src="https://img-blog.csdnimg.cn/20210308091033667.png" alt="">

当我使用了 `Snipaste` 截图后，再按住快捷键（⌘ ⇧ P），就可以立即将你的图床上传至指定图床，并且将上传后的链接以 markdown 的图片格式复制到剪切板中，你可以直接粘贴使用。

### 3. 方案的设想

由于这一整工具，我已经使用了三年，各种操作都非常的熟悉，对他们我已经产生了极度的依赖，因此现在我想要实现自动加水印的功能，也一定是建立在这套工具的基础上完成的。

Snipaste 和 PicGo 本身都不支持自定义水印，也不提供第三方插件的开发入口。

Snipaste 和 PicGo 之所以能够在一起工作，是因为有了剪切板这个桥梁，因此想要实现自己的需求，只能从剪切板上寻找突破口。

多余的废话就不多说了，我直接说下我的方案：
1. 在 Snipaste 将图像放入剪切板后1. 由我敲入自定义的热键去触发 Python 脚本去从剪切板中读取图像1. 然后使用 PIL 去给该图像加水印，重新放入剪切板中1. 接着利用 Python 脚本去自动化触发 PicGo 的快捷键1. PicGo 被激活后，就能将带有水印的图片上传到图床
为了让你对这个方案，有一个直观的理解，我特地画了一张流程图，其中虚线就是我得自己实现的功能。

<img src="https://img-blog.csdnimg.cn/2021030809103455.png" alt="">

### 4. 代码完整解析

#### 4.1 定义热键并监听键盘

在 Python 中有一个 pynput 库，利用它可以来监听系统的键盘。

在它的官方文档中，很快找到了一个可以自定义热键组合的方案。

```
from pynput import keyboard

def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('&lt;ctrl&gt;+&lt;alt&gt;+h'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()

```

但是很遗憾的是，这个功能目前来看是有 BUG 的，我在 Mac 上亲测是没有效的，而在 github 的  中也有人在 2020 年8月反应过问题， 没想到到现在还没有解决

<img src="https://img-blog.csdnimg.cn/20210308091034366.png" alt="">

虽然它本身提供的组合键监听模式无法使用，但普通的监听模式还是可以使用的，只要有这个做为基础，那我自己造轮子也不难实现组合热键的功能。

第一步：先定义好你的热键：⌘ ⌃ ⌥ P

```
upload_pic_set = {<!-- -->
    keyboard.Key.ctrl.value.vk,
    keyboard.Key.cmd.value.vk,
    keyboard.Key.alt.value.vk,
    keyboard.KeyCode(35).vk
}

```

第二步：监听所有的键盘动作

```
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

```

只要有一个键处于 press 的状态，就往列表中存放这个键

```
key_list = []

def on_press(key):
    if isinstance(key, keyboard.KeyCode):
        key_list.append(key.vk)
    elif isinstance(key, keyboard.Key):
        key_list.append(key.value.vk)

    if set(key_list) == upload_pic_set:
        image = get_image_from_clipboard()
        new_image = make_watermark(image)
        put_image_to_clip(new_image)
        upload_image_via_picgo()
        notify_to_mac("成功添加水印并上传到图床")

```

但是一旦有键释放了，就要清空这个列表

```
def on_release(key):
    key_list.clear()

```

每一次按下键都会检查，key_list 是否等于 定义好的快捷键，如果刚好是相等，就可以开始图片的处理逻辑了。

```
if set(key_list) == upload_pic_set:
  pass

```

#### 4.2 从内存中读取图像

PIL 有一个 ImageGrab 模块，在这个模块中有一个 grabclipboard 函数，它实现了从剪切板中读取图像的功能，不过读取的 rgb 格式，由于我们后面加水印时，必须使用 rgba 格式才可以，因此再用 convert 转一下。

```
  from PIL import  ImageGrab
  
  img_rgb = ImageGrab.grabclipboard()
  image = img_rgb.convert("RGBA")

```

###4.3 添加水印生成新图像

以下是添加水印的代码，其实可能要注意的一点就是如果你的文字里包含中文，那么选择字体时一定要是中文字体，否则会出现方块字

```
def make_watermark(image):
    txt = Image.new('RGBA', image.size, (0, 0, 0, 0))
    fnt = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 20)
    draw = ImageDraw.Draw(txt)
    draw.text(((txt.size[0]-300)//2, txt.size[1]-40), "微信公众号: Python编程时光", font=fnt, fill=(240, 49, 48, 255))
    draw.text(((txt.size[0]-300)//2, txt.size[1]-70), "未经授权请勿转载", font=fnt, fill=(240, 49, 48,  255))
    out = Image.alpha_composite(image, txt)
    return out

```

#### 4.4 将新图像重新放入剪切板

内置的 io 模块支持在内存中读写 bytes，只要PIL 的 image 对象在 save 的时候保存保存在 BytesIO 对象中，然后通过 pasteboard 模块从 BytesIO 对象中载入数据，就可以实现往剪切板中放入图像的功能。

```
def put_image_to_clip(image):
    img_byte_arr = io.BytesIO() 
    pb = pasteboard.Pasteboard()

    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    pb.set_contents(img_byte_arr, pasteboard.PNG)

```

pasteboard 载入的图像只支持 PNG 格式，因此在保存时，一定要指定 PNG。

此外 pasteboard 还支持更多格式的数据，比如 PDF，音频数据，HTML、颜色数据等等

更多格式可查看：https://developer.apple.com/documentation/appkit/nspasteboardtypestring

#### 4.5 模拟触发 PicGo

正常情况下，我们是通过快捷键来触发 PicGo 去从剪切板中上传图像的，因此想要在程序中激活 PicGo，也只需要在 Python 脚本中模拟键盘动作即可。

具体的代码如下：

```
from pykeyboard import PyKeyboard

def upload_image_via_picgo():
    k = PyKeyboard()
    k.press_keys(['Command', 'shift', 'p'])

```

#### 4.6 通知 Mac 通知台

上面整个过程都是脚本在后台默默运行的，如果没有任何通知，作为用户，很难知道我们的图片是否处理好，是否上传成功，因此建议加一个通知的函数。

```
import os

def notify_to_mac(message):
    os.system("osascript -e 'display notification \"{}\"\'".format(message))

```

不过其实 PicGo 上传完图片后，本身就会通知，所以这个通知并不是必要的，看个人需求啦~

### 5. 其他设置工作

#### 5.1 设置程序权限

如果你在使用如上脚本时，发现有的键无法捕捉，那一定是系统没有给予权限，需要你手动开启。

<img src="https://img-blog.csdnimg.cn/20210308091034658.png" alt="">

#### 5.2 设置开机自启

在这里添加一个开机启动项，而这个 `init.sh` 是一个 Shell 脚本。

<img src="https://img-blog.csdnimg.cn/20210308091034960.png" alt="">

这个脚本的内容如下，注意最后那个 `&amp;` 一定不能省略。

<img src="https://img-blog.csdnimg.cn/20210308091035519.png" alt="">

### 6. 运行效果

代码全部解析完了，是不是很想看这个程序运行后，可以实现怎样的效果呢？

我录制了个 GIF 动态图，你可以瞧一瞧，真的太方便了。

<img src="https://img-blog.csdnimg.cn/20210308091054189.png" alt="">

### 7. 写在最后

对于有和我一样写博客习惯的朋友来说，我相信这篇文章的思路一定会有帮助，脚本我已经脚本上传好了(链接： https://wws.lanzous.com/iIDt1ml8mpi)，直接下载即可。

另外，即使你没有防搬运的需求，代码的实现依然值得学习，比如
- 如何监听键盘并定义程序的热键？- 如何从剪切板中读取图像？- 如何给图像添加水印？- 如何将图像再放入到剪切板？- 如何模拟键盘来激活程序？
在编码的时候，也遇到了不少的坑，有的第三方库并不适用于 Mac，有的有 BUG 至今也还没修复，有的甚至要阅读源码才能知道如何使用，经过多轮的调试和搜索，最终才完成这个脚本。

文章最后给大家介绍三个我自己写的在线文档：

**第一个文档**：

花了两个多月的时间，整理了 100 个 PyCharm 的使用技巧，为了让新手能够直接上手，我花了很多的时间录制了上百张 GIF 动图，有兴趣的前往在线文档阅读。

<img src="https://img-blog.csdnimg.cn/20210308091103270.png" alt="">

**第二个文档**：

系统收录各种 Python 冷门知识，Python Shell 的多样玩法，令人疯狂的 Python 炫技操作，Python 的超详细进阶知识解读，非常实用的 Python 开发技巧等。

<img src="https://img-blog.csdnimg.cn/20210308091104294.png" alt="">

**第三个文档**：

花了三个月时间写的一本 适合零基础入门 Python 的全中文教程，搭配大量的代码案例，让初学者对 代码的运作效果有一个直观感受，教程既有深度又有广度，每篇文章都会标内容的难度，是基础还是进阶的，可供读者进行选择，是一本难得的 Python 中文电子教程。

<img src="https://img-blog.csdnimg.cn/20210308091105420.png" alt="">
