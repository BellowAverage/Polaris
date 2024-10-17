
--- 
title:  CryptoJS实现vue项目路由传参AES加密 
tags: []
categories: [] 

---
安装：

```
npm i crypto-js

```

封装方法：

```
import CryptoJS from 'crypto-js/crypto-js';
// const CryptoJS = require("crypto-js");

const KEY = CryptoJS.enc.Utf8.parse('1234567890ABCDEF'); //  密钥        长度必须为16位
const IV = CryptoJS.enc.Utf8.parse('123456'); //  初始向量    长度随意

/*
 * AES加密 ：字符串 key iv  返回base64
 */
export function Encrypt(str) {<!-- -->
  let key = KEY;
  let iv = IV;
  let srcs = CryptoJS.enc.Utf8.parse(str);
  var encrypt = CryptoJS.AES.encrypt(srcs, key, {<!-- -->
    iv: iv,
    mode: CryptoJS.mode.CBC, //这里可以选择AES加密的模式
    padding: CryptoJS.pad.Pkcs7
  });
  return CryptoJS.enc.Base64.stringify(encrypt.ciphertext);
}

/*
 * AES 解密 ：字符串 key iv  返回base64
 */
export function Decrypt(str) {<!-- -->
  let key = KEY;
  let iv = IV;
  let base64 = CryptoJS.enc.Base64.parse(str);
  let src = CryptoJS.enc.Base64.stringify(base64);
  var decrypt = CryptoJS.AES.decrypt(src, key, {<!-- -->
    iv: iv,
    mode: CryptoJS.mode.CBC, //这里可以选择AES解密的模式
    padding: CryptoJS.pad.Pkcs7
  });

  var decryptedStr = decrypt.toString(CryptoJS.enc.Utf8);
  return decryptedStr.toString();
}

```

路由传参使用：

```
// 传参
const queryValue = Encrypt(JSON.stringify(detailInfo))
router.push({<!-- -->
  path: '/sign',
  query: {<!-- -->
    queryValue: queryValue
  }
});
// 接收参数
const queryValue = JSON.parse(Decrypt(router.currentRoute.value.query.queryValue))

```
