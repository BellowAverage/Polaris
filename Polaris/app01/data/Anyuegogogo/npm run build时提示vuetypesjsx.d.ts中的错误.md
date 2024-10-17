
--- 
title:  npm run build时提示vue/types/jsx.d.ts中的错误 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/e364aebcacc64e3facd0b39e84cc344b.png" alt="在这里插入图片描述"> **解决方法一：** 可能是因为vue版本过高引起的 我直接将package.json中vue以及vue-template-compiler的版本的前面^去掉，安装指定的版本 注意：vue和vue-template-compiler需要版本一致 <img src="https://img-blog.csdnimg.cn/direct/078404b3067e495f807397e6f63bf990.png" alt="在这里插入图片描述"> 参考链接：

**解决方法二：** 如果如上操作还是不行，升级typescript版本 <img src="https://img-blog.csdnimg.cn/direct/43eaf4d1c113486aaba31a76b3aafb6f.png" alt="在这里插入图片描述">
