
--- 
title:  [python] ETL 工作流程 Prefect 
tags: []
categories: [] 

---
Prefect 是一个用于构建、调度和监控数据流程的 Python 库。它提供了一种简单而强大的方式来管理 ETL（Extract, Transform, Load）工作流程。下面是一个简单的示例，演示了如何使用 Prefect 来创建和运行一个简单的任务：

首先，确保你已经安装了 Prefect 库。你可以使用 pip 安装：

```
pip install prefect

```

接下来，你可以创建一个简单的任务并运行它：

```
from prefect import task, Flow

@task
def hello_task():
    return "Hello, Prefect!"

with Flow("My First Flow") as flow:
    result = hello_task()

flow.run()

```

在这个示例中，我们定义了一个简单的 `hello_task` 函数作为一个任务，并将其添加到名为 “My First Flow” 的流程中。然后，我们运行这个流程，该流程将执行 `hello_task` 任务并返回结果。

除了这个简单的示例之外，Prefect 还提供了许多功能，如任务依赖关系、定时调度、任务状态监控等。你可以查阅 Prefect 的官方文档以获取更多信息和示例：。

以下是一个稍微复杂一点的 Prefect 库案例，其中涉及到任务之间的依赖关系、参数化任务以及定时调度：

```
from datetime import timedelta
from prefect import task, Flow
from prefect.schedules import IntervalSchedule

@task
def extract():
    # 模拟数据提取
    return "Raw data"

@task
def transform(raw_data):
    # 模拟数据转换
    transformed_data = raw_data.upper()
    return transformed_data

@task
def load(transformed_data):
    # 模拟数据加载
    print("Loaded data:", transformed_data)

schedule = IntervalSchedule(interval=timedelta(days=1))

with Flow("ETL Flow", schedule=schedule) as flow:
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load(transformed_data)

flow.run()

```

在这个示例中，我们定义了一个名为 “ETL Flow” 的数据处理流程。该流程包括三个任务：`extract`、`transform` 和 `load`。`extract` 任务模拟数据提取过程，`transform` 任务对提取的数据进行转换，`load` 任务将转换后的数据加载到目标位置。

这些任务之间通过参数传递建立了依赖关系，即 `transform` 任务依赖于 `extract` 任务的输出，`load` 任务依赖于 `transform` 任务的输出。此外，我们使用了 `IntervalSchedule` 对流程进行了定时调度，使得该流程每隔一天执行一次。

除了这个简单的示例之外，Prefect 还支持更复杂的任务依赖关系、分支和合并、错误处理等功能。你可以根据具体需求在 Prefect 的官方文档中找到更多示例和详细信息：。

https://listen-lavender.gitbook.io/prefect-docs/gettingstarted/whyprefect
