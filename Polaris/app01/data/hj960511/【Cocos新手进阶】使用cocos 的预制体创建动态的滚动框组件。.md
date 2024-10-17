
--- 
title:  【Cocos新手进阶】使用cocos 的预制体创建动态的滚动框组件。 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，使用cocos 游戏引擎制作动态生成的滚动框实例教程。 日期：2023年11月1日 作者：任聪聪 引擎版本：2.4.3 至 2.4.11 


## 关于预制体的说明和概念

cocos中的预制体的作用是能够让你使用数据的形式进行控制界面的变化，同时可以对界面中的相关动态元素进行绑定，在界面中显示相对应的动态变化。

在开发的过程中，可以将单个做好的组件变为预制体，这可以在未来的开发和修改过程中让自己更为事半功倍的进行二次的开发和修改工作，避免一个个界面和场景进行修改。只需要在其他场景中引用预制体即可。

## 实际效果：

效果说明：不需要手动进行创建，cocos引擎自动加载数据创建一个动态的界面。 <img src="https://img-blog.csdnimg.cn/a295867de0ec4344bce4e7601dda8d7e.gif#pic_center" alt="在这里插入图片描述">

## 一、打开我们的cocos dashboard 创建一个空项目命名为 preFabDemo

### 步骤一、打开后进入到如下界面，找到顶部的新建项目如下图。

<img src="https://img-blog.csdnimg.cn/cbd27efc465145668c88c35d21cf91c5.png" alt="在这里插入图片描述">

### 步骤二、点击新建项目后，进入如下界面。

<img src="https://img-blog.csdnimg.cn/b1fbf8fe1e3041c0b9bce358e2d64d57.png" alt="在这里插入图片描述"> 提示说明：选择指定的版本并在左下方项目名称处，修改项目名称为“preFabDemo ” 点击创建并打开。

## 二、构建一个页面并创建相对应的脚本及预制体的声明

### 步骤一、找到资源管理器，右键assets，选择scene，如下图。

<img src="https://img-blog.csdnimg.cn/96a0afb7685c48b7902802e60f2c8c5d.png" alt="在这里插入图片描述">

### 步骤二、将页面名命名为home，如下图。

<img src="https://img-blog.csdnimg.cn/8e60b5b1b86d4c8daa8203c5c3f01173.png" alt="在这里插入图片描述">

### 步骤三、创建一个home同名的ts脚本如下图：

<img src="https://img-blog.csdnimg.cn/71989ffdc901407a857b1032e7ce8650.png" alt="在这里插入图片描述"> 说明：方法一致都是点击assets右键菜单中选择。

### 步骤四、双击打开home的ts脚本，修改脚本类名如下图

<img src="https://img-blog.csdnimg.cn/c434de1e68944cd59ded6710a334ecfd.png" alt="在这里插入图片描述"> 修改为 home 。 <img src="https://img-blog.csdnimg.cn/0253d8c9fcc84237b8e4e86136ebe1e0.png" alt="在这里插入图片描述"> 提示：创建完其他的脚本也需要进行修改不然会报错喔。

### 步骤五、构建home界面的相关功能组件。

#### 组件一、动态显示item信息的滚动框

操作说明：在home界面中创建一个滚动框组件如下图，拖拽到画布中即可。 <img src="https://img-blog.csdnimg.cn/51dd6b23b26f41dc93d1c7aa0931f439.png" alt="在这里插入图片描述">

#### 组件二、修改content中的lable为：item_label_obj

<img src="https://img-blog.csdnimg.cn/fad6b53f129f40d9aedf68b017f186da.png" alt="在这里插入图片描述"> 修改后： <img src="https://img-blog.csdnimg.cn/6ab98414f4d24b98bc94212e417677b1.png" alt="在这里插入图片描述">

### 步骤六、创建item_label_obj 的ts脚本 如下：

<img src="https://img-blog.csdnimg.cn/7686f6f2782c4aa7a6f45dc9b14b8fb3.png" alt="在这里插入图片描述">

### 步骤七、点击home 的页面文件，回到home 的界面中，对界面的滚动框和item进行自适应的调整

详细操作教程见：

### 步骤八、给 item_label_obj 组件添加上脚本关联，如下图：

