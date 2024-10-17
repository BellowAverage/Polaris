
--- 
title:  用Python写了一个疫苗信息管理系统 
tags: []
categories: [] 

---
### 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

https://blog.csdn.net/weixin_43425784/article/details/118585467

>  
  本来这个小应用是给一个客户做的，后来找个理由又说不要了，当时心里真是我艹（一种植物）了，其实之前没用过Tkinter，只能边做边学，还好不是太难，一夜就肝出来了。由于时间比较紧，所以只实现了基本功能，有很多地方的代码可以进行优化，界面美化页没有怎么弄，后期应该也不弄了，反正我也用不到这玩意儿。Tkinter对于那些只是临时使用，需要快速开发出一个满足基本需求的轻型应用的用户来说，还是非常香的，相关组件也是相当完整的，看到这里估计肯定有人想说pyside2和pyqt5，嗯~~，它俩也挺好的。下面的代码供大家交流使用，哪位大佬想赐教可以直接评论，嘿嘿嘿！ 
 

<img src="https://img-blog.csdnimg.cn/img_convert/ea7ccdb0896bd26071f1ec7500187a4d.png" height="80" width="80">

#### 整体结构图

<img src="https://img-blog.csdnimg.cn/img_convert/53e33045700892a2dd3d1a477535afea.png">

#### 连接数据库

```
    def connect_DBS(self, database, content):
        db = pymysql.connect(host="localhost", user="root", password="pwd", database=database)
        cursor = db.cursor()
        cursor.execute(content)
        data = cursor.fetchone()
        db.commit()
        db.close()
        return data

```

#### 主界面

<img src="https://img-blog.csdnimg.cn/img_convert/0dbe6609fde6d4cef431be22e36b520e.png" height="350" width="600">

```
    def main_window(self):
        tk.Button(app, text='登录', bg='white', font=("Arial,12"), width=12, height=1, command=self.login).place(x=260,                                                                                                      y=200)
        tk.Button(app, text='注册', bg='white', font=("Arial,12"), width=12, height=1, command=self.register).place(x=260,                                                                                                                y=240)
        tk.Button(app, text='退出', bg='white', font=("Arial,12"), width=12, height=1, command=self.quit_mainloop).place(x=260, y=280)

```

#### 注册界面

<img src="https://img-blog.csdnimg.cn/img_convert/150e1c3407e9360fb07d750154b852e2.gif" height="400" width="600">

```
    def register(self):
        register = tk.Toplevel(app)
        register.title('用户注册')
        register.geometry("600x400")
        tk.Label(register, text="欢迎注册", font=("KaiTi", 40)).place(x=200, y=20)
        tk.Label(register, text='添加管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
        tk.Label(register, text='确认管理员编号：', font=('Arial', 9)).place(x=80, y=150)
        entry1 = tk.Entry(register, font=("Arial, 9"), width=46, )
        entry2 = tk.Entry(register, font=("Arial, 9"), width=46, )
        entry1.pack()
        entry2.pack()
        entry1.place(x=180, y=120, width=350, height=25)
        entry2.place(x=180, y=150, width=350, height=25)


        def user_register():
            user_name = entry1.get()
            user_code = entry2.get()
            if user_name == "" or user_code == "":
                tkinter.messagebox.showwarning(title="警告", message="用户名或密码不能为空！")
            else:
                content = "INSERT INTO user_info (user_name, user_code) VALUES ('%s', '%s');" % (user_name, user_code)
                self.connect_DBS(database="vaccine_info", content=content)
                tkinter.messagebox.showinfo(title="信息", message="注册成功！")
        tk.Button(register, text="注册", bg='white', font=("Arial,9"), width=12, height=0, command=user_register).place(x=250, y=250)

```

#### 登陆界面

<img src="https://img-blog.csdnimg.cn/img_convert/286365bea047dc748d4836294aad9048.gif" height="400" width="600">

