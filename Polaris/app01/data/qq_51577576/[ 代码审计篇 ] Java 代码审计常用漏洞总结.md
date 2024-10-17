
--- 
title:  [ 代码审计篇 ] Java 代码审计常用漏洞总结 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - - - - - - - - - - - 


## 前言

主要代码审计方法是跟踪用户输入数据和敏感函数参数回溯： 跟踪用户的输入数据， 判断数据进入的每一个代码逻辑是否有可利用的点， 此处的代码逻辑可以是一个函数，或者是条小小的条件判断语句。 敏感函数参数回溯， 根据敏感函数， 逆向追踪参数传递的过程。这个方法是最高效， 最常用 的方法。大多数漏洞的产生是因为函数的使用不当导致的， 只要找到这些函数， 就能够快速 挖掘想要的漏洞。 以下是基于关键词审计技巧总结：在搜索时要注意是否为整个单词, 以及小写敏感这些设置

## 1、密码硬编码、密码明文存储

关键词：password、pass、jdbc 审计方法：密码硬编码最容易找，直接用 Sublime Text 打开项目目录，然后按 Ctrl + Shift + F 进行全局 搜索 password 关键词。

## 2、XSS

关键词：getParamter、&lt;%=、param. 审计方法： 反射型 XSS 一般 fortify 一般都能扫描出来，如果是手工找，可全局搜索以下关键词。

## 3、SQL 注入

关键词：Select、Dao、from、delete、update、insert 审计方法：SQL 注入一般 fortify 一般都能扫描出来，手动找的话，一般直接搜索 select 、update 、delete 、insert 关键词就会有收获，如果 sql语句中有出现+append 、 $ () # 等字眼， 如果没有配置 SQL 过滤文件， 则判断存 在 SQL 注入漏洞。

## 4、任意文件下载

关键词：download、fileName、filePath、write、getFile、getWriter 审计方法：全局搜索关键词。

## 5、任意文件删除

关键词：Delete、deleteFile、fileName、filePath 审计方法： 任意文件删除漏洞搜索关键词。

## 6、文件上传

关键词：Upload、write、fileName、filePath 审计方法：文件上传可以搜索关键词， 需注意有没有配置文件上传白名单。

## 7、命令注入

关键词：getRuntime、exec、cmd、shell 审计方法：全局搜索关键词。

## 8、缓冲区溢出

关键词：strcpy,strcat,scanf,memcpy,memmove,memeccpy，Getc(),fgetc(),getchar;read,printf 审计方法：主要通过搜索关键词定位， 再分析上下文。

## 9、XML 注入

关键词：DocumentBuilder、XMLStreamReader、SAXBuilder、SAXParser SAXReader 、XMLReader、 SAXSource、TransformerFacto、SAXTransformerFactory、SchemaFactory 审计方法：XML 解析一般在导入配置、数据传输接口等场景可能会用到，可全局搜索关键词。

## 10、反序列化漏洞

关键词：ObjectInputStream.readObject、ObjectInputStream.readUnshared 、XMLDecoder.readObject Yaml.load 、 XStream.fromXML、ObjectMapper.readValue 、 JSON.parseObject 审计方法： Java 程序使用 ObjectInputStream 对象的 readObject 方法将反序列化数据转换为 java 对象。 但当输入的反序列化的数据可被用户控制，那么攻击者即可通过构造恶意输入， 让反序列化 产生非预期的对象， 在此过程中执行构造的任意代码。 反序列化操作一般在导入模版文件、网络通信、数据传输、日志格式化存储、对象数据落磁 盘或 DB 存储等业务场景,在代码审计时可重点关注一些反序列化操作函数并判断输入是否可控。

## 11、url 跳转

关键词：sendRedirect 、setHeader 、forward 审计方法：全局搜索关键词。

## 12、不安全组件暴露

关键词：activity、Broadcast Receiver、Content Provider 、 Service、inter-filter 审计方法：全局搜索关键词。

## 13、日志记录敏感信息

关键词：log、log.info、logger.info 审计方法：全局搜索关键词。

## 14、代码执行

关键词：eval、system、exec 审计方法：全局搜索关键词，存在这些函数就可能存在代码执行命令。
