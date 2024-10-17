
--- 
title:  斗地主老是输？一起用Python做个自动出牌器，欢乐豆蹭蹭涨！ 
tags: []
categories: [] 

---
### 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

https://blog.csdn.net/hhladminhhl/article/details/119304504

#### 

#### **前言**

最近在网上看到一个有意思的开源项目，快手团队开发的开源AI斗地主——DouZero。今天我们就一起来学习制作一个基于DouZero的欢乐斗地主出牌器，看看AI是如何来帮助我们斗地主，赢欢乐豆，实现财富自由的吧！

首先一起来看看AI斗地主出牌器的效果：<img src="https://img-blog.csdnimg.cn/img_convert/2c435dc9bc67bf5bd67f3b57dc0f1025.png">下面，我们开始介绍这个AI出牌器的制作过程。

#### **一、核心功能设计**

首先我们这款出牌器是基于DouZero开发的，核心是需要利用训练好的AI模型来帮住我们，给出最优出牌方案。

其次关于出牌器，先要需要确认一个AI出牌角色，代表我们玩家自己。我们只要给这个AI输入玩家手牌和三张底牌。确认好地主和农民的各个角色，告诉它三个人对应的关系，这样就可以确定队友和对手。我们还要将每一轮其他两人的出牌输入，这样出牌器就可以根据出牌数据，及时提供给我们最优出牌决策，带领我们取得胜利！

那么如何获取三者之间的关系呢？谁是地主？谁是农民？是自己一人作战还是农民合作？自己玩家的手牌是什么？三张底牌是什么？这些也都需要在开局后确认好。

拆解需求，大致可以整理出核心功能如下：

UI设计排版布局
- 显示三张底牌- 显示AI角色出牌数据区域，上家出牌数据区域，下家出牌数据区域，本局胜率区域- AI玩家手牌区域- AI出牌器开始停止
手牌和出牌数据识别
- 游戏刚开始根据屏幕位置，截图识别AI玩家手牌及三张底牌- 确认三者之间的关系，识别地主和农民角色，确认队友及对手关系- 识别每轮三位玩家依次出了什么牌，刷新显示对应区域
AI出牌方案输出
- 加载训练好的AI模型，初始化游戏环境- 每轮出牌判断，根据上家出牌数据给出最优出牌决策- 自动刷新玩家剩余手牌和本局胜率预测
#### **二、实现步骤**

##### 1. UI设计排版布局

根据上述功能，我们首先考虑进行简单的UI布局设计，这里我们使用的是pyqt5。核心设计代码如下：

