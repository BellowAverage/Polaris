
--- 
title:  使用python+selenium+PantomJs+javascript爬取专利数据 
tags: []
categories: [] 

---
### 环境准备
- 安装-  - 下载.exe
### 爬取目标
- - 爬取专利名，申请人，发明人等
### 爬取过程
<li>通过selenium获取PhantomJs的webdriver实例 
  <ul><li>先导入webdriver的包 
    <blockquote> 
     from selenium import webdriver 
    </blockquote></li><li>获取实例 
    <blockquote> 
     driver = webdriver.PhantomJS(executable_path=’.\res\phantomjs.exe’) 
    </blockquote></li></ul> 其中，executable_path为PhantomJs.exe的位置。</li><li>连接网址  
  <blockquote> 
   driver.get(url_path) 
  </blockquote></li><li>填写查询信息 
  1. 通过chrome查看了元素的dom，如图：  <img src="https://img-blog.csdn.net/20170403012121315?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">1. 根据显示编写js代码，然后用webdriver执行脚本，举个例子 
  <blockquote> 
   driver.execute_script(“document.getElementById(\”tableSearchItemIdIVDB021\”).setAttribute(\”value\”,\”” + inventor + “\”)”) 
  </blockquote> 
  1. 填写完相应参数后，提交表单。</li><li>采集数据 
  <ul>1. 根据chrome获取各个参数的路径。如图  <img src="https://img-blog.csdn.net/20170403013147896?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title=""><li>通过webdriver执行js脚本，获取各参数，举个例子 
    <blockquote> 
     driver.execute_script(“return document.getElementsByClassName(\”item\”).length;”) 
    </blockquote></li></ul></li><li>采集过程中，可能会遇到各种各样的问题，比方说： 
  <ul><li>查询超时，需要刷新浏览器，可用 
    <blockquote> 
     driver.refresh() 
    </blockquote></li><li>可能需要判断页面中含有什么字符串，可通过一下代码获取： 
    <blockquote> 
     driver.page_source 
    </blockquote></li><li>关闭浏览器 
    <blockquote> 
     driver.quit() 
    </blockquote></li></ul></li>
>  
   driver.get(url_path) 
  
- 通过chrome查看了元素的dom，如图：  <img src="https://img-blog.csdn.net/20170403012121315?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">- 根据显示编写js代码，然后用webdriver执行脚本，举个例子- 根据chrome获取各个参数的路径。如图  <img src="https://img-blog.csdn.net/20170403013147896?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title=""><li>通过webdriver执行js脚本，获取各参数，举个例子 
    <blockquote> 
     driver.execute_script(“return document.getElementsByClassName(\”item\”).length;”) 
    </blockquote></li>
>  
     driver.page_source 
    

### 代码资源





代码中含有将xlwt,xlrd和xlutils用工厂模式封装的excel操作模块，可供参考。
