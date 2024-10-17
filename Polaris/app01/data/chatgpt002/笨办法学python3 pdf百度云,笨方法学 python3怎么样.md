
--- 
title:  笨办法学python3 pdf百度云,笨方法学 python3怎么样 
tags: []
categories: [] 

---
大家好，小编来为大家解答以下问题，笨办法学python第五版百度云，笨办法学python3 pdf百度云，现在让我们一起来看看吧！



<img alt="" height="1068" src="https://img-blog.csdnimg.cn/img_convert/b7d8175541ca2e95142831bd1dc01094.jpeg" width="800">

这章断断续续续写了一周，今天放出来......<s>主要是翻译那些场景描述很烦人，毕竟0级英语。</s>

面向对象的分析和设计的基本流程：
1. 把要解决的问题写下来，或者画下来1. 将第一条的关键概念提取出来并加以研究1. 创建一个类层次结构和对象图1. 用代码实现各个类，并写一个测试来运行它们1. 重复上述步骤并细化代码 
    这一流程可以看成是一个“自顶向下”的，也就是从很抽象的概念入手，逐渐细化，直到概念变成具体的可用代码实现的东西。

#### 作者将用这个流程来实现一个游戏引擎和一个游戏，以作举例：

        游戏名叫《来自Percal 25号行星的哥顿人》，这是一个太空冒险游戏。起初脑海里只有这个概念，然后作者沿着这个思路，慢慢完善这个游戏。

##### 1. 先把问题写下来或者画出来

        作者为这个游戏写一段描述：“外星人入侵了宇宙飞船，我们的英雄需要通过各种房间组成的迷宫，打败遇到的外星人，这样才能通过救生船回到下面的行星去。这个游戏会跟《Zork》或者《Adventure》类似，会用文字输出各种搞笑的死法。游戏会用到一个引擎，带动一张充满房间和场景的地图。当玩家进入一个房间时，这个房间会显示出自己的描述，并且会告诉引擎下一步应该到哪个房间去。”

        接下来要描述各个场景：
- 死亡（Death）：玩家死去的场景。- 中央走廊（Central Corridor）：这是游戏的起点，哥顿人已经在那儿把守着了，玩家需要讲一个笑话才能继续。- 激光武器库（Laser Weapon Armory）：在这里英雄会找到一个中子弹，在乘坐逃生舱离开飞船时用它把飞船炸掉。这个房间有个数字键盘，英雄需要猜密码组合。- 飞船主控舱（The Bridge）：另一个战斗场景，英雄需要在这里埋炸弹。- 逃生舱（Escape Pod）：英雄逃离的场景，但需要猜对哪艘是好的。
##### 2. 提取和研究关键概念

        现在有了足够的信息来提取一些名词，并分析它们的类层次结构。首先整理一个名词列表：
- 外星人（Alien）- 玩家（Player）- 飞船（Ship）- 迷宫（Maze）- 房间（Room）- 场景（Scene）- 哥顿人（Gothon）- 逃生舱（Escape Pod）- 行星（Planet）- 地图（Map）- 引擎（Engine）- 死亡（Death）- 中央走廊（Central Corridor）- 激光武器库（Laser Weapon Armory）- 主控舱（The Bridge）
        然而并不是是所有的名词都适合作函数名的，然后需要挑选一个合适的名字做函数名。

##### 3. 为各种概念创建类层次结构和对象图

        完成上面的工作，然后通过提问问题的方式把它转化成一个类层次结构。问题可以是“和其他东西有哪些类似？”或者“哪个只不过是某个东西的另一种叫法？”

        然后就可以发现，“房间”和“场景”基本上是同一个东西，然后又发现“中央走廊”是一种场景，“死亡”又是一种场景等等。通过这种方式，理清思路后画下了一个类层次结构：
- Map- Engine- Scene-         --Death-         --Central Corridor-         --Laser Weapon Armory-         --The Bridge-         --Escape Pod
然后查看每个层次结构里的场景描述，提取其中的动词部分。例如：从描述中我知道，我需要一种方法来运行游戏引擎，在地图里转到下一个场景，获得初始场景，以及进入下一个场景。加上这些后大致是下面这样的：
- Map-         --next_scene-         --opening_scene- Engine-         --play- Scene-         --enter-         --Death-         --Central Corridor-         --Laser Weapon Armory-         --The Bridge-         --Escape Pod
        注意，我只在Scene 的下面添加了 enter 这个方法，因为我知道具体的场景会继承并覆盖这个方法。

