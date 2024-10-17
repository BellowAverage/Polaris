
--- 
title:  Python中 run()函数和start()函数的比较和差别 
tags: []
categories: [] 

---
## Python run()函数和start()函数的比较和差别

run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。 start() 方法是启动一个子线程，线程名就是自己定义的name。 因此，如果你想启动多线程，就必须使用start()方法。
