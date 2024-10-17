
--- 
title:  《Python笔记》安装(pip)第三方包报错 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - <ul><li>- - - - - 


### Python版本

```
$ python
Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; exit()

```

### 报错信息

#### pip 安装numpy报错

<img src="https://img-blog.csdnimg.cn/9531e56c2f8745fdb635ebb6e0e2a110.png" alt="在这里插入图片描述">

```
$ pip install numpy
Looking in indexes: 
Collecting numpy
  Using cached /numpy-1.22.4.zip
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Building wheels for collected packages: numpy
  Building wheel for numpy (PEP 517) ... error
  Complete output from command 
  Processing numpy/random\_bounded_integers.pxd.in
  Processing numpy/random\bit_generator.pyx
  Processing numpy/random\mtrand.pyx
  Processing numpy/random\_bounded_integers.pyx.in
  Processing numpy/random\_common.pyx
  Processing numpy/random\_generator.pyx
  Processing numpy/random\_mt19937.pyx
  Processing numpy/random\_pcg64.pyx
  Processing numpy/random\_philox.pyx
  Processing numpy/random\_sfc64.pyx
  Cythonizing sources
  INFO: blas_opt_info:
  INFO: blas_armpl_info:
  INFO: No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
  INFO: customize MSVCCompiler
  INFO:   libraries armpl_lp64_mp not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: blas_mkl_info:
  INFO:   libraries mkl_rt not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: blis_info:
  INFO:   libraries blis not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: openblas_info:
  INFO:   libraries openblas not found in ['\\lib', 'C:\\']
  INFO: get_default_fcompiler: matching types: '['gnu', 'intelv', 'absoft', 'compaqv', 'intelev', 'gnu95', 'g95', 'intelvem', 'intelem', 'flang']'
  INFO: customize GnuFCompiler
  WARN: Could not locate executable g77
  WARN: Could not locate executable f77
  INFO: customize IntelVisualFCompiler
  WARN: Could not locate executable ifort
  WARN: Could not locate executable ifl
  INFO: customize AbsoftFCompiler
  WARN: Could not locate executable f90
  INFO: customize CompaqVisualFCompiler
  INFO: Found executable C:\Program Files\Git\usr\bin\DF.exe
  WARN: Could not locate executable C:\Program
  INFO: customize IntelItaniumVisualFCompiler
  WARN: Could not locate executable efl
  INFO: customize Gnu95FCompiler
  WARN: Could not locate executable gfortran
  WARN: Could not locate executable f95
  INFO: customize G95FCompiler
  WARN: Could not locate executable g95
  INFO: customize IntelEM64VisualFCompiler
  INFO: customize IntelEM64TFCompiler
  WARN: Could not locate executable efort
  WARN: Could not locate executable efc
  INFO: customize PGroupFlangCompiler
  WARN: Could not locate executable flang
  WARN: don't know how to compile Fortran code on platform 'nt'
  INFO:   NOT AVAILABLE
  INFO:
  INFO: accelerate_info:
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_blas_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries tatlas not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_blas_info:
  INFO:   libraries satlas not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_blas_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries ptf77blas,ptcblas,atlas not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_blas_info:
  INFO:   libraries f77blas,cblas,atlas not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: blas_info:
  INFO:   libraries blas not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: blas_src_info:
  INFO:   NOT AVAILABLE
  INFO:
  INFO:   NOT AVAILABLE
  INFO:
  non-existing path in 'numpy\\distutils': 'site.cfg'
  INFO: lapack_opt_info:
  INFO: lapack_armpl_info:
  INFO:   libraries armpl_lp64_mp not found in ['\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: lapack_mkl_info:
  INFO:   libraries mkl_rt not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: openblas_lapack_info:
  INFO:   libraries openblas not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: openblas_clapack_info:
  INFO:   libraries openblas,lapack not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: flame_info:
  INFO:   libraries flame not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries tatlas,tatlas not found in \lib
  INFO:   libraries tatlas,tatlas not found in C:\
  INFO: &lt;class 'numpy.distutils.system_info.atlas_3_10_threads_info'&gt;
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_info:
  INFO:   libraries satlas,satlas not found in \lib
  INFO:   libraries satlas,satlas not found in C:\
  INFO: &lt;class 'numpy.distutils.system_info.atlas_3_10_info'&gt;
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries ptf77blas,ptcblas,atlas not found in \lib
  INFO:   libraries ptf77blas,ptcblas,atlas not found in C:\
  INFO: &lt;class 'numpy.distutils.system_info.atlas_threads_info'&gt;
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_info:
  INFO:   libraries f77blas,cblas,atlas not found in \lib
  INFO:   libraries f77blas,cblas,atlas not found in C:\
  INFO: &lt;class 'numpy.distutils.system_info.atlas_info'&gt;
  INFO:   NOT AVAILABLE
  INFO:
  INFO: lapack_info:
  INFO:   libraries lapack not found in ['\\lib', 'C:\\']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: lapack_src_info:
  INFO:   NOT AVAILABLE
  INFO:
  INFO:   NOT AVAILABLE
  INFO:
  INFO: numpy_linalg_lapack_lite:
  INFO:   FOUND:
  INFO:     language = c
  INFO:     define_macros = [('HAVE_BLAS_ILP64', None), ('BLAS_SYMBOL_SUFFIX', '64_')]
  INFO:
  running bdist_wheel
  running build
  running config_cc
  INFO: unifing config_cc, config, build_clib, build_ext, build commands --compiler options
  running config_fc
  INFO: unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
  running build_src
  INFO: build_src
  INFO: building py_modules sources
  creating build
  creating build\src.win-amd64-3.8
  creating build\src.win-amd64-3.8\numpy
  creating build\src.win-amd64-3.8\numpy\distutils
  INFO: building library "npymath" sources
  Running from numpy source directory.
  \pip-install-trxrwr8e\numpy\numpy\distutils\system_info.py:2077: UserWarning:
      Optimized (vendor) Blas libraries are not found.
      Falls back to netlib Blas library which has worse performance.
      A better performance should be easily gained by switching
      Blas library.
    if self._calc_info(blas):
 \pip-install-trxrwr8e\numpy\numpy\distutils\system_info.py:2077: UserWarning:
      Blas (http://www.netlib.org/blas/) libraries not found.
      Directories to search for the libraries can be specified in the
      numpy/distutils/site.cfg file (section [blas]) or by setting
      the BLAS environment variable.
    if self._calc_info(blas):
 pip-install-trxrwr8e\numpy\numpy\distutils\system_info.py:2077: UserWarning:
      Blas (http://www.netlib.org/blas/) sources not found.
      Directories to search for the sources can be specified in the
      numpy/distutils/site.cfg file (section [blas_src]) or by setting
      the BLAS_SRC environment variable.
    if self._calc_info(blas):
pip-install-trxrwr8e\numpy\numpy\distutils\system_info.py:1902: UserWarning:
      Lapack (http://www.netlib.org/lapack/) libraries not found.
      Directories to search for the libraries can be specified in the
      numpy/distutils/site.cfg file (section [lapack]) or by setting
      the LAPACK environment variable.
    return getattr(self, '_calc_info_{}'.format(name))()
 \numpy\numpy\distutils\system_info.py:1902: UserWarning:
      Lapack (http://www.netlib.org/lapack/) sources not found.
      Directories to search for the sources can be specified in the
      numpy/distutils/site.cfg file (section [lapack_src]) or by setting
      the LAPACK_SRC environment variable.
    return getattr(self, '_calc_info_{}'.format(name))()
  Warning: attempted relative import with no known parent package
 \lib\distutils\dist.py:274: UserWarning: Unknown distribution option: 'define_macros'
    warnings.warn(msg)
  error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

  ----------------------------------------
  Failed building wheel for numpy
  Running setup.py clean for numpy
  Complete output from command \Scripts\python.exe -u -c "import setuptools, tokenize;__file__='
  \\pip-install-  trxrwr8e\\numpy\\setup.py';
  f=getattr(tokenize, 'open', open)(__file__);
  code=f.read().replace('\r\n', '\n');
  f.close();exec(compile(code, __file__, 'exec')
)" clean --all:
  Running from numpy source directory.

  `setup.py clean` is not supported, use one of the following instead:

    - `git clean -xdf` (cleans all files)
    - `git clean -Xdf` (cleans all versioned files, doesn't touch
                        files that aren't checked into the git repo)

  Add `--force` to your command to use it anyway if you must (unsupported).


  ----------------------------------------
  Failed cleaning build dir for numpy
Failed to build numpy
Could not build wheels for numpy which use PEP 517 and cannot be installed directly

```

