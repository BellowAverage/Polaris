
--- 
title:  【Cocos新手入门】 cocos creator 制作 select下拉框且可以选择获取选中参数数值的方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解使用cocos creator 制作 select下拉框且可以选择获取选中参数数值的方法。 作者：任聪聪 日期：2023年2月7日 cocos 引擎版本：2.4.3 


在我们实现select框的时候，我们可以通过按钮+显示隐藏某个元素来达成这个目标，如下是整体的select框自定义及传参获取的方法教程。

## 效果展示

可以看到这是一个非常简单流畅的select下拉框。 <img src="https://img-blog.csdnimg.cn/3d7013226e3049e2b044262dab1b50e8.gif" alt="在这里插入图片描述">

## 实现方式

步骤一、使用creator 在按钮下面制作一个select box的空节点，然后刻画出一个下拉框。 <img src="https://img-blog.csdnimg.cn/8fef17ecdd2b4b619d6ffeeafa5f716e.png" alt="在这里插入图片描述">

tips：要使用layout布局进行刻画，设置如下（box层级）。 <img src="https://img-blog.csdnimg.cn/cb92a9dcd39e4f2183616cbe23c5cdff.png" alt="在这里插入图片描述"> tips: 不要忘记了在box中填充label类型的item文本，用它来模拟select中的option对象。

整体结构说明：

```
-box
	--- item
	--- item
	--- item
	--- item
	--- item
	--- item
	--- item

```

步骤二、item的设置参数，给每个item设置不同的值 <img src="https://img-blog.csdnimg.cn/0d3d7529557747329270c79d9538ec11.png" alt="在这里插入图片描述"> tips：这里需要绑定button，才可以实现点击传值的效果。 <img src="https://img-blog.csdnimg.cn/949d0f5254cb493aad72fe7a56203604.png" alt="在这里插入图片描述"> 说明：这里绑定的事件传递的是字符串，代码层次是通过转换成数组来实现获取参数的。

步骤三、绑定指定的box及label，并默认隐藏box（将opacity设置为0）

在代码中声明：

```
    @property(cc.Label)
    color_select_box_lab: cc.Label = null;

    @property(cc.Node)
    color_select_box : cc.Node=null ;

```

隐藏box。 <img src="https://img-blog.csdnimg.cn/5790971cbd614142a9927110dcb813ff.png" alt="在这里插入图片描述"> 步骤三、拖拽绑定组件对象： <img src="https://img-blog.csdnimg.cn/d5e80df7590e4a92a188b423bcb26fa3.png" alt="在这里插入图片描述"> 步骤四、给下拉框按钮绑定显示事件 <img src="https://img-blog.csdnimg.cn/211200bed4f64b9d8a4111897800cf11.png" alt="在这里插入图片描述"> 通过事件显示box：

```
	showSelect(){<!-- -->
				if(that.color_select_box.opacity==0){<!-- -->
                    that.color_select_box.zIndex = 100;
                    that.color_select_box.opacity = 255;
                }else{<!-- -->
                    that.color_select_box.zIndex = 0;
                    that.color_select_box.opacity = 0;
                }
      }

```

步骤五、给item绑定按钮 <img src="https://img-blog.csdnimg.cn/2cdebed9927a4ebf8bc400f3a475b674.png" alt="在这里插入图片描述"> 获取参数代码：

```
itemClicked(e,v){<!-- -->
		//v为传递的参数
        cc.log(e,v)
        let t_arr = v.split(',');
        //修改按钮的label文本
           that.color_select_box_lab.string = t_arr[1].toString();
        //隐藏select
                that.color_select_box.zIndex = 0;
                that.color_select_box.opacity = 0;
        }

```

## 相关文章：

  
