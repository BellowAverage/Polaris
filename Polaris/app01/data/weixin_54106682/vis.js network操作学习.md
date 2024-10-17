
--- 
title:  vis.js network操作学习 
tags: []
categories: [] 

---
### 前言

网络是显示网络以及由节点和边组成的网络的可视化。可视化易于使用，并支持自定义形状、样式、颜色、尺寸、图像等。网络可视化可以在任何现代浏览器上顺利运行，最多可显示数千个节点和边缘。为了处理大量节点，网络提供了集群支持。Network 使用 HTML 画布进行渲染。

### 一、简单的例子

①引入 vis-network.js 和 vis-network.css 文件，您可以从 链接它们 或从 要求/导入 。

②指定节点和边，还可以使用 vis.DataSets 进行动态数据绑定，例如，在初始化网络后更改颜色、标签或任何选项。

③获得数据后，需要一个容器 div 来告诉 vis 将网络放置在哪里。

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
    &lt;style&gt;
        html,
        body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
        }

        #mynetwork {
            position: relative;
            width: 100%;
            height: 100%;
            /* border: 1px solid lightgray; */
        }
    &lt;/style&gt;
&lt;/head&gt;

&lt;body&gt;
    &lt;div id="mynetwork"&gt;&lt;/div&gt;
&lt;/body&gt;

&lt;!-- 该示例中，script代码中需要获取DOM元素，因此要将script代码放在body之后 --&gt;
&lt;script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"&gt;&lt;/script&gt;

&lt;script type="text/javascript"&gt;
    // create an array with nodes
    var nodes = new vis.DataSet([
        { id: 1, label: "Node 1" },
        { id: 2, label: "Node 2" },
        { id: 3, label: "Node 3" },
        { id: 4, label: "Node 4" },
        { id: 5, label: "Node 5" }
    ]);

    // create an array with edges
    var edges = new vis.DataSet([
        { from: 1, to: 3 },
        { from: 1, to: 2 },
        { from: 2, to: 4 },
        { from: 2, to: 5 },
        { from: 3, to: 3 }
    ]);

    // create a network
    var container = document.getElementById("mynetwork");
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {};
    var network = new vis.Network(container, data, options);
&lt;/script&gt;

&lt;/html&gt;
```

### 二、模块学习

#### 1、configure

生成具有过滤功能的交互式选项编辑器。

```
var options = {
        configure: {
            // 配置界面开关 如果为false 即使设置了configure 界面上也不会有设置选项的面板
            enabled: true,
            // 节点和边的配置
            filter: 'nodes,edges, layout, interaction, manipulation, physics, selection, renderer',
            // 将配置面板放置在DOM元素中
            container:document.getElementById("configuration"),
            // 生成选项按钮在配置器的底部
            showButton: true
        }
    };
```

<img alt="" height="799" src="https://img-blog.csdnimg.cn/direct/bbdedc9e91af449f9d5b23830b9079d2.png" width="561">

<img alt="" height="372" src="https://img-blog.csdnimg.cn/direct/7564c9ee138e4c789cb553c9f1db2cb5.png" width="564">

#### 2、manipulation

提供 API 和可选 GUI 来更改网络中的数据。

```
var options = {
        manipulation: {
            // 操纵节点和边的选项按钮 有新增节点 新增边
            enabled: true,
            // true工具栏可见 false编辑按钮可见 点击后 工具栏可见
            initiallyActive: false,
            // 当您提供布尔值时，您只需切换操纵系统 GUI 上的“添加节点”按钮。缺少处理函数可能会影响使用这些方法时的 API。
            // addNode: true,
            addEdge: true,
            // 当提供函数时，当用户在“addNode”模式下单击画布时将调用该函数。该函数将接收两个变量：可以创建的节点的属性和回调函数。如果使用新节点的属性调用回调函数，则会添加该节点。
            addNode: function (nodeData, callback) {
                nodeData.label = 'hello world';
                callback(nodeData);
            },
            // 仅当处理函数被提供，编辑节点操作才可用
            editNode: undefined,
            editEdge: true,
            deleteNode: true,
            deleteEdge: true,
            // 节点模块提供的所有方法都是可用的
            controlNodeStyle: {
                shape: 'diamond',
                size: 6,
                color: {
                    background: '#3c3c3c',
                    border: '#3c3c3c',
                    highlight: {
                        background: '#3c3c3c',
                        border: '#3c3c3c'
                    }
                },
                borderWidth: 4,
                borderWidthSelected: 2
            }
        }
    };
```


