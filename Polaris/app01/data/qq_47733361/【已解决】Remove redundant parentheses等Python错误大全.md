
--- 
title:  【已解决】Remove redundant parentheses等Python错误大全 
tags: []
categories: [] 

---
本篇文章就是记录一些在学习Python过程中出现的一些警告错误与修改方法，在你不知道是什么错误时，不妨进来看看这些千奇百怪的报错，说不定其中就有你的那一个呢，解决！！！

本篇文章实时更新，收藏不亏！！！

### 1、End of statement expected

这个意思是：预计报表结束，即输出这里没加括号 解决：使用括号把输出内容括起来 <img src="https://img-blog.csdnimg.cn/ed798e1933d44f57b813206f24ed3dac.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 2、Remove redundant parentheses

这个意思是：删除多余的括号 解决：删掉外面括号即可 例图： <img src="https://img-blog.csdnimg.cn/93e24392cf9e4623897bd3399542e576.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 3、Too few arguments for format string

这个意思是：格式字符串的参数太少 解决：使用print进行格式输出时，注意前后类型与数量的对应 例图：本来是字符串，没经过变化就直接按整形输出 <img src="https://img-blog.csdnimg.cn/eb7d5b5186ae4172a10a01b80706d095.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 4、ValueError: too many values to unpack (expected 3)

这个意思是：ValueError:要解压缩的值太多（预期为3个） 解决：若你在输入的地方报这个错误，就是你的接受变量少了，或者忽略了分隔符，此时你可以在input()后添加split()试试； 例图： <img src="https://img-blog.csdnimg.cn/0a4a1d862fa84c10a1fd50b8130198ab.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 5、Simplify chained comparison

这个意思是：简化链式比较 解决：这个错误比较容易出现在选择结构中，是要你简化逻辑表达式，具体看下例图： <img src="https://img-blog.csdnimg.cn/0a36f3da162540219275972f6dbaf18c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_15,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 修改为如下：波浪线已经消失啦 <img src="https://img-blog.csdnimg.cn/52fd00bfc26a4c5badc3a87cb72af125.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_15,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 6、Redeclared ‘s’ defined above without usage

这个意思是：上面定义的重新声明的“s”没有使用 解决：出现这个错误的原因大部分是由于你的表达式丢了一些变量，致使逻辑不通 例图（换颜色了，黑色看久了太难受^ - ^）： <img src="https://img-blog.csdnimg.cn/3dc837b175464aff825fe783157b6a1f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 7、Expected type ‘Union[str, bytes, CodeType]’, got ‘int’ instead

这个意思是：应为“Union[str，bytes，CodeType]”类型，改为“int” 解决：这个错误是由于类型不对应造成的，出现这个错误你需要在报错的位置仔细检查符号两边的类型，如下图就是多此一举： 例图： eval可以进行表达式运算，却又转成了int类型（只是举例），可以用eval处理输入，也可使用print直接输出x+y； <img src="https://img-blog.csdnimg.cn/6c47d7a51e3a483e94bff63fe9b8fa70.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 8、Typo: In word ‘zimu’

这个意思是：拼写错误：在单词“子母”中；这是一个警告，出现这个警告的原因就是你定义的变量名字单词拼写出错。 解决：若你想让他消失，可以修改变量为正确字母拼写或者修改变量名。 例图： <img src="https://img-blog.csdnimg.cn/2a8d850060a14b97845868f13f0d9016.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 9、Indent expected

这个意思是：预期缩进 解决：这个错误常出现在if、循环后的冒号后面没有语句；解决只需添加语句即可 例图： <img src="https://img-blog.csdnimg.cn/50295d3b69e64b2394d899ab2aa8b0df.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 10、TypeError: ‘float’ object cannot be interpreted as an integer

这个意思是：TypeError:“float”对象不能解释为整数 解决：出现这个问题的原因是因为前后数据类型不一样；可以使用强制类型转换来尝试解决 例图： <img src="https://img-blog.csdnimg.cn/4e3d751c58244ee9b67629f13fd6e1dc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9653406088764a4bac62703252f79e68.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 11、Unused import statement ‘import turtle’ 这个意思是：未使用的导入语句“import turtle” 解决：这个并不是报错，只是提示当前代码中没有用到这个包而已，后面的代码用到这个包的话，它会自动恢复高亮的。 例图： <img src="https://img-blog.csdnimg.cn/134f5f70bc284221b37bb1f4f2f4d9a0.png" alt="在这里插入图片描述">
