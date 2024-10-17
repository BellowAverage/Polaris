
--- 
title:  vscode 调试使用 make 编译的项目 
tags: []
categories: [] 

---
###### **1、首先点击运行 --&gt; 启动调试：**

<img src="https://img-blog.csdnimg.cn/18c2bf060b904854adc7b7cef3d9ea7d.png" alt="在这里插入图片描述">

###### **2、选择g++或gcc生成和调试活动文件：**

<img src="https://img-blog.csdnimg.cn/ccc811cd5b9d46e787685ee9402dc76e.png" alt="在这里插入图片描述">

###### **3、出现下面提示是正常的，点击仍要调试：**

<img src="https://img-blog.csdnimg.cn/2c9061b5d41648839dbb43bc1adb3ba4.png" alt="在这里插入图片描述"> 点击打开“launch.json”： <img src="https://img-blog.csdnimg.cn/0ca8ceb1c62d4136a4a5f9c55e928969.png" alt="在这里插入图片描述">

###### **4、此时会在项目工作目录下生成tsak.josn和launch.json文件：**

如下，下面为默认生成的内容，我们需要根据项目情况来修改： **task.json文件：**

```
{<!-- -->
    "tasks": [
        {<!-- -->
            "type": "cppbuild",
            "label": "C/C++: g++ 生成活动文件",
            "command": "/usr/bin/g++",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "options": {<!-- -->
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {<!-- -->
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ],
    "version": "2.0.0"
}

```

**launch.json文件：**

```
{<!-- -->
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": []
}

```

###### 5、修改task.json与launch.json文件

若项目工作空间为 Test，并且Test 下有个目录为 MyProject，其中存放 Makefile 等文件； **首先修改tsak.json文件：** ${workspaceFolder} 代表工作空间 Test，make 命令应该在 Makefile 同级目录下使用，则cwd应按下面方式修改：

```
{<!-- -->
    "tasks": [
        {<!-- -->
            "type": "shell",
            "label": "build MyProject",
            "command": "make",
            "options": {<!-- -->
                "cwd": "${workspaceFolder}/MyProject"
            },
            "group": "build"
        }
    ],
    "version": "2.0.0"
}

```

**修改launch.json文件：** launch.json文件需要修改
- program：可执行文件；- preLaunchTask：同tsak.josn中lable内容需要保持相同；
```
{<!-- -->
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {<!-- -->
            "name": "(gdb) 启动",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/MyProject/bin/MyProject",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {<!-- -->
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                },
                {<!-- -->
                    "description": "将反汇编风格设置为 Intel",
                    "text": "-gdb-set disassembly-flavor intel",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "build MyProject"
        }
    ]
}

```
