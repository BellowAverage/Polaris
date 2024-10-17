
--- 
title:  泛微移动平台e-mobile漏洞利用 
tags: []
categories: [] 

---
### 泛微移动平台e-mobile漏洞利用基本信息

漏洞情报编号：vulbox-intel-15244

是否可自动化组件：是

CVE-ID：暂无

发布日期：2022/04/01 15:48:45

CNNVD-ID：暂无

最新更新时间：2022/04/08 18:02:59

CNVD-ID：CNVD-2017-02376

漏洞类型：

其它

<img alt="" height="372" src="https://img-blog.csdnimg.cn/da7de20ca0484ed7a27bfdddf96495ed.png" width="825">

 

### 泛微移动平台e-mobile漏洞利用漏洞危害

恶意攻击者可通过SQL注入漏洞构造SQL注入语句，对服务器端返回特定的错误信息来获取有利用价值的信息，甚至可篡改数据库中的内容并进行提权

### 泛微移动平台e-mobile漏洞利用影响范围

上海泛微网络科技股份有限公司 移动OA解决方案e-mobile

### 泛微移动平台e-mobile漏洞利用漏洞复现

<img alt="" height="271" src="https://img-blog.csdnimg.cn/2fa9d34024714c4d85823d8fdbb52e0e.png" width="670">

 

### 泛微移动平台e-mobile漏洞利用的修复方案

1. 对产生漏洞模块的传入参数进行有效性检测，对传入的参数进行限定 2. 当用户输入限定字符时，立刻转向自定义的错误页，不能使用服务器默认的错误输出方式 3. 对以上标签进行危险字符过滤，禁止('、"、+、%、&amp;、&lt;&gt;、（）、;、and、select等)特殊字符的传入 4. 加密数据库内存储信息 5. 与数据库链接并访问数据时，使用参数化查询方式进行链接访问

 
