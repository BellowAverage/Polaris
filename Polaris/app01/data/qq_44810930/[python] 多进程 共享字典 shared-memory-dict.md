
--- 
title:  [python] 多进程 共享字典 shared-memory-dict 
tags: []
categories: [] 

---


>  
 Requires: Python &gt;= 3.8 


```
pip install shared-memory-dict

```

打开一个python终端

```
Python 3.8.6 

&gt;&gt;&gt; from shared_memory_dict import SharedMemoryDict
&gt;&gt;&gt;
&gt;&gt;&gt; smd = SharedMemoryDict(name='tokens', size=1024)
&gt;&gt;&gt;
&gt;&gt;&gt; smd['some-key'] = 'some-value-with-any-type'
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; smd['some-key']
'some-value-with-any-type'

```

再打开一个python终端, 此时可以看到上一个终端进程中的数据

```
Python 3.8.6 

&gt;&gt;&gt; from shared_memory_dict import SharedMemoryDict
&gt;&gt;&gt;
&gt;&gt;&gt; existing_smd = SharedMemoryDict(name='tokens', size=1024)
&gt;&gt;&gt;
&gt;&gt;&gt; # 可以看到上一个终端进程中的数据 #
&gt;&gt;&gt; existing_smd['some-key']
'some-value-with-any-type'
&gt;&gt;&gt;
&gt;&gt;&gt; # 并且可以设置新的键值对
&gt;&gt;&gt; existing_smd['new-key'] = 'some-value-with-any-type'
&gt;&gt;&gt; # 并且在第一个终端中也能看到 new-key

```
