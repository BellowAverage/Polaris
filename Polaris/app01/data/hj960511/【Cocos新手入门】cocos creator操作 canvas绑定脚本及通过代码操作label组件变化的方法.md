
--- 
title:  【Cocos新手入门】cocos creator操作 canvas绑定脚本及通过代码操作label组件变化的方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解利用cocos creator操作 canvas绑定脚本及通过代码操作label组件变化的方法 作者：任聪聪 日期：2023年1月31日 本篇文章仅适合cocos 2.4.3引擎版本下进行练习，其他版本可参考只有写法不同。 


## 基本的操作说明

步骤一、通过cocos creator 给canvas绑定自己创建的脚本。 <img src="https://img-blog.csdnimg.cn/f1a26af0a3ef4b6388084af82d7e17c8.png" alt="在这里插入图片描述"> 步骤二、在脚本中声明组件，代码如下

```
const {<!-- -->ccclass, property} = cc._decorator;

@ccclass
export default class loading extends cc.Component {<!-- -->

    @property(cc.Label)
    loading_txt: cc.Label = null;

    @property(cc.Sprite)
    bg:cc.Sprite = null;

    // LIFE-CYCLE CALLBACKS:

    onLoad () {<!-- -->
        // this.node.getChildByName("loading_txt").getComponent(cc.Label).string="111111";
        this.loading_txt.string = "恭喜恭喜"
    }
    //执行加载并跳转到主页面
    start () {<!-- -->

    }
    // update (dt) {<!-- -->}
}


```

tips：创建的新的脚本重命名后记得修改class的名。

步骤三、刷新后可以看到 canvas的属性菜单中出现了声明的组件 <img src="https://img-blog.csdnimg.cn/428fc90292e1493ba856db24fa1b22e0.png" alt="在这里插入图片描述">

步骤四、绑定制定的元素： <img src="https://img-blog.csdnimg.cn/8a805c0f2144486c801d63e8b5503193.png" alt="在这里插入图片描述"> 步骤五、通过代码修改指定元素

```
   onLoad () {<!-- -->
        // this.node.getChildByName("loading_txt").getComponent(cc.Label).string="111111";
        this.loading_txt.string = "恭喜恭喜"
    }

```

实际效果： <img src="https://img-blog.csdnimg.cn/c501b26356d7436e9a65cd1f8341640a.png" alt="在这里插入图片描述"> 可以看到通过代码将创建的界面label组件的string内容进行了修改，同理背景也是如此的修改方式。

## 注意

组件的属性记得修改成下划线形式 <img src="https://img-blog.csdnimg.cn/dc6266d4d81c4473a33fd888bf887b31.png" alt="在这里插入图片描述">