```
    def login(self):
        login = tk.Toplevel(app)
        login.title('用户登录')
        login.geometry("600x400")
        tk.Label(login, text="欢迎登录", font=("KaiTi", 40)).place(x=200, y=20)
        tk.Label(login, text='管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
        tk.Label(login, text='管理员编号：', font=('Arial', 9)).place(x=80, y=150)
        entry1 = tk.Entry(login, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(login, font=("Arial, 9"), width=46, show="*")
        entry1.pack()
        entry2.pack()
        entry1.place(x=180, y=120, width=350, height=25)
        entry2.place(x=180, y=150, width=350, height=25)


        def user_check():
            user_name = entry1.get()
            user_code = entry2.get()
            content = "SELECT * FROM user_info WHERE user_name = '%s';" % user_name
            data = self.connect_DBS(database="vaccine_info", content=content)
            try:
                if user_name == data[1] and user_code == data[2]:
                    tkinter.messagebox.showinfo(title="信息", message="欢迎登录！")
                    self.options()
                elif user_name != data[1]:
                    tkinter.messagebox.showerror(title="错误", message="请注册后再进行登录！")
                elif user_name == data[1] and user_code != data[2]:
                    tkinter.messagebox.showerror(title="错误", message="密码错误！")
            except TypeError:
                tkinter.messagebox.showerror(title="错误", message="请注册后再进行登录！")
        tk.Button(login, text="登录", bg='white', font=("Arial,9"), width=12, height=0, command=user_check).place(x=250, y=250)

```

#### 功能选项

##### 功能区主界面

<img src="https://img-blog.csdnimg.cn/img_convert/6151e6eccf95e37d534b421b743878dc.png" height="500" width="600">

```
    def options(self):
        options = tk.Toplevel(app)
        options.title('功能选项')
        options.geometry("600x500")
        tk.Label(options, text="欢迎使用！", font=("KaiTi", 40)).place(x=180, y=15)
        tk.Button(options, text='新建疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.add_vacc_info).place(x=100, y=100)
        tk.Button(options, text='新建疫苗分配信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.add_vaccine_distr_info).place(x=100, y=160)
        tk.Button(options, text='新建疫苗养护信息', bg='white', font=("Arial,12"), width=20, height=2,              command=self.add_vaccine_maintenance_info).place(x=100, y=220)
        tk.Button(options, text='新建接种人员信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.add_vaccination_person_info).place(x=100, y=280)
        tk.Button(options, text='查询疫苗分配信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccine_distr_info_query).place(x=100, y=340)
        tk.Button(options, text='查询疫苗养护信息', bg='white', font=("Arial,12"), width=20, height=2,           command=self.vaccination_maintenance_info_query).place(x=320, y=100)
        tk.Button(options, text='查询接种人员信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccination_person_info_query).place(x=320, y=160)
        tk.Button(options, text='查询疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccine_info_query).place(x=320, y=220)
        tk.Button(options, text='修改疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.modify_vaccine_info).place(x=320, y=280)
        tk.Button(options, text='删除疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.del_vaccine_info).place(x=320, y=340)

```

###### 新建疫苗信息

<img src="https://img-blog.csdnimg.cn/img_convert/ec3a58d81ad5c0c031996d36e2a6fdde.gif" height="400" width="600">

```
    def add_vacc_info(self):
        add_vacc_info = tk.Toplevel(app)
        add_vacc_info.title('添加疫苗信息')
        add_vacc_info.geometry("600x400")
        tk.Label(add_vacc_info, text='疫苗批号：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(add_vacc_info, text='疫苗名称：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(add_vacc_info, text='企业名称：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(add_vacc_info, text='企业编号：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(add_vacc_info, text='    规格：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(add_vacc_info, text='    进价：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(add_vacc_info, text='  预售价：', font=('Arial', 9)).place(x=80, y=240)
        tk.Label(add_vacc_info, text='企业上限：', font=('Arial', 9)).place(x=80, y=270)
        tk.Label(add_vacc_info, text='企业下限：', font=('Arial', 9)).place(x=80, y=300)
        entry1 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry8 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry9 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry1.pack()
        entry2.pack()
        entry3.pack()
        entry4.pack()
        entry5.pack()
        entry6.pack()
        entry7.pack()
        entry8.pack()
        entry9.pack()
        entry1.place(x=180, y=60, width=350)
        entry2.place(x=180, y=90, width=350)
        entry3.place(x=180, y=120, width=350)
        entry4.place(x=180, y=150, width=350)
        entry5.place(x=180, y=180, width=350)
        entry6.place(x=180, y=210, width=350)
        entry7.place(x=180, y=240, width=350)
        entry8.place(x=180, y=270, width=350)
        entry9.place(x=180, y=300, width=350)


        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            text8 = entry8.get()
            text9 = entry9.get()
            content = "INSERT INTO vaccine_info (" \
                      "vaccine_num, vaccine_name, company_name, company_num, size, buy_price, pre_sale_price, limit_up, limit_down" \
                      ")" \
                      " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                      text1, text2, text3, text4, text5, text6, text7, text8, text9)
            self.connect_DBS(database="vaccine_info", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")


        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")
        tk.Button(add_vacc_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0, command=add).place(x=400,                                                                                                       y=360)
        tk.Button(add_vacc_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0, command=clear).place(x=160,                                                                                                             y=360)

```

