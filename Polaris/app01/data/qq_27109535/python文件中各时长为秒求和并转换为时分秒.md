
--- 
title:  python文件中各时长为秒求和并转换为时分秒 
tags: []
categories: [] 

---
文件中各时长为秒求和并转换为时分秒 <img src="https://img-blog.csdnimg.cn/7db3c655b35148f3b9965a1a867ed8a9.png" alt="在这里插入图片描述">

```
def get_time():
    n = 0
    with open("文件.txt", mode="r", encoding='utf-8') as f:
        for line in f:
            if line.startswith("#EXTINF:"):
                line = line.strip()
                line = line.strip(",")
                n += float(line.split(":")[-1])
    times =str(datetime.timedelta(seconds=n))
    print(times)


def main():
    get_time()


if __name__ == '__main__':
    main()

```
