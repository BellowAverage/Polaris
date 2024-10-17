
--- 
title:  用 Python 破解了同学压缩文件的密码 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/3e3cd2d4fa0e88d24f407a85f83888df.png">

作者：blank#

https://blog.csdn.net/weixin_39098318/article/details/104980832

**经常遇到百度网盘的压缩文件加密了，今天我们就破解它！**

实现思路

**爆破密码的思路**其实都大同小异：无非就是字典爆破，就看你是有现成密码字典，还是自己生成密码字典，然后进行循环输入密码，直到输入正确位置。现在很多都有防爆破限制，根本无法进行暴力破解，但是似乎zip这种大家都是用比较简单的密码而且没有什么限制。因此 实现思路就是 **生成字典-&gt;输入密码-&gt;成功解压**

实现过程

**1.  生成字典**生成密码字典其实就是一个字符组合的过程。小伙伴们可别用列表去组合噢，很容易就内存溢出了，用生成器就最好啦。这里我选择使用python的**itertools**模块。**itertools**是2.3版本加入的用于创建循环用迭代器的函数模块。而 **itertools.product(*iterables[, repeat])** 函数是**对应有序的重复抽样过程****。**写出来生成密码字典的方法：（输出1，2组成长度为4的所有密码）

```
import itertools


def allkeyword(dic,num):
    allkey1 = itertools.product(dic,repeat=num)
    allkey2 = (''.join(i) for i in allkey1)
    return allkey2


dictionaries = ['1', '2']
print(list(allkeyword(dictionaries,4)))
# ['1111', '1112', '1121', '1122', '1211', '1212', '1221', '1222', '2111', '2112', '2121', '2122', '2211', '2212', '2221', '2222']

```

**2.  解压文件**好家伙，python的 **zipfile** 模块不就可以对文件压缩解压嘛？使用方法参考官方文档：https://docs.python.org/zh-cn/2/library/zipfile.html

```
import zipfile


try:
    ZIPFILE = zipfile.ZipFile(r'D:\123\1.zip')  # 注意路径
    ZIPFILE.extractall(path=r'D:\123',pwd=b'1234')  # 解压到哪个路径
    print("解压成功")


except:
    print("解压失败")



```

没有意外测试文件应该可以解压成功的。

**3.  模拟项目所需加密的压缩文件**

<img src="https://img-blog.csdnimg.cn/img_convert/6c3900d609689fd764526968562bbd3d.png">

新建abc.txt文件，输入abc

<img src="https://img-blog.csdnimg.cn/img_convert/da8d8a0189a9c0e258112ca0d2624a77.png">

右键txt文件，添加到压缩文件，并设置密码，确定

<img src="https://img-blog.csdnimg.cn/img_convert/8ebae4ec0fdd68aa11477df2f3e7384d.png">

这里我们删除原有的txt文件，方便测试，破解成功后解压到当前路径

**4.  使用生成的字典去爆破密码**

结合1和2步骤，完整的代码：（注意看注释学习）

```
import zipfile
import itertools


# 破解一个4位数密码数字和字母为23ab大概5-10分钟，仅供参考。
dictionaries = ['1', '2', '3', '4','5','6','7','8','9','0',
                'a','b','c','d','e','f','g','h','i','j','k',
                'l','m','n','o','p','q','r','s','t','u','v',
                'w','x','y','z']         #组成破解字典的关键字符（可以按照自己需求添加）
end_for = True      # 用于破解成功后，停止循环的变量
# 设置密码的长度1到16位密码
for x in range (1,17):
    if end_for:
        def allkeyword():
            allkey1 = itertools.product(dictionaries,repeat=x)
            allkey2 = (''.join(i) for i in allkey1)
            return allkey2


        def trypassword (password):
            try:
                ZIPFILE = zipfile.ZipFile(r'D:\zip\abc.zip')   # 需要解压带有密码的本地abc.zip
                ZIPFILE.extractall(path=r'D:\zip',pwd=password.encode('utf-8'))     # 解压到哪个路径下
                print(f"解压成功,正确密码为：{password}")       # 解压成功，并打印出正确密码
                global end_for      # 声明为全局变量，没有声明，重新赋值无效
                end_for = False     # 解压成功，停止循环
                return True
            except:
                print(f"解压失败,尝试密码为：{password}")  
                return False


        #用trypassword函数返回的True或者Flase来判定程序是否终止。
        for pwd in allkeyword() :   
            if trypassword(pwd):
                break

```

<img src="https://img-blog.csdnimg.cn/img_convert/cde9ea9b1da423eb9754b89be06c5b85.png">

执行代码后，4位数的密码（数字字母组合的）大概5-10分钟就能成功解压，破解打印密码了。

<img src="https://img-blog.csdnimg.cn/img_convert/0a88597ade31405eeb1b03606b59e68d.png">

破解密码后，由于我们设置的是解压到当前路径下，可以看到abc.txt文件就出来了。

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/72abcf275e0234df5d0cec2c925e3c8a.gif">

微信扫码关注，了解更多内容
