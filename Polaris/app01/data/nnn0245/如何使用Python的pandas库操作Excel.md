
--- 
title:  如何使用Python的pandas库操作Excel 
tags: []
categories: [] 

---
#### 使用Python的库操作Excel

最近因需要用Excel电子表格处理数据，使用了其它一些方式处理Excel文件数据，这是学习笔记的整理。

Excel2003及以前版：列数最大256(2的8次方)列，行数最大65536(2的16次方)行；Excel2007及以后版：列数最大16384(2的14次方)，行数最大1048576(2的20次方)；

获取Excel最大行和最大列的方法：

启动Excel后通过快捷键Ctrl+方向键（←↑↓→），可以定位到最左、最上、最下、最右的单元格，从而可以看到行和列的最大值。

Python中有很多库可以操作Excel，像pandas、xlrd、xlwt、xlutils、openpyxl 等。

xlrd 库：读取 Excel 文件

xlwt 库：写入 Excel 文件

xlutils 库：操作 Excel 文件的实用工具，如复制、分割、筛选等

xlrd、xlwt、xlutils 库可以读写操作后缀为xls的excel文件。

openpyxl库 ：操作xlsx后缀的excel文件，还要用到这个库。

本文主要介绍pandas。特别提示：

pandas 库是基于numpy库 的软件库，因此安装Pandas 之前需要先安装numpy库。默认的pandas不能直接读写excel文件，需要安装读、写库即xlrd、xlwt才可以实现xls后缀的excel文件的读写，要想正常读写xlsx后缀的excel文件，还需要安装openpyxl库 。

#### **pandas库****简介**

pandas官网 

pandas 中文教程 

 

pandas库是一个Python的核心数据分析支持库，它提供了强大的一维数组和二维数组处理能力，其非常擅长与处理二维表结构，带行列标签的矩阵数据，时间序列数据。pandas提供的两个主要数据结构一维数组（Series）和二维数组（DataFrame）强力的支撑着当今金融、统计、社会科学、工程等诸多领域的数据分析工作。通过pandas我们可以方便的操作数据的增、查、改、删、合并、重塑、分组、统计分析，此外pandas还提供了非常成熟的I/O工具，用于读
