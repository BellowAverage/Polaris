
--- 
title:  MovieWriter stderr:[AVFilterGraph @ 0000000002b9c140] No such filter: ‘palettegen‘ 
tags: []
categories: [] 

---


MovieWriter stderr: [AVFilterGraph @ 0000000002b9c140] No such filter: 'palettegen'

错误代码：

```
  anim.save(gifname)
```



解决方法：

```
 anim.save("aaaa.gif",writer='pillow')
```


