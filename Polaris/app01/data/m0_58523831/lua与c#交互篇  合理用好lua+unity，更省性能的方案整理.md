
--- 
title:  lua与c#交互篇 | 合理用好lua+unity，更省性能的方案整理 
tags: []
categories: [] 

---
#### 前言

在看了uwa之前发布的《Unity项目常见Lua解决方案性能比较》，决定动手写一篇关于lua+unity方案的性能优化文。

整合lua是目前最强大的unity热更新方案，毕竟这是唯一可以支持ios热更新的办法。然而作为一个重度ulua用户，我们踩过了很多的坑才将ulua上升到一个可以在项目中大规模使用的状态。事实上即使到现在lua+unity的方案仍不能轻易的说可以肆意使用，要用好，你需要知道很多。

因此，这篇文章是从一堆简单的优化建议里头，逐步挖掘出背后的原因。只有理解了原因，才能很清楚自己做的优化，到底是为了什么，有多大的效果。

从最早的lua纯反射调用c#，以及云风团队尝试的纯c#实现的lua虚拟机，一直发展到现在的各种luajit+c#静态lua导出方案，lua+unity才算达到了性能上实用的级别。

但即使这样，实际使用中我们会发现，比起cocos2dx时代luajit的发扬光大，现在lua+unity的性能依然存在着相当的瓶颈。仅从《性能比较》的test1就可以看到，iphone4s下二十万次position赋值就已经需要3000ms，如果是coc这样类型的游戏，不处理其他逻辑，一帧仅仅上千次位置赋值（比如数百的单位、特效和血条）就需要15ms，这显然有些偏高。

是什么导致lua+unity的性能并未达到极致，要如何才能更好的使用？我们会一些例子开始，逐步挖掘背后的细节。

由于我们项目主要使用的是ulua（集成了topameng的cstolua，但是由于持续的性能改进，后面已经做过大量的修改），本文的大部分结论都是基于ulua+cstolua的测试得出来的，slua都是基于其源码来分析（根据我们分析的情况来看，两者原理上基本一致，仅在实现细节上有一些区别），但没有做过深入测试，如有问题的话欢迎交流。

既然是lua+unity，那性能好不好，基本上要看两大点：
- lua跟c#交互时的性能如何- 纯lua代码本身的性能如何
因为这两部分都各有自己需要深入探讨的地方，所以我们会分为多篇去探讨整个lua+unity到底如何进行优化。

### lua与c#交互篇

##### 1.从致命的gameobj.transform.position = pos开始说起

像gameobj.transform.position = pos这样的写法，在unity中是再常见不过的事情

但是在ulua中，大量使用这种写法是非常糟糕的。为什么呢？

因为短短一行代码，却发生了非常非常多的事情，为了更直观一点，我们把这行代码调用过的关键luaapi以及ulua相关的关键步骤列出来（以ulua+cstolua导出为准，gameobj是GameObject类型，pos是Vector3）：

**第一步：**

|步骤|含义
|------
|GameObjectWrap.get_transform|lua想从gameobj拿到transform，对应gameobj.transform
|LuaDLL.luanet_rawnetobj|把lua中的gameobj变成c#可以辨认的id
|ObjectTranslator.TryGetValue|用这个id，从ObjectTranslator中获取c#的gameobject对象
|gameobject.transform|准备这么多，这里终于真正执行c#获取gameobject.transform了
|ObjectTranslator.AddObject|给transform分配一个id，这个id会在lua中用来代表这个transform，transform要保存到ObjectTranslator供未来查找
|LuaDLL.luanet_newudata|在lua分配一个userdata，把id存进去，用来表示即将返回给lua的transform
|LuaDLL.lua_setmetatable|给这个userdata附上metatable，让你可以transform.position这样使用它
|LuaDLL.lua_pushvalue|返回transform，后面做些收尾
|LuaDLL.lua_rawseti|
|LuaDLL.lua_remove|

