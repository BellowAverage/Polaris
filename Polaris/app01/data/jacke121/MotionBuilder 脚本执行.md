
--- 
title:  MotionBuilder 脚本执行 
tags: []
categories: [] 

---
**目录**









### MediaPipe_Pose_in_MotionBuilder





### tcp通信





### 你可以用以下几种方式执行你的脚本：

从资产浏览器拖放一个脚本 通过Python编辑器执行脚本 在PythonStartup文件夹中放置一个Python工具 使用快捷键运行脚本 使用函数FBApplication::ExecuteScript 从命令行启动启动脚本 注： 1.资产浏览器为(菜单栏Window —&gt; Asset Browser) 资产浏览器中的Scripts中的脚本直接拖到Viewer窗口 (如下图)

<img alt="" height="762" src="https://img-blog.csdnimg.cn/direct/e1cf3640da0845c5b3ec32f894c9869c.png" width="915">

2. Window—&gt;PythonEditor 打开脚本编辑器 ，可新建或打开已有脚本进行执行，也可选中几行代码按回车键进行选择执行 3. PythonStartup 文件夹的位置为(C:\Program Files\Autodesk\MotionBuilder 2019\bin\config\PythonStartup) 该文件夹的python脚本会在motionbuilder启动起来后被执行 4. 暂未测试 5. C++ 调用FBApplication::ExecuteScript 进行python代码的执行

 6. (Ps1 命令行启动python脚本运行) Start -Process -FilePath "C:\Program Files\Autodesk\MotionBuilder 2019\bin\x64\motionbuilder.exe" -ArgumentList "-batch -console -verbosePython $ExecuteFilePath" ($ExecuteFilePath = 需要执行的脚本路径)

(cmd 命令行启动python脚本运行) “C:\Program Files\Autodesk\MotionBuilder 2019\bin\x64\motionbuilder.exe” -batch -console -verbosePython D:/MoMobu/trunk/MoDsMotionBuilderCmdBackStage/MainExecute.py                          原文链接：https://blog.csdn.net/qq_42855293/article/details/118177304
