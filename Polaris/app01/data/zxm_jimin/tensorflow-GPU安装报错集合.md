
--- 
title:  tensorflow-GPU安装报错集合 
tags: []
categories: [] 

---
最后成功运行环境 **Anaconda2+cuda8.0+cudnn v5.1+tensorflow-gpu1.0.1**

## **错误一：import tensorflow报错：**

```
Traceback (most recent call last):
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 18, in swig_import_helper
    return importlib.import_module(mname)
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 986, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 969, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 958, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 666, in _load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 577, in module_from_spec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 906, in create_module
  File "&lt;frozen importlib._bootstrap&gt;", line 222, in _call_with_frames_removed
ImportError: DLL load failed: 找不到指定的模块。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 41, in &lt;module&gt;
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 21, in &lt;module&gt;
    _pywrap_tensorflow_internal = swig_import_helper()
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 20, in swig_import_helper
    return importlib.import_module('_pywrap_tensorflow_internal')
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ImportError: No module named '_pywrap_tensorflow_internal'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\__init__.py", line 24, in &lt;module&gt;
    from tensorflow.python import *
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\__init__.py", line 49, in &lt;module&gt;
    from tensorflow.python import pywrap_tensorflow
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 52, in &lt;module&gt;
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 18, in swig_import_helper
    return importlib.import_module(mname)
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 986, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 969, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 958, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 666, in _load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 577, in module_from_spec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 906, in create_module
  File "&lt;frozen importlib._bootstrap&gt;", line 222, in _call_with_frames_removed
ImportError: DLL load failed: 找不到指定的模块。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 41, in &lt;module&gt;
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 21, in &lt;module&gt;
    _pywrap_tensorflow_internal = swig_import_helper()
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\site-packages\tensorflow\python\pywrap_tensorflow_internal.py", line 20, in swig_import_helper
    return importlib.import_module('_pywrap_tensorflow_internal')
  File "D:\Program Files (x86)\Anaconda3\envs\gputf\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ImportError: No module named '_pywrap_tensorflow_internal'


Failed to load the native TensorFlow runtime.

```

我的个人经验：tensorflow-gpu版本的问题，建议去查看相应环境下到底支持哪个版本的tensorflow-gpu 我是Anaconda2+cuda8.0+cudnn6.0+tensorflow-gpu1.3.0,报错！ 官网建议是装1.4.0和1.3.0 从1.4.0一直尝试到1.1.0,统统报错。 降到**1.0.1**终于不报错了，但是又出现错误2。

<img src="https://img-blog.csdnimg.cn/2019071000032255." alt="在这里插入图片描述">

## **错误二：cudnn DSO不能生成**

```
Check failed: s.ok() could not find cudnnCreate in cudnn DSO; dlerror: cudnnCreate not found
Process finished with exit code -1073740791 (0xC0000409)

```

一开始以为是Anaconda2版本过低，又装了Anaconda3，但是发现还是一样的错。 最后其实Anaconda的版本无关。 是依赖库有问题 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\bin下 dll文件有缺失， <img src="https://img-blog.csdnimg.cn/20190710110953380." alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190710111034156." alt="在这里插入图片描述"> **解决：** 抓一个成功安装并成功运行的小伙伴（版本要最好是一样的）的bin里面的文件全部靠过来，相同的直接替代。 <img src="https://img-blog.csdnimg.cn/20190710002418765.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/2019071000245958.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 应该要有这些。运行后报错误三。

## **错误三：import tensorflow报错，运行时报错Check failed: stream-&gt;parent()-&gt;GetConvolveAlgorithms(&amp;algorithms)**

```
Loaded runtime CuDNN library: 5005 (compatibility version 5000) but source was compiled with 5110 (compatibility version 5100).  If using a binary install, upgrade your CuDNN library to match.  If building from sources, make sure the library loaded at runtime matches a compatible version specified during compile configuration.
F tensorflow/core/kernels/conv_ops.cc:605] Check failed: stream-&gt;parent()-&gt;GetConvolveAlgorithms(&amp;algorithms) 

```

参考博客：https://blog.csdn.net/u010099080/article/details/57405184

**解决：**

从报错信息很明显可以看出，是 cuDNN 的版本问题，那么我只需要升级 cuDNN 版本就可以了。我现在的版本是 5.0，升级到 5.1 即可。可从 官网 下载或者从 这里 直接下载我下载好的。

下载好后就是替换原有的 5.0 版本了。如果原先你安装 cuDNN 的时候是用将 C:\cuda\bin 加进 Path 环境变量的方法安装的，那么你直接用 5.1 版本文件替换原有文件应该就可以。

成功运行啦！
