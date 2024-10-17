
--- 
title:  Python 读写 Excel 常用的几种方法 
tags: []
categories: [] 

---
### xlwt、xlrd 

```
import xlwt
import xlrd

# 存入的数据为二维列表形式
my_list = [
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
]


def excel_save(excel_name, my_list):
    info_result = []
    title = ["第一列", "第二列", "第三列"]
    info_result.append(title)
    info_result.extend(my_list)
    workbook = xlwt.Workbook(encoding='utf_8_sig')
    worksheet = workbook.add_sheet(excel_name, cell_overwrite_ok=True)
    # red_style = xlwt.easyxf("font:colour_index red;")
    for i, row in enumerate(info_result):
        for j, col in enumerate(row):
            worksheet.write(i, j, col)
            # worksheet.write(i, j, col, red_style)
    # for row in range(len(info_result)):
    #     for column in range(len(info_result[row])):
    #         worksheet.write(row, column, info_result[row][column])
    workbook.save(excel_name)


def excel_read(excel_name):
    workbook = xlrd.open_workbook(excel_name)
    worksheet = workbook.sheet_by_index(0)
    nrows = worksheet.nrows
    for nr in range(nrows):
        print(worksheet.row_values(nr))
    # ['第一列', '第二列', '第三列']
    # [1.0, 2.0, 3.0]
    # [2.0, 3.0, 4.0]
    # [4.0, 5.0, 6.0]


excel_save('test.xls', my_list)
excel_read('test.xls')

```

### csv.writer、csv.reader 

```
import csv

title = ["第一列", "第二列", "第三列"]
my_list = [
    title,
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
]

with open('test.csv', 'w', newline='', encoding='utf-8') as f:
# with open('test.csv', 'a+', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=' ')
    for row in my_list:
        writer.writerow(row)
# 第一列   第二列	第三列
# 1	       2	    3
# 2	       3	    4
# 4	       5	    6

with open('test.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['第一列', '第二列', '第三列']
# ['1', '2', '3']
# ['2', '3', '4']
# ['4', '5', '6']


```

### csv.DictWriter、csv.DictReader

我比较推荐下面这种 csv 读写方式，可以直接写一行数据，列的顺序由 filenames 决定（就算重新修改列顺序也很方便），这样就不用像其他写法那样刻意去关注 row 中元素的顺序了。 

```
import csv

data = [
    {'age': 18, 'city': 'BeiJing'},
    {'age': 30, 'city': 'ShangHai'},
    {'age': 25, 'city': 'GuangZhou'},
    {'age': 40, 'city': 'ShenZhen'},
]

with open('test.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['age', 'city']        # fieldnames 的顺序决定了 csv 列的顺序
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
# age	city
# 18	BeiJing
# 30	ShangHai
# 25	GuangZhou
# 40	ShenZhen

with open('test.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# OrderedDict([('age', '18'), ('city', 'BeiJing')])
# OrderedDict([('age', '30'), ('city', 'ShangHai')])
# OrderedDict([('age', '25'), ('city', 'GuangZhou')])
# OrderedDict([('age', '40'), ('city', 'ShenZhen')])
```

### pandas.to_excel、pandas.read_excel

```
import pandas as pd

data = {
    "age": [18, 30, 25, 40],
    "city": ["BeiJing", "ShangHai", "GuangZhou", "ShenZhen"]
}
index = pd.Index(data=["Tom", "Bob", "Mary", "James"], name="name")
user_info = pd.DataFrame(data=data, index=index)

user_info.to_excel('test.xls')
# name	age	city
# Tom	18	BeiJing
# Bob	30	ShangHai
# Mary	25	GuangZhou
# James	40	ShenZhen
print(pd.read_excel('test.xls'))
#     name  age       city
# 0    Tom   18    BeiJing
# 1    Bob   30   ShangHai
# 2   Mary   25  GuangZhou
# 3  James   40   ShenZhen


# 设定 index=False 以后，索引就不会再写到 excel 里边了。
user_info.to_excel('test.xls', index=False)
# age	city
# 18	BeiJing
# 30	ShangHai
# 25	GuangZhou
# 40	ShenZhen
print(pd.read_excel('test.xls'))
#    age       city
# 0   18    BeiJing
# 1   30   ShangHai
# 2   25  GuangZhou

```