##### 4.编写类和运行类的测试代码

        准备好了类和函数的树，我需要在编辑器里打开一个源文件，并试着编写代码。通常直接把这个树直接复制到源文件，把它扩展写成各个类就行了，这里是一个初始的简单例子，文件最后还包含一点简单的测试。

```
class Scene(object):   #场景

	def enter(self):
		pass

		
class Engine(object):   #引擎

	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass

		
class Death(Scene):   #死亡
		
	def enter(self):
		pass


class CentralCorridor(Scene):  #中央走廊

	def enter(self):
		pass

class LaserWeaponArmory(Scene):    #激光武器库

	def enter(self):
		pass
		
class TheBridge(Scene):   #主控舱
	
	def enter(self):
		pass
		
		
class EscapePod(Scene):   #逃生舱
	
	def enter(self):
		pass

class Finished(Scene):   #游戏结束
	
	def enter(self):
		pass
			
class Map(object):   #地图
	
	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
	
	def opening_scene(self):
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
```

##### 5.重复和细化

        完成上一步之后，再回头重复整个流程，基于你从后面步骤中学到的东西来细化你写的内容，在这个步骤中，你不需要把自己锁定在一个层面上去完成某个特定的任务。假如说你不知道怎样写 Engine.play 这个方法，可以停下来，就在这个任务上使用这个流程，直到弄明白为止。

##### 6.完成代码《来自Percal 25号行星的哥顿人》：

