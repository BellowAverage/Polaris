
--- 
title:  C# 流程图完整功能，矩形，菱形圆，三角形，直线，折线，放大，滚动条，保存等等功能（附下载链接） 
tags: []
categories: [] 

---
### C# 流程图完整功能，矩形，菱形圆，三角形，直线，折线，放大，滚动条，保存等等功能

 流程图具体功能如下： <img src="https://img-blog.csdnimg.cn/74096a36762e4f9ba8309a56a0643de5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5a0fa0e49de14dc381a81009cd1ae342.png" alt="在这里插入图片描述"> 连接时图形有线帽 <img src="https://img-blog.csdnimg.cn/7cca95c492cd4201af2364800c8bd43a.png" alt="在这里插入图片描述"> 部分动漫展示 public virtual void Draw() {<!-- --> Graphics gr = canvas.AntiAliasGraphics; if (Visible) {<!-- --> if (canvas.OnScreen(UpdateRectangle)) {<!-- --> Trace.WriteLine("Shape:Draw " + ToString()); Draw(gr); } // Draw text before anchors and CP’s, otherwise centered text will overlay // on top of any center anchor/CP. if (!String.IsNullOrEmpty(Text)) {<!-- --> DrawText(gr); } if (ShowAnchors) {<!-- --> DrawAnchors(gr); } if (ShowConnectionPoints) {<!-- --> DrawConnectionPoints(gr); } if (IsBookmarked) {<!-- --> DrawBookmark(gr); } } else {<!-- --> Hide(); } } 
