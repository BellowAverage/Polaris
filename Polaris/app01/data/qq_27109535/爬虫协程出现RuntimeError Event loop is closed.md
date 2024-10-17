
--- 
title:  爬虫协程出现RuntimeError: Event loop is closed 
tags: []
categories: [] 

---
爬虫协程出现RuntimeError: Event loop is closed 解决办法一： asyncio.run(download_all_ts()) # 报错换以下 # loop = asyncio.get_event_loop() # loop.run_until_complete(download_all_ts())

解决办法二： 协程存储文件通过加入Sources Root，整个文件夹就编译为项目文件，子级就可以直接导入父级中的py文件 .<img src="https://img-blog.csdnimg.cn/4b95f393936a460eb2cc12282fa81d98.png" alt="在这里插入图片描述">