<img src="https://img-blog.csdnimg.cn/1f46cf3a1a174dc886ef370fb3a5c130.png" alt="在这里插入图片描述"> 然后，将组件进行关联label： <img src="https://img-blog.csdnimg.cn/f65da2d127db47d09f438b45368ac6a5.png" alt="在这里插入图片描述"> 构建 item_label_obj.ts的代码如下：

```
const {<!-- -->ccclass, property} = cc._decorator;

@ccclass
export default class item_label_obj extends cc.Component {<!-- -->

    @property(cc.Label)
    label: cc.Label = null;

    /**
     * onLoad 
     */
    protected onLoad(): void {<!-- -->
 
    }
    /**
     * 初始化
     * @param data 
     */
    public createdPre(data: {<!-- --> title: string }) {<!-- -->
        console.log(data);
        this.label.string = "我是第："+data.title+"个，预制体。";
        //给label 注册事件监听
        this.node.on(cc.Node.EventType.TOUCH_END, this.click_info_log, this);
    }
 
    /**
     * 事件监听
     */
    protected click_info_log() {<!-- -->
        console.log(`成功点击:[${<!-- -->this.label.string}]`);
    }
}




```

### 步骤九、选中做好的 item_label_obj ，并拖拽到底部，将其编程预制体。

<img src="https://img-blog.csdnimg.cn/4d48aec1b60a4e6fbc37b8855091a721.png" alt="在这里插入图片描述"> 完成效果说明： <img src="https://img-blog.csdnimg.cn/01ae867f13f34614a032c4ccec007cef.png" alt="在这里插入图片描述">

### 步骤十、在home脚本中创建和声明预制体、预制体的父级节点，及引入预制体脚本和生成预制体的代码。

```

import item_label_obj from "./item_label_obj";

const {<!-- -->ccclass, property} = cc._decorator;

@ccclass
export default class home extends cc.Component {<!-- -->

    @property({<!-- -->
        type: cc.Prefab,
        displayName: "预制体对象"
    })
    protected preItemObj: cc.Prefab = null;
 
    @property({<!-- -->
        type: cc.Node,
        displayName: "预制体父节点"
    })
    
    protected preItemObjParent: cc.Node = null;
 
    protected preData: Array&lt;{<!-- --> title: string}&gt; = [];
 
    protected onLoad(): void {<!-- -->
        let temporaryData = null;
        let num = 0;
        //循环生成60个预制组件数据
        for (let i = 0; i &lt; 60; i++) {<!-- -->
            temporaryData = {<!-- -->
                title: ""
            };
            temporaryData.title = `${<!-- -->++num}`;
            this.preData.push(temporaryData);
        }
        //根据数组情况批量创建预制体
        let length = this.preData.length;
        for (let i = 0; i &lt; length; i++) {<!-- -->
            let prefabricatedObject = cc.instantiate(this.preItemObj);
            prefabricatedObject.parent = this.preItemObjParent;
            //初始化预制体对象并执行
            prefabricatedObject.getComponent(item_label_obj).createdPre(this.preData[i]);
        }
    }
}


```

完成后回到cocos dashboard 中，将组件的层级进行拖拽管理，具体事宜如下。 <img src="https://img-blog.csdnimg.cn/eeff48602d9e44e79128deff67a39904.png" alt="在这里插入图片描述">

### 步骤十二、点击canvas 创建用户组件，关联脚本。

<img src="https://img-blog.csdnimg.cn/45192271469d467da5205686add3595e.png" alt="在这里插入图片描述"> 而后，将预制体对象进行关联，如下图： <img src="https://img-blog.csdnimg.cn/e8969a1dc7f3489cb648411ac8c0f923.png" alt="在这里插入图片描述"> 而后再将父节点进行关联，如下图： <img src="https://img-blog.csdnimg.cn/d8d7e584d5824a3fbce92a9bf0d3db24.png" alt="在这里插入图片描述">

## 三、运行代码并优化item的样式

运行后，发现效果很差，如下图： <img src="https://img-blog.csdnimg.cn/ae015e134dcc45ea94cb561370b13621.png" alt="在这里插入图片描述"> 这是要由于没有做样式或者样式不对导致的，解决办法如下： <img src="https://img-blog.csdnimg.cn/1ea6677ab86d4690916ae0bca40e8177.png" alt="在这里插入图片描述"> 将content中的配置，按红框中的layout进行配置即可自适应增加高度。
