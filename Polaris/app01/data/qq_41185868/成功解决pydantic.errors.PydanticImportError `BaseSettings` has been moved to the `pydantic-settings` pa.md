
--- 
title:  成功解决pydantic.errors.PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` pa 
tags: []
categories: [] 

---
成功解决pydantic.errors.PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` package







**目录**













## **解决问题**

pydantic.errors.PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` package



## **解决思路**

pydantic导入错误:' basessettings '已移动到' pydantic-settings '包中





## **解决方法**

参考文章：

BaseSettings类已经被移动到pydantic-settings包中，因此你需要相应地调整你的导入语句。确保你的代码中的BaseSettings类来自正确的位置。

```
将
from pydantic import BaseSettings
改为
from pydantic_settings import BaseSettings
```






