
--- 
title:  python3 sha256加密用法 
tags: []
categories: [] 

---
#### hashlib模块简介：

hashlib模块为不同的安全哈希/安全散列（Secure Hash Algorithm）和 信息摘要算法（Message Digest Algorithm）实现了一个公共的、通用的接口，也可以说是一个统一的入口。因为hashlib模块不仅仅是整合了md5和sha模块的功能，还提供了对更多中算法的函数实现，如：MD5，SHA1，SHA224，SHA256，SHA384和SHA512。 以SHA256为例：

```
def has_test():
    c = "hello world"
    s = hashlib.sha256()
    s.update(c.encode())
    b = s.hexdigest()
    # parameters_authentication("111", b, 1634884391)
    print(len(b), b, type(b))
# 运行结果：
64 b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9 &lt;class 'str'&gt;

```