###### 新建疫苗分配信息

<img src="https://img-blog.csdnimg.cn/img_convert/925bb18f6d6ad8de1053079dac46e9f1.gif" height="400" width="600">

```
    def add_vaccine_distr_info(self):
        add_vaccine_distr_info = tk.Toplevel(app)
        add_vaccine_distr_info.title('添加疫苗分配信息')
        add_vaccine_distr_info.geometry("600x400")
        tk.Label(add_vaccine_distr_info, text='疫苗分配单号：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(add_vaccine_distr_info, text='       日期：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(add_vaccine_distr_info, text='   疫苗批号：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(add_vaccine_distr_info, text='   疫苗名称：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(add_vaccine_distr_info, text='   企业编号：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(add_vaccine_distr_info, text=' 质检员编号：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(add_vaccine_distr_info, text='      数量：', font=('Arial', 9)).place(x=80, y=240)
        entry1 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry1.pack()
        entry2.pack()
        entry3.pack()
        entry4.pack()
        entry5.pack()
        entry6.pack()
        entry7.pack()
        entry1.place(x=180, y=60, width=350)
        entry2.place(x=180, y=90, width=350)
        entry3.place(x=180, y=120, width=350)
        entry4.place(x=180, y=150, width=350)
        entry5.place(x=180, y=180, width=350)
        entry6.place(x=180, y=210, width=350)
        entry7.place(x=180, y=240, width=350)


        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            content = "INSERT INTO vaccine_distr_info (" \
                      "vaccine_distr_num, date, vaccine_num, vaccine_name, company_num, operator_num, num" \
                      ")" \
                      " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7)
            self.connect_DBS(database="vaccine_info", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")


        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            entry6.delete(0, "end")
            entry7.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")
        tk.Button(add_vaccine_distr_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0,command=add).place(x=400,y=360)
        tk.Button(add_vaccine_distr_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0,command=clear).place(x=160,y=360)

```

###### 新建疫苗养护信息

<img src="https://img-blog.csdnimg.cn/img_convert/b34848ccaf5a715d49b1d913ee82099b.gif" height="400" width="600">

```
    def add_vaccine_maintenance_info(self):
        vaccine_maintenance_info = tk.Toplevel(app)
        vaccine_maintenance_info.title('添加疫苗养护信息')
        vaccine_maintenance_info.geometry("600x400")
        tk.Label(vaccine_maintenance_info, text='养护疫苗批号：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(vaccine_maintenance_info, text='养护疫苗名称：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(vaccine_maintenance_info, text=' 管理员编号：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(vaccine_maintenance_info, text=' 管理员姓名：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(vaccine_maintenance_info, text='   养护时间：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(vaccine_maintenance_info, text=' 冷藏室温度：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(vaccine_maintenance_info, text=' 冷冻室温度：', font=('Arial', 9)).place(x=80, y=240)
        tk.Label(vaccine_maintenance_info, text='设备运转情况：', font=('Arial', 9)).place(x=80, y=270)
        tk.Label(vaccine_maintenance_info, text='    是否报警：', font=('Arial', 9)).place(x=80, y=300)
        entry1 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry8 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry9 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry1.pack()
        entry2.pack()
        entry3.pack()
        entry4.pack()
        entry5.pack()
        entry6.pack()
        entry7.pack()
        entry8.pack()
        entry9.pack()
        entry1.place(x=180, y=60, width=350)
        entry2.place(x=180, y=90, width=350)
        entry3.place(x=180, y=120, width=350)
        entry4.place(x=180, y=150, width=350)
        entry5.place(x=180, y=180, width=350)
        entry6.place(x=180, y=210, width=350)
        entry7.place(x=180, y=240, width=350)
        entry8.place(x=180, y=270, width=350)
        entry9.place(x=180, y=300, width=350)


        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            text8 = entry8.get()
            text9 = entry9.get()
            content = "INSERT INTO vaccine_maintenance_info (" \
                      "vaccine_maintenance_num, vaccine_maintenance_name, admin_num, admin_name, maintenance_time, cold_storage_temp, freezer_temp, equipment_operation, alter_info" \
                      ")" \
                      " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7, text8, text9)
            self.connect_DBS(database="vaccine_info", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")


        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            entry6.delete(0, "end")
            entry7.delete(0, "end")
            entry8.delete(0, "end")
            entry9.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")
        tk.Button(vaccine_maintenance_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0,command=add).place(x=400,y=360)
        tk.Button(vaccine_maintenance_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0,command=clear).place(x=160,y=360)

```

