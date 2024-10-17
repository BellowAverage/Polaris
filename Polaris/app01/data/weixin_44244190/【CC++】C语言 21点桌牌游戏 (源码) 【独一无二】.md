
--- 
title:  【C/C++】C语言 21点桌牌游戏 (源码) 【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>C语言 21点桌牌游戏 (源码) 【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - <ul><li>- - - - - - - -  
   </li>- </ul> 
  
  


## 一、设计要求

21点又名黑杰克(Blackiack)，起源于法国，已流传到世界各地，有着悠久的历史。该游戏由2到6个人玩，使用除大小王之外的52张牌，游戏者的目标是使手中的牌的点数之和不超过 21点且尽量大。21点一般用到 1-8副牌。大家手中扑克点数的计算是:2至9牌，按其原点数计算:K、Q、J和10牌都算作10 点(一般记作 T，即 ten 之意);A 牌(ace)既可算作1点也可算作11 点，由玩家自己决定(当玩家停牌时，点数一律视为最大而尽量不爆，如A+9为20，A+4+8为13，A+3+A 视为15)。简易规则:玩家电脑各发2张牌，玩家两张牌均为明牌，电脑一明一暗;玩家电脑轮流要牌(都为明牌)，也可以选择停牌，当某一方点数为21点时则直接获胜，超过21点则直接淘汰;当各方都选择停牌时，则计算各方点数，点数大者获胜。

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈 


【功能要求】
1. 系统主界面和菜单MainMenu(5分);1. 能够设置用几副牌(1-8)(2分):1. 能够支持单玩家模式(5分):1. 能够支持玩家电脑模式(5分);1. 能够支持玩家多电脑(最多5个)模式(3分):1. 打印牌池 Display，利用 ASCI码3、4、5、6的字符和 2-10AKQJ来显示各方初始和后续手牌(5分);1. 必须有某方点数计算函数CalcPoints(5分);
## 二、代码示例

### 2.1 主界面展示

<img src="https://img-blog.csdnimg.cn/direct/0750b456ff044efc839c0d878960e178.png" alt="在这里插入图片描述">

### 2.2 单玩家模式

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈 


<img src="https://img-blog.csdnimg.cn/direct/75813ba4f14849c6af79235b353492d4.png" alt="在这里插入图片描述">

### 2.3 玩家要牌(单玩家)

<img src="https://img-blog.csdnimg.cn/direct/3f536e90323a4ecab66ca00bfbe52edc.png" alt="在这里插入图片描述">

### 2.4 玩家停牌牌(单玩家)

<img src="https://img-blog.csdnimg.cn/direct/a9fa94a2643b4e2da9a4328975d8d97e.png" alt="在这里插入图片描述">

### 2.5 玩家VS电脑

<img src="https://img-blog.csdnimg.cn/direct/ccf5c2f4b05f4d39a3228b43833c7a74.png" alt="在这里插入图片描述">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈 


### 2.6 玩家要牌(玩家VS电脑)

<img src="https://img-blog.csdnimg.cn/direct/6d2060027d6d4d4780a1bdfda4421a27.png" alt="在这里插入图片描述">

### 2.7 玩家VS玩家

<img src="https://img-blog.csdnimg.cn/direct/dda784425ae249cfa49b70aeaea52a41.png" alt=" 	">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈 


### 2.8 玩家1要牌(玩家VS玩家)

<img src="https://img-blog.csdnimg.cn/direct/eecc6c54ce10442a89855101912d874a.png" alt="在这里插入图片描述">

### 2.9 玩家2要牌(玩家VS玩家)

<img src="https://img-blog.csdnimg.cn/direct/94d0fe85c5504affaf1cf241d40a98a9.png" alt="在这里插入图片描述">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈 


## 三、代码展示

```

#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;time.h&gt;

// 定义牌的点数
enum CardValue {<!-- -->
    TWO = 2, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE
};

// 定义副牌数量的上下限
#define MIN_DECKS 1
#define MAX_DECKS 8

// 函数声明
void MainMenu();
void SetDeckCount();
void SinglePlayerMode();
void PlayerVsComputerMode();
void MultiPlayerVsComputerMode();
void Display(int* hand, int numCards, const char* playerName);
int CalculatePoints(int* hand, int numCards);

// 初始化牌堆
void InitializeDeck(int* deck, int numDecks) {<!-- -->
    for (int i = 0; i &lt; 52 * numDecks; i++) {<!-- -->
        deck[i] = i; // 使用整数表示52张牌
    }

    // 打乱牌堆，可以使用洗牌算法
    for (int i = 0; i &lt; 52 * numDecks; i++) {<!-- -->
        int j = rand() % (52 * numDecks);
        int temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
}

// 抽牌
int DrawCard(int* deck) {<!-- -->
    static int index = 0; // 用于跟踪抽牌的位置
    return deck[index++];
}

int main() {<!-- -->
    srand(time(NULL)); // 初始化随机数种子
    MainMenu();
    return 0;
}
// &gt;👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈

void MainMenu() {<!-- -->
    int choice;
    while (1) {<!-- -->
        printf("1. 单玩家模式\n");
        printf("2. 玩家vs电脑模式\n");
        printf("3. 玩家多电脑模式\n");
        printf("4. 退出游戏\n");
        printf("请选择游戏模式: ");
        scanf("%d", &amp;choice);

        switch (choice) {<!-- -->
        case 1:
            SinglePlayerMode();
            break;
        case 2:
            PlayerVsComputerMode();
            break;
        case 3:
            MultiPlayerVsComputerMode();
            break;
        case 4:
            printf("感谢游玩21点游戏！再见。\n");
            exit(0);
        default:
            printf("无效的选项，请重新选择。\n");
            break;
        }
    }
}

// 函数实现略.......
// 函数实现略.......

```

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 桌牌游戏 ” 获取。👈👈👈 

