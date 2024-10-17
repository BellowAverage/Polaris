
--- 
title:  Python 捕获全局的 KeyboardInterrupt 异常 
tags: []
categories: [] 

---
当然，像下面这种情况。

你要是把所有代码像下面那样都放到 try, except 的情况，就当我什么也没说。

```
import time


def main():
    print('before ...')
    time.sleep(10)
    print('after ...')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt ...')
    print('the end')

```

```
root@master ~/w/python3_learning# python3 test.py 
before ...
^C
KeyboardInterrupt ...
the end

```

**一般情况下，程序运行过程当中要执行的代码量会比较大，一般用户执行 Ctrl + C 程序就报错 KeyboardInterrupt 停止了。**

```
import time


def main():
    print('before ...')
    time.sleep(10)
    print('after ...')


if __name__ == '__main__':
    main()
    print('the end')

```

```
root@master ~/w/python3_learning# python3 test.py 
before ...
^CTraceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    main()
  File "test.py", line 6, in main
    time.sleep(10)
KeyboardInterrupt

```

**但是有时候，我们希望用户在 Ctrl + C 之后再继续执行一些清理操作。**

```
import sys
import time


def suppress_keyboard_interrupt_message():
    old_excepthook = sys.excepthook

    def new_hook(exctype, value, traceback):
        if exctype != KeyboardInterrupt:
            old_excepthook(exctype, value, traceback)
        else:
            print('\nKeyboardInterrupt ...')
            print('do something after Interrupt ...')
    sys.excepthook = new_hook


def main():
    print('before ...')
    time.sleep(10)
    print('after ...')


if __name__ == '__main__':
    suppress_keyboard_interrupt_message()
    main()
    print('the end')

```

```
root@master ~/w/python3_learning# python3 test.py 
before ...
^C
KeyboardInterrupt ...
do something after Interrupt ...

```

由于 suppress_keyboard_interrupt_message 函数中的 new_hook 是自定义的，所以你也不一定局限于只处理某种异常，甚至对所有异常做统一处理也是可以的。
