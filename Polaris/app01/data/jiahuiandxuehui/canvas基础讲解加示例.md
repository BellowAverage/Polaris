
--- 
title:  canvas基础讲解加示例 
tags: []
categories: [] 

---


#### 目录标题
- - <ul><li><ul><li>- - 


## 技术栈

之前其实有介绍过，只是没有给示例我们再来说说他。

>  
 canvas元素是HTML5中新出现的，我们可以将其当做一个像素级的画布，它 
 允许我们绘制直线、圆、矩形等基本形状，以及图像和文字。使用canvas元素， 可以实时渲染图形、游戏动画或其他虚拟图像，而且它已经为快速绘图做过优化了。各大主流浏览器都已经支持GPU加速的2Dcanvas渲染，因此，使用canvas绘制出的游戏动画运行速度会很快。 


它内部封装的函数：

```
rect( x, y, width, height )   绘制矩形

fillRect( x, y, width, height )  绘制被填充的矩形

strokeRect( x, y, width, height )  绘制矩形（无填充）

clearRect( x, y, width, height ) 清除指定的矩形内的像素



fill()  填充当前绘图（路径）

stroke() 绘制已定义的路径

beginPath()  起始（重置）当前路径

moveTo( x, y )  将笔触移动到指定的坐标(x,y)

lineTo( x, y )  绘制一条从当前位置到指定的坐标(x,y)的直线

clip()  从原始画布剪切任意形状和尺寸的区域

quadraticCurveTo()  创建二次贝塞尔曲线

bezierCurveTo()   创建三次贝塞尔曲线

arc( x, y, radius, startAngle, endAngle, anticlockwise)  绘制圆或圆弧

arcTo( x1, y1, x2, y2, radius)  根据给定点画圆弧，再以直线连接两个点

isPointInPath( x, y )  检测指定的点是否在当前路径中，在则返回true。



fillStyle  设置或返回用于填充绘画的颜色、渐变或模式

strokeStyle  设置或返回用于笔触的颜色、渐变或模式

shadowColor  设置或返回用于阴影的颜色

shadowBlur   设置或返回用于阴影的模糊级别

shadowOffsetX  设置或返回阴影与形状的水平距离

shadowOffsetY  设置或返回阴影与形状的垂直距离



lineCap  设置或返回线条的结束点样式（butt、round、square）

lineJoin  设置或返回当两条线交汇时，边角的类型（bevel、round、miter）

lineWidth  设置或返回当前的线条宽度

miterLimit  设置或返回最大斜接长度



createLinearGradient( x0, y0, x1, y1 )  创建线性渐变

createPattern( image/canvas/video, repeat )  在指定的方向内重复绘制指定的元素

createRadialGradient( x0, y0, r0, x1, y1, r1 ) 创建径向渐变

addColorStop( stop, color )  规定渐变对象中的颜色和停止位置



font  设置或返回文本内容的当前字体属性（和css的font一样）

textAlign  设置或返回文本内容的当前对齐方式

textBaseline  设置或返回在绘制文本时使用的当前文本基线

fillText( text, x, y )  在画布上绘制“被填充”的文本

strokeText( text, x, y )  在画布上绘制文本（无填充）

measureText( text )  返回包含指定文本宽度的对象（属性width获取宽度）



drawImage( image/canvas, x, y )、drawImage( image/canvas, x, y, width, height )、drawImage( image/canvas, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight )  在画布上绘制图像、画布或视频



createImageData( width, height )、createImageData(imageData)  绘制ImageData对象

getImageData( x, y, width, height )  返回ImageData对象，该对象为画布上指定的矩形复制像素数据。

putImageData( ImageData, x, y )、putImageData( imageData, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight )  把图像数据放回画布上。

width  返回ImageData对象的宽度

height  返回ImageData对象的高度

data  返回一个对象，包含指定的ImageData对象的图像数据



globalAlpha  设置或返回绘图的当前alpha或透明度

globalCompositeOperation  设置或返回新图像如何绘制到已有的图像上。



scale( x, y )  缩放当前绘图

translate( x, y )  重新设置画布上的(0,0)位置

rotate( angle )  选择当前绘图，单位为“弧度”，角度转弧度公式（ degrees*Math.PI/180）

transform( m11, m12, m21, m22, dx, dy )  替换绘图的当前转换矩阵

setTransform()  将当前转换重置为单元矩阵，然后运行transform()



save()  保存当前环境的状态

restore()  恢复之前保存过的路径状态和属性



getContext('2d')  获取2d对象

toDataURL()  将canvas转换成图片，返回地址



```

