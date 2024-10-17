
--- 
title:  App爬虫之强大的Airtest的操作总结 
tags: []
categories: [] 

---
## App爬虫之强大的Airtest的操作总结

App爬虫之强大的Airtest的操作总结

```
# Python使用该框架需要安装的依赖库
pip install airtest
pip install poco
pip install pocoui


```

```
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

"""
自动配置运行环境， 如果没有连接设备， 默认连接安卓设备
参数：
    basedir - 设置当前脚本所在路径，也可以直接传_file_变量进来
    devices - 一个内容为connect_device url 字符串的列表
    logdir - 可设置脚本运行是log保存路径，默认值为None则不保存log，如果设置为True则自动保存在&lt;basedir&gt;/log目录中
    project_root - 用于设置PROJECT_ROOT变量，方便using接口调用
"""
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/10.2.145.168:5555?cap_method=MINICAP&amp;&amp;ori_method=MINICAPORI&amp;&amp;touch_method=MAXTOUCH"])

# 连接本机默认端口连的设备号为123和456的两台手机
# auto_setup(__file__,devices=["Android://127.0.0.1:5037/123","Androd://127.0.0.1:5037/456"])

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# script content
print("start...")

# 唤醒并解锁目标设备
wake()

# 启动APP
start_app("com.bonade.xxp")

# home键操作
# home()

# 若是设置的APP开着，则关闭APP
# stop_app("com.bonade.xxp")

# 安装待测软件apk，路径信息。
# install("path/to/your/apk")

# 卸载安装
# uninstall("package_name_of_your_apk")

```

### 一、 定位方式

**child：获取当前节点下的子节点，** 如果是多个获取多个，用for循环获取，不使用循环提取的默认提取第一个节点

```
def child(self, name=None, **attrs): 

```

示例：

```
menuList1=poco("com.aa.bb:ide_bottom_navigator").child("android.widget.LinearLayout")
for i in range(0,len(menuList1)):  #同列表方式一致，节点序号从0开始
    print ("第 %d 次用child获取menuList底部全部菜单=====%s"%(i,menuList1[i]))

```

**children：获取子节点** 获取字节点，如果是多个获取多个，用for循环获取，不使用循环提取的默认提取第一个节点

```
def children(self): 

```

示例：

```
menuList2=poco("com.tencent.nbagametime:ide_bottom_navigator").child("android.widget.LinearLayout").children()
for i in range(0,len(menuList2)):
    print ("第 %d 次用children获取menuList底部菜单名=====%s"%(i,menuList2[i]))

```

**offspring：孙节点** 获取当前节点下的孙节点，如果是多个获取多个，用for循环获取，不使用循环提取的默认提取第一个节点

```
def offspring(self, name=None, **attrs): 

```

offspring查找孙节点的顺序：树结构自底往上，同一层从中间右边左边的顺序 **sibling：兄弟节点** 获取当前节点的兄弟节点

```
def sibling(self, name=None, **attrs):  

```

**parent：父节点** 获取当前节点的父节点，如果获取的当前节点是多个（用children获取的），则获取列表第一个节点的父节点

```
def parent(self): 

```

注意：此方法在Android上可用，在Ios上不可用，会报错：AttributeError: ‘UIObjectProxy’ object has no attribute ‘parent’ attr(‘type’)：提取属性值 示例：

```
poco('ssion').attr('type') #提取指定元素属性为type的值

```

**get_text()：提取文本内容** 示例：

```
poco('ssion').get_text() #提取指定元素的文本内容

```

**exists()：判断元素是否存在** 示例：

```
poco('ssion').exists() #判断指定元素是否在当前屏幕上存在，返回True

```

**元素文本正则匹配：**

```
poco(textMatches='^测试.*$', type='Button', enable=True)

```

### 二、 元素操作

**click()：点击操作**

```
def click(self, focus=None, sleep_interval=None): 

```

