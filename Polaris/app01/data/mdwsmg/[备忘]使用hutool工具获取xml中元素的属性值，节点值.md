
--- 
title:  [备忘]使用hutool工具获取xml中元素的属性值，节点值 
tags: []
categories: [] 

---
本方法是基于hutool工具包，org.w3c.dom。与dom4j方法差不多，不过支持XPath了

传入String格式的xml字符串，如果能明确知晓元素节点信息，可以使用XPath表达式获取节点值与元素属性值

```
import cn.hutool.core.util.XmlUtil;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import javax.xml.xpath.XPathConstants;

/**
 * @author crayon
 * @since 2021/3/30 11:01
 */
public class XmlTest {<!-- -->

    public static void main(String[] args) {<!-- -->
        String xml = "&lt;root&gt;&lt;a name = \"第一个元素\"&gt;&lt;b&gt;最底层节点值&lt;/b&gt;&lt;/a&gt;&lt;/root&gt;";
        Document document = XmlUtil.parseXml(xml);
        Element goalElement = XmlUtil.getElementByXPath("//root/a",document);
        Object bString = XmlUtil.getByXPath("//root/a/b", document, XPathConstants.STRING);
        System.out.println("b元素节点值："+bString);
        String name = goalElement.getAttribute("name");
        System.out.println("a元素属性值："+name);
    }

}


```

>  
 如果xml节点信息未知，不能使用XPath的xml，可以一个个获取节点元素，判断并获取目标值 