```
def setupUi(self, Form):
    Form.setObjectName("Form")
    Form.resize(440, 395)
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(9)
    font.setBold(True)
    font.setItalic(False)
    font.setWeight(75)
    Form.setFont(font)
    self.WinRate = QtWidgets.QLabel(Form)
    self.WinRate.setGeometry(QtCore.QRect(240, 180, 171, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.WinRate.setFont(font)
    self.WinRate.setAlignment(QtCore.Qt.AlignCenter)
    self.WinRate.setObjectName("WinRate")
    self.InitCard = QtWidgets.QPushButton(Form)
    self.InitCard.setGeometry(QtCore.QRect(60, 330, 121, 41))
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    self.InitCard.setFont(font)
    self.InitCard.setStyleSheet("")
    self.InitCard.setObjectName("InitCard")
    self.UserHandCards = QtWidgets.QLabel(Form)
    self.UserHandCards.setGeometry(QtCore.QRect(10, 260, 421, 41))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.UserHandCards.setFont(font)
    self.UserHandCards.setAlignment(QtCore.Qt.AlignCenter)
    self.UserHandCards.setObjectName("UserHandCards")
    self.LPlayer = QtWidgets.QFrame(Form)
    self.LPlayer.setGeometry(QtCore.QRect(10, 80, 201, 61))
    self.LPlayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.LPlayer.setFrameShadow(QtWidgets.QFrame.Raised)
    self.LPlayer.setObjectName("LPlayer")
    self.LPlayedCard = QtWidgets.QLabel(self.LPlayer)
    self.LPlayedCard.setGeometry(QtCore.QRect(0, 0, 201, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.LPlayedCard.setFont(font)
    self.LPlayedCard.setAlignment(QtCore.Qt.AlignCenter)
    self.LPlayedCard.setObjectName("LPlayedCard")
    self.RPlayer = QtWidgets.QFrame(Form)
    self.RPlayer.setGeometry(QtCore.QRect(230, 80, 201, 61))
    font = QtGui.QFont()
    font.setPointSize(16)
    self.RPlayer.setFont(font)
    self.RPlayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.RPlayer.setFrameShadow(QtWidgets.QFrame.Raised)
    self.RPlayer.setObjectName("RPlayer")
    self.RPlayedCard = QtWidgets.QLabel(self.RPlayer)
    self.RPlayedCard.setGeometry(QtCore.QRect(0, 0, 201, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.RPlayedCard.setFont(font)
    self.RPlayedCard.setAlignment(QtCore.Qt.AlignCenter)
    self.RPlayedCard.setObjectName("RPlayedCard")
    self.Player = QtWidgets.QFrame(Form)
    self.Player.setGeometry(QtCore.QRect(40, 180, 171, 61))
    self.Player.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.Player.setFrameShadow(QtWidgets.QFrame.Raised)
    self.Player.setObjectName("Player")
    self.PredictedCard = QtWidgets.QLabel(self.Player)
    self.PredictedCard.setGeometry(QtCore.QRect(0, 0, 171, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.PredictedCard.setFont(font)
    self.PredictedCard.setAlignment(QtCore.Qt.AlignCenter)
    self.PredictedCard.setObjectName("PredictedCard")
    self.ThreeLandlordCards = QtWidgets.QLabel(Form)
    self.ThreeLandlordCards.setGeometry(QtCore.QRect(140, 10, 161, 41))
    font = QtGui.QFont()
    font.setPointSize(16)
    self.ThreeLandlordCards.setFont(font)
    self.ThreeLandlordCards.setAlignment(QtCore.Qt.AlignCenter)
    self.ThreeLandlordCards.setObjectName("ThreeLandlordCards")
    self.Stop = QtWidgets.QPushButton(Form)
    self.Stop.setGeometry(QtCore.QRect(260, 330, 111, 41))
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    self.Stop.setFont(font)
    self.Stop.setStyleSheet("")
    self.Stop.setObjectName("Stop")


    self.retranslateUi(Form)
    self.InitCard.clicked.connect(Form.init_cards)
    self.Stop.clicked.connect(Form.stop)
    QtCore.QMetaObject.connectSlotsByName(Form)


def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "AI欢乐斗地主--Dragon少年"))
    self.WinRate.setText(_translate("Form", "胜率：--%"))
    self.InitCard.setText(_translate("Form", "开始"))
    self.UserHandCards.setText(_translate("Form", "手牌"))
    self.LPlayedCard.setText(_translate("Form", "上家出牌区域"))
    self.RPlayedCard.setText(_translate("Form", "下家出牌区域"))
    self.PredictedCard.setText(_translate("Form", "AI出牌区域"))
    self.ThreeLandlordCards.setText(_translate("Form", "三张底牌"))
    self.Stop.setText(_translate("Form", "停止"))

```

实现效果如下：<img src="https://img-blog.csdnimg.cn/img_convert/f09596d1d6aea2480f69f5a24fb43e89.png">

##### 2. 手牌和出牌数据识别

下面我们需要所有扑克牌的模板图片与游戏屏幕特定区域的截图进行对比，这样才能获取AI玩家手牌、底牌、每一轮出牌、三者关系（地主、地主上家、地主下家）。

识别AI玩家手牌及三张底牌：

我们可以截取游戏屏幕，根据固定位置来识别当前AI玩家的手牌和三张底牌。核心代码如下：

```
# 牌检测结果滤波
def cards_filter(self, location, distance):  
    if len(location) == 0:
        return 0
    locList = [location[0][0]]
    count = 1
    for e in location:
        flag = 1  # “是新的”标志
        for have in locList:
            if abs(e[0] - have) &lt;= distance:
                flag = 0
                break
        if flag:
            count += 1
            locList.append(e[0])
    return count


# 获取玩家AI手牌
def find_my_cards(self, pos):
    user_hand_cards_real = ""
    img = pyautogui.screenshot(region=pos)
    for card in AllCards:
        result = pyautogui.locateAll(needleImage='pics/m' + card + '.png', haystackImage=img, confidence=self.MyConfidence)
        user_hand_cards_real += card[1] * self.cards_filter(list(result), self.MyFilter)
    return user_hand_cards_real


# 获取地主三张底牌
def find_three_landlord_cards(self, pos):
    three_landlord_cards_real = ""
    img = pyautogui.screenshot(region=pos)
    img = img.resize((349, 168))
    for card in AllCards:
        result = pyautogui.locateAll(needleImage='pics/o' + card + '.png', haystackImage=img,
                                     confidence=self.ThreeLandlordCardsConfidence)
        three_landlord_cards_real += card[1] * self.cards_filter(list(result), self.OtherFilter)
    return three_landlord_cards_real

```

