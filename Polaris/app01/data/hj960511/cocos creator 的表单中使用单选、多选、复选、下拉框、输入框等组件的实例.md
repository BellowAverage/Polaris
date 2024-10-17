
--- 
title:  cocos creator 的表单中使用单选、多选、复选、下拉框、输入框等组件的实例 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：使用cocos creator 是如何使用表单中单选、多选、复选、下拉框、输入框等组件的方法。 作者：任聪聪 日期：2023年2月7日 cocos 引擎版本2.4.3 


提示: 如果是新手同学，建议结合附件中的demo，来进行学习，这样会有一个整体的操作认知,掌握表单制作的能力也会快一点。

>  
 文章附件下载地址： 


## 一、按钮的使用

### 1.1 构造按钮及修改样式

步骤一、点击button组件，拖拽到画布中 <img src="https://img-blog.csdnimg.cn/38266ed8a49c4586b636395557de22d9.png" alt="在这里插入图片描述"> 步骤二、点击button组件，在左侧可以看到相对应的属性及尺寸，这里我们可以多按钮的大小和尺寸进行调整以及背景和交互效果。 <img src="https://img-blog.csdnimg.cn/82cf8d6647c24bcda9aefb8fcab1f5bc.png" alt="在这里插入图片描述"> 步骤三、修改按钮的名称，点击左侧的层级管理中的，label。 <img src="https://img-blog.csdnimg.cn/fd89bc20d2ba4161a8233307372a87f7.png" alt="在这里插入图片描述"> 在右侧我们就会看到 <img src="https://img-blog.csdnimg.cn/574aff2c2e904ceba6d025eab1c91b27.png" alt="在这里插入图片描述"> 点击修改string为，按钮ok。 <img src="https://img-blog.csdnimg.cn/24a550ff0ebe4110a8b14e251263396f.png" alt="在这里插入图片描述">

### 1.2 事件绑定及获取数据

步骤一、创建一个脚本，右击选择typescript <img src="https://img-blog.csdnimg.cn/1e3c14c876eb4e32ba78d0aa88935ac7.png" alt="在这里插入图片描述"> 步骤二、点击空节点，绑定这个脚本，如下： <img src="https://img-blog.csdnimg.cn/485155c0eb954ccc91da1fb757c14a34.png" alt="在这里插入图片描述"> 步骤三、点击button <img src="https://img-blog.csdnimg.cn/d52a39c3893c4970b8737a11d517aa57.png" alt="在这里插入图片描述"> 找到右侧的click events，输入一 <img src="https://img-blog.csdnimg.cn/f93d6d0d3a4947bbb3eebe065e37b9d3.png" alt="在这里插入图片描述"> 步骤四、拖拽空节点到cc.node中，并选择脚本，选择脚本中的函数。 <img src="https://img-blog.csdnimg.cn/af9d0530e3f548bbaf6514a766a7efd8.png" alt="在这里插入图片描述">

步骤五、修改class name 及创建一个按钮函数

```
    //按钮绑定事件
    testBtn (e,v) {<!-- -->
        cc.log(e,v)
    }

```

creator中的配置 <img src="https://img-blog.csdnimg.cn/cc51bfaab3614043aa06498339f8cabf.png" alt="在这里插入图片描述"> 查看点击效果： <img src="https://img-blog.csdnimg.cn/f8c01906778e4ae4854883adf1fdf38c.png" alt="在这里插入图片描述">

## 二、单选组件绑定及获取参数说明

### 2.1 单选框的配置

步骤一、创建单选框组件 <img src="https://img-blog.csdnimg.cn/59470029d6034e258d272a29e326fa88.png" alt="在这里插入图片描述"> 步骤二、点击 checkmark 修改单选框的默认属性 <img src="https://img-blog.csdnimg.cn/d8c5428a44be427ba540100a35c7e431.png" alt="在这里插入图片描述"> 步骤三、增加文本说明，右击组件选择label <img src="https://img-blog.csdnimg.cn/f6d762efea4e41e8ae817e9552973b22.png" alt="在这里插入图片描述"> label配置如下： <img src="https://img-blog.csdnimg.cn/b9ca5cf17bc44533ab5379336528a35a.png" alt="在这里插入图片描述"> 实际效果： <img src="https://img-blog.csdnimg.cn/543779effd964a87873d7b9333e92774.png" alt="在这里插入图片描述">

### 2.2 单选框获取数据

步骤一、绑定事件，与上一步相同，这里不做细讲 <img src="https://img-blog.csdnimg.cn/24dc721a7bec47c8be4ac254b24fdb90.png" alt="在这里插入图片描述">

步骤二、创建对应事件

