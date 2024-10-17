
--- 
title:  Python requests 考试宝爬虫js逆向分析 
tags: []
categories: [] 

---
**目录**





















## 说明

本文仅记录一次学习实验的过程。

## 效果

<img alt="" height="461" src="https://img-blog.csdnimg.cn/03ee07afacd44c44973a63447c1201da.png" width="1200">



## 登录接口

### 分析

拿下登录接口是为了我们更方便的获取token 。之后搜题都是用token搜题，不再需要密码。

我们可以看到这个登录包的密码是被加密的，但是可以发现。如果密码相同，加密结果也一样，所以优先考虑对称加密。

<img alt="" height="523" src="https://img-blog.csdnimg.cn/e1bf6d8f239348ca9eb7066515c0b89a.png" width="1182">

一般情况下先尝试简单的md5这些，发现不是，只好开始抠源代码。

直接搜索关键字encrypt，出来一堆匹配结果。

<img alt="" height="429" src="https://img-blog.csdnimg.cn/2735597442064cf2aa279e2ec2cf12ca.png" width="1200">

凭经验点进去一个，看见ECB。百分之99就是它了，打断点。点击登录，果然断住。而且e就是输入的密码，t大家都猜到了吧，就是密钥，先复制下来。

<img alt="" height="307" src="https://img-blog.csdnimg.cn/f29a6a92b66d4c17b4b695a7f2990a94.png" width="700">

var n = o.enc.Utf8.parse(t);通过进去分析，其实是将密钥转换为CryptoJS WordArray对象形式

<img alt="" height="114" src="https://img-blog.csdnimg.cn/257d19ff69a54d98b48e568ff210f646.png" width="612">

而

return o.TripleDES.encrypt(e, n, {<!-- -->                 mode: o.mode.ECB,                 padding: o.pad.Pkcs7             }).toString()         }

就是加密函数了

<img alt="" height="304" src="https://img-blog.csdnimg.cn/599d738529724edfa580d297b806bd59.png" width="718">

<img alt="" height="132" src="https://img-blog.csdnimg.cn/7ef980edec27433389acc6fe06d71729.png" width="636">

再进去。

<img alt="" height="286" src="https://img-blog.csdnimg.cn/4a4c0c0b5b08421dbce163b46fce6a4f.png" width="715">



### 实现

所以可以用以下python代码复现这个过程

```
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import binascii

# 将密钥转换为CryptoJS WordArray对象形式
def string_to_word_array(s):
    utf8_encoded = s.encode('utf-8')  # 将字符串编码为 UTF-8 字节串
    words = []
    sig_bytes = len(utf8_encoded)

    for i in range(0, sig_bytes, 4):
        word = 0
        for j in range(4):
            if i + j &lt; sig_bytes:
                word |= utf8_encoded[i + j] &lt;&lt; (24 - j * 8)
        words.append(word)

    return {
        "words": words,
        "sigBytes": sig_bytes
    }

# TripleDES加密函数
def triple_des_encrypt(data, key):
    # 将密钥的word array转换为字节串
    key_bytes = binascii.unhexlify(''.join(f'{x:08x}' for x in key['words']))
    # 创建加密器，使用ECB模式和PKCS7填充
    cipher = DES3.new(key_bytes, DES3.MODE_ECB)
    # 对数据进行填充，并加密
    padded_data = pad(data.encode('utf-8'), DES3.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    # 将加密后的数据转换为base64编码的字符串
    encrypted_data_b64 = binascii.b2a_base64(encrypted_data).decode('utf-8')
    return encrypted_data_b64.strip()

def password(data_to_encrypt):
    # 密钥字符串
    t = "AmrGowGCtUwd/2PgTyrJuV=="
    # 将密钥字符串转换为word array
    key_word_array = string_to_word_array(t)
    # 执行加密
    encrypted_data = triple_des_encrypt(data_to_encrypt, key_word_array)
    return encrypted_data

print(password("11111111"))

```