**第二步：**
- TransformWrap.set_position : lua想把pos设置到transform.position- LuaDLL.luanet_rawnetobj : 把lua中的transform变成c#可以辨认的id- ObjectTranslator.TryGetValue : 用这个id，从ObjectTranslator中获取c#的transform对象- LuaDLL.tolua_getfloat3 : 从lua中拿到Vector3的3个float值返回给c#- lua_getfield + lua_tonumber 3次 : 拿xyz的值，退栈- lua_pop- transform.position = new Vector3(x,y,z) 准备了这么多，终于执行transform.position = pos赋值了
就这么一行代码，竟然做了这么一大堆的事情！如果是c++，a.b.c = x这样经过优化后无非就是拿地址然后内存赋值的事。但是在这里，频繁的取值、入栈、c#到lua的类型转换，每一步都是满满的cpu时间，还不考虑中间产生了各种内存分配和后面的GC！

下面我们会逐步说明，其中有一些东西其实是不必要的，可以省略的。我们可以最终把他优化成：

lua_isnumber + lua_tonumber 4次，全部完成

##### 2.在lua中引用c#的object，代价昂贵

从上面的例子可以看到，仅仅想从gameobj拿到一个transform，就已经有很昂贵的代价

c#的object，不能作为指针直接供c操作（其实可以通过GCHandle进行pinning来做到，不过性能如何未测试，而且被pinning的对象无法用gc管理），因此主流的lua+unity都是用一个id表示c#的对象，在c#中通过dictionary来对应id和object。同时因为有了这个dictionary的引用，也保证了c#的object在lua有引用的情况下不会被垃圾回收掉。

因此，每次参数中带有object，要从lua中的id表示转换回c#的object，就要做一次dictionary查找；每次调用一个object的成员方法，也要先找到这个object，也就要做dictionary查找。

如果之前这个对象在lua中有用过而且没被gc，那还就是查下dictionary的事情。但如果发现是一个新的在lua中没用过的对象，那就是上面例子中那一大串的准备工作了。

如果你返回的对象只是临时在lua中用一下，情况更糟糕！刚分配的userdata和dictionary索引可能会因为lua的引用被gc而删除掉，然后下次你用到这个对象又得再次做各种准备工作，导致反复的分配和gc，性能很差。

例子中的gameobj.transform就是一个巨大的陷阱，因为.transform只是临时返回一下，但是你后面根本没引用，又会很快被lua释放掉，导致你后面每次.transform一次，都可能意味着一次分配和gc。

##### 3.在lua和c#间传递unity独有的值类型（Vector3/Quaternion等）更加昂贵

既然前面说了lua调用c#对象缓慢，如果每次vector3.x都要经过c#，那性能基本上就处于崩溃了，所以主流的方案都将Vector3等类型实现为纯lua代码，Vector3就是一个{x,y,z}的table，这样在lua中使用就快了。

但是这样做之后，c#和lua中对Vector3的表示就完全是两个东西了，所以传参就涉及到lua类型和c#类型的转换，例如c#将Vector3传给lua，整个流程如下：
1. c#中拿到Vector3的x,y,z三个值1. push这3个float给lua栈1. 然后构造一个表，将表的x,y,z赋值1. 将这个表push到返回值里
一个简单的传参就要完成3次push参数、表内存分配、3次表插入，性能可想而知。

那么如何优化呢？我们的测试表明，直接在函数中传递三个float，要比传递Vector3要更快。

例如void SetPos(GameObject obj, Vector3 pos)改为void SetPos(GameObject obj, float x, float y, float z)

具体效果可以看后面的测试数据，提升十分明显。

##### 4.lua和c#之间传参、返回时，尽可能不要传递以下类型：
- 严重类： Vector3/Quaternion等unity值类型，数组- 次严重类：bool string 各种object- 建议传递：int float double
虽然是lua和c#的传参，但是从传参这个角度讲，lua和c#中间其实还夹着一层c（毕竟lua本身也是c实现的），lua、c、c#由于在很多数据类型的表示以及内存分配策略都不同，因此这些数据在三者间传递，往往需要进行转换（术语parameter mashalling），这个转换消耗根据不同的类型会有很大的不同。

