
--- 
title:  Pyside6/PyQT 项目实战，从0开始写一个GUI可视化项目：总览 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/2f3c9038f1b64187b273f13c31371f59.jpeg#pic_center" alt="在这里插入图片描述">

## 前言

>  
 最近使用 `Pyside6` 编写了几个**GUI**工具，发现效果出奇的好。遂产生了分享它的念头。 接下来如果不出意外，大概没有意外，我会开始写，介绍从零开始去编写一个实用的**GUI**工具。 这是`Pyside6`第一篇：《总览》 


本文对Pyside6在开发使用中进行了知识点的提炼，所以后面本专栏更新文章内容大致就是针对本文的每个小内容做一些拓展。

建议有需要的小伙伴通过官方文档去进行系统地学习！！ Pyside6 文档：

后面专栏新增文章时候，本文会做出相应修改！！ 专栏整体大概在10篇往上，反正学了你就能使用`Pyside6` 编写自己的**GUI**工具了。

<font color="blue" size="5">先在此大放厥词，本专栏无论是质量，还是质量，都是市面上你能找到的最好的！！！ <font color="red" size="5">效果是市面上最好的，欢迎各种打脸 <font color="red" size="5">效果是市面上最好的，欢迎各种打脸 <font color="red" size="5">效果是市面上最好的，欢迎各种打脸</font></font></font></font>

## 专栏脉络

>  
 专栏内容大体如下，会酌情增加一些使用技巧以及方法。 


初级文章暂定0篇，后续有空再慢慢更新； 《高阶文章》多线程部分已经更新完成。

<font color="blueredyellow" size="4"> 《初阶文章》基本操作系列 </font>
- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 大概率不会分享基础操作，选择性地分享一些**PySide6**使用中的小技巧- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如使用designer.exe绘制等比例缩放的窗口- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如鼠标悬停提示- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如窗口阴影、窗口状态栏- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如文件的导入的常用方法、文件拖拽- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如部分控件的指定操作，如单击、双击、拖拽- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如应用程序适应屏幕缩放- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如制作流畅的窗口控件动画，组合动画- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如使用MVC模型去拆解代码- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 如打包自己的PySide6/PyQT程序- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 以上的操作等，都没有技术上的难度。只有操作上的难度~- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 但最难的还是**UI**设置，笔者实在是没有审美，只有审丑- <input type="checkbox" class="task-list-item-checkbox" disabled> <font color="red">待更新</font> 暂待定，更新了效果图再说~
<font color="blueredyellow" size="4"> 《进阶文章》多线程系列操作 </font>
- - - - - - - - - 
### 基本流程
1. 布局（通过designer.exe 手动绘制1. 编写逻辑1. 将布局展示
### 前置操作

**安装模块**

```
pip install pyside6

```

### 文件转换

关于pyside6文件：https://doc.qt.io/qtforpython/tutorials/pretutorial/typesoffiles.html
- ui文件：布局文件，基于 XML 的格式- qrc文件：**Qt Recources file**，是一个 **XML** 格式的资源配置文件
**ui to py**

```
pyside2-uic xxx.ui -o xxx.py

```

**qrc to py**

```
pyside2-rcc xxx.qrc -o xxx.py

```

### 默认模板

**官方展示的案例**

```
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())

```

加载 **ui** 有两种方式，
- 一种是直接加载**ui**- 一种是将**ui**转成**py**，然后再加载**py**
**直接加载ui**
- 不好用，不做展示。
**加载py**

```
from PySide2.QtWidgets import QApplication, QMainWindow

from demo_ui import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


```

### 设置焦点

>  
 鼠标点击某个组件就执行指定操作时候，可以用到这一步。结合 。 


**方法一：**

在**designer** 中，选中对应的组件，

`属性编辑器 -&gt; focusPolicy -&gt; ClickFocus`

后面当鼠标点击在该组件时候，ui当前的焦点就在该组件上。

**方法二：**

```
self.QWidget.setFocusPolicy(Qt.ClickFocus)

```

### 固定界面大小

```
self.setFixedSize(self.width(), self.height())

```

### TableWidget

#### 设置行数

```
TableWidget.setRowCount(int())	# 输入int

```

#### 不显示行号

```
TableWidget.verticalHeader().setVisible(False)

```

#### 列可拖拽

```
TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

```

#### 均分列的宽度

```
TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

```

#### 根据内容长度分配列宽
- 两句一起用，效果更好
```
TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# 指定第0列
TableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
# 也可以不指定列，作用于所有列
TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

```

#### Table显示

```
from PySide2.QtWidgets import QTableWidgetItem

data = [('c1', 'c2', 'c3'), ('d1', 'd2', 'd3')...]
for row, row_data in enumerate(data):
    for columns, columns_data in enumerate(row_data):
        TableWidget.setItem(row, columns, QTableWidgetItem(str(columns_data)))

```

#### 表格复制