运行结果对比<img alt="" height="124" src="https://img-blog.csdnimg.cn/553a7136ebc641a297ce0db4bb8d28a8.png" width="508">

<img alt="" height="130" src="https://img-blog.csdnimg.cn/40f2979d135043c6995f5a52212b1163.png" width="711">

逆向成功



## 查询接口

### 分析

首先查看查询问题的接口

<img alt="" height="88" src="https://img-blog.csdnimg.cn/direct/0047c268659441ef9459bb8989b162d6.png" width="569">

请求头信息如下

```
Accept: xxx
Accept-Encoding: xxx
Accept-Language: xxx
Authorization: xxx
CLIENT-IDENTIFIER: xxx
Cache-Control: xxx
Connection: xxx
Content-Length: xxx
Content-Type: xxx
Cookie: xxx
Host: xxx
Origin: xxx
Pragma: xxx
Referer: xxx
Sec-Fetch-Dest: xxx
Sec-Fetch-Mode: xxx
Sec-Fetch-Site: xxx
Sign: xxx
TimeStamp: xxx
User-Agent: xxx
VERSION: xxx
platform: xxx
sec-ch-ua: xxx
sec-ch-ua-mobile: xxx
sec-ch-ua-platform: xxx
```

请求体信息如下

```
keyword: "mysql"
page: 1
paperid: ""
qtype: ""
size: 20
```

可以看到请求体的内容是没有加密的，所以实现身份验证的部分在请求头中。可以推测请求头中身份校验的字段可能有**Authorization**、**CLIENT-IDENTIFIER**、**Cookie**、**Sign**、**TimeStamp**。具体他们有什么联系，这就需要进一步进行js逆向了。

一般来说**Authorization**存放的是token信息，查看浏览器的localstorage可以验证这个猜想，所以重点应该是sign怎么生成的。

全局搜索关键字Sign，可以看到Sign生成的地方。

<img alt="" height="287" src="https://img-blog.csdnimg.cn/direct/dc9bde63b44641c988bc1c964ba5a467.png" width="806">

很明显可以看到Sign的生成表达式是**l = no()(o + t + c + n + o)，其中o**、**t**、**c**、**n**的含义在这个函数中都有定义。重点是这个**no()(o + t + c + n + o)**函数的执行逻辑。打上断点进去查看。

经过第一个函数

<img alt="" height="214" src="https://img-blog.csdnimg.cn/direct/0ca0e4c84601404eb00a5cb16d04c22f.png" width="755">

随后执行createOutputMethod方法

<img alt="" height="108" src="https://img-blog.csdnimg.cn/direct/05b631e757db4bdb8706bc3ac65ed297.png" width="753">

经过第二个函数

<img alt="" height="235" src="https://img-blog.csdnimg.cn/direct/fa078005290046a5b5932d73c8dedb35.png" width="656">

经过第三个函数

<img alt="" height="273" src="https://img-blog.csdnimg.cn/direct/f81143e72954405f9919f3974ff38850.png" width="740">

经过第四个函数

<img alt="" height="158" src="https://img-blog.csdnimg.cn/direct/3b9a54e0e6484be0bdb3baebfc421b7d.png" width="752">



经过第五个函数

<img alt="" height="267" src="https://img-blog.csdnimg.cn/direct/d38dcb28c43d4310beab869d3f3dab40.png" width="760">

### 实现

把这些用到的函数全部抄下来，放到一个js文件里面然后补齐一些变量。可以得到下面的加密js。

