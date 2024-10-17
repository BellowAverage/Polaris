
--- 
title:  python分析作业提交情况 
tags: []
categories: [] 

---
      这次做一个比较贴近我实际的东西：



要求：

    将服务器中交作业的学生（根据文件的名字进行提取）和统计成绩的表格中的学生的信息进行比对，输出所有没有交作业的同学的信息（学号和姓名），并输出所交的作业中命名格式有问题的文件名的信息（如1627406012_E03....）。

提示：

提示：

1、根据服务器文件可以拿到所有交了作业的同学的信息。

<img src="https://img-blog.csdn.net/20170117152936949?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 



2、根据表格可以拿到所有上课学生的信息



3、对1和2中的信息进行比对，找出想要得到的信息

注意：提取服务器中学生交的作业的信息的时候应该考虑到文件格式不对的情况，所以提取信息的时候要做好相关的处理，以避免异常。

     下面直接上程序（python3的版本）：



```
#coding:utf-8
import os
import xlrd


"""
此函数用于获取dir文件夹中的文件的内容,dir中不能含有中文名
"""
def getFilesInfo(dir):
    fileNum=dir[len(dir)-2:len(dir)]    # 取得题目的编号
    trueList=[]
    errorList=[]
    t=os.walk(dir)
    for item in t:
        for name in item[2]:
            if len(name)!=18:
                errorList.append(name)
            else:
                if name[13:15]==fileNum:
                    trueList.append(name[0:10])
                else:
                    errorList.append(name)
    return [trueList,errorList]

# 此函数用于读取xml表格文件中的内容
def readTableContent(fileName):
    date=xlrd.open_workbook(fileName)
    # sheet_name = date.sheet_names()[0]
    stuList=[]      # 存放学号和姓名
    try:  # 获取你要处理的XLS的第一张表
        sh = date.sheet_by_index(0)
    except:
        print("出现问题")
    for i in range(2,sh.nrows):
        id=sh.row_values(i)[1]
        name=sh.row_values(i)[2]
        student=(id,name);  # 存放学生的学号和姓名的元组
        stuList.append(student)
    return stuList


address="D://我的文件/python作业批改/2016级老姜班级作业成绩 2016-10-25.xls"
submitStuList=getFilesInfo("D:\E01")

stuList=readTableContent(address)     # 存放学生的信息的列表

notSubmitStudent=[]      # 存放没有提交作业的学生的信息
for student in stuList:
    if student[0] not in submitStuList [0]:
        notSubmitStudent.append(student)
print("==================================没有交作业的人为================================")
for student in notSubmitStudent:
    print(student[0],student[1])
print("==================================格式错误的文件为=================================")
for error in submitStuList[1]:
    print(error)



```



1、首先进行如下操作：

<img src="https://img-blog.csdn.net/20170117165524757?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

2、然后点击“+”号（由于我是提前下载好了的，所以下面的图中有xlrd的包）：

<img src="https://img-blog.csdn.net/20170117165558288?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

3、在输入框中输入包名并搜索

<img src="https://img-blog.csdn.net/20170117165658648?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

4、完成安装：

<img src="https://img-blog.csdn.net/20170117165751259?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

关于程序中使用到的os和xlrd的相关知识可以自行查阅相关的文档，这里不再进行详细说明。

 

下面是py2.7版本的程序：



```
#coding:utf-8
import os
import xlrd
import xlwt


"""
此函数用于获取dir文件夹中的文件的内容,dir中不能含有中文名
"""
def getFilesInfo(dir):
    fileNum=dir[len(dir)-2:len(dir)]    # 取得题目的编号
    trueList=[]
    errorList=[]
    t=os.walk(dir)
    for item in t:
        for name in item[2]:
            if len(name)!=18:
                errorList.append(name)
            else:
                if name[13:15]==fileNum:
                    trueList.append(name[0:10])
                else:
                    errorList.append(name)
    return [trueList,errorList]

# 此函数用于读取xml表格文件中的内容
def readTableContent(fileName):
    date=xlrd.open_workbook(fileName)
    # sheet_name = date.sheet_names()[0]
    stuList=[]      # 存放学号和姓名
    try:  # 获取你要处理的XLS的第一张表
        sh = date.sheet_by_index(0)
    except:
        print "出现问题"
    for i in range(2,sh.nrows):
        id=sh.row_values(i)[1].encode('utf-8')
        name=sh.row_values(i)[2]
        student=(id,name);  # 存放学生的学号和姓名的元组
        stuList.append(student)
    return stuList


address=unicode("D://我的文件/python作业批改/2016级老姜班级作业成绩 2016-10-25.xls",'utf-8')   # 对于中文名的路径要进行转换
submitStuList=getFilesInfo("D:\E01")

stuList=readTableContent(address)     # 存放学生的信息的列表

notSubmitStudent=[]      # 存放没有提交作业的学生的信息
for student in stuList:
    if student[0] not in submitStuList [0]:
        notSubmitStudent.append(student)
print "==================================没有交作业的人为================================"
for student in notSubmitStudent:
    print student[0],student[1]
print "==================================格式错误的文件为================================="
for error in submitStuList[1]:
    print error



```


