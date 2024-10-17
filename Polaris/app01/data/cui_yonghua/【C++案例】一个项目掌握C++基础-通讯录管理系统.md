
--- 
title:  【C++案例】一个项目掌握C++基础-通讯录管理系统 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- - - - <ul><li>- - - - - - - - - - - - - - - 


### 1、系统需求

用C++来实现一个通讯录管理系统，实现的功能如下：
- `添加联系人`：向通讯录中添加新人，信息包括（姓名、性别、年龄、联系电话、家庭住址）最多记录1000人- `显示联系人`：显示通讯录中所有联系人信息- `删除联系人`：按照姓名进行删除指定联系人- `查找联系人`：按照姓名查看指定联系人信息- `修改联系人`：按照姓名重新修改指定联系人- `清空联系人`：清空通讯录中所有信息- `退出通讯录`：退出当前使用的通讯录
### 2、菜单功能

**功能描述：** 用户选择功能的界面

```
#include&lt;iostream&gt;
using namespace std;

//菜单界面
void showMenu()
{<!-- -->
	cout &lt;&lt; "***************************" &lt;&lt; endl;
	cout &lt;&lt; "*****  1、添加联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  2、显示联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  3、删除联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  4、查找联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  5、修改联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  6、清空联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  0、退出通讯录  *****" &lt;&lt; endl;
	cout &lt;&lt; "***************************" &lt;&lt; endl;
}

int main() {<!-- -->
	showMenu();

	return 0;
}

```

### 3、退出功能

功能描述：退出通讯录系统

思路：根据用户不同的选择，进入不同的功能，可以选择switch分支结构，将整个架构进行搭建

当用户选择0时候，执行退出，选择其他先不做操作，也不会退出程序

**代码：**

```
int main() {<!-- -->

	int select = 0;

	while (true)
	{<!-- -->
		showMenu();

		cin &gt;&gt; select;
		
		switch (select)
		{<!-- -->
		case 1:  //添加联系人
			break;
		case 2:  //显示联系人
			break;
		case 3:  //删除联系人
			break;
		case 4:  //查找联系人
			break;
		case 5:  //修改联系人
			break;
		case 6:  //清空联系人
			break;
		case 0:  //退出通讯录
			cout &lt;&lt; "欢迎下次使用" &lt;&lt; endl;
			return 0;
			break;
		default:
			break;
		}
	}
	return 0;
}

```

### 4、添加联系人

功能描述：实现添加联系人功能，联系人上限为1000人，联系人信息包括（姓名、性别、年龄、联系电话、家庭住址）

添加联系人实现步骤：
- 设计联系人结构体- 设计通讯录结构体- main函数中创建通讯录- 封装添加联系人函数- 测试添加联系人功能
#### 4.1 设计联系人结构体

联系人信息包括：姓名、性别、年龄、联系电话、家庭住址，设计如下：

```
#include &lt;string&gt;  //string头文件
//联系人结构体
struct Person
{<!-- -->
	string m_Name; //姓名
	int m_Sex; //性别：1男 2女
	int m_Age; //年龄
	string m_Phone; //电话
	string m_Addr; //住址
};

```

#### 4.2 设计通讯录结构体

设计时候可以在通讯录结构体中，维护一个容量为1000的存放联系人的数组，并记录当前通讯录中联系人数量，设计如下

```
#define MAX 1000 //最大人数

//通讯录结构体
struct Addressbooks
{<!-- -->
	struct Person personArray[MAX]; //通讯录中保存的联系人数组
	int m_Size; //通讯录中人员个数
};

```

#### 4.3 main函数中创建通讯录

添加联系人函数封装好后，在main函数中创建一个通讯录变量，这个就是我们需要一直维护的通讯录

```
mian函数起始位置添加：

	//创建通讯录
	Addressbooks abs;
	//初始化通讯录中人数
	abs.m_Size = 0;

```

#### 4.4 封装添加联系人函数

思路：添加联系人前先判断通讯录是否已满，如果满了就不再添加，未满情况将新联系人信息逐个加入到通讯录，添加联系人代码：