```
// 辅助变量和函数定义
const HEX_CHARS = '0123456789abcdef'.split('');
const EXTRA = [128, 32768, 8388608, -2147483648,];
const SHIFT = [0, 8, 16, 24];
const ARRAY_BUFFER = true;

function Md5(append) {
    var buffer = new ArrayBuffer(68);
    var buffer8 = new Uint8Array(buffer);
    var blocks = new Uint32Array(buffer);
    if (true)
        blocks[0] = blocks[16] = blocks[1] = blocks[2] = blocks[3] = blocks[4] = blocks[5] = blocks[6] = blocks[7] = blocks[8] = blocks[9] = blocks[10] = blocks[11] = blocks[12] = blocks[13] = blocks[14] = blocks[15] = 0,
            this.blocks = blocks,
            this.buffer8 = buffer8;
    else if (ARRAY_BUFFER) {
        var t = new ArrayBuffer(68);
        this.buffer8 = new Uint8Array(t),
            this.blocks = new Uint32Array(t)
    } else
        this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    this.h0 = this.h1 = this.h2 = this.h3 = this.start = this.bytes = this.hBytes = 0,
        this.finalized = this.hashed = !1,
        this.first = !0
}

Md5.prototype.update = function (e) {
    if (!this.finalized) {
        var t, n = typeof e;
        if ("string" !== n) {
            if ("object" !== n)
                ;
            if (null === e)
                ;
            if (ARRAY_BUFFER &amp;&amp; e.constructor === ArrayBuffer)
                e = new Uint8Array(e);
            else if (!(Array.isArray(e) || ARRAY_BUFFER &amp;&amp; ArrayBuffer.isView(e)))
                throw ERROR;
            t = !0
        }
        for (var code, i, r = 0, o = e.length, l = this.blocks, c = this.buffer8; r &lt; o;) {
            if (this.hashed &amp;&amp; (this.hashed = !1,
                l[0] = l[16],
                l[16] = l[1] = l[2] = l[3] = l[4] = l[5] = l[6] = l[7] = l[8] = l[9] = l[10] = l[11] = l[12] = l[13] = l[14] = l[15] = 0),
                t)
                if (ARRAY_BUFFER)
                    for (i = this.start; r &lt; o &amp;&amp; i &lt; 64; ++r)
                        c[i++] = e[r];
                else
                    for (i = this.start; r &lt; o &amp;&amp; i &lt; 64; ++r)
                        l[i &gt;&gt; 2] |= e[r] &lt;&lt; SHIFT[3 &amp; i++];
            else if (ARRAY_BUFFER)
                for (i = this.start; r &lt; o &amp;&amp; i &lt; 64; ++r)
                    (code = e.charCodeAt(r)) &lt; 128 ? c[i++] = code : code &lt; 2048 ? (c[i++] = 192 | code &gt;&gt; 6,
                        c[i++] = 128 | 63 &amp; code) : code &lt; 55296 || code &gt;= 57344 ? (c[i++] = 224 | code &gt;&gt; 12,
                        c[i++] = 128 | code &gt;&gt; 6 &amp; 63,
                        c[i++] = 128 | 63 &amp; code) : (code = 65536 + ((1023 &amp; code) &lt;&lt; 10 | 1023 &amp; e.charCodeAt(++r)),
                        c[i++] = 240 | code &gt;&gt; 18,
                        c[i++] = 128 | code &gt;&gt; 12 &amp; 63,
                        c[i++] = 128 | code &gt;&gt; 6 &amp; 63,
                        c[i++] = 128 | 63 &amp; code);
            else
                for (i = this.start; r &lt; o &amp;&amp; i &lt; 64; ++r)
                    (code = e.charCodeAt(r)) &lt; 128 ? l[i &gt;&gt; 2] |= code &lt;&lt; SHIFT[3 &amp; i++] : code &lt; 2048 ? (l[i &gt;&gt; 2] |= (192 | code &gt;&gt; 6) &lt;&lt; SHIFT[3 &amp; i++],
                        l[i &gt;&gt; 2] |= (128 | 63 &amp; code) &lt;&lt; SHIFT[3 &amp; i++]) : code &lt; 55296 || code &gt;= 57344 ? (l[i &gt;&gt; 2] |= (224 | code &gt;&gt; 12) &lt;&lt; SHIFT[3 &amp; i++],
                        l[i &gt;&gt; 2] |= (128 | code &gt;&gt; 6 &amp; 63) &lt;&lt; SHIFT[3 &amp; i++],
                        l[i &gt;&gt; 2] |= (128 | 63 &amp; code) &lt;&lt; SHIFT[3 &amp; i++]) : (code = 65536 + ((1023 &amp; code) &lt;&lt; 10 | 1023 &amp; e.charCodeAt(++r)),
                        l[i &gt;&gt; 2] |= (240 | code &gt;&gt; 18) &lt;&lt; SHIFT[3 &amp; i++],
                        l[i &gt;&gt; 2] |= (128 | code &gt;&gt; 12 &amp; 63) &lt;&lt; SHIFT[3 &amp; i++],
                        l[i &gt;&gt; 2] |= (128 | code &gt;&gt; 6 &amp; 63) &lt;&lt; SHIFT[3 &amp; i++],
                        l[i &gt;&gt; 2] |= (128 | 63 &amp; code) &lt;&lt; SHIFT[3 &amp; i++]);
            this.lastByteIndex = i,
                this.bytes += i - this.start,
                i &gt;= 64 ? (this.start = i - 64,
                    this.hash(),
                    this.hashed = !0) : this.start = i
        }
        return this.bytes &gt; 4294967295 &amp;&amp; (this.hBytes += this.bytes / 4294967296 &lt;&lt; 0,
            this.bytes = this.bytes % 4294967296),
            this
    }
}


Md5.prototype.finalize = function () {
    if (!this.finalized) {
        this.finalized = !0;
        var e = this.blocks
            , i = this.lastByteIndex;
        e[i &gt;&gt; 2] |= EXTRA[3 &amp; i],
        i &gt;= 56 &amp;&amp; (this.hashed || this.hash(),
            e[0] = e[16],
            e[16] = e[1] = e[2] = e[3] = e[4] = e[5] = e[6] = e[7] = e[8] = e[9] = e[10] = e[11] = e[12] = e[13] = e[14] = e[15] = 0),
            e[14] = this.bytes &lt;&lt; 3,
            e[15] = this.hBytes &lt;&lt; 3 | this.bytes &gt;&gt;&gt; 29,
            this.hash()
    }
}

Md5.prototype.hash = function () {
    var a, b, e, t, n, r, o = this.blocks;
    this.first ? b = ((b = ((a = ((a = o[0] - 680876937) &lt;&lt; 7 | a &gt;&gt;&gt; 25) - 271733879 &lt;&lt; 0) ^ (e = ((e = (-271733879 ^ (t = ((t = (-1732584194 ^ 2004318071 &amp; a) + o[1] - 117830708) &lt;&lt; 12 | t &gt;&gt;&gt; 20) + a &lt;&lt; 0) &amp; (-271733879 ^ a)) + o[2] - 1126478375) &lt;&lt; 17 | e &gt;&gt;&gt; 15) + t &lt;&lt; 0) &amp; (t ^ a)) + o[3] - 1316259209) &lt;&lt; 22 | b &gt;&gt;&gt; 10) + e &lt;&lt; 0 : (a = this.h0,
        b = this.h1,
        e = this.h2,
        b = ((b += ((a = ((a += ((t = this.h3) ^ b &amp; (e ^ t)) + o[0] - 680876936) &lt;&lt; 7 | a &gt;&gt;&gt; 25) + b &lt;&lt; 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a &amp; (b ^ e)) + o[1] - 389564586) &lt;&lt; 12 | t &gt;&gt;&gt; 20) + a &lt;&lt; 0) &amp; (a ^ b)) + o[2] + 606105819) &lt;&lt; 17 | e &gt;&gt;&gt; 15) + t &lt;&lt; 0) &amp; (t ^ a)) + o[3] - 1044525330) &lt;&lt; 22 | b &gt;&gt;&gt; 10) + e &lt;&lt; 0),
        b = ((b += ((a = ((a += (t ^ b &amp; (e ^ t)) + o[4] - 176418897) &lt;&lt; 7 | a &gt;&gt;&gt; 25) + b &lt;&lt; 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a &amp; (b ^ e)) + o[5] + 1200080426) &lt;&lt; 12 | t &gt;&gt;&gt; 20) + a &lt;&lt; 0) &amp; (a ^ b)) + o[6] - 1473231341) &lt;&lt; 17 | e &gt;&gt;&gt; 15) + t &lt;&lt; 0) &amp; (t ^ a)) + o[7] - 45705983) &lt;&lt; 22 | b &gt;&gt;&gt; 10) + e &lt;&lt; 0,
        b = ((b += ((a = ((a += (t ^ b &amp; (e ^ t)) + o[8] + 1770035416) &lt;&lt; 7 | a &gt;&gt;&gt; 25) + b &lt;&lt; 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a &amp; (b ^ e)) + o[9] - 1958414417) &lt;&lt; 12 | t &gt;&gt;&gt; 20) + a &lt;&lt; 0) &amp; (a ^ b)) + o[10] - 42063) &lt;&lt; 17 | e &gt;&gt;&gt; 15) + t &lt;&lt; 0) &amp; (t ^ a)) + o[11] - 1990404162) &lt;&lt; 22 | b &gt;&gt;&gt; 10) + e &lt;&lt; 0,
        b = ((b += ((a = ((a += (t ^ b &amp; (e ^ t)) + o[12] + 1804603682) &lt;&lt; 7 | a &gt;&gt;&gt; 25) + b &lt;&lt; 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a &amp; (b ^ e)) + o[13] - 40341101) &lt;&lt; 12 | t &gt;&gt;&gt; 20) + a &lt;&lt; 0) &amp; (a ^ b)) + o[14] - 1502002290) &lt;&lt; 17 | e &gt;&gt;&gt; 15) + t &lt;&lt; 0) &amp; (t ^ a)) + o[15] + 1236535329) &lt;&lt; 22 | b &gt;&gt;&gt; 10) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ e &amp; ((a = ((a += (e ^ t &amp; (b ^ e)) + o[1] - 165796510) &lt;&lt; 5 | a &gt;&gt;&gt; 27) + b &lt;&lt; 0) ^ b)) + o[6] - 1069501632) &lt;&lt; 9 | t &gt;&gt;&gt; 23) + a &lt;&lt; 0) ^ a &amp; ((e = ((e += (a ^ b &amp; (t ^ a)) + o[11] + 643717713) &lt;&lt; 14 | e &gt;&gt;&gt; 18) + t &lt;&lt; 0) ^ t)) + o[0] - 373897302) &lt;&lt; 20 | b &gt;&gt;&gt; 12) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ e &amp; ((a = ((a += (e ^ t &amp; (b ^ e)) + o[5] - 701558691) &lt;&lt; 5 | a &gt;&gt;&gt; 27) + b &lt;&lt; 0) ^ b)) + o[10] + 38016083) &lt;&lt; 9 | t &gt;&gt;&gt; 23) + a &lt;&lt; 0) ^ a &amp; ((e = ((e += (a ^ b &amp; (t ^ a)) + o[15] - 660478335) &lt;&lt; 14 | e &gt;&gt;&gt; 18) + t &lt;&lt; 0) ^ t)) + o[4] - 405537848) &lt;&lt; 20 | b &gt;&gt;&gt; 12) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ e &amp; ((a = ((a += (e ^ t &amp; (b ^ e)) + o[9] + 568446438) &lt;&lt; 5 | a &gt;&gt;&gt; 27) + b &lt;&lt; 0) ^ b)) + o[14] - 1019803690) &lt;&lt; 9 | t &gt;&gt;&gt; 23) + a &lt;&lt; 0) ^ a &amp; ((e = ((e += (a ^ b &amp; (t ^ a)) + o[3] - 187363961) &lt;&lt; 14 | e &gt;&gt;&gt; 18) + t &lt;&lt; 0) ^ t)) + o[8] + 1163531501) &lt;&lt; 20 | b &gt;&gt;&gt; 12) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ e &amp; ((a = ((a += (e ^ t &amp; (b ^ e)) + o[13] - 1444681467) &lt;&lt; 5 | a &gt;&gt;&gt; 27) + b &lt;&lt; 0) ^ b)) + o[2] - 51403784) &lt;&lt; 9 | t &gt;&gt;&gt; 23) + a &lt;&lt; 0) ^ a &amp; ((e = ((e += (a ^ b &amp; (t ^ a)) + o[7] + 1735328473) &lt;&lt; 14 | e &gt;&gt;&gt; 18) + t &lt;&lt; 0) ^ t)) + o[12] - 1926607734) &lt;&lt; 20 | b &gt;&gt;&gt; 12) + e &lt;&lt; 0,
        b = ((b += ((r = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + o[5] - 378558) &lt;&lt; 4 | a &gt;&gt;&gt; 28) + b &lt;&lt; 0)) + o[8] - 2022574463) &lt;&lt; 11 | t &gt;&gt;&gt; 21) + a &lt;&lt; 0) ^ a) ^ (e = ((e += (r ^ b) + o[11] + 1839030562) &lt;&lt; 16 | e &gt;&gt;&gt; 16) + t &lt;&lt; 0)) + o[14] - 35309556) &lt;&lt; 23 | b &gt;&gt;&gt; 9) + e &lt;&lt; 0,
        b = ((b += ((r = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + o[1] - 1530992060) &lt;&lt; 4 | a &gt;&gt;&gt; 28) + b &lt;&lt; 0)) + o[4] + 1272893353) &lt;&lt; 11 | t &gt;&gt;&gt; 21) + a &lt;&lt; 0) ^ a) ^ (e = ((e += (r ^ b) + o[7] - 155497632) &lt;&lt; 16 | e &gt;&gt;&gt; 16) + t &lt;&lt; 0)) + o[10] - 1094730640) &lt;&lt; 23 | b &gt;&gt;&gt; 9) + e &lt;&lt; 0,
        b = ((b += ((r = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + o[13] + 681279174) &lt;&lt; 4 | a &gt;&gt;&gt; 28) + b &lt;&lt; 0)) + o[0] - 358537222) &lt;&lt; 11 | t &gt;&gt;&gt; 21) + a &lt;&lt; 0) ^ a) ^ (e = ((e += (r ^ b) + o[3] - 722521979) &lt;&lt; 16 | e &gt;&gt;&gt; 16) + t &lt;&lt; 0)) + o[6] + 76029189) &lt;&lt; 23 | b &gt;&gt;&gt; 9) + e &lt;&lt; 0,
        b = ((b += ((r = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + o[9] - 640364487) &lt;&lt; 4 | a &gt;&gt;&gt; 28) + b &lt;&lt; 0)) + o[12] - 421815835) &lt;&lt; 11 | t &gt;&gt;&gt; 21) + a &lt;&lt; 0) ^ a) ^ (e = ((e += (r ^ b) + o[15] + 530742520) &lt;&lt; 16 | e &gt;&gt;&gt; 16) + t &lt;&lt; 0)) + o[2] - 995338651) &lt;&lt; 23 | b &gt;&gt;&gt; 9) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + o[0] - 198630844) &lt;&lt; 6 | a &gt;&gt;&gt; 26) + b &lt;&lt; 0) | ~e)) + o[7] + 1126891415) &lt;&lt; 10 | t &gt;&gt;&gt; 22) + a &lt;&lt; 0) ^ ((e = ((e += (a ^ (t | ~b)) + o[14] - 1416354905) &lt;&lt; 15 | e &gt;&gt;&gt; 17) + t &lt;&lt; 0) | ~a)) + o[5] - 57434055) &lt;&lt; 21 | b &gt;&gt;&gt; 11) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + o[12] + 1700485571) &lt;&lt; 6 | a &gt;&gt;&gt; 26) + b &lt;&lt; 0) | ~e)) + o[3] - 1894986606) &lt;&lt; 10 | t &gt;&gt;&gt; 22) + a &lt;&lt; 0) ^ ((e = ((e += (a ^ (t | ~b)) + o[10] - 1051523) &lt;&lt; 15 | e &gt;&gt;&gt; 17) + t &lt;&lt; 0) | ~a)) + o[1] - 2054922799) &lt;&lt; 21 | b &gt;&gt;&gt; 11) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + o[8] + 1873313359) &lt;&lt; 6 | a &gt;&gt;&gt; 26) + b &lt;&lt; 0) | ~e)) + o[15] - 30611744) &lt;&lt; 10 | t &gt;&gt;&gt; 22) + a &lt;&lt; 0) ^ ((e = ((e += (a ^ (t | ~b)) + o[6] - 1560198380) &lt;&lt; 15 | e &gt;&gt;&gt; 17) + t &lt;&lt; 0) | ~a)) + o[13] + 1309151649) &lt;&lt; 21 | b &gt;&gt;&gt; 11) + e &lt;&lt; 0,
        b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + o[4] - 145523070) &lt;&lt; 6 | a &gt;&gt;&gt; 26) + b &lt;&lt; 0) | ~e)) + o[11] - 1120210379) &lt;&lt; 10 | t &gt;&gt;&gt; 22) + a &lt;&lt; 0) ^ ((e = ((e += (a ^ (t | ~b)) + o[2] + 718787259) &lt;&lt; 15 | e &gt;&gt;&gt; 17) + t &lt;&lt; 0) | ~a)) + o[9] - 343485551) &lt;&lt; 21 | b &gt;&gt;&gt; 11) + e &lt;&lt; 0,
        this.first ? (this.h0 = a + 1732584193 &lt;&lt; 0,
            this.h1 = b - 271733879 &lt;&lt; 0,
            this.h2 = e - 1732584194 &lt;&lt; 0,
            this.h3 = t + 271733878 &lt;&lt; 0,
            this.first = !1) : (this.h0 = this.h0 + a &lt;&lt; 0,
            this.h1 = this.h1 + b &lt;&lt; 0,
            this.h2 = this.h2 + e &lt;&lt; 0,
            this.h3 = this.h3 + t &lt;&lt; 0)
}

Md5.prototype.hex = function () {
    this.finalize();
    var e = this.h0
        , h1 = this.h1
        , h2 = this.h2
        , h3 = this.h3;
    return HEX_CHARS[e &gt;&gt; 4 &amp; 15] + HEX_CHARS[15 &amp; e] + HEX_CHARS[e &gt;&gt; 12 &amp; 15] + HEX_CHARS[e &gt;&gt; 8 &amp; 15] + HEX_CHARS[e &gt;&gt; 20 &amp; 15] + HEX_CHARS[e &gt;&gt; 16 &amp; 15] + HEX_CHARS[e &gt;&gt; 28 &amp; 15] + HEX_CHARS[e &gt;&gt; 24 &amp; 15] + HEX_CHARS[h1 &gt;&gt; 4 &amp; 15] + HEX_CHARS[15 &amp; h1] + HEX_CHARS[h1 &gt;&gt; 12 &amp; 15] + HEX_CHARS[h1 &gt;&gt; 8 &amp; 15] + HEX_CHARS[h1 &gt;&gt; 20 &amp; 15] + HEX_CHARS[h1 &gt;&gt; 16 &amp; 15] + HEX_CHARS[h1 &gt;&gt; 28 &amp; 15] + HEX_CHARS[h1 &gt;&gt; 24 &amp; 15] + HEX_CHARS[h2 &gt;&gt; 4 &amp; 15] + HEX_CHARS[15 &amp; h2] + HEX_CHARS[h2 &gt;&gt; 12 &amp; 15] + HEX_CHARS[h2 &gt;&gt; 8 &amp; 15] + HEX_CHARS[h2 &gt;&gt; 20 &amp; 15] + HEX_CHARS[h2 &gt;&gt; 16 &amp; 15] + HEX_CHARS[h2 &gt;&gt; 28 &amp; 15] + HEX_CHARS[h2 &gt;&gt; 24 &amp; 15] + HEX_CHARS[h3 &gt;&gt; 4 &amp; 15] + HEX_CHARS[15 &amp; h3] + HEX_CHARS[h3 &gt;&gt; 12 &amp; 15] + HEX_CHARS[h3 &gt;&gt; 8 &amp; 15] + HEX_CHARS[h3 &gt;&gt; 20 &amp; 15] + HEX_CHARS[h3 &gt;&gt; 16 &amp; 15] + HEX_CHARS[h3 &gt;&gt; 28 &amp; 15] + HEX_CHARS[h3 &gt;&gt; 24 &amp; 15]
}


function md5Hex(msg) {
    const md5 = new Md5();
    md5.update(msg);
    return md5.hex();
}

const input = process.argv[2];
const result = md5Hex(input);
console.log(result);
```

