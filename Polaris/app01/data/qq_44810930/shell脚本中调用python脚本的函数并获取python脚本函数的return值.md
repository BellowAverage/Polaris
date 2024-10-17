
--- 
title:  shell脚本中调用python脚本的函数并获取python脚本函数的return值 
tags: []
categories: [] 

---
**1. 编写Python脚本**

假设你有一个Python脚本`example.py`，其中包含一个名为`my_function`的函数，并且你希望在Shell脚本中调用这个函数并获取其返回值。示例Python脚本如下：

```
# example.py

def my_function():
    return "Hello from Python"

```

**2. 编写Shell脚本**

现在，你可以编写一个Shell脚本`run_python.sh`，在其中调用Python脚本中的函数并获取其返回值。示例Shell脚本如下：

```
#!/bin/bash

# 调用Python脚本并获取返回值
output=$(python - &lt;&lt;END
import example
print(example.my_function())
END
)

echo "Python函数的返回值为: $output"

```

在这个Shell脚本中，我们使用了`python - &lt;&lt;END`的形式，它允许在Shell脚本中嵌入Python代码。

在嵌入的Python代码中，我们导入了`example`模块并调用了其中的`my_function`函数，然后将其输出作为Shell变量`output`的值。

**3. 运行Shell脚本**

现在，你可以在Shell中运行`run_python.sh`脚本，它会调用Python脚本中的函数并打印出返回值。

```
bash run_python.sh

```

当你运行Shell脚本后，你应该能够看到从Python函数中获取的返回值被打印出来。

```
$ sh run_python.sh 
Python函数的返回值为: Hello from Python

```
