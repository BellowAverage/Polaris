
--- 
title:  Android WebView安全方面的一些坑 
tags: []
categories: [] 

---
>  
 公司一款app有将近两年没有更新了，虽然用户量不大，但是因为与第三方有合作，出现问题时需要进行维护；没想到最近第三方对他们所有的软件进行了网络安全扫描，这款`Android app`也未能幸免… 


<img src="https://img-blog.csdnimg.cn/img_convert/c18555d246f8d2c15e067197e8d47688.jpeg" alt="Android安全问题（WebView）">

因为`app`是13年左右开发的，维护也只是到`16、17`年左右就终止了，所以，扫描出不少漏洞；因为是采用了`webview+html`混合开发，因此，需要解决一些`webview`相关的问题：

#### 一、webview隐藏接口问题（任意命令执行漏洞）

`android webview`组件包含3个隐藏的系统接口：`searchBoxJavaBridge_`, `accessibilityTraversal`以及`accessibility`，恶意程序可以通过反射机制利用它们实现远程代码执行；该问题在`Android4.4`以下版本出现。 于是，在`Android3.0`到`4.4`之间的版本，我们通过移除这些隐藏接口，来解决该问题：

```
 // 19  4.4  Build.VERSION.KITKAT
    // 11  3.0  Build.VERSION_CODES.HONEYCOMB
    if(Build.VERSION.SDK_INT &gt;= Build.VERSION_CODES.HONEYCOMB 
        &amp;&amp; Build.VERSION.SDK_INT &lt; 19 &amp;&amp; webView != null) { 
        webView.removeJavascriptInterface("searchBoxJavaBridge_");
        webView.removeJavascriptInterface("accessibility");
        webView.removeJavascriptInterface("accessibilityTraversal");
    } 

```

#### 二、addJavascriptInterface任何命令执行漏洞

在`webview`中使用`js`与`html`进行交互是一个不错的方式，但是，在`Android4.2(16，包含4.2)`及以下版本中，如果使用`addJavascriptInterface`，则会存在被注入`js接口的`漏洞；在`4.2`之后，由于`Google`增加了`@JavascriptInterface`，该漏洞得以解决。

解决该问题，最彻底的方式是在`4.2`以下放弃使用`addJavascriptInterface`，采用`onJsPrompt`或其它方法替换。或者使用一些方案来降低该漏洞导致的风险：如使用`https`并进行证书校验，如果是`http`则进行页面完整性校验，如上面所述移除隐藏接口等。

```
 public boolean onJsPrompt(WebView view, String url, String message,String defaultValue, JsPromptResult result) {
        result.confirm(CGJSBridge.callJava(view, message));
        Toast.makeText(view.getContext(),"message="+message,Toast.LENGTH_LONG).show();
        return true;
    } 

```

#### 三、绕过证书校验漏洞

`webviewClient`中有`onReceivedError`方法，当出现证书校验错误时，我们可以在该方法中使用`handler.proceed()`来忽略证书校验继续加载网页，或者使用默认的`handler.cancel()`来终端加载。 因为我们使用了`handler.proceed()`，由此产生了该“绕过证书校验漏洞”。 如果确定所有页面都能满足证书校验，则不必要使用`handler.proceed()`

```
 @SuppressLint("NewApi")
    @Override
    public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error) {
        //handler.proceed();// 接受证书
        super.onReceivedSslError(view, handler, error);
    } 

```

#### 四、allowFileAccess导致的File域同源策略绕过漏洞

如果`webview.getSettings().setAllowFileAccess(boolean)`设置为`true`，则会面临该问题；该漏洞是通过`WebView`对`Javascript`的延时执行和html文件替换产生的。 解决方案是禁止`WebView`页面打开本地文件，即

```
 webview.getSettings().setAllowFileAccess(false); 

```

或者更直接的禁止使用`JavaScript`

```
 webview.getSettings().setJavaScriptEnabled(false); 

```

### 题外话

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。 <img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
