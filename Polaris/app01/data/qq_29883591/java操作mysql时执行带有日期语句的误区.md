
--- 
title:  java操作mysql时执行带有日期语句的误区 
tags: []
categories: [] 

---
最近在写服务器端的一些接口，在用java对mysql进行含有日期信息的查询的时候，遇到了一些问题，分享一下 。

首先把数据库中的一个用于用户签到的表的代码部分贴出来：

```
create table signUpInfo
(
phoneNum nvarchar(11) not null,      #手机号码
signTime timestamp not null,         #时间戳
foreign key(phoneNum) references usersInformation(phoneNum)     #外键，对于我这里主表就不贴了，大家测试可以删去这一句
);
```



下面插入一条语句，带表用户签到：



```
insert into signUpInfo values('18351088222',CURRENT_TIMESTAMP);
```

```

```





```
select * from signUpInfo;
```



<img src="https://img-blog.csdn.net/20161207233016162?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">

这个时候，我们就有了一条记录，那么就可以用来做测试了。



```
package com.huan.jsonservlet;


import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;


/**
 * Created by liuhu on 2016/11/28.
 */

public class SignDBService {
    private Connection conn=DBHelper.getConnection();          #链接数据库


    /*
    此函数用于更新数据库中签到表中的数据，向里面插入phoneNum用户的签到信息，返回值为0表示服务器异常，
    返回值为1签到成功，返回值为2表示不在签到时间，返回值为3表示已经签到，不可重复签到。
    */
    public int updateSignUp(String tableName,String phoneNum)
    {
        int result;
        try{
            Statement stmt = conn.createStatement();
            Date currentTime=new Date();     //当前时间
            SimpleDateFormat formatter=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            String nowtime=formatter.format(currentTime);    //当前时间的字符串表示
            String dateTime=nowtime.substring(0,10);       //当前时间的日期的字符串表示

            //初始化签到的规定时间
            String startTime1=dateTime+" 07:30:00";
            String endTime1=dateTime+" 08:30:00";
            String startTime2=dateTime+" 13:30:00";
            String endTime2=dateTime+" 23:55:00";       #此时间是为了写博客特地改的

            System.out.println(dateTime);

            //创建三个日历对象，用于包装签到时间
            Calendar now=Calendar.getInstance();
            Calendar start=Calendar.getInstance();
            Calendar end=Calendar.getInstance();

            int flag=0;      //用于标记当前签到时间是否符合要求，不是0就是符合要求
            try {
                now.setTime(formatter.parse(nowtime));
                start.setTime(formatter.parse(startTime1));
                end.setTime(formatter.parse(endTime1));
            } catch (ParseException e) {
                result=0;    //表示服务器异常
                e.printStackTrace();
            }
            //对上午的时间段进行比较
            if(now.compareTo(start)&gt;=0&amp;&amp;now.compareTo(end)&lt;=0)
            {
                flag=1;
            }
            else       //对下午的时间段进行比较
            {
                try {
                    start.setTime(formatter.parse(startTime2));
                    end.setTime(formatter.parse(endTime2));
                } catch (ParseException e) {
                    e.printStackTrace();
                }
                if(now.compareTo(start)&gt;=0&amp;&amp;now.compareTo(end)&lt;=0)
                {
                    flag=2;
                }
            }
            //当flag为false时，表示不在签到时间里
            if(flag==0) {
                return 2;
            }
            ResultSet rs=null;

            if (flag == 1) {
                rs = stmt.executeQuery("select * from " + tableName + " where phoneNum=" + phoneNum
                        + " and signTime &gt;= " + startTime1 + " and signTime &lt;= " + endTime2 + ";");
            } else if (flag == 2) {
                rs = stmt.executeQuery("select * from " + tableName + " where phoneNum=" + phoneNum
                        + " and signTime &gt;= " + startTime2 + " and signTime &lt;= " + endTime2 + ";");
            }

            if(rs==null){     //此时表示可以签到
                try {
                    stmt.executeQuery("insert into " + tableName + " values(" + phoneNum
                            + ",CURRENT_TIMESTAMP);");
                    return 1;                          //签到成功
                }
                catch(SQLException e){
                    result=0;    //表示服务器异常
                    e.printStackTrace();
                }
            }
            else{
                return 3;       //此时表示已经签到过了，不可重复签到
            }
//            ResultSet rs=stmt.executeQuery("insert into "+tableName+" values("+phoneNum
//                    +",CURRENT_TIMESTAMP);");
        }catch(SQLException e){
            result=0;    //表示服务器异常
            e.printStackTrace();
        }
        return result;
    }
    public static void main(String[] args){
        SignDBService service=new SignDBService();
        int result=service.updateSignUp("signUpInfo","18351088222");
        System.out.println(result);

    }
}

```



com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '13:30:00 and signTime &lt;= 2016-12-07 23:55:00' at line 1 0 at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method) at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62) at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45) at java.lang.reflect.Constructor.newInstance(Constructor.java:408) at com.mysql.jdbc.Util.handleNewInstance(Util.java:425) at com.mysql.jdbc.Util.getInstance(Util.java:408) at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:943) at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3970) at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3906) at com.mysql.jdbc.MysqlIO.sendCommand(MysqlIO.java:2524) at com.mysql.jdbc.MysqlIO.sqlQueryDirect(MysqlIO.java:2677) at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2545) at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2503) at com.mysql.jdbc.StatementImpl.executeQuery(StatementImpl.java:1369) at com.huan.jsonservlet.SignDBService.updateSignUp(SignDBService.java:131) at com.huan.jsonservlet.SignDBService.main(SignDBService.java:159) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.lang.reflect.Method.invoke(Method.java:483) at com.intellij.rt.execution.application.AppMain.main(AppMain.java:147) 

       看到这么多报错，说实话还是挺蒙的，看第一句中 ，提示的是sql语法错误，并提示了 near '13:30:00 and signTime &lt;= 2016-12-07 23:55:00，那就很容易定位错误了，迅速找到这行代码，如下：



```
if (flag == 1) {
                rs = stmt.executeQuery("select * from " + tableName + " where phoneNum=" + phoneNum
                        + " and signTime &gt;= " + startTime1 + " and signTime &lt;= " + endTime2 + ";");
            } else if (flag == 2) {
                rs = stmt.executeQuery("select * from " + tableName + " where phoneNum=" + phoneNum
                        + " and signTime &gt;= " + startTime2 + " and signTime &lt;= " + endTime2 + ";");
            }
```



 



```
if (flag == 1) {
                rs = stmt.executeQuery("select * from " + tableName + " where phoneNum=" + phoneNum
                        + " and signTime &gt;= '" + startTime1 + "' and signTime &lt;= '" + endTime2 + "';");
            } else if (flag == 2) {
                rs = stmt.executeQuery("select * from " + tableName + " where phoneNum=" + phoneNum
                        + " and signTime &gt;= '" + startTime2 + "' and signTime &lt;= '" + endTime2 + "';");
            }
```



 