```
//1、添加联系人信息
void addPerson(Addressbooks *abs)
{<!-- -->
	//判断电话本是否满了
	if (abs-&gt;m_Size == MAX)
	{<!-- -->
		cout &lt;&lt; "通讯录已满，无法添加" &lt;&lt; endl;
		return;
	}
	else
	{<!-- -->
		//姓名
		string name;
		cout &lt;&lt; "请输入姓名：" &lt;&lt; endl;
		cin &gt;&gt; name;
		abs-&gt;personArray[abs-&gt;m_Size].m_Name = name;

		cout &lt;&lt; "请输入性别：" &lt;&lt; endl;
		cout &lt;&lt; "1 -- 男" &lt;&lt; endl;
		cout &lt;&lt; "2 -- 女" &lt;&lt; endl;

		//性别
		int sex = 0;
		while (true)
		{<!-- -->
			cin &gt;&gt; sex;
			if (sex == 1 || sex == 2)
			{<!-- -->
				abs-&gt;personArray[abs-&gt;m_Size].m_Sex = sex;
				break;
			}
			cout &lt;&lt; "输入有误，请重新输入";
		}

		//年龄
		cout &lt;&lt; "请输入年龄：" &lt;&lt; endl;
		int age = 0;
		cin &gt;&gt; age;
		abs-&gt;personArray[abs-&gt;m_Size].m_Age = age;

		//联系电话
		cout &lt;&lt; "请输入联系电话：" &lt;&lt; endl;
		string phone = "";
		cin &gt;&gt; phone;
		abs-&gt;personArray[abs-&gt;m_Size].m_Phone = phone;

		//家庭住址
		cout &lt;&lt; "请输入家庭住址：" &lt;&lt; endl;
		string address;
		cin &gt;&gt; address;
		abs-&gt;personArray[abs-&gt;m_Size].m_Addr = address;

		//更新通讯录人数
		abs-&gt;m_Size++;

		cout &lt;&lt; "添加成功" &lt;&lt; endl;
	}
}

```

#### 4.5 测试添加联系人功能

选择界面中，如果玩家选择了1，代表添加联系人，我们可以测试下该功能

在switch case 语句中，case1里添加：

```
case 1:  //添加联系人
	addPerson(&amp;abs);
	break;

```

### 5、显示联系人

功能描述：显示通讯录中已有的联系人信息，显示联系人实现步骤：
- 封装显示联系人函数- 测试显示联系人功能
#### 5.1 封装显示联系人函数

思路：判断如果当前通讯录中没有人员，就提示记录为空，人数大于0，显示通讯录中信息

显示联系人代码：

```
//2、显示所有联系人信息
void showPerson(Addressbooks * abs)
{<!-- -->
	if (abs-&gt;m_Size == 0)
	{<!-- -->
		cout &lt;&lt; "当前记录为空" &lt;&lt; endl;
	}
	else
	{<!-- -->
		for (int i = 0; i &lt; abs-&gt;m_Size; i++)
		{<!-- -->
			cout &lt;&lt; "姓名：" &lt;&lt; abs-&gt;personArray[i].m_Name &lt;&lt; "\t";
			cout &lt;&lt; "性别：" &lt;&lt; (abs-&gt;personArray[i].m_Sex == 1 ? "男" : "女") &lt;&lt; "\t";
			cout &lt;&lt; "年龄：" &lt;&lt; abs-&gt;personArray[i].m_Age &lt;&lt; "\t";
			cout &lt;&lt; "电话：" &lt;&lt; abs-&gt;personArray[i].m_Phone &lt;&lt; "\t";
			cout &lt;&lt; "住址：" &lt;&lt; abs-&gt;personArray[i].m_Addr &lt;&lt; endl;
		}
	}
}

```

#### 5.2 测试显示联系人功能

在switch case语句中，case 2 里添加

```
case 2:  //显示联系人
	showPerson(&amp;abs);
	break;

```

### 6、删除联系人

功能描述：按照姓名进行删除指定联系人，删除联系人实现步骤：
- 封装检测联系人是否存在- 封装删除联系人函数- 测试删除联系人功能
#### 6.1 封装检测联系人是否存在

设计思路：删除联系人前，我们需要先判断用户输入的联系人是否存在，如果存在删除，不存在提示用户没有要删除的联系人

因此我们可以把检测联系人是否存在封装成一个函数中，如果存在，返回联系人在通讯录中的位置，不存在返回-1

检测联系人是否存在代码：

```
//判断是否存在查询的人员，存在返回在数组中索引位置，不存在返回-1
int isExist(Addressbooks * abs, string name)
{<!-- -->
	for (int i = 0; i &lt; abs-&gt;m_Size; i++)
	{<!-- -->
		if (abs-&gt;personArray[i].m_Name == name)
		{<!-- -->
			return i;
		}
	}
	return -1;
}


```

