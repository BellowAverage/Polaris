
--- 
title:  用 Python 库 PySimpleGUI 制作办公自动化小软件 
tags: []
categories: [] 

---
<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcTIyWFdpY3diaDlXTGtsazJYNTF6dkdEWTN4UmtpY0NzT2huSlQ5V2xDejFvbnZ2c2RXd0JRb0IwaWNaZkNRaDl5SVJvaWM0MUlYd05XRVEvNjQw?x-oss-process=image/format,png">

作者：Be_melting

https://blog.csdn.net/lys_828/article/details/111238568

## Python 在运维和办公自动化中扮演着重要的角色，PySimpleGUI 是一款很棒的自动化辅助模块，让你更轻松的实现日常任务的自动化。

## **1 PySimpleGUI安装**

在命令行/终端输入：`pip install pysimplegui`，等待安装完成后，进入python环境，输入`import PySimpleGUI`回车无误后，确认安装成功<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjU2cm52WTZMekFRdnRkMG10ZW9qR2VKMlVreWF5NVpvYzdUdkVVWUFwdnBJbUtsNDcwUWRZVlEvNjQw?x-oss-process=image/format,png">2 PySimpleGUI制作简易弹窗界面

### 2.1 两种界面设计模式

（1） 单次显示界面（one-shot window）
- 类似于弹窗，出现一次- 常用于提示信息，收集信息
（2）持续显示界面（Persistent window）
- 持续不断显示，除非用户手动关闭- 常作为软件的主界面
### 2.2 制作弹窗

官网默认的库的缩写为sg，使用时建议保持统一，也是使用sg<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVGSFlZd3NWT3NXZnFYYUg4Y2pzN0lER2ljeWxpYk5vOXdidXRnZWNkUEM0NDVKamljTjVpYm9QWHNnLzY0MA?x-oss-process=image/format,png">弹窗类型：(第一种和第二种是一致的)
- `sg.popup('注意！')`- `sg.popup_ok('默认弹窗')`- `sg.popup_yes_no('带Yes和No按钮的弹窗')`- `sg.popup_cancel('带cancel按钮的弹窗')`- `sg.popup_ok_cancel('带OK和cancel按钮的弹窗')`- `sg.popup_error('带红色error按钮的弹窗')`- `sg.popup_auto_close('几秒后自动关闭的弹窗')`
最后一个执行后程序会在2s左右自动退出，除了以上的简单的默认函数外，还可以手动设置参数，相关的参数如下<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjUwQktMOVJKN2ljaG40TFhtZUJtVVZpYzRabkxublYzdGtabzdBczJJZktZczMzSWtyeWNHZ3lLQS82NDA?x-oss-process=image/format,png">比如设置一个定制化的小窗口，进行相关参数的添加

```
sg.popup(
  '这是弹窗',
  title='Hello',
  button_color=('#A81B0C', '#FFFFFF'),
  background_color='#F47264',
  line_width=2,
  custom_text=' 好的 '
)

```

输出结果：（第一个参数就是要显示的信息，可以是单个，也可多个字符串，多个字符串时候，默认换行，如果是单个字符串可以通过line_with指定每行的宽度）<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVMMEVTQnN6WWJpYlVVVE5JcFBVYkthWmJQQTBkWXVpYlU5bVdzV2liY1FPM3VsaWF4UHBQdFl3d1dnLzY0MA?x-oss-process=image/format,png">当第一个参数是多个字符串时，自动换行显示（由于自动的窗体长宽很小，所以标题就没有看到，但不是代表不显示，下面的示例中就可以看到）<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVnY3ZyaWNhc0VrMlRtRU1UWlhxVW45N3R2NGhucTB1Tm1OcGJhNlRVZWlhN21BSnNKYUc3RkRXUS82NDA?x-oss-process=image/format,png">**2.3 文字内容弹窗**

采用`popup_scrolled()`方法，括号中添加要显示的内容即可

