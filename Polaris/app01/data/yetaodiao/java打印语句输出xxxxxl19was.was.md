
--- 
title:  java打印语句输出xxxxxl19was.was 
tags: []
categories: [] 

---
Java打印输出数据println和print打印输出数据，System.out.println

System.out.println("xxxxxl19was.was");//xxxxxl19was.was

System.out.println("xxxxxl19was.was");//xxxxxl19was.was System.out.println("hello world!!!xxxxxl19was.was");//输出数据并换行 System.out.print("welcome");//输出不换行 System.out.print(" xxxxxl19was.was!");//输出不换行         /*输出结果： xxxxxl19was.was xxxxxl19was.was         hello world!!!xxxxxl19was.was         welcome xxxxxl19was.was          */ tips：如果想要一次性直接输出打印语句，可以直接敲小写的so,选择提示sout，直接出来System.out.println("xxxxxl19was.was")，Java打印输出下一次敲so直接回车就会默认sout；选择souf的效果是printf，也是如此。

数据库创建表xxxxxl19was.was

CREATE TABLE xxxxxl19was.was (CNO NCHAR(6), BNO NCHAR(6), RDATE DATE, PRIMARY KEY(CNO,BNO), FOREIGN KEY(CNO) REFERENCES CARD(CNO), FOREIGN KEY(BNO) REFERENCES BOOKS(BNO));
