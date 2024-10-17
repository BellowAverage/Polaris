
--- 
title:  C语言版点餐系统源码，C语言课程大作业设计报告-点餐系统 
tags: []
categories: [] 

---
## **** 
 <center>
   C语言课程大作业设计报告 
 </center>

### 简介

本系统实现了一个餐厅管理系功能，涉及到运营一个餐厅的日常运营管理，该系统分别面向餐厅管理人员及服务员和顾客运行，可从管理人员层面完成餐厅信息收集更新，完成服务员与顾客的点菜交互。 源码下载地址：

### 分工

```
//main.c 主要功能函数
int main(int argc, char const *argv[]);//程序主函数，主要负责调用其他函数和 完成必要的初始化
void customers();//顾客菜单
void admins();//管理员菜单
void waiters();//服务员菜单
void engineers();//开发者菜单
void aboutUs();//关于程序，弹出一个包含小组成员等信息的对话框。

//begin.c 与程序初始化有关的函数
void initMain();//播放背景音乐和ASCII码字符画
void playMusic();//播放背景音乐
void stopMusic();//停止播放背景音乐
void setBgColor();//设置控制台的背景颜色

//file.c 文件操作相关函数
int file_exists(char const *file_path);//获取指定文件的内容 ，并以字符串的形式返回
char *file_get_contents(char const *file_path);//将指定的内容写入指定的文件
int file_put_contents(char const *file_path,char const *contents);//判断指定的文件是否存在
int file_delete(char const *file_path);//删除指定的文件

//exception.c 异常处理相关函数
void throw_exception(int errornum,char const message[],char const position[]);
//抛出异常及相关信息，如发生异常的源文件名
Exception catch_exception();//捕获异常
void record_exception();//将异常写入本地文件，以记录程序运行时产生的异常

//view.c 与屏幕显示（视图）相关的函数
void printMenu(char const *viewName);//根据传入的视图名称，找到本地缓存文件，最终将完整的菜单打印出来
void creatMenu(char const *viewName,char *menuList[],int num);//然后生成完整的菜单并写入本地缓存文件
void clearScreenBuffer(void);//清空屏幕缓冲区
void rainbowcolor();//使屏幕背景颜色按照彩虹色的排列顺序以一定的时间间隔变换

//timeController.c 与时间相关的函数
struct tm *setTime();//将当前的时间保存到全局变量中
int getHour();//获取保存到全局变量中的小时
int getMinute();//获取保存到全局变量中的分钟
int getSecond();//获取保存到全局变量中的秒
int getDay();//获取保存到全局变量中的天
int getMonth();//获取保存到全局变量中的月份
int getYear();//获取保存到全局变量中的年
void clockDelay(int delaySecond);//在下一条语句执行前暂停多少秒

//food.c 与菜品相关的工具函数
dish *creatDish();//创建单个菜品
void addToDishes(dishes *head,dish *newDish);//将单个菜品添加到二级菜单中
void creatDishes(dishes *dishHead,int dishNum);//从用户输入获得必要信息来同时创建多个菜品并将这些菜品添加到二级菜单中
void writeDishes(dishes *head,char const *viewName);//处理菜单并将完整菜单写入本地缓存
void printDishes();//打印全部菜品
dishClass *creatDishClass();//创建单个一级菜单
void fixDishClass(dishes *dishHead,int thisId);//为一级菜单添加描述等信息
void setDishList();//设置一级菜单的全局变量初始值

//login.c 与登录有关的函数
int login(userType currentUser);//主登录函数负责根据传入的用户类型分别调用相应的子登录函数
user* getUserFromFile(userType currentUser);//从本地文件读取用户信息，并生成保存着用户信息的链表
int saveUserToFile(userType currentUser,user *head,int i);//将用户信息储存在本地
int adminLogin(userType currentUser);//管理员登录
int customerLogin();//顾客登录
void printUser();//打印所有用户身份的信息
void currentCustomer();//打印所有客户的信息
void operatUser();//对用户链表进行添加和删除节点的操作

//dishMain.c 与点菜 修改菜单相关的功能函数
dishes* dishesController();// 修改菜单


```

张宇负责的函数

