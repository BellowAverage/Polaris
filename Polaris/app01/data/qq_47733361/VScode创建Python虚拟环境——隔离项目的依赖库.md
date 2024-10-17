
--- 
title:  VScode创建Python虚拟环境——隔离项目的依赖库 
tags: []
categories: [] 

---
虚拟环境可以隔离项目所需的依赖库，从而避免全局安装和权限问题。 按照以下步骤创建和使用虚拟环境：

### 1、安装虚拟环境工具（如果尚未安装）

```
pip install virtualenv

```

### 2、在项目目录中创建一个新的虚拟环境

```
virtualenv venv

```

### 3、激活虚拟环境

```
source venv/bin/activate

```

### 4、在激活的虚拟环境中安装 matplotlib 和其他依赖项

```
pip install matplotlib

```

### 5、退出虚拟环境

```
deactivate

```

这样，您就可以在虚拟环境中运行脚本，并且不会与系统的 Python 环境或其他项目的依赖冲突
