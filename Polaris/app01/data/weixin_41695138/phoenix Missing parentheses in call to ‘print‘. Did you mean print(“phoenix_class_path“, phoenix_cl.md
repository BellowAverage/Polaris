
--- 
title:  phoenix Missing parentheses in call to ‘print‘. Did you mean print(“phoenix_class_path:“, phoenix_cl 
tags: []
categories: [] 

---
(base) [root@node01 apache-phoenix-5.0.0-HBase-2.0-bin]# bin/sqlline.py node01:2181 Traceback (most recent call last): File “bin/sqlline.py”, line 25, in  import phoenix_utils File “/export/servers/apache-phoenix-5.0.0-HBase-2.0-bin/bin/phoenix_utils.py”, line 208 print “phoenix_class_path:”, phoenix_class_path ^ SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“phoenix_class_path:”, phoenix_class_path)? <img src="https://img-blog.csdnimg.cn/471c69d0a24542279f54443159685afe.png" alt="在这里插入图片描述"> 参考  按着这篇博客 成功， 非常感谢博主的分享 <img src="https://img-blog.csdnimg.cn/11d719134db44a619093b00569cf4412.png" alt="在这里插入图片描述">
