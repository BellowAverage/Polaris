
--- 
title:  pycharm找不到包和pip无法找到路径的解决 
tags: []
categories: [] 

---
## 故障描述：

从git拉取代码，代码没有任何问题，但是提示各种找不到包。

然后发现原因是：
- 使用cmd访问- pycharm没有将cmd添加path，导致无法访问python- pycharm会默认修改workdir为当前路径，执行的路径不对，系统会在当前目录、默认路径和环境变量里面找包，而我用pycharm执行脚本的时候会以.py文件所在的路径执行命令，导致根本找不到包。
## 解决方案：将所有包的路径的上一个路径点击–右键–将目录标记为–测试源根。

### 系统要找utils/func。那么就把utils的父路径设置为测试源根。

### pycharm终端无法使用pip

pycharm直接使用终端是直接调用了cmd，cmd没有他就没有。

解决方案:设置环境变量。可以在windows写入path也可以在pycharm设置。

Python的pip和Python在一个路径，导入{你的安装路径}/bin到Path即可。
