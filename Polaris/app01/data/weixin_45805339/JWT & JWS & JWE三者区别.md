
--- 
title:  JWT & JWS & JWE三者区别 
tags: []
categories: [] 

---
## JWT &amp; JWS &amp; JWE

JWT : Json Web Token

Json web token (JWT), 是为了在网络应用环境间传递声明而执行的一种基于JSON的开放标准（).该token被设计为紧凑且安全的，特别适用于分布式站点的单点登录（SSO）场景。JWT的声明一般被用来在身份提供者和服务提供者间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可以增加一些额外的其它业务逻辑所必须的声明信息，该token也可直接被用于认证，也可被加密。

**JWS**和**JWE**是JWT的两种实现

JWS : Json Web Signature

#### header

jwt的头部承载两部分信息：
- 声明类型，这里是jwt- 声明加密的算法 通常直接使用 HMAC SHA256
完整的头部就像下面这样的JSON：

```
{<!-- -->
  'typ': 'JWT',
  'alg': 'HS256'
}

```

然后将头部进行base64加密（该加密是可以对称解密的),构成了第一部分.

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9

```

#### payload

载荷就是存放有效信息的地方。这个名字像是特指飞机上承载的货品，这些有效信息包含三个部分

1.标准中注册的声明

2.公共的声明

3.私有的声明

**标准中注册的声明** (建议但不强制使用) ：

①**iss**: jwt签发者

②**sub**: jwt所面向的用户

③**aud**: 接收jwt的一方

④**exp**: jwt的过期时间，这个过期时间必须要大于签发时间

⑤**nbf**: 定义在什么时间之前，该jwt都是不可用的.

⑥**iat**: jwt的签发时间

⑦**jti**: jwt的唯一身份标识，主要用来作为一次性token,从而回避重放攻击。

**公共的声明** ： 公共的声明可以添加任何的信息，一般添加用户的相关信息或其他业务需要的必要信息.但不建议添加敏感信息，因为该部分在客户端可解密.

**私有的声明** ： 私有声明是提供者和消费者所共同定义的声明，一般不建议存放敏感信息，因为base64是对称解密的，意味着该部分信息可以归类为明文信息。

定义一个payload:

```
{<!-- -->
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}

```

然后将其进行base64加密，得到JWT的第二部分。

```
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9

```

#### signature

JWS的第三部分是一个签证信息，这个签证信息由三部分组成：
- header (base64后的)- payload (base64后的)- secret
这个部分需要base64加密后的header和base64加密后的payload使用`.`连接组成的字符串，然后通过header中声明的加密方式进行加盐`secret`组合加密，然后就构成了jws的第三部分。

```
// javascript
var encodedString = base64UrlEncode(header) + '.' + base64UrlEncode(payload);

var signature = HMACSHA256(encodedString, 'secret'); // TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ

```

将这三部分用`.`连接成一个完整的字符串,构成了最终的jws:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ

```

**注意：secret是保存在服务器端的，jws的签发生成也是在服务器端的，secret就是用来进行jws的签发和jws的验证，所以，它就是你服务端的私钥，在任何场景都不应该流露出去。一旦客户端得知这个secret, 那就意味着客户端是可以自我签发jws了。**

JWE : JSON Web Encryption
