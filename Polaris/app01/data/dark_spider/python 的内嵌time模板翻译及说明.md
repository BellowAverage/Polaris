
--- 
title:  python 的内嵌time模板翻译及说明 
tags: []
categories: [] 

---
 python 的内嵌time模板翻译及说明    一、简介

   time模块提供各种操作时间的函数   说明：一般有两种表示时间的方式:        第一种是时间戳的方式(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的        第二种以数组的形式表示即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同     year (four digits, e.g. 1998)     month (1-12)     day (1-31)     hours (0-23)     minutes (0-59)     seconds (0-59)     weekday (0-6, Monday is 0)     Julian day (day in the year, 1-366)     DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时     If the DST flag is 0, the time is given in the regular time zone;     if it is 1, the time is given in the DST time zone;     if it is -1, mktime() should guess based on the date and time.     夏令时介绍：http://baike.baidu.com/view/100246.htm     UTC介绍：http://wenda.tianya.cn/wenda/thread?tid=283921a9da7c5aef&amp;clk=wttpcts      二、函数介绍 1.asctime()   asctime([tuple]) -&gt; string   将一个struct_time(默认为当时时间)，转换成字符串         Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.         When the time tuple is not present, current time as returned by localtime()         is used.          2.clock()   clock() -&gt; floating point number   该函数有两个功能，   在第一次调用的时候，返回的是程序运行的实际时间；   以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔      示例：  
1.  import time  1.  if __name__ == '__main__':  1.      time.sleep(1)  1.      print "clock1:%s" % time.clock()  1.      time.sleep(1)  1.      print "clock2:%s" % time.clock()  1.      time.sleep(1)  1.      print "clock3:%s" % time.clock()  