从报错内容看疑似编译环境问题 https://wiki.python.org/moin/WindowsCompilers

#### pip 安装 scipy报错

```
$ pip install scipy
Looking in indexes: 
Collecting scipy
  Using cached /scipy-1.8.1.tar.gz
  Installing build dependencies ... error
  Complete output from command \Scripts\python.exe \lib\site-packages\pip-19
.0.3-py3.8.egg\pip install --ignore-installed --no-user --prefix 
\pip-build-env-iogzj8v9\overlay --no-warn-script-location --no-binary :none: -
-only-binary :none:  --trusted-host  -- wheel&lt;0.38.0 setuptools&lt;60.0.0 Cython&gt;=0.29.18,&lt;3.0 pybind
11&gt;=2.4.3,&lt;2.9.0 pythran&gt;=0.10.0,&lt;0.11.0 "numpy==1.19.2; python_version=='3.8' and platform_machine=='aarch64' and platform_python_implementation != 'PyPy'" "numpy==1.20.0; p
ython_version=='3.8' and platform_machine=='arm64' and platform_system=='Darwin'" "numpy==1.20.0; python_version=='3.9' and platform_machine=='arm64' and platform_system=='Da
rwin'" "numpy==1.17.5; python_version=='3.8' and platform_machine=='s390x' and platform_python_implementation != 'PyPy'" "numpy==1.17.3; python_version=='3.8' and (platform_m
achine!='arm64' or platform_system!='Darwin') and platform_machine!='aarch64' and platform_machine!='s390x' and platform_python_implementation != 'PyPy'" "numpy==1.19.3; pyth
on_version=='3.9' and (platform_machine!='arm64' or platform_system!='Darwin') and platform_python_implementation != 'PyPy'" "numpy==1.21.4; python_version=='3.10' and platfo
rm_python_implementation != 'PyPy'" "numpy; python_version&gt;='3.11'" "numpy; python_version&gt;='3.8' and platform_python_implementation=='PyPy'":
  Ignoring numpy: markers 'python_version == "3.8" and platform_machine == "aarch64" and platform_python_implementation != "PyPy"' don't match your environment
  Ignoring numpy: markers 'python_version == "3.8" and platform_machine == "arm64" and platform_system == "Darwin"' don't match your environment
  Ignoring numpy: markers 'python_version == "3.9" and platform_machine == "arm64" and platform_system == "Darwin"' don't match your environment
  Ignoring numpy: markers 'python_version == "3.8" and platform_machine == "s390x" and platform_python_implementation != "PyPy"' don't match your environment
  Ignoring numpy: markers 'python_version == "3.9" and (platform_machine != "arm64" or platform_system != "Darwin") and platform_python_implementation != "PyPy"' don't match
your environment
  Ignoring numpy: markers 'python_version == "3.10" and platform_python_implementation != "PyPy"' don't match your environment
  Ignoring numpy: markers 'python_version &gt;= "3.11"' don't match your environment
  Ignoring numpy: markers 'python_version &gt;= "3.8" and platform_python_implementation == "PyPy"' don't match your environment
  Looking in indexes: 
  Collecting wheel&lt;0.38.0
    Using cached /wheel-0.37.1-py2.py3-none-any.whl
  Collecting setuptools&lt;60.0.0
    Using cached /setuptools-59.8.0-py3-none-any.whl
  Collecting Cython&lt;3.0,&gt;=0.29.18
    Using cached /Cython-0.29.30-py2.py3-none-any.whl
  Collecting pybind11&lt;2.9.0,&gt;=2.4.3
    Using cached /pybind11-2.8.1-py2.py3-none-any.whl
  Collecting pythran&lt;0.11.0,&gt;=0.10.0
    Using cached /pythran-0.10.0-py3-none-any.whl
  Collecting numpy==1.17.3
    Using cached /numpy-1.17.3.zip
  Collecting ply&gt;=3.4 (from pythran&lt;0.11.0,&gt;=0.10.0)
    Using cached /ply-3.11-py2.py3-none-any.whl
  Collecting gast~=0.5.0 (from pythran&lt;0.11.0,&gt;=0.10.0)
    Using cached /gast-0.5.3-py3-none-any.whl
  Collecting beniget~=0.4.0 (from pythran&lt;0.11.0,&gt;=0.10.0)
    Using cached /beniget-0.4.1-py3-none-any.whl
  Building wheels for collected packages: numpy
    Building wheel for numpy (setup.py): started
    Building wheel for numpy (setup.py): finished with status 'error'
    Complete output from command \Scripts\python.exe -u -c "import setuptools, tokenize;__file__='\\pip-install-szyxpo9w\\numpy\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec
'))" bdist_wheel -d C:\pip-wheel-czsqh5ng --python-tag cp38:
    Running from numpy source directory.
    blas_opt_info:
    blas_mkl_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries mkl_rt not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    blis_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries blis not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    openblas_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries openblas not found in ['\\lib', 'C:\\']
    get_default_fcompiler: matching types: '['gnu', 'intelv', 'absoft', 'compaqv', 'intelev', 'gnu95', 'g95', 'intelvem', 'intelem', 'flang']'
    customize GnuFCompiler
    Could not locate executable g77
    Could not locate executable f77
    customize IntelVisualFCompiler
    Could not locate executable ifort
    Could not locate executable ifl
    customize AbsoftFCompiler
    Could not locate executable f90
    customize CompaqVisualFCompiler
    Found executable C:\Program Files\Git\usr\bin\DF.exe
    Could not locate executable C:\Program
    customize IntelItaniumVisualFCompiler
    Could not locate executable efl
    customize Gnu95FCompiler
    Could not locate executable gfortran
    Could not locate executable f95
    customize G95FCompiler
    Could not locate executable g95
    customize IntelEM64VisualFCompiler
    customize IntelEM64TFCompiler
    Could not locate executable efort
    Could not locate executable efc
    customize PGroupFlangCompiler
    Could not locate executable flang
    don't know how to compile Fortran code on platform 'nt'
      NOT AVAILABLE

    atlas_3_10_blas_threads_info:
    Setting PTATLAS=ATLAS
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries tatlas not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_3_10_blas_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries satlas not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_blas_threads_info:
    Setting PTATLAS=ATLAS
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries ptf77blas,ptcblas,atlas not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_blas_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries f77blas,cblas,atlas not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    accelerate_info:
      NOT AVAILABLE

   \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:690: UserWarning:
        Optimized (vendor) Blas libraries are not found.
        Falls back to netlib Blas library which has worse performance.
        A better performance should be easily gained by switching
        Blas library.
      self.calc_info()
    blas_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries blas not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

   \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:690: UserWarning:
        Blas (http://www.netlib.org/blas/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [blas]) or by setting
        the BLAS environment variable.
      self.calc_info()
    blas_src_info:
      NOT AVAILABLE

   \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:690: UserWarning:
        Blas (http://www.netlib.org/blas/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [blas_src]) or by setting
        the BLAS_SRC environment variable.
      self.calc_info()
      NOT AVAILABLE

    'svnversion' 不是内部或外部命令，也不是可运行的程序
    或批处理文件。
    non-existing path in 'numpy\\distutils': 'site.cfg'
    lapack_opt_info:
    lapack_mkl_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries mkl_rt not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    openblas_lapack_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries openblas not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    openblas_clapack_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries openblas,lapack not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    flame_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries flame not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

    atlas_3_10_threads_info:
    Setting PTATLAS=ATLAS
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries tatlas,tatlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries tatlas,tatlas not found in C:\
    &lt;class 'numpy.distutils.system_info.atlas_3_10_threads_info'&gt;
      NOT AVAILABLE

    atlas_3_10_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries satlas,satlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries satlas,satlas not found in C:\
    &lt;class 'numpy.distutils.system_info.atlas_3_10_info'&gt;
      NOT AVAILABLE

    atlas_threads_info:
    Setting PTATLAS=ATLAS
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries ptf77blas,ptcblas,atlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries ptf77blas,ptcblas,atlas not found in C:\
    &lt;class 'numpy.distutils.system_info.atlas_threads_info'&gt;
      NOT AVAILABLE

    atlas_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries f77blas,cblas,atlas not found in \lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries f77blas,cblas,atlas not found in C:\
    &lt;class 'numpy.distutils.system_info.atlas_info'&gt;
      NOT AVAILABLE

    lapack_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack not found in ['\\lib', 'C:\\']
      NOT AVAILABLE

   \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:1712: UserWarning:
        Lapack (http://www.netlib.org/lapack/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [lapack]) or by setting
        the LAPACK environment variable.
      if getattr(self, '_calc_info_{}'.format(lapack))():
    lapack_src_info:
      NOT AVAILABLE

   \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:1712: UserWarning:
        Lapack (http://www.netlib.org/lapack/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [lapack_src]) or by setting
        the LAPACK_SRC environment variable.
      if getattr(self, '_calc_info_{}'.format(lapack))():
      NOT AVAILABLE

    \lib\distutils\dist.py:274: UserWarning: Unknown distribution option: 'define_macros'
      warnings.warn(msg)
    running bdist_wheel
    running build
    running config_cc
    unifing config_cc, config, build_clib, build_ext, build commands --compiler options
    running config_fc
    unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
    running build_src
    build_src
    building py_modules sources
    creating build
    creating build\src.win-amd64-3.8
    creating build\src.win-amd64-3.8\numpy
    creating build\src.win-amd64-3.8\numpy\distutils
    building library "npymath" sources
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/

    ----------------------------------------
    Failed building wheel for numpy
    Running setup.py clean for numpy
    Complete output from command \Scripts\python.exe -u -c "import setuptools, tokenize;__file__='\\pip-install-szyxpo9w\\numpy\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec
'))" clean --all:
    Running from numpy source directory.

    `setup.py clean` is not supported, use one of the following instead:

      - `git clean -xdf` (cleans all files)
      - `git clean -Xdf` (cleans all versioned files, doesn't touch
                          files that aren't checked into the git repo)

    Add `--force` to your command to use it anyway if you must (unsupported).


    ----------------------------------------
    Failed cleaning build dir for numpy
  Failed to build numpy
  Installing collected packages: wheel, setuptools, Cython, pybind11, ply, gast, numpy, beniget, pythran
    Running setup.py install for numpy: started
      Running setup.py install for numpy: finished with status 'error'
      Complete output from command \Scripts\python.exe -u -c "import setuptools, tokenize;__file__='\\pip-install-szyxpo9w\\numpy\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'ex
ec'))" install --record \pip-record-_j9_fs2m\install-record.txt --single-version-externally-managed --prefix \pi
p-build-env-iogzj8v9\overlay --compile --install-headers include\site\python3.8\numpy:
      Running from numpy source directory.

      Note: if you need reliable uninstall behavior, then install
      with pip instead of using `setup.py install`:

        - `pip install .`       (from a git repo or downloaded source
                                 release)
        - `pip install numpy`   (last NumPy release on PyPi)


      blas_opt_info:
      blas_mkl_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries mkl_rt not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      blis_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries blis not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      openblas_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries openblas not found in ['\\lib', 'C:\\']
      get_default_fcompiler: matching types: '['gnu', 'intelv', 'absoft', 'compaqv', 'intelev', 'gnu95', 'g95', 'intelvem', 'intelem', 'flang']'
      customize GnuFCompiler
      Could not locate executable g77
      Could not locate executable f77
      customize IntelVisualFCompiler
      Could not locate executable ifort
      Could not locate executable ifl
      customize AbsoftFCompiler
      Could not locate executable f90
      customize CompaqVisualFCompiler
      Found executable C:\Program Files\Git\usr\bin\DF.exe
      Could not locate executable C:\Program
      customize IntelItaniumVisualFCompiler
      Could not locate executable efl
      customize Gnu95FCompiler
      Could not locate executable gfortran
      Could not locate executable f95
      customize G95FCompiler
      Could not locate executable g95
      customize IntelEM64VisualFCompiler
      customize IntelEM64TFCompiler
      Could not locate executable efort
      Could not locate executable efc
      customize PGroupFlangCompiler
      Could not locate executable flang
      don't know how to compile Fortran code on platform 'nt'
        NOT AVAILABLE

      atlas_3_10_blas_threads_info:
      Setting PTATLAS=ATLAS
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries tatlas not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      atlas_3_10_blas_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries satlas not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      atlas_blas_threads_info:
      Setting PTATLAS=ATLAS
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries ptf77blas,ptcblas,atlas not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      atlas_blas_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries f77blas,cblas,atlas not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      accelerate_info:
        NOT AVAILABLE

     \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:690: UserWarning:
          Optimized (vendor) Blas libraries are not found.
          Falls back to netlib Blas library which has worse performance.
          A better performance should be easily gained by switching
          Blas library.
        self.calc_info()
      blas_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries blas not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

     \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:690: UserWarning:
          Blas (http://www.netlib.org/blas/) libraries not found.
          Directories to search for the libraries can be specified in the
          numpy/distutils/site.cfg file (section [blas]) or by setting
          the BLAS environment variable.
        self.calc_info()
      blas_src_info:
        NOT AVAILABLE

      \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:690: UserWarning:
          Blas (http://www.netlib.org/blas/) sources not found.
          Directories to search for the sources can be specified in the
          numpy/distutils/site.cfg file (section [blas_src]) or by setting
          the BLAS_SRC environment variable.
        self.calc_info()
        NOT AVAILABLE

      'svnversion' 不是内部或外部命令，也不是可运行的程序
      或批处理文件。
      non-existing path in 'numpy\\distutils': 'site.cfg'
      lapack_opt_info:
      lapack_mkl_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries mkl_rt not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      openblas_lapack_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries openblas not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      openblas_clapack_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries openblas,lapack not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      flame_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries flame not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

      atlas_3_10_threads_info:
      Setting PTATLAS=ATLAS
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries tatlas,tatlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in C:\
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries tatlas,tatlas not found in C:\
      &lt;class 'numpy.distutils.system_info.atlas_3_10_threads_info'&gt;
        NOT AVAILABLE

      atlas_3_10_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries satlas,satlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in C:\
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries satlas,satlas not found in C:\
      &lt;class 'numpy.distutils.system_info.atlas_3_10_info'&gt;
        NOT AVAILABLE

      atlas_threads_info:
      Setting PTATLAS=ATLAS
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries ptf77blas,ptcblas,atlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in C:\
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries ptf77blas,ptcblas,atlas not found in C:\
      &lt;class 'numpy.distutils.system_info.atlas_threads_info'&gt;
        NOT AVAILABLE

      atlas_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries f77blas,cblas,atlas not found in \lib
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack_atlas not found in C:\
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries f77blas,cblas,atlas not found in C:\
      &lt;class 'numpy.distutils.system_info.atlas_info'&gt;
        NOT AVAILABLE

      lapack_info:
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      customize MSVCCompiler
        libraries lapack not found in ['\\lib', 'C:\\']
        NOT AVAILABLE

     \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:1712: UserWarning:
          Lapack (http://www.netlib.org/lapack/) libraries not found.
          Directories to search for the libraries can be specified in the
          numpy/distutils/site.cfg file (section [lapack]) or by setting
          the LAPACK environment variable.
        if getattr(self, '_calc_info_{}'.format(lapack))():
      lapack_src_info:
        NOT AVAILABLE

     \pip-install-szyxpo9w\numpy\numpy\distutils\system_info.py:1712: UserWarning:
          Lapack (http://www.netlib.org/lapack/) sources not found.
          Directories to search for the sources can be specified in the
          numpy/distutils/site.cfg file (section [lapack_src]) or by setting
          the LAPACK_SRC environment variable.
        if getattr(self, '_calc_info_{}'.format(lapack))():
        NOT AVAILABLE

     \lib\distutils\dist.py:274: UserWarning: Unknown distribution option: 'define_macros'
        warnings.warn(msg)
      running install
      running build
      running config_cc
      unifing config_cc, config, build_clib, build_ext, build commands --compiler options
      running config_fc
      unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
      running build_src
      build_src
      building py_modules sources
      building library "npymath" sources
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/


  ----------------------------------------
Command "\Scripts\python.exe \lib\site-packages\pip-19.0.3-py3.8.egg\pip ins
tall --ignore-installed --no-user --prefix \pip-build-env-iogzj8v9\overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i
  --trusted-host  -- wheel&lt;0.38.0 setuptools&lt;60.0.0 Cython&gt;=0.29.18,&lt;3.0 pybind11&gt;=2.4.3,&lt;2.9.0 pythr
an&gt;=0.10.0,&lt;0.11.0 "numpy==1.19.2; python_version=='3.8' and platform_machine=='aarch64' and platform_python_implementation != 'PyPy'" "numpy==1.20.0; python_version=='3.8' a
nd platform_machine=='arm64' and platform_system=='Darwin'" "numpy==1.20.0; python_version=='3.9' and platform_machine=='arm64' and platform_system=='Darwin'" "numpy==1.17.5;
 python_version=='3.8' and platform_machine=='s390x' and platform_python_implementation != 'PyPy'" "numpy==1.17.3; python_version=='3.8' and (platform_machine!='arm64' orCommand "\Scripts\python.exe \lib\site-packages\pip-19.0.3-py3.8.egg\pip
 install --ignore-installed --no-user --prefix \pip-bu
ild-env-iogzj8v9\overlay --no-warn-script-location --no-binary :none: --only-binary :
none: 
inghua.edu.cn -- wheel&lt;0.38.0 setuptools&lt;60.0.0 Cython&gt;=0.29.18,&lt;3.0 pybind11&gt;=2.4.3,
&lt;2.9.0 pythran&gt;=0.10.0,&lt;0.11.0 "numpy==1.19.2; python_version=='3.8' and platform_mac
hine=='aarch64' and platform_python_implementation != 'PyPy'" "numpy==1.20.0; python_
version=='3.8' and platform_machine=='arm64' and platform_system=='Darwin'" "numpy==1
.20.0; python_version=='3.9' and platform_machine=='arm64' and platform_system=='Darw
in'" "numpy==1.17.5; python_version=='3.8' and platform_machine=='s390x' and platform_python_implementation != 'PyPy'" "numpy==1.17.3; python_version=='3.8' and (platform_mac
hine!='arm64' or platform_system!='Darwin') and platform_machine!='aarch64' and platform_machine!='s390x' and platform_python_implementation != 'PyPy'" "numpy==1.19.3; python
_version=='3.9' and (platform_machine!='arm64' or platform_system!='Darwin') and platform_python_implementation != 'PyPy'" "numpy==1.21.4; python_version=='3.10' and platin'" "numpy==1.17.5; python_version=='3.8' and platform_machine=='s390x' and platform
_python_implementation != 'PyPy'" "numpy==1.17.3; python_version=='3.8' and (platform
_machine!='arm64' or platform_system!='Darwin') and platform_machine!='aarch64' and p
latform_machine!='s390x' and platform_python_implementation != 'PyPy'" "numpy==1.19.3
; python_version=='3.9' and (platform_machine!='arm64' or platform_system!='Darwin')
and platform_python_implementation != 'PyPy'" "numpy==1.21.4; python_version=='3.10' and platform_python_implementation != 'PyPy'" "numpy; python_version&gt;='3.11'" "numpy; pyt
hon_version&gt;='3.8' and platform_python_implementation=='PyPy'"" failed with error code 1 in None

```

