
--- 
title:  [ vulhub漏洞复现篇 ] vulhub 漏洞集合（含漏洞复现文章连接） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ Vulhub是一个面向大众的开源漏洞靶场，无需docker知识，简单执行两条命令即可编译、运行一个完整的漏洞靶场镜像。旨在让漏洞复现变得更加简单，让安全研究者更加专注于漏洞原理本身。 




#### 文章目录
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## 前言

介绍：Vulhub是一个面向大众的开源漏洞靶场，无需docker知识，简单执行两条命令即可编译、运行一个完整的漏洞靶场镜像。 计划：这里记录了 vulhub 所有的漏洞，本专栏也会将这些漏洞全部复现，欢迎持续订阅 我也会不定期再中间更新复现文章链接 目的：以复现 vulhub 漏洞为路径，展示不同的渗透思路及手法，同类漏洞我会尽量用多种渗透思路进行复现，不仅仅是提高个人能力，也是想再 CSDN 这个平台认识更多的安全爱好者 环境： 

## 1、activemq

>  
   


## 2、airflow

>  
    


## 3、apereo-cas

>  
 4.1-rce 


## 4、apisix

>  
  


## 5、appweb

>  
  


## 6、aria2

>  
 rce 


## 7、bash

>  
 CVE-2014-6271 


## 8、celery

>  
  


## 9、cgi

>  
 CVE-2016-5385 


## 10、coldfusion

>  
 CVE-2010-2861 CVE-2017-3066 


## 11、confluence

>  
 CVE-2019-3396 CVE-2021-26084 


## 12、couchdb

>  
 CVE-2017-12635 CVE-2017-12636 


## 13、discuz

>  
 wooyun-2010-080723 x3.4-arbitrary-file-deletion 


## 14、django

>  
  CVE-2018-14574  CVE-2020-9402  


## 15、dns

>  
 dns-zone-transfer 


## 16、docker

>  
 unauthorized-rce 


## 17、drupal

>  
       


## 18、dubbo

>  
 CVE-2019-17564 


## 19、ecshop

>  
   


## 20、elasticsearch

>  
 CVE-2014-3120 CVE-2015-1427 CVE-2015-3337 CVE-2015-5531 WooYun-2015-110216 


## 21、electron

>  
 CVE-2018-1000006 CVE-2018-15685 


## 22、elfinder

>  
 CVE-2021-32682 


## 23、fastjson

>  
 1.2.24-rce 1.2.47-rce vuln 


## 24、ffmpeg

>  
 CVE-2016-1897 phdays 


## 25、flask

>  
 ssti 


## 26、flink

>  
   


## 27、ghostscript

>  
    


## 28、git

>  
 CVE-2017-8386 


## 29、gitea

>  
 1.4-rce 


## 30、gitlab

>  
 CVE-2016-9086 CVE-2021-22205 


## 31、gitlist

>  
 0.6.0-rce CVE-2018-1000533 


## 32、glassfish

>  
 4.1.0 


## 33、goahead

>  
 CVE-2017-17562 CVE-2021-42342 


## 34、gogs

>  
 CVE-2018-18925 


## 35、grafana

>  
  


## 36、h2database

>  
 h2-console-unacc 


## 37、hadoop

>  
  


## 38、httpd

>  
 apache_parsing_vulnerability CVE-2017-15715 CVE-2021-40438 CVE-2021-41773 CVE-2021-42013 ssi-rce 


## 39、imagemagick

>  
 CVE-2020-29599 imagetragick  


## 40、influxdb

>  
 unacc 


## 41、jackson

>  
 CVE-2017-7525 


## 42、java

>  
 rmi-codebase rmi-registry-bind-deserialization rmi-registry-bind-deserialization-bypass 


## 43、jboss

>  
    


## 44、jenkins

>  
 CVE-2017-1000353 CVE-2018-1000861 


## 45、jetty

>  
    


## 46、jira

