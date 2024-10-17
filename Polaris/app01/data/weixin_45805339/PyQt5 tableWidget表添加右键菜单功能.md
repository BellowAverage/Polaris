
--- 
title:  PyQt5 tableWidget表添加右键菜单功能 
tags: []
categories: [] 

---
### 右键菜单功能函数

```
    def tableWidget_VTest_menu(self, pos):
        """
        :return:
        """
        row_num = -1
        for i in self.tableWidget_VTest.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num &lt; 500: # 表格生效的行数，501行点击右键，不会弹出菜单
            menu = QMenu() #实例化菜单
            item1 = menu.addAction(u"清除")
            item2 = menu.addAction(u"拷贝")
            item3 = menu.addAction(u"粘贴")
            action = menu.exec_(self.tableWidget_VTest.mapToGlobal(pos))
        else:
            return
        if action == item1:
            print("清除表格内容")
        elif action == item2:
        	print("拷贝选中内容")
        elif action == item3:
        	print("粘贴拷贝内容")

```

### 信号与槽函数连接

```
# table widget 右键菜单 放在主窗口__init__(self):下
self.tableWidget_VTest.setContextMenuPolicy(Qt.CustomContextMenu) # 允许右键产生子菜单
self.tableWidget_VTest.customContextMenuRequested.connect(self.tableWidget_VTest_menu)  # 右键菜单

```
