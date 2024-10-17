
--- 
title:  opengl pyqt 显示文字 
tags: []
categories: [] 

---
**目录**





### 效果图

<img alt="" height="144" src="https://img-blog.csdnimg.cn/direct/6cdfdd9077cd44da95b42825f629b9b3.png" width="219">

```

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)

    def initializeGL(self):
        glClearColor(0, 0, 0, 0)
        glEnable(GL_DEPTH_TEST)
        glutInit()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 1, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-1.5, 0.0, -6)

        # 使用GLUT渲染数字
        glColor3f(1.0, 1.0, 1.0)  # 设置数字颜色
        glRasterPos2f(0, 0)  # 设置数字位置
        for char in "123":
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(OpenGLWidget(self))
        self.setWindowTitle("PyQt OpenGL Example")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```


