
--- 
title:  建议收藏，5个Python迷你项目(附源码) 
tags: []
categories: [] 

---
在使用Python的过程中，我最喜欢的就是Python的各种第三方库，能够完成很多操作。

 下面就给大家介绍5个通过Python构建的项目，以此来学习Python编程。

### **一、石头剪刀布游戏**

目标：创建一个命令行游戏，游戏者可以在石头、剪刀和布之间进行选择，与计算机PK。如果游戏者赢了，得分就会添加，直到结束游戏时，最终的分数会展示给游戏者。

提示：接收游戏者的选择，并且与计算机的选择进行比较。计算机的选择是从选择列表中随机选取的。如果游戏者获胜，则增加1分。

```
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    # 判断游戏者和电脑的选择
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='E':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    computer = random.choice(choices)
```

### **二、随机密码生成器**

目标：创建一个程序，可指定密码长度，生成一串随机密码。

提示：创建一个数字+大写字母+小写字母+特殊字符的字符串。根据设定的密码长度随机生成一串密码。

```
import random
passlen = int(input("enter the length of password" ))
s=" abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKL MNOPQRSTUVIXYZ!aN$x*6*( )?"
p = ".join(random.sample(s,passlen ))
print(p)
----------------------------
enter the length of password
6
Za1gB0
```

### **三、骰子模拟器**

目的：创建一个程序来模拟掷骰子。

提示：当用户询问时，使用random模块生成一个1到6之间的数字。

```
import random;
while int(input('Press 1 to roll the dice or 0 to exit:\n')): print( random. randint(1,6))
--------------------------------------------------------------------
Press 1 to roll the dice or 0 to exit
1
4
```

### **四、自动发送邮件**

目的：编写一个Python脚本，可以使用这个脚本发送电子邮件。

提示：email库可用于发送电子邮件。

```
import smtplib 
from email.message import EmailMessage
email = EmailMessage() ## Creating a object for EmailMessage
email['from'] = 'xyz name'   ## Person who is sending
email['to'] = 'xyz id'       ## Whom we are sending
email['subject'] = 'xyz subject'  ## Subject of email
email.set_content("Xyz content of email") ## content of email
with smtlib.SMTP(host='smtp.gmail.com',port=587)as smtp:     
## sending request to server 
    smtp.ehlo()          ## server object
smtp.starttls()      ## used to send data between server and client
smtp.login("email_id","Password") ## login id and password of gmail
smtp.send_message(email)   ## Sending email
print("email send")    ## Printing success message
```

### **五、闹钟**

目的：编写一个创建闹钟的Python脚本。

提示：你可以使用date-time模块创建闹钟，以及playsound库播放声音。

```
from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3') ## download the alarm sound from link
                    break
```

<img src="https://img-blog.csdnimg.cn/img_convert/d7854883098625aae2d9b294c212ca1c.png" alt="d7854883098625aae2d9b294c212ca1c.png">