```
from sys import exit
from random import randint
from textwrap import dedent   
#为了写房间描述时使用三引号字符串，引入了dedent函数，它会把字符串开头的空白去掉，如果不用这个函数，使用三引号风格字符串就会失败，因为它们会砸屏幕上缩进，和在Python 代码中一样。


class Scene(object):   #场景

	def enter(self):
		print('This scene is not yet configured.---此场景尚未配置。')
		print('Subclass it and implement enter().---对它进行子类化并实现输入。')
		exit(1)

		
class Engine(object):   #引擎

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		#
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to print out the last scene_map
		current_scene.enter()

		
class Death(Scene):   #死亡
	
	quips = [
		"You died. You kinda suck at this.---你死了。你在这方面有点烂。",
		"You mom would be proud...if she were smarter.---你妈妈会感到骄傲的……如果她更聪明的话。",
		"Such a luser.---这样一个失败者。",
		"I have a small puppy that's better at this.---我有一只小狗，它更擅长这个。",
		"You're worse than your Dad's jokes.---你比你爸爸的笑话还烂。"
	]
	
	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])   #randint(0，x)函数，在0-x之间（包含）随机生成一个整数
		exit(1)


class CentralCorridor(Scene):  #中央走廊

	def enter(self):
		print(dedent("""
			The Gothons of planet Percal #25 haveinvaded your ship and desteoyed your entire crew.
			You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory,
			put it in the bridge, and blow the ship up afther getiing into an escape pod.
			You're running down the central corridor to the Weapons Armory when a Gothon jumps out , 
			red scaly skin, dark grimy filled body.
			He's blocking the door to the Armory and about topull a weapon blast you.
			---
			Percal25号星球上的哥顿人入侵了你的飞船，杀了你的全体船员。
			你是最后的幸存者，你最后的任务获得武器库里的中子毁灭炸弹，放在主控舱，然后把船炸成逃生舱。
			你沿着中央走廊跑去找武器军械库时，一只哥顿人跳出来，红色的鳞片皮肤，全身黑色的污垢。
			他挡住了军械库的门并用武器攻击你。
		"""))
		
		action = input('&gt; ')
		
		if action == "shoot!":
			print(dedent("""
				Quick on the draw you yank out your blaster and fire it at the Gothon. 
				His clown costume is flowing and moving around his body, which throws off you aim.
				This completely ruins his brand new costume but misses him entirely,
				which makes him fly into an insane rage and blast you repeatedly in the face untill you are dead.
				Then he eats you.
				---
				你迅速拔出你的爆破枪，向Gothon开火。
				他滑稽的服饰在他的身边流动，这使你无法瞄准。
				这完全破坏了他的全新服饰，但没有命中他，
				这使他勃然大怒，不断地朝你脸上猛烈攻击，直到你死去。
				然后他吃了你。
			"""))
			return 'death'
		
		elif action == 'dodge!':
			print(dedent("""
				Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. 
				In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. 
				You wake up shortly after only to die as the Gothon stomps on your head and eats you.
				---
				就像一个世界级的拳击手，你躲避、迂回、滑动、向右滚动，Gothon的爆破枪发射的激光在你头上闪过。
				在巧妙闪避中你的脚滑了一下，你的头撞在了金属墙上之后晕倒了。
				你醒来后不久就死了，因为Gothon踩着你的头并吃掉了你。
			"""))
			return 'death'
		
		elif action == 'tell a joke!':
			print(dedent("""
				Lucky for you they made you learn Gothon insults in the academy. 
				You tell the one Gothon joke you know:
				Lbhe zbgure vf fb sng , jura fur fvgf nebhaq gur ubhfr, jura fur fvgf nebhaq gur ubhfr. 
				The Gothon stops, tries not to laugh, then busts out laughing and can't move.
				While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door.
				---
				幸运的是，他们让你在学院里学会了Gothon侮辱性语言。
				你讲了一个你知道的Gothon笑话:
				Lbhe zbgure vf fb sng, jura fur fvgf nebhaq ubhfr, jura fur fvgf nebhaq ubhfr。
				Gothon停下来，试着不笑，然后突然大笑起来，动弹不得。
				当他在笑的时候，你跑上去朝他的头部开了一枪把他打倒，然后从武器室的门跳过去。
			"""))
			return 'laser_weapon_armory'  #激光武器库
			
		else:
			print('DOES NOT COMPUTE! --不算，重来--')
			return 'central_corridor'  #中央走廊


class LaserWeaponArmory(Scene):    #激光武器库

	def enter(self):
		print(dedent("""
			You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. 
			It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container.
			There's a keypad lock on the box and you need the code to get the bomb out. 
			If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. 
			The code is 3 digits.
			---
			你俯冲翻滚进武器库，蹲伏并扫描房间以寻找可能隐藏的更多Gothon。
			这里很安静，非常安静，你站起来跑到房间的另一边，在它的容器里找到了中子弹。
			盒子上有一个键盘锁，你需要密码才能把炸弹取出来。 如果你错了10次，锁就会永远关闭，你就得不到炸弹。 
			密码是3位数。
		"""))
		
		code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
		guess = input("[keypad]&gt; ")
		guesses = 0
		
		while guess != code and guesses &lt; 10:
			print('BZZZZEDDD!')
			guesses += 1
			guess = input("[keypad]&gt; ")
			
		if guess == code:
			print(dedent("""
				The container clicks open and the seal breaks, letting gas out. 
				You grab the neutron bomb and run as fast as you can to he bridge where you must place it in the right spot.
				---
				容器咔嗒一声打开，密封破裂，让气体排出。 
				你抓住中子弹并尽可能快地跑到主控舱，你必须将它放在正确的位置。
			"""))
			return 'the_bridge'   #主控舱
		
		else:
			print(dedent("""
				The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. 
				You decide to sit there, and you die .
				锁最后一次发出嗡嗡声，当装置融合在一起时你听到了令人作呕的融化声。 
				你决定就坐在那里，你死了。 
			"""))
			return 'death'
			

class TheBridge(Scene):   #主控舱
	
	def enter(self):
		print(dedent("""
			You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship.
			Each of them has an even uglier clown costume than the last. 
			They haven't pulled their weapons out yet, 
			as they see the active bomb under your arm and don't want to set it off.
			---
			你胳膊挟着毁灭炸弹突然出现在主控舱，让试图控制这艘船的5个哥顿人大吃一惊。
			他们每个人都有比上一个更丑的滑稽服饰。
			他们没拿出武器，因为他们看到你胳膊下的炸弹，不想让它引爆。
		"""))
		
		action = input('&gt; ')
		
		if action == 'throw the bomb':   #投掷炸弹
			print(dedent("""
				In a panic you throw the bomb at the group of Gothons and make a leap for the door. 
				Right as you drop it a Gothon shoots you right in the back killing you. 
				As you die you see another Gothon frantically try to disarm the bomb. 
				You die knowing they will probably blow up when it goes off.
				---
				你惊慌失措地把炸弹扔向哥顿人，然后向门口跳去。
				就在你扔下它的时候，一只Gothon朝你的背部开枪杀死了你。
				当你死的时候，你会看到另一只Gothon疯狂地试图拆除炸弹。
				你死的时候知道它们可能会在拆弹的时候爆炸。
			"""))
			return 'death'
		
		elif action == 'slowly place the bomb':   #慢慢放置炸弹
			print(dedent("""
				You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat .
				You inch backward to the door, open it ,and then carefully place the bomb on the floor, pointing your blaster at it. 
				You then jump back through the door, punch the close button and blast the lock so the Gothon can't get out . 
				Now that the bomb is placed you run to the escape pod to get off this tin can.
				---
				你用爆破枪指着你胳膊下的炸弹，哥顿人举起手开始冒汗。
				你慢慢的向门移动，打开门，然后小心地把炸弹放在地板上，用爆破枪指着它。
				然后你跳回门里，按下关闭按钮，破坏门锁，让Gothon跑不出去。
				既然炸弹已经放好了，你就跑到逃生舱去把这个“罐头”弄下来。
			"""))
			return 'escape_pod'   #逃生舱
		
		else:
			print('DOES NOT COMPUTE！--不算，重来--')
			return 'the_bridge'
		
		
class EscapePod(Scene):   #逃生舱
	
	def enter(self):
		print(dedtne("""
			You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. 
			It seems like hardly any Gothons are on the ship, so your run is clear of interference. 
			You get to the chamber with the escape pods ,and now need to pick one to take. 
			Some of them could be damage but you don't have time to look.
			There's 5 pods, which one do you take?
			---
			你拼命冲过飞船，试图在整个飞船爆炸前到达逃生舱。
			看来船上几乎没有哥顿人，所以你的奔跑没有干扰。
			你带着逃生舱来到了密室，现在需要选择一个逃生舱。
			其中一些可能会造成损害，但你没有时间去看。
			有5个逃生舱，你带哪一个?
		"""))
		
		good_pod = randint(1,5)
		guess = input('[pod #]&gt; ')
		
		if int(guess) != good_pod:
			print(dedent("""
				You jump into pod {guess} and hit the eject button.
				The escapes pod  out into the void of space, 
				then implodes as the hull ruptures, crushing your body into jam jelly.
				---
				进入{guess}#舱，然后点击弹出按钮。
				逃生舱飞出太空，
				然后在船体破裂时发生内爆，把你的身体压成果冻酱。
			"""))
			return 'death'
			
		else:
			print(dedent("""
				You jump into pod {guess} and hit the eject button.
				The pod easily slides out into space heading to the planet below. 
				As it flies to the planet, you look back and see your ship implode then explode like a
				bright star, taking out the Gothon ship at the same time.
				You won!
				---
				进入{guess}#舱，然后点击弹出按钮。
				逃生舱很容易的飞出太空，，飞向下面的行星。
				当它飞向地球时，你回头看，你的飞船爆炸了，然后像一颗明亮的星，同时把Gothon飞船干掉了。
				你赢了！
			"""))
			return 'finished'
			

class Finished(Scene):   #游戏结束
	
	def enter(self):
		print("You won! Good job.")
		return 'finished'
			
			
class Map(object):   #地图

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
```

##### 自顶向下和自底向上

        “自顶向上” 是从抽象的概念（顶层）开始，一直向下到具体的代码实现，另外还有一种解决编码问题的方法，那就是先从代码开始，一直向上做到抽象概念，这种方法叫“自底向上”。

        一般步骤如下：
- 取出要解决的问题中的一小块，写些代码让它差不多能工作。- 加上类和自动测试，细化代码让它更加正式。- 把关键概念抽取出来然后研究它们。- 把真正需要实现的东西描述出来。- 回去细化代码，有可能需要全部丢弃重头做起。- 在问题的另一小块里重复上述流程。
这个方法对于更加成熟的程序员来说比较好使，各有优势。



##### END！！！
