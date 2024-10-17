
--- 
title:  APScheduler四种组件 
tags: []
categories: [] 

---
## APScheduler四种组件
- 触发器（triggers）- 任务存储(job stores)- 任务执行人(executors)- 任务调度者(schedulers)
**触发器**可以理解为任务什么时候执行。每个任务都有自己的触发器。除了初始配置之外，触发器完全是无状态的。

**任务存储**是安排任务存储在哪里。默认存储只是将任务保留在内存中，但也可以将它们存储在各种类型的数据库中(例如sqlite,mysql,redis等)。

**任务执行人**是处理任务的运行。他们通常是将任务提交给线程或进程池来完成此操作。任务完成后，执行程序会通知调度程序，调度程序随后会发出相应的事件。

**任务调度者**是将任务存储（job stores），任务执行人(executors)绑定在一起，起到管理定时任务的作用。通常只在应用程序中运行一个调度程序。应用程序开发人员通常不直接处理作业存储，执行程序或触发器，一般都是通过修改配置信息来实现。配置作业存储和执行程序是通过调度程序完成的，添加，修改和删除任务由调度者管理。

#### 快速入门

安装

```
pip install apscheduler

```

效果案例

```
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
"""
jobstores
存储
"""
jobstores = {<!-- -->
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
"""
executors 
将作业中指定的可调用对象提交给线程或进程池来完成此操作
"""
executors = {<!-- -->
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
"""
BackgroundScheduler
希望调度程序在应用程序内部的后台运行.不会阻塞进程
"""
# 创建定时任务的调度器对象
scheduler = BackgroundScheduler(executors=executors,jobstores=jobstores)


# 定义定时任务
def my_job(param1, param2):
    print('我是定时任务 我的参数是：{}-{}'.format(param1,param2))
    print(threading.current_thread())
    return True
"""
trigger
触发任务，interval 采用是以固定的时间间隔运行作业时使用
seconds 表示间隔秒数
"""
# 向调度器中添加定时任务
scheduler.add_job(my_job,
                  'interval',
                  seconds=10,
                  args=[100, 'python'])

# 启动定时任务调度器工作
scheduler.start()
#如有必要，执行删除任务
# scheduler.remove_all_jobs()

#因为是后台运行，所以我们需要让当前程序一直运行来查看效果
while True:
   pass

```
