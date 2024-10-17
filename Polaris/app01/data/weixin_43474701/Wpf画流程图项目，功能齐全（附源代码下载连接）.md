
--- 
title:  Wpf画流程图项目，功能齐全（附源代码下载连接） 
tags: []
categories: [] 

---
### Wpf 画流程图项目

1、通过鼠标拖拽左边的工具到画布 2、点击图形里面可以输入参数 3、点击图形节点拖拽可以连接其他图形节点 4、可以撤销步骤 5、可以保存文件 6、可以运行流程（开始、暂停、结束），底部有运行输出 7、代码注释详细，模块层次清晰 详细情况如下图所示



<img src="https://img-blog.csdnimg.cn/91a5a66568754a19a4f4873f25396290.png" alt="请添加图片描述"> 部分代码 public class AddLinkAction : Action {<!-- --> public SlotInfo SlotInfo { get; private set; } public NodeInfo NodeInfo { get; private set; } public AddLinkAction(SlotInfo slotInfo, NodeInfo nodeInfo) {<!-- --> SlotInfo = slotInfo; NodeInfo = nodeInfo; } public override void Do() {<!-- --> SlotInfo.Slot.Nodes.Add(NodeInfo.Node); NodeInfo.FlowInfo.Update(); } public override void Undo() {<!-- --> SlotInfo.Slot.Nodes.Remove(NodeInfo.Node); NodeInfo.FlowInfo.Update(); } } 
