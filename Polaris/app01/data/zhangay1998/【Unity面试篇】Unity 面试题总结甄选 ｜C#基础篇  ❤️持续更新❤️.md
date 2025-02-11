
--- 
title:  【Unity面试篇】Unity 面试题总结甄选 ｜C#基础篇 | ❤️持续更新❤️ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">

#### 前言
- 关于Unity面试题相关的所有知识点：- 为了方便大家可以重点复习某个模块，所以将各方面的知识点进行了拆分并更新整理了新的内容，并对之前的版本中有些模糊的地方进行了纠正。- 所以本篇文章就来整理一下<font color="#green" size="4">C#基础篇的面试题</font>，说不准就会面试的时候就会遇到！


#### 【Unity面试篇】Unity 面试题总结甄选 ｜C#基础篇 | ❤️持续更新❤️
- <ul><li><ul><li>- <ul><li>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


<img src="https://img-blog.csdnimg.cn/4e48586ad74c4742a075c74f28b72c03.png" alt="请添加图片描述">

### ❤️C#基础 进入正题

##### 1. 面向对象的三大特点
1. **继承**： 提高代码重用度，增强软件可维护性的重要手段，符合开闭原则。继承最主要的作用就是把子类的公共属性集合起来，便与共同管理，使用起来也更加方便。你既然使用了继承，那代表着你认同子类都有一些共同的特性，所以你把这些共同的特性提取出来设置为父类。继承的传递性：传递机制 a▶b; b▶c; c具有a的特性 。继承的单根性：在C#中一个类只能继承一个类，不能有多个父类。1. **封装**： 封装是将数据和行为相结合，通过行为约束代码修改数据的程度，增强数据的安全性，属性是C#封装实现的最好体现。就是将一些复杂的逻辑经过包装之后给别人使用就很方便，别人不需要了解里面是如何实现的，只要传入所需要的参数就可以得到想要的结果。封装的意义在于保护或者防止代码（数据）被我们无意中破坏。1. **多态性**： 多态性是指同名的方法在不同环境下，自适应的反应出不同得表现，是方法动态展示的重要手段。多态就是一个对象多种状态，子类对象可以赋值给父类型的变量。
##### 2. 简述值类型和引用类型

**介绍**
- **值类型**：包含了所有简单类型（整数、浮点、bool、char）、struct、enum。 继承自System.ValueTyoe- **引用类型**包含了string，object，class，interface，delegate，array 继承自System.Object
**区别**
1. 值类型存储在内存栈中，引用类型数据存储在内存堆中，而内存单元中存放的是堆中存放的地址。1. 值类型存取快，引用类型存取慢。1. 值类型表示实际数据，引用类型表示指向存储在内存堆中的数据的指针和引用。1. 栈的内存是自动释放的，堆内存是.NET 中会由 GC 来自动释放。1. 值类型继承自 System.ValueType,引用类型继承自 System.Object。1. 值类型在栈中存储的是直接的值，引用类型数据本身实在堆中，栈中存放的是一个引用的地址。
##### 3. 重载和重写的区别
1. 封装、继承、多态所处位置不同，重载在同类中，重写在父子类中。1. 定义方式不同，重载方法名相同参数列表不同，重写方法名和参数列表都相同。1. 调用方式不同，重载使用相同对象以不同参数调用，重写用不同对象以相同参数调用。1. 多态时机不同，重载时编译时多态，重写是运行时多态。
##### 4. Net与 Mono 的关系？

.Net是一个语言平台，Mono为.Net提供集成开发环境，集成并实现了.NET的编译器、CLR 和基础类库，使得.Net既可以运行在windows也可以运行于 linux，Unix，Mac OS 等。

##### 5. C#中所有引用类型的基类是什么

引用类型的基类是System.Object值类型的基类是 System.ValueType。

同时，值类型也隐式继承自System.Object。

##### 6. 请简述ArrayList和 List的主要区别
- ArrayList 不带泛型 数据类型丢失- List 带泛型 数据类型不丢失- ArrayList 需要装箱拆箱 List不需要
ArrayList存在不安全类型（ArrayList会把所有插 ⼊其中的数据都当做Object来处理）装箱拆箱的 操作（费时）IList是接⼝，ArrayList是⼀个实现了 该接⼝的类，可以被实例化

List类是ArrayList类的泛型等效类。它的大部分用法都与ArrayList相似，因为List类也继承了IList接口。最关键的区别在于，在声明List集合时，我们同时需要为其声明List集合内数据的对象类型。

##### 7. GC 相关知识点

**GC的概念**
1. C#内部有两个内存管理池:堆内存和栈内存。栈内存(stack)主要用来存储较小的和短暂的数据，堆内存(heap)主要用来存储较大的和存储时间较长的数据。C#中的变量只会在堆栈或者堆内存上进行内存分配，变量要么存储在栈内存上，要么处于堆内存上。1. 只要变量处于激活状态，则其占用的内存会被标记为使用状态，则该部分的内存处于被分配的状态。1. 一旦变量不再激活，则其所占用的内存不再需要，该部分内存可以被回收到内存池中被再次使用，这样的操作就是内存回收。处于栈上的内存回收及其快速，处于堆上的内存并不是及时回收的，此时其对应的内存依然会被标记为使用状态。不再使用的内存只会在GC的时候才会被回收。1. 垃圾回收主要是指堆上的内存分配和回收，C#中会定时对堆内存进行GC操作。
**GC会带来的问题**
1.  游戏性能：GC操作是一个极其耗费事件的操作，堆内存上的变量或者引用越多则导致遍历检查时的操作变得十分缓慢，使得游戏运行缓慢，例如当CPU处于游戏性能的关键时刻，任何一个操作就会导致游戏帧率下降，造成极大的影响。 1.  游戏内存：（unityGC采用的是非分代非压缩的标记清除算法）GC操作会产生“内存碎片化”。当一个单元内存从堆中分配出来，其大小取决于存储变量的大小。当内存被回收到堆上时，有可能被堆内存分割成碎片化的单元。（就是说总容量大小时固定的，但是单元内存较小。例如房子很大，房间很小，找不到合适的房间）即下次分配时找不到合适的储存单元，就会触发GC操作，或者堆内存扩容操作，导致GC频发发生和游戏内存越来越大。 
**GC触发时机**
1. 在堆内存上进行内存分配操作，而内存不够的时候都会触发垃圾回收来利用闲置的内存;1. GC会自动的触发，不同平台运行频率不—样;1. GC可以被强制执行。
**如何避免GC？**
1. 减少临时变量的使用，多使用公共对象，多利用缓存机制。（将容器定义到函数外，用到容器的时候进行修改即可）1. 减少new对象的次数。1. 对于大量字符串拼接时，将StringBuilder代替String。（string不可修改性，修改即创建一个新的string对象，旧的直接抛弃等待GC，但少量字符串拼接用string，性能优于stringbuilder）1. 使用扩容的容器时，例如：List，StringBuilder等，定义时尽量根据存储变量的内存大小定义储存空间，减少扩容的操作。（扩容后，旧的容器直接抛弃等待GC）1. 代码逻辑优化：例如计时器当大于1s后才进行文本修改，而不是每帧都修改，或者禁止在关键时候GC，影响游戏性能，可以在加载页面或者进度条的时候GC。1. 利用对象池：对象池是一种Unity经常用到的内存管理服务，针对经常消失生成的对象，例如子弹，怪物等，作用在于减少创建每个对象的系统开销。在我们想要对象消除时，不直接Destory，而是隐藏起来SetActive（false），放入池子中，当需要再次显示一个新的对象时，先去池子中看有没有隐藏对象，有就取出来（显示） SetActive（true），没有的话，再实例化。1. 减少装箱拆箱( 装箱是将值类型转换为 object 类型或由此值类型实现的任何接口类型的过程)的操作1. 协程： yeild return 0 会产生装箱拆箱，可以替换为 yeild return null。
##### 8. 结构体和类