效果如下所示：<img src="https://img-blog.csdnimg.cn/img_convert/57feb0ab11d888d55409649d85c6e9e5.png">

地主、地主上家、地主下家：

同理我们可以根据游戏屏幕截图，识别地主的图标，确认地主角色。核心代码如下：

```
# 查找地主角色
def find_landlord(self, landlord_flag_pos):
    for pos in landlord_flag_pos:
        result = pyautogui.locateOnScreen('pics/landlord_words.png', region=pos, confidence=self.LandlordFlagConfidence)
        if result is not None:
            return landlord_flag_pos.index(pos)
    return None

```

<img src="https://img-blog.csdnimg.cn/img_convert/7ef43f29feb3ca0db27b4840c3340214.png">这样我们就可以得到玩家AI手牌，其他玩家手牌（预测），地主三张底牌，三者角色关系，出牌顺序。核心代码如下：

```
# 坐标
self.MyHandCardsPos = (414, 804, 1041, 59)  # AI玩家截图区域
self.LPlayedCardsPos = (530, 470, 380, 160)  # 左侧玩家截图区域
self.RPlayedCardsPos = (1010, 470, 380, 160)  # 右侧玩家截图区域
self.LandlordFlagPos = [(1320, 300, 110, 140), (320, 720, 110, 140), (500, 300, 110, 140)]  # 地主标志截图区域(右-我-左)
self.ThreeLandlordCardsPos = (817, 36, 287, 136)      # 地主底牌截图区域，resize成349x168


def init_cards(self):
    # 玩家手牌
    self.user_hand_cards_real = ""
    self.user_hand_cards_env = []
    # 其他玩家出牌
    self.other_played_cards_real = ""
    self.other_played_cards_env = []
    # 其他玩家手牌（整副牌减去玩家手牌，后续再减掉历史出牌）
    self.other_hand_cards = []
    # 三张底牌
    self.three_landlord_cards_real = ""
    self.three_landlord_cards_env = []
    # 玩家角色代码：0-地主上家, 1-地主, 2-地主下家
    self.user_position_code = None
    self.user_position = ""
    # 开局时三个玩家的手牌
    self.card_play_data_list = {}
    # 出牌顺序：0-玩家出牌, 1-玩家下家出牌, 2-玩家上家出牌
    self.play_order = 0
    self.env = None
    # 识别玩家手牌
    self.user_hand_cards_real = self.find_my_cards(self.MyHandCardsPos)
    self.UserHandCards.setText(self.user_hand_cards_real)
    self.user_hand_cards_env = [RealCard2EnvCard[c] for c in list(self.user_hand_cards_real)]
    # 识别三张底牌
    self.three_landlord_cards_real = self.find_three_landlord_cards(self.ThreeLandlordCardsPos)
    self.ThreeLandlordCards.setText("底牌：" + self.three_landlord_cards_real)
    self.three_landlord_cards_env = [RealCard2EnvCard[c] for c in list(self.three_landlord_cards_real)]
    # 识别玩家的角色
    self.user_position_code = self.find_landlord(self.LandlordFlagPos)
    if self.user_position_code is None:
        items = ("地主上家", "地主", "地主下家")
        item, okPressed = QInputDialog.getItem(self, "选择角色", "未识别到地主，请手动选择角色:", items, 0, False)
        if okPressed and item:
            self.user_position_code = items.index(item)
        else:
            return
    self.user_position = ['landlord_up', 'landlord', 'landlord_down'][self.user_position_code]
    for player in self.Players:
        player.setStyleSheet('background-color: rgba(255, 0, 0, 0);')
    self.Players[self.user_position_code].setStyleSheet('background-color: rgba(255, 0, 0, 0.1);')


    # 整副牌减去玩家手上的牌，就是其他人的手牌,再分配给另外两个角色（如何分配对AI判断没有影响）
    for i in set(AllEnvCard):
        self.other_hand_cards.extend([i] * (AllEnvCard.count(i) - self.user_hand_cards_env.count(i)))
    self.card_play_data_list.update({
        'three_landlord_cards': self.three_landlord_cards_env,
        ['landlord_up', 'landlord', 'landlord_down'][(self.user_position_code + 0) % 3]:
            self.user_hand_cards_env,
        ['landlord_up', 'landlord', 'landlord_down'][(self.user_position_code + 1) % 3]:
            self.other_hand_cards[0:17] if (self.user_position_code + 1) % 3 != 1 else self.other_hand_cards[17:],
        ['landlord_up', 'landlord', 'landlord_down'][(self.user_position_code + 2) % 3]:
            self.other_hand_cards[0:17] if (self.user_position_code + 1) % 3 == 1 else self.other_hand_cards[17:]
    })
    print(self.card_play_data_list)
    # 生成手牌结束，校验手牌数量
    if len(self.card_play_data_list["three_landlord_cards"]) != 3:
        QMessageBox.critical(self, "底牌识别出错", "底牌必须是3张！", QMessageBox.Yes, QMessageBox.Yes)
        self.init_display()
        return
    if len(self.card_play_data_list["landlord_up"]) != 17 or \
        len(self.card_play_data_list["landlord_down"]) != 17 or \
        len(self.card_play_data_list["landlord"]) != 20:
        QMessageBox.critical(self, "手牌识别出错", "初始手牌数目有误", QMessageBox.Yes, QMessageBox.Yes)
        self.init_display()
        return
    # 得到出牌顺序
    self.play_order = 0 if self.user_position == "landlord" else 1 if self.user_position == "landlord_up" else 2

```

