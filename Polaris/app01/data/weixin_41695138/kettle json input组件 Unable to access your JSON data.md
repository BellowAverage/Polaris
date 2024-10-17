
--- 
title:  kettle json input组件 Unable to access your JSON data 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/8a505573f0a4487dbea0c8e33ec0dbd9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
Unable to access your JSON data 

It looks like the location you specified is either incorrect or you do not have access. Check your settings in the File tab and try again. 

```

用 kettle 的 JSON input组件输入时，点击 select fileds 时，出现以上异常。原因是我的json 文件路径中包含了 “+”，因此识别不了。文件路径修改之后正常。 <img src="https://img-blog.csdnimg.cn/d7dd8211ba904fafbaa3121ccfcc5e5f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
