
--- 
title:  Python实现智能停车场车牌识别计费系统 
tags: []
categories: [] 

---
前段时间练习过的一个小项目，今天再看看，记录一下~

### 项目结构

**说明：**
- datefile文件夹：保存车辆信息表的xlsx文件- file文件夹：保存图片文件夹。ic_launcher.jpg是窗体的右上角图标文件；income.png是实现收入统计的柱状图（下一篇文章实现）；key.txt是使用百度的图片识别AI接口申请的key；test.jpg保存的是摄像头抓取的图片- venv文件夹：项目所需要的各种模块，即项目运行环境- btn.py文件：按钮模块- main.py文件：程序主文件- ocrutil.py文件：车牌识别模块- timeutil.py文件：时间处理模块
### 主要代码

```
# 车位文字
def text1(screen):
    # 剩余车位
    k = Total - carn
    if k &lt; 10:
        # 剩余车位
        sk = '0' + str(k)
    else:
        sk = str(k)
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 20)
    # 重新开始按钮
    textstart = xtfont.render('共有车位：' + str(Total) + '  剩余车位：' + sk, True, WHITE)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 30
    # 绘制内容
    screen.blit(textstart, text_rect)


# 停车场信息表头
def text2(screen):
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 15)
    # 重新开始按钮
    textstart = xtfont.render('  车号       时间    ', True, WHITE)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 820
    text_rect.centery = 70
    # 绘制内容
    screen.blit(textstart, text_rect)
    pass


# 停车场车辆信息
def text3(screen):
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 12)
    # 获取文档表信息
    cars = pi_table[['carnumber', 'date', 'state']].values
    # 页面就绘制10辆车信息
    if len(cars) &gt; 10:
        cars = pd.read_excel(path + '停车场车辆表.xlsx', skiprows=len(cars) - 10, sheet_name='data').values
    # 动态绘制y点变量
    n = 0
    # 循环文档信息
    for car in cars:
        n += 1
        # 车辆车号 车辆进入时间
        textstart = xtfont.render(str(car[0]) + '   ' + str(car[1]), True, WHITE)
        # 获取文字图像位置
        text_rect = textstart.get_rect()
        # 设置文字图像中心点
        text_rect.centerx = 820
        text_rect.centery = 70 + 20 * n
        # 绘制内容
        screen.blit(textstart, text_rect)
    pass
```

### 实现效果

### 源码素材

完整代码已经打包整理好了，有需要的小伙伴可以**关注下方视频号：来去如风**私信**人员**免费获取~

友情提示：点击上方视频后点**圆形头像**，再点**关注**后**私信**关键字**人员**，未关注的可能不会发哦<img src="https://img-blog.csdnimg.cn/img_convert/e03151ca09be987ef89332c8fd136e5e.png" alt="e03151ca09be987ef89332c8fd136e5e.png">，已经关注的直接私信关键字即可<img src="https://img-blog.csdnimg.cn/img_convert/b06a42b4bfbbf04b02048f0c3ef1c361.png" alt="b06a42b4bfbbf04b02048f0c3ef1c361.png">

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/919920db03b2649a47bcea2596b754f7.gif" alt="919920db03b2649a47bcea2596b754f7.gif">
