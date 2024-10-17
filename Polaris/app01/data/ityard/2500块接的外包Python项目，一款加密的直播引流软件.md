
--- 
title:  2500块接的外包Python项目，一款加密的直播引流软件 
tags: []
categories: [] 

---
### 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

### blog.csdn.net/Python_shannian/article/details/120059842

这次给大家带来的是一个2500的爬虫外包项目，在这里肯定有人说这个不值这么多，也有人会各种嘲讽。但是别忘了，人的眼界不一样，做事的决定自然会不同。

如果2500能给你带来25000的利润，那么你会选择毫不犹豫的支付吗？话不多说，看聊天记录，还是挺久以前做的了。（我后面再给大家一一道来，暂时先看咱们的教程。）

<img src="https://img-blog.csdnimg.cn/img_convert/85dca0d9820a339abdc59d52a2d40428.png">

## 分析（x0）

进入目标网站：https://www.laifeng.com/

<img src="https://img-blog.csdnimg.cn/img_convert/422dd2109455e44bbd374a53a3baf7d2.png" height="808" width="1200">

随便进入一个分类，点击进入某直播间

<img src="https://img-blog.csdnimg.cn/img_convert/2245e67a448d210e9916ab8b3f988beb.png" height="884" width="1200">

当我们点击弹幕直播框时，它会要求咱们登录账号。这也实属正常，没办法那咱们就登录吧。

登录成功后，咱们抓一下这个发送弹幕的包：

<img src="https://img-blog.csdnimg.cn/img_convert/d8db6d3459bc1aff00cd6176cd87fc97.png" height="907" width="1200">

确实尴尬，我不知道发送什么，就说了句您好，没想到小姐姐很惊讶的说您好，您也好......然后说听完一首《飘向北方》就下播了......我不知道他下播了后，我还是否可以发送弹幕。

不管了，我先抽支烟看看小姐姐听完这首歌再接着写。

emmm，roomid为直播间的房间号，content为我发送的内容。

roomid可以在url中看得到的，前面那个图我没截出来，自己看一下就知道了。

<img src="https://img-blog.csdnimg.cn/img_convert/838b6192dadcfe5d9aafdf789ac83d4e.png" height="224" width="1200">

t为时间戳，sign签名也是JavaScript加密的。其它值不变，自己发送两次弹幕抓包对比一下就好了。

## 分析（x1） 

有人会奇怪你怎么知道t为时间戳......这玩意还需要说么，还是说一下吧，查找一下t的来源，我觉得向这种短的参数，最好别直接搜t，你会搜出来一大堆的。我建议搜临近的值sign，因为你提交的表单中有这么多的参数，那么在js文件中基本也会有相对应的参数的。

<img src="https://img-blog.csdnimg.cn/img_convert/f8cb7f3eb9409da80a015f0eb2e8df37.png" height="736" width="1200">

t:i意思是把i赋值给t，而

```
i = (new Date).getTime()

```

哦豁，没学过前端的人就看不懂这个是啥意思了，这个其实就是JavaScript语法中的取现行时间。

在我们的鬼鬼js调试工具看看效果：

<img src="https://img-blog.csdnimg.cn/img_convert/0b2c1ac5b738a46ef53f1c9a75e75e63.gif">

可以看到是它是一直在变化的，就像咱们的时间一样一直在流逝变化。不懂什么是时间戳的自己去谷歌一下。

或者在咱们的控制台也可以得到它：

<img src="https://img-blog.csdnimg.cn/img_convert/1253c99c3aeef19801df9d9f7c27c782.png" height="741" width="1200">

既然它是利用JavaScript这么个语法生成的参数，那么我们用Python如何实现？

<img src="https://img-blog.csdnimg.cn/img_convert/6e7add6d3d415e7bd72da8406a8841d7.png" height="370" width="1178">

OK，至此已经解决第一个加密的参数。

## 分析（x2） 

接下来就是大头菜了，咱们分析sign签名是如何得到的：

<img src="https://img-blog.csdnimg.cn/img_convert/f8987dcda13bd5535ad1e95ed2f4d774.png" height="484" width="961">

好吧，很多位置参数，压根不知道是如何得来的但是可以看到它用到 i 这个参数，也就是咱们的时间戳。

还是debug一下吧：

