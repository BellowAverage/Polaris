
--- 
title:  C#读取XML文件的数据 
tags: []
categories: [] 

---
 **C#中可以用XmlDocument类操作Xml文件**

 **例如要读取如下Xml文件**

 **程式如下**

 其中XmlElement继承自XmlNode

 XmlElement有GetAttribute()&amp;GetElementsByTagName()等方法而XmlNode没有

 不管使用XmlNode的ChildNodes属性还是XmlElement的GetElementsByTagName()方法获取的都是XmlNodeList

 那这里就存在获取的XmlNodeList中的XmlNode到底是什么类型的问题

 可以根据XmlNode的NodeType属性判断

 如若等于XmlNodeType.Element就可以强转为XmlElement从而使用XmlElement的方法
