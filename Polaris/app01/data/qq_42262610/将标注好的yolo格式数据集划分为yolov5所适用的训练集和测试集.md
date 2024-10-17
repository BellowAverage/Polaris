
--- 
title:  将标注好的yolo格式数据集划分为yolov5所适用的训练集和测试集 
tags: []
categories: [] 

---
有两个文件夹images和labels，分别存放着图片和标注好的yolo格式检测数据标签，如何划分为train和val两个文件夹，且train和val两个文件夹下分别有划分好比例的images和labels文件夹，其中images和labels文件夹下分别存放相对应的图片和标签呢？

脚本一：（生成划分好的train.txt和val.txt）

```
import os
import random
random.seed(1)

trainval_percent = 1 
train_percent = 0.9

jsonfilepath = 'F:\衣服检测数据集\\labels\\'
txtsavepath = 'F:\衣服检测数据集\\'

total_json = os.listdir(jsonfilepath)
num = len(total_json)
list = range(num)  # range(0,num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

if not os.path.exists('F:\衣服检测数据集\\txt'):
    os.mkdir('F:\衣服检测数据集\\txt')

ftrainval = open('F:\衣服检测数据集\\txt\\trainval.txt', 'w')
ftrain = open('F:\衣服检测数据集\\txt\\train.txt', 'w')
fval = open('F:\衣服检测数据集\\txt\\val.txt', 'w')

for i in list:
    print(i+1)
    name = total_json[i].split('.')[0] + '\n'
    if i in trainval:
       ftrainval.write(name)
        if i in train:
           ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
print('Create_txt Done, txt file in {} browser'.format('F:\衣服检测数据集\\txt'))
```

脚本二：（生成划分好的traint和val文件夹，且包含有划分好比例的images和labels文件夹）

```
import shutil
import os
import os.path as osp

num_dict = {}
sets = ['train',  'val']
for image_set in sets:
    # 创建图像分类文件夹
    image_set_browser = 'F:\\衣服检测数据集\\images_cls\\' + image_set  # 字符串拼接
    if os.path.exists(image_set_browser):
        shutil.rmtree(image_set_browser)  #递归删除user\tester 目录的内容
        print('Deleted previous {} file and created a new one'.format(image_set_browser))
    os.makedirs(image_set_browser)

# 创建标注分类文件夹
    json_set_browser = 'F:\\衣服检测数据集\\labels_cls\\' + image_set
    if os.path.exists(json_set_browser):
        shutil.rmtree(json_set_browser)
        print('Deleted previous {} file and created a new one'.format(json_set_browser))
    os.makedirs(json_set_browser)
    image_ids = open('F:\\衣服检测数据集\\txt\\{}.txt'.format(image_set)).read().strip().split()
    print(image_set)
    for i, image_id in enumerate(image_ids):
        print(i+1, image_id)
        img = 'F:\\衣服检测数据集\\images\\{}.jpg'.format(image_id)
        json = 'F:\\衣服检测数据集\\labels\\{}.txt'.format(image_id)
        shutil.copy(img, image_set_browser)
        shutil.copy(json, json_set_browser)
    print('img set: {} num: {}'.format(image_set, len(os.listdir(image_set_browser))))
    print('json set: {} num: {} \n'.format(image_set, len(os.listdir(json_set_browser))))
    num_dict[image_set] = len(os.listdir(json_set_browser))  # 创建字典
print("image and json files classify Done")
for key, value in num_dict.items():          # 利用字典，进行显示
    print('{} num: {}'.format(key, value))

```


