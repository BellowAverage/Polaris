
--- 
title:  11套烟花代码，多种方式实现的烟花代码，基于Html/jQuery/css实现的烟花代码合集，总有一款是你喜欢的 
tags: []
categories: [] 

---
基于HTML/CSS/Echarts的会议展览、业务监控、风险预警、数据分析展示等多种展示需求可视化集合 完整代码下载地址： 运行效果： <img src="https://img-blog.csdnimg.cn/7ee68555063640ef9be19bda6c52221c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3b60d243727a479888bf8056638aff39.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/dce997bfc7bd40d7a34820d4643d2e8e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/410be61e1b95468c871dba5454d37b1e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/376b39f83e40474db0bf87e4d6b24733.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8f566a217b114911815944c3517ddd01.png" alt="在这里插入图片描述"> index.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="ie=edge"&gt;
    &lt;title&gt;烟花合集&lt;/title&gt;
    &lt;style&gt;
        body {
            background: #000;
        }
        
        .header {
            width: 1000px;
            margin: 0 auto;
        }
        .header p.p1 {
            width: 60px;
            height: 60px;
            margin: 0 auto;
            margin-top: 110px;
        }
        .header p.p2 {
            height: 40px;
            margin: 0 auto;
            text-align: center;
            line-height: 40px;
            margin-top: 10px;
            font-size: 20px;
            color: #fec468;
        }
        .header p.p3 {
            margin: 0 auto;
            text-align: center;
            line-height: 40px;
            font-size: 28px;
            color: #bddde6;
        }

        .contain {
            /*width: 1210px;*/
            margin: 0 auto;
            margin-top: 80px;
            height: 400px;
        }

        .border {
            width: 400px;
            height: 370px;
            background-color: red;
            float: left;
            margin: 40px;
            transform: translate(0%, 0%);
            border: 1px solid #0E273D;
            /*background: #444;*/
        }

        .border &gt; div {
            position: absolute;
            width: 100%;
            height: 100%;
            transition: .5s;
        }

        .border:hover &gt; .border-top-bottom {
            transform: rotateY(0);
        }

        .border:hover &gt; .border-left-right {
            transform: rotateX(0);
        }

        .border-top-bottom {
            border: 1px solid transparent;
            border-top: 1px solid #57daff;
            border-bottom: 1px solid #57daff;
            transform: rotateY(90deg);
        }

        .border-left-right {
            border: 1px solid transparent;
            border-left: 1px solid #57daff;
            border-right: 1px solid #57daff;
            transform: rotateX(90deg);
        }
        
        .border_div {
            width: 400px;
            height: 370px;
        }
        .border_div_top {
            width: 400px;
            height: 300px;
            background-color: #fff;
        }
        .img {
            width: 100%;
            height: 100%;
        }
        .border_div_bottom {
            width: 400px;
            height: 70px;
            color: #57daff;
            background-color: #0E273D;
            line-height: 70px;
            text-align: center;
            font-weight: 600;
        }
        
    &lt;/style&gt;
    
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="header"&gt;
        &lt;p class="p2"&gt;&lt;/p&gt;
        &lt;p class="p3"&gt;烟花合集&lt;/p&gt;
        &lt;p class="p2"&gt;——by XiongZe 演示&lt;/p&gt;
    &lt;/div&gt;

    &lt;div class="contain" style="width:1600px;"&gt;
	&lt;a href="data/8jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/8.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5 Canvas庆祝春节过年放烟花动画代码&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
	 

        &lt;a href="data/5jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/5.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5烟花绽放场景动画&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
		
		 &lt;a href="data/6jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/6.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5炫酷喜庆全屏烟花动画特效&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
	
        &lt;a href="data/1jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/1.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5点击燃放烟花&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;

        &lt;a href="data/2jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/2.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5漂亮的3D烟花动画&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;

        &lt;a href="data/3jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/3.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5烟花粒子特效&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;

		 &lt;a href="data/7jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/7.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;jQuery随机点名中奖后放烟花动画特效&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
		
		
		
		 &lt;a href="data/9jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/9.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;css3烟花和霓虹灯文字动画效果&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
		
		 &lt;a href="data/10jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/10.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5 Canvas彩色烟花动画特效&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;

		 &lt;a href="data/11jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/11.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;jQuery+css3实现鼠标点击烟花播放效果&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
		
       &lt;a href="data/4jQuery/index.html" target="_blank"&gt;
            &lt;div class="border"&gt;
                &lt;div class="border_div"&gt;
                    &lt;div class="border_div_top"&gt;
                        &lt;img class="img" src="images/4.png" /&gt;
                    &lt;/div&gt;
                    &lt;div class="border_div_bottom"&gt;HTML5 Canvas烟花喷泉动画特效&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="border-top-bottom"&gt;&lt;/div&gt;
                &lt;div class="border-left-right"&gt;&lt;/div&gt;
            &lt;/div&gt;
        &lt;/a&gt;
        
&lt;/div&gt;
    
&lt;/body&gt;
&lt;/html&gt;

```

完整代码下载地址：
