
--- 
title:  jsrsasign签名 rsa非对称加密（MD5加密32位大写+私钥签名） 
tags: []
categories: [] 

---
安装：

```
npm install jsrsasign
npm i js-md5

```

封装方法：

```
// 公私钥签名

import {<!-- --> KEYUTIL, KJUR, hextob64 } from 'jsrsasign';
import md5 from 'js-md5';

const privateKeyString = -----BEGIN PRIVATE KEY-----这里放你的私钥-----END PRIVATE KEY-----;
// 注意：一定要以上写法

// 加密
export function doSign(str) {<!-- -->
  // 将要签名的字符串进行md5加密（这里根据业务需求来，不是必需的）
  const newStr = md5(str).toUpperCase();
  // 方式1: 先建立 key 对象, 构建 signature 实例, 传入 key 初始化 -&gt; 签名
  const key = KEYUTIL.getKey(privateKeyString);
  // 创建 Signature 对象，设置签名编码算法
  const signature = new KJUR.crypto.Signature({<!-- -->
    alg: 'SHA256withRSA'
  });
  // 传入key实例, 初始化signature实例
  signature.init(key);
  // 传入待加密字符串
  signature.updateString(newStr);
  // 签名, 得到16进制字符结果
  let a = signature.sign();
  let sign = hextob64(a);
  return sign;
}


```