**结构体和类的区别**
1. 结构体是值类型，类是引用类型。1. 结构体存在栈中，类存在堆中。1. 结构体变量和类对象进行类型传递时,结构体变量进行的就是值传递,而类对象进行的是引用传递，或者说传递的是指针,这样在函数中改变参数值,结构体对象的值是不变的,而类对象的值是变化了。1. 在C#中结构体类型定义时，成员是不能初始化的,这样就导致了，定义结构体变量时,变量的所有成员都要自己赋值初始化。但对于类，在定义类时,就可以初始化其中的成员变量,所以在定义对象时,对象本身就已经有了初始值,你可以自己在重新给个别变量赋值。(注意在C++中，类的定义中是不能初始化的，初始化要放在构造函数中)1. 结构体不能申明无参的构造函数，而类可以。1. 声明了结构类型后，可以使用new运算符创建构造对象，也可以不使用new关键字。如果不使用new，那么在初始化所有字段之前，字段将保持未赋值状态且对象不可用。1. 结构体申明有参构造函数后，无参构造不会被顶掉。1. 结构体不能申明析构函数，而类可以。1. 结构体不能被继承，而类可以。1. 结构体需要在构造函数中初始化所有成员变量，而类随意。1. 结构体不能被静态static修饰(不存在静态结构体)，而类可以。
**使用情景** 结构体：
1. 结构体是值类型在栈中，栈的存取速度比堆快，但是容量小，适合轻量级的对象，比如点、矩形、颜色。1. 如果对象是数据集合时，优先考虑接结构体（位置，坐标）1. 在变量传值的时候，希望传递对象的是拷贝，而不是对象的引用地址，这个时候就可以使用结构体。
类：
1. 类是引用类型，存储在堆中，堆的容量大，适合重量级的对象，栈的空间不大，大量的对应当存在于堆中。1. 如果对象需要继承和多态特征，用类（玩家、怪物）。
##### 9. C#中四种访问修饰符是哪些？各有什么区别？
1. **属性修饰符**1. **存取修饰符**1. **类修饰符**1. **成员修饰符**
**属性修饰符：** Serializable：按值将对象封送到远程服务器。 STATread：是单线程套间的意思，是⼀种线程模型。 MATAThread：是多线程套间的意思，也是⼀种线程模 型。

**存取修饰符：** public：存取不受限制。 private：只有包含该成员的类可以存取。 internal：只有当前⼯程可以存取。 protected：只有包含该成员的类以及派⽣类可以存 取。

**类修饰符：** abstract：抽象类。指示⼀个类只能作为其它类的基 类。 sealed：密封类。指示⼀个类不能被继承。理所当 然，密封类不能同时⼜是抽象类，因为抽象总是希望 被继承的。

**成员修饰符：** abstract：指示该⽅法或属性没有实现。 sealed：密封⽅法。可以防⽌在派⽣类中对该⽅法的 override（᯿载）。不是类的每个成员⽅法都可以作为 密封⽅法密封⽅法，必须对基类的虚⽅法进⾏᯿载， 提供具体的实现⽅法。所以，在⽅法的声明中， sealed修饰符总是和override修饰符同时使⽤。 delegate：委托。⽤来定义⼀个函数指针。C#中的事 件驱动是基于delegate + event的。 const：指定该成员的值只读不允许修改。 event：声明⼀个事件。 extern：指示⽅法在外部实现。 override：᯿写。对由基类继承成员的新实现。 readonly：指示⼀个域只能在声明时以及相同类的内 部被赋值。 static：指示⼀个成员属于类型本身，⽽不是属于特定 的对象。即在定义后可不经实例化，就可使⽤。 virtual：指示⼀个⽅法或存取器的实现可以在继承类中 被覆盖。 new：在派⽣类中隐藏指定的基类成员，从⽽实现᯿ 写的功能。 若要隐藏继承类的成员，请使⽤相同名称 在派⽣类中声明该成员，并⽤ new 修饰符修饰它。

##### 10. 修饰符 简述private，public，protected，internal的区别
- public：对任何类和成员都公开，无限制访问- private：仅对该类公开- protected：对该类和其派生类公开- internal：只能在包含该类的程序集中访问该类- protected internal：protected + internal
##### 11. 堆和栈的区别?