效果如下：<img src="https://img-blog.csdnimg.cn/img_convert/43ca239217ef8f4d668ec5abbc38516a.png">

##### 3. AI出牌方案输出

下面我们就需要用到DouZero开源的AI斗地主了。DouZero项目地址：https://github.com/kwai/DouZero。我们需要将该开源项目下载并导入项目中。

创建一个AI玩家角色，初始化游戏环境，加载模型，进行每轮的出牌判断，控制一局游戏流程的进行和结束。核心代码如下：

```
# 创建一个代表玩家的AI
ai_players = [0, 0]
ai_players[0] = self.user_position
ai_players[1] = DeepAgent(self.user_position, self.card_play_model_path_dict[self.user_position])
# 初始化游戏环境
self.env = GameEnv(ai_players)
# 游戏开始
self.start()


def start(self):
    self.env.card_play_init(self.card_play_data_list)
    print("开始出牌\n")
    while not self.env.game_over:
        # 玩家出牌时就通过智能体获取action，否则通过识别获取其他玩家出牌
        if self.play_order == 0:
            self.PredictedCard.setText("...")
            action_message = self.env.step(self.user_position)
            # 更新界面
            self.UserHandCards.setText("手牌：" + str(''.join(
                [EnvCard2RealCard[c] for c in self.env.info_sets[self.user_position].player_hand_cards]))[::-1])


            self.PredictedCard.setText(action_message["action"] if action_message["action"] else "不出")
            self.WinRate.setText("胜率：" + action_message["win_rate"])
            print("\n手牌：", str(''.join(
                    [EnvCard2RealCard[c] for c in self.env.info_sets[self.user_position].player_hand_cards])))
            print("出牌：", action_message["action"] if action_message["action"] else "不出", "， 胜率：",
                  action_message["win_rate"])
            while self.have_white(self.RPlayedCardsPos) == 1 or \
                    pyautogui.locateOnScreen('pics/pass.png',
                                             region=self.RPlayedCardsPos,
                                             confidence=self.LandlordFlagConfidence):
                print("等待玩家出牌")
                self.counter.restart()
                while self.counter.elapsed() &lt; 100:
                    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 50)
            self.play_order = 1
        elif self.play_order == 1:
            self.RPlayedCard.setText("...")
            pass_flag = None
            while self.have_white(self.RPlayedCardsPos) == 0 and \
                    not pyautogui.locateOnScreen('pics/pass.png',
                                                 region=self.RPlayedCardsPos,
                                                 confidence=self.LandlordFlagConfidence):
                print("等待下家出牌")
                self.counter.restart()
                while self.counter.elapsed() &lt; 500:
                    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 50)
            self.counter.restart()
            while self.counter.elapsed() &lt; 500:
                QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 50)
            # 不出
            pass_flag = pyautogui.locateOnScreen('pics/pass.png',
                                                 region=self.RPlayedCardsPos,
                                                 confidence=self.LandlordFlagConfidence)
            # 未找到"不出"
            if pass_flag is None:
                # 识别下家出牌
                self.other_played_cards_real = self.find_other_cards(self.RPlayedCardsPos)
            # 找到"不出"
            else:
                self.other_played_cards_real = ""
            print("\n下家出牌：", self.other_played_cards_real)
            self.other_played_cards_env = [RealCard2EnvCard[c] for c in list(self.other_played_cards_real)]
            self.env.step(self.user_position, self.other_played_cards_env)
            # 更新界面
            self.RPlayedCard.setText(self.other_played_cards_real if self.other_played_cards_real else "不出")
            self.play_order = 2
        elif self.play_order == 2:
            self.LPlayedCard.setText("...")
            while self.have_white(self.LPlayedCardsPos) == 0 and \
                    not pyautogui.locateOnScreen('pics/pass.png',
                                                region=self.LPlayedCardsPos,
                                                confidence=self.LandlordFlagConfidence):
                print("等待上家出牌")
                self.counter.restart()
                while self.counter.elapsed() &lt; 500:
                    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 50)
            self.counter.restart()
            while self.counter.elapsed() &lt; 500:
                QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 50)
            # 不出
            pass_flag = pyautogui.locateOnScreen('pics/pass.png',
                                                 region=self.LPlayedCardsPos,
                                                 confidence=self.LandlordFlagConfidence)
            # 未找到"不出"
            if pass_flag is None:
                # 识别上家出牌
                self.other_played_cards_real = self.find_other_cards(self.LPlayedCardsPos)
            # 找到"不出"
            else:
                self.other_played_cards_real = ""
            print("\n上家出牌：", self.other_played_cards_real)
            self.other_played_cards_env = [RealCard2EnvCard[c] for c in list(self.other_played_cards_real)]
            self.env.step(self.user_position, self.other_played_cards_env)
            self.play_order = 0
            # 更新界面
            self.LPlayedCard.setText(self.other_played_cards_real if self.other_played_cards_real else "不出")
        else:
            pass


        self.counter.restart()
        while self.counter.elapsed() &lt; 100:
            QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 50)


    print("{}胜，本局结束!\n".format("农民" if self.env.winner == "farmer" else "地主"))
    QMessageBox.information(self, "本局结束", "{}胜！".format("农民" if self.env.winner == "farmer" else "地主"),
                            QMessageBox.Yes, QMessageBox.Yes)
    self.env.reset()
    self.init_display()

```