```
text = '''大家好，
我们一起来学习PySimpleGUI制作简单的图形用户界面。'''
sg.popup_scrolled(text,title='Hello')

```

输出结果为：（这里的标题就正常的显示出来了）<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVpYzdiUEVmZnBsYVFKYXZxQ1MwaWJUbm9JYTdhS0lvNnJBcjNtaWF2M2dJVzF3NHBkZ3hyUkZUblEvNjQw?x-oss-process=image/format,png">这个文字内容弹窗里面也有相关的设置参数，可以根据自己的需要进行设置，参数如下：（注意之前的弹窗的参数也可以在这类弹窗中使用，比如刚刚用的title）<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVBM3lUb0V5blpjUFdsaFlqNG5taWI4cEtpYmlhaWEyVnRTdmU0WGZZVFRjUU9YYnZqM0E0SFdBVnVnLzY0MA?x-oss-process=image/format,png">**2.4 获取用户输入的弹窗**

采用`popup_get_text()`方法，括号内容有点类似`input()`语句中的提示语，提醒用户输入

```
text1 = sg.popup_get_text('请输入文字1')
print(text1)
text2 = sg.popup_get_text('请输入文字2')
print(text2)

```

输出结果为：（当点击Ok时候控制台输出端就会获取到用户输入的文字，如果是点击Cancel，输出端为None，这里执行了两次用户输入弹出的指令，当第一次输入后点击Ok会自动弹出第二个窗口）<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVFU0xoaWNEQXR3T25mbUNHNW9DZTNRY1ROaWNSZUZ5NWVQWTFjMVF1Z1YycVZIcnNYZUpvbUx0US82NDA?x-oss-process=image/format,png">该类弹窗也有自己特定的参数供选择，比如既然进行输入的操作，有时输入密码时候就不希望别人看到，就可以采用输入的显示方式，如下<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVHVk92WklOS3VmR3B3YzRKUkphMnZNVkZmTFpaWTZpY09DOWtmUGlidUlxbGVhRVJNQUEycEh1US82NDA?x-oss-process=image/format,png">测试进行密码隐藏输入，可以直接顺势将用户输入的密码也以弹窗的形式<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVKcjJsalJGSm5GYkVEcDlqWWlhMW43d2pWd2dlY3U2M1VxM0VIMWtKOVBTNWljSXBsc1RraWJBdGcvNjQw?x-oss-process=image/format,png">

### **2.5 文件选择弹出窗口**

直接采用`sg.popup_get_file()`方法，括号里面的内容也是输入的提示语<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVoSno1dmliUlFRbElBaWFkVFpWN0lEQk92TVdyV2Rsc1lEaWFSYTZkcmlhWkQwQlZGWkxuYlFBaWNxdy82NDA?x-oss-process=image/format,png">选择后就会把详细的地址直接显示在输入框中，如下<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjV5aWJ0blh4ZHZpYjk2VW1oVjlTTmlid0x4aWNET0NzaWJQaWFpYmpKSFgwcGtPUko3aWFKSU8xSHN5QUN1dy82NDA?x-oss-process=image/format,png">那么同样该类弹出也有自己的特有属性参数设置，具体如下。里面的每个参数几乎都是超级常用的参数，可以自行测试一下。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVwOXpwSTZkQ2dORUlwdlY1dzVxS3h3dWYwbEFCWlh4V3VpYXFxNHdFc0J1OFhxbVpxSU5reTl3LzY0MA?x-oss-process=image/format,png">默认后缀，这个参数也是常用的，比如在sublime中点击另存为时候，本身是py文件，在给文件命名的时候只需要输出文件名，后缀自动给添加上去了。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVCa0hUSTBVTUhxeGxIOFprQWljRVEyUFJFdE5RVU02anh4bWhzRTlGM2szYllXTzZkcmw4QWZnLzY0MA?x-oss-process=image/format,png">**2.6 文件夹选择窗口**