通常保存着我们代码执行的步骤，如在代码段1中 AddFive()方法，int pValue变量，int result变量等等。 而堆上存放的则多是对象，数据等。(译者注:忽略编 译器优化)我们可以把栈想象成一个接着一个叠放在 一起的盒子。当我们使用的时候，每次从最顶部取走 一个盒子。 栈也是如此，当一个方法(或类型)被调 用完成的时候，就从栈顶取走(called a Frame，译 注:调用帧)，接着下一个。堆则不然，像是一个仓 库，储存着我们使用的各种对象等信息，跟栈不同的 是他们被调用完毕不会立即被清理掉。
1. GC方面：栈保持着先进后出的原则，是一片连续的内存域，有系统自动分配和维护，产生的垃圾系统自动释放。而堆是无序的，他是一片不连续的内存域，用户自己来控制和释放，如果用户自己不释放的话，当内存达到一定的特定值时，通过垃圾回收器(GC)来回收。1. 存储方面：栈通常保存着我们代码执行的步骤，如方法变量等等。而堆上存放的则多是对象，数据等。我们可以把栈想象成一个接着一个叠放在一起的盒子(越高内存地址越低)。当我们使用的时候，每次从最顶部取走一个盒子，当一个方法（或类型）被调用完成的时候，就从栈顶取走接着下一个。堆则不然，像是一个仓库，储存着我们使用的各种对象等信息，跟栈不同的是他们被调用完毕不会立即被清理掉。1. 缓存方面：栈使用的是一级缓存，他们通常都是被调用时处于存储空间中，调用完毕立即释放;堆是存放在二级缓存中，生命周期由虚拟机的垃圾回收算法来决定（并不是一旦成为孤儿对象就能被回收)。所以调用这些对象的速度要相对来得低一些。1. 存储方面：栈(Stack)是一种先进后出的数据结构，在内存中，变量会被分配在栈上来进行操作。堆(heap)是用于为引用类型的实例(对象),分配空间的内存区域，在堆上创建一个对象，会将对象的地址传给栈上的变量(反过来叫变量指向此对象，或者变量引用此对象)-----也就是栈上的变量指向了堆上地址为XXX的实例(对象)。
##### 12. 静态构造函数
1. 静态构造函数既没有访问修饰符，也没有参数。1. 在创建第一个类实例或任何静态成员被引用时，.NET将自动调用静态构造函数来初始化类。1. 一个类只能有一个静态构造函数。1. 无参数的构造函数可以与静态构造函数共存。1. 最多只运行一次。1. 静态构造函数不可以被继承。1. 如果没有写静态构造函数，而类中包含带有初始值设定的静态成员，那么编译器会自动生成默认的静态构造函数。1. 如果静态构造函数引发异常，运行时将不会再次调用该构造函数，并且在程序运行所在的应用程序域的生存期内，类型将保持未初始化。
**在类的构造函数前加上static会报什么错?为什么?** 构造函数格式为public+类名如果加上 static 会报错（静态构造函数不能有访问、型的对象，静态构造函数只执行一次； 运行库创建类实例或者首次访问静态成员之前，运行库调用静态构造函数； 静态构造函数执行先于任何实例级别的构造函数； 显然也就无法使用this和 base 来调用构造函数。 一个类只能有一个静态函数，如果有静态变量，系统也会自动生成静态函数

##### 13. C# String类型比 stringBuilder 类型的优势是什么?

如果是处理字符串的话，用string中的方法每次都需要创建一个新的字符串对象并且分配新的内存地址，而 stringBuilder 是在原来的内存里对字符串进行修改，所以在字符串处理方面还是建议用stringBuilder这样比较节约内存。但是 string 类的方法和功能仍然还是比 stringBuilder 类要强。

string类由于具有不可变性（即对一个 string 对象进行任何更改时，其实都是创建另外一个 string 类的对象），所以当需要频繁的对一个 string 类对象进行更改的时候，建议使用StringBuilder 类，StringBuilder 类的原理是首先在内存中开辟一定大小的内存空间，当对此 StringBuilder 类对象进行更改时， 如果内存空间大小不够， 会对此内存空间进行扩充，而不是重新创建一个对象，这样如果对一个字符串对象进行频繁操作的时候，不会造成过多的内存浪费，其实本质上并没有很大区别，都是用来存储和操作字符串的，唯一的区别就在于性能上。

String主要用于公共 API，通用性好、用途广泛、读取性能高、占用内存小。

StringBuilder主要用于拼接 String，修改性能好。

不过现在的编译器已经把String的 + 操作优化成 StringBuilder 了， 所以一般用String 就可以了

String是不可变的，所以天然线程同步。

StringBuilder可变，非线程同步。

##### 14. C#函数 Func(string a, string b)用 Lambda 表达式怎么写?

```
(a,b) =&gt; {<!-- -->};

```

##### 15. 虚函数实现原理

每个虚函数都会有一个与之对应的虚函数表，该虚函数表的实质是一个指针数组，存放的是每一个对象的虚函数入口地址。对于一个派生类来说，他会继承基类的虚函数表同时增加自己的虚函数入口地址，如果派生类重写了基类的虚函数的话，那么继承过来的虚函数入口地址将被派生类的重写虚函数入口地址替代。 那么在程序运行时会发生动态绑定，将父类指针绑定到实例化的对象实现多态。

##### 16. 指针和引用的区别
1. 引用不能为空，即不存在对空对象的引用，指针可以为空，指向空对象。1. 引用必须初始化，指定对哪个对象的引用，指针不需要。1. 引用初始化后不能改变，指针可以改变所指对象的值。1. 引用访问对象是直接访问，指针访问对象是间接访问。1. 引用的大小是所引用对象的大小，指针的大小，是指针本身大小，通常是4字节。1. 引用没有const，指针有const1. 引用和指针的+自增运算符意义不同。1. 引用不需要分配内存空间，指针需要。
##### 17. C#中有哪些常用的容器类，各有什么特点。

