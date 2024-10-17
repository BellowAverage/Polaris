
--- 
title:  如何将Python打包后的exe还原成.py？ 
tags: []
categories: [] 

---
来源：https://www.jianshu.com/p/5871c3dd633b

用到的工具
1. pyinstxtractor.py 拆包（解压）工具，将exe文件解压成一个文件夹1. uncompyle6 pyc反编译工具1. 010EditorEditor 或者其他二进制查看与修改工具，我这里用的010Editor
#### 安装方法

```
pip install uncompyle6
```

##### 第一步：解包

```
python3 pyinstxtractor.py ***.exe   #  这里替换成你要反编译的exe文件

#  会生成一个以 exe文件名+_extracted 的文件夹，这个就是解包后的数据
```

##### 第二步：添加头信息

PyInstaller打包后，pyc文件的前8个字节会被抹掉，所以最后要自己添加回去。前四个字节为python编译的版本，后四个字节为时间戳。想要获得编译版本可以查看打包文件里struct的信息

1). 进入文件夹，找到以exe文件名命名的文件(没有后缀)，这个就是目的文件<img src="https://img-blog.csdnimg.cn/img_convert/51c03bd7c39f846c945d83f8b8bc06ca.png" alt="51c03bd7c39f846c945d83f8b8bc06ca.png">

2). 用 010Editor 打开 struct，前八位就是我们想要的信息，将其复制

3). 用 010Editor 打开目的文件我这里是 abc_text，将上一步复制的信息插入到开头

修改前：

修改后：

4). 将目的文件我这里是 abc_text，添加pyc的后缀

##### 第三步：逆向目的文件.pyc

1). 其实这里已经可以使用了。了解python的都知道pyc是py文件编译后的二进制文件，因此如果想要分析源码还得继续逆向成.py文件<img src="https://img-blog.csdnimg.cn/img_convert/209d9ff0fc168476b15cfd78356460fd.png" alt="209d9ff0fc168476b15cfd78356460fd.png">

2). uncompyle6逆向pyc文件

```
uncompyle6 abc_text.pyc &gt; abc_text.py
```

<img src="https://img-blog.csdnimg.cn/img_convert/984677facdd6d3525aea4efc7cb42b2f.png" alt="984677facdd6d3525aea4efc7cb42b2f.png">

<img src="https://img-blog.csdnimg.cn/img_convert/aeb42e5d96e91715c11a84688d8c6e76.png" alt="aeb42e5d96e91715c11a84688d8c6e76.png">

**往期推荐：**
- ****- ****- - - - - 
PS：如果觉得我的分享不错，欢迎大家随手点赞、在看~