```
//begin.c 与程序初始化有关的函数
void deldetesomecache();//删除部分本地文件的内容

//dishesMain.c  与点菜 修改菜单相关的功能函数
void dishesMain();//点菜主程序
void printflist(struct dish *h,int mod);//打印菜单链表
void printfsingledish(struct dish *h,int ID);//查找打印菜单里面的一个元素
struct dish *findsingledish(struct dish *h,int ID);//查找并且返回菜单里面的一个元素
int finddishlist(struct dish *h,int mod,int target);//在对应的菜系里面查找元素
void choosemaindish(struct dish *h);//进入点主菜的程序
void choosesnack(struct dish *h);//进入点小吃的程序
void choosedrink(struct dish *h);//进入点饮料的程序
void printbill(struct dishes *s);//打印账单
void deletepro(struct dishes *s);//删除已点订单里的程序
void deletedishlist(struct dishes *s,int target,int count);//删除订单里的内容
void writeoder(struct dishes *s);//存入订单信息

//seatselection.c 选择座位有关的函数
void printseatlist(char *list);//打印座位表选择界面
void printonlyseat(char *list);//只打印座位表
void printseatnumber(void);//打印当前已使用的座位数量
void seatselection();//选择座位的主程序



```

### 目录

#### 第1章：引言
1. 设计目的1. 功能要求1. 信息描述
#### 第2章：总体设计大纲
1. 程序运行结构图1. 程序模块结构图
#### 第3章：程序详细设计
<li>主程序运行 
  <ol>1. 系统进行初始化1. 选择用户身份1. 登录操作1. 选择座位1. 下单菜品1. 菜单操作1. 用户操作1. 查看用户1. 座位操作1. 客户信息查询1. 清空缓存操作1. 控制台背景操作1. 背景音乐操作
#### 第4章：测试和总结
1. 测试和调试1. 系统存在的问题及解决方案1. 收获及心得体会
### 第1章：引言
1.  设计目的 这是一款面向餐厅的管理系统，该系统旨在为餐厅不同身份的人员服务，通过把餐厅的一系列流水信息存储在本地文件，从而使得相应权限的用户得以访问进行修改查询操作，实现运行一个餐厅的管理操作系统。 <li> 功能要求 
  <ol>1. 功能：菜单数据的本地文件读取到链表与写入到该本地文件，菜单数据读取之后对链表的增加、删除和查找功能。同理地实现对订单信息及账号信息地操作。1. 输入：菜品的各项信息，账号的各项信息，订单信息。1. 输出：订单流水信息，座位信息。
信息描述
1. 菜品信息：编号（菜系）、名称、菜品内容描述、菜品价格1. 订单信息：创建订单时间、订单内所点菜品的编号、订单总价格1. 座位信息：单个座位占用情况、可用的座位数量
### **第2章：总体设计大纲**
1.  程序运行结构图 <img src="image-20220605190403474.png" width="200%" alt="image-20220605190403474"> 1.  程序模块结构图 [外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-seRszK5I-1672984871182)(image-20220605190436385.png)] 
### **第3章：程序详细设计**
<li> **主程序运行** 
  <ol>1.  系统进行初始化 首先会检查必要的文件是否缺失，如果缺失程序会自行终止，然后会调用winmm.lib这个静态库的函数播放背景音乐。由于背景音乐加载需要一定的时间，这会导致程序进入“假死”的状态，所以我们利用ASCII字符画设计了一个加载动画，这样既增加了趣味性，又保证了所需要的功能的正常加载。 <li> 选择用户身份 在动画结束后，会提示选择用户的身份，以便后续使用相应的功能。选择用户身份功能依托switch语句来实现，并且在默认情况下设置运行错误记录以便后续维护。 <pre><code class="prism language-c">#main.c

int menuNum = getchar();
	switch(menuNum){<!-- -->
		case '0':
			getchar();
			admins();
			break;
		case '1':
			getchar();
			waiters();
			break;
		case '2':
			getchar();
			customers();
			break;
		case '3':
			getchar();
			engineers();
			break;
		case '4':
			aboutUs();
			break;					
		default:
			throw_exception(100,"缺乏相应身份的界面！","main.c");
			break;
	}

</code></pre> </li><li> 登录操作 在主界面选择对应的用户身份以后便来到了相应的登录界面。登录函数会根据用户选择的身份分别调用不同的登录函数，然后从本地的文件读取用户数据，以支持验证用户ID和密码操作。其中特别的是顾客身份不会进行验证密码的操作，而是判断用户ID（手机号）是否已经存在用来区分新老顾客。 <pre><code class="prism language-c">//用户权限
enum userType{<!-- -->
admin,waiter,customer,engineer
};

//用户
struct userNode
{<!-- -->
    int userId;
    char information[16];
    userType role;
    char passWord[32];
    struct userNode *next;
};

