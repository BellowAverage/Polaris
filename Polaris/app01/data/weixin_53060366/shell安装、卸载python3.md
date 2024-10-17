
--- 
title:  shell安装、卸载python3 
tags: []
categories: [] 

---
## shell安装、卸载python3

>  
 执行脚本后需要做选择，是安装python还是卸载python。安装脚本需要填写到小版本号，例如：python3.9.5 
 卸载python的时候只需要填写大版本号，例如python3.9 即可。 


```
#!/bin/bash
# 安装或卸载Python环境

echo "请选择要执行的操作:"
echo "1. 安装Python环境"
echo "2. 卸载Python环境"
read -p "请输入操作编号: " choice

if [ $choice -eq 1 ]; then
  # 安装Python环境
  read -p "请输入要安装的Python版本号: " version
  echo "开始安装Python ${version}..."

  # 安装必要的依赖
  yum install -y gcc openssl-devel bzip2-devel libffi-devel

  # 下载Python源码并解压
  cd /usr/local/src
  wget https://www.python.org/ftp/python/${version}/Python-${version}.tgz
  tar xzf Python-${version}.tgz

  # 编译并安装Python
  cd Python-${version}
  ./configure --enable-optimizations
  make altinstall

  # 安装pip
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python${version} get-pip.py

  # 配置环境变量
  echo "export PATH=\"/usr/local/bin:\$PATH\"" &gt;&gt; ~/.bashrc
  source ~/.bashrc

  echo "Python ${version}安装成功！"

elif [ $choice -eq 2 ]; then
  # 卸载Python环境
  read -p "请输入要卸载的Python版本号: " version
  echo "开始卸载Python ${version}..."

  # 检查Python是否已安装
  if [ -f "/usr/local/bin/python${version}" ]; then
    # 删除Python安装目录
    rm -rf "/usr/local/bin/python${version}"
    rm -rf "/usr/local/bin/pip${version}"
    rm -rf "/usr/local/lib/python${version}/"

    # 删除环境变量配置
    sed -i "/export PATH=\/usr\/local\/bin:$PATH/d" ~/.bashrc
    source ~/.bashrc

    echo "Python ${version}卸载成功！"
  else
    echo "Python ${version}未安装，无需卸载。"
  fi
else
  echo "无效的操作编号。"
fi

```