List，HashTable，Dictionary，Stack，Queue
- **Stack栈**：先进后出，入栈和出栈，底层泛型数组实现，入栈动态扩容2倍- **Queue队列**：先进先出，入队和出队，底层泛型数组实现，表头表尾指针，判空还是满通过size比较 Queue和Stack主要是用来存储临时信息的- **Array数组**：需要声明长度，不安全- **ArrayList数组列表**：动态增加数组，不安全，实现了IList接口（表示可按照索引进行访问的非泛型集合对象），Object数组实现- **List列表**：底层实现是泛型数组，特性，动态扩容，泛型安全 将泛型数据（对值类型来说就是数据本身，对引用类型来说就是引用）存储在一个泛型数组中，添加元素时若超过当前泛型数组容量，则以2倍扩容，进而实现List大小动态可变。（注：大小指容量，不是Count）- **LinkList链表** 1、数组和List、ArrayList集合都有一个重大的缺陷，就是从数组的中间位置删除或插入一个元素需要付出很大的代价，其原因是数组中处于被删除元素之后的所有元素都要向数组的前端移动。 2、LinkedList（底层是由链表实现的）基于链表的数据结构，很好的解决了数组删除插入效率低的问题，且不用动态的扩充数组的长度。 3、LinkedList的优点：插入、删除元素效率比较高；缺点：访问效率比较低。- **HashTable哈希表（散列表）** 概念：不定长的二进制数据通过哈希函数映射到一个较短的二进制数据集，即Key通过HashFunction函数获得HashCode 装填因子：α=n/m=0.72 ,存储的数据N和空间大小M 然后通过哈希桶算法，HashCode分段，每一段都是一个桶结构，一般是HashCode直接取余。 桶结构会加剧冲突，解决冲突使用拉链法，将产生冲突的元素建立一个单链表，并将头指针地址存储至Hash表对应桶的位置。这样定位到Hash表桶的位置后可通过遍历单链表的形式来查找元素。 1、Key—Value形式存取，无序，类型Object，需要类型转换。 2、Hashtable查询速度快，而添加速度相对慢 3、Hashtable中的数据实际存储在内部的一个数据桶里（bucket结构体数组），容量固定，根据数组索引获取值。
```
//哈希表结构体
private struct bucket {<!-- -->
   public Object key;//键
    public Object val;//值
    public int hash_col;//哈希码
}
//字典结构体
private struct Entry {<!-- -->
    public int hashCode;    // 除符号位以外的31位hashCode值, 如果该Entry没有被使用，那么为-1
    public int next;        // 下一个元素的下标索引，如果没有下一个就为-1
    public TKey key;        // 存放元素的键
    public TValue value;    // 存放元素的值
}

private int[] buckets;      // Hash桶
private Entry[] entries;    // Entry数组，存放元素
private int count;          // 当前entries的index位置
private int version;        // 当前版本，防止迭代过程中集合被更改
private int freeList;       // 被删除Entry在entries中的下标index，这个位置是空闲的
private int freeCount;      // 有多少个被删除的Entry，有多少个空闲的位置
private IEqualityComparer&lt;TKey&gt; comparer;   // 比较器
private KeyCollection keys;     // 存放Key的集合
private ValueCollection values;     // 存放Value的集合



```

**性能排序：**
- 插入性能： LinkedList &gt; Dictionary &gt; HashTable &gt; List- 遍历性能：List &gt; LinkedList &gt; Dictionary &gt; HashTable- 删除性能： Dictionary &gt; LinkedList &gt; HashTable &gt; List
##### 18. C#中常规容器和泛型容器有什么区别，哪种效率高？

不带泛型的容器需要装箱和拆箱操作速度慢所以泛型容器效率更高数据类型更安全

##### 19. 有哪些常见的数值类？

简单值类型：包括 整数类型、实数类型、字符类型、布尔类型

复合值类型：包括 结构类型、枚举类型

##### 20. 泛型是什么

多个代码对 【不同数据类型】 执行 【相同指令】的情况 泛型：多个类型共享一组代码 泛型允许类型参数化，泛型类型是类型的模板 5种泛型：类、结构、接口、委托、方法 类型占位符 T 来表示泛型

泛型类不是实际的类，而是类的模板 从泛型类型创建实例 声明泛型类型》通过提供【真实类型】创建构造函数类型》从构造类型创建实例 类&lt;T1,T2&gt; 泛型类型参数

**性能**：泛型不会强行对值类型进行装箱和拆箱，或对引用类型进行向下强制类型转换，所以性能得到提高

**安全**：通过知道使用泛型定义的变量的类型限制，编译器可以在一定程度上验证类型假设，所以泛型提高了程序的类型安全。

##### 21. C#中unsafe关键字是用来做什么的？什么场合下使用？

非托管代码才需要这个关键字一般用在带指针操作的场合。 项目背包系统的任务装备栏使用到

##### 22. C#中ref和out关键字有什么区别？

**ref修饰引用参数**。参数必须赋值，在内部可改可不改，带回返回值，又进又出 **out修饰输出参数**。参数可以不赋值，在内部必须修改该值，带回返回值之前必须明确赋值。

引用参数和输出参数不会创建新的存储位置

如果ref参数是值类型，原先的值类型数据，会随着方法里的数据改变而改变， 如果ref参数值引用类型，方法里重新赋值后，原对象堆中数据会改变，如果对引用类型再次创建新对象并赋值给ref参数，引用地址会重新指向新对象堆数据。方法结束后形参和新对象都会消失。实参还是指向原始对象，值不够数据改变了

##### 23. For，foreach，Enumerator.MoveNext的使用，与内存消耗情况

for循环可以通过索引依次进行遍历，foreach和Enumerator.MoveNext通过迭代的方式进行遍历。 内存消耗上本质上并没有太大的区别。 但是在Unity中的Update中，一般不推荐使用foreach 因为会遗留内存垃圾。

##### 24. foreach迭代器遍历和for循环遍历的区别

如果集合需要foreach遍历，是否可行，存在一定问题 foreach中的迭代变量item是的只读，不能对其进行修改，比如list.Remove（item）操作 foreach只读的时候记录下来，在对记录做操作，或者直接用for循环遍历 foreach对int[]数组循环已经不产生GC，避免对ArrayList进行遍历

for语句中初始化变量i的作用域，循环体内部可见。 通过索引进行遍历，可以根据索引对所遍历集合进行修改 unity中for循环使用lambda表达式注意闭包问题

foreach遍历原理 任何集合类（Array）对象都有一个GetEnumerator()方法，该方法可以返回一个实现了 迭代器IEnumerator接口的对象。 这个返回的IEnumerator对象既不是集合类对象，也不是集合的元素类对象，它是一个独立的类对象。 通过这个实现了 IEnumerator接口对象A，可以遍历访问集合类对象中的每一个元素对象 对象A访问MoveNext方法，方法为真，就可以访问Current方法，读取到集合的元素。

```
	    List&lt;string&gt; list = new List&lt;string&gt;() {<!-- --> "25", "哈3", "26", "花朵" };
 		IEnumerator listEnumerator = list.GetEnumerator();
        while (listEnumerator.MoveNext())
        {<!-- -->
            Console.WriteLine(listEnumerator.Current);
        }

```

##### 25. Foreach循环迭代时，若把其中的某个元素删除，程序报错，怎么找到那个元素？以及具体怎么处理这种情况？(注：Try…Catch捕捉异常，发送信息不可行)

foreach不能进行元素的删除，因为迭代器会锁定迭代的集合，解决方法：记录找到索引或者key值，迭代结束后再进行删除。

##### 26. JIT和AOT区别

Just-In-Time -实时编译

执行慢安装快占空间小一点

