
--- 
title:  Python学生信息管理系统源码，学生教师端分离，支持数据的增删查改、数据分析与统计 基于Tkinter带图形界面 
tags: []
categories: [] 

---
##### 介绍

Python学生信息管理系统。学生教师端分离，支持数据的增删查改、数据分析与统计。 <img src="https://img-blog.csdnimg.cn/1a526fe680e64001a6187af3e9ec3e3b.png" alt="在这里插入图片描述"> 下载地址：

##### 软件架构

Python3.9版本 Python-Tkinter库开发的图形界面 Python-Pandas库数据处理 Python-matplotlib库数据分析与展示 Python-Pickle库登录信息序列化处理（Pickle版本：Python3.9-5） **低于该版本的Python，可能会出现无法读取当前版本的pickle文件** 。

##### 软件功能
- 学生、教师登录- 成绩分析与统计- 成绩登记、发布与导出- 添加班级信息与管理
##### 默认测试账号

**初始默认管理员账号密码为admin,admin** 可以使用pickle或pandas.pickle模块的读user_data文件下的udpk文件获取详细账号信息，student为学生，teacher为老师 main.py

```
# -*- coding:utf-8 -*-

import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmsg
import tkinter.filedialog as tflg
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Data_analysis:
    def __init__(self, width, height, frame, status, *data):
        """
        :param width: 屏幕宽度
        :param height: 屏幕高度
        :param frame: 所有学生的信息与成绩列表 (源: self.data_d)
        :param status: 登入身份 1教师/0学生 (学生只展示自己的成绩报告，老师不仅可以查询学生数据，还可以查看班级所有成绩报告)
        :param data: 学生的姓名、学号 (考虑到学生登入，所以从这里单独获取学生的姓名和学号, 学生登入是会同时获取其成绩信息)
        """
        self.status = status
        if self.status:  # 根据登入身份不同，准备学生数据
            self.stuNum = ["全部"] + list(data[0])
            self.stuName = ["全部"] + list(data[1])
        else:
            self.stuNum = data[0]
            self.stuName = data[1]
            self.data_lst = data[2]
        self.alys_win = tk.Toplevel(win)
        self.alys_win.geometry("1000x900+%d+%d"% ((width - 1000) / 2, (height - 900) / 2))
        self.alys_win.resizable(width=False, height=False)

        """初始化绘图的数据框架以及绘制表的参数信息 开始"""
        self.dataframe = pd.DataFrame(frame, columns=["学号", "姓名", "班级", "高数", "英语", "Python"])
        plt.rcParams["font.family"] = "simhei"  # 绘制表的参数信息 字体
        plt.rcParams['font.size'] = 10  # 绘制表的参数信息 字体大小
        plt.rcParams['axes.unicode_minus'] = False  # 绘制表的参数信息 字体显示中文
        """初始化绘图的数据框架以及绘制表的参数信息 开始"""

        self.command_part()
        self.data_clearner()

    def command_part(self):

        self.var_Subject = tk.StringVar()
        self.var_stuNumb = tk.StringVar()
        self.var_stuName = tk.StringVar()

        self.command_frame = tk.LabelFrame(self.alys_win, text="控件区")
        self.command_frame.place(x=5, y=5, width=990, height=125)
        self.allSubject_frame = tk.LabelFrame(self.alys_win, text="总成绩分析")
        self.allSubject_frame.place(x=5, y=130, width=495, height=770)
        self.subjeScore_frame = tk.LabelFrame(self.alys_win, text="各科成绩分析")
        self.subjeScore_frame.place(x=500, y=130, width=495, height=770)

        tk.Label(self.command_frame, text="学生学号: ").place(x=125, y=35)
        tk.Label(self.command_frame, text="学生姓名: ").place(x=335, y=35)

        self.stuNum_box = ttk.Combobox(self.command_frame, textvariable=self.var_stuNumb)
        self.stuNum_box["value"] = self.stuNum
        self.stuNum_box.current(0)
        self.stuNum_box["state"] = "readonly"
        self.stuNum_box.place(x=195, y=35, width=120, height=25)

        self.stuName_box = ttk.Combobox(self.command_frame, textvariable=self.var_stuName)
        self.stuName_box["value"] = self.stuName
        self.stuName_box.current(0)
        self.stuName_box["state"] = "readonly"
        self.stuName_box.place(x=405, y=35, width=120, height=25)

        if self.status:
            ttk.Button(self.command_frame, text="搜索",
                       command=self.searchStuDt).place(x=615, y=35)

        self.stu_INFO_index = 0
        def select_numb(event = None):
            num_lst = self.stuNum_box["value"]
            self.stu_INFO_index = num_lst.index(self.var_stuNumb.get())
            self.stuName_box.current(self.stu_INFO_index)

        def select_name(event = None):
            name_lst = self.stuName_box["value"]
            self.stu_INFO_index = name_lst.index(self.var_stuName.get())
            self.stuNum_box.current(self.stu_INFO_index)

        self.stuNum_box.bind("&lt;&lt;ComboboxSelected&gt;&gt;", select_numb)
        self.stuName_box.bind("&lt;&lt;ComboboxSelected&gt;&gt;", select_name)

    @classmethod
    def count_subject(cls, data):
        """
        统计各科成绩分布区间的类方法
        通过遍历数组数据，并进行if条件判断即可进行成绩判断
        :param data: 学生的成绩列表
        :return: 分布区间的字典
        """
        count_score = {
            "30分以下": 0,
            "30分至60分以内": 0,
            "60分至70分以内": 0,
            "70分至80分以内": 0,
            "80分至90分以内": 0,
            "90分以上": 0
        }
        for score in data:
            if score &lt; 30:
                count_score["30分以下"] += 1
            elif 30 &lt;= score &lt; 60:
                count_score["30分至60分以内"] += 1
            elif 60 &lt;= score &lt; 70:
                count_score["60分至70分以内"] += 1
            elif 70 &lt;= score &lt; 80:
                count_score["70分至80分以内"] += 1
            elif 80 &lt;= score &lt; 90:
                count_score["80分至90分以内"] += 1
            else:
                count_score["90分以上"] += 1
        else: return count_score

    @classmethod
    def count_total(cls, data):
        """
        统计总分分布区间的类方法
        通过遍历数组数据，并进行if条件判断即可进行成绩判断
        :param data: 学生的总分列表
        :return: 分布区间的字典
        """
        count_score = {
            "90分以下": 0,
            "90分至180分以内": 0,
            "180分至210分以内": 0,
            "210分至240分以内": 0,
            "240分至270分以内": 0,
            "270分以上": 0,
        }

        for score in data:
            if score &lt; 150:
                count_score["90分以下"] += 1
            elif 150 &lt;= score &lt; 200:
                count_score["90分至180分以内"] += 1
            elif 200 &lt;= score &lt; 250:
                count_score["180分至210分以内"] += 1
            elif 250 &lt;= score &lt; 300:
                count_score["210分至240分以内"] += 1
            elif 300 &lt;= score &lt; 350:
                count_score["240分至270分以内"] += 1
            else:
                count_score["270分以上"] += 1
        else: return count_score

    def searchStuDt(self):
        """
        搜索学生数据并绘图方法，该方法仅在教师身份登录时可用
        # self.stu_INFO_index是当前下拉框的序列值，从0~len(下拉框数据) - 1排列序列
        """
        if self.stu_INFO_index:  # 选项不是“全部”，搜索当前下拉选项的学生数据
            try:
                """将原来的所有窗体全部隐藏"""
                self.subjeScore_frame.place_forget()
                self.allSubject_frame.place_forget()
                self.stuINFO_frame.place_forget()
            except Exception as E:
                pass
            finally:
                self.draw_stuSubject(list(self.dataframe.iloc[self.stu_INFO_index - 1]))
        else:
            try:  # 选项是“全部”，显示专业全部学生数据
                self.stuINFO_frame.place_forget()
                self.allSubject_frame.place(x=5, y=130, width=495, height=770)
                self.subjeScore_frame.place(x=500, y=130, width=495, height=770)
            except:
                pass

    def draw_stuSubject(self, data_lst):
        ID, Name, Class, Math, Engl, Pyth = data_lst
        labels = ['高数', '英语', 'Python', '总分']

        fig3 = plt.figure(figsize=(7, 5), dpi=100, facecolor="gold", edgecolor='green', )
        plt.subplots_adjust(top=0.95, hspace=0.4)
        self.stuINFO_frame = tk.LabelFrame(self.alys_win, text = f"{ID}: {Name} 学生成绩分析报告")
        self.stuINFO_frame.place(x = 5, y = 130, width = 990, height = 770)

        # 添加子图
        ax1 = fig3.add_subplot(121, ) # 绘制学生成绩和班级平均成绩的柱状图
        ax2 = fig3.add_subplot(122, polar = True) # 绘制学生平均成绩与班级平均成绩的雷达图

        """绘制学生成绩和班级平均成绩的柱状图 开始"""
        ave_score = [self.math_ave, self.engl_ave, self.pyth_ave, self.Total_ave]
        score = data_lst[3:6] + [self.Total_lst[self.stu_INFO_index - 1]]
        x = np.arange(len(labels))
        width = 0.35
        a1 = ax1.bar(x - width / 2, ave_score, width , label = "平均成绩", color = "b")
        a2 = ax1.bar(x + width / 2, score, width, label="学生成绩", color="r", )
        ax1.set_title("各科分数")
        ax1.set_xticks(x)
        ax1.set_xticklabels(labels)
        for text in a1+a2:
            height = text.get_height()
            ax1.text(text.get_x() + text.get_width() / 2, height, '%d'%(int(height)), ha="center", va = "bottom")
        """绘制学生成绩和班级平均成绩的柱状图 结束"""

        """绘制学生平均成绩与班级平均成绩的雷达图 开始"""
        angles = np.linspace(0, 2 * np.pi, 4, endpoint=False)  # 计算角度
        plot_score = [score, ave_score] # 成绩二维列表
        score_a = np.concatenate((plot_score[0], [plot_score[0][0]]))
        score_b = np.concatenate((plot_score[1], [plot_score[1][0]]))
        angles = np.concatenate((angles, [angles[0]])) # 闭合数据图
        labels = np.concatenate((labels, [labels[0]])) # 闭合数据图
        ax2.plot(angles, score_a,  )  # 绘制学生个人的成绩图
        ax2.fill(angles, score_a, facecolor='r', alpha=0.5)# 填充颜色和透明度
        ax2.plot(angles, score_b, )  # 绘制年级平均成绩图
        ax2.fill(angles, score_b, facecolor = "b", alpha = 0.5)
        # 设置雷达图中每一项的标签显示
        ax2.set_thetagrids(angles * 180 / np.pi, labels)
        # 设置雷达图的0度起始位置
        ax2.set_theta_zero_location('N')
        ax2.set_rlabel_position(270)
        ax2.set_title("成绩专业平均水平")
        plt.legend([ "专业平均", "本人成绩"], loc='best')
        """绘制学生平均成绩与班级平均成绩的雷达图 结束"""

        """将分析好的数据表放入到UI窗体 开始"""
        self.stu_canvas = FigureCanvasTkAgg(fig3, self.stuINFO_frame)
        self.stu_canvas.get_tk_widget().place(x=1, y=1)
        self.stu_canvas.draw()
        Toolbar = NavigationToolbar2Tk(self.stu_canvas, self.stuINFO_frame)
        Toolbar.update()
        self.stu_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        """将分析好的数据表放入到UI窗体 结束"""

    def draw_allSubject(self):
        """
        用来画 左侧 总成绩分析区的方法
        """
        self.fig1, self.ax1 = plt.subplots(2, 1, num=1, figsize=(7, 5), dpi=100, facecolor="gold", edgecolor='green')
        plt.subplots_adjust(top=0.95, hspace=0.4)
        self.fig2, self.ax2 = plt.subplots(2, 2, num=2, figsize=(7, 5), dpi=100, facecolor="gold", edgecolor='green')
        plt.subplots_adjust(top=0.95, hspace=0.4)

        """分割绘图数据表的子窗体 一分为二 开始"""
        ax1 = self.ax1[0]
        ax2 = self.ax1[1]
        """分割绘图数据表的子窗体 一分为二 开始"""

        """绘制总成绩分布区间柱状图 开始"""
        label_bar = list(self.Total_score.keys())  # 取出label标签
        dtset_bar = list(self.Total_score.values())  # 取出所有数据
        ax1.bar(label_bar, dtset_bar)  # 绘制条形图
        ax1.set_title("总分区间排行")  # 添加条形标题
        xlabels = ax1.get_xticks()  # 实例化条形图标签
        for a, b in zip(label_bar, dtset_bar):  # 添加条形图标签
            ax1.text(a, b + 0.001, '%.f' % b, ha='center', va='bottom', fontsize=9)
        ax1.xaxis.set_major_locator(mticker.FixedLocator(xlabels))
        ax1.set_xticklabels(labels=label_bar, rotation=35)
        """绘制总成绩分布区间柱状图 结束"""

        """绘制总成绩分布区间饼状图 开始"""
        ax2.pie(dtset_bar, labels=label_bar, autopct="%1.1f%%", shadow=True, startangle = 50) # 绘制饼状图
        """绘制总成绩分布区间饼状图 结束"""

        self.all_canvas = FigureCanvasTkAgg(self.fig1, self.allSubject_frame)
        self.all_canvas.get_tk_widget().place(x=1, y=1)
        self.all_canvas.draw()
        Toolbar = NavigationToolbar2Tk(self.all_canvas, self.allSubject_frame)
        Toolbar.update()
        self.all_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_subjeScore(self):
        """
        绘制 右侧 各科成绩数据表方法
        """

        """分类各科成绩分布区间的数据标签、成绩 开始"""
        math_bar = [list(self.math_score.keys()), list(self.math_score.values())]  # 高数
        engl_bar = [list(self.engl_score.keys()), list(self.engl_score.values())]  # 英语
        pyth_bar = [list(self.pyth_score.keys()), list(self.pyth_score.values())]  # Python
        subj_ave = [self.math_ave, self.engl_ave, self.pyth_ave, ["高数平均分", "英语平均分", "Python平均分"]]  # 各科平均分
        """分类各科成绩分布区间的数据标签、成绩 结束"""

        """分割绘图数据表的子窗体 一分为四 开始"""
        math_ax1 = self.ax2[0, 0]
        engl_ax2 = self.ax2[0, 1]
        pyth_ax3 = self.ax2[1, 0]
        aver_ax4 = self.ax2[1, 1]
        """分割绘图数据表的窗体 一分为四 结束"""

        """绘制高数成绩分布区间柱状图 开始"""
        math_ax1.bar(math_bar[0], math_bar[1])
        math_ax1.set_title("高数成绩分布区间")
        xlabels = math_ax1.get_xticks()
        math_ax1.xaxis.set_major_locator(mticker.FixedLocator(xlabels))
        math_ax1.set_xticklabels(labels = math_bar[0], rotation=35)
        """绘制高数成绩分布区间柱状图 结束"""

        """绘制英语成绩分布区间柱状图 开始"""
        engl_ax2.bar(engl_bar[0], engl_bar[1])
        engl_ax2.set_title("英语成绩分布区间")
        xlabels = engl_ax2.get_xticks()
        engl_ax2.xaxis.set_major_locator(mticker.FixedLocator(xlabels))
        engl_ax2.set_xticklabels(labels = engl_bar[0], rotation=35)
        """绘制英语成绩分布区间柱状图 结束"""

        """绘制Python成绩分布区间柱状图 开始"""
        pyth_ax3.bar(pyth_bar[0], engl_bar[1])
        pyth_ax3.set_title("Python成绩分布区间")
        xlabels = pyth_ax3.get_xticks()
        pyth_ax3.xaxis.set_major_locator(mticker.FixedLocator(xlabels))
        pyth_ax3.set_xticklabels(labels = pyth_bar[0], rotation=35)
        """绘制Python成绩分布区间柱状图 结束"""

        """绘制各科平均成绩分布区间柱状图 开始"""
        aver_ax4.bar(subj_ave[3], subj_ave[0:3])
        aver_ax4.set_title("各科平均成绩分布区间")
        xlabels = aver_ax4.get_xticks()
        aver_ax4.xaxis.set_major_locator(mticker.FixedLocator(xlabels))
        aver_ax4.set_xticklabels(labels = subj_ave[3], rotation=35)
        """绘制各科平均成绩分布区间柱状图 结束"""

        def draw_label(ax, label, bar):
            for a, b in zip(label, bar):
                ax.text(a, float(b) + 0.001, '%.f' % b, ha='center', va='bottom', fontsize=9)
        [
            draw_label(ax, labels, bars)
            for ax, labels, bars in
            [
                 [math_ax1, math_bar[0], math_bar[1]],
                 [engl_ax2, engl_bar[0], engl_bar[1]],
                 [pyth_ax3, pyth_bar[0], pyth_bar[1]],
                 [aver_ax4, subj_ave[3], subj_ave[0:3]]
            ]
        ]

        """将分析好的数据表放入到UI窗体 开始"""
        self.sub_canvas = FigureCanvasTkAgg(self.fig2, self.subjeScore_frame)
        self.sub_canvas.get_tk_widget().place(x=1, y=1)  #
        self.sub_canvas.draw()
        Toolbar = NavigationToolbar2Tk(self.sub_canvas, self.subjeScore_frame)
        Toolbar.update()
        self.sub_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        """将分析好的数据表放入到UI窗体 结束"""
    
    def data_clearner(self):
        """
        根据传入的成绩数据，进行数据清洗。绘制完成后，开始绘制分析结果框架
        清洗内容:
            1. 各科成绩分布区间
            2. 各科平均分/最高分/最低分
            3. 该班级总分分布区间
            4. 该班级总分各科/总分平均分
        """
        try:
            self.math = list(map(int, self.dataframe["高数"]))
            self.engl = list(map(int, self.dataframe["英语"]))
            self.pyth = list(map(int, self.dataframe["Python"]))
        except:
            self.alys_win.destroy()
            tmsg.showerror(title="没有成绩数据", message="无成绩数据，无法分析")
            return -1
        """数学统计区"""
        self.math_score = self.count_subject(self.math)  # 统计高数单科各区间
        self.math_ave = round((sum(self.math) / len(self.math)), 2)  # 统计 高数平均分
        self.math_max = max(self.math)  # 高数最高分
        self.math_min = min(self.math)  # 高数最低分

        """英语统计区"""
        self.engl_score = self.count_subject(self.engl)  # 统计英语单科各区间
        self.engl_ave = round((sum(self.engl) / len(self.engl)), 2)  # 统计 英语平均分
        self.engl_max = max(self.engl)  # 英语最高分
        self.engl_min = min(self.engl)  # 英语 最低分

        """Python统计区"""
        self.pyth_score = self.count_subject(self.pyth)  # 统计Python 单科各区间
        self.pyth_ave = round((sum(self.pyth) / len(self.pyth)), 2)  # 统计 Python平均分
        self.pyth_max = max(self.pyth)  # Python最高分
        self.pyth_min = min(self.pyth)  # Python最低分

        """总分统计区"""
        self.Total_lst = []
        append = self.Total_lst.append
        for i in range(self.dataframe.shape[0]):  # 统计 总分
            Sum = self.math[i] + self.engl[i] + self.pyth[i]
            append(Sum)
        else:
            del append
        self.Total_ave = round((sum(self.Total_lst) / self.dataframe.shape[0]), 2)  # 统计 总分平均分
        self.Total_score = self.count_total(self.Total_lst)  # 统计 总分各区间

        """根据登入身份的不同，开始绘制分析图表"""
        if self.status:
            self.draw_allSubject()
            self.draw_subjeScore()
        else:
            self.draw_stuSubject(self.data_lst)

class Main(tk.Frame):
    def __init__(self, **master):
        super().__init__(master=win) # 继承Tkinter方法

        """获取屏幕尺寸，使得窗体居中"""
        get_screenWidth = win.winfo_screenwidth() # 获取屏幕尺寸
        get_screenHeight = win.winfo_screenheight()  # 获取屏幕尺寸
        relX = (get_screenWidth - 500) / 2
        relY = (get_screenHeight - 300) / 2
        """获取屏幕尺寸，使得窗体居中"""

        """加载主窗口"""
        win.geometry("%dx%d+%d+%d"%(500,300,relX,relY))  # 使窗口居中
        win.title("Mannagement System TestVersion 1.0")
        win.bind("&lt;Return&gt;", self.usr_validate_Login)
        """加载主窗口"""

        self.login_frame()  # 加载绘制登录界面方法

    def login_frame(self):  # 主登陆界面
        """
        用于构建主登陆界面
        :return: None
        """
        """绘制登录界面的图片 开始"""
        self.canvas = tk.Canvas(win, height=200, width=500)
        self.image_file = tk.PhotoImage(file="img/welcome.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_file)  # nw(0, 0)作为锚点放置图片
        self.canvas.pack(side="top")
        """绘制登录界面的图片 结束"""

        """定义控件变量 开始"""
        self.var_radioButton = tk.StringVar(value="A")
        self.var_userLable = tk.StringVar(value="学 号: ")
        self.var_username = tk.StringVar()
        self.var_password = tk.StringVar()
        self.var_show_psw = tk.IntVar(value=0)
        self.var_check_showpsw = tk.IntVar()
        """定义控件变量 结束"""

        """绘制登录界面信息标签 开始"""
        tk.Label(win, textvariable=self.var_userLable).place(x=50, y=150)  #
        tk.Label(win, text="密 码: ").place(x=50, y=190)  #
        tk.Label(win, text="请选择您的身份: ").place(x=50, y=120)
        """绘制登录界面信息标签 开始"""

        """绘制登录界面登入身份选择按钮 开始"""
        choice_student = ttk.Radiobutton(win, text="学 生", variable=self.var_radioButton, value="A" ,command = self.change_name)
        choice_student.place(x=150, y=120)
        choice_family = ttk.Radiobutton(win, text="教 师", variable=self.var_radioButton, value="B" ,command = self.change_name)
        choice_family.place(x=220, y=120)
        """绘制登录界面登入身份选择按钮 结束"""

        """绘制账号、密码输入框 开始"""
        ttk.Entry(win, textvariable=self.var_username).place(x=150, y=150)
        self.psw_entry = ttk.Entry(win, textvariable=self.var_password, show="*")
        self.psw_entry.place(x=150, y=190)
        """绘制账号、密码输入框 结束"""

        """绘制登录界面的显示密码勾选框、登录按键 开始"""
        show_pswBtn = ttk.Checkbutton(win, text="显示密码", variable=self.var_check_showpsw,
                                          command=self.show_psw, onvalue=1, offvalue=0)
        show_pswBtn.place(x=330, y=190)
        ttk.Button(win, text="登录", command=self.usr_validate_Login).place(x=170, y=240)
        """绘制登录界面的显示密码勾选框、登录按键 结束"""

    def change_name(self):  # 切换身份改变Lable标签方法
        """
        运用推导式，对切换身份登陆时可以用于切换标签内容
        """
        return self.var_userLable.set("工 号: ") \
            if self.var_radioButton.get() == "B" \
                else self.var_userLable.set("学 号: ")

    def show_psw(self):  # 显示密码方法
        """
        登陆界面的显示密码选择框的模块函数
        主要方式为：将原来的输入框隐藏，再重新绘制一个新的输入框里放入原来的密码。通过勾选框按钮checkBtn来响应
        """
        if self.var_check_showpsw.get():
            self.psw_entry.place_forget()
            self.unshow_entryUi = ttk.Entry(win, textvariable=self.var_password)
            self.unshow_entryUi.place(x=150, y=190)
        if self.var_check_showpsw.get() == 0:
            self.unshow_entryUi.place_forget()
            self.psw_entry.place(x=150, y=190)

    @staticmethod
    def read_psw_info(status, usrn, usrp):  # 验证登陆方法
        """
        用于读取本地的账号密码文件，验证登录信息。
        返回信息验证信息是否正确 正确时包含所在班级信息，失败则返回错误提示
        :param status: 登录的身份码
        :param usrn: 需要验证登录的账号
        :param usrp: 需要验证登录的密码
        :return: 登录验证的信息 True+所在班级信息/False
        """
        status_code = {"A": "student", "B": "teacher"}  # 根据登入身份获取验证字段
        try:
            usr_login_info = pd.read_pickle(f"data/user_data/users_{status_code[status]}_info.udpk")
        except FileNotFoundError:
            if status_code == "A":
                usr_login_info = {"admin": {"psw": "admin", "class": "20软件工程一班"}}
                pd.to_pickle(usr_login_info, f"data/user_data/users_{status_code[status]}_info.udpk")
            else:
                usr_login_info = {"admin": {"psw": "admin", "class": ["20软件工程一班", "21人工智能二班"]}}
                pd.to_pickle(usr_login_info, f"data/user_data/users_{status_code[status]}_info.udpk")
        try:
            if usrn in usr_login_info:
                if usrp == usr_login_info[usrp]["psw"]:
                    class_info = usr_login_info[usrp]["class"]
                    return True, class_info
                else:
                    return False
            else:
                return False
        except KeyError:
            return False

    def usr_validate_Login(self, event=None):  # 登陆方法
        """
        用于按下登录按钮后处理登录信息的
        登录成功则开启新窗口并返回该用户的班级信息
        登录失败则弹出错误提示窗口修改信息
        """
        def get_Screeninfo():
            """
            验证登录成功后，隐藏主窗口并回传屏幕信息使得模块居中
            :return: 屏幕的宽高信息
            """
            win.withdraw()
            get_screenWidth = win.winfo_screenwidth()  # 获取屏幕尺寸
            get_screenHeight = win.winfo_screenheight()  # 获取屏幕尺寸
            return get_screenWidth, get_screenHeight
        users_name = self.var_username.get()
        users_password = self.var_password.get()
        usr_login_info = self.read_psw_info(self.var_radioButton.get(), users_name, users_password)

        if users_name == "" or users_password == "":
            tmsg.showerror(title="账号或密码为空", message="请正确输入账号或密码")
            return -1
        if self.var_radioButton.get() == "A":  # 根据登入身份判断，当前身份为 学生
            if usr_login_info is False:
                tmsg.showerror(title="账号或密码错误", message="账号或密码错误，请重新输入！")
            else:
                wid, hei = get_Screeninfo()
                self.main_Frame_stu(wid, hei, usr_login_info[1], users_name)

        elif self.var_radioButton.get() == "B":  # 根据登入身份判断，当前身份为 教师
            if usr_login_info is False:
                tmsg.showerror(title="账号或密码错误", message="账号或密码错误，请重新输入！")
            else:
                Width, Height = get_Screeninfo()
                self.score_register(Width, Height, usr_login_info[1])

    def main_Frame_stu(self, get_screenWidth, get_screenHeight, class_info, account):
        """
        学生主窗口
        :param account: 学生学号
        :param class_info: 学生账号信息
        :param get_screenWidth: 屏幕宽度
        :param get_screenHeight: 屏幕高度
        """
        dt = pd.read_pickle("data/user_data/class_info.udcl") # 读取班级最新成绩的文件
        if class_info in dt.keys(): # 读取班级最新成绩的文件
            read = pd.read_csv(dt[class_info])  # 根据读取的最新成绩文件路径，打开并读取数据文件
            self.data_d = pd.DataFrame(read)  # 将成绩转为pandas框架
            cpy_frame = self.data_d.copy(deep=True)  # 临时深拷贝一份班级成绩框架，
            cpy_frame.set_index(["学号"], inplace=True)  # 将深拷贝的成绩框架的学号转成索引
            stuName = cpy_frame.loc[int(account)]["姓名"]  # 根据索引来寻找该学生的学号、成绩信息
            score_lst = [account, *cpy_frame.loc[int(account)]]
            del cpy_frame # 释放拷贝的框架
            return Data_analysis(get_screenWidth, get_screenHeight, self.data_d, 0, account, stuName, score_lst)
        else:  # 如果班级没有发布最新成绩，提示没有发布
            tmsg.showinfo(title="没有发布成绩", message="老师还没发布成绩噢！")
            win.deiconify()

    def load_analys(self, width, height, stuNum, stuName):
        """
        加载数据，传输至数据分析类进行数据分析与展示，数据来源主要通过当前登记信息、过往成绩登记信息的方法
        :param width: 屏幕宽度
        :param height: 屏幕高度
        :param stuNum: 学生学号信息
        :param stuName:  学生姓名信息
        """
        def temp_func():
            """
            临时函数可以为教师提供直接读取过去的班级成绩文件的方法，可以未登记成绩的情况下获取过往成绩分析报告
            """
            load_path = tflg.askopenfilename(defaultextension=".udsc", filetypes=[("成绩文件格式", "*.udsc")])
            self.data_d = pd.read_csv(load_path).to_dict(orient = "records")
            return Data_analysis(width, height, self.data_d, 1,
                                 list(map(lambda x:x["学号"], self.data_d)),
                                 list(map(lambda x:x["姓名"], self.data_d)))
        try:
            """
            数据列表 self.data_d是用来存储数据的列表，里面存储每一个学生信息的字典，包含 学号、姓名、班级、高数成绩、英语成绩、Python成绩
            类似于：[{"学号" : "1001", "姓名" : "张三", "班级" : "xx班", "高数" : 100, "英语" : 80, "Python" : 85}, ......]
            """
            temp = self.data_d[0]["高数"]  # 故意引发bug，由此引发KeyError 防止未登记信息而去进行成绩分析。因为登记了以后是必定存在成绩数据在里面
            return Data_analysis(width, height, self.data_d, 1, stuNum, stuName)
        except AttributeError:  # 因为 self.data_d 是成绩信息列表，如果正常加载班级数据的话就会存在当前实例属性，不存在就需要去加载过往数据
            temp_func()
        except KeyError: # 由上 防止未登记信息而去进行成绩分析。因为登记了以后是必定存在成绩数据在里面
            temp_func()

    def insert_info(self, args, *values):
        """
        用于插入内容到表格当中
        :param args:  判断插入信息位置
        :param values:  需要插入的数据
        """
        self.put = True
        if values[-1] == "":
            tmsg.showerror(title="输入成绩为空", message="输入成绩为空，请重新输入！")
            return -1
        elif int(values[-1]) &lt; 0 or int(values[-1]) &gt; 100:
            tmsg.showerror(title="输入内容有误", message="输入内容有误，请重新输入！")
            return -1

        if not args:
            self.score_Tree.insert("", "end", values=values)
        else:
            item_text = self.score_Tree.get_children()[-1]
            self.score_Tree.set(item_text, column = 2 + args, value=values[-1])

        item = self.data_d[self.stu_INFO_index]
        item[self.subject_combobox.get()] = values[-1]
        self.sub_index += 1
        self.subject_combobox.current(self.sub_index % len(self.subName))

        if args == 2:
            self.stu_INFO_index += 1
            self.StuNum_combobox.current(self.stu_INFO_index % self.stu_INFO_len)
            self.StuName_combobox.current(self.stu_INFO_index % self.stu_INFO_len)

    def open_class(self, event=None):
        """
        用于读取班级信息，包括姓名、学号、班级，
        """
        column = self.class_tree.identify_column(event.x)  # 列
        column = int(str(column).replace("#", ""))
        if column == 2:
            delete_data = self.score_Tree.get_children()
            for i in delete_data:
                self.score_Tree.delete(i)
            self.data_d = []
            """
            数据列表 self.data_d是用来存储数据的列表，里面存储每一个学生信息的字典，包含 学号、姓名、班级、高数成绩、英语成绩、Python成绩
            类似于：[{"学号" : "1001", "姓名" : "张三", "班级" : "xx班", "高数" : 100, "英语" : 80, "Python" : 85}, ......]
            """
            for item in self.class_tree.selection():
                self.item_text = self.class_tree.item(item, "values")[0]
                read_info = pd.read_csv(f"data/class_data/{self.item_text}.csv")
                data_frame = pd.DataFrame(read_info)
                self.data_d = data_frame.to_dict(orient = "records")
                self.StuNum_combobox["value"] = [list(i.values())[0] for i in self.data_d]
                self.StuName_combobox["value"] = [list(i.values())[1] for i in self.data_d]
                self.StuName_combobox.current(0)
                self.StuNum_combobox.current(0)
                self.var_classInfo.set(f"正在给 {self.item_text} 登记")
            self.stu_INFO_index = 0
            self.stu_INFO_len = len(self.data_d)

    def save_data(self):
        """
        保存成绩文件，self.put用来判断是否输入信息
        """
        try:
            if self.put:
                sava_frame = pd.DataFrame(self.data_d)
                save_path = tflg.asksaveasfilename(defaultextension=".udsc", filetypes=[("成绩文件格式", "*.udsc")])
                sava_frame.to_csv(save_path, index = False, encoding="utf-8")
        except AttributeError:
            tmsg.showerror(title="无法保存", message="未添加数据无法保存")

    def Release_score(self):
        """
        发布成绩方法
        根据用户的选择成绩文件路径，更新至最新班级成绩信息文件里的数据
        """
        try:
            path = "data/work_data"
            save_path = tflg.askopenfilename(defaultextension=".udsc", filetypes=[("成绩文件格式", "*.udsc")])  # 打开文件
            path += "/" + os.path.split(save_path)[1]
            read_class = pd.read_pickle("data/user_data/class_info.udcl")
            read_class[self.item_text] = path  # 更新班级的最新成绩信息
            pd.to_pickle(read_class, "data/user_data/class_info.udcl")
            tmsg.showinfo(title="发布成功", message="成绩发布成功！")
        except FileNotFoundError:
            tmsg.showerror(title="无法找到成绩文件", message="请确认安装目录是否为源目录")

    def add_info(self, Width, Height):
        """
        用于绘制添加班级信息窗口方法
        :param Width: 屏幕宽度
        :param Height: 屏幕高度
        """
        add_win = tk.Toplevel(win)
        add_win.geometry("%dx%d+%d+%d" % (730, 520, (Width - 730) / 2, (Height - 520) / 2))
        add_win.title("添加班级信息")

        def template_win():
            """
            学号模板设置临时窗口
            """
            temp = tk.Toplevel(add_win)
            temp.title("添加学号模板")
            temp.geometry("%dx%d+%d+%d" % (200, 60, (Width - 200) / 2, (Height - 60) / 2))

            def run():
                var_StuID.set(int(var_tempEntry.get()))
                temp.destroy()
                return 0

            var_tempEntry = tk.StringVar(value="")
            var_tempEntry.set(var_tempEntry)
            ttk.Entry(temp, textvariable = var_tempEntry).pack()
            ttk.Button(temp, text = "保存模板", command = run).pack()

        """绘制控件变量 开始"""
        self.count  = 0
        self.var_StuClass = tk.StringVar()
        self.var_TeacerID = tk.StringVar()
        var_len = tk.StringVar(value="")
        var_StuName = tk.StringVar()
        var_StuID = tk.StringVar()
        """绘制控件变量 结束"""

        """绘制功能区 开始"""
        register_frame = tk.LabelFrame(add_win, text="班级信息登记区", width=230, height=240)
        register_frame.place(x=10, y=5)
        control_frame = tk.LabelFrame(add_win, text="控件区", width=230, height=240)
        control_frame.place(x=250, y=5)
        class_frame = tk.LabelFrame(add_win, text="已登录班级信息", width=230, height=240)
        class_frame.place(x=490, y=5)
        addS_frame = tk.LabelFrame(add_win, text="已登记班级信息", width=710, height=260)
        addS_frame.place(x=10, y=250)
        """绘制功能区 结束"""

        """绘制班级名称/教师工号/学生学号/学生姓名 开始"""
        tk.Label(register_frame, textvariable=var_len).place(x=10, y=10)
        tk.Label(register_frame, text="班级名称: ").place(x=10, y=45)
        tk.Label(register_frame, text="教师工号: ").place(x=10, y=90)
        tk.Label(register_frame, text="学生学号: ").place(x=10, y=135)
        tk.Label(register_frame, text="学生姓名: ").place(x=10, y=180)
        """绘制班级名称/教师工号/学生学号/学生姓名 结束"""

        """绘制信息输入框 开始"""
        ttk.Entry(register_frame, textvariable = self.var_StuClass).place(x = 80, y = 45, width = 120, height = 25)
        ttk.Entry(register_frame, textvariable = self.var_TeacerID).place(x = 80, y = 90, width = 120, height = 25)
        ttk.Entry(register_frame, textvariable = var_StuID).place(x = 80, y = 135, width = 120, height = 25)
        ttk.Entry(register_frame, textvariable = var_StuName).place(x = 80, y = 180, width = 120, height = 25)
        """绘制信息输入框 结束"""

        """绘制信息表列表框 开始"""
        add_cols = ("班级名称", "教师工号", "学生学号", "学生姓名")
        add_Tree = ttk.Treeview(addS_frame, show="headings", columns=add_cols,
                                       selectmode=tk.EXTENDED)
        add_Tree.place(relwidth=1, relheight=1)
        for state_col in add_cols:
            add_Tree.heading(state_col, text=state_col)
            add_Tree.column(state_col, width=25, anchor="w")
        else:
            del add_cols

        name_colum = ("班级名称", "教师工号","班级人数")
        class_tree = ttk.Treeview(class_frame, show="headings", columns=name_colum,
                                       selectmode=tk.EXTENDED)
        class_tree.place(relwidth=1, relheight=1)
        for state_col in name_colum:
            class_tree.heading(state_col, text=state_col)
            class_tree.column(state_col, width=25, anchor="w")
        else:
            del name_colum
        """绘制信息表列表框 结束"""

        def add_func():
            """
            信息插入相应函数
                根据学号模板，每次默认+1
                自动清空学生姓名输入框
            """
            if self.var_StuClass.get() == "" or self.var_TeacerID.get() == "" or var_StuID.get() == "" or var_StuName.get() == "":
                tmsg.showerror(title="信息为空", message="信息不能为空")
                return -1
            else:
                add_Tree.insert("", "end", values=(self.var_StuClass.get(), self.var_TeacerID.get(),
                                                   var_StuID.get(), var_StuName.get()))
                self.var_TemplateID = int(var_StuID.get()) + 1
                self.count += 1
                var_len.set(f"当前共有 {self.count} 位学生")
                var_StuID.set(self.var_TemplateID)
                var_StuName.set("")

        def Import_func():
            """
            导入现有班级信息到信息列表框函数定义
            """
            if self.var_StuClass.get() == "" or self.var_TeacerID.get() == "":
                tmsg.showwarning(title="班级与教师信息为空", message="请在左侧添加班级与教师信息")
                return -1
            path = tflg.askopenfilename(defaultextension=".csv", filetypes=[("班级文件格式", "*.csv")])
            read = pd.read_csv(path)
            temp = list(zip(read["学号"], read["姓名"]))
            for stu in temp:
                add_Tree.insert("", "end", values=(self.var_StuClass.get(), self.var_TeacerID.get(), *stu))
            var_len.set(f"当前共有 {len(temp)} 位学生")
            self.count = len(temp)
            var_StuID.set((int(temp[-1][0]) + 1))  # 插入到最后一个，根据现有的最后一个学号，学号+1

        def save_func():
            """
            保存班级信息到csv文件里
                同时，如果教师工号/学生学号不存在，会自动生成最新账号信息，默认两者相同
            """
            class_lst = []
            stu_lst = []
            append_cls = class_lst.append
            append_stu = stu_lst.append
            for i in add_Tree.get_children():
                class_dict = {"学号": add_Tree.item(i, "values")[2],
                            "姓名": add_Tree.item(i, "values")[3],
                            "班级": add_Tree.item(i, "values")[0]}
                stu_dict = {add_Tree.item(i, "values")[2] : {"psw" : add_Tree.item(i, "values")[2],
                                                             "class" : add_Tree.item(i, "values")[0]}}
                append_cls(class_dict)
                append_stu(stu_dict)
            if not len(class_lst):
                tmsg.showerror(title="信息为空", message="信息不能为空")
                return -1
            add_teacher = pd.read_pickle(r"data\user_data\users_teacher_info.udpk")  # 读取教师账号数据文件
            add_student = pd.read_pickle(r"data\user_data\users_student_info.udpk")  # 读取学生账号数据文件
            if self.var_StuClass.get() in add_teacher[self.var_TeacerID.get()]["class"]:  # 如果教师已负责当前班级，弹出是否更新提示
                mess = tmsg.askyesno(title="该教师已负责该班级", message="该教师已负责该班级, 是否更新班级？")
                if not mess: return -1
            if self.var_TeacerID.get() not in add_teacher.keys():  # 如果教师工号不存在，生成工号
                add_teacher[self.var_TeacerID.get()] = {"psw": self.var_TeacerID.get(),
                                                        "class" : [self.var_StuClass.get()]}
                pd.to_pickle(add_teacher, r"data\user_data\users_teacher_info.udpk")
                class_tree.insert("", "end", values=(self.var_StuClass.get(),
                                                     self.var_TeacerID.get(), len(class_lst)))
                [add_student.update(info) for info in stu_lst]  # 默认更新学生数据文件
                pd.to_pickle(add_student, r"data\user_data\users_student_info.udpk")
                tmsg.showinfo(title="生成班级成功", message="生成班级成功！并默认生成该教师/学生账号，初始密码为工/学号")
            else:
                add_teacher[self.var_TeacerID.get()]["class"].append(self.var_StuClass.get())
                pd.to_pickle(add_teacher, r"data\user_data\users_teacher_info.udpk")
                class_tree.insert("", "end", values=(self.var_StuClass.get(),
                                                     self.var_TeacerID.get(), len(class_lst)))
                self.class_tree.insert("", "end", values = (self.var_StuClass.get(), "打开"))
                [add_student.update(info) for info in stu_lst] # 默认更新学生数据文件
                pd.to_pickle(add_student, r"data\user_data\users_student_info.udpk")
                tmsg.showinfo(title="生成班级成功", message="生成班级成功！并默认生成学生账号，初始密码为学号")
            dtfr = pd.DataFrame(class_lst, columns=("学号", "姓名", "班级"))
            dtfr.to_csv(f"data/class_data/{self.var_StuClass.get()}.csv", index=False, encoding="utf-8")  # 班级文件生成

        ttk.Button(control_frame, text="添加信息", command = add_func).place(x=10, y=25) # 添加信息btn
        ttk.Button(control_frame, text="返回上一级", command= lambda: [ add_win.destroy()]).place(x=10, y=75) # 删除信息btn
        ttk.Button(control_frame, text="删除信息", command =
            lambda: [ add_Tree.delete(select) for select in add_Tree.selection()] ).place(x=120, y=25)  # 绘制登记界面 保存本地btn
        ttk.Button(control_frame, text="添加学号模板", command= template_win).place(x=120, y=75, width=100) # 绘制模板界面，添加
        ttk.Button(control_frame, text="生成班级", command=lambda: [save_func()]).place(x=10, y=125)
        ttk.Button(control_frame, text="导入班级", command = Import_func).place(x=120, y=125)
        add_win.bind("&lt;Return&gt;", add_func)  # 绑定回车键事件——添加信息,

    def score_register(self, Width , Height, class_info):
        """
        教师成绩登记界面
        :param class_info: 当前教师所管理的班级
        :param Width: 屏幕宽度
        :param Height: 屏幕高度
        """
        win_register = tk.Toplevel(win)
        win_register.geometry("%dx%d+%d+%d" % (730, 520, (Width - 730) / 2, (Height - 520) / 2))
        win_register.resizable(width=False, height=False)
        win_register.protocol("WM_DELETE_WINDOW", win.quit)

        """定义控件变量 开始"""
        self.var_classInfo = tk.StringVar(value="")  # 班级名称标签变量
        self.var_stu_name = tk.StringVar()  # 学生姓名下拉框变量
        self.var_stu_Numb = tk.StringVar()  # 学生学号下拉框变量
        var_Subject = tk.StringVar()  # 科目名称下拉框变量
        var_Subject_entry = tk.StringVar()  # 所得成绩输入框变量
        """定义控件变量 结束"""

        """绘制功能区 开始"""
        register_frame = tk.LabelFrame(win_register, text= "成绩登记区", width = 230, height = 240)
        register_frame.place(x = 10, y = 5)
        control_frame = tk.LabelFrame(win_register, text = "控件区", width = 230, height = 240)
        control_frame.place(x = 250, y = 5)
        class_frame = tk.LabelFrame(win_register, text = "我的班级", width = 230, height = 240)
        class_frame.place(x = 490, y = 5)
        addS_frame = tk.LabelFrame(win_register, text = "已登记成绩信息", width = 710, height = 260)
        addS_frame.place(x = 10, y = 250)
        """绘制功能区 结束"""

        """绘制学生班级/姓名/学号/科目名称/成绩标签 开始"""
        tk.Label(register_frame, textvariable = self.var_classInfo).place(x = 10, y  = 10)  # 班级
        tk.Label(register_frame, text = "学生学号").place(x = 10, y = 45)  # 学生学号
        tk.Label(register_frame, text = "学生姓名: ").place(x = 10, y = 90)  # 学生姓名
        tk.Label(register_frame, text = "科目名称: ").place(x = 10 , y = 135)  # 科目名称
        tk.Label(register_frame, text = "所得成绩:").place(x = 10, y = 180)  # 所得成绩
        """绘制学生班级/姓名/学号/科目名称/成绩标签 结束"""

        """绘制学生姓名/学号下拉框 开始"""
        self.stu_INFO_index = 0
        self.stu_INFO_len = 0
        self.StuNum_combobox = ttk.Combobox(register_frame, textvariable = self.var_stu_Numb, state = "readonly")
        self.StuNum_combobox.place(x = 80, y = 45, width = 120, height = 25)
        self.StuName_combobox = ttk.Combobox(register_frame, textvariable=self.var_stu_name, state="readonly")
        self.StuName_combobox.place(x = 80, y = 90, width = 120, height = 25)
        """绘制学生姓名/学号下拉框 结束"""

        """绘制科目下拉框 开始"""
        self.sub_index = 0
        self.subject_combobox = ttk.Combobox(register_frame, textvariable=var_Subject, state = "readonly")
        self.subName = self.subject_combobox["value"] = ("高数", "英语", "Python")  # self.subName 是存储科目元组，用于定位当前科目定位和插入操作
        self.subject_combobox.current(self.sub_index)
        self.subject_combobox.place(x = 80, y = 135, width = 120, height = 25)
        """绘制科目下拉框 结束"""

        """绘制成绩输入框 开始"""
        subject_entry = ttk.Entry(register_frame, textvariable = var_Subject_entry)
        subject_entry.place(x = 80, y = 180, width = 120, height = 25)
        """绘制成绩输入框 结束"""

        """绘制控制区按钮 开始"""
        ttk.Button(control_frame, text = "添加信息", command =  # 绘制登记界面 添加信息btn
                        lambda : [self.insert_info(self.subName.index(var_Subject.get()),
                                  self.var_stu_name.get(),
                                  self.var_stu_Numb.get(),
                                  var_Subject_entry.get()),]).place(x = 10, y = 25)
        ttk.Button(control_frame, text = "删除信息", command =  # 绘制登记界面 删除信息btn
                        lambda : [self.score_Tree.delete(select)
                                  for select in self.score_Tree.selection()]).place(x = 10, y = 75)
        ttk.Button(control_frame, text = "导出成绩", command = self.save_data).place(x = 120, y = 25) # 绘制登记界面 保存本地btn
        ttk.Button(control_frame, text = "成绩分析", command =  # 绘制登记界面 成绩分析btn
                        lambda : [self.load_analys(width = Width, height = Height,
                                                   stuNum = [*self.StuNum_combobox["value"]],
                                                   stuName = [*self.StuName_combobox["value"]])]).place(x = 120, y = 75)
        ttk.Button(control_frame, text = "添加班级信息", command =   # 绘制登记界面 添加班级信息btn
                        lambda :[self.add_info(Width, Height)]).place(x = 10, y = 125, width= 100)
        ttk.Button(control_frame, text = "发布成绩", command = self.Release_score).place(x = 120, y = 125)  # 绘制登记界面 发布成绩btn
        """绘制控制区按钮 结束"""

        """绘制班级信息、成绩登录插入表的组件信息 开始"""
        score_cols = ("姓名", "学号", "高数", "英语", "Python")
        self.score_Tree = ttk.Treeview(addS_frame, show = "headings", columns = score_cols, # 成绩登录插入表
                                            selectmode = tk.EXTENDED)
        self.score_Tree.place(relwidth = 1, relheight = 1)
        for state_col in score_cols:
            self.score_Tree.heading(state_col, text = state_col)
            self.score_Tree.column(state_col, width = 25, anchor="w")
        else:
            del score_cols

        class_colum = ("班级","状态")
        self.class_tree = ttk.Treeview(class_frame, show = "headings", columns = class_colum,  # 班级信息表
                                       selectmode = tk.EXTENDED)
        self.class_tree.place(relwidth = 1, relheight = 1)
        for state_col in class_colum:
            self.class_tree.heading(state_col, text = state_col)
            self.class_tree.column(state_col, width = 25, anchor = "w")
        else:
            del class_colum
        [self.class_tree.insert("", "end", values = (info, "打开")) for info in class_info]
        """绘制班级信息、成绩登录插入表的组件信息 结束"""

        """控件绑定事件函数定义 开始"""
        def select_num(event=None):
            """
            设置选择学生学号下拉框时，姓名下拉框的跳转机制函数
            原理：
                # 先获取学号下拉框内容定义为num_lst
                # 获取当前新的学号下拉框数据，并从num_lst获取其具体序列位置信息
                # 最后根据获取到的序列信息，将姓名下拉框的序列值替换为 上一则获取的位置信息
            :param event: 事件响应信息
            """
            num_lst = self.StuNum_combobox["value"]  # 先获取学号下拉框内容
            self.stu_INFO_index = num_lst.index(int(self.StuNum_combobox.get()))
            self.StuName_combobox.current(self.stu_INFO_index)

        def select_name(event=None):
            """
            设置选择学生姓名下拉框时，学号下拉框的跳转机制函数
            原理：
                # 先获取姓名下拉框内容定义为name_lst
                # 获取当前新的姓名下拉框数据，并从name_lst获取其具体序列位置信息
                # 最后根据获取到的序列信息，将学号下拉框的序列值替换为 上一则获取的位置信息
            :param event: 事件响应信息
            """
            name_lst = self.StuName_combobox["value"]
            self.stu_INFO_index = name_lst.index(self.StuName_combobox.get())
            self.StuNum_combobox.current(self.stu_INFO_index)

        def return_add(event=None):
            """
            添加信息事件绑定机制，响应条件为按下回车键
            :param event: 事件响应信息
            """
            self.insert_info(self.subName.index(var_Subject.get()),
                             self.var_stu_name.get(),
                             self.var_stu_Numb.get(),
                             var_Subject_entry.get())
            var_Subject_entry.set("")
        """控件绑定事件函数定义 结束"""

        """控件事件绑定机制设置 开始"""
        win_register.bind("&lt;Return&gt;", return_add)
        self.class_tree.bind("&lt;Double-Button-1&gt;", self.open_class)  # 双击班级信息区里的 打开按钮时，打开读取对应班级信息
        self.StuNum_combobox.bind("&lt;&lt;ComboboxSelected&gt;&gt;", select_num)
        self.StuName_combobox.bind("&lt;&lt;ComboboxSelected&gt;&gt;", select_name)
        """控件事件绑定机制设置 结束"""

if __name__ == "__main__":
    """程序入口"""
    win = tk.Tk() # 实例化Tkinter方法，类继承的方法传入主类
    w = Main(master=win)
    w.mainloop()

```

##### 文件目录
- work_data- ​ .udsc格式文件 本质为csv文件转型，已登记完成的成绩文件- user_data- ​ |-- .udcl格式文件 pickle加密文件，各班最新发布成绩文件- ​ |-- .udpk格式文件 pickle加密文件，student和teacher分别是学生、教师的账号信息- ​ 其中包含了账号、密码、所在班级信息- class_data- ​ |-- .csv格式文件 班级成员信息- img- ​ |-- welcome.png 登录界面背景图 下载地址：