
--- 
title:  bvh 显示 t-pose 
tags: []
categories: [] 

---


把第一帧所有数据为0，播放就可以显示 t-pose了



```
import logging

if __name__ == '__main__':

    bvh_path=r"C:\fbx.bvh"

    file = open(bvh_path, 'r')

    lines = file.readlines()
    datas=[]
    start=0

    for line in lines:
        if line.startswith("Time:") or line.startswith("Frame Time:"):
            start = 1
        elif start==1:
            data=line.split(" ")
            if len(data)&lt;50:
                logging.error('err len(data)&lt;50',len(data))
            add_data=["0"]*(len(data)-1)

            datas.append(" ".join(add_data)+'\n')
            start=2
        datas.append(line)
    if start==0:
        logging.error('none find start')
    # bvh_path = r"C:\Users\banggeng_li\Music\model\unity\fbx_retarget\test_Dream.fbx_rtg.bvh"

    with open(bvh_path, 'w') as file:
        file.writelines(datas)





```