Ahead-Of-Time -预先编译

执行快安装慢占内存占外存大

##### 27. 给定一个存放参数的数组，重新排列数组

void SortArray(Array arr){Array.Sort(arr);}

##### 28. 当需要频繁创建使用某个对象时，有什么好的程序设计方案来节省内存？

设计单例模式进行创建对象或者使用对象池

##### 29. C#的委托是什么?有何用处?

委托类似于一种安全的指针引用，在使用它时是 当做类来看待而不是一个方法，相当于对一组方 法的列表的引用，可以便捷的使用委托对这个方法集合进行操作。委托是对函数指针的封装。

用处：使用委托使程序员可以将方法引用封装在 委托对象内。然后可以将该委托对象传递给可调 用所引用方法的代码，而不必在编译时知道将调 用哪个方法。与C或C++中的函数指针不同，委托 是面向对象，而且是类型安全的。

##### 30. C#中 委托和事件的区别

大致来说，委托是一个类，该类内部维护着一个字段，指向一个方法。事件可以被看作一个委托类型的变量，通过事件注册、取消多个委托或方法。
- 委托可以用“=”来赋值，事件不可以。- 委托可以在声明它的类外部进行调用，而事件只能在类的内部进行调用。- 委托是一个类型，事件修饰的是一个对象。- 委托就是一个类，也可以实例化，通过委托的构造函数来把方法赋值给委托实例- 触发委托有2种方式: 委托实例.Invoke(参数列表)，委托实例(参数列表)- 事件可以看作是一个委托类型的变量- 通过+=为事件注册多个委托实例或多个方法- 通过-=为事件注销多个委托实例或多个方法- EventHandler就是一个委托
##### 31. C#中委托 和 接口有什么区别？各用在什么场合？

**接口（interface）** 是约束类应该具备的功能集合，约束了类应该具备的功能，使类从千变万化的具体逻辑中解脱出来，便于类的管理和扩展，同时又合理解决了类的单继承问题。

**C#中的委托** 是约束方法集合的一个类，可以便捷的使用委托对这个方法集合进行操作。

在以下情况中使用接口：

1.无法使用继承的场合 2.完全抽象的场合 3.多人协作的场合

以上等等

在以下情况中使用委托：多用于事件处理中

##### 32. 接口Interface与抽象类

**概念**

抽象类
1. 当2个或多个类中有重复部分的时候，我们可以抽象出来一个基类，如果希望这个基类不能被实例化，就可以把这个基类设计成抽象类。1. 当需要为一些类提供公共的实现代码时，应优先考虑抽象类。因为抽象类中的非抽象方法可以被子类继承下来，使实现功能的代码更简单。
接口
1. 当注重代码的扩展性跟可维护性时，应当优先采用接口。1. 接口与实现它的类之间可以不存在任何层次关系，接口可以实现毫不相关类的相同行为，比抽象类的使用更加方便灵活;1. 接口只关心对象之间的交互的方法，而不关心对象所对应的具体类。接口是程序之间的一个协议，比抽象类的使用更安全、清晰。一般使用接口的情况更多。
**区别**
1. 接口不是类（无构造函数和析构函数），不能被实例化，抽象类可以间接实例化（可以被继承，有构造函数，可以实例化子类的同时间接实例化抽象类这个父类）。1. 接口只能做方法申明，抽象类中可以做方法申明，也可以做方法实现。1. 抽象类中可以有实现成员，接口只能包含抽象成员。因此接口是完全抽象，抽象类是部分抽象。1. 抽象类要被子类继承，接口要被类实现。1. 抽象类中所有的成员修饰符都能使用，接口中的成员都是对外的，所以不需要修饰符修饰。1. 接口可以实现多继承，抽象类只能实现单继承，一个类只能继承一个类但可以实现多个接口。1. 抽象方法要被实现，所以不能是静态的，也不能是私有的。
**使用情形**
- 使用抽象类是为了代码的复用，而使用接口的动机是为了实现多态性。- 抽象类适合用来定义某个领域的固有属性，也就是本质，接口适合用来定义某个领域的扩展功能。
##### 33. 函数中多次使用string的+=处理，会产生大量内存垃圾（垃圾碎片），有什么好的方法可以解决。

通过StringBuilder那进行append，这样可以减少内存垃圾

##### 34. C#和C++的区别?

简单的说:C# 与C++ 比较的话，最重要的特性 就是C# 是一种完全面向对象的语言，而C++ 不 是，另外C# 是基于IL 中间语言 和.NET Framework CLR 的，在可移植性，可维 护性和强壮性都比C++ 有很大的改进。C# 的设 计目标是用来开发快速稳定可扩展的应用程序， 当然也可以通过Interop和Pinvoke 完成一些底层操作

**具体对比**：
1. 继承：C++支持多继承，C#类只能继承一个基类中的实现但可以实现多个接口。1. 数组：声明 C# 数组和声明 C++ 数组的语法不同。在 C# 中，“[]”标记出现在数组类型的后面。1. 数据类型：在C++中bool类可以与整型转换，但C#中bool 类型和其他类型（特别是 int）之间没有转换。long 类型：在 C# 中，long 数据类型为 64 位，而在 C++ 中为 32 位。1. struct 类型：在 C# 中，类和结构在语义上不同。struct 是值类型，而 class 是引用类型。1. switch 语句：与 C++ 中的 switch 语句不同，C# 不支持从一个 case 标签贯穿到另一个 case 标签。1. delegate 类型：委托与 C++ 中的函数指针基本相似，但前者具有类型安全，是安全的。1. 从派生类调用重写基类成员。 base1. 使用 new 修饰符显式隐藏继承成员。1. 重写方法需要父类方法中用virtual声名，子类方法用override 关键字。1. 预处理器指令用于条件编译。C# 中不使用头文件。 C# 预处理器指令1. 异常处理：C#中引入了 finally 语句，这是C++没有的。1. C# 运算符：C# 支持其他运算符，如 is 和 typeof。它还引入了某些逻辑运算符的不同功能。1. static 的使用，static方法只能由类名调用，改变static变量。1. 在构造基类上替代 C++ 初始化列表的方法。1. Main 方法和 C++ 及Java中的 main 函数的声明方式不同，Main而不能用main1. 方法参数：C# 支持 ref 和 out 参数，这两个参数取代指针通过引用传递参数。1. 在 C# 中只能在unsafe不安全模式下才使用指针。1. 在 C# 中以不同的方式执行重载运算符。1. 字符串：C# 字符串不同于 C++ 字符串。1. foreach:C#從VB中引入了foreach关键字使得以循环访问数组和集合。1. C# 中没有全局方法和全局变量：方法和变量必须包含在类型声明（如 class 或 struct）中。1. C# 中没有头文件和 #include 指令：using 指令用于引用其他未完全限定类型名的命名空间中的类型。1. C# 中的局部变量在初始化前不能使用。1. 析构函数：在 C# 中，不能控制析构函数的调用时间，原因是析构函数由垃圾回收器自动调用。 析构函数1. 构造函数：与 C++ 类似，如果在 C# 中没有提供类构造函数，则为您自动生成默认构造函数。该默认构造函数将所有字段初始化为它们的默认值。1. 在 C# 中，方法参数不能有默认值。如果要获得同样的效果，需使用方法重载。
##### 35. C#引用和C++指针的区别