先说次严重类中的bool string类型，涉及到c和c#的交互性能消耗，根据微软官方文档，在数据类型的处理上，c#定义了Blittable Types和Non-Blittable Types，其中bool和string属于Non-Blittable Types，意思是他们在c和c#中的内存表示不一样，意味着从c传递到c#时需要进行类型转换，降低性能，而string还要考虑内存分配（将string的内存复制到托管堆，以及utf8和utf16互转）。

可以参考，这里有更详细的关于c和c#交互的性能优化指引。

而严重类，基本上是ulua等方案在尝试lua对象与c#对象对应时的瓶颈所致。

Vector3等值类型的消耗，前面已经有所提及。

而数组则更甚，因为lua中的数组只能以table表示，这和c#下完全是两码事，没有直接的对应关系，因此从c#的数组转换为lua table只能逐个复制，如果涉及object/string等，更是要逐个转换。

##### 5.频繁调用的函数，参数的数量要控制

无论是lua的pushint/checkint，还是c到c#的参数传递，参数转换都是最主要的消耗，而且是逐个参数进行的，因此，lua调用c#的性能，除了跟参数类型相关外，也跟参数个数有很大关系。一般而言，频繁调用的函数不要超过4个参数，而动辄十几个参数的函数如果频繁调用，你会看到很明显的性能下降，手机上可能一帧调用数百次就可以看到10ms级别的时间。

##### 6.优先使用static函数导出，减少使用成员方法导出

前面提到，一个object要访问成员方法或者成员变量，都需要查找lua userdata和c#对象的引用，或者查找metatable，耗时甚多。直接导出static函数，可以减少这样的消耗。

像obj.transform.position = pos。

我们建议的方法是，写成静态导出函数，类似

```
class LuaUtil{<!-- -->
	static void SetPos(GameObject obj, float x, float y, float z)
	{<!-- -->
  		obj.transform.position = new Vector3\(x, y, z); 
	}
}

```

然后在lua中LuaUtil.SetPos(obj, pos.x, pos.y, pos.z)，这样的性能会好非常多，因为省掉了transform的频繁返回，而且还避免了transform经常临时返回引起lua的gc。

##### 7.注意lua拿着c#对象的引用时会造成c#对象无法释放，这是内存泄漏常见的起因

前面说到，c# object返回给lua，是通过dictionary将lua的userdata和c# object关联起来，只要lua中的userdata没回收，c# object也就会被这个dictionary拿着引用，导致无法回收。

最常见的就是gameobject和component，如果lua里头引用了他们，即使你进行了Destroy，也会发现他们还残留在mono堆里。

不过，因为这个dictionary是lua跟c#的唯一关联，所以要发现这个问题也并不难，遍历一下这个dictionary就很容易发现。ulua下这个dictionary在ObjectTranslator类、slua则在ObjectCache类

##### 8.考虑在lua中只使用自己管理的id，而不直接引用c#的object

想避免lua引用c# object带来的各种性能问题的其中一个方法就是自己分配id去索引object，同时相关c#导出函数不再传递object做参数，而是传递int。

这带来几个好处：
1. 函数调用的性能更好；1. 明确地管理这些object的生命周期，避免让ulua自动管理这些对象的引用，如果在lua中错误地引用了这些对象会导致对象无法释放，从而内存泄露1. c#object返回到lua中，如果lua没有引用，又会很容易马上gc，并且删除ObjectTranslator对object的引用。自行管理这个引用关系，就不会频繁发生这样的gc行为和分配行为。
例如，上面的LuaUtil.SetPos(GameObject obj, float x, float y, float z)可以进一步优化为LuaUtil.SetPos(int objID, float x, float y, float z)。然后我们在自己的代码里头记录objID跟GameObject的对应关系，如果可以，用数组来记录而不是dictionary，则会有更快的查找效率。如此下来可以进一步省掉lua调用c#的时间，并且对象的管理也会更高效。

##### 9.合理利用out关键字返回复杂的返回值

在c#向lua返回各种类型的东西跟传参类似，也是有各种消耗的。 比如

```
Vector3 GetPos(GameObject obj)

```