#### 6.2 封装删除联系人函数

根据用户输入的联系人判断该通讯录中是否有此人，查找到进行删除，并提示删除成功，查不到提示查无此人。

```
//3、删除指定联系人信息
void deletePerson(Addressbooks * abs)
{<!-- -->
	cout &lt;&lt; "请输入您要删除的联系人" &lt;&lt; endl;
	string name;
	cin &gt;&gt; name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{<!-- -->
		for (int i = ret; i &lt; abs-&gt;m_Size; i++)
		{<!-- -->
			abs-&gt;personArray[i] = abs-&gt;personArray[i + 1];
		}
         abs-&gt;m_Size--;
		cout &lt;&lt; "删除成功" &lt;&lt; endl;
	}
	else
	{<!-- -->
		cout &lt;&lt; "查无此人" &lt;&lt; endl;
	}
}

```

#### 6.3 测试删除联系人功能

在switch case 语句中，case3里添加：

```
case 3:  //删除联系人
	deletePerson(&amp;abs);
	break;

```

### 7、查找联系人

功能描述：按照姓名查看指定联系人信息，查找联系人实现步骤
- 封装查找联系人函数- 测试查找指定联系人
#### 7.1 封装查找联系人函数

实现思路：判断用户指定的联系人是否存在，如果存在显示信息，不存在则提示查无此人。查找联系人代码：

```
//4、查找指定联系人信息
void findPerson(Addressbooks * abs)
{<!-- -->
	cout &lt;&lt; "请输入您要查找的联系人" &lt;&lt; endl;
	string name;
	cin &gt;&gt; name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{<!-- -->
		cout &lt;&lt; "姓名：" &lt;&lt; abs-&gt;personArray[ret].m_Name &lt;&lt; "\t";
		cout &lt;&lt; "性别：" &lt;&lt; abs-&gt;personArray[ret].m_Sex &lt;&lt; "\t";
		cout &lt;&lt; "年龄：" &lt;&lt; abs-&gt;personArray[ret].m_Age &lt;&lt; "\t";
		cout &lt;&lt; "电话：" &lt;&lt; abs-&gt;personArray[ret].m_Phone &lt;&lt; "\t";
		cout &lt;&lt; "住址：" &lt;&lt; abs-&gt;personArray[ret].m_Addr &lt;&lt; endl;
	}
	else
	{<!-- -->
		cout &lt;&lt; "查无此人" &lt;&lt; endl;
	}
}

```

#### 7.2 测试查找指定联系人

在switch case 语句中，case4里添加：

```
case 4:  //查找联系人
	findPerson(&amp;abs);
	break;

```

### 8、修改联系人

功能描述：按照姓名重新修改指定联系人，修改联系人实现步骤
- 封装修改联系人函数- 测试修改联系人功能
#### 8.1 封装修改联系人函数

实现思路：查找用户输入的联系人，如果查找成功进行修改操作，查找失败提示查无此人，修改联系人代码：

```
//5、修改指定联系人信息
void modifyPerson(Addressbooks * abs)
{<!-- -->
	cout &lt;&lt; "请输入您要修改的联系人" &lt;&lt; endl;
	string name;
	cin &gt;&gt; name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{<!-- -->
		//姓名
		string name;
		cout &lt;&lt; "请输入姓名：" &lt;&lt; endl;
		cin &gt;&gt; name;
		abs-&gt;personArray[ret].m_Name = name;

		cout &lt;&lt; "请输入性别：" &lt;&lt; endl;
		cout &lt;&lt; "1 -- 男" &lt;&lt; endl;
		cout &lt;&lt; "2 -- 女" &lt;&lt; endl;

		//性别
		int sex = 0;
		while (true)
		{<!-- -->
			cin &gt;&gt; sex;
			if (sex == 1 || sex == 2)
			{<!-- -->
				abs-&gt;personArray[ret].m_Sex = sex;
				break;
			}
			cout &lt;&lt; "输入有误，请重新输入";
		}

		//年龄
		cout &lt;&lt; "请输入年龄：" &lt;&lt; endl;
		int age = 0;
		cin &gt;&gt; age;
		abs-&gt;personArray[ret].m_Age = age;

		//联系电话
		cout &lt;&lt; "请输入联系电话：" &lt;&lt; endl;
		string phone = "";
		cin &gt;&gt; phone;
		abs-&gt;personArray[ret].m_Phone = phone;

		//家庭住址
		cout &lt;&lt; "请输入家庭住址：" &lt;&lt; endl;
		string address;
		cin &gt;&gt; address;
		abs-&gt;personArray[ret].m_Addr = address;

		cout &lt;&lt; "修改成功" &lt;&lt; endl;
	}
	else
	{<!-- -->
		cout &lt;&lt; "查无此人" &lt;&lt; endl;
	}
}

```

