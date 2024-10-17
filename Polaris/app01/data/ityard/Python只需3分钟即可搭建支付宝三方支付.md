
--- 
title:  Python只需3分钟即可搭建支付宝三方支付 
tags: []
categories: [] 

---
**为什么使用三方支付？**

再没有三方支付平台之前，用户发起支付请求的时候，用户要去和银行签约(转账)，特别的不方便，为了解决这些问题，就有了三方支付，三方平台去完成签约，给用户节省时间。

**支付宝支付的流程**

商户拿到支付宝的公钥、自己的私钥（私钥加密、公钥解密），用私钥请求支付宝，支付宝解密、验签、进行支付处理，支付宝将处理的返回值传给商户，当支付成功后，返还给商户订单号、金额、时间戳等消息，支付失败后同样给商户反馈结果。

**配置流程**

**1、获取APPID**

>  
  支付宝开放平台:https://open.alipay.com/ 
 
- 登录支付宝开放平台–&gt;点击控制台
<img src="https://img-blog.csdnimg.cn/img_convert/a545b5699bb7ada83f46d86ae021edff.png" alt="a545b5699bb7ada83f46d86ae021edff.png">
- 点击沙箱(复制APPID)
<img src="https://img-blog.csdnimg.cn/img_convert/c7d66d1b8c29647882359ebef6de5763.png" alt="c7d66d1b8c29647882359ebef6de5763.png">

**2、在线生成密钥**
- 点击文档，找到开发助手，点击在线加密。
<img src="https://img-blog.csdnimg.cn/img_convert/f65a4766640a26b14074067e55faedee.png" alt="f65a4766640a26b14074067e55faedee.png">
- 获取私钥
<img src="https://img-blog.csdnimg.cn/img_convert/410369cf174e6541d7576d97ed48d489.png" alt="410369cf174e6541d7576d97ed48d489.png">

**3、获取公钥**
- 点击应用公钥
<img src="https://img-blog.csdnimg.cn/img_convert/e1ed38a90bcfe1dbe26194566c2b397d.png" alt="e1ed38a90bcfe1dbe26194566c2b397d.png">
- 生成公钥
<img src="https://img-blog.csdnimg.cn/img_convert/0689d7124ae73363e19f87e0ecf32ff8.png" alt="0689d7124ae73363e19f87e0ecf32ff8.png">

现在已经拿到了需要的公钥。

**python项目中集成支付宝**
- 构建支付类
```
from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib.parse import quote_plus
from base64 import decodebytes, encodebytes
import json




class AliPay:
    """
    支付宝支付接口(PC端支付接口)
    """




    def __init__(self, appid, app_notify_url, app_private_key_path,
                 alipay_public_key_path, return_url, debug=False):
        self.appid = appid
        self.app_notify_url = app_notify_url
        self.app_private_key_path = app_private_key_path
        self.app_private_key = None
        self.return_url = return_url
        with open(self.app_private_key_path) as fp:
            self.app_private_key = RSA.importKey(fp.read())
        self.alipay_public_key_path = alipay_public_key_path
        with open(self.alipay_public_key_path) as fp:
            self.alipay_public_key = RSA.importKey(fp.read())




        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"




    def direct_pay(self, subject, out_trade_no, total_amount, return_url=None, **kwargs):
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FAST_INSTANT_TRADE_PAY",
        }




        biz_content.update(kwargs)
        data = self.build_body("alipay.trade.page.pay", biz_content, self.return_url)
        return self.sign_data(data)




    def build_body(self, method, biz_content, return_url=None):
        data = {
            "app_id": self.appid,
            "method": method,
            "charset": "utf-8",
            "sign_type": "RSA2",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0",
            "biz_content": biz_content
        }




        if return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url




        return data




    def sign_data(self, data):
        data.pop("sign", None)
        unsigned_items = self.ordered_data(data)
        unsigned_string = "&amp;".join("{0}={1}".format(k, v) for k, v in unsigned_items)
        sign = self.sign(unsigned_string.encode("utf-8"))
        quoted_string = "&amp;".join("{0}={1}".format(k, quote_plus(v)) for k, v in unsigned_items)




        signed_string = quoted_string + "&amp;sign=" + quote_plus(sign)
        return signed_string




    def ordered_data(self, data):
        complex_keys = []
        for key, value in data.items():
            if isinstance(value, dict):
                complex_keys.append(key)




        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',', ':'))




        return sorted([(k, v) for k, v in data.items()])




    def sign(self, unsigned_string):
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(unsigned_string))
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        return sign




    def _verify(self, raw_content, signature):
        key = self.alipay_public_key
        signer = PKCS1_v1_5.new(key)
        digest = SHA256.new()
        digest.update(raw_content.encode("utf8"))
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False




    def verify(self, data, signature):
        if "sign_type" in data:
            data.pop("sign_type")
        unsigned_items = self.ordered_data(data)
        message = "&amp;".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(message, signature)
```
- 实例化类
```
def init_alipay():
    # 初始化Alipay
    alipay = AliPay(
        appid="appid",
        app_notify_url="回调地址",
        return_url="回调地址",
        app_private_key_path="私钥相对路径",
        alipay_public_key_path="公钥相对路径",
        debug=True  # 支付环境
    )
    return alipay
```
- API
```
async def get(self):


    alipay = init_alipay()
    # 传一个标题  订单号  订单价格
    params = alipay.direct_pay("三方广告平台", order_no, money)
    url = f"https://openapi.alipaydev.com/gateway.do?{params}"
    return self.write(ret_json(url))




# 构建一个回调地址,用于支付成功后回调,在回调地址中可以获取订单号(out_trade_no)、金额(total_amount)、时间戳(timestamp),然后进行处理业务逻辑。
```

#### 

#### **总结**

支付包有自己的接口文档，以上是我在Python环境下配置的，可以直接使用。

版权声明：本文为博主原创文章，遵循 CC 4.0 BY 版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/weixin_45394086/article/details/121843483
