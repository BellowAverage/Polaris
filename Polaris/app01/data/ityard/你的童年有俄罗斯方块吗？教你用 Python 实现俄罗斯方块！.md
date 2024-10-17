
--- 
title:  你的童年有俄罗斯方块吗？教你用 Python 实现俄罗斯方块！ 
tags: []
categories: [] 

---
在那个电子产品比较匮乏的年代，小游戏机

<img src="https://img-blog.csdnimg.cn/20191111204505955.gif" alt="">

还是为数不多的游戏类电子产品，对小孩子更是有着不可抗拒的魔力，在当时如果哪个小孩买了一个小游戏机，大伙一定迅速围上去…

<img src="https://img-blog.csdnimg.cn/20191111211702738.jpg" alt="">

俄罗斯方块作为其中一款小游戏，尽管规则简单、只有黑白双色，但其对当时游戏玩家的影响丝毫不亚于 LOL、农药、吃鸡对现在游戏玩家的影响，下面我们来看一下如何用 Python 实现俄罗斯方块这款小游戏。

### 规则

>  
 由小方块组成的不同形状的板块陆续从屏幕上方落下来，玩家通过调整板块的位置和方向，使它们在屏幕底部拼出完整的一条或几条。这些完整的横条会随即消失，给新落下来的板块腾出空间，与此同时，玩家得到分数奖励。没有被消除掉的方块不断堆积起来，一旦堆到屏幕顶端，玩家便告输，游戏结束。 — **百度百科** 


### 环境
- **操作系统**：Windows- **Python 版本**：3.6- **涉及模块**：sys、random、PyQt5
### 实现

首先安装第三方模块 PyQt5，使用 `pip install PyQt5` 即可。

➢ **游戏主界面**

实现代码

```
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class MainBoard(QFrame):
    msg = pyqtSignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300
    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()
    def initBoard(self):
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []
        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False

```

效果图如下

<img src="https://img-blog.csdnimg.cn/20191113081358253.png#pic_" alt="" height="500">

➢ **小板块**

定义小版块的形状

```
class ShapeForm(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class Shape(object):
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = ShapeForm.NoShape
        self.setShape(ShapeForm.NoShape)

```

画出图形

```
def drawSquare(self, painter, x, y, shape):
    colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                  0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
    color = QColor(colorTable[shape])
    painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
        self.squareHeight() - 2, color)
    painter.setPen(color.lighter())
    painter.drawLine(x, y + self.squareHeight() - 1, x, y)
    painter.drawLine(x, y, x + self.squareWidth() - 1, y)
    painter.setPen(color.darker())
    painter.drawLine(x + 1, y + self.squareHeight() - 1,
        x + self.squareWidth() - 1, y + self.squareHeight() - 1)
    painter.drawLine(x + self.squareWidth() - 1,
        y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

```

效果图如下

<img src="https://img-blog.csdnimg.cn/2019111320040240.PNG" alt="">

➢ **按键事件**

```
    def keyPressEvent(self, event):
        if not self.isStarted or self.curPiece.shape() == ShapeForm.NoShape:
            super(MainBoard, self).keyPressEvent(event)
            return
        key = event.key()
        if key == Qt.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
        elif key == Qt.Key_Space:
            self.dropDown()
        elif key == Qt.Key_D:
            self.oneLineDown()
        else:
            super(MainBoard, self).keyPressEvent(event)

    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x &lt; 0 or x &gt;= MainBoard.BoardWidth or y &lt; 0 or y &gt;= MainBoard.BoardHeight:
                return False
            if self.shapeAt(x, y) != ShapeForm.NoShape:
                return False
        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        return True

```

➢ **计时器事件**

```
def timerEvent(self, event):
    if event.timerId() == self.timer.timerId():
        if self.isWaitingAfterLine:
            self.isWaitingAfterLine = False
            self.newPiece()
        else:
            self.oneLineDown()
    else:
        super(MainBoard, self).timerEvent(event)

```

➢ **开始和暂停**

```
    def start(self):
        if self.isPaused:
            return
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        self.msg.emit(str(self.numLinesRemoved))
        self.newPiece()
        self.timer.start(MainBoard.Speed, self)

    def pause(self):
        if not self.isStarted:
            return
        self.isPaused = not self.isPaused
        if self.isPaused:
            self.timer.stop()
            self.msg.emit("paused")
        else:
            self.timer.start(MainBoard.Speed, self)
            self.msg.emit(str(self.numLinesRemoved))
        self.update()

```

➢ **游戏类及初始化**

```
class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tboard = MainBoard(self)
        self.setCentralWidget(self.tboard)
        self.statusbar = self.statusBar()
        self.tboard.msg[str].connect(self.statusbar.showMessage)
        self.tboard.start()
        self.resize(300, 500)
        self.center()
        self.setWindowTitle('俄罗斯方块')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)

```

启动

```
if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())

```

最终效果

<img src="https://img-blog.csdnimg.cn/20191113213501428.PNG#pic_" alt="" height="500">

### 打包

为了方便运行，我们将 Python 文件打成 exe 文件，用到的插件为 pyinstaller。

首先，安装 pyinstaller，使用 `pip install pyinstaller` 即可。 安装完成后，在文件目录

<img src="https://img-blog.csdnimg.cn/20191114080622448.PNG" alt="">

打开命令窗口，在命令窗口执行命令 `pyinstaller --onefile --nowindowed --icon="C:\Users\LE\Desktop\tetris\tetris.ico" tetris.py` 即可。执行完成后，我们到 dist 目录下

<img src="https://img-blog.csdnimg.cn/20191114080637412.PNG" alt=""> 即可找到生成的 exe 文件。

**完整代码 + PyQt5 学习资料** 请关注文末公众号，后台回复 **g1** 获取。

<img src="https://img-blog.csdnimg.cn/20191118111747841.jpg#pic_center" alt="" width="600">