<img src="https://img-blog.csdnimg.cn/img_convert/57e7042fe4405ae29563c69faefa7833.png" height="920" width="1200">

打个断点，在浏览器上随意发送一弹幕，发现g就是appkey是一个定值，c为一个字典，咱们要取的是c字典中data键所对应的值：

<img src="https://img-blog.csdnimg.cn/img_convert/6aaea9daed78010625379940d7f2c0f7.png" height="438" width="1043">

是不是好熟悉，这不就是咱们post中的data的值么？那么就只剩下d了。 

d为一个字典，而咱们需要的是d里面的一个叫token键对应的值：

<img src="https://img-blog.csdnimg.cn/img_convert/fb0ca4a75366145edbca025be690217f.png" height="495" width="1200">

凭我经验，这个d根本不需咱们去找它应该就是咱们的cookies，直接搜一下就完事了......

<img src="https://img-blog.csdnimg.cn/img_convert/97f2e4afcf42777a518125e6ad05eac7.png" height="601" width="1200">

那么到此为止，咱们的所有参数都已经分析完了，咱们开始测试一下：

<img src="https://img-blog.csdnimg.cn/img_convert/da7905c747daaef71a7ae894105920d7.png" height="649" width="938">

发现缺少对象，emmmmm我三十岁的人都没对象......这里毫无疑问就是少了h这个函数对象。

那么咱们去给它找出来即可

<img src="https://img-blog.csdnimg.cn/img_convert/b79c6a405c47cbe14ff445a27421c289.png" height="557" width="1193">

点一下这个花括号，然后这样子的话函数末也有出现这么一个横杠，然后把JavaScript代码抠下来再来测试：

<img src="https://img-blog.csdnimg.cn/img_convert/1be3acfd59cfef72b999292f218d5dea.gif">

OK，到此为止，咱们已经完成了百分之五十了，为什么最核心的部分完成确只完成百分之五十呢？因为这个项目为三个程序：自动对接接吗台子注册账号、房间ID号采集筛选出主播在线的ID号、咱们这个的话就是关键的发送程序。

## 代码

Python代码：