#### 8.2 测试修改联系人功能

在switch case 语句中，case 5里添加：

```
case 5:  //修改联系人
	modifyPerson(&amp;abs);
	break;

```

### 9、清空联系人

功能描述：清空通讯录中所有信息，清空联系人实现步骤
- 封装清空联系人函数- 测试清空联系人
#### 9.1 封装清空联系人函数

实现思路： 将通讯录所有联系人信息清除掉，只要将通讯录记录的联系人数量置为0，做逻辑清空即可。清空联系人代码：

```
//6、清空所有联系人
void cleanPerson(Addressbooks * abs)
{<!-- -->
	abs-&gt;m_Size = 0;
	cout &lt;&lt; "通讯录已清空" &lt;&lt; endl;
}

```

#### 9.2 测试清空联系人

在switch case 语句中，case 6 里添加：

```
case 6:  //清空联系人
	cleanPerson(&amp;abs);
	break;

```

**至此，通讯录管理系统完成！**

### 10、总的代码

```
#include&lt;iostream&gt;
#include&lt;string&gt;
using namespace std;
const int MAX = 1000;// #define MAX 1000

// 菜单界面，封装函数显示该界面  如 `void showMenu()`
// 在main函数中调用封装好的函数
void showMenu()
{<!-- -->
	cout &lt;&lt; "***************************" &lt;&lt; endl;
	cout &lt;&lt; "*****  1、添加联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  2、显示联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  3、删除联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  4、查找联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  5、修改联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  6、清空联系人  *****" &lt;&lt; endl;
	cout &lt;&lt; "*****  0、退出通讯录  *****" &lt;&lt; endl;
	cout &lt;&lt; "***************************" &lt;&lt; endl;
}

// 设计联系人结构体
// 包括姓名、性别、年龄、联系电话、家庭住址
struct Person
{<!-- -->
	string m_Name;// 姓名
	int m_Sex;// 性别	 1 男 2 女
	int m_Age;// 年龄
	string m_Phone;	// 电话
	string m_Addr;	// 住址
};

// 设计通讯录的结构体
// 维护一个容量为1000的存放联系人的数组，并记录当前通讯录中联系人数量
struct Addressbooks
{<!-- -->
	struct Person personArray[MAX];// 通讯录中保存的联系人数组，结构体嵌套
	int m_Size;// 通讯录中当前记录联系人个数
};

// 1. 添加联系人
void addPerson(Addressbooks* abs)// 使用结构体指针，addressbooks是结构体嵌套结构体
{<!-- -->
	// 首先判断通讯录是否已满，如果满了就不再添加
	if (abs-&gt;m_Size == MAX)
	{<!-- -->
		cout &lt;&lt; "通讯录已满，无法添加！" &lt;&lt; endl;
	}
	else
	{<!-- -->
		// 然后添加具体的联系人

		string name;// 姓名
		cout &lt;&lt; "请输入姓名：" &lt;&lt; endl;
		cin &gt;&gt; name;
		abs-&gt;personArray[abs-&gt;m_Size].m_Name = name;

		cout &lt;&lt; "请输入性别：" &lt;&lt; endl;// 性别
		cout &lt;&lt; "1 -- 男" &lt;&lt; endl;
		cout &lt;&lt; "2 -- 女" &lt;&lt; endl;
		int sex = 0;
		while (true) // 死循环，直到输入的是对的才停止
		{<!-- -->
			// 如果输入的是1或者2可以退出循环，因为输入的是正确值
			// 如果输入的有误，重新输入
			cin &gt;&gt; sex;
			if (sex == 1 || sex == 2)
			{<!-- -->
				abs-&gt;personArray[abs-&gt;m_Size].m_Sex = sex;// abs-&gt;m_Size表示第几个联系人，从0开始
				break;
			}
			cout &lt;&lt; "输入有误，请重新输入" &lt;&lt; endl;
		}

		cout &lt;&lt; "请输入年龄：" &lt;&lt; endl;// 年龄
		int  age = 0;
		cin &gt;&gt; age;
		abs-&gt;personArray[abs-&gt;m_Size].m_Age = age;

		cout &lt;&lt; "请输入联系电话：" &lt;&lt; endl;// 电话
		string phone;
		cin &gt;&gt; phone;
		abs-&gt;personArray[abs-&gt;m_Size].m_Phone = phone;

		cout &lt;&lt; "请输入家庭住址：" &lt;&lt; endl;// 住址
		string address;
		cin &gt;&gt; address;
		abs-&gt;personArray[abs-&gt;m_Size].m_Addr = address;// 结构体嵌套

		abs-&gt;m_Size++;// 更新下通讯录人数，扩展新的人数

		cout &lt;&lt; "添加成功" &lt;&lt; endl;
	}
}

// 2.显示联系人
void showPerson(Addressbooks* abs)
{<!-- -->
	// 判断通讯录中人数abs-&gt;m_Size是否为0，如果为0，提示记录为空
	// 如果不为0，显示记录的联系人信息
	if (abs-&gt;m_Size == 0)
	{<!-- -->
		cout &lt;&lt; "当前记录为空" &lt;&lt; endl;
	}
	else
	{<!-- -->
		for (int i = 0; i &lt; abs-&gt;m_Size; i++)// 在一行里显示所有信息
		{<!-- -->
			cout &lt;&lt; "姓名：" &lt;&lt; abs-&gt;personArray[i].m_Name &lt;&lt; "\t";// 水平制表符三个空位
			cout &lt;&lt; "性别：" &lt;&lt; (abs-&gt;personArray[i].m_Sex == 1 ? "男" : "女") &lt;&lt; "\t";// 双目运算符
			cout &lt;&lt; "年龄：" &lt;&lt; abs-&gt;personArray[i].m_Age &lt;&lt; "\t";
			cout &lt;&lt; "电话：" &lt;&lt; abs-&gt;personArray[i].m_Phone &lt;&lt; "\t";
			cout &lt;&lt; "住址：" &lt;&lt; abs-&gt;personArray[i].m_Addr &lt;&lt; endl;
		}
	}
}

// 3.删除联系人
// 3.1 检测联系人是否存在，如果存在返回联系人所在数组中的具体位置，不存在返回-1
// 参数1 通讯录 参数2 对比姓名
int isExist(Addressbooks* abs, string name)
{<!-- -->
	for (int i = 0; i &lt; abs-&gt;m_Size; i++)
	{<!-- -->
		// 找到用户输入的姓名了
		if (abs-&gt;personArray[i].m_Name == name)
		{<!-- -->
			return i;	// 如果找到了，返回这个人在数组中的下标编号
		}
	}
	return -1;	// 如果遍历结束都没有找到，返回-1
}

// 3.2 删除指定的联系人
void deletePerson(Addressbooks* abs)
{<!-- -->
	cout &lt;&lt; "请输入您需要删除的联系人：" &lt;&lt; endl;
	string name;
	cin &gt;&gt; name;

	// ret == -1 未查到；ret != -1 查到
	int ret = isExist(abs, name);

	if (ret != -1)
	{<!-- -->
		// 查找到人，进行删除操作
		for (int i = ret; i &lt; abs-&gt;m_Size; i++)// ret不为零的情况下，返回的是需要删除的联系人所在的下标
		{<!-- -->
			// 数据前移，一个一个往前移动
			abs-&gt;personArray[i] = abs-&gt;personArray[i + 1];
		}
		abs-&gt;m_Size--;	// 更新通讯录中的人员数
		cout &lt;&lt; "删除成功" &lt;&lt; endl;
	}
	else
	{<!-- -->
		cout &lt;&lt; "查无此人" &lt;&lt; endl;
	}
}

// 4.查找指定联系人信息
void findPerson(Addressbooks* abs)
{<!-- -->
	cout &lt;&lt; "请输入您要查找的联系人" &lt;&lt; endl;
	string name;
	cin &gt;&gt; name;

	// 判断指定的联系人是否存在通讯录中
	int ret = isExist(abs, name);

	if (ret != -1)	// 找到联系人(类似2.显示联系人信息)
	{<!-- -->
		cout &lt;&lt; "姓名：" &lt;&lt; abs-&gt;personArray[ret].m_Name &lt;&lt; "\t";
		cout &lt;&lt; "性别：" &lt;&lt; (abs-&gt;personArray[ret].m_Sex == 1 ? "男" : "女") &lt;&lt; "\t";
		cout &lt;&lt; "年龄：" &lt;&lt; abs-&gt;personArray[ret].m_Age &lt;&lt; "\t";
		cout &lt;&lt; "电话：" &lt;&lt; abs-&gt;personArray[ret].m_Phone &lt;&lt; "\t";
		cout &lt;&lt; "住址：" &lt;&lt; abs-&gt;personArray[ret].m_Addr &lt;&lt; endl;
	}
	else   // 未找到联系人
	{<!-- -->
		cout &lt;&lt; "查无此人" &lt;&lt; endl;
	}
}

// 5.修改指定联系人信息
void modifyPerson(Addressbooks* abs)
{<!-- -->
	cout &lt;&lt; "请输入您要修改的联系人" &lt;&lt; endl;
	string name;
	cin &gt;&gt; name;

	int ret = isExist(abs, name);
	if (ret != -1)
	{<!-- -->
		string name;// 姓名
		cout &lt;&lt; "请输入姓名：" &lt;&lt; endl;
		cin &gt;&gt; name;
		abs-&gt;personArray[ret].m_Name = name;

		cout &lt;&lt; "请输入性别：" &lt;&lt; endl;// 性别
		cout &lt;&lt; "1 -- 男" &lt;&lt; endl;
		cout &lt;&lt; "2 -- 女" &lt;&lt; endl;
		int sex = 0;
		while (true)
		{<!-- -->
			cin &gt;&gt; sex;
			if (sex == 1 || sex == 2)
			{<!-- -->
				// 输入正确 退出循环输入
				abs-&gt;personArray[ret].m_Sex = sex;
				break;
			}
			cout &lt;&lt; "输入有误，请重新输入";
		}

		cout &lt;&lt; "请输入年龄：" &lt;&lt; endl;// 年龄
		int age = 0;
		cin &gt;&gt; age;
		abs-&gt;personArray[ret].m_Age = age;

		cout &lt;&lt; "请输入联系电话：" &lt;&lt; endl;// 联系电话
		string phone;
		cin &gt;&gt; phone;
		abs-&gt;personArray[ret].m_Phone = phone;

		cout &lt;&lt; "请输入家庭住址：" &lt;&lt; endl;// 家庭住址
		string address;
		cin &gt;&gt; address;
		abs-&gt;personArray[ret].m_Addr = address;

		cout &lt;&lt; "修改成功" &lt;&lt; endl;
	}
	else
	{<!-- -->
		cout &lt;&lt; "查无此人" &lt;&lt; endl;
	}
}

// 6.清空联系人
void cleanPerson(Addressbooks* abs)
{<!-- -->
	abs-&gt;m_Size = 0;	// 将当前记录联系人数量置为0，做逻辑清空操作
	cout &lt;&lt; "通讯录已清空" &lt;&lt; endl;
}

int main()
{<!-- -->
	Addressbooks abs;// 创建通讯录结构体变量
	abs.m_Size = 0;// 初始化通讯录中当前人员个数
	int select = 0;	// 创建用户选择输入的变量

	while (true)// 只有0是真正意义上的退出，选择其他的值都不会退出，而是进行循环
	{<!-- -->
		showMenu();// 菜单的调用

		cin &gt;&gt; select;

		switch (select)
		{<!-- -->
		case 1:	// 1.添加联系人
			addPerson(&amp;abs);	// 利用地址传递可以修改形参
			break;
		case 2:	// 2.显示联系人
			showPerson(&amp;abs);
			break;
		case 3:  // 3.删除联系人，case中如果后面有打断代码，用{}括起来，不会报错
		/*{
			cout &lt;&lt; "请输入删除联系人姓名：" &lt;&lt; endl;
			string name;
			cin &gt;&gt; name;

			if (isExist(&amp;abs, name) == -1)
			{
				cout &lt;&lt; "查无此人" &lt;&lt; endl;
			}
			else
			{
				cout &lt;&lt; "找到此人" &lt;&lt; endl;
			}
		}*/
			deletePerson(&amp;abs);
			break;// break前面的程序比较长时加大括号
		case 4:	// 4.查找联系人
			findPerson(&amp;abs);
			break; 
		case 5:	// 5.修改联系人
			modifyPerson(&amp;abs);
			break;
		case 6:	// 6.清空联系人
			cleanPerson(&amp;abs);
			break;
		case 0:	// 0.退出通讯录
			cout &lt;&lt; "欢迎下次使用" &lt;&lt; endl;
			return 0;
			break;
		default:
			break;
		}
	}
	return 0;
}


```
