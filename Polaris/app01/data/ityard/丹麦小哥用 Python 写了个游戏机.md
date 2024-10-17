
--- 
title:  丹麦小哥用 Python 写了个游戏机 
tags: []
categories: [] 

---
>  
  开源最前线（ID：OpenSourceTop） 猿妹编译  
  https://www.reddit.com/r/Python/comments/g484d4/today_im_releasing_pyboy_v100_a_game_boy_emulator/、https://github.com/Baekalfen/PyBoy/ 
 

最近有一个叫PyBoy的开源项目火了，原因是它使用了Python 2.7重新将那些在GameBoy上的上古游戏的整个模拟器实现了出来。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9rT1ROa2ljNWdWQkhBU1F6dFl4QWcyTENhU2ljTTJDYkNITlFWVzI3RzRuSmliYUlDb01ndWliREplM0JTN2pBN1VVQUt2R3pkdW14YmNudEJDaWNLS3dEbEZnLzY0MA?x-oss-process=image/format,png">

利用现代技术重新实现上古游戏一直是一件相当有意思的事情，大家都知道，Game Boy是任天堂公司在1989年发售的第一代便携式游戏机，对于一群80/90后来说，Gameboy是他们童年里不可或缺的一部分，有的人可能忘记了，但是提起《口袋妖怪》，很多人应该就能想起来了。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X2dpZi9rT1ROa2ljNWdWQkhBU1F6dFl4QWcyTENhU2ljTTJDYkNIaEI3cGliSnJOdDExSTdKYmljb0dDTVdrbFUzTnp6QTlTcExEam5POTR0ZFA2RXI1d0V1MmpLVUEvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X2dpZi9rT1ROa2ljNWdWQkhBU1F6dFl4QWcyTENhU2ljTTJDYkNIRlhNQ3FNRE1zeVRMUWRkOXhMM0ZQTXp2TW9OZldpYVBaWkYwV1A4VUNacVlWTUUyamxrNU1oUS82NDA?x-oss-process=image/format,png">

除此之外，PyBoy支持通过API编写脚本，还添加了类型定义，使其可以使用Cython编译软件，从而获得与用C和C++编写的模拟器相媲美的性能。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9rT1ROa2ljNWdWQkhBU1F6dFl4QWcyTENhU2ljTTJDYkNITlhTTFFBWUl0dzhFYm45aWNLT3lpYjMwWlVNdm1ZNllZdXpxVXltVzc0WEltSEFNZ3ZKN3lUbXcvNjQw?x-oss-process=image/format,png">

目前，PyBoy在Github上标星**2.6K**，累计Fork有 **239**** **个（Github地址：https://github.com/Baekalfen/PyBoy/wiki/Scripts,-AI-and-Bots）

**特性**

PyBoy 被设计成通过 Python 访问，因此支持并鼓励人们做实验研究，对机器人和AI感兴趣的人都可以尝试一下。创建者正在构建特定于游戏的包装器，目前，这些包装器可让程序员与俄罗斯方块和超级玛丽进行交互，而不需要对 Game Boy 有深入的了解。

具体你可以参考该文档：https://docs.pyboy.dk。

说到这里，不得不提的是，创建这个项目的是一个丹麦小哥，早在2015年，PyBoy就已经是一个大学项目，目前，创建者还想学习和尝试更多奇特的功能，根据大学项目的研究，他们向模拟器添加了倒回功能，也就是说，你可以在任何游戏中倒回时间。

PyBoy可作为Python中的对象加载。这意味着它可以从另一个脚本初始化，并可以由该脚本控制和探测。看一下gamewrapper_tetris.py与游戏互动的原始“机器人”。

所有外部组件都可以在PyBoy文档中找到，以下是从屏幕读取数据的简短演示。该代码也可以在gamewrapper_mario.py以下位置找到：

