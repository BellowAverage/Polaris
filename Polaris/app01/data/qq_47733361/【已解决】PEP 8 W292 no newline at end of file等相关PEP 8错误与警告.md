
--- 
title:  【已解决】PEP 8: W292 no newline at end of file等相关PEP 8错误与警告 
tags: []
categories: [] 

---
最近pycharm总是报这些错误与警告，真是逼死强迫症啊，因此搜索才知道这是PEP8规范( Python Enhancement Proposal ），线总结如下：

注：例图中的错误位置在波浪线出！

### 1、PEP 8: W292 no newline at end of file

这个意思是：**W292文件末尾没有换行符** 解决：在代码最后一行加一个**回车**即可 例图： <img src="https://img-blog.csdnimg.cn/37da79e0dee64c93bb7042c3a33a0dd5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_10,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 2、PEP 8: W391 blank line at end of file

这个意思是：**W391文件末尾的空行** 解决：代码最后有**两行空行，删除一行**即可 例图： <img src="https://img-blog.csdnimg.cn/41fe9af370eb45739f806c5b48897a98.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_15,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 3、PEP 8: E221 multiple spaces before operator

这个意思是：**E221运算符前面的多个空格** 解决：在相关运算符处只保留一个空格 例图： <img src="https://img-blog.csdnimg.cn/b344d063b26946fdb53a140ad957fa66.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 4、PEP 8: E228 missing whitespace around modulo operator

这个意思是：PEP 8:E228模运算符周围缺少空格 解决：在运算符附近添加空格 例图： <img src="https://img-blog.csdnimg.cn/9e50a2b167af426a8dc5bbeaa4c35f65.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 5、PEP 8: E402 module level import not at top of file

这个意思是：PEP 8:E402模块级导入不在文件顶部 解决：把import这行放在代码最上方 例图： <img src="https://img-blog.csdnimg.cn/1e3568d89b504ce783cbc42da6c4d7ec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 6、PEP 8: E303 too many blank lines (3)

这个意识是：PEP 8:E303空行过多（3） 解决：下图中9,10,11三行空行，保留一行 例图： <img src="https://img-blog.csdnimg.cn/19d34a79dbb64da5960338c61e8dc529.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 7、PEP 8: E501 line too long (143 &gt; 120 characters)

这个意思是：PEP 8:E501行太长（143&gt;120个字符） 解决：可以进行换行，不要一行太多 例图： <img src="https://img-blog.csdnimg.cn/204f541090ae418a9819854c286149c6.png" alt="在这里插入图片描述">

### 8、PEP 8: E265 block comment should start with '# ’

这个意思是：PEP 8:E265块注释应以“#”开头 解决：出现这个是因为你的注释‘#’后面没有加空格 例图： <img src="https://img-blog.csdnimg.cn/52b02f3ff7ff467fa7b6c63960331cfb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 9、PEP 8: E251 unexpected spaces around keyword / parameter equals

这个意思是：PEP 8:E251关键字/参数equals周围出现意外空格 解决：把报错地方的空格删掉即可 例图： <img src="https://img-blog.csdnimg.cn/bac0008a4d9b4fd0b76b01790d2dd516.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 10、PEP 8: E721 do not compare types, use ‘isinstance()’

这个意思是：PEP 8:E721不比较类型，请使用’isinstance（）’ 解决：这里说他是不比较类型，当然不对呀，所以所这个警告可以忽略，光标移到波浪线处，按Alt + Enter，选择忽略这个警告 <img src="https://img-blog.csdnimg.cn/22bc7deab0d94a7a8fa48caf72a52897.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

例图： <img src="https://img-blog.csdnimg.cn/ccf1545565cf4c1bb272c3f8244efdfd.png" alt="在这里插入图片描述">

### 11、PEP 8: E261 at least two spaces before inline comment

这个意思是：PEP 8:E261内联注释前至少有两个空格 解决：注释与代码中间放两个空格就好啦 例图： <img src="https://img-blog.csdnimg.cn/2607abcc314c4c028a8af41919211561.png" alt="在这里插入图片描述">

### 12、PEP 8: E262 inline comment should start with '# ’

这个意思是：PEP 8:E262内联注释应以“#”开头 解决：出现这个错误的原因是注释以‘#’开头，但与后面内容没有空格隔开，会出现这个警告 例图： <img src="https://img-blog.csdnimg.cn/09d8e3282ef3407194f326471e1b79e1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAMjHlsoHooqvov6vnp4PlpLQ=,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 13、Function name should be lowercase

这个意思是：函数名应为小写 解决：函数名中不要使用大写 例图： <img src="https://img-blog.csdnimg.cn/c93ae902b3224009b1cb4dbd9818ff8f.png" alt="在这里插入图片描述">