C#不支持指针，但可以使用Unsafe，不安全模式，CLR不检测 C#可以定义指针的类型、整数型、实数型、struct结构体 C#指针操作符、C#指针定义 使用fixed，可以操作类中的值类型 相同点：都是地址 指针指向一块内存，它的内容是所指内存的地址；而引用则是某块内存的别名。

**不同点**：
- 指针是个实体，引用是个别名。- sizeof 引用”得到的是所指向的变量(对象)的大小，而“sizeof 指针”得到的是指针本身的大小；- 引用是类型安全的，而指针在不安全模式下- 引用不能为空，即不存在对空对象的引用，指针可以为空，指向空对象。- 引用必须初始化，指定对哪个对象的引用，指针不需要。- 引用初始化后不能改变，指针可以改变所指对象的值。- 引用访问对象是直接访问，指针访问对象是间接访问。- 引用的大小是所引用对象的大小，指针的大小，是指针本身大小，通常是4字节。- 引用没有const，指针有const- 引用和指针的+自增运算符意义不同。- 引用不需要分配内存空间，指针需要。
##### 36. 反射的实现原理？

可以在加载程序运行时，动态获取和加载程序集，并且可以获取到程序集的信息反射即在运行期动态获取类、对象、方法、对象数据等的一种重要手段。

主要使用的类库：System.Reflection

**核心类：**
1. Assembly描述了程序集1. Type描述了类这种类型1. ConstructorInfo描述了构造函数1. MethodInfo描述了所有的方法1. FieldInfo描述了类的字段1. PropertyInfo描述类的属性
通过以上核心类可在运行时动态获取程序集中的类，并执行类构造产生类对象，动态获取对象的字段或属性值，更可以动态执行类方法和实例方法等。

审查元数据并收集关于它的类型信息的能⼒。

```
实现步骤：
1. 导⼊using System.Reflection;
2. Assembly.Load("程序集")加载程序集,返回类型是
⼀个Assembly
3.  foreach (Type type in assembly.GetTypes())
         {<!-- -->
            string t = type.Name;
         }
得到程序集中所有类的名称
4. Type type = assembly.GetType("程序集.类名");获取
当前类的类型
5. Activator.CreateInstance(type); 创建此类型实例
6. MethodInfo mInfo = type.GetMethod("⽅法名");获取
当前⽅法
7. mInfo.Invoke(null,⽅法参数);

```

##### 37. C#中基本类型占用的字节数

|类型|字节
|------
|bool|true/false
|byte、char|1字节
|char、short|2字节
|int，float|4字节
|long、double|8字节

##### 38. Mock和Stub有何区别?

Mock与Stub的区别:Mock:关注行为验证。细粒度的 测试，即代码的逻辑，多数情况下用于单元测试。 Stub:关注状态验证。粗粒度的测试，在某个依赖系 统不存在或者还没实现或者难以测试的情况下使用， 例如访问文件系统，数据库连接，远程协议等。

##### 39. 为什么dynamic font 在 unicode环境下优于 staticfont（字符串编码）

Unicode是国际组织制定的可以容纳世界上所有⽂字和符号的字符编码⽅案。 使⽤动态字体时，Unity将不会预先⽣成⼀个与所有字体的字符纹理。 当需要⽀持亚洲语⾔或者较⼤的字体的时候，若使⽤正常纹理，则字体的纹理将⾮常⼤。

##### 40. 简述StringBuilder和String的区别？（字符串处理）

String是字符串常量。StringBuilder是字符串变量，线程不安全。

String类型是个不可变的对象，当每次对String进⾏改变时都需要⽣成⼀个新的String对象，然后将指针指向⼀个新的对象，如果在⼀个循环⾥⾯，不断的改变⼀个对象，就要不断的⽣成新的对象，所以效率很低，建议在不断更改String对象的地⽅不要使⽤String类型。

StringBuilder对象在做字符串连接操作时是在原来的字符串上进⾏修改，改善了性能。这⼀点我们平时使⽤中也许都知道，连接操作频繁的时候，使⽤StringBuilder对象。

##### 41. string、stringBuilder
-  **String**不变性，字符序列不可变，对原管理中实例对象赋值，会重新开一个新的实例对象赋值，新开的实例对象会等待被GC。 string拼接要重新开辟空间，因为string原值不会改变，导致GC频繁，性能消耗大。 -  **StringBuilder**是字符串可变对象。 StringBuilder是非线程安全，所以性能略好，一般用于单线程。 
性能比较 StringBuilder&gt;String
1. 如果要操作少量的数据 =string1. 单线程操作字符串缓冲区 下操作大量数据 = StringBuilder
##### 42. 字典Dictionary的内部实现原理

泛型集合命名空间using System.Collections.Generic; 任何键都必须是唯一

该类最大的优点就是它查找元素的时间复杂度接近O(1)，实际项目中常被用来做一些数据的本地缓存，提升整体效率。

**实现原理**
1. 哈希算法：将不定长度的二进制数据集给映射到一个较短的二进制长度数据集一个Key通过HashFunc得到HashCode1. Hash桶算法：对HashCode进行分段显示，常用方法是对HashCode直接取余1. 解决碰撞冲突算法（拉链法）：分段会导致key对应的桶会相同，拉链法的思想就像对冲突的元素，建立一个单链表，头指针存储到对应的哈希桶位置。反之就是通过确定hash桶位置后，遍历单链表，获取对应的value
##### 43.using的作用

资源：实现了IDisposable接口的类或结构。 using语句确保这些资源能够被适当的释放（Resource.Dispose） using原理：using（分配资源）{ 使用资源 } ——&gt; 释放资源 （隐式） 使用资源（可能会导致异常）会被放进Try块里，释放资源（有无异常）都会放进在finally块

