
--- 
title:  实现简单的三D立方体自动旋转 
tags: []
categories: [] 

---


#### 目录标题
- - - - <ul><li><ul><li>- 


## 演示

<img src="https://img-blog.csdnimg.cn/img_convert/822ef18551cdaf829832802a6d5b0621.gif#pic_center" alt="在这里插入图片描述">

## 技术栈

display:inline-block，block，inline元素的区别:

>  
 display：block将元素显示为块级元素，从而可以更好地操控元素的宽高，以及内外边距，每一个块级元素都是从新的一行开始。 


>  
 display : inline将元素显示为行内元素，高度，行高以及底边距不可改变，高度就是内容文字或者图片的宽度，不可以改变。多个相邻的行内元素排在同一行里，知道页面一行排列不下，才会换新的一行。 


>  
 display：inline-block看上去值名inline-block是一个混合产物，实际上确是如此，将元素显示为行内块状元素，设置该属性后，其他的行内块级元素会排列在同一行。比如我们li元素一个inline-block，使其既有block的宽度高度特性，又有inline的同行特性，在同一行内有不同高度内容的元素时，通常要设置对齐方式如vertical-align:top;来使元素顶部对齐。 


行内标签：不能设置宽度 高度 padding margin，标签不能自动伸展。可以通过display灵活的将标签在行内和行间随意转换；display：inline;转换成行内标签display：block;转换成块级标签。

`opacity 属性设置或返回元素的不透明度。`

>  
 元素的不透明度级别描述了透明度级别，当不透明度为 1 时表示完全不透明，当不透明度为 0.5 时表示半透明，当不透明度为 0 时表示完全透明。 


## 源码

#### css

```
* {<!-- -->
    margin: 0;
    padding: 0;
}
html, body {<!-- -->
    width: 100%;
    height: 100%;
    overflow: hidden;
}
canvas {<!-- -->
    display: block;
    position: absolute;
    z-index: -2;
}

.snowback{<!-- -->
    height: 100%;
    width: 100%;
    overflow: hidden;
    position: absolute;
    z-index: 1;
}
.ziti{<!-- -->
    height: 50px;
    width: 100%;
    font-size: 60px;
    text-align: center;
    position: absolute;
    margin-top: 100px;
    z-index: 11;
}
.ziti span {<!-- -->
    height: 30px;
    width: 100%;
    font-size: 25px;
    font-family: "å¾®è½¯é›…é»‘";
    text-align: center;
    line-height: 30px;
     /*å…³é”®ä»£ç */
    background-image: -webkit-linear-gradient(left, rgb(20, 26, 150), #E6D205 25%, rgb(196, 30, 30) 50%, rgb(41, 197, 111) 75%, rgb(175, 23, 221));
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
    -webkit-background-size: 200% 100%;
    animation: masked-animation 4s infinite linear;
}

/*å…³é”®ä»£ç */
@keyframes masked-animation {<!-- -->
    0% {<!-- -->
        background-position: 0 0;
    }
    100% {<!-- -->
        background-position: -100% 0;
    }
}
.main{<!-- -->
    width: 200px;
    height: 200px;
    top:calc(calc(50% - 100px));
    margin-left: calc(50% - 100px);
    position: absolute;
}
.box {<!-- -->
    width: 200px;
    height: 200px;
    opacity: 1;
    position: absolute;
    transform: scale(0.8);
}
.box-biger:hover+.box{<!-- -->
    transform: scale(0.8);
}
.box-biger{<!-- -->
    width: 200px;
    height: 200px;
    opacity: 0;
    transition: all 1s;
    position: absolute;
    z-index: 10;
}
.box-biger:hover{<!-- -->
    width: 600px;
    height: 600px;
    opacity: 1;
    margin-top: calc(50% - 300px);
    margin-left: calc(50% - 300px);
}
.box ul {<!-- -->
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    background-color: transparent;
    list-style: none;
    position: absolute;
    transition: all 1s;
    transform-origin: 50% 50% 0;
}
.box-biger ul{<!-- -->
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    background-color: transparent;
    list-style: none;
    position: absolute;
    transition: all 1s;
}
.small {<!-- -->
    font-size: 60px;
    text-align: center;
    display: inline-block;
    width: 100%;
    height: 100%;
    position: absolute;
    box-sizing: border-box;
}
.biger {<!-- -->
    font-size: 60px;
    text-align: center;
    display: inline-block;
    width: 100%;
    height: 100%;
    position: absolute;
    box-sizing: border-box;
}
.small img{<!-- -->
    height: 100%;
    width: 100%;
    opacity: 1;
}
.biger img{<!-- -->
    height: 70%;
    width: 70%;
    margin-top: 15%;
    margin-left: 15%;
    opacity: 0.3;
}
.idv1 {<!-- -->
    background-size: cover;
    left: 0;
    top: 100%;
    transform: translateZ(-100px)  rotateY(180deg)  rotate(180deg);
    transform-origin: top;
}

.idv2 {<!-- -->
    background-size: cover;
    top: 0;
    margin-left: 50%;
    transform: rotateY(90deg);
}

.idv3 {<!-- -->
    background-size: cover;
    left: 0;
    top: 0;
    margin-left: -50%;
    transform: rotateY(90deg);
}

.idv4 {<!-- -->
    transform: rotateX(90deg);
    top: -50%;
}

.idv5 {<!-- -->
    transform: rotateX(270deg);
    top: 50%;
}

.idv6 {<!-- -->
    background-size: cover;
    left: 0;
    top: 0;
    transform: translateZ(100px);
}

.idv7 {<!-- -->
    background-size: cover;
    left: 0;
    top: 100%;
    transform: translateZ(-100px)  rotateY(180deg)  rotate(180deg);
    transform-origin: top;
    transition: all 1s;
}

.idv12 {<!-- -->
    background-size: cover;
    left: 0;
    top: 0;
    transform: translateZ(100px);
    transition: all 1s;
}

.box-biger:hover&gt;ul&gt;.idv7{<!-- -->
    transform: translateZ(-300px)  rotateY(180deg)  rotate(180deg);
}
.box-biger:hover&gt;ul&gt;.idv12{<!-- -->
    transform: translateZ(300px);
}

.btn {<!-- -->
    height: 60px;
    text-align: center;
    line-height: 60px;
    width: 90px;
    margin-left: 20px;
    float: left;
    box-sizing: border-box;
    position: absolute;
    border-radius: 30px;
    z-index: 30;
}
.btn img{<!-- -->
    height: 100%;
    width: 100%;
}
.btn:hover {<!-- -->
    cursor: pointer;
}
.inpbtn {<!-- -->
    height: 40px;
    float: right;
    line-height: 40px;
    margin-left: 200px;
    background-color: pink;
    color: white;
    border-radius: 30px;
}


input {<!-- -->
    height: 40px;
    width: 180px;
    float: left;
    border-radius: 20px;
    font-size: 15px;
}

audio {<!-- -->
    height: 40px;
    width: 350px;
    margin-left: -40px;
    margin-top: -1px;
}

.audiobox {<!-- -->
    height: 40px;
    width: 300px;
    border-radius: 20px;
    overflow: hidden;
}
.btnonlond:hover&gt;.hiddenbox{<!-- -->
    visibility: inherit;
}
.hiddenbox {<!-- -->
    margin-top: -60px;
    margin-left: 100px;
    height: 80px;
    width: 300px;
    transition: all 2s;
    visibility: hidden;
    position: absolute;
    z-index: 30;
}

```