```
import os
import sys

from pyboy import PyBoy, WindowEvent

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

# Check if the ROM is given through argv
if len(sys.argv) &gt; 1:
    filename = sys.argv[1]
else:
    print("Usage: python mario_boiler_plate.py [ROM file]")
    exit(1)

quiet = "--quiet" in sys.argv
pyboy = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
pyboy.set_emulation_speed(0)
assert pyboy.cartridge_title() == "SUPER MARIOLAN"

mario = pyboy.game_wrapper()
mario.start_game()

assert mario.score == 0
assert mario.lives_left == 2
assert mario.time_left == 400
assert mario.world == (1, 1)
assert mario.fitness == 0 # A built-in fitness score for AI development
last_fitness = 0

print(mario)

pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
for _ in range(1000):
    assert mario.fitness &gt;= last_fitness
    last_fitness = mario.fitness

    pyboy.tick()
    if mario.lives_left == 1:
        assert last_fitness == 27700
        assert mario.fitness == 17700 # Loosing a live, means 10.000 points in this fitness scoring
        print(mario)
        break
else:
    print("Mario didn't die?")
    exit(2)

mario.reset_game()
assert mario.lives_left == 2

pyboy.stop()

```

如果在加载了Super Mario Land ROM的情况下运行上述代码，则将在下面获得类似图片和终端的打印输出。请注意，Mario的形状显示为索引0、1、16和17。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9rT1ROa2ljNWdWQkhBU1F6dFl4QWcyTENhU2ljTTJDYkNIbUs5VFBLSnl6dlhtek9YeGlhOUZ6U2ZHcGpva01qeEJSY2xwYk1XaWI3QnM3dmdPaWJwbXN3SGJBLzY0MA?x-oss-process=image/format,png">

```
Super Mario Land: World 1-1
Coins: 0
lives_left: 2
Score: 0
Time left: 400
Level progress: 251
Fitness: 0
Sprites on screen:
Sprite [3]: Position: (35, 112), Shape: (8, 8), Tiles: (Tile: 0), On screen: True
Sprite [4]: Position: (43, 112), Shape: (8, 8), Tiles: (Tile: 1), On screen: True
Sprite [5]: Position: (35, 120), Shape: (8, 8), Tiles: (Tile: 16), On screen: True
Sprite [6]: Position: (43, 120), Shape: (8, 8), Tiles: (Tile: 17), On screen: True
Tiles on screen:
     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
____________________________________________________________________________________
0  | 339 339 339 339 339 339 339 339 339 339 339 339 339 339 339 339 339 339 339 339
1  | 320 320 320 320 320 320 320 320 320 320 320 320 320 320 320 320 320 320 320 320
2  | 300 300 300 300 300 300 300 300 300 300 300 300 321 322 321 322 323 300 300 300
3  | 300 300 300 300 300 300 300 300 300 300 300 324 325 326 325 326 327 300 300 300
4  | 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300
5  | 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300
6  | 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300 300
7  | 300 300 300 300 300 300 300 300 310 350 300 300 300 300 300 300 300 300 300 300
8  | 300 300 300 300 300 300 300 310 300 300 350 300 300 300 300 300 300 300 300 300
9  | 300 300 300 300 300 129 310 300 300 300 300 350 300 300 300 300 300 300 300 300
10 | 300 300 300 300 300 310 300 300 300 300 300 300 350 300 300 300 300 300 300 300
11 | 300 300 310 350 310 300 300 300 300 306 307 300 300 350 300 300 300 300 300 300
12 | 300 368 369 300 0   1   300 306 307 305 300 300 300 300 350 300 300 300 300 300
13 | 310 370 371 300 16  17  300 305 300 305 300 300 300 300 300 350 300 300 300 300
14 | 352 352 352 352 352 352 352 352 352 352 352 352 352 352 352 352 352 352 352 352
15 | 353 353 353 353 353 353 353 353 353 353 353 353 353 353 353 353 353 353 353 353
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
