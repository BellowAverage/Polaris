
--- 
title:  centos7安装 virtualenv 
tags: []
categories: [] 

---
### centos7安装 virtualenv

参考 
1. 安装虚拟环境包：
```
pip install virtualenv -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

```

<img src="https://img-blog.csdnimg.cn/5254fc6c88ab42b098b962a563303d12.png" alt="在这里插入图片描述"> 2. 安装虚拟环境扩展包

```
pip install virtualenvwrapper -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

```

<img src="https://img-blog.csdnimg.cn/9327efca33ff4b3d9a92aa5bcf5ad1da.png" alt="在这里插入图片描述"> 3. 查找virtualenvwrapper所在的路径(记得加.sh要不然查到出来的路径不正确)

```
sudo find / -name virtualenvwrapper.sh

```

<img src="https://img-blog.csdnimg.cn/e19805e0b7054346af47f9eb942e77da.png" alt="在这里插入图片描述"> 4. 创建一个管理所有virtualenvwrapper的存放文件夹，一般建议在home目录下

```
mkdir ~/.virtualenvs

```

<img src="https://img-blog.csdnimg.cn/29efdffd641a4a92b6d65bbcf5c877ed.png" alt="在这里插入图片描述"> 5. 修改用户家目录下的配置文件.bashrc,添加如下内容：

```
vi .bashrc

```

添加一下内容

```
export WORKON_HOME=$HOME/.virtualenvs  
source /usr/local/bin/virtualenvwrapper.sh

```

<img src="https://img-blog.csdnimg.cn/56e438ee6cdd446ebae8083213fd7758.png" alt="在这里插入图片描述"> 6. 激活更新配置

```
source .bashrc

```

<img src="https://img-blog.csdnimg.cn/8aa87b29e00844f0b966c338cf3389a0.png" alt="在这里插入图片描述"> 7. 创建python3虚拟环境

```
mkvirtualenv  python3

```

<img src="https://img-blog.csdnimg.cn/9ebbfb7d44aa41d5ad0f8ac83746e15a.png" alt="在这里插入图片描述"> 常用虚拟环境命令

```
mkvirtualenv -p python3 虚拟环境名称  # 创建虚拟环境
workon 两次tab键  # 查看所有虚拟环境
workon 虚拟环境名称  # 进入虚拟环境
rmvirtualenv 虚拟环境名称  # 删除虚拟环境
deactivate  # 退出虚拟环境


```
