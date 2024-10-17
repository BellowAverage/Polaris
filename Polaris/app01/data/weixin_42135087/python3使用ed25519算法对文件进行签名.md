
--- 
title:  python3使用ed25519算法对文件进行签名 
tags: []
categories: [] 

---
>  
 pip install cryptography 


```
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import os

def load_ed25519_private_key(private_key_path):
    # 从文件中加载Ed25519私钥
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
    
    return private_key

def sign_file(file_path, private_key):
    # 读取文件内容
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # 使用私钥对文件内容进行签名
    signature = private_key.sign(data)
    
    return signature

def save_signature(signature, signature_path):
    # 将签名二进制保存到文件
    with open(signature_path, "wb") as sig_file:
        sig_file.write(signature)

def main():
    # 私钥文件路径
    private_key_path = 'path/to/your/private_key.pem'
    
    # 加载私钥
    private_key = load_ed25519_private_key(private_key_path)
    
    # 指定需要签名的文件路径
    file_path = 'path/to/your/file.txt'
    
    # 指定签名保存的文件路径
    signature_path = 'path/to/your/signature.sig'
    
    # 对文件进行签名
    signature = sign_file(file_path, private_key)
    
    # 保存签名到文件
    save_signature(signature, signature_path)
    
    # 输出消息
    print(f"Signature saved to {signature_path}")

if __name__ == "__main__":
    main()


```
