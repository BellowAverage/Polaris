
--- 
title:  用python3快速读取30G+的txt文件 
tags: []
categories: [] 

---
#### 分块读取：

处理大文件是很容易想到的就是将大文件分割成若干小文件处理，处理完每个小文件后释放该部分内存。案例脚本如下：

```
# -*- encoding: utf-8 -*-

def read_in_chunks(file_path, chunk_size=1024*1024):
    """按块读取文本
    一个接一个地读取文件的懒惰函数（生成器）。
    默认块大小: 1M, 当然也可以设置默认块大小
    """
    file_object = open(file_path)
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


if __name__ == "__main__":
    path = './path/filename.txt'
    chunks = read_in_chunks(path)
    for num, chunk in enumerate(chunks):
        print(f'{<!-- -->num} {<!-- -->chunk}')
		
		# 处理每一个块
        single_chunk = chunk.split('\n')
        for number, single in enumerate(single_chunk):
            print(f'{<!-- -->num} {<!-- -->number} {<!-- -->single}')


```

1、上面的代码中，每次读取1M的文件，直到把数据读取完。 2、对于35G的txt文件，测试用了3分钟读取完成。8G的文件用了不到1分钟。