最终查询问题的主函数代码如下

```
import requests
import json
import time
import Getsign
import Login
import uuid


def getToken(phone, password):
    try:
        token = Login.getLoginToken(phone, password)
        return token
    except:
        print("Failed to retrieve token")
        return None


def search(question, token, time):

    url = "https://www.kaoshibao.com/api/search/questions"
    cookie = str(uuid.uuid4())
    sign = Getsign.sign(t=cookie, n=time, c=url)
    proxies = {"http": "http://127.0.0.1:10809", "https": "http://127.0.0.1:10809"}



    headers = {
        "Authorization": "%22" + token + "=%22",
        "Cookie": "uu=" + cookie + "; token=" + token,
        "Sign": sign,
        "TimeStamp": time,
    }

    data = {
        "keyword": "\"" + question + "\"",
        "page": "1",
        "paperid": "\"\"",
        "qtype": "\"\"",
        "size": "20"
    }

    response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

    # 将响应文本转换为JSON格式
    data_json = json.loads(response.text)

    # 转换Unicode编码并打印结果
    print(json.dumps(data_json, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    time = str(time.time())
    search("mysql", "", time)

```

可以配合用户名密码登录获取token

```
import requests
import json
import PasswordEncrypt
import uuid
import time
import Getsign


def getLoginToken(phone, password):
    proxies = {"http": "http://127.0.0.1:10809", "https": "http://127.0.0.1:10809"}

    url = "https://www.kaoshibao.com/api/user/login"

    IDENTIFIER = str(uuid.uuid4())
    time1 = str(time.time())

    headers = {
        "CLIENT-IDENTIFIER": IDENTIFIER,
        "Sign": Getsign.sign(t=IDENTIFIER, n=time1, c=url),
        "TimeStamp": time1,
    }

    password = PasswordEncrypt.password(password)

    data = {
        "password": password,
        "phone": phone,
    }

    response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

    # 检查响应状态码
    if response.status_code == 200:
        json_data = json.loads(response.text)
        print(json_data)
        if json_data["code"] == '200':
            print(json_data["data"]["token"])
            return json_data["data"]["token"]
        else:
            print("Failed to retrieve token: Code", json_data["code"])
            return "Failed to retrieve token: Code", json_data["code"]

    else:
        print("Failed to retrieve cookies: Status code", response.status_code)

getLoginToken("12222222222", "123456")
```

最终获得的数据如下，对其处理一下即可。

<img alt="" height="527" src="https://img-blog.csdnimg.cn/direct/98b58cfc67a94c8ca3053ac1d3eb8549.png" width="1200">

完整代码地址

```
https://github.com/incredibleeeeee/kaoshibao/tree/master/PythonTest/kaoshibao
```










