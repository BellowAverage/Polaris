
--- 
title:  python3 定时任务APScheduler 
tags: []
categories: [] 

---
### 1.安装

简单暴力，直接上代码

```
pip install apscheduler -i https://pypi.tuna.tsinghua.edu.cn/simple #清华镜像源

```

### 2.任务函数

```
def execute_func(cmd):
    """
    执行cmd
    :return:
    """
    try:
        res = os.system(cmd)
        if res != 0:
            print("execute %s fail" % cmd)
    except Exception as e:
        print("Error:{}".format(e))


def get_sim_query():
    """
    要着行的任务函数
    :return:
    """
    return execute_func("ll /home")

```

### 3.任务执行函数

```
scheduler = BlockingScheduler()
# scheduler.add_job(current_time, 'interval', minutes=0.2)
scheduler.add_job(get_sim_query, 'cron', day_of_week='mon-sun', hour=0, minute=10)
scheduler.start() # 启动调度
"""
参数说明：
1 get_sim_query 定时任务函数
2   cron： 当您想在一天中的特定时间定期运行作业时使用
	interval: 当您想以固定的时间间隔运行作业时使用
	date: 当你想在某个时间点只运行一次作业时使用
3 day_of_week='mon-sun' （也可用0-6表示）周一到周日执行，即每天都会执行
4 hour=0, minute=10 每天的00:10执行
"""

```

### 4.官方文档


