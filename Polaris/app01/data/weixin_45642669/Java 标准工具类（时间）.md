
--- 
title:  Java 标准工具类（时间） 
tags: []
categories: [] 

---
Java Date时间转化为字符串

```
Date date = new Date();
SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
 simpleDateFormat.format(date);

```

java lang3 时间格式转化

```
Date date = new Date();
DateFormatUtils.format(date, "yyyy-MM-dd hh:mm:ss");

```

java 获取随机时间 faker

```
Faker faker = new Faker(Locale.CHINA);
Date startTime = DateUtils.addDays(new Date(), -5);
Date endTime = DateUtils.addDays(new Date(), 5);
Date between = faker.date().between(startTime, endTime);

```

java 增加时间日期 lang3

```
Date dataAdd = DateUtils.addDays(new Date(), 5);

```

java 多格式日期匹配

```
String str = "2023-08-02 09:18:25";
Date date1 = DateUtils.parseDate(str, "yyyy-mm-dd", "yyyy-MM-dd hh:mm:ss");

```

Java LocalDateTime

```
LocalDateTime now = LocalDateTime.now();
LocalDateTime start2 = LocalDateTime.of(1995, 1, 1, 20, 25, 1);

```

比较两个时间之间的差距 LocalDateTime

```
LocalDateTime start2 = LocalDateTime.of(1995, 1, 1, 20, 25, 1);
LocalDateTime end2 = LocalDateTime.of(1996, 1, 1, 13, 34, 1);
long seconds = Duration.between(start2, end2).getSeconds();

```

java 截取时间到当前日期

```
Date round = DateUtils.truncate(new Date(), Calendar.DATE);

```

生成连续日期

```
List&lt;Date&gt; list = new ArrayList&lt;&gt;();
Date startTime = new Date();
Date endTime = DateUtils.addDays(new Date(), 5);
int step = 1;
if (startTime.compareTo(endTime) &gt; 0) {<!-- -->
	throw new IllegalArgumentException();
}
while (startTime.compareTo(endTime) &lt;= 0) {<!-- -->
	list.add(startTime);
	startTime = DateUtils.addDays(startTime, 1);
}
System.out.println(list);

```