```
import requests
import execjs
import time




# 携带cookies进入主页
ck = '123456'
headers = {
    'authority': 'www.laifeng.com',
    'method': 'GET',
    'path': '/?',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'cookie': ck,
    'pragma': 'no-cache',


    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400',
}
url = 'https://www.laifeng.com/'
r = requests.get(url, headers=headers)
print(r.text)


# 进入直播间
url = f'https://v.laifeng.com/711329'
headers = {
    'authority': 'v.laifeng.com',
    'method': 'GET',
    'path':  '/711329',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'mk=453ed14d2f6e4871ba8f09cfefcba1a3; cna=XacYGCzzLgkCAW411IXRpIVk; P_ck_ctl=5633DEE6E3B29B5783C835500682978B; xlly_s=1; P_ck_ctr=870A7039ED41E1AF8A4E5AF9A7D413C5; premium_cps=0_0%7C76%7C85232%7C0___; cmk=80ff16e81ec844f7946cfb91262dc197; P_pck_rm=z99ATxqw33e2f40cb442c0ZBnFgC5IrE%2BWMeN4%2BR%2BFlfXo6CU2HuinwjayRmNzYP5BIz5HRZzLPXYEPoNGojmxulCSHs6dFdWS1WNMYs6WkVelQxcsN%2FkHwmDvakV1b8hA0MqQXvBvTdMeakZiDzsBNT%2BuFifi6PNbRVoQ%3D%3D%5FV2; P_gck=NA%7CPmRanzni%2BsGuV8NRBrUBaw%3D%3D%7CNA%7C1621735722621; P_sck=8agJlNkqujZS6MrSyNJwjanMcMbXipu2qC%2BxD4UmyvNoTDHSq7Nah1Epvqm%2FaUXXcspBt9AU9cvP8ksA8NHQKpdD9h1%2Bd0oOFKVzm2HD0ZkEUaPPVJ28NNQmgMPfzqvrbS6Rz1TAHSvGhiEJt9gmuQ%3D%3D; uk=1362040016; anchor-task-tips=vistived; fansTuan-tips=vistived; _m_h5_tk=298bfbf0d1f474b3cd1e7566f68193a1_1621744352184; _m_h5_tk_enc=2d0745b898b59366cf07b6efa7cd875b; isg=BGVlUl6Rac0flo0Rbvh1ju8VdCGfohk0iyhzDmdLjxyrfoTwL_CVBFBWCOII_jHs; imk=MTM2MjA0MDAxNi0xLTE2MjE3NDA2ODg4MDUtMTYyMTgyNzA4ODgwNQ%3D%3D-FC64AFD62649932D1C07520D9BCA6A50; __ysuid=1621740688797e9b',


    'pragma': 'no-cache',


    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400',
    'x-requested-with': 'XMLHttpRequest',
}
r = requests.get(url, headers=headers)
print(r)
print(r.text)


# 获取sign
t = str(int(time.time()*1000))
with open('js1.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


sign = ctx.call('test', '{"roomId":"711329","content":"找个壮男薇123456"}', t)
print(sign)




# 发送弹幕
url = f'https://acs.laifeng.com/h5/mtop.youku.live.platform.chat/1.0/?jsv=2.6.1&amp;appKey=24679788&amp;t={t}&amp;sign={sign}&amp;type=originaljson&amp;dataType=json&amp;api=mtop.youku.live.platform.chat&amp;v=1.0&amp;ecode=1'
data = {
    'data': '{"roomId":"711329","content":"找个壮男薇123456"}'
}


headers = {
    'authority': 'acs.laifeng.com',
    'method': 'POST',
    'path': f'/h5/mtop.youku.live.platform.chat/1.0/?jsv=2.6.1&amp;appKey=24679788&amp;t={t}&amp;sign={sign}&amp;type=originaljson&amp;dataType=json&amp;api=mtop.youku.live.platform.chat&amp;v=1.0&amp;ecode=1',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-length': '65',


    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mk=453ed14d2f6e4871ba8f09cfefcba1a3; cna=XacYGCzzLgkCAW411IXRpIVk; xlly_s=1; cmk=80ff16e81ec844f7946cfb91262dc197; P_gck=NA%7CPmRanzni%2BsGuV8NRBrUBaw%3D%3D%7CNA%7C1621735722621; uk=1362040016; anchor-task-tips=vistived; fansTuan-tips=vistived; P_sck=%2BUdo1iqrKx4%2FVd0vPYAbiHOpyqJ39%2Fw8brn2mmb2jYLlctldDNJ2qXSzYFPJDEYzodI65rDbJDzRtM6T7xkFNfREb9ajH8aAhsEioWLTbTp9LqNh%2ByYY7yW43dhpBBcSerlcOCmoajgMf%2BWzmhN7zw%3D%3D; P_pck_rm=z99ATxqw33e2f40cb442c0ZBnFgC5IrE%2BWMeN4%2BR%2BFlfXo6CU2HuinwjayRmNzYP5BIz5HRZzLPXYEPoNGojmxulCSHs6dFdWS1WNMYs6WkVelQxcsN%2FkHwmDvakV1b8hA0MqQXvBvTdMeakZiDzsBNT%2BuFifi6PNbRVoQ%3D%3D_V2; _m_h5_tk=83a19c51d0630a852efa9b4189393fca_1621764171783; _m_h5_tk_enc=2346991bccefcfc40b4ddb78c83c888f; __ysuid=1621760043001XhI; imk=MTM2MjA0MDAxNi0xLTE2MjE3NjAwNDM3MTAtMTYyMTg0NjQ0MzcxMA%3D%3D-1AEDB0971C2FA6CB9B62CAA7858E1C42; isg=BNHRDPTLVUpHT7ldmhTZitMx4N1rPkWwB8xnQrNkNxiMWvOs-ouggV6o_i68yd3o',
    'cookie': ck,
    'origin': 'https://v.laifeng.com',
    'pragma': 'no-cache',
    'referer': 'https://v.laifeng.com/711329',


    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400',
}
r = requests.post(url, headers=headers, data=data)
print(r)
print(r.text)

```

需要自己手动拿下登录页码的cookies，然后自己更改好发送的内容与房间id即可。

JavaScript源码：

