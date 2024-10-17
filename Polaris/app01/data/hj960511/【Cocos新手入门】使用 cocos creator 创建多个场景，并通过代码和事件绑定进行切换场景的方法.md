
--- 
title:  【Cocos新手入门】使用 cocos creator 创建多个场景，并通过代码和事件绑定进行切换场景的方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解使用 cocos creator 创建多个场景，并通过代码和事件绑定进行切换 作者：任聪聪 日期：2023年1月31日 cocos 引擎版本 2.4.3 


## 场景的创建

步骤一、右击资源管理器下的assets目录，点击新建，献出案件一个scene的文件夹。 <img src="https://img-blog.csdnimg.cn/0de88756c7b64e99b5b39e06b2f80c29.png" alt="在这里插入图片描述"> 步骤二、在我们创建的scene文件夹上右击，点击创建scene场景 <img src="https://img-blog.csdnimg.cn/2fee7e112a9d487aab427a1e5dfe74ea.png" alt="在这里插入图片描述"> 步骤三、这里我创建的新的场景为home，双击home场景文件进入到场景的层级管理界面中 <img src="https://img-blog.csdnimg.cn/25601afdd2df4e12a58c18dcbb5bf400.png" alt="在这里插入图片描述"> tips：同样的想回到上一个场景也是双击进入，此时我们就可以在新的场景中进行布置界面组件了。

## 场景的切换方法

场景的切换可以通过代码进行直接切换，绑定事件进行切换的方式也是使用这样的代码，如下2.1节所说。

### 2.1 代码进行切换

```
 cc.director.loadScene("你的场景名称英文");

```

### 2.2 绑定按钮进行切换

步骤一、通过button进行举例说明，这里我们先在新的场景中创建一个按钮。

<img src="https://img-blog.csdnimg.cn/eec3a6768cdb4fc297f55c37f1edb8a4.png" alt="在这里插入图片描述"> 操作说明：右击main 相机，选择创建节点，选择创建ui节点，选择button按钮。

步骤二、修改我们的button的按钮名称，先点击lable <img src="https://img-blog.csdnimg.cn/569a4741721b4ad291ae734f923137c5.png" alt="在这里插入图片描述"> 注意：此处需要修改按钮的宽度和label的宽度，否则字显示不出完整的样式。

步骤三、创建一个新的场景的脚本文件，右击script文件夹（没有的自己先手动创建这个文件夹），点击新建选择typescript文件 <img src="https://img-blog.csdnimg.cn/370bc0506c034f71939c40dc55e17648.png" alt="在这里插入图片描述">

步骤四、给空节点“Main Camera” 挂上脚本，点击空节点，点击添加组件选择用户脚本。

<img src="https://img-blog.csdnimg.cn/99d4abd7e5f749e0ae2f37ce5700aafb.png" alt="在这里插入图片描述"> tips：点击后看右侧的属性菜单，即可找到添加组件的按钮，在最底部。

步骤五、绑定函数 <img src="https://img-blog.csdnimg.cn/2bf563f8427b433590b5868c9e06cd47.png" alt="在这里插入图片描述"> tips：点击的时间是在eventes中输入1后弹出的，如果不输入1是看不到箭头3所指的框。

步骤五、书写脚本代码函数

```
const {<!-- -->ccclass, property} = cc._decorator;

@ccclass
export default class NewClass extends cc.Component {<!-- -->

    @property(cc.Label)
    label: cc.Label = null;

    @property
    text: string = 'hello';

    // LIFE-CYCLE CALLBACKS:

    // onLoad () {<!-- -->}

    start () {<!-- -->

    }

    test(){<!-- -->
        //测试按钮回到加载场景
        cc.director.loadScene("loading");
    }

    // update (dt) {<!-- -->}
}


```

给按钮绑定这个函数： <img src="https://img-blog.csdnimg.cn/b52633c42e4f4d0e81eb2f36989526cb.png" alt="在这里插入图片描述"> 运行查看实际效果： <img src="https://img-blog.csdnimg.cn/8183d87b909841b2ba0eac4784030c37.gif" alt="在这里插入图片描述">