//统一登录函数
int login(userType currentUser){<!-- -->
	switch(currentUser){<!-- -->
		case admin:
		case waiter:
			return adminLogin(currentUser);
			break;
		case customer:
			return customerLogin();
			break;
		case engineer:
			return adminLogin(currentUser);
			break;
		default:
			printf("没有相应的登录模块，请检查相关代码！");
			throw_exception(100,"no login part","login.c");

	}
	return 0;
}
</code></pre> </li>
**客户操作**
1.  选择座位 从本地文件中读取座位的信息，存储到字符数组中，0代表该座位空缺，1代表已经被占用。再把座位表的情况打印到屏幕上给顾客选择，顾客选择完成之后把座位信息再存储进本地文件。 <li> 下单菜品 在主程序中先初始化订单链表和菜品链表，再读取本地文件中的菜品信息，先打印一级菜单让顾客选择菜品的大类，再进入该大类的函数中进行选菜，可以再次选择菜品的种类或者删除已经点的菜品，或者是结束点菜生成订单。 <pre><code class="prism language-c">while(dishOrder != -1){<!-- -->
		system("cls");
		printMenu("dishmenu");
		printf("输入-1结束点菜\n");
		scanf("%d",&amp;dishClass);
		getchar();
		system("cls");
		
		switch(dishClass)
		{<!-- -->
			case 1:choosemaindish(dishdatahead);			//选择主菜
			break;
			case 2:choosesnack(dishdatahead);				//选择小吃
			break;
			case 3:choosedrink(dishdatahead);				//选择饮料
			break;
			default:printf("请输入正确的编号哦~\n");
			throw_exception(114,"switchwrong1","wrong place");
			break;
		}
		system("cls");
		printbill(Sum);
		printf("输入-1结束点菜进入结算，输入1删除已点菜品，输入其他数字继续点菜\n");
		scanf("%d",&amp;dishOrder);
		getchar();
		if(dishOrder == 1){<!-- -->
			deletepro(Sum);
		}
	}
</code></pre> </li>
**3.管理人员操作**
1.  管理员的一级菜单有菜单操作、用户操作、查看用户和返回主菜单的操作 <li> 菜单操作 可以实时向现有的菜单里写入新的菜品，并且一次输入的菜品没有数量的限制。在完成输入操作后，会将更新后的菜单写入本地缓存文件，在点菜时可以看到更新后的菜单。 <pre><code class="prism language-c">dishes* dishesController(){<!-- -->
	creatDishClass();
	clearScreenBuffer();
	printf("请输入需要添加的菜品的数量\n");
	int dishNumber  = getchar();
	dishNumber -= '0';
	dishes *dishHead = (dishes *)malloc(sizeof(dishes));
	printf("请依次输入菜品编号 名字 描述 价格\n");
	creatDishes(dishHead,dishNumber);

	clearScreenBuffer();
	printf("请再次输入菜系的数字编号进行确认\n");
	int dishClasssNum  = getchar();
	dishClasssNum -= '0';

	writeDishes(dishHead,"dishdata");
	printf("增加菜单成功！");
	system("cls");
	return dishHead;
}
</code></pre> </li><li> 用户账号操作 可对除了开发者（engineer）身份的所有用户进行添加和删除操作。 <pre><code class="prism language-c">void operatUser(){<!-- -->
	int whoami;
	int toperator;
	int userId;
	userType tmpUser;
	printf("请输入 操作符 用户类型 用户id\n用户类型（数字） 管理员0 服务员1 顾客2 开发者3\n操作符（数字） 添加用户1 删除用户0");
	scanf("%d %d %d",&amp;toperator,&amp;whoami,&amp;userId);

	switch(whoami){<!-- -->
		case 0:
			tmpUser = admin;
			break;
		case 1:
			tmpUser = waiter;
			break;
		case 2:
			tmpUser = customer;
			break;
		case 3:
			tmpUser = engineer;
			break;
	}
	user *usertmp = getUserFromFile(tmpUser);
	user *usertmp2 = usertmp;
	user *tempSave = (user *)malloc(sizeof(user));

	switch(toperator){<!-- -->
		case 1:
			tempSave-&gt;next=NULL;
			tempSave-&gt;userId=userId;
			tempSave-&gt;role = tmpUser;
			printf("请输入用户信息 密码\n");
			scanf("\n%s %s",tempSave-&gt;information,tempSave-&gt;passWord);
			saveUserToFile(tmpUser,tempSave);
			break;
		case 0:
			while(usertmp &amp;&amp; usertmp-&gt;next){<!-- -->
				if(usertmp-&gt;next-&gt;userId == userId){<!-- -->
					usertmp-&gt;next = usertmp-&gt;next-&gt;next;
					break;
				}
				usertmp = usertmp-&gt;next;
			}
			//usertmp-&gt;next = NULL;
			saveUserToFile(tmpUser,usertmp2,1);
			break;
	}
	free(tempSave);
	free(usertmp);
	printf("操作成功，返回主菜单\n");
}
</code></pre> </li><li> 查看用户 可以查看所有身份的用户的信息 <pre><code class="prism language-c">
void printUser(){<!-- -->
	system("cls");
	fflush(stdout);
	userType tmpUser;
	int whoami;
	printf("请输入用户类型（数字）\n管理员0 服务员1 顾客2 开发者3");
	scanf("%d",&amp;whoami);

	switch(whoami){<!-- -->
		case 0:
			tmpUser = admin;
			break;
		case 1:
			tmpUser = waiter;
			break;
		case 2:
			tmpUser = customer;
			break;
		case 3:
			tmpUser = engineer;
			break;
	}
	user *usertmp = getUserFromFile(tmpUser);
	printf("用户ID 用户信息 用户密码");
	while(usertmp-&gt;next){<!-- -->
		printf("%d %s %s\n",usertmp-&gt;userId,usertmp-&gt;information,usertmp-&gt;passWord);
		usertmp = usertmp-&gt;next;
	}
}
</code></pre> </li>
**4.服务员操作**
1.  服务员的一级菜单有查看座位情况、查看客户信息的操作。 <li> 有查看座位情况 座位信息的存储是由一串01相间的字符组成，直接从本地文件读入到字符数组中。服务员可直接对该字符串进行操作，查看当前座位的占用情况。 <pre><code class="prism language-c">void printseatnumber(void){<!-- -->
    char *SEAT = file_get_contents("./cache/seatdata.txt");
    int t = 0;
    int number = 0;
    for(int a = 0;a &lt; 5;a++){<!-- -->
        for(int b = 0;b &lt; 5;b++){<!-- -->
            if(*(SEAT + t) == '1'){<!-- -->
                number++;
                }
            }
            t++;
        }
        printf("The seat amount = %d\n",number);
    t = 0;
    int full = 0;
    for(int a = 0;a &lt; 5;a++){<!-- -->
        for(int b = 0;b &lt; 5;b++){<!-- -->
            if(*(SEAT+ t) == '0')
                printf("[%02d]  ",t + 1);
            else{<!-- -->
                printf("[xx]  ");
                full++;
            }
            t++;
        }
        printf("\n\n");
    }

}
</code></pre> </li>1.  查看客户信息 服务员有权限查看所有的客户账号的信息，包括客户的手机号、附加信息。 
**5.开发者操作**
1.  开发者的一级菜单有强制清空缓存、停止播放音乐、播放音乐、修改控制台背景和返回主菜单的操作。 1.  清空缓存操作 删除./cache目录下所有菜单缓存，以便于更新菜单后打印出最新的菜单，以及整个系统的快速运行。 <li> 修改控制台背景 通过调用控制台的color命令，实现修改控制台的背景颜色。 <pre><code class="prism language-c">void setBgColor(){<!-- -->
	int color1;
	int color2;
	char finalColor[] = "color xx"; 
	printf("请输入两个颜色数字");
	printf("%s\n",file_get_contents("./cache/color.cache"));
	scanf("%c%c",&amp;color1,&amp;color2);
	finalColor[6] = color1;
	finalColor[7] = color2;
	system(finalColor);
}
</code></pre> </li><li> 背景音乐操作 使用静库里的函数，实现播放和停止播放背景音乐的操作。其中背景音乐为根目录下的1.mp3 <pre><code class="prism language-c">void playMusic(){<!-- -->
	mciSendString("open 1.mp3 alias bkmusic", NULL, 0, NULL);
	mciSendString("play bkmusic repeat", NULL, 0, NULL);
}