到这里，整个AI斗地主出牌流程基本已经完成了。<img src="https://img-blog.csdnimg.cn/img_convert/a6359cf5657bb50a6e0e968313c849ac.png">

#### **三、出牌器用法**

按照上述过程，这款AI出牌器已经制作完成了。后面应该如何使用呢？如果不想研究源码，只想使用这款AI斗地主出牌器，验证下效果，该怎么配置环境运行这个AI出牌器呢？下面就开始介绍。

##### 1. 环境配置

首先我们需要安装这些第三方库，配置相关环境，如下所示：

```
torch==1.9.0
GitPython==3.0.5
gitdb2==2.0.6
PyAutoGUI==0.9.50
PyQt5==5.13.0
PyQt5-sip==12.8.1
Pillow&gt;=5.2.0
opencv-python
rlcard

```

##### 2. 坐标调整确认

我们可以打开欢乐斗地主游戏界面，将游戏窗口模式下最大化运行，把AI出牌器程序窗口需要移至右下角，不能遮挡手牌、地主标志、底牌、历史出牌这些关键位置。

其次我们要确认屏幕截图获取的各个区域是否正确。如果有问题需要进行区域位置坐标调整。

```
# 坐标
self.MyHandCardsPos = (414, 804, 1041, 59)  # 我的截图区域
self.LPlayedCardsPos = (530, 470, 380, 160)  # 左边截图区域
self.RPlayedCardsPos = (1010, 470, 380, 160)  # 右边截图区域
self.LandlordFlagPos = [(1320, 300, 110, 140), (320, 720, 110, 140), (500, 300, 110, 140)]  # 地主标志截图区域(右-我-左)
self.ThreeLandlordCardsPos = (817, 36, 287, 136)      # 地主底牌截图区域，resize成349x168

```

<img src="https://img-blog.csdnimg.cn/img_convert/830f0f58cf7fe5cbb63482ff31dc442b.png">

##### 3. 运行测试

当所有环境配置完成，各区域坐标位置确认无误之后，下面我们就可以直接运行程序，测试效果啦~

首先我们运行AI出牌器程序，打开欢乐斗地主游戏界面，进入游戏。当玩家就位，手牌分发完毕，地主身份确认之后，我们就可以点击画面中开始按钮，让AI来帮助我们斗地主了。

下面可以一起来看看这款AI出牌器的实验效果喔，看看AI是如何带领农民打倒地主，取得胜利的！

若本篇内容对您有所帮助，请三连**点赞**，**在看**，**转发**支持下。