可以写成

```
void GetPos(GameObject obj, out float x, out float y, out float z)

```

表面上参数个数增多了，但是根据生成出来的导出代码（我们以ulua为准），会从： LuaDLL.tolua_getfloat3（内含get_field + tonumber 3次） 变成 isnumber + tonumber 3次

get_field本质上是表查找，肯定比isnumber访问栈更慢，因此这样做会有更好的性能。

#### 实测

好了，说了这么多，不拿点数据来看还是太晦涩

为了更真实地看到纯语言本身的消耗，我们直接没有使用例子中的gameobj.transform.position，因为这里头有一部分时间是浪费在unity内部的。

我们重写了一个简化版的GameObject2和Transform2。

```
class Transform2{<!-- -->
  public Vector3 position = new Vector3();
}

class GameObject2{<!-- -->
   public Transform2 transform = new Transform2();
}

```

然后我们用几个不同的调用方式来设置transform的position
- 方式1：gameobject.transform.position = Vector3.New(1,2,3)- 方式2：gameobject:SetPos(Vector3.New(1,2,3))- 方式3：gameobject:SetPos2(1,2,3)- 方式4：GOUtil.SetPos(gameobject, Vector3.New(1,2,3))- 方式5：GOUtil.SetPos2(gameobjectid, Vector3.New(1,2,3))- 方式6：GOUtil.SetPos3(gameobjectid, 1,2,3)
分别进行1000000次，结果如下（测试环境是windows版本，cpu是i7-4770，luajit的jit模式关闭，手机上会因为luajit架构、il2cpp等因素干扰有所不同，但这点我们会在下一篇进一步阐述）：

<img src="https://img-blog.csdnimg.cn/img_convert/68f31248049f35ce228e09e2cd5bfbbc.png" alt="">
- 方式1：903ms- 方式2：539ms- 方式3：343ms- 方式4：559ms- 方式5：470ms- 方式6：304ms
可以看到，每一步优化，都是提升明显的，尤其是移除.transform获取以及Vector3转换提升更是巨大，我们仅仅只是改变了对外导出的方式，并不需要付出很高成本，就已经可以节省66%的时间。

实际上能不能再进一步呢？还能！在方式6的基础上，我们可以再做到只有200ms！

这里卖个关子，下一篇luajit集成中我们进一步讲解。一般来说，我们推荐做到方式6的水平已经足够。

这只是一个最简单的案例，有很多各种各样的常用导出（例如GetComponentsInChildren这种性能大坑，或者一个函数传递十几个参数的情况）都需要大家根据自己使用的情况来进行优化，有了我们提供的lua集成方案背后的性能原理分析，应该就很容易去考虑怎么做了。

附测试用例的c#代码：

```
public class Transform2
{<!-- -->
    public Vector3 position = new Vector3();
}

public class GameObject2
{<!-- -->
    public Transform2 transform = new Transform2();
    public void SetPos(Vector3 pos)
    {<!-- -->
        transform.position = pos;
    }

    public void SetPos2(float x, float y, float z)
    {<!-- -->
        transform.position.x = x;
        transform.position.y = y;
        transform.position.z = z;
    }
}

 
public class GOUtil
{<!-- -->
    private static List&lt;GameObject2&gt; mObjs = new List&lt;GameObject2&gt;();
    public static GameObject2 GetByID(int id)
    {<!-- -->
        if(mObjs.Count == 0)
        {<!-- -->
            for (int i = 0; i &lt; 1000; i++ )
            {<!-- -->
                mObjs.Add(new GameObject2());
            }
        }

        return mObjs[id];
    }

    public static void SetPos(GameObject2 go, Vector3 pos)
    {<!-- -->
        go.transform.position = pos;
    }

    public static void SetPos2(int id, Vector3 pos)
    {<!-- -->
        mObjs[id].transform.position = pos;
    }

    public static void SetPos3(int id, float x, float y ,float z)
    {<!-- -->
        var t = mObjs[id].transform;
        t.position.x = x;
        t.position.y = y;
        t.position.z = z;
    }

}

```
