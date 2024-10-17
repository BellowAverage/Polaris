
--- 
title:  knife4j文档-个人笔记 
tags: []
categories: [] 

---
### 文档中返回值不显示的解决办法

>  
 文档中swagger 中是支持泛型返回的，所有在统一返回类中，泛型一定要写。也必须加上@ApiModel注解 

- 返回类展示
<img src="https://img-blog.csdnimg.cn/20201120135405268.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
- 控制层返回类展示
<img src="https://img-blog.csdnimg.cn/20201120135554385.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
- 效果如下： <img src="https://img-blog.csdnimg.cn/20201120135850588.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">