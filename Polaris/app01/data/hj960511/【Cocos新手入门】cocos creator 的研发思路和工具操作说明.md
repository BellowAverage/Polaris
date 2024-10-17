
--- 
title:  【Cocos新手入门】cocos creator 的研发思路和工具操作说明 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解cocos creator 的研发思路和工具操作说明 作者：任聪聪 日期：2023年1月29日 


## 研发思路

### 关于cocos creator 工具说明

首先cocos creator 是一个编辑游戏界面的窗口，省去了我们日常开发游戏时频繁修改参数调整动画、场景的工作。即为我们提供了：所见即所得的游戏开发方式。

其次cocos creator 是帮助我们对设计的场景、精灵、动画等进行管理的一个工具，他能够帮我们管理和关联资源及脚本，以及不同场景的编辑。

### 关于cocos creator 编程思路

在我们通过使用cocoscreator后，对对应的精灵和组件进行绑定脚本和事件来监听相对应的操作和动画的展现。如下图： <img src="https://img-blog.csdnimg.cn/7d88c826b084439bb425564d5a5dd7d6.png" alt="在这里插入图片描述"> 总结：可以理解为cocos creator 就是cocos游戏引擎的一个可视化的界面、动画及资源管理的工具，在我们设计好界面后，通过其他的编辑器进行代码层次的控制，利用代码控制显示切换、动画播放、人物走动等，这便就是它的基本研发思路。

## cocos creator 工具操作说明

### 1.资源管理器、场景编辑器、层级管理器的对应关系说明

#### 1.1 关联性说明

资源管理器中创建的场景可以双击进入到场景编辑器中进行特定的刻画。 <img src="https://img-blog.csdnimg.cn/1f95a14ad3cc492c8522c559475eb46c.png" alt="在这里插入图片描述"> tips：script 脚本可以拖拽到node的节点组件中进行关联，这样button就可以监听和绑定到事件。

#### 1.2 新建场景说明

鼠标右键asset即可看到scene，点击scene即可创建新的场景。 <img src="https://img-blog.csdnimg.cn/6b03b60cd0b74383a174ccdca496b0f4.png" alt="在这里插入图片描述"> 点击后，双击scene后，设置一个新的场景名称 <img src="https://img-blog.csdnimg.cn/c92479eb995c4fdfb2403e8ca3506c19.png" alt="在这里插入图片描述"> 如上便是我们新建的play场景，在这个场景我们可以对其进行针对性的刻画，右侧的控件库中可以让我们增加相对应的精灵、文本、富文本、表单等等。

#### 1.3 控件库组件及node

<img src="https://img-blog.csdnimg.cn/f6fb010ae5d54baf80e6f5a9894efa48.png" alt="在这里插入图片描述"> tips：这里的控制库可以让我们构建出按钮、菜单、表单、场景等游戏元素的展示。

添加组件菜单：能够帮我们设置单个组件的属性和关联的脚本及绑定的事件等。 <img src="https://img-blog.csdnimg.cn/93a38c3bc49447478db8d603fc5f5541.png" alt="在这里插入图片描述">

#### 1.4 绑定脚本操作

首先你需要点击script穿件一个typescript的文件脚本。 <img src="https://img-blog.csdnimg.cn/d1f0a7f7f88d4f31961fffa72185c9b0.png" alt="在这里插入图片描述">

然后点击层级管理器中的canvas或者你想绑定脚本的任意一个节点。 <img src="https://img-blog.csdnimg.cn/52a7a2ec434c40a3b0d715cc429cadea.png" alt="在这里插入图片描述">

在这个节点的属性配置中选择添加组件–&gt;添加用户脚本即可完成，对脚本的绑定。 <img src="https://img-blog.csdnimg.cn/e79efb8e02194315b457e785ef5ba17c.png" alt="在这里插入图片描述">

#### 1.5 绑定事件操作