```
using（分配资源）
{<!-- -->
	try{<!-- --> 使用资源 }
	finally{<!-- --> Resource.Dispose}
}

```

using指令,using+命名空间（或命名空间一个类型） 在源文件的顶端声明 调用成员方法时也可以不使用using，直接命名空间.类.成员方法

##### 44. Mathf.Round和Mathf.Clamp和Mathf.Lerp含义？
- Mathf.Round：四舍五入- Mathf.Clamp：左右限值- Mathf.Lerp：插值
##### 45. 能用foreach遍历访问的对象需要实现___接⼝或声明___⽅法的类型（C#遍历）

IEnumerable；GetEnumerator

List和Dictionary类型可以用foreach遍历，他们都实现了IEnumerable接口，申明了GetEnumerator方法。 <img src="https://img-blog.csdnimg.cn/920c06dd780f4f0f81db839c2a2032ee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5ZGG5ZGG5pWy5Luj56CB55qE5bCPWQ==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 46. 什么是里氏替换原则？（C#多态）

里氏替换原则(Liskov Substitution Principle LSP)⾯向对象设计的基本原则之⼀。
- 里氏替换原则中说，任何基类可以出现的地⽅，⼦类⼀定可以出现，作⽤⽅便扩展功能能- 子类可以实现父类的抽象方法，但是不能覆盖父类的非抽象方法。- 子类中可以增加自己特有的方法。- 当子类覆盖或实现父类的方法时，方法的前置条件（即方法的形参）要比父类方法的输入参数更宽松。- 当子类的方法实现父类的抽象方法时，方法的后置条件（即方法的返回值）要比父类更严格。
##### 47. 想要在for循环中删除List（或者vector，都行）中的元素时，有可能出现什么问题，如何避免？

当删除遍历节点后面的节点时，会导致List.Count进行变化，删除元素后，当根据i++，遍历到删除的节点会发生异常。

处理方法：可以从后往前遍历元素进行操作，即删除在访问的前面。

##### 48. 概述c#中代理和事件？

代理就是⽤来定义指向⽅法的引⽤。 C＃事件本质就是对消息的封装，⽤作对象之间的通信；发送⽅叫事件发送器，接收⽅叫事件接收器；

##### 49. New的实现逻辑

rPoint1 = new RefPoint(1);
1. 在应用程序堆上创建一个引用类型对象的实例，并为它分配内存地址。1. 自动传递该实例的引用给构造函数(正因如此，在构造函数中才能使用this来访问这个实例)。1. 调用该类型的构造函数。1. 返回该实例的引用内存地址，复制给 rPoint1 变量，该rPoint1 引用对象保存的数据是指向在堆上创建该类型的实例地址。
##### 50.请简述关键字Sealed用在类声明和函数声明时的作用

类声明时可防止其他类继承此类，在方法中声明则可防止派生类重写此方法。

##### 51. 下列代码在运行中会发生什么问题？如何避免？

```
List&lt;int&gt; ls = new List&lt;int&gt;(new int[]{<!-- --> 1, 2, 3, 4, 5 });
         foreach (int item in ls)
         {<!-- -->
             Console.WriteLine(item * item);
             ls.Remove(item);
         }

```

会产⽣运⾏时错误，因为foreach是只读的。不能⼀边遍历⼀边修改。

使用For循环遍历可以解决。

##### 52. 什么是装箱拆箱，怎样减少操作

C#装箱是将值类型转换为引用类型； 拆箱是将引用类型转换为值类型。 牵扯到装箱和拆箱操作比较多的就是在集合中，例如：ArrayList或者HashTable之类。

值类型和引用类型互相转换：拆箱和装箱 装箱：值类型====》引用类型object
1. 分配内存堆1. 值类型数据拷贝到新的内存堆中1. 栈中分配一个新的引用地址指向内存堆
拆箱：引用类型object====》值类型
1. 检查确保对象是给定值类型的一个装箱值1. 将该值数据复制到栈中的值类型
##### 53. MVC

MVC全名是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范。

用一种业务逻辑、数据、界面显示分离的方法，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。MVC被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面的结构中。
- Model（模型）是应用程序中用于处理应用程序数据逻辑的部分。 　　通常模型对象负责在数据库中存取数据。- View（视图）是应用程序中处理数据显示的部分。 　　通常视图是依据模型数据创建的。- Controller（控制器）是应用程序中处理用户交互的部分。 　　通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据
##### 54. 非托管代码与不安全代码

**托管代码**: 在公共语言运行时(CLR)控制下运行的代码。

**非托管代码**: 不在公共语言运行时(CLR)控制下运行的代码。

**不安全(Unsafe)代码**: 不安全代码可以被认为是介于托管代码和非托管代码之间的。不安全代码仍然在公共语言运行时(CLR)控制下运行，但它将允许您直接通过指针访问内存。

##### 55. C#中基本类型占用的字节数

|类型|字节
|------
|bool|true/false
|byte、char|1字节
|char、short|2字节
|int，float|4字节
|long、double|8字节

##### 56. Heap与Stack有何区别?
1. heap是堆，stack是栈。1. stack的空间由操作系统自 动分配和释放，heap的空间是手动申请和释放的， heap常用new关键字来分配。1. stack空间有限，heap 的空间是很大的自由区。
##### 57. 栈溢出一般是由什么原因导致
1. 无限递归。函数递归调用时，系统要在栈中不断保存函数调用时的现场和产生的变量，如果递归调用太深，就会造成栈溢出，这时递归无法返回。再有，当函数调用层次过深时也可能导致栈无法容纳这些调用的返回地址而造成栈溢出。1. 无限循环。1. 大量局部变量分配。
##### 58. Stack栈和Queue队列

**相同点：**
1. 都是线性结构。1. 插入操作都是限定在表尾进行。1. 都可以通过顺序结构和链式结构实现。1. 插入与删除的时间复杂度都是O（1），在空间复杂度上两者也一样。1. 多链栈和多链队列的管理模式可以相同。1. 底层都是由泛型数组实现。
**不同点：**
1. 栈先进后出，队列先进先出：删除数据元素的位置不同，栈的删除操作在表尾进行，队列的删除操作在表头进行。1. 顺序栈能够实现多栈空间共享，而顺序队列不能。1. 应用场景不同
常见栈的应用场景包括
1. 括号问题的求解，1. 深度优先搜索遍历等；1. 函数调用和递归实现，1. 表达式的转换和求值
常见的队列的应用场景包括
1. 计算机系统中各种资源的管理，1. 消息缓冲器的管理1. 广度优先搜索遍历等
##### 59. 链表相关

