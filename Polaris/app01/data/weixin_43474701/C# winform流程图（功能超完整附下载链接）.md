
--- 
title:  C# winform流程图（功能超完整附下载链接） 
tags: []
categories: [] 

---
### C# winform流程图（功能超完整）工具箱，文件存储打开，画布放大缩小，图元操作，操作步骤（可撤销），图元属性调节



1、工具箱创建图元（矩形，菱形，圆，直线，曲线，其他图形可以自行仿照开发） 2、图元有六个操纵柄，四个连接点（一定范围可自动与连接线连接），两个伸缩，可以编辑内部文字 3、直线有箭头，有直线和曲线两种，移动图形，已经连接的直线跟着移动 4、带操作记录，可以回溯步骤撤销 5、有属性窗口，可以条件属性（背景图，填充，文字等等） <img src="https://img-blog.csdnimg.cn/275a114cb439459490bcdebac700fac0.png" alt="请添加图片描述">

部分代码 void LinePointMoved(BaseBoxComponent cmp) {<!-- --> foreach (FlowChartPoint edgePoint in cmp.EdgePoints) {<!-- --> float d = GraphicsUtil.Distance(edgePoint, linePoint); cmp.IsSelected = (d &lt; cmp.View.ViewFactory.EdgeBoxWidth * 5); if (d &lt; cmp.View.ViewFactory.EdgeBoxWidth * 2) {<!-- --> linePoint.X = edgePoint.X; linePoint.Y = edgePoint.Y; if (lineCmp.StartPoint == linePoint) {<!-- --> lineCmp.ConnectionStart = cmp; lineCmp.ConnectionStartPointIndex = cmp.EdgePoints.IndexOf(edgePoint); } else if (lineCmp.EndPoint == linePoint) {<!-- --> lineCmp.ConnectionEnd = cmp; lineCmp.ConnectionEndPointIndex = cmp.EdgePoints.IndexOf(edgePoint); } return; } } } 