#### 样例介绍1

<img src="https://img-blog.csdnimg.cn/f6db9625f995448f938d9c97a0fe76a2.png" alt="在这里插入图片描述">

```
  &lt;canvas width="500px" height="300px" id="canvas"&gt;&lt;/canvas&gt;
	&lt;script&gt;
		//	1. 获取canvas元素对象
		var canvas=document.getElementById("canvas");
//			2. 通过元素对象创建画布对象
		var context=canvas.getContext("2d");
		console.log(context);
		/*
			3. 使用context画布对象的API 来绘制图形
			绘制矩形：
				fillRect(x,y,width,height) - 绘制实心矩形
					x,y表示绘制图形的起始坐标值 - 相对于画布的左上点
					width - 表示绘制矩形的宽度
					height- 表示绘制矩形的高度
				strokeRect(x,y,width,height) - 绘制空心矩形
					x,y表示绘制图形的起始坐标值 - 相对于画布的左上点
					width - 表示绘制矩形的宽度
					height- 表示绘制矩形的高度
		*/
		context.fillRect(10,10,100,100);
		context.strokeRect(120,10,100,100);
	&lt;/script&gt;

```

#### 样例2

<img src="https://img-blog.csdnimg.cn/a26ff15ed6634bfe9cac58cc5a8f6487.png" alt="在这里插入图片描述">

```
&lt;canvas width="500" height="300" id="canvas"&gt;&lt;/canvas&gt;
	
&lt;script&gt;
    var canvas=document.getElementById("canvas");
	var context=canvas.getContext("2d");
	/*
		fillStyle - 设置实心图形样式
			单词
			#XXX
			rgb(r,g,b)
		strokeStyle - 设置空心图形样式
		注意：设置样式一定要在绘制图形之前
	*/
	context.fillStyle="blue";
	context.fillRect(10,10,100,100);
	context.strokeStyle="red";
	context.strokeRect(120,10,100,100);
&lt;/script&gt;

```

#### 样例3

<img src="https://img-blog.csdnimg.cn/f7d9a2b9612b493c947b20ed86a2e25a.gif" alt="请添加图片描述">

```
&lt;script&gt;
    var canvas=document.getElementById("canvas");
	var context=canvas.getContext("2d");
	var n;
//	第一行的矩形绘制
	/*for(var i=0;i&lt;8;i+=2){
		context.fillRect(100*i,100*0,100,100);
	}
//  第二行的矩形绘制
	for(var i=0;i&lt;8;i+=2){
		context.fillRect(100*(i+1),100*1,100,100);
	}
//	第三行的矩形绘制
	for(var i=0;i&lt;8;i+=2){
		context.fillRect(100*i,100*2,100,100);
	}
//	第四行的矩形绘制
	for(var i=0;i&lt;8;i+=2){
		context.fillRect(100*(i+1),100*3,100,100);
	}*/
	
	setInterval(function(){<!-- -->
		for(var j=0;j&lt;8;j++){<!-- -->	
			for(var i=0;i&lt;8;i+=2){<!-- -->
				j%2==0?n=i:n=i+1;// 如果j%2==0表示是奇数行
				context.fillStyle=rgb();
				context.fillRect(100*n,100*j,100,100);
			}
		}
	},200);
	function rgb(){<!-- -->
		var r=Math.floor(Math.random()*256);
		var g=Math.floor(Math.random()*256);
		var b=Math.floor(Math.random()*256);
		return "rgb("+r+","+g+","+b+")";
	}
&lt;/script&gt;

```

## <font color="red" size="6">点击直接资料领取</font>

**如果你在学习python或者Java哪怕是C遇到问题都可以来给我留言，因为在学习初期新手总会走很多弯路，这个时候如果没有有个人来帮一把的话很容易就放弃了。身边很多这样的例子许多人学着学着就转了专业换了方向，不仅是自身问题还是没有正确的学习。所以作为一个过来人我希望有问题给我留言，说不上是帮助就是顺手敲几行字的事情。**

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
