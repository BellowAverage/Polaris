
--- 
title:  我用Python摆摊算命 
tags: []
categories: [] 

---
  来源：blog.csdn.net/qq_35488769?type=blog

### 背景 

一直以来，中式占卜都是基于算命先生手工实现，程序繁琐（往往需要沐浴、计算天时、静心等等流程）。准备工作复杂（通常需要铜钱等道具），计算方法复杂，需要纯手工计算二进制并转换为最终的卦象，为了解决这个问题，笔者基于python实现了一套科学算命工具，用于快速进行占卜。

本文的算命方式采用八卦 + 周易+ 梅花易数实现，脚本基于python3.9.0开发。本人对于周易五行研究较浅，如有疏漏请见谅 最终效果如图，在运行程序之后，会根据当前的运势自动获取你心中所想之事的卦象（本卦、互卦、变卦）

### 前置知识 

#### 基础原理

首先我们需要了解一些最基本的占卜知识，目前我国几种比较主流的占卜方式基本都是基于易演化而来。总体而言都是根据某些现象，得到不同的卦象，而不同的卦象最终会代表所占卜事情的开端，发展和结果。

>  
  太极生两仪，两仪生四象，四象生八卦 
 

这句话相信大家在很多影视作品中都听说过，但很少有人知道它的真正含义，这句话其实概括了卦象产生的流程。
- 太极：代表一个绝对混沌的状态，是一个哲学观念，非要套用我们的客观世界，可以理解为是大爆炸之前宇宙的状态，所有的物理法则都不生效，当我们还未起卦时就处于这个状态。- 两仪：同样是一个哲学观念，代表一个事物的两个对立状态，套用到客观世界可以是“生-死”、“黑-白”、“清-浊”，在占卜的过程中，我们通常会有“阴-阳”两个状态，为了方便记录，古人发明了两个符号代表这两个状态，在占卜的时候，一个这样的状态我们称之为一爻（yao）- 四象：当我们将阴阳两两组合时，就可以得到四种不同的组合，古人称之为四象，注意，这里的四象同样是哲学层面的状态，它可以是“青龙白虎朱雀玄武”，也可以是东南西北四个方位，在占卜的时候，我们通常会用“太阴”、“少阴”、“太阳”、“少阳”来称呼这四象- 八卦：当给我们在四象中增加一爻，也就是三个阴阳组合在一起的时候，我们可以得到八个组合，古人认为这八个组合可以代表自然界中的八类事物（八中状态），即是为八卦
当然，八个状态用来代表事情的发展方向还是不够用，于是古人又将八卦（单独的八卦称之为经卦）两两组合，从而得到了64个不同的别卦，易经中的六十四卦就是这么产生的

目前，国内的主流占卜基本都是通过不同的取数方式得到不同的别卦，最终判断事情的走向。其实对于程序员来说，可以吧两仪当做一个一位二进制数，有0、1两个状态。四象就是两位二进制数，有00,01,10,11四个状态。八卦则是三位二进制数，有000,、001、010、011、100、101、110、111四个状态

#### 如何产生卦象

现在我们知道了卦象是如何演变的，但是我们还没有能够得到卦象的方式，其实在占卜的过程中，不同的占卜方式往往最大的区别就是起卦方式不同，我们这里采用梅花易数的方式起卦。

梅花易数起卦法（这里只截取两种起卦方式）：

**1、年月日时起卦**

即以农历之年月日总和除以八，以余数为卦数求上卦;以年月日时总和除以八，以余数为卦数求下卦，再以年月日时总和除以六，以余数为动爻。

例：农历壬申年四月十一日巳时起卦：申年9数，巳时6数。

上卦为：（年+月+日）÷8，取余数。即：（9+4+11）÷8，此处无余数。

下卦为：（年+月+日+时）÷8，取余数。即：（9+4+11+6）÷8，余数为6为坎卦。

动爻数为：（年+月+日+时）÷6，取余数。即：（9+4+11+6）除以6，此处无余数。

此卦为：上卦为坤，下卦为坎，动爻为上爻。

**2、直接以数起卦**

这是一种简便而准确率极高的起卦方法。当有人求测某事时，可以让来人随意说出两个数，第一个数取为上卦，第二个数取为下卦，两数之和除以6，余数为动爻，或者可以随便借用其他能得到两数的办法起卦，如翻书、日历等等。

### 开发 