```
def __init__(self):
    # 剪切板
    self.cb = QtWidgets.QApplication.clipboard()
    ...
    # 单击表格单元格，即黏贴到剪切板
    self.table_show.clicked.connect(lambda: self.cb.setText(self.QTableWidget.currentItem().text()))



def keyPressEvent(self, event):
    """ Ctrl + C复制表格内容 """
    if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
        # 获取表格的选中行
        # 只取第一个数据块,其他的如果需要要做遍历,简单功能就不写得那么复杂了
        selected_ranges = self.QTableWidget.selectedRanges()[0]  
        # 最后总的内容
        text_str = ""  
        # 行（选中的行信息读取）
        for _row in range(selected_ranges.topRow(), selected_ranges.bottomRow() + 1):
            row_str = ""
            # 列（选中的列信息读取）
            for col in range(selected_ranges.leftColumn(), selected_ranges.rightColumn() + 1):
                item = self.QTableWidget.item(_row, col)
                # 制表符间隔数据
                row_str += item.text() + '\t'  
            # 换行	
            text_str += row_str + '\n' 
        self.cb.setText(text_str)


```

### 鼠标悬停文字提示

```
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont

QToolTip.setFont(QFont('SansSerif', 10))
self.button_run.setToolTip('点击该按钮可以&lt;br&gt;&lt;b&gt;打开与关闭数据预览&lt;/b&gt;')

```

### QFileDialog

#### 导入文件&amp;文件夹

```
from PySide2.QtWidgets import QFileDialog

# 对应的，做一些格式的筛选
path = QFileDialog.getOpenFileName(self, '选择文件', '.py', 'Python Files (*.py)')[0]

# 选择多个文件
path = QFileDialog.getOpenFileNames(self, '选择文件', '.py', 'Python Files (*.py)')[0]

```

#### 导出文件

```
QFileDialog.getSaveFileName(self, '保存文档', 'untitled.xlsx', 'excel文件 (*.xls *.xlsx)')[0]

```

### QMessageBox

#### 提示弹窗

```
from PySide2.QtWidgets import QFileDialog

QMessageBox.information(self, '提示', '这是提示弹窗')

```

#### 可选提示弹窗

```
res = QMessageBox.question(self, 'Message', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
if res == QMessageBox.Yes:
    print('你选择了是.')
else:
    print('你选择了否.')

```

### radioButton

#### 清空选择

```
QRadioButton.setAutoExclusive(False)
QRadioButton.setChecked(False)
QRadioButton.setAutoExclusive(True)

```

### 事件监听

#### 文件拖拽

```
# 设置文件支持拖拽
self.setAcceptDrops(True)

def dragEnterEvent(self, event) -&gt; None:
    """文件拖拽事件"""
    if event.mimeData().hasText():
        # 获取拖拽进来的文件路径
        file_path = event.mimeData().urls()[0].toLocalFile()
        # 鼠标放开函数事件
        event.accept()
        # do something
    else:
        event.ignore()

```

#### 关闭事件

```
def closeEvent(self, event) -&gt; None:
    """关闭事件"""
    res = QMessageBox.question(self, 'Message', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if res == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()

```

#### 鼠标点击事件

```
def mousePressEvent(self, event) -&gt; None:
    """鼠标点击事件"""
    # 判定是左键点击
    if event.button() == Qt.MouseButton.LeftButton:
        time.sleep(1)
        self.import_file()
    return
self.focusWidget().objectName() == 'groupBox'

```

### 窗口可拖拽
- 重写3个函数，
```
from PySide2.QtCore import Qt, QPoint

def __init__(self):
    # 窗口移动、设置鼠标动作位置
    self._move = False
    self.m_position = QPoint(0, 0)


# 鼠标点击事件产生
def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
        self._move = True
        self.m_position = event.globalPos() - self.pos()
        event.accept()

# 鼠标移动事件
def mouseMoveEvent(self, QMouseEvent):
    if Qt.LeftButton and self._move:
        self.move(QMouseEvent.globalPos() - self.m_position)
        QMouseEvent.accept()

# 鼠标释放事件
def mouseReleaseEvent(self, QMouseEvent):
    self._move = False


```

### 隐藏边框、阴影效果

```
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGraphicsDropShadowEffect


def __init__(self):
    # 隐藏边框
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)

    # 阴影效果
    effect = QGraphicsDropShadowEffect(self)
    effect.setBlurRadius(30)
    effect.setOffset(0, 0)
    effect.setColor(Qt.gray)
    self.setGraphicsEffect(effect)


```

### 状态栏图标

```
from ctypes import windll

# 这段代码放在前面即可
try:
    myapp_id = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
except ImportError:
    pass


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    # 指定状态栏和程序左上角的图标,需要绝对路径
	app.setWindowIcon(QtGui.QIcon(r'C:\User\Desktop\icon.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

```

### 退出所有进程

在 **closeEvent** 关闭事件里，退出主线程连带退出子线程。
- 添加 **os._exit(0)**
```
def closeEvent(self, event) -&gt; None:
    """关闭事件"""
    res = QMessageBox.question(self, 'Message', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if res == QMessageBox.Yes:
        event.accept()
        os._exit(0)
    else:
        event.ignore()

```

而这有一个前提，就是子线程需要为 **threading.Thread** 创建的新线程， 如下所示：

```
from threading import Thread


def new_thread():
    t = Thread(target=demo, args=())
    t.start()

def demo():
    ...

```

### 打包成 .exe

…

## 后话

本次分享远远未结束！！ 建议关注本专栏，以获得文章更新的最新消息哦！！ 🐱‍🏍🐱‍🏍