```
    //radio事件
    radioBtn(e,v){<!-- -->
        cc.log(v)
        this.radio_txt.string = "单选框数据："+v;
    }

```

实际效果： <img src="https://img-blog.csdnimg.cn/1e28dfa724db4280810bb1e025096d3e.png" alt="在这里插入图片描述">

## 三、多选框的创建及数据获取

步骤一、创建多选框，并自定义多选组件。 <img src="https://img-blog.csdnimg.cn/418c24322c1f4b16a0b119f76cb9073e.png" alt="在这里插入图片描述"> 步骤二、创建事件并绑定事件

事件代码： <img src="https://img-blog.csdnimg.cn/4b56bc999b894285bd67072a08dda179.png" alt="在这里插入图片描述">

绑定事件： <img src="https://img-blog.csdnimg.cn/32300309aebb4c9a8544cb943ef5cf6c.png" alt="在这里插入图片描述"> tips：与其他组件的绑定形式一致。

实际效果： <img src="https://img-blog.csdnimg.cn/9567d541212443ff95d057c7d7410242.png" alt="在这里插入图片描述"> tips：上述需要声明对象，并绑定对象，这个在文章的附件中有整体的体现。也可以看我的这篇文章学习如何声明页面对象，控制页面元素变化。 <img src="https://img-blog.csdnimg.cn/2a779a0664d847058961e38a87c4db61.png" alt="在这里插入图片描述">

如上图所示，本文章所绑定的相关组件信息。

## 四、下拉框

步骤一、创建一个按钮，并修改为如下样式 <img src="https://img-blog.csdnimg.cn/fb818865fe8642d98351014ff434c5b9.png" alt="在这里插入图片描述"> 步骤二、创建一个select_box的空节点 <img src="https://img-blog.csdnimg.cn/65fea47e53f3409faad4e996a4df98bd.png" alt="在这里插入图片描述"> 步骤三、给空节点绑定上layout的布局，并设置为如下，改为：select_item_box <img src="https://img-blog.csdnimg.cn/07c4de8fcaa3421a9703d1c400977184.png" alt="在这里插入图片描述"> 在空节点中创建item，label类型的。 <img src="https://img-blog.csdnimg.cn/898ec234c94741959a6f76e2d0065f21.png" alt="在这里插入图片描述"> 步骤四、修改样式 <img src="https://img-blog.csdnimg.cn/af7be0422a764945bc9680640e5dde92.png" alt="在这里插入图片描述"> 步骤五、将opacity改为0，隐藏itembox

<img src="https://img-blog.csdnimg.cn/ff4895b8501e4522823413d6423ddac1.png" alt="在这里插入图片描述">

步骤六、绑定事件 <img src="https://img-blog.csdnimg.cn/810c4179c1e54c209c7e00ef0d68303e.png" alt="在这里插入图片描述">

事件代码： <img src="https://img-blog.csdnimg.cn/e4496851d1a545bb9455f76fb8c3ca81.png" alt="在这里插入图片描述"> 绑定item的事件 <img src="https://img-blog.csdnimg.cn/52f0fbecf7894606a68f3eac116d4a8c.png" alt="在这里插入图片描述">

## 五、输入框

### 5.1 单行及多行文本说明

<img src="https://img-blog.csdnimg.cn/5fe41b842fd647dd8f164dd4ce6cdec8.png" alt="在这里插入图片描述"> **文本框属性说明** string ：默认的输入框存在的值

placeholder ：提示信息，输入即消失

input mode： any为多行，其他都为单行

max length ： 最大输入字符数限制

### 5.2 文本框的数据获取方式

#### 1.监听状态说明

如下是一个文本框的四种监听状态类型，分为输入开始、输入改变、输入结束、输入返回 <img src="https://img-blog.csdnimg.cn/a30a33f97221462490c04397dd815fbd.png" alt="在这里插入图片描述">

此处的绑定方式也可在我上方提到的文章内容中找到。

#### 2.监听输入数据并赋值

说明：分别为四种形式的数据获取形式，通过一个函数来做演示，查看我们输入表单后对数据的获取效果。

代码片段：

```
	// v 值  e 事件对象  s 为customEventData的值
    getInput(v,e,s){<!-- -->
        console.log(v,e,s)
    }

```

监听效果，四种形式 <img src="https://img-blog.csdnimg.cn/863a94de43d04c6a8f2dfb7e36fc837d.png" alt="在这里插入图片描述"> 故此：我们选择适合自己场景下的方式即可，这里我们选择的是changed 的状态类型

文本框操作详细教程：

最终效果： <img src="https://img-blog.csdnimg.cn/aa57eb60effa488b8f509efddef62346.png" alt="在这里插入图片描述">