****focus****：值为：(x,y)或“anchor”或“center”。(x,y)意思是距元素左上角的偏移点，值必须在0~1范围内。 ****center****是指点击ui元素边界框的中心。 anchor”是指监视器中UI包围盒的小红点。 ****sleep_interval****：点击操作后等待的秒数。默认值为无，这里默认睡眠间隔。这个值可以通过POCO初始化进行配置。 示例：

```
poco('home_bottom_navigator').click() #无参数默认点中间位置无间隔时间
poco('home_bottom_navigator').click([0.5, 0.5]) #相当于点中间位置
poco('home_bottom_navigator').click([0.5, 0.5],3) #传参，点击元素中间红点后等待3秒

```

**rclick()：右键点击**

```
def rclick(self, focus=None, sleep_interval=None): 

```

****focus****：同click方法 ****sleep_interval****：同click方法

**double_click()：双击操作**

```
def double_click(self, focus=None, sleep_interval=None): 

```

****focus****：同click方法 ****sleep_interval****：同click方法

**long_click()：长按操作**

```
def long_click(self, duration=2.0): 

```

****duration****：整个动作持续时间

**swipe()：滑动操作**

```
def swipe(self, direction, focus=None, duration=0.5): 

```

****direction****：坐标，可以是(x,y)格式坐标，也可以是’up’, 'down’, 'left’, 'right’ (up=[0, -0.1]，down=[0, 0.1]，left=[-0.1, 0]，right=[0, 0.1]) ****focus****：同click方法 duration：间隔时间,float类型，默认0.5秒 示例：

```
node= poco('home_bottom_navigator').child('point_img')
node.swipe('up') #向上滑动
node.swipe([0.2, -0.2])  # 以45度角向上和向右滑动sqrt(0.08)单位距离

```

说明：swipe操作以 锚点anchor为起点，如果想改变起点可用 focus 方法，然后朝给定方向滑动，距离就是向量的长度。

**drag_to：拖拽**

```
def drag_to(self, target, duration=2.0): 

```

****target****：拖动后的目标元素 ****duration****：间隔时间,float类型，默认2秒 备注：

****区别：**** ****darg 是从一个UI拖到另一个UI， 而 swipe 是将一个UI朝某个方向拖动。**** 示例： .

```
poco(text='比赛').drag_to(poco(text='开始')) #把比赛元素拖动到开始元素上

```

**scroll：卷动效果**

就是从一个方向一点一点的显示出来 一种特效，就是下拉页面啊，或者其他移动的时候，眼睛会比较舒适，其实区别不大。

```
def scroll(self, direction='vertical', percent=0.6, duration=2.0): 

```

****direction****：滚动方向。”垂直“或水平”，默认垂直 percent：在指定元素上按高或宽的滚动百分比 ****duration****：间隔时间,float类型，默认2秒

**pinch：捏合操作** 双指捏合是一个比较常见的手势操作了，我们经常打开相册时用这个手势去放大、缩小图片，以便查看。

```
def pinch(self, direction='in', percent=0.6, duration=2.0, dead_zone=0.1): 

```

****direction****：滚动方向。”垂直“或水平”，默认垂直 ****percent****：在指定元素上按高或宽的滚动百分比 ****duration****：间隔时间,float类型，默认2秒 dead_zone：

**focus：局部定位**

```
def focus(self, f): 

```

****f****：同click()方法 示例：

```
poco('比赛').focus('center').click()  #定位到元素中间点，进行点击
poco('比赛').focus([0.5,1]).click()  #定位到元素最下边缘的中间点，进行点击

```

将 focus 和 drag_to 结合使用还能产生卷动(scroll)的效果，下面例子展示了如何将一个列表向上卷动半页。 第9点中的scroll实现方式就是这样的 示例：

```
poco(“元素”).focus([0.5, 0.8]).drag_to(poco(“元素”).focus([0.5, 0.2])) #从指定节点的中下方拖拽到中上方，比如手机端的从下往上滑动  

```

**start_gesture()：移动设备手势分解方法,** 返回用于生成序列化手势操作的对象。 示例：

