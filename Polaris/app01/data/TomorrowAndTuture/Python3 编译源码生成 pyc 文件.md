
--- 
title:  Python3 编译源码生成 pyc 文件 
tags: []
categories: [] 

---
### python3 -m compileall . 

这种方式会将生成的 pyc 文件放到和 py 文件同目录下的 __pycache__ 目录下面，而不是和 py 文件同目录，而且 pyc 文件中间部分会插入解释器版本，比如这儿的 cpython-36。

```
[root@master learning_log]# pwd
/root/learning_log
[root@master learning_log]# ls
db.sqlite3  learning_log  learning_logs  manage.py  users

[root@master learning_log]# python3 -m compileall .
Listing '.'...
Listing './.git'...
Listing './.git/branches'...
...

[root@master learning_log]# find . -name '__pycache__'
./learning_log/__pycache__
./learning_logs/migrations/__pycache__
./learning_logs/__pycache__
./users/migrations/__pycache__
./users/__pycache__
./__pycache__

[root@master learning_log]# find . -name '*.pyc'
./learning_log/__pycache__/__init__.cpython-36.pyc
./learning_log/__pycache__/settings.cpython-36.pyc
./learning_log/__pycache__/urls.cpython-36.pyc
./learning_log/__pycache__/wsgi.cpython-36.pyc
./learning_log/__pycache__/asgi.cpython-36.pyc
./learning_logs/migrations/__pycache__/0001_initial.cpython-36.pyc
./learning_logs/migrations/__pycache__/0002_entry.cpython-36.pyc
./learning_logs/migrations/__pycache__/__init__.cpython-36.pyc
./learning_logs/migrations/__pycache__/0003_topic_owner.cpython-36.pyc
...

[root@master learning_log]# find . -name '__pycache__' | xargs rm -rf
```

### python3 -m compileall -b . 

编译打包，用这个命令简直是太实用了。

添加 -b 参数的话，会将编译生成的 pyc 文件放到和 py 文件同目录下。删掉 .py 的源码文件，剩下的就是编译好的 pyc 文件了。

```
[root@master learning_log]# python3 -m compileall -b .
Listing '.'...
Listing './.git'...
Listing './.git/branches'...
...

[root@master learning_log]# find . -name '*.pyc'
./learning_log/__init__.pyc
./learning_log/asgi.pyc
./learning_log/settings.pyc
./learning_log/urls.pyc
./learning_log/wsgi.pyc
...

[root@master learning_log]# find . -name '*.py' | xargs rm -f

[root@master ~]# tar -czvf learning_log.tar.gz learning_log/
learning_log/
learning_log/learning_log/
learning_log/learning_log/__init__.pyc
learning_log/learning_log/asgi.pyc
learning_log/learning_log/settings.pyc
learning_log/learning_log/urls.pyc
learning_log/learning_log/wsgi.pyc
...

[root@master ~]# ll learning_log.tar.gz 
-rw-r--r--. 1 root root 169853 Mar 20 15:09 learning_log.tar.gz
```

假如你不想敲那么多命令，可以像下面那样写个简单的 Shell 脚本，也是很方便的（记得添加可执行权限）。

```
#!/usr/bin/env bash
python3 -m compileall -b $1
find $1 -name '*.py' | xargs rm -f
tar -czvf "$1.tar.gz" $1
```

```
[root@master ~]# ./test.sh learning_log
Listing './learning_log/'...
Listing './learning_log/.git'...
...

[root@master ~]# ll learning_log.tar.gz 
-rw-r--r--. 1 root root 171763 Mar 20 18:32 learning_log.tar.gz

```

 
