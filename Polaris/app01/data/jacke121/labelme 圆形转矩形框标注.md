
--- 
title:  labelme 圆形转矩形框标注 
tags: []
categories: [] 

---


```
import json
import math
import os


def calculate_square_from_circle(circle_center, radius_point):
    """
    根据圆心和圆上一点计算正方形边界框的左上角和右下角坐标。
    """
    # 计算半径
    radius = math.sqrt((circle_center[0] - radius_point[0]) ** 2 + (circle_center[1] - radius_point[1]) ** 2)

    # 计算正方形边界框的左上角和右下角坐标
    left_top = (circle_center[0] - radius, circle_center[1] - radius)
    right_bottom = (circle_center[0] + radius, circle_center[1] + radius)

    return [left_top, right_bottom]


def process_json_file(file_path):
    """
    读取并处理一个JSON文件。
    """
    with open(file_path, 'r') as file:
        data = json.load(file)

    # 遍历shapes，寻找圆形标注并计算正方形边界框
    for shape in data.get("shapes", []):
        if shape.get("shape_type") == "circle":
            circle_center, radius_point = shape.get("points")
            square_points = calculate_square_from_circle(circle_center, radius_point)
            shape["points"] = square_points
            shape["shape_type"] = "rectangle"  # 更新形状类型为矩形

    # 将修改后的数据写回文件
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def process_all_json_files(folder_path):
    """
    遍历文件夹中的所有JSON文件并处理它们。
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            process_json_file(file_path)
            print(f"Processed {file_name}")


# 指定你的文件夹路径
folder_path = r'D:\GZ_草原\yuan111'
process_all_json_files(folder_path)

```


