
--- 
title:  [工具备忘]JAVA获取MYSQL数据库表结构、字段信息 
tags: []
categories: [] 

---


#### 获取数据库表结构
- 


产品让给出数据库的结构信息，excel表格形式如下： <img src="https://img-blog.csdnimg.cn/20210407103133903.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## MYSQL

写了一个临时工具，核心sql为

>  
 SELECT TABLE_NAME,TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=(SELECT DATABASE()) SELECT * FROM information_schema.`COLUMNS` WHERE TABLE_SCHEMA=(SELECT DATABASE()) 


使用了hutool的集合工具类与excel工具类，代码如下

```
import cn.hutool.core.collection.CollUtil;
import cn.hutool.poi.excel.ExcelUtil;
import cn.hutool.poi.excel.ExcelWriter;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * @author roamay.com
 * @since 2021/4/6
 */

@Slf4j
public class DatabaseTest {<!-- -->

    public static void main(String[] args) {<!-- -->
        // 可以用 @Slf4j 代替
        Logger log = LoggerFactory.getLogger(Object.class);
        // 数据库连接参数
        String URL = "jdbc:mysql://127.0.0.1:3306/march_user?useUnicode=true&amp;characterEncoding=utf8&amp;serverTimezone=GMT%2b8";
        String NAME = "root";
        String PASSWORD = "root";
        // 查询当前连接数据库的表信息,根据表名查询表信息的的sql
        String databaseStrSql = "SELECT TABLE_NAME,TABLE_COMMENT FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=(SELECT DATABASE())";
        String tableStrSql = "SELECT * FROM information_schema.`COLUMNS` WHERE TABLE_SCHEMA=(SELECT DATABASE()) AND TABLE_NAME = ? ";
        // 使用hutool的excel工具建表导出（直接使用poi也可以），随便导出到某一文件夹即可，我导出在桌面
        ExcelWriter writer = ExcelUtil.getWriter("C:\\Users\\91036\\Desktop\\表结构.xlsx");
        List&lt;List&lt;String&gt;&gt; rows = new ArrayList&lt;&gt;();
        List&lt;String&gt; titleRow = CollUtil.newArrayList("表英文名", "表中文名", "字段名", "字段说明", "数据类型", "备注", "字段码值以及码描述");
        rows.add(titleRow);
        try {<!-- -->
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection coon = DriverManager.getConnection(URL, NAME, PASSWORD);
            Statement statement = coon.createStatement();
            PreparedStatement preparedStatement = coon.prepareStatement(tableStrSql);
            ResultSet databaseResult = statement.executeQuery(databaseStrSql);
            while (databaseResult.next()) {<!-- -->
                preparedStatement.setString(1, databaseResult.getString("TABLE_NAME"));
                ResultSet tableResult = preparedStatement.executeQuery();
                while (tableResult.next()) {<!-- -->
                    List&lt;String&gt; row = new ArrayList&lt;&gt;();
                    row.add(databaseResult.getString("TABLE_NAME"));
                    row.add(databaseResult.getString("TABLE_COMMENT"));
                    row.add(tableResult.getString("COLUMN_NAME"));
                    row.add(tableResult.getString("COLUMN_COMMENT"));
                    row.add(tableResult.getString("COLUMN_TYPE"));
                    String temp = tableResult.getString("COLUMN_KEY").equals("PRI") ? "主键" : "";
                    row.add(temp);
                    row.add("");
                    rows.add(row);
                }
            }

        } catch (ClassNotFoundException e) {<!-- -->
            log.error("驱动加载失败", e);
        } catch (SQLException e) {<!-- -->
            log.error("获取句柄失败", e);
        }
        writer.write(rows,true);
        writer.close();
    }
}


```

附依赖

```
        &lt;!--常用工具类--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;cn.hutool&lt;/groupId&gt;
            &lt;artifactId&gt;hutool-all&lt;/artifactId&gt;
            &lt;version&gt;5.6.0&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;!--excel--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.poi&lt;/groupId&gt;
            &lt;artifactId&gt;poi-ooxml&lt;/artifactId&gt;
            &lt;version&gt;5.0.0&lt;/version&gt;
        &lt;/dependency&gt;

```