###### 新建接种人员信息

<img src="https://img-blog.csdnimg.cn/img_convert/8988365ffb240c437d8a2e2e5370d18d.gif" height="400" width="600">

```
    def add_vaccination_person_info(self):
        add_vaccination_person_info = tk.Toplevel(app)
        add_vaccination_person_info.title('添加接种人员信息')
        add_vaccination_person_info.geometry("600x400")
        tk.Label(add_vaccination_person_info, text='姓名：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(add_vaccination_person_info, text='性别：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(add_vaccination_person_info, text='年龄：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(add_vaccination_person_info, text='身份证号：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(add_vaccination_person_info, text='家庭住址：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(add_vaccination_person_info, text='是否过敏：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(add_vaccination_person_info, text='接种时间：', font=('Arial', 9)).place(x=80, y=240)
        entry1 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry1.pack()
        entry2.pack()
        entry3.pack()
        entry4.pack()
        entry5.pack()
        entry6.pack()
        entry7.pack()
        entry1.place(x=180, y=60, width=350)
        entry2.place(x=180, y=90, width=350)
        entry3.place(x=180, y=120, width=350)
        entry4.place(x=180, y=150, width=350)
        entry5.place(x=180, y=180, width=350)
        entry6.place(x=180, y=210, width=350)
        entry7.place(x=180, y=240, width=350)


        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            content = "INSERT INTO vaccination_person_info (" \
                      "name, sexy, age, ID_num, address, allergy, date" \
                      ")" \
                      " VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7)
            self.connect_DBS(database="vaccine_info", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")


        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            entry6.delete(0, "end")
            entry7.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")
        tk.Button(add_vaccination_person_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0,command=add).place(x=400, y=360)
        tk.Button(add_vaccination_person_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0,command=clear).place(x=160, y=360)

```

###### 查询疫苗分配信息

<img src="https://img-blog.csdnimg.cn/img_convert/975b93d09281219d58494b0cef317933.gif" height="400" width="600">

```
    def vaccine_distr_info_query(self):
        query = tk.Toplevel(app)
        query.title('信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗分配单号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)


        def base_query():
            vaccine_distr_num = entry.get()
            print(vaccine_distr_num)
            content = "SELECT * FROM vaccine_distr_info WHERE vaccine_distr_num = %s;" % vaccine_distr_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")
        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,
                                                                                                                y=75)

```

###### 查询疫苗养护信息

<img src="https://img-blog.csdnimg.cn/img_convert/327bce87201376493c3b78f4ad5d3f79.gif" height="400" width="600">

```
    def vaccination_maintenance_info_query(self):
        query = tk.Toplevel(app)
        query.title('疫苗养护信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗养护批号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)


        def base_query():
            vaccine_maintenance_num = entry.get()
            print(vaccine_maintenance_num)
            content = "SELECT * FROM vaccine_maintenance_info WHERE vaccine_maintenance_num = %s;" % vaccine_maintenance_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")
        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,
                                                                                                                y=75)
    def vaccine_distr_info_query(self):
        query = tk.Toplevel(app)
        query.title('信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗分配单号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)


        def base_query():
            vaccine_distr_num = entry.get()
            print(vaccine_distr_num)
            content = "SELECT * FROM vaccine_distr_info WHERE vaccine_distr_num = %s;" % vaccine_distr_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")
        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,
                                                                                                                y=75)

```

###### 查询接种人员信息

<img src="https://img-blog.csdnimg.cn/img_convert/d8e256cb4f77dc82865b91d38ca1cb68.gif" height="400" width="600">

