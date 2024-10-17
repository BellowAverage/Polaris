
--- 
title:  Pythonapscheduler 在pyintaller 打包后运行失败的解决 
tags: []
categories: [] 

---
不扯多的。直接上代码：

失败的代码：

```
from apscheduler.schedulers.background import BackgroundScheduler

```

改成这样即可：

```
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

```

而调用之前，指定需要的trigger。结果如下：

```
scheduler = BackgroundScheduler()
trigger=IntervalTrigger(seconds=120)
scheduler.add_job(mail_get.mail_get, seconds=120, jitter=30, next_run_time=datetime.datetime.now(), trigger=trigger)
scheduler.add_job(get_num_mail, args=[50], seconds=600, jitter=30, next_run_time=datetime.datetime.now(), trigger=trigger)
scheduler.start()

```

原因：是因为pyinstaller没有打包triggers导致的。需要打包对应的trigger。

我是这么解决的。
