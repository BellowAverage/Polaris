
--- 
title:  pip is configured with locations that require TLS/SSL 
tags: []
categories: [] 

---
**我这儿是出现在 centos6.8 上安装 python3.7 以后，pip 无法正常 install 安装依赖模块。**

```
[root@centos68 insight-tool]# pip3 --version
pip 10.0.1 from /usr/local/python3.7/lib/python3.7/site-packages/pip (python 3.7)
[root@centos68 insight-tool]# pip3 install -r requirement.txt 
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting pygrok==1.0.0 (from -r requirement.txt (line 1))
  Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pygrok/
  Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pygrok/
  Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pygrok/
  Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pygrok/
  Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pygrok/
  Could not fetch URL https://pypi.org/simple/pygrok/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pygrok/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
  Could not find a version that satisfies the requirement pygrok==1.0.0 (from -r requirement.txt (line 1)) (from versions: )
No matching distribution found for pygrok==1.0.0 (from -r requirement.txt (line 1))
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
[root@centos68 insight-tool]# openssl version
OpenSSL 1.0.1e-fips 11 Feb 2013

```

提示说 ssl 不可用，但是实际上 openssl 是有的。既然有却不可用，那大概率的问题就是版本不满足要求了。因此解决方案也就出来了。

### 解决方案1

#### 重新编译安装 python3.6

降低 python 版本，既然 python3.7 安装后对应的 pip 无法正常安装，那就下载 python3.6 或更低的 python3 源码包编译安装。

```
[root@centos68 ~]# wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
[root@centos68 ~]# xz -d Python-3.6.0.tar.xz 
[root@centos68 ~]# tar -xf Python-3.6.0.tar 
[root@centos68 Python-3.6.0]# ./configure --prefix=/usr/local/python3.6
[root@centos68 Python-3.6.0]# make &amp;&amp; make install
```

使用 python3.6 对应的 pip 安装依赖包的话，我这儿是可以正常安装的。 

```
[root@centos68 insight-tool]# /usr/local/python3.6/bin/pip3 install -r requirement.txt 
Collecting pygrok==1.0.0 (from -r requirement.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/ce/a5/963d78c4eda7edb0ea827679dbcf5f77e4d767562b59681bd23ea5913af6/pygrok-1.0.0.tar.gz
Collecting PyYAML (from -r requirement.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/7a/5b/bc0b5ab38247bba158504a410112b6c03f153c652734ece1849749e5f518/PyYAML-5.4.1-cp36-cp36m-manylinux1_x86_64.whl (640kB)
    100% |████████████████████████████████| 645kB 1.7MB/s 
Collecting regex==2020.11.13 (from -r requirement.txt (line 3))
  Downloading https://files.pythonhosted.org/packages/5a/75/aca08032c9752a75acc60ff7f4e58f1a74164b996395f44727ffdb17ebaf/regex-2020.11.13-cp36-cp36m-manylinux1_x86_64.whl (666kB)
    100% |████████████████████████████████| 675kB 1.2MB/s 
Collecting requests==2.25.0 (from -r requirement.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/39/fc/f91eac5a39a65f75a7adb58eac7fa78871ea9872283fb9c44e6545998134/requests-2.25.0-py2.py3-none-any.whl (61kB)
    100% |████████████████████████████████| 61kB 11.2MB/s 
Collecting xmltodict==0.12.0 (from -r requirement.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/28/fd/30d5c1d3ac29ce229f6bdc40bbc20b28f716e8b363140c26eff19122d8a5/xmltodict-0.12.0-py2.py3-none-any.whl
Collecting urllib3&lt;1.27,&gt;=1.21.1 (from requests==2.25.0-&gt;-r requirement.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/5f/64/43575537846896abac0b15c3e5ac678d787a4021e906703f1766bfb8ea11/urllib3-1.26.6-py2.py3-none-any.whl (138kB)
    100% |████████████████████████████████| 143kB 8.5MB/s 
Collecting certifi&gt;=2017.4.17 (from requests==2.25.0-&gt;-r requirement.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/05/1b/0a0dece0e8aa492a6ec9e4ad2fe366b511558cdc73fd3abc82ba7348e875/certifi-2021.5.30-py2.py3-none-any.whl (145kB)
    100% |████████████████████████████████| 153kB 9.3MB/s 
Collecting chardet&lt;4,&gt;=3.0.2 (from requests==2.25.0-&gt;-r requirement.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 9.3MB/s 
Collecting idna&lt;3,&gt;=2.5 (from requests==2.25.0-&gt;-r requirement.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 12.3MB/s 
Installing collected packages: regex, pygrok, PyYAML, urllib3, certifi, chardet, idna, requests, xmltodict
  Running setup.py install for pygrok ... done
Successfully installed PyYAML-5.4.1 certifi-2021.5.30 chardet-3.0.4 idna-2.10 pygrok-1.0.0 regex-2020.11.13 requests-2.25.0 urllib3-1.26.6 xmltodict-0.12.0
You are using pip version 9.0.1, however version 21.2.4 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

```

### 解决方案2

升级 openssl，感觉可能是 python3.7 对需要的 openssl 的版本要求要高一些。如果你是硬脾气，非要使用 python3.7，可以尝试一下升级 openssl （升级有风险，操作需谨慎，毕竟 centos6.8 默认的源最新的就只有 openssl-1.0.1e-48.el6_8.4.x86_64）。

#### 编译安装 openssl

```
[root@centos68 ~]# wget https://www.openssl.org/source/openssl-1.1.1l.tar.gz
[root@centos68 ~]# tar -xzvf openssl-1.1.1l.tar.gz
[root@centos68 ~]# cd openssl-1.1.1l
[root@centos68 openssl-1.1.1l]# ./config shared zlib --prefix=/usr/local/openssl
[root@centos68 openssl-1.1.1l]# make &amp;&amp; make install
```

#### 原 openssl 备份

```
[root@centos68 openssl-1.1.1l]# mv /usr/bin/openssl /usr/bin/openssl.bak
[root@centos68 openssl-1.1.1l]# mv /usr/include/openssl /usr/include/openssl.bak
```

#### 替换原来的 openssl

```
[root@centos68 openssl-1.1.1l]# ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl
[root@centos68 openssl-1.1.1l]# ln -s /usr/local/openssl/include/openssl/ /usr/include/openssl
[root@centos68 openssl-1.1.1l]# echo "/usr/local/openssl/lib" &gt;&gt; /etc/ld.so.conf
[root@centos68 openssl-1.1.1l]# ldconfig
[root@centos68 ~]# openssl version
OpenSSL 1.1.1l  24 Aug 2021
```

#### 重新编译安装 python3.7 

```
[root@centos68 ~]# cd Python-3.7.0
[root@centos68 Python-3.7.0]# ./configure --prefix=/usr/local/python3.7 --with-openssl=/usr/local/openssl/
[root@centos68 Python-3.7.0]# make &amp;&amp; make install
```

#### 测试 pip3

```
[root@centos68 ~]# /usr/local/python3.7/bin/pip3 install redis
Collecting redis
  Downloading https://files.pythonhosted.org/packages/a7/7c/24fb0511df653cf1a5d938d8f5d19802a88cef255706fdda242ff97e91b7/redis-3.5.3-py2.py3-none-any.whl (72kB)
    100% |████████████████████████████████| 81kB 94kB/s 
Installing collected packages: redis
Successfully installed redis-3.5.3
You are using pip version 10.0.1, however version 21.2.4 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

```

经测试 pip3 可以正常安装依赖包了，表示升级成功。