```
 def vaccination_person_info_query(self):
        query = tk.Toplevel(app)
        query.title('接种人员信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入接种人员身份证号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)


        def base_query():
            ID_num = entry.get()
            content = "SELECT * FROM vaccination_person_info WHERE ID_num = %s;" % ID_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")
        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,                                                                                                          y=75)

```

###### 查询疫苗信息

<img src="https://img-blog.csdnimg.cn/img_convert/b9f391e36e23472a900eff04fede9a90.gif" height="400" width="600">

```
    def vaccine_info_query(self):
        query = tk.Toplevel(app)
        query.title('疫苗信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗批号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)


        def base_query():
            vaccine_num = entry.get()
            content = "SELECT * FROM vaccine_info WHERE vaccine_num = %s;" % vaccine_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")
        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,                                                                                                          y=75)

```

###### 修改疫苗信息

<img src="https://img-blog.csdnimg.cn/img_convert/0efc21842be5ec3904554752ec9f8f1d.gif" height="400" width="600">

```
    def modify_vaccine_info(self):
        modify_info = tk.Toplevel(app)
        modify_info.title('疫苗信息修改')
        modify_info.geometry("600x400")
        entry = tk.Entry(modify_info, width=30)
        entry.pack()
        entry.place(x=200, y=60)
        tk.Label(modify_info, text="请输入疫苗分配单号：", font=("Arial", 9)).place(x=50, y=60)
        tk.Label(modify_info, text='疫苗批号：', font=("Arial", 9)).place(x=80, y=100)
        tk.Label(modify_info, text='疫苗名称：', font=('Arial', 9)).place(x=80, y=130)
        tk.Label(modify_info, text='企业名称：', font=('Arial', 9)).place(x=80, y=160)
        tk.Label(modify_info, text='企业编号：', font=('Arial', 9)).place(x=80, y=190)
        tk.Label(modify_info, text='    规格：', font=('Arial', 9)).place(x=80, y=220)
        tk.Label(modify_info, text='    进价：', font=('Arial', 9)).place(x=80, y=250)
        tk.Label(modify_info, text='  预售价：', font=('Arial', 9)).place(x=80, y=280)
        tk.Label(modify_info, text='企业上限：', font=('Arial', 9)).place(x=80, y=310)
        tk.Label(modify_info, text='企业下限：', font=('Arial', 9)).place(x=80, y=340)
        text1 = tk.Text(modify_info, width=50, height=1)
        text2 = tk.Text(modify_info, width=50, height=1)
        text3 = tk.Text(modify_info, width=50, height=1)
        text4 = tk.Text(modify_info, width=50, height=1)
        text5 = tk.Text(modify_info, width=50, height=1)
        text6 = tk.Text(modify_info, width=50, height=1)
        text7 = tk.Text(modify_info, width=50, height=1)
        text8 = tk.Text(modify_info, width=50, height=1)
        text9 = tk.Text(modify_info, width=50, height=1)
        text1.pack()
        text2.pack()
        text3.pack()
        text4.pack()
        text5.pack()
        text6.pack()
        text7.pack()
        text8.pack()
        text9.pack()
        text1.place(x=150, y=100)
        text2.place(x=150, y=130)
        text3.place(x=150, y=160)
        text4.place(x=150, y=190)
        text5.place(x=150, y=220)
        text6.place(x=150, y=250)
        text7.place(x=150, y=280)
        text8.place(x=150, y=310)
        text9.place(x=150, y=340)


        def base_query():
            vaccine_modify_num = entry.get()
            content = "SELECT * FROM vaccine_info WHERE vaccine_num = %s;" % vaccine_modify_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text2.delete(1.0, "end")
            text3.delete(1.0, "end")
            text4.delete(1.0, "end")
            text5.delete(1.0, "end")
            text6.delete(1.0, "end")
            text7.delete(1.0, "end")
            text8.delete(1.0, "end")
            text9.delete(1.0, "end")
            text1.insert(chars="{}".format(data[0]), index="insert")
            text2.insert(chars="{}".format(data[1]), index="insert")
            text3.insert(chars="{}".format(data[2]), index="insert")
            text4.insert(chars="{}".format(data[3]), index="insert")
            text5.insert(chars="{}".format(data[4]), index="insert")
            text6.insert(chars="{}".format(data[5]), index="insert")
            text7.insert(chars="{}".format(data[6]), index="insert")
            text8.insert(chars="{}".format(data[7]), index="insert")
            text9.insert(chars="{}".format(data[8]), index="insert")


        def update_info():
            vaccine_del_num = entry.get()
            str_ls = [text1.get("1.0", "end")[0:-1], text2.get("1.0", "end")[0:-1], text3.get("1.0", "end")[0:-1],
                      text4.get("1.0", "end")[0:-1], text5.get("1.0", "end")[0:-1], text6.get("1.0", "end")[0:-1],
                      text7.get("1.0", "end")[0:-1], text8.get("1.0", "end")[0:-1], text9.get("1.0", "end")[0:-1]]
            str_ls = [str(i) for i in str_ls]
            content = "UPDATE vaccine_info  SET vaccine_num='%s', vaccine_name='%s', company_name='%s', vaccine_num='%s'" \
                      ", size='%s', buy_price='%s', pre_sale_price='%s', limit_up='%s', limit_down='%s' WHERE " \
                      "vaccine_num = '%s';" % (
                      str_ls[0], str_ls[1], str_ls[2], str_ls[3], str_ls[4], str_ls[5], str_ls[6], str_ls[7], str_ls[8],vaccine_del_num)
            self.connect_DBS(database="vaccine_info", content=content)
            tkinter.messagebox.showinfo(title="信息", message="疫苗分配单号：{}数据修改成功！".format(vaccine_modify_num)
            return None
        tk.Button(modify_info, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=55)
        tk.Button(modify_info, text='修改', bg='white', font=("Arial,12"), width=9, height=0, command=update_info).place(x=260,y=370)

```

