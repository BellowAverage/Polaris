
--- 
title:  python中大批量m3u8文件合并总结 
tags: []
categories: [] 

---
### python中大批量m3u8文件合并总结

该函数合并，**适应于大批量m3u8文本合并m3u8文件** 合并m3u8文件函数实现如下

```
def merge_ts():
    name_list = []
    with open("m3u8文件.txt", mode="r", encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            name_list.append(file_name)
    print(name_list)
    # 切换工作目录 到 ./合并文件夹/
    # 1.记录当前工作目录
    now_dir = os.getcwd()
    print(now_dir)
    # 2. 切换工作目录 到 ./合并文件夹/
    os.chdir("./合并文件夹/")
    print(now_dir)
    # 分而治之
    # 一次性合并100个文件
    temp = []
    n = 1
    for i in range(len(name_list)):
        name = name_list[i]
        temp.append(name)  # [a.ts, b.ts, c.ts]
        if i != 0 and i % 100 == 0:  # 每100个合并一次
            # 合并,
            # type a.ts b.ts c.ts &gt; xxx.mp4
            # copy /b a.ts + b.ts + c.ts xxx.mp4
            names = " ".join(temp)
            # win时type  os时copy /b           type
            os.system(f"type {<!-- -->names} &gt; {<!-- -->n}.ts")
            n += 1
            temp = []  # 还原成新的待合并列表
    # 把最后没有合并的进行收尾
    names = " ".join(temp)
    os.system(f"type {<!-- -->names} &gt; {<!-- -->n}.ts")
    n += 1

    temp_2 = []
    # 把所有的n进行循环
    for i in range(1, n):
        temp_2.append(f"{<!-- -->i}.ts")

    names = " ".join(temp_2)
    os.system(f"type {<!-- -->names} &gt; 合并文件.mp4")

    # 3. 所有的操作之后. 一定要把工作目录切换回来
    os.chdir(now_dir)
def main():


    # 合并ts文件
    merge_ts()


if __name__ == '__main__':
    main()


```
