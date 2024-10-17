
--- 
title:  用Python写个学生宿舍管理系统(附源码) 
tags: []
categories: [] 

---
今天我们用Python写个简单的学生宿舍管理系统。

学生宿舍管理系统可以包括学生信息管理、宿舍信息管理、评价管理等功能。以下是一个简单的Python实现：

```
class Student:
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id

class Dorm:
    def __init__(self, name, floor, capacity):
        self.name = name
        self.floor = floor
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students)&lt; self.capacity:
            self.students.append(student)
        else:
            print("宿舍已满，无法添加学生。")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("学生不在此宿舍，无法移除。")

    def get_students(self):
        return self.students

class DormManagementSystem:
    def __init__(self):
        self.dorms = []
        self.students = []

    def add_dorm(self, dorm):
        self.dorms.append(dorm)

    def add_student(self, student):
        self.students.append(student)

    def assign_student_to_dorm(self, student, dorm):
        if student in self.students and dorm in self.dorms:
            dorm.add_student(student)
        else:
            print("学生或宿舍不存在，无法分配。")

    def remove_student_from_dorm(self, student, dorm):
        if student in self.students and dorm in self.dorms:
            dorm.remove_student(student)
        else:
            print("学生或宿舍不存在，无法移除。")

    def get_dorm_students(self, dorm):
        if dorm in self.dorms:
            return dorm.get_students()
        else:
            print("宿舍不存在。")

# 示例
dms = DormManagementSystem()

# 添加宿舍和学生
dms.add_dorm(Dorm("A楼1号楼", 1, 6))
dms.add_dorm(Dorm("A楼2号楼", 2, 6))
dms.add_student(Student("张三", 20, "男", "20230001"))
dms.add_student(Student("李四", 21, "女", "20230002"))

# 分配学生到宿舍
dms.assign_student_to_dorm(dms.students[0], dms.dorms[0])
dms.assign_student_to_dorm(dms.students[1], dms.dorms[1])

# 获取宿舍学生信息
print(dms.get_dorm_students(dms.dorms[0]))

# 移除宿舍学生
dms.remove_student_from_dorm(dms.students[0], dms.dorms[0])
```

这个示例中，我们定义了三个类：`Student`、`Dorm`和`DormManagementSystem`。`Student`表示学生，`Dorm`表示宿舍，`DormManagementSystem`表示学生宿舍管理系统。

`DormManagementSystem`类包括添加宿舍、添加学生、分配学生到宿舍、移除宿舍学生、获取宿舍学生信息等方法。

在示例中，我们创建了一个`DormManagementSystem`实例，添加了两个宿舍和两个学生，然后将学生分配到宿舍，并获取宿舍学生信息。

我们可以使用Python的Tkinter库来实现一个简单的GUI界面。以下是一个示例：

```
import tkinter as tk
from tkinter import ttk

class Student:
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id

class Dorm:
    def __init__(self, name, floor, capacity):
        self.name = name
        self.floor = floor
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students)&lt; self.capacity:
            self.students.append(student)
        else:
            print("宿舍已满，无法添加学生。")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("学生不在此宿舍，无法移除。")

    def get_students(self):
        return self.students

class DormManagementSystem:
    def __init__(self):
        self.dorms = []
        self.students = []

    def add_dorm(self, dorm):
        self.dorms.append(dorm)

    def add_student(self, student):
        self.students.append(student)

    def assign_student_to_dorm(self, student, dorm):
        if student in self.students and dorm in self.dorms:
            dorm.add_student(student)
        else:
            print("学生或宿舍不存在，无法分配。")

    def remove_student_from_dorm(self, student, dorm):
        if student in self.students and dorm in self.dorms:
            dorm.remove_student(student)
        else:
            print("学生或宿舍不存在，无法移除。")

    def get_dorm_students(self, dorm):
        if dorm in self.dorms:
            return dorm.get_students()
        else:
            print("宿舍不存在。")

class DormManagementGUI:
    def __init__(self, dms):
        self.dms = dms
        self.window = tk.Tk()
        self.window.title("学生宿舍管理系统")

        # 添加宿舍按钮
        self.add_dorm_button = ttk.Button(self.window, text="添加宿舍", command=self.add_dorm)
        self.add_dorm_button.grid(column=0, row=0)

        # 添加学生按钮
        self.add_student_button = ttk.Button(self.window, text="添加学生", command=self.add_student)
        self.add_student_button.grid(column=1, row=0)

        # 分配学生到宿舍按钮
        self.assign_student_button = ttk.Button(self.window, text="分配学生到宿舍", command=self.assign_student_to_dorm)
        self.assign_student_button.grid(column=0, row=1)

        # 移除宿舍学生按钮
        self.remove_student_button = ttk.Button(self.window, text="移除宿舍学生", command=self.remove_student_from_dorm)
        self.remove_student_button.grid(column=1, row=1)

        # 获取宿舍学生信息按钮
        self.get_dorm_students_button = ttk.Button(self.window, text="获取宿舍学生信息", command=self.get_dorm_students)
        self.get_dorm_students_button.grid(column=0, row=2)

        self.window.mainloop()

    def add_dorm(self):
        pass

    def add_student(self):
        pass

    def assign_student_to_dorm(self):
        pass

    def remove_student_from_dorm(self):
        pass

    def get_dorm_students(self):
        pass

# 示例
dms = DormManagementSystem()
gui = DormManagementGUI(dms)
```

