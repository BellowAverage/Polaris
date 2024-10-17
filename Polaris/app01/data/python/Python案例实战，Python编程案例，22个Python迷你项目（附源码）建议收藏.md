
--- 
title:  Python案例实战，Python编程案例，22个Python迷你项目（附源码）建议收藏 
tags: []
categories: [] 

---
### 前言

22个通过Python构建的项目，以此来学习Python编程。

### ① 骰子模拟器

目的：创建一个程序来模拟掷骰子。

提示：当用户询问时，使用random模块生成一个1到6之间的数字。

```
import random;
while int(input( 'Press 1 to roll the dice or 0 to exit:\n')): print(random.randint(1,6))
--------------------------------------------------------------------
Press 1 to roll the dice or e to exit

```

### ② 石头剪刀布游戏

目标：创建一个命令行游戏，游戏者可以在石头、剪刀和布之间进行选择，与计算机PK。如果游戏者赢了，得分就会添加，直到结束游戏时，最终的分数会展示给游戏者。

提示：接收游戏者的选择，并且与计算机的选择进行比较。计算机的选择是从选择列表中随机选取的。如果游戏者获胜，则增加1分。

```
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    # 判断游戏者和电脑的选择
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='E':
        print("Final Scores:")
        print(f"CPU:{
     <!-- -->cpu_score}")
        print(f"Plaer:{
     <!-- -->player_score}")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    computer = random.choice(choices)

```

### ③ 随机密码生成器

目标：创建一个程序，可指定密码长度，生成一串随机密码。

提示：创建一个数字+大写字母+小写字母+特殊字符的字符串。根据设定的密码长度随机生成一串密码。

```
import random
passlen = int(input( "enter the length of password" ))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLNNOPQRSTUVWXYZ!@#$%^&amp;*()?
p= "".join(random.sample(s,passlen ))
print (p)
----------------------------------------------aw--enter the length of password
za1gBo

```

### ④ 句子生成器

目的：通过用户提供的输入，来生成随机且唯一的句子。

提示：以用户输入的名词、代词、形容词等作为输入，然后将所有数据添加到句子中，并将其组合返回。

```
color = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: )celebrity = input(“Enter a celebrity: ")print("Rases are", color)
print(pluralNoun i - are blue-)
print(I love-, celebrity）
-------------------------------------
Red
Teeth
RDJ
Roses are red. teeth are blue.I Love RDJ

```

### ⑤ 猜数字游戏

目的：在这个游戏中，任务是创建一个脚本，能够在一个范围内生成一个随机数。如果用户在三次机会中猜对了数字，那么用户赢得游戏，否则用户输。

提示：生成一个随机数，然后使用循环给用户三次猜测机会，根据用户的猜测打印最终的结果。

```
import random
nu nber = randomn.randint(1,10)for i in range(0,3):
user = int(input("guess the nunber"))if user number:
print("Hurray !")
print(f"you guessed the number right it's {nunber ")break
elif user&gt;number:
print("Your guess is too high" )clif user&lt;number :
print("Your guess is toa low.")
else:
print( f"Nice Try!, but the nunber is {
     <!-- -->number}")

```

### ⑥ 故事生成器

目的：每次用户运行程序时，都会生成一个随机的故事。

提示：random模块可以用来选择故事的随机部分，内容来自每个列表里。

```
import random
when = [ 'A few years ago'，"Yesterday','Last night', 'A long time ago' , ' n 2eth Jan']who = [ 'a rabbit', 'an elephant ', 'a mouse", "a turtie' , 'a cat']
namne =[ 'Ali',_"Miriam " , 'daniel ,"Hoouk ' , 'starwalker"j

```
