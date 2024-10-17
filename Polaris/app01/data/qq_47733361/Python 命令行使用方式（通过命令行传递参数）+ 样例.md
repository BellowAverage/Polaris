
--- 
title:  Python 命令行使用方式（通过命令行传递参数）+ 样例 
tags: []
categories: [] 

---
### 一、引入相关库

与命令行相关的库有两个：

```
import getopt
import sys

```

### 二、使用样例

```
def main(argv):
    try:
        savePath = 'image.png'
        filenamePES = None
        x = None # 0
        y = None # 2
        opts, args = getopt.getopt(argv, "f:x:y:s:")
        for opt, arg in opts:
            if opt in ("-f"):
                filenamePES = arg
            elif opt in ("-x"):
                x = int(arg)
            elif opt in ("-y"):
                y = int(arg)
            elif opt in ("-s"):
                savePath = arg
        
        print("The filename is %s, the X-axis represents column %d of the file, and the Y-axis represents column %d of the file.", filenamePES, x, y)
        print("The picture save path is %s", savePath)

        while True:
            realTimeLine(filenamePES, x, y, savePath)

    except getopt.GetoptError:
        print(f"usage: {<!-- -->sys.argv[0]} -f &lt;filenamePath&gt; -x &lt;X-axis&gt; -y &lt;Y-axis&gt; -s &lt;savePath&gt;")
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])

```

**命令行传递：**

```
./test.py -f /home/test/test.log -x 0 -y 0 -s ./image.png

```

如上述代码：
- 使用 sys.argv 可以获取到命令行输入的参数；- argv[0] 默认为 ./test.py；因此我们所传递的参数是从 argv[1] 开始；- 在main函数中使用 getopt.getopt() 方法，传递两个参数，第一个为命令行相关，第二个为相关短选项，初始化命令行解析方法；