#### pip 安装 pywin32 报错

```
$ pip install pywin32
Looking in indexes: 
Collecting pywin32
  Could not find a version that satisfies the requirement pywin32 (from versions: )
No matching distribution found for pywin32

```

### 解决办法

#### 网络方法1

```

$ pip install numpy+mkl-cp38-none-win_amd64.whl
Requirement 'numpy+mkl-cp38-none-win_amd64.whl' looks like a filename, but the file does not exist
numpy+mkl-cp38-none-win_amd64.whl is not a valid wheel filename.

```

**请测不适用，无效**

#### 网络方法2

根据 https://visualstudio.microsoft.com/visual-cpp-build-tools/ 安装微软 Visual Studio 重新搭建C++编译环境

```
$ pip install numpy-1.18.5+mkl-cp38-none-win_amd64.whl
Requirement 'numpy-1.18.5+mkl-cp38-none-win_amd64.whl' looks like a filename, but the file does not exist
Looking in indexes: 
Processing \numpy-1.18.5+mkl-cp38-none-win_amd64.whl
Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: '\\numpy-1.18.5+mkl-cp38-non
e-win_amd64.whl'

```

过程繁琐未测试

#### 亲测解决方法

将pip版本退回较低版本，不使用最新的版本

```
$ python -m pip install pip==20.2.4
Looking in indexes: 
Collecting pip==20.2.4
  Downloading /pip-20.2.4-py2.py3-none-any.whl (1.5 MB)
     ---------------------------------------- 1.5/1.5 MB 2.2 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.1.2
    Uninstalling pip-22.1.2:
      Successfully uninstalled pip-22.1.2
Successfully installed pip-20.2.4

$

```

再次安装，成功

```
$ pip install numpy
Looking in indexes: 
Collecting numpy
  Downloading /numpy-1.22.4-cp38-cp38-win_amd64.whl (14.8 MB)
     |████████████████████████████████| 14.8 MB 1.3 MB/s
Installing collected packages: numpy
Successfully installed numpy-1.22.4
WARNING: You are using pip version 20.2.4; however, version 22.1.2 is available.
You should consider upgrading via the '\Scripts\python.exe -m pip install --upgrade pip' command.


```