void stopMusic(){<!-- -->
	mciSendString("stop bkmusic", NULL, 0, NULL);
	mciSendString("close bkmusic", NULL, 0, NULL);	
}
</code></pre> </li>
### **第4章：测试和总结**

**测试和调试**
1. 本地文件的读与写操作在一开始的时候很容易出问题，经常出现写不进文件，读不出文件的情况，在多次从小的地方测试，在每个读取文件的节点设置测试点，以检查该文件操作是否正常进行，同时关注每一步文件操作之后的数据内容动向，最终调试出一套可靠的文件操作函数
**系统存在的问题及解决方案**
1. 前期在运行系统的时候会遇到直接退出控制台崩溃的情况，经过多次排除锁定问题多出现在文件的读取上，例如读取本地文件的格式不对从而导致报错崩溃直接退出原有的程序运行结构。最终合理改进数据的读取以及存储方式和结构，不同的数据分别用链表或者字符数组来存储以达到最高的效应。
**收获及心得体会**
1. 链表在流水数据处理上的应用拥有极高的效率，利于增删查改的操作，但同时链表的数据与本地文件的交互过程需要多次测试以使其可靠。1. 类似的管理系统分用户权限操作利于对整体的数据管理，多方协同运作对本地数据进行访问使得整体运行效率增加。1. 面对体量较大的程序，应该在调试的时候设置错误记录点，在运行出错时才能找到问题点，把单个的问题拿出来单独测试，逐一排查，及时是最小的实现功能也使其可靠，才能使整体可靠。
源码下载地址：
