
--- 
title:  爬虫逆向AES加密基础版本和加强版参考 
tags: []
categories: [] 

---
## AES加密

```
Python默认想要进行AES加密，都要通过一个第三方模块。pip install pycryptodome==3.10.1

```

### 一、基础版本：

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
​
​
def aes_encrypt(data_string):
    key = "fd6b639dbcff0c2a1b03b389ec763c4b"
    iv = "77b07a672d57d64c"
    aes = AES.new(
        key=key.encode('utf-8'),
        mode=AES.MODE_CBC,
        iv=iv.encode('utf-8')
    )
    raw = pad(data_string.encode('utf-8'), 16)
    return aes.encrypt(raw)
​
​
data = "aadzfalskdjf;lkaj;dkjfa;skdjf;akjsdf;kasd;fjaoqwierijhnlakjdhf"
result = aes_encrypt(data)
print(result)

```

### 二、加强版：

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
​
KEY = "4E2918885FD98109869D14E0231A0BF4"
KEY = binascii.a2b_hex(KEY)
​
IV = "16B17E519DDD0CE5B79D7A63A4DD801C"
IV = binascii.a2b_hex(IV)
​
​
def aes_encrypt(data_string):
    aes = AES.new(
        key=KEY,
        mode=AES.MODE_CBC,
        iv=IV
    )
    raw = pad(data_string.encode('utf-8'), 16)
    aes_bytes = aes.encrypt(raw)
    return binascii.b2a_hex(aes_bytes).decode().upper()
​
​
data = "|878975262|d000035rirv|1631615607|mg3c3b04ba|1.3.5|ktjwlm89_to920weqpg|4330701|https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"
result = aes_encrypt(data)
print(result)

```

### 三、总结

```
逆向的过程中，如果看到的AES，一定要去找：key、iv

大家还有什么加密算法更好的加强版，欢迎留言讨论

```
