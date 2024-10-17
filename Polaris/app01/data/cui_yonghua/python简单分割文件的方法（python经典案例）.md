
--- 
title:  python简单分割文件的方法（python经典案例） 
tags: []
categories: [] 

---
在某些情况下，我们需要将一个大文件分割成多个小文件，或者根据长度、行数等规则将一个文件分割成多个文件。Python提供了简单的方式来实现这些操作。

### 方法1：使用seek和read方法

下面是一段示例代码，它将一个文件分割成5个小文件，每个小文件大小为10M（除了最后一个文件，大小可能小于10M）：

```
# 定义文件名和分割的大小
filename = 'large_file.dat'
file_size = 10 * 1024 * 1024  # 10MB

# 打开文件
with open(filename, 'rb') as f:
    index = 0
    while True:
        # 定位到要读取的位置
        f.seek(index * file_size)
        # 读取数据
        data = f.read(file_size)
        # 如果已经读到文件末尾，退出循环
        if not data:
            break
        # 写入分割后的文件
        with open(f'{<!-- -->filename}_{<!-- -->index}', 'wb') as f1:
            f1.write(data)
        # 更新位置
        index += 1

```

上述代码会将large_file.dat文件分割成多个文件，文件名格式为large_file.dat_0、large_file.dat_1、large_file.dat_2等等。

### 方法2：使用split方法

另一种常用的方法是使用Python的split方法来分割文件。下面是一段示例代码，它将一个文件分成10个小文件，每个文件包含10行数据：

```
# 定义文件名和分割的大小
filename = 'large_file.txt'
lines_per_file = 10

# 打开文件
with open(filename) as f:
    # 使用切片操作分割文件
    file_data = f.readlines()
    split_data = [file_data[i:i+lines_per_file] for i in range(0, len(file_data), lines_per_file)]
    # 写入分割后的文件
    for i, data in enumerate(split_data):
        with open(f'{<!-- -->filename}_{<!-- -->i}', 'w') as f1:
            f1.writelines(data)

```

上述代码将large_file.txt文件中的数据按行分割成多个文件，文件名格式为large_file.txt_0、large_file.txt_1、large_file.txt_2等等。

### 总结

以上就是两种Python在处理文件分割时的常用方法。使用这些方法可以很容易地将一个大文件分割成多个小文件，或者按照规则将一个文件分割成多个子文件。在实际应用中，我们可以根据具体需求选择合适的方法。
