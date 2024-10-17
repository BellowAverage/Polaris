
--- 
title:  《Python小游戏汇总》- 1. 表白神器 
tags: []
categories: [] 

---
https://blog.csdn.net/meenr/article/details/119185683

## 《Python小游戏汇总》系列文章开篇：1. 表白神器



#### 目录
- - <ul><li>- - - - - - <ul><li>- 


### 1 Python系列游戏案例

<img src="https://img-blog.csdnimg.cn/21fdfaab2f4c4f91b02738d718b77c9e.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="220" height="350">

### 2 开发环境

Windows10、Python3.7、PyCharm

### 3 效果

<img src="https://img-blog.csdnimg.cn/9da443ef41c64bbdb5cded0fca4e544c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="350" height="200">

**功能演示视频**  https://www.bilibili.com/video/BV1Mf4y1V7xx/



https://mp.weixin.qq.com/s/RxVASEEEIznOuRjvMNm1LA

### 4 代码

```
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, fontpath, fontsize, fontcolor, bgcolors, edgecolor, edgesize=1, is_want_to_be_selected=True, screensize=None, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(fontpath, fontsize)
        self.fontcolor = fontcolor
        self.bgcolors = bgcolors
        self.edgecolor = edgecolor
        self.edgesize = edgesize
        self.is_want_tobe_selected = is_want_to_be_selected
        self.screensize = screensize

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.is_want_tobe_selected:
                while self.rect.collidepoint(mouse_pos):
                    self.rect.left, self.rect.top = random.randint(0, self.screensize[
                        0] - self.rect.width), random.randint(0, self.screensize[1] - self.rect.height)
            pygame.draw.rect(screen, self.bgcolors[0], self.rect, 0)
            pygame.draw.rect(screen, self.edgecolor, self.rect, self.edgesize)
        else:
            pygame.draw.rect(screen, self.bgcolors[1], self.rect, 0)
            pygame.draw.rect(screen, self.edgecolor, self.rect, self.edgesize)
        text_render = self.font.render(self.text, True, self.fontcolor)
        fontsize = self.font.size(self.text)
        screen.blit(text_render, (
        self.rect.x + (self.rect.width - fontsize[0]) / 2, self.rect.y + (self.rect.height - fontsize[1]) / 2))



def showText(screen, text, position, fontpath, fontsize, fontcolor, is_bold=False):
    font = pygame.font.Font(fontpath, fontsize)
    font.set_bold(is_bold)
    text_render = font.render(text, True, fontcolor)
    screen.blit(text_render, position)


```

### 5 桌面应用

可直接发送到无Python环境的电脑上运行，实现“表白最后一步”。 下载地址：在2贰进制公众号回复“表白神器可执行文件”

无需安装，解压即可运行。

### 干货获取

由于篇幅限制，不在陈列全部代码。感兴趣的读者如需要全部代码和**.exe** 文件，可通过以下渠道获得。

#### 5.1

**关注下方微信公众号，分别回复：“ 表白神器代码 ”和“表白神器可执行文件”**，可获得代码和应用程序。

<img src="https://img-blog.csdnimg.cn/5878521fb89947ce8ce2aed0dcdd2aec.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_30,color_222FFF,t_70#pic_center" alt="请添加图片描述" width="411" height="150">

#### 5.2

**加入下方QQ群，群文件自行下载或者联系管理员获取** <img src="https://img-blog.csdnimg.cn/bfb5e8b62e064795876ce49e898b3e7c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="请添加图片描述" width="200" height="200">

**2贰进制–Echo 2020年5月** 如果您已阅读至此，请点赞＋评论＋收藏，要是关注那更是对我极大地支持了，您的支持便是我前进的动力！ 如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来给予我更大支持：

此致 感谢您的阅读、点赞、评论、收藏与打赏。