#### js

```
// Customize these...
var n = 300,
    speed = 5,//速度定义
    startSize = rand(100,300);//大小定义

// ...not these
var c = document.getElementById("c"),
    ctx = c.getContext("2d"),
    cw = (c.width = window.innerWidth),
    ch = (c.height = window.innerHeight),
    mousePos = {<!-- -->x:"", y:""},
    img = new Image(),
    particles = [],
    particleNumber = 0,
    Particle = function(index) {<!-- -->
      this.index = index;
      this.dur = (100-rand(9, 90))/speed;
      this.draw = function() {<!-- -->
        ctx.translate( this.x, this.y );
        ctx.globalAlpha = this.alpha;
        ctx.globalCompositeOperation = 'lighter';
        // if (index%1.5==0) ctx.globalCompositeOperation = 'overlay';
        if (index%2==0) ctx.globalCompositeOperation = 'xor';
        ctx.drawImage(img, -this.size/2, -this.size/2, this.size, this.size);
        ctx.translate( -this.x, -this.y );
      }
    };

function setParticle(p, firstRun) {<!-- -->
  var _x = cw*rand(0,1), _y = ch*rand(0,1), _s = startSize;
  if (rand(0,1)&gt;0.3 &amp;&amp; mousePos.x!=""){<!-- --> //console.log(mousePos)
    _x = mousePos.x;
    _y = mousePos.y;
    _s = _s/10;
  }
  var _tl = new TimelineMax()
            .fromTo(p, p.dur, {<!-- -->
                x:_x,
                y:_y,
                size:_s,
                alpha:0
            },{<!-- -->
                size:'+='+String(rand(200,400)),
                bezier:[{<!-- -->alpha:rand(0.15,0.65)},{<!-- -->alpha:0}],
                ease:Power1.easeOut,//ease:Power0.easeNone,
                onComplete:function(){<!-- --> setParticle(p); }
            });

  if (firstRun) _tl.seek(p.dur*rand()); //fast-forward on first run
}


TweenMax.ticker.addEventListener("tick", function(){<!-- -->
  ctx.clearRect(0, 0, cw, ch);
  for (var i=0; i&lt;n; i++) particles[i].draw();
});


window.addEventListener('resize', doResize)
function doResize() {<!-- -->
  particleNumber = 0;  
  cw = (c.width = window.innerWidth);
  ch = (c.height = window.innerHeight);
  for (var i=0; i&lt;n; i++) {<!-- -->
    TweenMax.killTweensOf(particles[i]);
    setParticle(particles[i], true);
  }
  TweenMax.fromTo(c, 0.3, {<!-- -->alpha:0},{<!-- -->alpha:1, ease:Power3.easeInOut});
}

// First run
for (var i=0; i&lt;n; i++) particles.push(new Particle(i));
doResize();


function rand(min, max) {<!-- -->
  (min) ? min=min : min=0;
  (max) ? max=max : max=1;
  return min + (max-min)*Math.random();
}







```

## <font color="red" size="6">点击直接资料领取</font>

**如果你在学习python或者Java哪怕是C遇到问题都可以来给我留言，因为在学习初期新手总会走很多弯路，这个时候如果没有有个人来帮一把的话很容易就放弃了。身边很多这样的例子许多人学着学着就转了专业换了方向，不仅是自身问题还是没有正确的学习。所以作为一个过来人我希望有问题给我留言，说不上是帮助就是顺手敲几行字的事情。**

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
