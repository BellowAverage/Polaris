
--- 
title:  【Python语法实例】-13发牌游戏代码高阶 
tags: []
categories: [] 

---
### 在之前的文章中我们已经学习过通过自定义函数编写发牌游戏，现在这个版本为通过类定义来实现此功能

```
# Cards Module
# Basic classes for a game with playing cards
class Card():
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]     #牌面数字 1--13
    SUITS = ["梅", "方", "红", "黑"]            #梅为梅花，方为方钻，红为红心，黑为黑桃 

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank                #指的是牌面数字 1--13
        self.suit = suit                #suit指的是花色 
        self.is_face_up = face_up       #是否显示牌正面，True为正面，False为牌背面

    def __str__(self): #print()
        if self.is_face_up:
            rep = self.suit + self.rank #+" "+ str(self.pic_order())  
        else:
            rep = "XX"
        return rep

    def flip(self):                     #翻牌方法
        self.is_face_up = not self.is_face_up
        
    def pic_order(self):                #牌的顺序号
        if self.rank=="A":
            FaceNum=1
        elif self.rank=="J":
            FaceNum=11       
        elif self.rank=="Q":
            FaceNum=12
        elif self.rank=="K":
            FaceNum=13
        else:
            FaceNum=int(self.rank) 
        if self.suit=="梅":
            Suit=1
        elif self.suit=="方":
            Suit=2
        elif self.suit=="红":
            Suit=3
        else:
            Suit=4
        return (Suit - 1) * 13 + FaceNum
      
class Hand( ):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):               #重写print()方法
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "无牌"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Poke(Hand):
    """ A deck of playing cards. """
    def populate(self):                     #生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):                      #洗牌
        import random
        random.shuffle(self.cards)          #打乱牌的顺序

    def deal(self, hands, per_hand = 13):    #发牌，发给玩家，每人默认13张牌   
        for rounds in range(per_hand):
            for hand in hands:
                
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
               



if __name__ == "__main__":
    print("This is a module with classes for playing cards.")
    #四个玩家
    players = [Hand(),Hand(),Hand(),Hand()]
    poke1 = Poke()
    poke1.populate()                #生成一副牌
    poke1.shuffle()                 #洗牌
    poke1.deal(players,13)          #发给玩家每人13张牌
    #显示4位牌手的牌
    n=1
    for hand in players:
        print("牌手",n ,end=":")
        print(hand)
        n=n+1
    input("\nPress the enter key to exit.")
    
    


```
