
--- 
title:  【Cocos新手进阶】父级预制体中的数据列表，在子预制体中的控制方法！ 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，cocos中在预制体操作过程中，父级预制体生成的数据列表中，绑定了子预制体中的事件，在子预制体的时间中如何控制上级列表的具体操作教程。 日期：2023年11月10日 作者：任聪聪 


## 一、实际效果情况

<img src="https://img-blog.csdnimg.cn/dfedc196caf24280966867c83d65d441.gif#pic_center" alt="在这里插入图片描述">

说明：预制体弹出框中的预制体item，给予item预制体的文本绑定点击事件，点击后即可传递数据到父级home脚本中进行更新。

## 二、制作父级预制体及子预制体

### 步骤一、创建空节点，如下图

<img src="https://img-blog.csdnimg.cn/9a4e9700ead94cbda1368a83b6c5fcf0.png" alt="在这里插入图片描述">

### 步骤二、创建名为“popup_list” 的节点及背景图如下图。

<img src="https://img-blog.csdnimg.cn/39233b169d98420bae2ca7de2244d056.png" alt="在这里插入图片描述"> 注意：点击修改所有的信息如图红框内所示。

### 步骤三、创建滚动窗

<img src="https://img-blog.csdnimg.cn/d367b68a16cc4e1f9c099b11e43547a7.png" alt="在这里插入图片描述"> 创建后，名称改为ScrollView： <img src="https://img-blog.csdnimg.cn/f3d220684c4a4e30ab3ff0086a88ab44.png" alt="在这里插入图片描述">

### 步骤四、将item设置为预制体

注意：记得解锁左侧的红色小锁，点击一下就可以。 <img src="https://img-blog.csdnimg.cn/c83ff847ef964e46bc192fce1beb2c88.png" alt="在这里插入图片描述"> 设置完毕： <img src="https://img-blog.csdnimg.cn/a745ba2d98794c6a89ecffe8a9af8bd5.png" alt="在这里插入图片描述"> 创建对应的预制体脚本，如下图，item.ts： <img src="https://img-blog.csdnimg.cn/7e805919be864596bc74b554a0dcba53.png" alt="在这里插入图片描述">

### 步骤五、创建home场景，及home脚本并将上述的弹出界面存到里面

<img src="https://img-blog.csdnimg.cn/5f2b6806d0504bb7928e084be5d9c989.png" alt="在这里插入图片描述"> 说明：点击保存即可进行配置，优先创建空的home，然后保存到home的fire界面。

创建home脚本，并声明预制体及父节点信息，如下内容： home.ts

```
import item from "./prefab/item";

const {<!-- -->ccclass, property} = cc._decorator;

@ccclass
export default class home extends cc.Component {<!-- -->

    @property({<!-- -->
        type: cc.Node,
        displayName: "预制体父节点"
    })
    protected prefabFatherNode: cc.Node = null;

    @property({<!-- -->
        type: cc.Prefab,
        displayName: "item预制体"
    })
    protected itemPrefab: cc.Prefab = null;
 
    protected preData: Array&lt;{<!-- --> title: string,id:number,bg_color:string}&gt; = [];
 
    onLoad() {<!-- -->
        this.node.on('up_list', this.onListUpdate, this);
        this.echoList();
    }
    
    //监听更新
    protected onListUpdate(data: any): void {<!-- -->
        console.log('父节点回收到的数据:', data.detail);
        this.echoList(data.detail.id);
    }

    //输出列表
    echoList(theId=0){<!-- -->
        let that = this;
        let temporaryData = null;
        let num = 0;
        for (let i = 0; i &lt; 60; i++) {<!-- -->
            temporaryData = {<!-- -->
                title: "",
                id: 0,
                bg_color: "#000000",
            };
            const id = ++num;
            temporaryData.title = `${<!-- -->id}`;
            temporaryData.id = id;
            that.preData.push(temporaryData);
        }
        console.log(that.preData);
        if (theId !== 0) {<!-- -->
            // 更新预制体
            let prefabChildren = that.prefabFatherNode.children;
            for (let i = 0; i &lt; prefabChildren.length; i++) {<!-- -->
                let prefabChild = prefabChildren[i];
                let itemComponent = prefabChild.getComponent(item);
                //that.preData 会记录上一次的修改，所以要进行颜色的还原
                that.preData[i].bg_color = "#000000";
                if (itemComponent &amp;&amp; itemComponent.getData().id === theId) {<!-- -->
                    that.preData[i].bg_color = "#C0331F";
                }
                itemComponent.updatePre(that.preData[i]);
            }
        } else {<!-- -->
            // 创建新的预制体
            let length = that.preData.length;
            for (let i = 0; i &lt; length; i++) {<!-- -->
                let prefabricatedObject = cc.instantiate(that.itemPrefab);
                prefabricatedObject.parent = that.prefabFatherNode;
                prefabricatedObject.getComponent(item).createdPre(that.preData[i]);
            }
        }
    }
    // update (dt) {<!-- -->}
}


```

