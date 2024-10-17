
--- 
title:  当 Python 遇到微信 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200505214354108.png" alt=""> 自从微信禁止网页版登陆之后，itchat 库实现的功能也就都不能用了，那现在 Python 还能操作微信吗？答案是还可以。

目前有一个项目 `WechatPCAPI` 可以对微信进行操作，简单来说它是直接操作 PC 版微信客户端的，当然它有一定不足之处就是：PC 版微信客户端和 Python 都需要使用指定版本的，本文我们使用的 Python 版本为 `3.7.6` ，微信客户端使用版本为 `2.6.8.52` ，WechatPCAPI 的 GitHub 地址为：`` `https://github.com/Mocha-L/WechatPCAPI`。

### 获取好友列表

`WechatPCAPI` 提供了方法 `get_friends()`，该方法返回信息包括：好友、群和公众号的列表信息，信息内容主要包括：微信号、昵称和自己设置的备注。

我们使用获取的昵称做个简单的词云展示，代码实现如下所示：

```
logging.basicConfig(level=logging.INFO)

def on_message(message):
 pass

def get_friends():
 # 初始化微信实例
 wx_inst = WechatPCAPI(on_message=on_message, log=logging)
 # 启动微信
 wx_inst.start_wechat(block=True)
 # 等待登陆成功，此时需要人为扫码登录微信
 while not wx_inst.get_myself():
  time.sleep(5)
 print('登陆成功')
 nicknames = []
 # 排除的词
 remove = ['还是', '不会', '一些', '所以', '果然',
     '起来', '东西', '为什么', '真的', '这么',
     '但是', '怎么', '还是', '时候', '一个',
     '什么', '自己', '一切', '样子', '一样',
     '没有', '不是', '一种', '这个', '为了'
   ]
 for key, value in wx_inst.get_friends().items():
  if key in ['fmessage', 'floatbottle', 'filehelper'] or 'chatroom' in key:
   continue
  nicknames.append(value['wx_nickname'])
 words = []
 for text in nicknames:
  if not text:
   continue
  for t in jieba.cut(text):
   if t in remove:
    continue
   words.append(t)
 global word_cloud
 # 用逗号隔开词语
 word_cloud = '，'.join(words)

def nk_cloud():
    # 打开词云背景图
    cloud_mask = np.array(Image.open('bg.png'))
    # 定义词云的一些属性
    wc = WordCloud(
        # 背景图分割颜色为白色
        background_color='white',
        # 背景图样
        mask=cloud_mask,
        # 显示最大词数
        max_words=300,
        # 显示中文
        font_path='./fonts/simkai.ttf',
        # 最大尺寸
        max_font_size=70
    )
    global word_cloud
    # 词云函数
    x = wc.generate(word_cloud)
    # 生成词云图片
    image = x.to_image()
    # 展示词云图片
    image.show()
    # 保存词云图片
    wc.to_file('nk.png')

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200505214101837.png" alt="">

### 消息防撤回

我们在使用微信和好友聊天时，对方有时会有撤回消息的情况，正常情况下，我们是不知道好友撤回的消息是什么的，通过 `WechatPCAPI` 就可以实现消息防撤回的功能。

我们知道通常撤回的消息是点击撤回操作前一步发送的内容，当然也可能撤回的是前两步、三步 … 的消息，这里我们只对撤回前一步的消息做处理，基本思路是：我们将撤回前一步发送的消息存一下，当对方点击撤回操作时，我们再将前一步的消息再次返回给自己。

下面看一下实现代码：

```
logging.basicConfig(level=logging.INFO)
queue_recved_event = Queue()

def on_message(msg):
    queue_recved_event.put(msg)

def login():
    pre_msg = ''
    # 初始化微信实例
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    # 启动微信
    wx_inst.start_wechat(block=True)
    # 等待登陆成功，此时需要人为扫码登录微信
    while not wx_inst.get_myself():
        time.sleep(5)
    print('登陆成功')
    while True:
        msg = queue_recved_event.get()
        data = msg.get('data')
        sendinfo = data.get('sendinfo')
        data_type = str(data.get('data_type'))
        msgcontent = str(data.get('msgcontent'))
        is_recv = data.get('is_recv')
        print(msg)
        if data_type == '1' and 'revokemsg' not in msgcontent:
            pre_msg = msgcontent
        if sendinfo is not None and 'revokemsg' in msgcontent:
            user = str(sendinfo.get('wx_id_search'))
            recall = '撤回的消息：' + pre_msg
            wx_inst.send_text(to_user=user, msg=recall)

```

看一下操作效果： <img src="https://img-blog.csdnimg.cn/20200505214200303.jpg" alt="">