我们将梅花易数的起卦方式流程用程序员的话总结一下，流程如下
1. 获取一个随机数（我们这里用当前的时间戳）对8取模，当做上挂（一个三位二进制数）1. 再获取一个随机数，对八取模，当做下挂（一个三位二进制数）1. 将上述两个随机数进行组合，得到一个六位二进制数1. 六位二进制数转化为十进制数并查表，得到本卦1. 取一个随机数，对6取模，将上述六位二进制数对应位数的0变为1,1变为0，然后转化为十进制数并查表，得到变卦1. 根据本卦和变卦查表，得到占卜结果
```
import json
import random
import time

#别挂配置数据
gua_data_path = "data.json"

#别卦数据
gua_data_map = {
        
}
fake_delay = 10

#读取别卦数据
def init_gua_data(json_path):
 with open(gua_data_path,'r',encoding='utf8')as fp:
  global gua_data_map
  gua_data_map = json.load(fp)
#爻图标映射
yao_icon_map = {
 0:"- -",
 1:"---"
}

#经卦名
base_gua_name_map = {
 0:"坤",1:"震",2:"坎",3:"兑",4:"艮",5:"离",6:"巽",7:"乾"
}

#数字转化为二进制数组
def base_gua_to_yao(gua, yao_length=3):
 result = []
 while gua &gt;= 1:
  level = 0 if gua % 2 == 0 else 1
  gua //= 2
  result.append(level)
 while len(result) &lt; yao_length:
  result.append(0)
 return result

#二进制数组转化为数字
def base_yao_to_gua(array):
 array = array[:]
 while len(array) &gt; 0 and array[-1] == 0:
  array.pop()
 result = 0
 for i in range(len(array)):
  if array[i] == 0:
   continue
  result += pow(2, i)
                
 return result

#打印一个挂
def print_gua(gua):
 yao_list = base_gua_to_yao(gua, 6)
 up_yao_list = yao_list[0:3]
 up = base_yao_to_gua(up_yao_list)

 print(yao_icon_map[up_yao_list[2]])
 print(yao_icon_map[up_yao_list[1]] + " " + base_gua_name_map[up])
 print(yao_icon_map[up_yao_list[0]])
        
 print("")

 down_yao_list = yao_list[3:6]
 down = base_yao_to_gua(down_yao_list)
 print(yao_icon_map[down_yao_list[2]])
 print(yao_icon_map[down_yao_list[1]] + " " + base_gua_name_map[down])
 print(yao_icon_map[down_yao_list[0]])

#使用梅花易数
def calculate_with_plum_flower():
 #起上卦
 print("使用梅花易数♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️")
 print_a_wait_animation("卜上卦：", fake_delay)
 up_base_gua = int(round(time.time() * 1000)) % 8
 up_yao_array = base_gua_to_yao(up_base_gua)
 print("上卦获取成功,上卦为:", base_gua_name_map[up_base_gua])
 #起下卦
 print_a_wait_animation("正在获取下卦：", fake_delay)
 down_base_gua = random.randint(0, 999999999999) % 8
 down_yao_array = base_gua_to_yao(down_base_gua)
 print("上卦获取成功,下卦为:", base_gua_name_map[down_base_gua])
 #组成卦象
 print_a_wait_animation("正在组成本卦：", fake_delay)
 print("------------------------------------------------本卦------------------------------------------------")
 yao_list = up_yao_array + down_yao_array
 gua = base_yao_to_gua(yao_list)
 print_gua(gua)
 #读取本卦象信息
 gua_code = str(base_gua_name_map[up_base_gua]) + str(base_gua_name_map[down_base_gua])
 gua_data = gua_data_map[gua_code]
 print("本卦为:", gua_data['name'])
 print("辞:", gua_data['words'],"译:",gua_data['white_words'])
 print("象:", gua_data['picture'],"译:",gua_data['white_picture'])
 print_a_wait_animation("正在组成互卦：", fake_delay)
 print("------------------------------------------------互卦------------------------------------------------")
 #读取互卦象信息
 up_hu_yao_list = [yao_list[4],yao_list[5],yao_list[0]]
 up_hu_gua = base_yao_to_gua(up_hu_yao_list)
 down_hu_yao_list =[yao_list[5],yao_list[0],yao_list[1]]
 down_hu_gua = base_yao_to_gua(down_hu_yao_list)
 hu_yao_list = up_hu_yao_list + down_hu_yao_list
 hu_gua = base_yao_to_gua(hu_yao_list)
 hu_gua_code = str(base_gua_name_map[up_hu_gua]) + str(base_gua_name_map[down_hu_gua])
 hu_gua_data = gua_data_map[hu_gua_code]
 print_gua(hu_gua)
 print("互卦为:", hu_gua_data['name'])
 print("辞:", hu_gua_data['words'],"译:",hu_gua_data['white_words'])
 print("象:", hu_gua_data['picture'],"译:",hu_gua_data['white_picture'])
 print_a_wait_animation("正在组成变卦：", fake_delay)
 print("------------------------------------------------变卦------------------------------------------------")
 change_index = int(round(time.time() * 1000)) % 6
 change_yao_list = yao_list[:]
 change_yao_list[change_index] = 0 if change_yao_list[change_index] == 1 else 1
 up_change_yao_list = change_yao_list[0:3]
 up_change_gua = base_yao_to_gua(up_change_yao_list)
 down_change_yao_list =change_yao_list[3:5]
 down_change_gua = base_yao_to_gua(down_change_yao_list)
 
 change_gua = base_yao_to_gua(change_yao_list)
 print_gua(change_gua)
 change_gua_code = str(base_gua_name_map[up_change_gua]) + str(base_gua_name_map[down_change_gua])
 change_gua_data = gua_data_map[change_gua_code]
 print("变卦为:", change_gua_data['name'])
 print("辞:", change_gua_data['words'],"译:",change_gua_data['white_words'])
 print("象:", change_gua_data['picture'],"译:",change_gua_data['white_picture'])

def print_a_wait_animation(tips,times):
 animation = "|/-\\"
 idx = 0
 for i in range(times):
  print(tips + animation[idx % len(animation)],animation[idx % len(animation)],animation[idx % len(animation)],animation[idx % len(animation)],animation[idx % len(animation)], end="\r"),
  idx += 1
  time.sleep(0.1)

init_gua_data(gua_data_path)
calculate_with_plum_flower()
```

### 源代码 

源码在公众号**Python小二**后台回复**占卜**获取~

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/9df89d746c844bec8d06bff520e3466d.gif" alt="9df89d746c844bec8d06bff520e3466d.gif">
