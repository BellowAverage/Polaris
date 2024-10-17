
--- 
title:  【yarn】 kill 一个spark任务 
tags: []
categories: [] 

---
要关闭一个正在运行的Spark任务，你可以使用以下命令来终止执行：

```
yarn application -kill &lt;application_id&gt;

```

将 `&lt;application_id&gt;` 替换为你要关闭的Spark应用程序的ID。这个ID通常以 `application_` 开头，后面跟着一串数字。

请确保你有适当的权限来执行这个命令。如果你没有足够的权限，可以联系集群管理员或具有相关权限的人员来完成这个操作。

### 检查 status

检查特定的 Spark 应用程序是否仍然活动，你可以使用以下命令：

```
yarn application -status &lt;application_id&gt;

```

### 查看占用资源

要查看 Spark 应用程序在 Spark WebUI 中占用了多少 CPU 和内存资源，可以按照以下步骤进行操作：
1.  打开 Web 浏览器并导航到正在运行的 Spark 应用程序的 WebUI 地址。一般情况下，默认地址为 `http://&lt;driver_node&gt;:4040`，其中 `&lt;driver_node&gt;` 是 Spark 驱动节点的主机名或 IP 地址。 1.  在 Spark WebUI 页面上，你将看到应用程序的概览信息和各个阶段的详细信息。点击应用程序的名称或 ID，以进入应用程序的详细页面。 <li> 在应用程序的详细页面中，你可以在不同的选项卡中查看有关任务执行的各种信息。主要关注下面两个选项卡： 
  1.  **“Executors”（执行者）**：这个选项卡显示了所有执行者的列表和相关的指标，包括 CPU 使用情况、内存使用情况等。你可以查看每个执行者的详细信息，并了解它们的资源使用情况。 1.  **“Environment”（环境）**：在这个选项卡中，你可以找到有关 Spark 应用程序的环境变量和相关配置的信息。这可能包括有关资源分配和使用的详细信息，例如 executor 内存和核心数等。  </li>