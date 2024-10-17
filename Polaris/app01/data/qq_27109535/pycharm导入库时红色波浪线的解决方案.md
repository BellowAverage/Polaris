
--- 
title:  pycharm导入库时红色波浪线的解决方案 
tags: []
categories: [] 

---
pycharm导入库时红色波浪线的解决方案

大家在使用pycharm的时候一定会遇到大量的红色波浪线，根本原因就是python解释器找不到相应的包和文件。 <img src="https://img-blog.csdnimg.cn/ea6c1eb0a3ea4c94bb39f7b17da15fe3.png" alt="在这里插入图片描述">

小编带大家一起解决吧： （1）进入pycharm的settings中，然后找到python Console 在这里插入图片描述 <img src="https://img-blog.csdnimg.cn/14470827029f41748f439c1326c39533.png" alt="在这里插入图片描述">

（2）选中上图中的Add source roots to PYTHONPATH，之后选中ok的按钮进行确定。 <img src="https://img-blog.csdnimg.cn/ce5b3577f3d140cfaca3309cd34e5941.png" alt="在这里插入图片描述">

（3）到工程的根目录中：选中根目录右键，找到Mark Directory as —&gt;选Source Root

（4）按ctrl+S之后代码里面的红色波浪线均消失了—哈哈，是不是很神奇
