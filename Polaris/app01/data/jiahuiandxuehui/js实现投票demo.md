
--- 
title:  js实现投票demo 
tags: []
categories: [] 

---


#### 目录标题
- - - - <ul><li><ul><li>- - 


## 演示

<img src="https://img-blog.csdnimg.cn/e2d07d7ddfd34b1981061eadbd936ac2.gif" alt="请添加图片描述">

## 说明

今天没有什么好的内容分享，跟大家讲一个标签吧增长姿势。

`line-height CSS` 属性用于设置多行元素的空间量，如多行文本的间距。 <img src="https://img-blog.csdnimg.cn/ac0a010376d6410da3920096e7b5fda3.png" alt="在这里插入图片描述">

>  
 根据浏览器的解析不同，line-height的表现方式有两种 
 1.基线之间的距离为line-height 
 2.lineHeight 为，font-size的上下加上半行距 


它的取值为：

>  
 1·normal： 默认。设置合理的行间距。取决于用户端。桌面浏览器（包括Firefox）使用默认值，约为1.2，这取决于元素的 
 2·font-family。 number： 设置数字，此数字会与当前的字体尺寸相乘来设置行间距，即number为当前font-size的倍数。 
 3·length ：设置固定的行间距。 
 4· % ：基于当前字体尺寸的百分比行间距。 
 5· inherit： 规定应该从父元素继承 line-height属性的值。 


## 源码

#### body设置

```
&lt;h2&gt;投票公布&lt;/h2&gt;
	&lt;div id="div1"&gt;
		&lt;div class="a_1"&gt;50%&lt;/div&gt;
		&lt;div class="a_2"&gt;50%&lt;/div&gt;
	&lt;/div&gt;
	&lt;!-- 红队投票 --&gt;
	&lt;div id="div2"&gt;
		&lt;div &gt;
			&lt;img src="img/1.jpg" height="100%" width="100%" /&gt;
		&lt;/div&gt;
		&lt;div class="diaphane" id="result_1"&gt;
			&lt;p&gt;红队投票数：0&lt;/p&gt;
		&lt;/div&gt;
		&lt;input type="button" name="aa" value="投红队" /&gt;
	&lt;/div&gt;
	&lt;!-- 蓝队投票 --&gt;
	&lt;div id="div3"&gt;
		&lt;div&gt;
			&lt;img src="img/2.jpg" height="100%" width="100%" /&gt;
		&lt;/div&gt;
		&lt;div class="diaphane" id="result_2"&gt;

			&lt;p&gt;蓝队投票数：0&lt;/p&gt;
		&lt;/div&gt;
		&lt;input type="button" name="aa" value="投蓝队" /&gt;
	&lt;/div&gt;

```

#### js实现投票的动画

```
window.onload = function () {<!-- -->
	//获取div1及下面的div
	var oDiv = document.getElementById('div1');
	var aDiv = oDiv.getElementsByTagName('div');
	//获取点击按钮
	var aBtn = document.getElementsByTagName('input');
	//初始化百分比数字
	var lNum = 50;
	var rNum = 50;
	//计算进度条宽度
	var lNums = (rNum / (lNum + rNum)) * 520;
	var rNums = 520 - lNums;
	//设置进度条width宽度
	aDiv[1].style.width = parseInt(lNums) + 'px';
	aDiv[0].style.width = 520 - parseInt(lNums) + 'px';
	//设置进度条百分比数字
	aDiv[0].innerHTML = sub((lNum / (lNum + rNum)) * 100 + "") + "%";
	aDiv[1].innerHTML = sub((1 - lNum / (lNum + rNum)) * 100 + "") + "%";
	//初始化投票数
	var leftNum = 0;
	var rightNum = 0;
	//绑定红队投票按钮点击事件
	aBtn[0].onclick = function () {<!-- -->
		//每次点击累加投票数
		lNum = lNum + (++leftNum);
		//计算div对应长度
		var lNumss = parseInt(leftNum / (leftNum + rightNum) * 520);
		//设置进度条width宽度
		aDiv[0].style.width = lNumss + 'px';
		aDiv[1].style.width = (520 - lNumss) + 'px';
		//计算div百分比数字
		aDiv[0].innerHTML = sub((leftNum / (leftNum + rightNum)) * 100 + "") + "%";
		aDiv[1].innerHTML = sub((1 - leftNum / (leftNum + rightNum)) * 100 + "") + "%";
		//设置投票数
		document.getElementById("result_1").innerHTML = "红队投票数：" + leftNum;
	}
	//绑定蓝队投票按钮点击事件
	aBtn[1].onclick = function () {<!-- -->
		//每次点击累加投票数
		rNum = rNum + (++rightNum);
		//计算div对应长度
		var rNumss = parseInt(rightNum / (leftNum + rightNum) * 520);
		//设置进度条width宽度
		aDiv[0].style.width = (520 - rNumss) + 'px';
		aDiv[1].style.width = rNumss + 'px';
		//计算div百分比数字
		aDiv[0].innerHTML = sub((leftNum / (leftNum + rightNum)) * 100 + "") + "%";
		aDiv[1].innerHTML = sub((1 - leftNum / (leftNum + rightNum)) * 100 + "") + "%";
		//设置投票数
		document.getElementById("result_2").innerText = "蓝队投票数：" + rightNum;
	}
	//保留小数点后两位
	function sub(str) {<!-- -->
		var index = str.lastIndexOf(".");
		if (index == -1) {<!-- -->
			return str;
		}
		return str.substring(0, index + 3);
	}
}

```

#### css设定

```
* {<!-- -->
	margin: 0;
	padding: 0;
	list-style-type:none;
}
a,img{<!-- -->border:0;}

.vote{<!-- -->
	width:530px;
	margin:100px auto;
}

.vote h2{<!-- -->
	height:24px;
	line-height:24px;
	font-size:18px;
	font-weight:400;
	margin-bottom:20px;
	text-align:center;
}

#div1 {<!-- -->
	width: 520px;
	height: 30px;
	position: relative;
}

#div2 {<!-- -->
	margin:30px 20px 0 0;
	width: 250px;
	height: 325px;
	float: left;
	display:inline;
	position: relative;
}

#div3 {<!-- -->
	margin-top: 30px;
	margin-left: 2px;
	width: 250px;
	height: 325px;
	float: left;
}

.a_1,
.a_2 {<!-- -->
	position: absolute;
	top: 0;
	color:#fff;
	text-align:center;
	height:30px;
	line-height:30px;
}

.a_1 {<!-- -->
	left: 0;
	background:#3366cc;
}

.a_2 {<!-- -->
	right: 0;
	background:#ff6600;
}

.vote input {<!-- -->
	padding-top: 20px;
	width: 250px;
	position: absolute;
	color: #fff;
	border-radius: 1rem;
	text-decoration: none;
	padding: 1rem 2rem;
	margin-bottom: 1rem;
	min-width: 10rem;
	text-align: center;
	background-color: #6a4;
	border:0;
	cursor:pointer;
}

.diaphane {<!-- -->
	color: #000;
	margin:10px 0;
	text-align:center;
}


```

## <font color="red" size="6">点击直接资料领取</font>

**如果你在学习python或者Java哪怕是C遇到问题都可以来给我留言，因为在学习初期新手总会走很多弯路，这个时候如果没有有个人来帮一把的话很容易就放弃了。身边很多这样的例子许多人学着学着就转了专业换了方向，不仅是自身问题还是没有正确的学习。所以作为一个过来人我希望有问题给我留言，说不上是帮助就是顺手敲几行字的事情。**

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
