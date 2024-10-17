
--- 
title:  Python 基础（十）：模块与包 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- <ul><li>- - - 


### 1 简介

#### 1.1 模块

Python 中一个以 `.py` 结尾的文件就是一个模块，模块中定义了变量、函数等来实现一些类似的功能。Python 有很多自带的模块（标准库）和第三方模块，一个模块可以被其他模块引用，实现了代码的复用性。

#### 1.2 包

包是存放模块的文件夹，包中包含 `__init__.py` 和其他模块，`__init__.py` 可为空也可定义属性和方法，在 Python3.3 之前的版本，一个文件夹中只有包含 `__init__.py`，其他程序才能从该文件夹引入相应的模块、函数等，之后的版本没有 `__init__.py` 也能正常导入，简单来说就是 Python3.3 之前的版本，`__init__.py` 是包的标识，是必须要有的，之后的版本可以没有。

### 2 使用

#### 2.1 创建

**创建包**

使用 PyCharm 创建包，步骤为：①打开 PyCharm 选中项目 ②右击鼠标选中 `New` 选项，然后再选中 `Python Package` 后单击鼠标，此时弹出创建窗口，如下所示：

<img src="https://img-blog.csdnimg.cn/20191212203724580.PNG#pic" alt="" width="400">

我们填好名字后点击 `OK` 按钮即可。创建好后我们会发现 PyCharm 已经自动帮我们创建了空文件 `__init__.py`。

**创建模块**

使用 PyCharm 创建模块，步骤为：①选中刚刚创建的包 ②右击鼠标选中 `New` 选项，然后再选中 `Python File` 后单击鼠标，此时弹出创建窗口，如下所示：

<img src="https://img-blog.csdnimg.cn/20191212205111397.PNG#pic" alt="" width="300"> 我们填好名字后点击 `OK` 按钮即可。

我们创建包和模块的最终目录结构为：

```
package
|- pg1
|- - __init__.py
|- - a.py
|- - b.py
|- pg2
|- - __init__.py
|- - c.py
|- - d.py

```

a.py

```
def a():
    print('a')

```

b.py

```
def b():
    print('b')

```

c.py

```
def c():
    print('c')

```

d.py

```
def d():
    print('d')

```

#### 2.2 引用

从包中引入模块有如下两种方式：

`import ...`

```
import 包名1.包名2...模块名

```

`from ... import ...`

```
from 包名1.包名2... import 模块名
from 包名1.包名2...模块名 import 变量名/函数名

```

下面我们使用创建好的包和模块演示一下，如下所示：

```
# a 模块中引入 b 模块
import pg1.b
from pg1 import b

# a 模块中引入 c 模块
import pg2.c
from pg2 import c

# a 模块中引入 c 模块和 d 模块
import pg2.c,pg2.d
from pg2 import c,d

# a 模块中引入包 pg2 下的所有模块
from pg2 import *

# a 模块中引入 d 模块中函数 d()
from pg2.d import d
# 调用函数 d()
d()

```

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">
