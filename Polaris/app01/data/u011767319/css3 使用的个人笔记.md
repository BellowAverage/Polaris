
--- 
title:  css3 使用的个人笔记 
tags: []
categories: [] 

---
### css3 做出顶边倾斜的 梯形 div

>  
 图片展示效果 


<img src="https://img-blog.csdnimg.cn/20201111173003306.png#pic_center" alt="在这里插入图片描述">

```
&lt;html&gt;
&lt;head&gt;
&lt;meta charset="utf-8"&gt; 
&lt;title&gt;顶边倾斜的div梯形&lt;/title&gt; 
&lt;style&gt; 
.box
{<!-- -->
    border-radius:0px;
    width:200px;
    height:100px;
    background-color:green;
    position:relative;
}
.content{<!-- -->
    margin-top:50px;
    width:200px;
    padding-top:50px;
    overflow:hidden;
    border-radius:0px;
}
.box::before
{<!-- -->
    position:absolute;
    top:0;
    left:0;
    content:"";
    z-index:-1;
    width:210px; /*如果需要圆角的话 不用比box的宽度长,如果不需要圆角需要增长*/
    height:100px;
    background-color:green;
    transform:rotate(-10deg);
    transform-origin:left top;
    border-radius:0px;
}
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="content"&gt;
&lt;div class="box"&gt;Hello&lt;/div&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```