前提条件：在我们对层级管理器中的单个节点进行了绑定脚本后，我们可以点击任意一个元素，添加组件为按钮类型，进行绑定脚本中书写好的函数。

如下是我的绑定脚本中的代码信息（这里我们要做的是将一个富文本绑定上onStartGame函数）： <img src="https://img-blog.csdnimg.cn/7ea71c6bb4c34e75a9212d0df23d0ad5.png" alt="在这里插入图片描述"> 回到我们的cocos creator中，选中富文本组件，点击添加组件 <img src="https://img-blog.csdnimg.cn/0fce3ec75e8440feb64696f580902805.png" alt="在这里插入图片描述"> 选择ui中的button <img src="https://img-blog.csdnimg.cn/e91d6e37409c4b18ab88fe4790fa0e1a.png" alt="在这里插入图片描述"> 选择后这个元素即变成了按钮可供点击： <img src="https://img-blog.csdnimg.cn/827c0f30d6b740fe877b1b2fa5a17f40.png" alt="在这里插入图片描述"> 此处我们在click events中输入1，来绑定这次的函数。 <img src="https://img-blog.csdnimg.cn/c3b83a4cd9c8432f80cdf1cd4c71d9f7.png" alt="在这里插入图片描述">

将绑定过脚本的节点拖拽到这里 <img src="https://img-blog.csdnimg.cn/411ea3909a2f4d81bf9694fe19e93700.png" alt="在这里插入图片描述"> 依次选择脚本和函数即可完成函数的监听绑定 <img src="https://img-blog.csdnimg.cn/806dea7d342141408225c2dc4d74a3c1.png" alt="在这里插入图片描述"> tips:如果需要获取传递的参数，记得使用e,正确的监听函数写法如下：

```
    onStartGame(e,youValName){<!-- -->
        console.log(e,youValName);
    }

```

监听效果： <img src="https://img-blog.csdnimg.cn/5db0c43444304d97bb252e843ae8bbae.png" alt="在这里插入图片描述">

### 2.工具常用设置说明

工具的设置实际上我们只需要将脚本编辑器和图片编辑器进行关联即可，其他的设置基本上并不常用。

step1：如下图，点击文件即可看到设置菜单的入口： <img src="https://img-blog.csdnimg.cn/7147e083a05a469e9b1cbb11e1f61ee3.png" alt="在这里插入图片描述"> step2：点击设置进入到设置界面： <img src="https://img-blog.csdnimg.cn/c04a5fc3d8e5453fb5d39ca7fa1272cc.png" alt="在这里插入图片描述"> 说明：此处可以设置我们的编辑器为中文，点击编辑器语言即可进行更改。

step3:：点击数据编辑 <img src="https://img-blog.csdnimg.cn/6cb60ccd9552423cafe06b179bebc8a6.png" alt="在这里插入图片描述"> 说明：这里是我已经设置好的，实际上在没有设置的时候，我们可以点击浏览，来关联编辑软件的exe文件，如vscode的exe，我们只需要在打开浏览后选择他的exe或者快捷键所在目录路径即可。

### 3.构建发布游戏说明

step1：点击项目，点击构建发布 <img src="https://img-blog.csdnimg.cn/79d0315d311c47c0b233e9e3e416b9f2.png" alt="在这里插入图片描述"> step2：选择对应的平台 <img src="https://img-blog.csdnimg.cn/c49a0aa8704c4d63a4c3edce08aab357.png" alt="在这里插入图片描述"> 说明：选择后即可根据相对应的小游戏的appid进行配置，配置完毕后即可点击构建，我们将可以在相对应的平台小游戏开发工具中进行发布。

## 其他方面解答

### 1.代码可以控制场景吗？

cocos本身代码就可以控制，详细的操作会在下个章节讲解。

### 2.动画可以通过cocos creator实现吗？

动画的制作也可以通过cocos creator 工具来实现，同时也可以通过代码进行控制。
