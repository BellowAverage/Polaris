
--- 
title:  unity 期末大作业-打僵尸怪物游戏（含下载链接，源码+导出exe+简单文档） 
tags: []
categories: [] 

---
### unity 期末大作业-打僵尸怪物游戏（含下载链接，源码+导出exe+简单文档）

ASDW移动键（或者上下左右箭头），E对话提示信息，C发射子弹，吃金币增加子弹，有血包可以吃，有血量显示，僵尸怪物可以攻击人物使其掉血，路过路障也会掉血，子弹打中怪物就不会再追击，击败所有怪物打开下一关； 具体如下图所示：



<img src="https://img-blog.csdnimg.cn/direct/01454f1f8019403cb227ce6bd6d13f08.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/256507ffc3c2413987b7b9f08c4ac19b.gif" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/55cc7e8b73a44a1ab1251159d0e9094f.gif" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/eedb4d5070e14506a3184c76f4e47b16.gif" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/833f7c4498eb470cabce172995f612fe.gif" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/350d06fc584f428993223e9298b26d39.gif" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/1d4f3c2dcfd240f28be142f2eb9fa6c0.png" alt="在这里插入图片描述"> 尽量使用unity2018

## 1 导入资源

### 1.1 找资源

### 1.2 导入资源

### 1.3 认识资源

## 2 认识窗口

### 2.1 资源窗口

### 2.2 游戏窗口

## 3 上下左右移动

### 3.1 创建文件夹和脚本

### 3.2 获取wsad

### 3.2 获取位置

### 3.3 保证速度

### 3.4 返回位置

## 4 tilemap

### 4.1 创建telemap

### 4.2 打开tile Palett窗口

### 4.3 调整tile为9格

### 4.4 拖入tile到tile Palett

### 4.5 调整 Pixels Per Unit 为64

### 4.6 将tile的order in layer调为-10

## 5 加入装饰物品

### 5.1 设置物品与人物的遮挡效果

### 5.2 调整物品判定中心

### 5.3 调整人物中心

### 5.4 建立预制件

### 5.5 将铁箱子变成金箱子

## 6 物品阻止移动

### 6.1 为人物添加Rigidbody 2D

### 6.2 禁用重力

### 6.3 添加Polygon Collider 2D

Box Collider太假了，换成了Polygon Collider

### 6.4 调整碰撞体积

### 6.5 禁用旋转

### 6.6 在代码中使用Rigidbody 2D

在代码中使用Rigidbody 2D，以防止物理强行移回人物造成的人物抖动

### 6.7 添加Tilemap Collider 2D

### 6.8 添加Composite Collider 2D

将小碰撞体组合，以提高性能

### 6.9 添加圆形透明物体

以弥补水流圆形地砖的大面积无法运动问题，扩大一定边界解决人物卡入问题

## 7 可收集的物品

### 7.1 添加生命值

公共的最大生命值

公共的当前生命值

Mathf.Clamp控制范围

### 7.2 触发器

设置触发器

触发器代码

判断是否触发

减小图层，一直显示在人物之下

## 8 攻击区域和敌人

### 8.1 攻击区域

攻击区域图像自动扩充

攻击区域代码

预制体

### 8.2 敌人

#### 8.2.1 导入控件和配置

教学是碰撞减血，但是现实中怪物不会等人碰到之后才攻击，是有攻击范围的

第一个区域用来判定刚体，第二个区域用来判定伤害，扁平的长方形更真实

#### 8.2.2 敌人代码

增大质量，防止敌人被角色推动

## 9 角色动画

### 9.1 创建Animator Controller

### 9.2 添加并设置Animator

### 9.3 使用Animation创建行走动画

感觉4有些别扭，改成6更顺畅一点

将中间两帧放到后面，让摆臂更自然顺畅

更换BoxCollider2D，并以手臂为基准重新设计攻击范围

### 9.4 设置Blend Tree

### 9.5 添加混合树代码

### 9.6 挂载ruby动画编写代码

## 10 丢出齿轮

### 10.1 创建齿轮，并配置BoxCollider2D和一个 Rigidbody2D

### 10.2 编写飞弹代码

### 10.3 ruby中添加发射代码

### 10.4 设置角色图层和飞弹图层

### 10.5 编写机器人修复代码

### 10.6 3s后齿轮销毁

### 10.7 机器人动画

依旧是4帧整理出6帧，让动画顺滑。Sample为6

## 11 摄像机跟随

### 11.1 添加Cinemachine 包

最新版报错，官网文档2.7.3也不行，垃圾官网。最终决定使用官方ruby教程的2.3.4的前一版2.2.9（垃圾官网，教程的包都没了）

### 11.2 配置Cinemachine

### 11.3 简单大地图和边界

### 11.4 调整飞弹图层

## 12 损坏机器人的烟雾粒子

### 12.1 创建Particle System

### 12.2 配置Particle System

增加随机性和渐变消失，以及跟随移动

### 12.3 编写修复消失代码

## 13 生命值（UI）

### 13.1 添加外框并设置锚点

### 13.2 添加头像并设置锚点

### 13.3 添加生命值条和设置Mask

### 13.4 编写生命值条的脚本

## 14 NPC与对话

### 14.1 创建NPC

npc动画变为三次呼吸一次眨眼，帧数为3

### 14.2 设置UI和文字

官方教程让用Text - TextMeshPro，虽然更好用，但是对于多语言支持较差，并且只是一个简单UI，因此改为直接使用Text

使用互补色并稍微提高饱和度高亮关键词

### 14.3 设置触发器射线投射并编写代码

## 15 背景音乐与游戏音效

### 15.1 背景音乐

### 15.2 拾取到生命值包、投掷齿轮或被攻击的声音

### 15.3 机器人走路的声音

### 15.4 修正衰减

### 15.5 机器人修复后停止播放走路声

## 16 参考b站视频

### 16.1 子弹数量

#### 16.1.1 UI

#### 16.1.2 ruby代码

#### 16.1.3 子弹包代码

#### 16.1.4 UI代码

### 16.2 物品动画

#### 16.2.1 草莓

#### 16.2.2 子弹包

### 16.3 其他粒子效果

#### 16.3.1 设置收集效果

#### 16.3.2 草莓代码

#### 16.3.3 子弹包代码

## 17 自由发挥

### 17.1 击中后产生火花

### 17.2 制作更多预制体

### 17.3 对话引导和动画

### 17.4 简单绘制地图

岛屿的路，按顺序为我的学号0217

### 17.5 机器人一定范围后追人物

### 17.6 关卡判定

### 17.7 boss

### 17.8 死亡重新开始和UI按键指导

### 17.9 完成恭喜界面

### 17.10 完善场景

## 18 构建、运行、分发

### 18.1 构建游戏

发现死亡重置地图代码有问题，修改后就通过编译了