```
ui1=poco("ui1")
ui2=poco("ui2")
ui1.start_gesture().hold(1).to(ui2).hold(1).up() #在ui1元素上按下，等待1秒，拖拽到ui2元素上再等1秒，最后抬起释放

```

**get_position()：获取元素位置坐标，** 返回(x, y)坐标

```
def get_position(self, focus=None) 

```

****focus****：同click()方法，默认空 wait()：等待，直到超过timeout的时间，超时后返回元素对象 def wait(self, timeout=3) 说明： 在给定时间内等待一个UI出现并返回这个元素，如果已经存在了那就返回这个元素。如果超时还没出现，同样也会返回，但是调用这个UI的操作时会报错。

```
经验：结合exists()方法可以判断元素是否出现，比如： poco(“元素”).wait(4).exists() #如果结果是True则元素存在，如果False则元素不存在
wait_for_appearance():等待出现，

```

****若超时返回****

```
PocoTargetTimeout def wait_for_appearance(self, timeout=120) 

```

备注： wait_for_appearance()同wait()的区别：前者超时没找到元素直接返回异常PocoTargetTimeout，后者超时后还返回元素当调用时会报错。 **wait_for_disappearance()：等待未出现，** 若超时返回

```
PocoTargetTimeout def wait_for_disappearance(self, timeout=120):  

```

****attr()****：获取属性 def attr(self, name)： ****name****：属性名 示例：

```
poco("节点").attr('text')

```

说明：通过给定的属性名检索ui元素的属性。如果属性不存在，则返回none。 属性名可以是以下类型之一，也可以是由SDK实现的任何其他自定义类型： -
<li>
```
- visible: whether or not it is visible to user
- text: string value of the UI element
- type: the type name of UI element from remote runtime
- pos: the position of the UI element
- size: the percentage size [width, height] in range of 0~1 according to the screen
- name: the name of UI element
- ...: other sdk implemented attributes

```

****setattr()：设置属性值，**** 更改ui元素的属性值。

```
def setattr(self, name, val) 

```

****name****：属性名 ****val****：属性值 说明：并非所有属性都可以转换为文本。如果改变不可变的属性或不存在的属性，将引发InvalidOperationException异常 **exists()：判断是否存在，** 返回True/False

```
def exists(self)  

```

**get_text()：获取UI元素的文本属性，** 如果没有此类属性，则返回None

```
def get_text(self)  

```

**set_text()：设置文本值**

```
def set_text(self, text) 

```

****text****：文本值

**get_name()：获取元素名，** 即属性是name的值， attr('name’)

```
def get_name(self)  

```

**get_size()：获取元素size，** 即属性中的size(attr('size’))， 值：size : [1, 0.76328125]

```
def get_size(self):  

```

**get_bounds()：获取UI元素边界框的参数**

```
def get_bounds(self) 

```

说明：返回列表形式，如 (top, right, bottom, left)形式的，与标准坐标系中屏幕边缘相关的坐标。

**nodes：在远程运行时中访问UI元素的只读属性。** def nodes(self) 调用方式：

```
poco("节点").nodes

```

**invalidate():重新获取元素标识**

```
def invalidate(self) 

```

说明：清除标志以指示重新查询或从层次结构中重新选择UI元素 等待时间：强制等待\全局隐式等待\显示等待时间 **全局隐式等待：**

```
ST.FIND_TIMEOUT=60 #设置隐式等待60秒

```

**隐式等待** 是一种智能等待，他可以规定在查找元素时，在指定时间内不断查找元素
- 如果找到则代码继续执行，直到超时没找到元素才会报错，也就是说如果在第三秒找到元素，则剩下的7秒不会被等待 **显式等待：wait()**-  1、显示等待也是一种智能等待，在指定超时时间范围内只要满足操作的条件就会继续执行后续代码 -  如果不满足条件则会一直等到超时 **强制等待：sleep()** -  隐式等待和显示等待的区别： -  1、隐式等待是全局的，可以随时更改的，显示等待是针对单一元素或者一组元素的 -  2、隐式等待只能针对元素查找方法，显示等待可以自定义等待条件 