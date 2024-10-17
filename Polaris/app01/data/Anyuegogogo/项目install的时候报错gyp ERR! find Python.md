
--- 
title:  项目install的时候报错gyp ERR! find Python 
tags: []
categories: [] 

---
**报错信息**

```
npm ERR! code 1
npm ERR! path D:\My\StudyCode\vue-typescript-admin-template\node_modules\deasync
npm ERR! command failed
npm ERR! command C:\Windows\system32\cmd.exe /d /s /c node ./build.js
npm ERR! gyp info it worked if it ends with ok
npm ERR! gyp info using node-gyp@8.4.1
npm ERR! gyp info using node@16.14.2 | win32 | x64
npm ERR! gyp ERR! find Python
npm ERR! gyp ERR! find Python checking Python explicitly set from command line or npm configuration
npm ERR! gyp ERR! find Python - "--python=" or "npm config get python" is "python2.7"
npm ERR! gyp ERR! find Python - "python2.7" is not in PATH or produced an error
npm ERR! gyp ERR! find Python Python is not set from environment variable PYTHON
npm ERR! gyp ERR! find Python checking if "python3" can be used
npm ERR! gyp ERR! find Python - "python3" is not in PATH or produced an error
npm ERR! gyp ERR! find Python checking if "python" can be used
npm ERR! gyp ERR! find Python - "python" is not in PATH or produced an error
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python39\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python39\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python39\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python39\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python39-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python39-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python39-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python39-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files (x86)\Python39-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files (x86)\Python39-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python38\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python38\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python38-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python38-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python38-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python38-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files (x86)\Python38-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files (x86)\Python38-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python37\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python37\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python37-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python37-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files (x86)\Python37-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files (x86)\Python37-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python36\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python36\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python36\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python36\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files\Python36-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files\Python36-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if Python is C:\Program Files (x86)\Python36-32\python.exe
npm ERR! gyp ERR! find Python - "C:\Program Files (x86)\Python36-32\python.exe" could not be run
npm ERR! gyp ERR! find Python checking if the py launcher can be used to find Python 3
npm ERR! gyp ERR! find Python - "py.exe" is not in PATH or produced an error
npm ERR! gyp ERR! find Python
npm ERR! gyp ERR! find Python **********************************************************
npm ERR! gyp ERR! find Python You need to install the latest version of Python.
npm ERR! gyp ERR! find Python Node-gyp should be able to find and use Python. If not,
npm ERR! gyp ERR! find Python you can try one of the following options:
npm ERR! gyp ERR! find Python - Use the switch --python="C:\Path\To\python.exe"
npm ERR! gyp ERR! find Python   (accepted by both node-gyp and npm)
npm ERR! gyp ERR! find Python - Set the environment variable PYTHON
npm ERR! gyp ERR! find Python - Set the npm configuration variable python:
npm ERR! gyp ERR! find Python   npm config set python "C:\Path\To\python.exe"
npm ERR! gyp ERR! find Python For more information consult the documentation at:
npm ERR! gyp ERR! find Python https://github.com/nodejs/node-gyp#installation
npm ERR! gyp ERR! find Python **********************************************************
npm ERR! gyp ERR! find Python
npm ERR! gyp ERR! configure error
npm ERR! gyp ERR! stack Error: Could not find any Python installation to use
npm ERR! gyp ERR! stack     at PythonFinder.fail (C:\Users\Administrator\AppData\Roaming\nvm\v16.14.2\node_modules\npm\node_modules\node-gyp\lib\find-python.js:330:47)        
npm ERR! gyp ERR! stack     at PythonFinder.&lt;anonymous&gt; (C:\Users\Administrator\AppData\Roaming\nvm\v16.14.2\node_modules\npm\node_modules\node-gyp\lib\find-python.js:228:18) 
npm ERR! gyp ERR! stack     at exithandler (node:child_process:406:5)
npm ERR! gyp ERR! stack     at ChildProcess.emit (node:events:526:28)
npm ERR! gyp ERR! stack     at Process.ChildProcess._handle.onexit (node:internal/child_process:289:12)
npm ERR! gyp ERR! stack     at onErrorNT (node:internal/child_process:478:16)
npm ERR! gyp ERR! System Windows_NT 10.0.18363
e-gyp.js" "rebuild"                                                                                                                                                            e-gyp.js" "rebuild"       
npm ERR! gyp ERR! node -v v16.14.2
npm ERR! gyp ERR! node-gyp -v v8.4.1
npm ERR! gyp ERR! not ok
npm ERR! Build failed

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\Administrator\AppData\Local\npm-cache\_logs\2022-12-16T07_51_14_042Z-debug-0.log

```

在网上找了许多方法，大部分是下载python，但是没啥用（试过了，至少对我没用）。 **其实真正的问题是node版本不兼容，下载项目中需要的node版本就行。** 如何知道自己的项目中匹配的是哪个node版本呢 **1、package.json**

```
"@types/node": "^14.14.37",

```

**2、如果项目有用yarn，也可以查看yarn.lock**

```
"@types/node@*", "@types/node@^14.14.37":
  version "14.14.41"

```
