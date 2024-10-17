
--- 
title:  python将自定义模块加入python系统库 
tags: []
categories: [] 

---
## 1.使用pycharm新建Python软件包<img alt="" height="639" src="https://img-blog.csdnimg.cn/f196ab09e83f4ad2ab52882767284460.png" width="1048">

### 2.新建.py文件，添加测试代码

```
def test2():
    print('测试')
```

 <img alt="" height="208" src="https://img-blog.csdnimg.cn/2b44882c5bdc44c6a9f056bbe4ddd4b1.png" width="631">

## 3.在test的同级目录下新增一个脚本setup.py

```
from distutils.core import setup
setup(name="我很牛逼", version="6.6.6", description="666 to install module", author="someone", py_modules=['test.test1'])
```

<img alt="" height="493" src="https://img-blog.csdnimg.cn/13c2bdba866447e581c81879ce444774.png" width="1031">

## 4.在测试路径下执行构建命令python setup.py build

## 5.执行打包命令python setup.py sdist，执行之后会出来一个压缩包，将其解压

<img alt="" height="194" src="https://img-blog.csdnimg.cn/d12d2d33e749472583a1f9bfe8e76039.png" width="696">

## 6.在解压目录下执行python setup.py install

## 7.新建py文件测试<img alt="" height="150" src="https://img-blog.csdnimg.cn/f6656b879f1f48f6af5f24972ec3c33d.png" width="594">








