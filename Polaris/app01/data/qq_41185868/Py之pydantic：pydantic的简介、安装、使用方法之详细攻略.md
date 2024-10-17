
--- 
title:  Py之pydantic：pydantic的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
Py之pydantic：pydantic的简介、安装、使用方法之详细攻略







**目录**

















## **p****ydantic****的简介**

pydantic是使用Python类型提示进行数据验证。快速且可扩展，Pydantic与您的检查器/IDE/思维相容。使用纯净、规范的Python 3.8+定义数据的格式；使用Pydantic进行验证。

pydantic_settings使用Pydantic进行设置管理，这是Pydantic的BaseSettings的新官方位置。此包由Daniel Daniels慷慨捐赠给了Pydantic组织，详情请参阅pydantic/pydantic#4492进行讨论。对于旧版的“管理应用程序设置的Hipster-orgazmic工具”包，请参见版本0.2.5。



### **<strong><strong>1、**</strong>**<strong>Pydantic V1.10 vs. V2**</strong></strong>

Pydantic V2 是一个从头开始的重写，提供了许多新功能、性能改进以及一些与 Pydantic V1 相比的破坏性变化。

如果您正在使用 Pydantic V1，您可能想查看 pydantic V1.10 文档或 1.10.X-fixes git 分支。Pydantic V2 也内置了 Pydantic V1 的最新版本，以便您可以逐步升级您的代码库和项目：from pydantic import v1 as pydantic_v1。







## **p****ydantic****的安装**

使用 pip install -U pydantic 或 conda install pydantic -c conda-forge 进行安装。要获取更多安装选项以使 Pydantic 更加快速，请参阅文档中的安装部分。

```
pip install -U pydantic
conda install pydantic -c conda-forge 
pip install -i https://mirrors.aliyun.com/pypi/simple pydantic
pip install -i https://mirrors.aliyun.com/pypi/simple pydantic_settings
```

<img alt="" height="444" src="https://img-blog.csdnimg.cn/direct/e7d415eb519043edb5ca811e56ce32a6.png" width="1200">





## **p****ydantic****的使用方法**

### **<strong><strong>1、**</strong>**<strong>简单的示例**</strong></strong>

```
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
#&gt; User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
#&gt; 123
```






