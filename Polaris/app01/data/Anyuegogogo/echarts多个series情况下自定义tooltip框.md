
--- 
title:  echarts多个series情况下自定义tooltip框 
tags: []
categories: [] 

---
**先上效果图** <img src="https://img-blog.csdnimg.cn/b1933d10ade1499a98a235d61a419175.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pqX5pyITW9vbg==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

>  
 其实就是用到tooltip下面的formatter，参数params就是当前横坐标对应的所有的不论是柱形图还是折线图还是什么图的数据，它是一个数组，是按series的数据的顺序来的，像上图，其实每个横坐标都是有五组数据的（有两组也是柱形图，只是没有数据，页面上没有显示）。formatter函数return的东西就是你的tooltip的内容。里面可以是标签文本，就是说你想要什么样子的tooltip框，就组什么样子的标签以及内容就好了。 


```
      tooltip: {<!-- -->
        trigger: 'axis',
        axisPointer: {<!-- -->
          // Use axis to trigger tooltip
          type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
        },
        formatter: (params) =&gt; {<!-- -->
        console.log(params);
          return `&lt;div style="padding: 5px 20px 5px 10px;"&gt;
                    &lt;div&gt;${<!-- -->params[0].axisValue}&lt;/div&gt;
                    &lt;div&gt;&lt;span style=\"display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#E638F4;\"&gt;&lt;/span&gt;${<!-- -->params[4].seriesName}: ${<!-- -->params[4].value}%&lt;/div&gt;
                    &lt;div&gt;&lt;span style=\"display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#347EF5;\"&gt;&lt;/span&gt;${<!-- -->params[0].seriesName}: ${<!-- -->params[0].value} 小时&lt;/div&gt;
                    &lt;div&gt;&lt;span style=\"display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#24B5FF;\"&gt;&lt;/span&gt;${<!-- -->params[1].seriesName}: ${<!-- -->params[1].value} 小时&lt;/div&gt;
                    &lt;div&gt;&lt;span style=\"display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#4BB6AB;\"&gt;&lt;/span&gt;${<!-- -->params[2].seriesName}: ${<!-- -->params[2].value} 小时&lt;/div&gt;
                    &lt;div&gt;&lt;span style=\"display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#FCC950;\"&gt;&lt;/span&gt;${<!-- -->params[3].seriesName}: ${<!-- -->params[3].value} 小时&lt;/div&gt;
                  &lt;/div&gt;`
        }
      },

```

在formtter里面打印出params,可以看到有五组数据（控制台会打印出很多条params数据,每条里面都有五组数据），然后每组数据里面的属性如下 1.五组数据 <img src="https://img-blog.csdnimg.cn/764bfc12dccf4358aa40c819dbe5feaa.png#pic_center" alt="在这里插入图片描述"> 2.每条数据里面都有哪些属性 <img src="https://img-blog.csdnimg.cn/d1fcf492bf574d63b32a43a2818846b4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5pqX5pyITW9vbg==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
