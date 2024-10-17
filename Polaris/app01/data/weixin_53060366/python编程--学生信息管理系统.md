
--- 
title:  python编程--学生信息管理系统 
tags: []
categories: [] 

---
## python编程–学生信息管理系统

>  
 初学python，自己上手做了一个简陋的学生信息管理系统，记录一下这美好的一刻！！！😀😀😀 


### 学生信息管理系统的模块：

>  
 - 添加学生及成绩信息；- 修改学生信息- 删除学生信- 查询学生信息- 排序（按单科成绩或总分排序）- 统计学生总人数- 显示所有学生信息- 将学生信息保存在文件中 


### 相关代码如下：

```
'''
python小案例--学生信息管理系统
'''
import os

filename='student.txt'

def main():
    while True:
        menu()
        try:
            choice=int(input('请选择：'))
        except:
            print('输入错误，请重新输入！')
            continue
        if choice in range(8):
            if choice == 0:
                answer=input('你确定要退出系统吗？y/n\t')
                if answer=='y' or answer=='Y':
                    print('感谢使用！！！')
                    break   #退出系统
                else:
                    continue
            elif choice == 1:
                insert()   #录入学生信息
            elif choice == 2:
                delete()   #删除学生信息
            elif choice == 3:
                modify()    #修改学生信息
            elif choice == 4:
                search()    #查找学生
            elif choice == 5:
                sort()     #排序
            elif choice == 6:
                total()    #学生总人数
            elif choice == 7:
                show()     #显示所有学生信息
        else:
            print('提示：请重新输入（0-7）')


def menu():
    print('====================================学生信息管理系统======================================')
    print('---------------------------------------功能菜单------------------------------------------')
    print('                                   1、增加学生信息')
    print('                                   2、删除学生信息')
    print('                                   3、修改学生信息')
    print('                                   4、查询学生信息')
    print('                                   5、排序')
    print('                                   6、统计学生总人数')
    print('                                   7、显示所有学生信息')
    print('                                   0、退出')
    print('----------------------------------------------------------------------------------------')


def insert():
    stu_lst=[]
    while True:
        id=input('请输入ID（如：1001）：')
        if not  id:
            break
        name=input('请输入姓名：')
        if not name:
            break
        try:
            en=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            java=int(input('请输入java成绩：'))

            print('=====学生信息录入完成。=====')
        except:
            print('输入无效，请重新输入。。。')
            continue
        #将录入的学生成绩保存到字典中
        student={<!-- -->'id':id,'name':name,'en':en,'python':python,'java':java}
        #将学生信息添加到列表中
        stu_lst.append(student)
        answer=input('是否继续添加？y/n\t')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

    #调用 save()函数，将学生信息保存到文件中
    save(stu_lst)
    # print('学生信息录入完成。')


def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def delete():   #输入ID，删除相应的学生
    while True:
        student_id=input('请输入学生的ID：')
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False   #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={<!-- -->}
                    for item in student_old:
                        d=dict(eval(item))   #将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'ID为{<!-- -->student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{<!-- -->student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()    #删除之后显示所有学生信息
            answer=input('是否继续删除？y/n\t')
            if answer=='y' or answer=='Y':
                continue
            else:
                break


def modify():
    show()    #修改前展示所有学生信息
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        print('暂未保存数据信息！！！')
        return

    student_id=input('请输入要修改的学生的ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改学生信息！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['en'] = int(input('请输入英语成绩：'))
                        d['python'] = int(input('请输入python成绩：'))
                        d['java'] = int(input('请输入java成绩：'))
                    except:
                        print('输入有误，请重新输入信息。')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('学生信息修改成功！！！')
            else:
                wfile.write(str(d)+'\n')
        wfile.close()
        answer = input('是否继续修改学生信息？y/n\t')
        if answer=='y' or answer=='Y':
            modify()


def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按学生ID查找请输入1，按姓名查找请输入2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('输入错误，请重新输入！！！')
                continue
                # search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)

            #显示查询结果：
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer = input('是否继续查询学生信息？y/n\t')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
        else:
            print('暂无该学生信息！！！')
            return


def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！！！')
        return

    #定义标题显示格式：
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','python成绩','java成绩','总成绩'))
    #定义内容显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^9}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('en'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('en'))+int(item.get('python'))+int(item.get('java'))
                                 ))
        print()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
        student_new=[]
        for item in students:
            d=dict(eval(item))
            student_new.append(d)
    else:
        print('暂未保存数据信息！！！')
        return
    while True:
        asc_or_desc=input('请选择（0、升序 1、降序）：')
        if asc_or_desc=='0':
            asc_or_desc_bool=False
        elif asc_or_desc=='1':
            asc_or_desc_bool=True
        else:
            print('输入错误，请重新输入！！！')
            continue
            # sort()
        mode=input('请选择排序方式（1、按英语成绩排序，2、按python排序，3、按java排序，4、按总成绩排序）：')
        if mode=='1':
            student_new.sort(key=lambda x :int(x['en']),reverse=asc_or_desc_bool)

        elif mode=='2':
            student_new.sort(key=lambda x :int(x['python']), reverse=asc_or_desc_bool)

        elif mode=='3':
            student_new.sort(key=lambda x :int(x['java']),reverse=asc_or_desc_bool)

        elif mode=='4':
            student_new.sort(key=lambda x :int(x['en'])+int(x['python'])+int(x['java']),reverse=asc_or_desc_bool)

        else:
            print('输入错误，请重新输入！！！')
            continue
            # sort()

        show_student(student_new)

        answer = input('是否继续排序？y/n\t')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def total():
    if os.path.exists(filename):   #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()    #读取全部内容
            if students:
                print(f'一共有 {<!-- -->len(students)} 名学生...\n')
                show()
                print()
            else:
                print('还没有录入学生信息！！！')
    else:
        print('暂未保存数据信息！！！')
        return

def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()    #读取全部内容
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
                print()
            else:
                print('还没有录入学生信息！！！')
    else:
        print('暂未保存数据信息！！！')
        return

if __name__ == '__main__':
    main()

```