```
function h(a) {
function b(a, b) {
    return a &lt;&lt; b | a &gt;&gt;&gt; 32 - b
}
function c(a, b) {
    var c, d, e, f, g;
    return e = 2147483648 &amp; a,
    f = 2147483648 &amp; b,
    c = 1073741824 &amp; a,
    d = 1073741824 &amp; b,
    g = (1073741823 &amp; a) + (1073741823 &amp; b),
    c &amp; d ? 2147483648 ^ g ^ e ^ f: c | d ? 1073741824 &amp; g ? 3221225472 ^ g ^ e ^ f: 1073741824 ^ g ^ e ^ f: g ^ e ^ f
}
function d(a, b, c) {
    return a &amp; b | ~a &amp; c
}
function e(a, b, c) {
    return a &amp; c | b &amp; ~c
}
function f(a, b, c) {
    return a ^ b ^ c
}
function g(a, b, c) {
    return b ^ (a | ~c)
}
function h(a, e, f, g, h, i, j) {
    return a = c(a, c(c(d(e, f, g), h), j)),
    c(b(a, i), e)
}
function i(a, d, f, g, h, i, j) {
    return a = c(a, c(c(e(d, f, g), h), j)),
    c(b(a, i), d)
}
function j(a, d, e, g, h, i, j) {
    return a = c(a, c(c(f(d, e, g), h), j)),
    c(b(a, i), d)
}
function k(a, d, e, f, h, i, j) {
    return a = c(a, c(c(g(d, e, f), h), j)),
    c(b(a, i), d)
}
function l(a) {
    for (var b, c = a.length,
    d = c + 8,
    e = (d - d % 64) / 64, f = 16 * (e + 1), g = new Array(f - 1), h = 0, i = 0; c &gt; i;) b = (i - i % 4) / 4,
    h = i % 4 * 8,
    g[b] = g[b] | a.charCodeAt(i) &lt;&lt; h,
    i++;
    return b = (i - i % 4) / 4,
    h = i % 4 * 8,
    g[b] = g[b] | 128 &lt;&lt; h,
    g[f - 2] = c &lt;&lt; 3,
    g[f - 1] = c &gt;&gt;&gt; 29,
    g
}
function m(a) {
    var b, c, d = "",
    e = "";
    for (c = 0; 3 &gt;= c; c++) b = a &gt;&gt;&gt; 8 * c &amp; 255,
    e = "0" + b.toString(16),
    d += e.substr(e.length - 2, 2);
    return d
}
function n(a) {
    a = a.replace(/\r\n/g, "\n");
    for (var b = "",
    c = 0; c &lt; a.length; c++) {
        var d = a.charCodeAt(c);
        128 &gt; d ? b += String.fromCharCode(d) : d &gt; 127 &amp;&amp; 2048 &gt; d ? (b += String.fromCharCode(d &gt;&gt; 6 | 192), b += String.fromCharCode(63 &amp; d | 128)) : (b += String.fromCharCode(d &gt;&gt; 12 | 224), b += String.fromCharCode(d &gt;&gt; 6 &amp; 63 | 128), b += String.fromCharCode(63 &amp; d | 128))
    }
    return b
}
var o, p, q, r, s, t, u, v, w, x = [],
y = 7,
z = 12,
A = 17,
B = 22,
C = 5,
D = 9,
E = 14,
F = 20,
G = 4,
H = 11,
I = 16,
J = 23,
K = 6,
L = 10,
M = 15,
N = 21;
for (a = n(a), x = l(a), t = 1732584193, u = 4023233417, v = 2562383102, w = 271733878, o = 0; o &lt; x.length; o += 16) p = t,
q = u,
r = v,
s = w,
t = h(t, u, v, w, x[o + 0], y, 3614090360),
w = h(w, t, u, v, x[o + 1], z, 3905402710),
v = h(v, w, t, u, x[o + 2], A, 606105819),
u = h(u, v, w, t, x[o + 3], B, 3250441966),
t = h(t, u, v, w, x[o + 4], y, 4118548399),
w = h(w, t, u, v, x[o + 5], z, 1200080426),
v = h(v, w, t, u, x[o + 6], A, 2821735955),
u = h(u, v, w, t, x[o + 7], B, 4249261313),
t = h(t, u, v, w, x[o + 8], y, 1770035416),
w = h(w, t, u, v, x[o + 9], z, 2336552879),
v = h(v, w, t, u, x[o + 10], A, 4294925233),
u = h(u, v, w, t, x[o + 11], B, 2304563134),
t = h(t, u, v, w, x[o + 12], y, 1804603682),
w = h(w, t, u, v, x[o + 13], z, 4254626195),
v = h(v, w, t, u, x[o + 14], A, 2792965006),
u = h(u, v, w, t, x[o + 15], B, 1236535329),
t = i(t, u, v, w, x[o + 1], C, 4129170786),
w = i(w, t, u, v, x[o + 6], D, 3225465664),
v = i(v, w, t, u, x[o + 11], E, 643717713),
u = i(u, v, w, t, x[o + 0], F, 3921069994),
t = i(t, u, v, w, x[o + 5], C, 3593408605),
w = i(w, t, u, v, x[o + 10], D, 38016083),
v = i(v, w, t, u, x[o + 15], E, 3634488961),
u = i(u, v, w, t, x[o + 4], F, 3889429448),
t = i(t, u, v, w, x[o + 9], C, 568446438),
w = i(w, t, u, v, x[o + 14], D, 3275163606),
v = i(v, w, t, u, x[o + 3], E, 4107603335),
u = i(u, v, w, t, x[o + 8], F, 1163531501),
t = i(t, u, v, w, x[o + 13], C, 2850285829),
w = i(w, t, u, v, x[o + 2], D, 4243563512),
v = i(v, w, t, u, x[o + 7], E, 1735328473),
u = i(u, v, w, t, x[o + 12], F, 2368359562),
t = j(t, u, v, w, x[o + 5], G, 4294588738),
w = j(w, t, u, v, x[o + 8], H, 2272392833),
v = j(v, w, t, u, x[o + 11], I, 1839030562),
u = j(u, v, w, t, x[o + 14], J, 4259657740),
t = j(t, u, v, w, x[o + 1], G, 2763975236),
w = j(w, t, u, v, x[o + 4], H, 1272893353),
v = j(v, w, t, u, x[o + 7], I, 4139469664),
u = j(u, v, w, t, x[o + 10], J, 3200236656),
t = j(t, u, v, w, x[o + 13], G, 681279174),
w = j(w, t, u, v, x[o + 0], H, 3936430074),
v = j(v, w, t, u, x[o + 3], I, 3572445317),
u = j(u, v, w, t, x[o + 6], J, 76029189),
t = j(t, u, v, w, x[o + 9], G, 3654602809),
w = j(w, t, u, v, x[o + 12], H, 3873151461),
v = j(v, w, t, u, x[o + 15], I, 530742520),
u = j(u, v, w, t, x[o + 2], J, 3299628645),
t = k(t, u, v, w, x[o + 0], K, 4096336452),
w = k(w, t, u, v, x[o + 7], L, 1126891415),
v = k(v, w, t, u, x[o + 14], M, 2878612391),
u = k(u, v, w, t, x[o + 5], N, 4237533241),
t = k(t, u, v, w, x[o + 12], K, 1700485571),
w = k(w, t, u, v, x[o + 3], L, 2399980690),
v = k(v, w, t, u, x[o + 10], M, 4293915773),
u = k(u, v, w, t, x[o + 1], N, 2240044497),
t = k(t, u, v, w, x[o + 8], K, 1873313359),
w = k(w, t, u, v, x[o + 15], L, 4264355552),
v = k(v, w, t, u, x[o + 6], M, 2734768916),
u = k(u, v, w, t, x[o + 13], N, 1309151649),
t = k(t, u, v, w, x[o + 4], K, 4149444226),
w = k(w, t, u, v, x[o + 11], L, 3174756917),
v = k(v, w, t, u, x[o + 2], M, 718787259),
u = k(u, v, w, t, x[o + 9], N, 3951481745),
t = c(t, p),
u = c(u, q),
v = c(v, r),
w = c(w, s);
var O = m(t) + m(u) + m(v) + m(w);
return O.toLowerCase()
}
function test(tk, data_one, i) {
g = "24679788";
/i = (new Date).getTime();
j = h(tk + "&amp;" + i + "&amp;" + g + "&amp;" + data_one);
return j;
}

```

## 效果

<img src="https://img-blog.csdnimg.cn/img_convert/b54064673d85eda1cd5e6c821ba02ed7.gif">

**点赞，在看，转发**三连哦~
