
--- 
title:  python3 -m pip install --user pipx报错解决 
tags: []
categories: [] 

---
root@linux:~# python3 -m pip install --user pipx Traceback (most recent call last):   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main     return _run_code(code, main_globals, None,   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code     exec(code, run_globals)   File "/usr/lib/python3/dist-packages/pip/__main__.py", line 16, in &lt;module&gt;     from pip._internal.cli.main import main as _main  # isort:skip # noqa   File "/usr/lib/python3/dist-packages/pip/_internal/cli/main.py", line 10, in &lt;module&gt;     from pip._internal.cli.autocompletion import autocomplete   File "/usr/lib/python3/dist-packages/pip/_internal/cli/autocompletion.py", line 9, in &lt;module&gt;     from pip._internal.cli.main_parser import create_main_parser   File "/usr/lib/python3/dist-packages/pip/_internal/cli/main_parser.py", line 7, in &lt;module&gt;     from pip._internal.cli import cmdoptions   File "/usr/lib/python3/dist-packages/pip/_internal/cli/cmdoptions.py", line 19, in &lt;module&gt;     from distutils.util import strtobool ModuleNotFoundError: No module named 'distutils.util'  

## **解决**

**方法一**

如果重新安装pip时出现错误，你可以尝试手动下载并安装pip。首先，使用以下命令下载pip的tarball文件

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

```

然后，使用以下命令安装pip

```
python3 get-pip.py --user

```

重新执行指令，成功

```
python3 -m pip install --user pipx
```

**方法二**

如果仍然无法解决问题，你可以尝试重新安装Python

```
sudo apt-get remove python3
sudo apt-get install python3

```


