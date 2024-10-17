
--- 
title:  Html 中使用 div 让两个表格并列排列 
tags: []
categories: [] 

---
示例的 html 行数有点多，请见谅（不过至少可以直接拿去用浏览器打开，也还是很方便的）。

**起因是这样的，我想将两个表格并列排列在同一行，**最先的想法是像下面这么弄（弄两个 &lt;div&gt; 把 &lt;table&gt; 套进去，并设置各自 &lt;div&gt; 的 width 百分比）。

```
&lt;html&gt;
 &lt;body&gt;
  &lt;h1 id="div2" align="center" style="margin-bottom:0px;padding-bottom:0px;font-size:1.625em;"&gt;so compare&lt;/h1&gt;&lt;br&gt;
  &lt;div style="width:20%;hight:100%;float:left;"&gt;
  &lt;table style="border-collapse:collapse;border:1px outset black;"&gt;
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;package&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;centos7.6&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libc-2.17.so&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libdl-2.17.so&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpthread-2.17.so&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;pcre&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpcre.so.1.2.0&lt;/td&gt;
    &lt;/tr&gt;
    &lt;/table&gt;
  &lt;/div&gt;
  &lt;div style="width:80%;hight:100%;float:left;"&gt;
  &lt;table style="border-collapse:collapse;border:1px outset black;"&gt;
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;package&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openEuler20.03&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libc-2.28.so&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libdl-2.28.so&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpthread-2.28.so&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libxcrypt&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libcrypt.so.1.1.0&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openssl-libs&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libcrypto.so.1.1.1f&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openssl-libs&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libssl.so.1.1.1f&lt;/td&gt;
    &lt;/tr&gt;
    
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;pcre&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpcre.so.1.2.12&lt;/td&gt;
    &lt;/tr&gt;
    &lt;/table&gt;
  &lt;/div&gt;&lt;br&gt;&lt;hr&gt;
 &lt;/body&gt;
&lt;/html&gt;
```

效果如下：

<img alt="" height="289" src="https://img-blog.csdnimg.cn/20210324171934273.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="928">

除了分割线离表格底部比较近之外（可以在第二个 &lt;table&gt; 外边套一个 &lt;form&gt; &lt;/form&gt; 来进行解决），其他好像没啥问题。

<img alt="" height="303" src="https://img-blog.csdnimg.cn/20210324172154628.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="968">

但是当我对网页进行缩放之后，问题就暴露出来了。

<img alt="" height="440" src="https://img-blog.csdnimg.cn/20210324172521231.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1039">

放大之后，这两个表格竟然有部分重叠（这可不是我希望的），所以只好再另外想想办法了。

于是乎，为了让两个 &lt;table&gt; 可以并列排列在同一行（不管怎么样，都不会重叠），我还是将两个 &lt;table&gt; 都包裹在了各自的 &lt;div&gt; 里边，并把样式设置为了 style="display:inline-block"。

```

&lt;html&gt;
&lt;body&gt;
  &lt;h1 id="div2" align="center" style="margin-bottom:0px;padding-bottom:0px;font-size:1.625em;"&gt;so compare&lt;/h1&gt;&lt;br&gt;
  &lt;div style="display:inline-block;margin-right:20px;float: left;"&gt;

  &lt;table style="border-collapse:collapse;border:1px outset black;"&gt;
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;package&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;centos7.6&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libc-2.28.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libdl-2.28.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpthread-2.28.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libxcrypt&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libcrypt.so.1.1.0&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openssl-libs&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libcrypto.so.1.1.1f&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openssl-libs&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libssl.so.1.1.1f&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;pcre&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpcre.so.1.2.12&lt;/td&gt;
    &lt;/tr&gt;
    &lt;/table&gt;
    &lt;/div&gt;
    &lt;div style="display:inline-block;float: none;"&gt;

  &lt;table style="border-collapse:collapse;border:1px outset black;"&gt;
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;package&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openEuler20.03&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libc-2.17.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libdl-2.17.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpthread-2.17.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;pcre&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpcre.so.1.2.0&lt;/td&gt;
    &lt;/tr&gt;
    &lt;/table&gt;
    &lt;/div&gt;
  &lt;br&gt;&lt;br&gt;&lt;hr&gt;
 &lt;/body&gt;
&lt;/html&gt;
```

上面的 html 可以实现如图效果： 

<img alt="" height="246" src="https://img-blog.csdnimg.cn/2021032417044262.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1049">

然鹅有个尴尬的问题就是，最后的 &lt;hr&gt; 分割线竟然没有贯穿整行，这可也不是我希望的（我当然希望分割线是在贯穿整行而且不会穿过表格）。

解决办法： 在两个 &lt;div&gt; 外边再套一层 &lt;div&gt; ，并将这个最外层的 &lt;div&gt; 的样式修改为 &lt;div style="display:inline-block"&gt;。

最后的效果就是下面这样（你可以肆意缩放，它们都不会再有重叠的部分啦）：

<img alt="" height="267" src="https://img-blog.csdnimg.cn/20210324170810625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="955">

```

&lt;html&gt;
&lt;body&gt;
  &lt;h1 id="div2" align="center" style="margin-bottom:0px;padding-bottom:0px;font-size:1.625em;"&gt;so compare&lt;/h1&gt;&lt;br&gt;
  &lt;div style="display:inline-block"&gt;
      &lt;div style="display:inline-block;margin-right:20px;float: left;"&gt;

  &lt;table style="border-collapse:collapse;border:1px outset black;"&gt;
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;package&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;centos7.6&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libc-2.28.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libdl-2.28.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpthread-2.28.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libxcrypt&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libcrypt.so.1.1.0&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openssl-libs&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libcrypto.so.1.1.1f&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openssl-libs&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libssl.so.1.1.1f&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;pcre&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpcre.so.1.2.12&lt;/td&gt;
    &lt;/tr&gt;
    &lt;/table&gt;
      &lt;/div&gt;
   &lt;div style="display:inline-block;float: none;"&gt;

  &lt;table style="border-collapse:collapse;border:1px outset black;"&gt;
   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;package&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;openEuler20.03&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libc-2.17.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libdl-2.17.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;glibc&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpthread-2.17.so&lt;/td&gt;
    &lt;/tr&gt;

   &lt;tr&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;pcre&lt;/td&gt;
    &lt;td class="row" style="background-color:#eeeeee;font-weight:bold;text-align:left;font-size:0.94em;white-space:nowrap;border:1px inset gray;padding: 3px;"&gt;libpcre.so.1.2.0&lt;/td&gt;
    &lt;/tr&gt;
    &lt;/table&gt;
   &lt;/div&gt;
  &lt;/div&gt;
  &lt;br&gt;&lt;br&gt;&lt;hr&gt;
 &lt;/body&gt;
&lt;/html&gt;
```

 
