
--- 
title:  Hadoop报错Could not locate executable XXX\bin\winutils.exe in the Hadoop binaries 
tags: []
categories: [] 

---
### 错误信息：

```
2022-12-11 22:02:39,468 ERROR [org.apache.hadoop.util.Shell] - Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable D:\Development_tools\Hadoop\hadoop-3.3.4\bin\winutils.exe in the Hadoop binaries.
	at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:356)
	at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:371)
	at org.apache.hadoop.util.Shell.&lt;clinit&gt;(Shell.java:364)
	at org.apache.hadoop.util.StringUtils.&lt;clinit&gt;(StringUtils.java:80)
	at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
	at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:272)
	at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:260)
	at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:790)
	at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:760)
	at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:633)
	at org.apache.hadoop.mapreduce.task.JobContextImpl.&lt;init&gt;(JobContextImpl.java:72)
	at org.apache.hadoop.mapreduce.Job.&lt;init&gt;(Job.java:142)
	at org.apache.hadoop.mapreduce.Job.getInstance(Job.java:185)
	at com.hadoop.workcount.WordCountDriver.main(WordCountDriver.java:19)

```

### 解决办法：

出现此问题是因为：在hadoop的bin目录下找不到可执行文件 bin\winutils.exe。因此将winutils.exe文件放入bin目录下即可解决：