配置content属性：

<img src="https://img-blog.csdnimg.cn/1e38e3cd1246423a80ee312393e85e93.png" alt="在这里插入图片描述"> 给home.ts绑定脚本： <img src="https://img-blog.csdnimg.cn/8d775ef351cc455b8c5b2be76621c210.png" alt="在这里插入图片描述"> 拖拽关联预制体和父节点： <img src="https://img-blog.csdnimg.cn/8dc00634bdf145b0b743489188ecda1e.png" alt="在这里插入图片描述">

### 步骤六、创建预制体并绑定脚本

点击打开预制体： <img src="https://img-blog.csdnimg.cn/8fb6cbdcf1d944c298d6f273ce390cd4.png" alt="在这里插入图片描述"> 点选预制体场景信息后，在左侧进行用户脚本的关联如下图： <img src="https://img-blog.csdnimg.cn/43dc2cda6c2942d9b8efeacfed04955d.png" alt="在这里插入图片描述"> 说明：选择item。

配置item.ts的脚本内容：

```
const {<!-- -->ccclass, property} = cc._decorator;

@ccclass
export default class item extends cc.Component {<!-- -->

    @property(cc.Label)
    label: cc.Label = null;

    private data: any = null; // 保存预制体的数据

    //点击事件监听 回调到home脚本
    protected onClick(theId): void {<!-- -->
        console.log("点击测试");
        let newData = {<!-- -->'id':theId}; 
        let customEvent = new cc.Event.EventCustom('up_list', true);
        customEvent.detail = newData;//自定义的数据调用处
        this.node.dispatchEvent(customEvent);//亲测有效的方式，使用this.node.parent.emit("xxxx",{<!-- -->[]});没有反应
    }

    /**
     * 初始化
     * @param data 
     */
    createdPre(data: {<!-- --> title: string,id:number,bg_color:string }) {<!-- -->
        let that = this;
        that.data =data;
        console.log(data);
        that.label.string = "我是第："+data.title+"个，预制体。";
        that.label.node.color = new cc.Color().fromHEX(data.bg_color);
        //给label 注册事件监听
        that.node.on(cc.Node.EventType.TOUCH_END,function(){<!-- -->
            const theId = data.id;//获取当前的id并返回，用于更新数据
            that.onClick(theId);
        })
    }

    //更新预制体
    updatePre(data: any) {<!-- -->
        this.data = data;
        this.label.string =  "我是第："+data.title+"个，预制体。";
        this.label.node.color = new cc.Color().fromHEX(data.bg_color);
    }

    //返回当前预制体的数据
    getData(): any {<!-- -->
        return this.data;
    }

}

```

关联对象信息，拖拽到指定的框即可： <img src="https://img-blog.csdnimg.cn/4cd0b0e8a2fc40c0b520a657f8a03da6.png" alt="在这里插入图片描述"> end：大功告成，运行进行测试。
