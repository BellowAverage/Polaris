
--- 
title:  pycharm 自定义的包找不到的解决方案 
tags: []
categories: [] 

---
遇见一个问题：找不到自定义的包。 项目结构：
<li>utils 
  <ul>- time
然后执行：

```
# main.py
import utils.time

```

提示找不到。

排查方式：

```
import sys
print(sys.path)

```

发现里面的目录没有项目目录

需要把项目根目录加入到Path里面即可

方式： 文件 - 设置 - 项目 -项目结构 - 添加内容根 把需要的路径添加到内容根里面 到本地测试：import untils，出现代码提示。 修复成功。

排除也是。 通常需要把.idea拍除出内容根。