这个示例中，我们定义了一个`DormManagementGUI`类，用于创建GUI界面。在`__init__`方法中，我们创建了一个窗口，并添加了添加宿舍、添加学生、分配学生到宿舍、移除宿舍学生、获取宿舍学生信息等按钮。每个按钮都有一个对应的方法，用于实现相应的功能。

接着我们可以在`DormManagementGUI`类中添加输入框和列表框等控件，以便用户输入信息和查看结果。以下是一个示例：

```
import tkinter as tk
from tkinter import ttk

class Student:
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id

class Dorm:
    def __init__(self, name, floor, capacity):
        self.name = name
        self.floor = floor
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students)&lt; self.capacity:
            self.students.append(student)
        else:
            print("宿舍已满，无法添加学生。")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("学生不在此宿舍，无法移除。")

    def get_students(self):
        return self.students

class DormManagementSystem:
    def __init__(self):
        self.dorms = []
        self.students = []

    def add_dorm(self, dorm):
        self.dorms.append(dorm)

    def add_student(self, student):
        self.students.append(student)

    def assign_student_to_dorm(self, student, dorm):
        if student in self.students and dorm in self.dorms:
            dorm.add_student(student)
        else:
            print("学生或宿舍不存在，无法分配。")

    def remove_student_from_dorm(self, student, dorm):
        if student in self.students and dorm in self.dorms:
            dorm.remove_student(student)
        else:
            print("学生或宿舍不存在，无法移除。")

    def get_dorm_students(self, dorm):
        if dorm in self.dorms:
            return dorm.get_students()
        else:
            print("宿舍不存在。")

class DormManagementGUI:
    def __init__(self, dms):
        self.dms = dms
        self.window = tk.Tk()
        self.window.title("学生宿舍管理系统")

        # 添加宿舍按钮
        self.add_dorm_button = ttk.Button(self.window, text="添加宿舍", command=self.add_dorm)
        self.add_dorm_button.grid(column=0, row=0)

        # 添加学生按钮
        self.add_student_button = ttk.Button(self.window, text="添加学生", command=self.add_student)
        self.add_student_button.grid(column=1, row=0)

        # 分配学生到宿舍按钮
        self.assign_student_button = ttk.Button(self.window, text="分配学生到宿舍", command=self.assign_student_to_dorm)
        self.assign_student_button.grid(column=0, row=1)

        # 移除宿舍学生按钮
        self.remove_student_button = ttk.Button(self.window, text="移除宿舍学生", command=self.remove_student_from_dorm)
        self.remove_student_button.grid(column=1, row=1)

        # 获取宿舍学生信息按钮
        self.get_dorm_students_button = ttk.Button(self.window, text="获取宿舍学生信息", command=self.get_dorm_students)
        self.get_dorm_students_button.grid(column=0, row=2)

        # 添加宿舍名称输入框
        self.dorm_name_label = ttk.Label(self.window, text="宿舍名称：")
        self.dorm_name_label.grid(column=0, row=3)
        self.dorm_name_entry = ttk.Entry(self.window)
        self.dorm_name_entry.grid(column=1, row=3)

        # 添加宿舍楼层输入框
        self.dorm_floor_label = ttk.Label(self.window, text="宿舍楼层：")
        self.dorm_floor_label.grid(column=0, row=4)
        self.dorm_floor_entry = ttk.Entry(self.window)
        self.dorm_floor_entry.grid(column=1, row=4)

        # 添加宿舍容量输入框
        self.dorm_capacity_label = ttk.Label(self.window, text="宿舍容量：")
        self.dorm_capacity_label.grid(column=0, row=5)
        self.dorm_capacity_entry = ttk.Entry(self.window)
        self.dorm_capacity_entry.grid(column=1, row=5)

        # 添加学生姓名输入框
        self.student_name_label = ttk.Label(self.window, text="学生姓名：")
        self.student_name_label.grid(column=0, row=6)
        self.student_name_entry = ttk.Entry(self.window)
        self.student_name_entry.grid(column=1, row=6)

        # 添加学生年龄输入框
        self.student_age_label = ttk.Label(self.window, text="学生年龄：")
        self.student_age_label.grid(column=0, row=7)
        self.student_age_entry = ttk.Entry(self.window)
        self.student_age_entry.grid(column=1, row=7)

        # 添加学生性别输入框
        self.student_gender_label = ttk.Label(self.window, text="学生性别：")
        self.student_gender_label.grid(column=0, row=8)
        self.student_gender_entry = ttk.Entry(self.window)
        self.student_gender_entry.grid(column=1, row=8)

        # 添加学生ID输入框
        self.student_id_label = ttk.Label(self.window, text="学生ID：")
        self.student_id_label.grid(column=0, row=9)
        self.student_id_entry = ttk.Entry(self.window)
        self.student_id_entry.grid(column=1, row=9)

        # 添加宿舍列表框
        self.dorm_listbox = tk.Listbox(self.window, height=5, width=20)
        self.dorm_listbox.grid(column=2, row=0, rowspan=5)

        # 添加学生列表框
        self.student_listbox = tk.Listbox(self.window, height=5, width=20)
        self.student_listbox.grid(column=2, row=5, rowspan=5)

        self.window.mainloop()

    def add_dorm(self):
        dorm_name = self.dorm_name_entry.get()
        dorm_floor = self.dorm_floor_entry.get()
        dorm_capacity = self.dorm_capacity_entry.get()
        dorm = Dorm(dorm_name, dorm_floor, dorm_capacity)
        self.dms.add_dorm(dorm)
        self.dorm_listbox.insert(tk.END, dorm_name)

    def add_student(self):
        student_name = self.student_name_entry.get()
        student_age = self.student_age_entry.get()
        student_gender = self.student_gender_entry.get()
        student_id = self.student_id_entry.get()
        student = Student(student_name, student_age, student_gender, student_id)
        self.dms.add_student(student)
        self.student_listbox.insert(tk.END, student_name)

    def assign_student_to_dorm(self):
        dorm_name = self.dorm_listbox.get(tk.ACTIVE)
        student_name = self.student_listbox.get(tk.ACTIVE)
        dorm = self.dms.get_dorm(dorm_name)
        student = self.dms.get_student(student_name)
        self.dms.assign_student_to_dorm(student, dorm)

    def remove_student_from_dorm(self):
        dorm_name = self.dorm_listbox.get(tk.ACTIVE)
        student_name = self.student_listbox.get(tk.ACTIVE)
        dorm = self.dms.get_dorm(dorm_name)
        student = self.dms.get_student(student_name)
        self.dms.remove_student_from_dorm(student, dorm)

    def get_dorm_students(self):
        dorm_name = self.dorm_listbox.get(tk.ACTIVE)
        dorm = self.dms.get_dorm(dorm_name)
        students = self.dms.get_dorm_students(dorm)
        for student in students:
            print(student.name)

# 示例
dms = DormManagementSystem()
gui = DormManagementGUI(dms)
```

这个示例中，我们在`DormManagementGUI`类中添加了输入框和列表框等控件，以便用户输入信息和查看结果。

这样我们就实现了一个简单的学生宿舍管理系统了，大家有兴趣的可以做进一步的完善。

```
👉 Python练手必备

👉 Python毕设实战项目
👉 Python爬虫实战必备
👉 30款Python小游戏附源码

👉 Python清理微信单向好友神器
```
