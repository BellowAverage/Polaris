
--- 
title:  mac 完全卸载python 
tags: []
categories: [] 

---
###### 这里主要是卸载pkg安装的python

**第一步：删除框架** sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.11

**第二步：删除应用目录** sudo rm -rf “/Applications/Python 3.11” **第三步：删除指向 Python 的连接** 法1 cd /usr/local/bin/ ls -l /usr/local/bin | grep ‘/Library/Frameworks/Python.framework/Versions/3.11’ 主要是显示有哪些链接 brew prune 删除这些链接 法2 ls -l /usr/local/bin | grep ‘…/Library/Frameworks/Python.framework/Versions/3.11’ | awk ‘{print $9}’ | tr -d @ | xargs rm <img src="https://img-blog.csdnimg.cn/c128b228fa114f45b2fafccc112f3560.png" alt="请添加图片描述" width="200"> 法3 cd /private/var/db/receipts ls <img src="https://img-blog.csdnimg.cn/b526eeeadf424d2391e8e6562ff721c5.png" alt="请添加图片描述" width="300">就是删除以上链接 快速进入这个目录的方式，第一种打开访达，使用ctrl+shift+G 出来这个页面： <img src="https://img-blog.csdnimg.cn/50cc6ea5dbfb4b2fb1438b8e17e0fb11.png" alt="请添加图片描述" width="200">第二种通过terimal 终端 使用 open /private/var/db/receipts 命令

至此，删除完成。