>  
 CVE-2019-11581 


## 47、jmeter

>  
 CVE-2018-1297 


## 48、joomla

>  
 CVE-2015-8562 CVE-2017-8917 


## 49、jupyter

>  
 notebook-rce 


## 50、kibana

>  
 CVE-2018-17246 CVE-2019-7609 


## 51、laravel

>  
 CVE-2021-3129 


## 52、libssh

>  
 CVE-2018-10933 


## 53、liferay-portal

>  
 CVE-2020-7961 


## 54、log4j

>  
   


## 55、magento

>  
 2.2-sqli 


## 56、mini_httpd

>  
 CVE-2018-18778 


## 57、mojarra

>  
 jsf-viewstate-deserialization 


## 58、mongo-express

>  
 CVE-2019-10758 


## 59、mysql

>  
 CVE-2012-2122 


## 60、nacos

>  
  


## 61、neo4j

>  
 CVE-2021-34371 


## 62、nexus

>  
 CVE-2019-7238 CVE-2020-10199 CVE-2020-10204 


## 63、nginx

>  
 CVE-2013-4547 CVE-2017-7529 insecure-configuration nginx_parsing_vulnerability 


## 64、node

>  
 CVE-2017-14849 CVE-2017-16082 


## 65、ntopng

>  
 CVE-2021-28073 


## 66、ofbiz

>  
 CVE-2020-9496 


## 67、opensmtpd

>  
 CVE-2020-7247 


## 68、openssh

>  
 CVE-2018-15473 


## 69、openssl

>  
 CVE-2014-0160 CVE-2022-0778 heartbleed 


## 70、opentsdb

>  
 CVE-2020-35476 


## 71、php

>  
 8.1-backdoor CVE-2012-1823 CVE-2018-19518 CVE-2019-11043 fpm inclusion php_xxe xdebug-rce 


## 72、phpmailer

>  
 CVE-2017-5223 


## 73、phpmyadmin

>  
   WooYun-2016-199433 


## 74、phpunit

>  
 CVE-2017-9841 


## 75、polkit

>  
  


## 76、postgres

>  
 CVE-2018-1058 CVE-2019-9193 


## 77、python

>  
 PIL-CVE-2017-8291 PIL-CVE-2018-16509 unpickle 


## 78、rails

>  
 CVE-2018-3760 CVE-2019-5418 


## 79、redis

>  
 Unacc CVE-2022-0543 


## 80、rocketchat

>  
 CVE-2021-22911 


## 81、rsync

>  
 common 


## 82、ruby

>  
 CVE-2017-17405 


## 83、saltstack

>  
 CVE-2020-11651 CVE-2020-11652 CVE-2020-16846 


## 84、samba

>  
  


## 85、scrapy

>  
  


## 86、shiro

>  
   


## 87、skywalking

>  
  


## 88、solr

>  
      


## 89、spark

>  
 unacc 


## 90、spring

>  
         


## 91、struts2

>  
                   


## 92、supervisor

>  
 CVE-2017-11610 


## 93、thinkphp

>  
 2-rce  5-rce  


## 94、tikiwiki

>  
  


## 95、tomcat

>  
 CVE-2017-12615 CVE-2020-1938 tomcat8 


## 96、unomi

>  
 CVE-2020-13942 


## 97、uwsgi

>  
 CVE-2018-7490 unacc 


## 98、weblogic

>  
 CVE-2017-10271 CVE-2018-2628 CVE-2018-2894 CVE-2020-14882 ssrf weak_password  


## 99、webmin

>  
 CVE-2019-15107 


## 100、wordpress

>  
 pwnscriptum 


## 101、xstream

>  
 CVE-2021-21351 CVE-2021-29505 


## 102、xxl-job

>  
 unacc（未授权访问） 


## 103、yapi

>  
 unacc（未授权访问） 


## 104、zabbix

>  
  CVE-2017-2824 CVE-2020-11800 

