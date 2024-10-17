
--- 
title:  在VScode中配置Python开发环境 
tags: []
categories: [] 

---
### 1、安装python

官网下载地址： 双击打开.exe文件 勾选 Add Python 3.8 to Path选项，然后点击install now即可安装。 <img src="https://img-blog.csdnimg.cn/6915a638c74d4d358967ef7de96e5642.png#pic_center" alt="在这里插入图片描述">

安装中： <img src="https://img-blog.csdnimg.cn/287de3c8db084569996cc755a5feaa56.png#pic_center" alt="在这里插入图片描述">

安装完毕后点击close即可。

### 2、测试

按键盘win+r，在左下角运行窗口里输入cmd，回车。 <img src="https://img-blog.csdnimg.cn/80b623defef84d428994e293a556a195.png#pic_center" alt="在这里插入图片描述"> 在弹出的窗口里输入python，回车。得到如下显示。 <img src="https://img-blog.csdnimg.cn/47c106055aa949bdbeb90200dc6163bf.png#pic_center" alt="在这里插入图片描述">

在提示符 &gt;&gt;&gt; 后面输入1+1，回车后显示2。 <img src="https://img-blog.csdnimg.cn/710cfdde2dff41f5b7c56ff37066b4c5.png#pic_center" alt="在这里插入图片描述">

安装成功。

### 3、安装VScode

官网下载地址： 找到下载好的安装包，双击打开，一直点下一步即可。

### 4、设置VScode

打开安装好的VScode，可以先设置好中文界面和解决中文注释乱码问题，详细步骤见上一篇博客： 按照下图步骤搜索并安装。

<img src="https://img-blog.csdnimg.cn/6e4a978ca5944c88917a0f1747c26409.png#pic_center" alt="在这里插入图片描述"> 添加一个准备存放代码的python文件夹。

<img src="https://img-blog.csdnimg.cn/afe168fb9c5a445a8d066bdc862848fd.png#pic_center" alt="在这里插入图片描述"> 打开设置。 <img src="https://img-blog.csdnimg.cn/2eff778e5cf64ea4bf5a17cf1eca1c2b.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/92413f0ec07e44d293da091a70dfe250.png#pic_center" alt="在这里插入图片描述"> 在settings.json中输入下列代码，用来配置flake8和yapf并关闭pylint工具。

```
{
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "yapf",
    "python.linting.flake8Args": ["--max-line-length=248"],
    "python.linting.pylintEnabled": false
}

```

<img src="https://img-blog.csdnimg.cn/6edd3541d07b4430adb9bf9338d33240.png#pic_center" alt="在这里插入图片描述"> 保存并关闭。

### 5、测试

在所选择的文件夹下新建一个python文件，以.py结束。 在文件中输入要测试的代码：

```
print('hello world')

```

运行并查看结果。

<img src="https://img-blog.csdnimg.cn/5f81c5e128e2478fbe588eee11d8f6d6.png#pic_center" alt="在这里插入图片描述"> 结果输出正常则安装完毕。