###### 删除疫苗信息

<img src="https://img-blog.csdnimg.cn/img_convert/135a84eb9ca0b60d60c800ed3d787478.gif" height="400" width="600">

```
   def del_vaccine_info(self):
        del_info = tk.Toplevel(app)
        del_info.title('疫苗信息删除')
        del_info.geometry("600x500")
        entry = tk.Entry(del_info, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(del_info, text="请输入疫苗批号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(del_info, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(del_info, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)


        def base_query():
            vaccine_del_num = entry.get()
            print(vaccine_del_num)
            content = "SELECT * FROM vaccine_info WHERE vaccine_num = %s;" % vaccine_del_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")


        def del_infor():
            vaccine_del_num = entry.get()
            print(vaccine_del_num)
            content = "DELETE FROM vaccine_info  WHERE vaccine_num = %s;" % vaccine_del_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            tkinter.messagebox.showinfo(title="信息", message="疫苗批号：{}数据已删除！".format(vaccine_del_num))
            return None
        tk.Button(del_info, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=75)
        tk.Button(del_info, text='删除', bg='white', font=("Arial,12"), width=9, height=0, command=del_infor).place(x=280,
                                                                                                                  y=400

```

数据库<img src="https://img-blog.csdnimg.cn/img_convert/2047bd942b1a6c725766c53df8094448.png" height="200" width="350">

```
create table vaccine_info(
    vaccine_num    char(50) not null primary key,
    vaccine_name   char(50) not null,
    company_name   char(50) not null,
    company_num    char(50) not null,
    size           char(50) null,
    buy_price      char(50) not null,
    pre_sale_price char(20) not null,
    limit_up       char(50) not null,
    limit_down     char(50) not null
);


create table user_info(
  id int auto_increment primary key,
    user_name char(50) NOT NULL ,
    user_code char(50) NOT NULL
);
                        
create table if not exists vaccine_distr_info (
    vaccine_distr_num char(50) primary key,
    date date not null ,
    vaccine_num char(50) not null ,
    vaccine_name char(50) not null ,
    company_num char(50) not null ,
    operator_num char(50) not null ,
    num int not null 
);


create table if not exists vaccine_maintenance_info (
    vaccine_maintenance_num char(50) primary key ,
    vaccine_maintenance_name char(50) not null ,
    admin_num char(50) not null ,
    admin_name char(50) not null ,
    maintenance_time date,
    cold_storage_temp char(20) not null ,
    freezer_temp char(20) not null ,
    equipment_operation char(50) not null ,
    alter_info char(50) not null 
);


create table if not exists vaccination_person_info(
    id int auto_increment primary key,
    name char(20) not null ,
    sexy char(10) not null ,
    age char(10) not null ,
    ID_num char(50) not null ,
    address char(70) not null ,
    allergy char(10) not null ,
    date date
);

```

**道友路过给个赞吧！！！**
