
--- 
title:  poi的使用 
tags: []
categories: [] 

---
### 导入jar包

```
&lt;!--EXCEl 表数据导入--&gt;
&lt;dependency&gt;
	&lt;groupId&gt;org.apache.poi&lt;/groupId&gt;
	&lt;artifactId&gt;poi&lt;/artifactId&gt;
	&lt;version&gt;3.13&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
	&lt;groupId&gt;org.apache.poi&lt;/groupId&gt;
	&lt;artifactId&gt;poi-ooxml&lt;/artifactId&gt;
	&lt;version&gt;3.13&lt;/version&gt;
&lt;/dependency&gt;

```

### 创建一个类使用

```
package com.zurun.excle.demo.sys.controller;



import com.zurun.excle.demo.sys.entity.EntryCustomer;
import com.zurun.excle.demo.sys.entity.TheCustomerHistory;
import com.zurun.excle.demo.sys.mapper.EntryCustomerMapper;
import com.zurun.excle.demo.sys.mapper.TheCustomerHistoryMapper;
import com.zurun.excle.demo.sys.service.ImportService;
import org.apache.poi.ss.usermodel.DateUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import javax.servlet.http.HttpServletRequest;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Controller
public class ImportController {
    @Autowired
    private ImportService importService;
    @Autowired
    private EntryCustomerMapper entryCustomerMapper;
    @Autowired
    private TheCustomerHistoryMapper theCustomerHistoryMapper;



    @PostMapping(value = "/upload")
    @ResponseBody
    public String uploadExcel(HttpServletRequest request) throws Exception {
    	// 实体类
        EntryCustomer entryCustomer =new EntryCustomer();
        //请求的request
        MultipartHttpServletRequest multipartRequest = (MultipartHttpServletRequest) request;
        //定义格式化时间
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        //new Map
        Map map =new HashMap();
        //初始化Object 
        Object str;
        //获取file 文件
        MultipartFile file = multipartRequest.getFile("filename");
        //判断文件不能为空
        if (file.isEmpty()) {
            return "文件不能为空";
        }
        //获取file文件的输入流
        InputStream inputStream = file.getInputStream();
        //定义list 集合装输入流
        List&lt;List&lt;Object&gt;&gt; list = importService.getBankListByExcel(inputStream, file.getOriginalFilename());
        //关闭输入流
        inputStream.close();
        //循环list里面的每一行
        for (int i = 0; i &lt; list.size(); i++) {
            List&lt;Object&gt; lo = list.get(i);
           循环list里面的每一列(并做校验)
	           for (int b=0; b&lt;num;b++){
	                if (lo.get(b)==null&amp;&amp;b!=4){
	                    map.put(b,"");
	                }else if (b!=4){
	                    map.put(b,lo.get(b).toString());
	                }else {
	                    if (isNumericzidai(lo.get(4).toString())==true){
	                        Double a= Double.valueOf(lo.get(4).toString());//将excel表日期转成double
	                        Date c= DateUtil.getJavaDate(a);
	                        java.sql.Date sqlDate=new java.sql.Date(c.getTime());
	                        map.put(b,sqlDate);
	                    }else {
	                        map.put(b,sdf.parse(lo.get(4).toString()));
	                    }
	                }
	            }
	            entryCustomer.setFollowUpPerson(map.get(1).toString());
	            entryCustomer.setTransactionOrNot(map.get(2).toString());
	            entryCustomer.setNegotiationMode(map.get(3).toString());
	            entryCustomer.setEntryTime(sdf.parse(map.get(4).toString()));
	            entryCustomer.setCustomerClassification(map.get(5).toString());
	            entryCustomer.setEmergencyDegree(map.get(8).toString());
	            entryCustomer.setProductLink(map.get(9).toString());
	            entryCustomer.setCustomerType(map.get(10).toString());
	            entryCustomer.setCorporateName(map.get(11).toString());
	            entryCustomer.setCompanyAddress(map.get(12).toString());
	            entryCustomer.setCustomerName(map.get(13).toString());
	            entryCustomer.setPostPosition(map.get(14).toString());
	            entryCustomer.setContactNumber(map.get(15).toString());
	            entryCustomer.setEmail(map.get(16).toString());
	            entryCustomer.setCustomerCategory(map.get(17).toString());
	            entryCustomer.setBasicBusinessDescription(map.get(18).toString());
	            entryCustomer.setBsorc(map.get(19).toString());
	            entryCustomer.setOldCustomerRemark(map.get(20).toString());
	             插入数据库-----
	            entryCustomerMapper.insert(entryCustomer);

            //TODO 随意发挥
        }
        return "上传成功";
    }
    //检验时间的方法
	public static boolean isNumericzidai(String str) {
        Pattern pattern = Pattern.compile("-?[0-9]+\\.?[0-9]*");
        Matcher isNum = pattern.matcher(str);
        if (!isNum.matches()) {
            return false;
        }
        return true;
    }

}


```

### 编写ImportService 工具类

```
//（包名）
package com.zurun.excle.demo.sys.service; 



import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.springframework.stereotype.Service;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

@Service
public class ImportService {
    public List getBankListByExcel(InputStream in, String fileName) throws Exception {
        List list = new ArrayList&lt;&gt;();
        //创建Excel工作薄
        Workbook work = this.getWorkbook(in, fileName);
        if (null == work) {
            throw new Exception("创建Excel工作薄为空！");
        }
        Sheet sheet = null;
        Row row = null;
        Cell cell = null;

        for (int i = 0; i &lt; work.getNumberOfSheets(); i++) {
            sheet = work.getSheetAt(i);
            if (sheet == null) {
                continue;
            }

            for (int j = sheet.getFirstRowNum(); j &lt;= sheet.getLastRowNum(); j++) {
                row = sheet.getRow(j);
                if (row == null || row.getFirstCellNum() == j) {
                    continue;
                }

                List&lt;Object&gt; li = new ArrayList&lt;&gt;();
                for (int y = row.getFirstCellNum(); y &lt; row.getLastCellNum(); y++) {
                    cell = row.getCell(y);
                    li.add(cell);
                }
                list.add(li);
            }
        }
        work.close();
        return list;
    }

    /**
     * 判断文件格式
     *
     * @param inStr
     * @param fileName
     * @return
     * @throws Exception
     */
    public Workbook getWorkbook(InputStream inStr, String fileName) throws Exception {
        Workbook workbook = null;
        String fileType = fileName.substring(fileName.lastIndexOf("."));
        if (".xls".equals(fileType)) {
            System.out.println(".xls");
            workbook = new HSSFWorkbook(inStr);
        } else if (".xlsx".equals(fileType)) {
            System.out.println(".xlsx");
            workbook = new XSSFWorkbook(inStr);

        } else {
            throw new Exception("请上传excel文件！");
        }
        return workbook;
    }

}


```