采用`sg.popup_get_folder()`方法，括号里面的内容也是输入的提示语。执行程序后会弹出选择文件的窗口，鼠标选择后就会把文件夹的路径添加到输入<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVuTmRRRDlnbkRMZGtLR1A5c0dYMzBpY2ZHZWljR3RPSEJHOGliZU1aclduTUY1cWgzSUFtSUlhWUEvNjQw?x-oss-process=image/format,png">

### **2.7 进度条弹窗**

采用`sg.one_line_progress_meter()`方法，括号中输入相关的参数设置内容

```
for i in range(1000):
  sg.one_line_progress_meter(
    '进度条',
    i + 1,
    1000,
    '该进度条key',
    '这是一个进度条'
  )

```

输出结果为：（会进行动态加载，直到达到100%）<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjUwaWJORWhiaENwZ21XaEpNVW1CWVF1QXdDclBqRVg3VjlpYWx6N1JqZGNOSmxyN2NiUWNweXJWZy82NDA?x-oss-process=image/format,png">当然此类弹窗也有自己特有的参数设置，如下。比如常见的设置竖直的还横向的，滚动条的上下限等。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjUwZGtrZmt2b0loNU1pYlU1d0ZTcDF5cjV3Tk9VVFFHOXlUMXU3cWQwWVRXQmxBenlHRGlheVlvZy82NDA?x-oss-process=image/format,png">比如尝试一下不同参数的组合输出

```
for i in range(1, 1000):
  sg.one_line_progress_meter(
    '进度条',
    i + 1,
    1000,
    '该进度条key',
    '这是一个进度条',
    orientation='h',
    bar_color=('#F47264', '#FFFFFF')
  )

```

输出结果为：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjUzNmw1OGFuWng0bmpld01DWEx6aWJlejcxamliZHc1UUpoa1R3Q0ZRaWJJN2ZBSzFSeGJ2aGQ4QkEvNjQw?x-oss-process=image/format,png">**3 制作简易压缩软件**

### **3.1 功能需求**
- 软件运行后弹出窗口让用户选择一个文件夹- 用户选择后再弹出窗口让用户选择压缩包保存的位置和名称- 用户输入完成后将该文件夹内所有的文件进行压缩打包- 完成压缩后再弹出一个窗口告诉用户这个压缩包的体积大小
### **3.2 功能拆解**

（1）软件运行后弹出窗口让用户选择一个文件夹
- `popup_get_folder()`
（2）用户选择后再弹出窗口让用户选择压缩包保存的位置和名称
- `popup_get_file()`- `save_as=True`- `default_extension = 'zip'`
（3）用户输入完成后将该文件夹内所有的文件进行压缩打包
- `zipfile`模块
（4）完成压缩后再弹出一个窗口告诉用户这个压缩包的体积大小
- `os.stat()`读取文件信息- `popup()`弹窗显示数据
### 3.3 全部代码

参考代码：（主要是细节部分，对于压缩路径的设置，需要进行处理一下，不然最后解压缩的会出现很多层级的不必要文件夹）

```
import PySimpleGUI as sg
import zipfile
import os




folder = sg.popup_get_folder('请选择要压缩的文件夹')
zip_path = sg.popup_get_file(
  '请选择要保存的压缩包位置',
  save_as=True,
  default_extension='zip',
  file_types=(('压缩包', '.zip'), )
)


with zipfile.ZipFile(zip_path, 'w') as zipobj:
  for file in os.scandir(folder):
    zipobj.write(file.path, file.path.replace(folder, '.'))


zip_size = os.stat(zip_path).st_size // 1024
sg.popup(f'压缩包体积大小为：{zip_size} KB')

```

输出结果演示如下：（完美，撒花✿✿ヽ(°▽°)ノ✿<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9maHVqem9RZTdUcDl1Q3BZamljRHlTNkxHaG1obElmWjVVN0Z2ZTYyUTRGWXF4ajdlTVNtQU9ReU1wRjNYcHozUkdpYUlHSDg3SXZDbHhwQ1hqNEp3Snh3LzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

微信扫码关注，了解更多内容
