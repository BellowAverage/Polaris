
--- 
title:  写入保存文件时出现错误TypeError: a bytes-like object is required, not ‘str‘ 
tags: []
categories: [] 

---
## 写入保存文件时出现错误TypeError: a bytes-like object is required, not ‘str’

### 代码分析

```
    content = []

    title_0 = html_01.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/h1')
    for title_01 in title_0:
        title = title_01.xpath('./text()')[0]
        print(title)
        chapter = []

        select = html_01.xpath('//*[@id="play_0"]/ul/li[position()&gt;6]')

        for select_01 in select:
            i_0 = select_01.xpath('./a/text()')[0]
            i_1 = select_01.xpath('./a/@href')[0]
            # print(i_0)
            # print(i_1)

            chapter.append({<!-- -->'href': i_1, 'chapter': i_0})
        content.append({<!-- -->'book': title, 'content': chapter})
    with open('daomubiji0.json', 'wb') as fp:  # 将所得的数据存储为json文件
        json.dump(content, fp=fp, ensure_ascii=False, indent=4, sort_keys=True)

```

<img src="https://img-blog.csdnimg.cn/dcc3e7a100b74e918fae2aa39df8afaf.png" alt="在这里插入图片描述">

### 解决方法：

将wb改为w 完美解决
