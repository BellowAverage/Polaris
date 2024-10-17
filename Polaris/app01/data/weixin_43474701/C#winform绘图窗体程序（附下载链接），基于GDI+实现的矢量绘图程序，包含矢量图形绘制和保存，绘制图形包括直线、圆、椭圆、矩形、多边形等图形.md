
--- 
title:  C#winform绘图窗体程序（附下载链接），基于GDI+实现的矢量绘图程序，包含矢量图形绘制和保存，绘制图形包括直线、圆、椭圆、矩形、多边形等图形 
tags: []
categories: [] 

---
**基于GDI+实现的矢量绘图程序，包含矢量图形绘制和保存，绘制图形包括直线、圆、椭圆、矩形、多边形等图形，支持插入图片和文字**

 详细情况如下所示： <img src="https://img-blog.csdnimg.cn/direct/5f265403c5964740bc5fe34e17476f53.png" alt="请添加图片描述"> 代码注释非常详细 <img src="https://img-blog.csdnimg.cn/direct/83b7e8431dfb4ee4a8e329aa62a1b25d.png" alt="在这里插入图片描述"> 部分代码展示： public struct LineStyle {<!-- --> public float Width;//线宽 public Color Color;//颜色 public DashStyle Style;//线型

```
        //创建构造函数，初始化各参数：颜色-黑色，线宽-1.0，线型-实线
        public LineStyle(Color color, float width = 1.0f, DashStyle style = DashStyle.Solid)
        {
            Width = width;
            Color = color;
            Style = style;
        }
        public LineStyle(float width, DashStyle style) : this(Color.Black, width, style)
        {
            //此处不用写代码，共享上面的构造函数内容
        }
    }

```


