
--- 
title:  Airtest工具根据App页面文字信息提取坐标进行截图保存在自定义文件夹 
tags: []
categories: [] 

---
### Airtest工具根据App页面文字信息提取坐标进行截图保存在自定义文件夹

### 一、项目背景
- 在一个项目中，选项被选中和未选中的节点元素的属性值无变化，通过AI识别率达不到百分百，想着通过计算图片的HSV值来判断选择能否被选中。（HSV比较友好，人更容易理解，为啥不要RGB是因为颜色模型太复杂，图片计算的RGB值不好判断颜色）回到正题上来，图片计算值时首先要扣出app选项的图片。看了网上好多资料，知识点比较零碎，我自己写了一个大体函数，有小伙伴遇到通用问题后就可以自己将函数粘贴的自己项目中，记住要带包。
### 二 、 解决思路及方法
- airtest工具根据app页面信息提取坐标进行截图保存在自定义文件夹，关键词app页面信息就是页面上的文字，根据文字提取文字的坐标和尺寸（计算出的坐标和尺寸是相当App整个页面长宽百分比，需要获取整个页面的长宽，通过百分比计算定位到左上和右下坐标），通过坐标和尺寸计算出左上和右下的坐标值，通过这两个坐标值进行截图并保存在自定义文件下。在python自动化测试中，批量截图的文件命名以时间戳进行命名。直接上代码。
<img src="https://img-blog.csdnimg.cn/c7fa37dc23a1476986793cf95de31c26.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a2bc83b609d74f07a5b27ca2acd0c925.png" alt="">

<img src="https://img-blog.csdnimg.cn/38273a891cc5461ea8abdd28019bead8.png" alt="在这里插入图片描述">

```
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.aircv import *

from airtest.core.api import *
from airtest.core.api import *
from airtest.aircv import *
from PIL import Image

from PIL import Image

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 刷脚本禁止写函数调用
screen = G.DEVICE.snapshot() 
# 局部截图

# 获取屏幕尺寸
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
android_poco= AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
screen_with, screen_height = android_poco.get_screen_size()
print("屏幕的宽度",screen_with,"屏幕的长度", screen_height)




def txt_zuo_biao_jie_tu(jiedian):
    
    print(len((jiedian)))
    for jiedian_i in range(len(jiedian)):
        print("开始计算")
        # 获取等级文本====成色
        jiedian_txt = jiedian[jiedian_i].child("android.view.View").get_text()
        print(jiedian_txt)
        # 获取元素节点

                
        jiedian_i_nod = jiedian[jiedian_i].child("android.view.View")
        # 获取节点坐标
        print(jiedian_i_nod.get_position())
        print(jiedian_i_nod.get_size())
        size_0 = jiedian_i_nod.get_size()
        position_0 = jiedian_i_nod.get_position()
        # 获取节点尺寸除以2

        for i_0 in range(len(size_0)):
            size_0[i_0] = size_0[i_0] / 2
        print(size_0)
#         # 计算坐标
        list_jia = []
        list_jian = []

        for index_0, item_0 in enumerate(position_0):
            list_jia.append(item_0 + size_0[index_0])

        print(list_jia)


        for index_0, item_0 in enumerate(position_0):
            list_jian.append(item_0 - size_0[index_0])

        print(list_jian)

        count = 1
        
        
        # 获取屏幕的大小
        
        
        list_jian_0 = []
        list_jia_0 = []
        # 获取坐标后开始截图
        list_jian_0.append(list_jian[0]*screen_with)
        list_jian_0.append(list_jian[1]*screen_height)

        list_jia_0.append(list_jia[0]*screen_with)
        list_jia_0.append(list_jia[1]*screen_height)
        
        
        

        c_0 = tuple(list_jian_0 + list_jia_0)
        print(c_0)
        # 截取图片区域
        screen = G.DEVICE.snapshot()

        # # 局部截图
        screen = aircv.crop_image(screen,c_0)

        # 保存局部截图到指定文件夹中
        pil_image = cv2_2_pil(screen)
        picture_name="{}_{}".format("截图颜色判断", time.strftime('%Y%m%d%H%M%S'))
        pil_image.save("G:/9月份pyqt项目/Airtest/代码/截图/untitled.air/{}.png".format(picture_name), quality=99, optimize=True)

    return("成功")

    
if __name__ == '__main__':
    jiedian = poco("android.widget.FrameLayout").offspring("com.wuba.zhuanzhuan:id/fah").child("android.webkit.WebView").offspring("app").child("android.view.View").child("android.view.View").child("android.view.View")[5].child("android.view.View").child("android.view.View")[1].child("android.view.View")[0].offspring("android.widget.ListView").child("android.view.View")

    txt_zuo_biao_jie_tu(jiedian)

```
- 思路值得参考，代码写的比较乱，大家可以作为参考，以后再遇到类似的问题，直接上代码。当然有不足之处，多多包涵，小伙伴就自己补充，争取项目在最短时间内，不烧脑细胞可以完活。