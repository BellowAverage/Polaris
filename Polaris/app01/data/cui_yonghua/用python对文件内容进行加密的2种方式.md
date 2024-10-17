
--- 
title:  用python对文件内容进行加密的2种方式 
tags: []
categories: [] 

---
方式1：有时候我们手中文件的内容十分的重要、十分地机密，我们可以选择对此进行加密，代码如下:

```
from cryptography.fernet import Fernet

def encrypt(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, 'wb') as enc_file:
        enc_file.write(encrypted)
        
key = Fernet.generate_key()
filename = "file.txt"
encrypt(filename, key)

```

然后对文件内容进行加密，当然这个密钥后面在对文件进行解密的时候会派上用场，因此密钥一定要保存完好，解密的代码如下

```
def decrypt(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)

decrypt(filename, key)

```

上面的脚本，其中的密钥是一个随机生成的随机数，当然密钥也可以是我们自己指定的，代码如下

```
import pyAesCrypt

def Encryption(input_file_path, output_file_path, key):
    pyAesCrypt.encryptFile(input_file_path, output_file_path, key)
    print("File has been decrypted")

def Decryption(input_file_path, output_file_path, key):
    pyAesCrypt.decryptFile(input_file_path, output_file_path, key)
    print("File has been decrypted")

```

方式2：使用RSA加密算法实现数据的加密解密：

```
import os
import rsa

def encrypt_file(file_path, public_key_file):
    """使用RSA算法加密文件
    
    参数：
    file_path: 需要加密的文件路径
    public_key_file: 公钥文件路径
    
    返回值：
    无
    """
    # 读取文件内容
    with open(file_path, "rb") as file:
        file_content = file.read()
    # 读取公钥
    with open(public_key_file, "rb") as key_file:
        public_key = rsa.PublicKey.load_pkcs1(key_file.read())
    # 加密文件内容
    encrypted_content = rsa.encrypt(file_content, public_key)
    # 将加密后的内容写入文件
    with open(file_path, "wb") as file:
        file.write(encrypted_content)

def decrypt_file(file_path, private_key_file, password):
    """使用RSA算法解密文件
    
    参数：
    file_path: 需要解密的文件路径
    private_key_file: 私钥文件路径
    password: 私钥文件密码
    
    返回值：
    无
    """
    # 读取文件内容
    with open(file_path, "rb") as file:
        encrypted_content = file.read()
    # 读取私钥
    with open(private_key_file, "rb") as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read(), password)
    # 解密文件内容
    file_content = rsa.decrypt(encrypted_content, private_key)
    # 将解密后的内容写入文件
    with open(file_path, "wb") as file:
        file.write(file_content)


```
