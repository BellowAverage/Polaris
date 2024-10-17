
--- 
title:  java对象转xml-个人笔记 
tags: []
categories: [] 

---
### 详情文件可以参考一下连接



### 例子

```
	@Data
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlRootElement(name = "Policy") //XML文件中的根标识
    @XmlType(propOrder = {<!-- -->
            "productGroup",
            "sn",
            "updateUser",
            "updateLastDate",
    }) //控制JAXB 绑定类中属性和字段的排序
    public static class Policy implements Serializable {<!-- -->

        private static final long serialVersionUID = 1L;

        // 产品族
        private List&lt;ProductGroup&gt; productGroup;

        // sn号
        private String sn;

        // 更新人员
        private String updateUser;

        // 最后更新时间
        private String updateLastDate;

    }

    @Data
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlRootElement(name = "ProductGroup")
    @XmlType(propOrder = {<!-- -->
            "product",
            "version",
    })
    public static class ProductGroup implements Serializable {<!-- -->

        private static final long serialVersionUID = 1L;

        // 产品
        private String product;

        // 版本
        private String version;

    }

	public static void main(String[] args) {<!-- -->
        Policy policy = new Policy();
        ProductGroup productGroup = new ProductGroup();
        productGroup.setProduct("12312");
        productGroup.setVersion("3123");
        policy.setProductGroup(Collections.singletonList(productGroup));
        policy.setSn("3213");
        policy.setUpdateUser("321");
        policy.setUpdateLastDate("321");
        // 创建输出流
        StringWriter sw = new StringWriter();
        try {<!-- -->
            // 利用jdk中自带的转换类实现
            JAXBContext context = JAXBContext.newInstance(Policy.class);
            Marshaller marshaller = context.createMarshaller();
            // 格式化xml输出的格式
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
            // 将对象转换成输出流形式的xml
            marshaller.marshal(policy, sw);
        } catch (JAXBException e) {<!-- -->
            e.printStackTrace();
        }
        System.out.println(sw.toString());
    }


```

>  
 生成效果如下： 


<img src="https://img-blog.csdnimg.cn/378bb0f834ab4d7384c755483b9dd055.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
&lt;?xml version="1.0" encoding="UTF-8" standalone="yes"?&gt;
&lt;Policy&gt;
    &lt;productGroup&gt;
        &lt;product&gt;12312&lt;/product&gt;
        &lt;version&gt;3123&lt;/version&gt;
    &lt;/productGroup&gt;
    &lt;sn&gt;3213&lt;/sn&gt;
    &lt;updateUser&gt;321&lt;/updateUser&gt;
    &lt;updateLastDate&gt;321&lt;/updateLastDate&gt;
&lt;/Policy&gt;

```

### XMLUtil.java

```
package com.riemann.springbootdemo.util;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
import java.io.*;

/**
 * 封装了XML转换成object，object转换成XML的代码
 *
 * @author ljq
 * @date 2019/08/29 22:34
 */
public class XMLUtil {<!-- -->

    /**
     * 将对象直接转换成String类型的 XML输出
     *
     * @param obj
     * @return
     */
    public static String convertToXml(Object obj) {<!-- -->
        // 创建输出流
        StringWriter sw = new StringWriter();
        try {<!-- -->
            // 利用jdk中自带的转换类实现
            JAXBContext context = JAXBContext.newInstance(obj.getClass());
            Marshaller marshaller = context.createMarshaller();
            // 格式化xml输出的格式
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
            // 将对象转换成输出流形式的xml
            marshaller.marshal(obj, sw);
        } catch (JAXBException e) {<!-- -->
            e.printStackTrace();
        }
        return sw.toString();
    }

    /**
     * 将对象根据路径转换成xml文件
     *
     * @param obj
     * @param path
     */
    public static String convertToXml(Object obj, String path) {<!-- -->
        FileWriter fw = null;
        try {<!-- -->
            // 利用jdk中自带的转换类实现
            JAXBContext context = JAXBContext.newInstance(obj.getClass());
            Marshaller marshaller = context.createMarshaller();
            // 格式化xml输出的格式
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
            // 将对象转换成输出流形式的xml
            // 创建输出流
            fw = new FileWriter(path);
            marshaller.marshal(obj, fw);
        } catch (JAXBException e) {<!-- -->
            e.printStackTrace();
        } catch (IOException e) {<!-- -->
            e.printStackTrace();
        }
        return fw.toString();
    }

    /**
     * 将String类型的xml转换成对象
     *
     * @param clazz
     * @param xmlStr
     * @return
     */
    public static Object convertXmlStrToObject(Class clazz, String xmlStr) {<!-- -->
        Object xmlObject = null;
        try {<!-- -->
            JAXBContext context = JAXBContext.newInstance(clazz);
            // 进行将Xml转成对象的核心接口
            Unmarshaller unmarshaller = context.createUnmarshaller();
            StringReader sr = new StringReader(xmlStr);
            xmlObject = unmarshaller.unmarshal(sr);
        } catch (JAXBException e) {<!-- -->
            e.printStackTrace();
        }
        return xmlObject;
    }

    /**
     * 将file类型的xml转换成对象
     *
     * @param clazz
     * @param xmlPath
     * @return
     */
    public static Object convertXmlFileToObject(Class clazz, String xmlPath) {<!-- -->
        Object xmlObject = null;
        try {<!-- -->
            JAXBContext context = JAXBContext.newInstance(clazz);
            Unmarshaller unmarshaller = context.createUnmarshaller();
            FileReader fr = null;
            fr = new FileReader(xmlPath);
            xmlObject = unmarshaller.unmarshal(fr);
        } catch (JAXBException e) {<!-- -->
            e.printStackTrace();
        } catch (FileNotFoundException e) {<!-- -->
            e.printStackTrace();
        }
        return xmlObject;
    }
}


```

### 控制类

```
package com.riemann.springbootdemo.controller;

import com.riemann.springbootdemo.model.ApiResponse;
import com.riemann.springbootdemo.model.ExportExcelData;
import com.riemann.springbootdemo.model.objectConvertXML.Policy;
import com.riemann.springbootdemo.service.impl.EmailTask;
import com.riemann.springbootdemo.util.ConstantsUtil;
import com.riemann.springbootdemo.util.XMLUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author ljq
 * @date 2019/08/29 23:05
 */
@RestController
@RequestMapping(value = "/jaxb")
public class ObjectConvertXMLController {<!-- -->

    private static final Logger logger = LoggerFactory.getLogger(ObjectConvertXMLController.class);

    @RequestMapping(value = "/objectToXML", method= RequestMethod.POST)
    public ApiResponse objectToXML(@RequestBody Policy policy) {<!-- -->
        String path = "D:\\Policy.xml";
        logger.info("---将对象转换成File类型的xml Start---");
        String str = XMLUtil.convertToXml(policy, path);
        logger.info(str);
        logger.info("---将对象转换成File类型的xml End---");

        logger.info("---将File类型的xml转换成对象 Start---");
        Policy policyObj = (Policy) XMLUtil.convertXmlFileToObject(Policy.class, path);
        logger.info(policyObj.toString());
        logger.info("---将File类型的xml转换成对象 End---");
        return new ApiResponse(ConstantsUtil.SUCCESS_CODE, null, ConstantsUtil.SUCCESS);
    }
}


```