**单双向链表的区别：**
- 指向不同：单向链表只有一个指向下一结点的指针，双向链表除了有一个指向下一结点的指针外，还有一个指向前一结点的指针。- 功能不同：单向链表只能next ，双向链表可以return。- 单双向不同：单链表只能单向读取，双向链表可以双向遍历。
**单向链表优缺点：**

优点：单向链表增加删除节点简单。遍历时候不会死循环； 缺点：只能从头到尾遍历。只能找到后继，无法找到前驱，也就是只能前进。

**双向链表优缺点：** 优点：可以找到前驱和后继，可进可退； 缺点：增加删除节点复杂，多需要分配一个指针存储空间。

##### 60. 链表与数组的对比
1. 数组必须事先定义固定的长度（元素个数），不能适应数据动态地增减的情况。当数据增加时，可能超出原先定义的元素个数；当数据减少时，造成内存浪费；数组可以根据下标直接存取，时间复杂度O(1)。1. 链表动态地进行存储分配，可以适应数据动态地增减的情况，且可以方便地插入、删除数据项。（数组中插入、删除数据项时，需要移动其它数据项，非常繁琐）链表必须根据next指针找到下一个元素。
如果需要快速访问数据，很少或不插入和删除元素，就应该用数组；相反，如果需要经常插入和删除元素就需要用链表数据结构了。

##### 61. 二叉树相关

**计算深度（高度）** 二叉树的高度是二叉树结点层次的最大值，也就是其左右子树的最大高度+1。当树为空时，高度为0；否则为其左右子树最大高度+1。

**遍历:（看根节点的位置）**
- 前序遍历：（根左右）先访问根节点，再访问左节点，再访问右节点。- 中序遍历：（左根右）先访问左节点，再访问根节点，再访问右节点。- 后序遍历：（左右根）先访问左节点，再访问右节点，再访问根节点。
##### 62. 字典相关

**介绍**
1. Dictionary表示键和值的集合。1. Dictionary&lt;object, object&gt;是一个泛型。1. 他本身有集合的功能有时候可以把它看成数组。1. 他的结构是这样的：Dictionary&lt;[key], [value]&gt;。1. 他的特点是存入对象是需要与[key]值一一对应的存入该泛型，任何键都是唯一。1. 通过某一个一定的[key]去找到对应的值。查找元素的时间复杂度为O(1)。
增删查改时间复杂度
- Dictionary字典类是hash表，Add操作是O(1)。- 其Containskey方法是O(1)，原因是通过hash来查找元素而不是遍历元素。- ContainsValue方法的时间复杂度是O(N)，原因是内部通过遍历key来查找value，而不是通过hash来查找。- ltem[Key]属性根据key来检索value，其时间复杂度也是O(1)。 基本都是O（1）
**底层实现原理** Dictionary在构造的时候做了以下几件事： 1.初始化一个桶数组this.buckets = new int[prime] 2.初始化一个this.entries = new Entry&lt;TKey, TValue&gt;[prime]

Bucket和entries的容量都为大于字典容量的一个最小的质数 其中this.buckets主要用来进行Hash碰撞

this.entries用来存储字典的内容，并且标识下一个元素的位置。

**详细过程**
1. 哈希表法：将不定长的二进制数据集映射到一个较短的二进制数据集，一个Key通过HashFunc得到HashCode。1. Hash桶算法：对HashCode进行分段显示，常用方法对HashCode直接取余。1. 拉链法：分段则会导致key对应的哈希桶相同，拉链法的基本思想就像对冲突的元素，建立一个单链表，头指针存储在对应哈希桶的位置。反之就是通过hash桶对应后，遍历单链表，获取value值。
##### 63. 哈希表与字典对比

**字典**：内部用了Hashtable作为存储结构
- 如果我们试图找到一个不存在的键，它将返回 / 抛出异常。- 它比哈希表更快，因为没有装箱和拆箱，尤其是值类型。- 仅公共静态成员是线程安全的。- 字典是一种通用类型，这意味着我们可以将其与任何数据类型一起使用（创建时，必须同时指定键和值的数据类型）。- Dictionay 是 Hashtable 的类型安全实现， Keys和Values是强类型的。- Dictionary遍历输出的顺序，就是加入的顺序
**哈希表**：
- 如果我们尝试查找不存在的键，则返回 null。- 它比字典慢，因为它需要装箱和拆箱。- 哈希表中的所有成员都是线程安全的，- 哈希表不是通用类型，- Hashtable 是松散类型的数据结构，我们可以添加任何类型的键和值。- HashTable是经过优化的，访问下标的对象先散列过，所以内部是无序散列的
##### 64.关于List与字典的遍历与查询效率
1.  List的底层，是一个泛型数组，连续且紧密的顺序存储，一般数据存储在缓存中。而字典是离散（散列）分布，由数组和哈希表共同组成，遍历的时候，会伴有换页的操作，且数组都存储在内存中。而读写速度是：缓存&gt;内存&gt;硬盘。因此List更适合遍历。 1.  字典的查询效率是通过元素的key值进行取余操作，找的对应的哈希桶，判定哈希桶对应的哈希表的头节点是不是该元素，若不是进行next操作，对哈希表进行遍历，这两个过程都是常数级别的操作。所以是O（1）。而List的查询效率是先遍历，找到对应的值，因此是O（n）。所以字典更适合查询。 
<img src="https://img-blog.csdnimg.cn/740dc5634e3847c6a1a576de5cae82a7.png" alt="请添加图片描述">

<font color="#ff6984" size="5"> **资料白嫖，技术互助**</font> <img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创 🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


|学习路线指引（点击解锁）|知识定位|人群定位
|------
||入门级|本专栏从Unity入门开始学习，快速达到Unity的入门水平
||进阶级|计划制作Unity的 100个实战案例！助你进入Unity世界，争取做最全的Unity原创博客大全。
||难度偏高|分享学习一些Unity成品的游戏Demo和其他语言的小游戏！
||互助/吹水|数万人游戏爱好者社区，聊天互助，白嫖奖品
||Unity查漏补缺|针对一些Unity中经常用到的一些小知识和技能进行学习介绍，核心目的就是让我们能够快速学习Unity的知识以达到查漏补缺

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
