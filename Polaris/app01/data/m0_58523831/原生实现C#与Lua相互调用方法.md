
--- 
title:  原生实现C#与Lua相互调用方法 
tags: []
categories: [] 

---
## 原生实现C#与Lua相互调用方法(Unity3D可用)

Lua是一种很好的扩展性语言,Lua解释器被设计成一个很容易嵌入到宿主程序的库,下面这篇文章主要给大家介绍了关于原生实现C#与Lua相互调用方法。

### 引言

本篇简单介绍如何在C#中执行Lua脚本，传递数据到Lua中使用，以及Lua中调用C#导出的方法等。在Unity中开发测试，并打IL2CPP的Android包在模拟器上运行通过。Lua版本使用的是Lua5.1.5。

### 一、编译Lua动态链接库

#### 1. 编译Windows下使用的DLL文件

使用VS2015创建一个空的动态链接库项目，删除里面默认创建的几个文件(如果想自定义拓展可用保留)，然后把Lua的源码拷贝进来，添加到项目工程中，编译宏需要配置LUA_BUILD_AS_DLL和_CRT_SECURE_NO_WARNINGS。然后就可以编译x86和x64的DLL动态库，整体步骤简单易操作。

#### 2. 编译Android下使用的SO文件

通过NDK编译Android需要的so动态库，因此需要手写Application.mk和Android.mk两个mk文件，下面是我使用的两个文件的内容，创建放在上面VS的工程里面即可，路径是在lua源码src的上一层目录。

```
# Application.mk
APP_PLATFORM = android-23
APP_ABI := armeabi-v7a arm64-v8a
APP_STL := stlport_shared

```

将上面的mk文件放置完成后，打开CMD命令行，执行ndk编译。由于并不是在Android的jni项目目录，因此执行命令会有所不同，可以使用下面的命令执行生成，等待ndk执行完成后就生成了需要的so库。

```
ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=./Android.mk NDK_APPLICATION_MK=./Application.mk

```

### 二、编写C#使用的API

#### 1. 动态链接库在Unity中的存放位置。

在Unity项目Assets目录里面创建Plugins目录，用于存放不同平台的DLL库。Windows需要的DLL存放的目录为Assets/Plugins/x86和Assets/Plugins/x86_64；Android需要的SO文件存放的目录为Assets/Android/[libs/arm64-v8a]括号里面的目录其实就是上面NDK编译后生成的路径。

#### 2. 编写C#使用的API

大部分的动态库中的接口直接使用以下这种方式即可使用，使用IntPtr来表示lua_State*对象，传入参数char*可用使用byte[]或者string，但是会有一点点区别。

```
[DllImport("CSharpLua", EntryPoint = "luaL_newstate")]
public static extern IntPtr luaL_newstate();
[DllImport("CSharpLua", EntryPoint = "luaL_openlibs")]
public static extern void luaL_openlibs(IntPtr L);
[DllImport("CSharpLua", EntryPoint = "luaL_loadbuffer")]
public static extern int luaL_loadbuffer(IntPtr L, byte[] buff, uint size, string name);
[DllImport("CSharpLua", EntryPoint = "lua_call")]
public static extern void lua_call(IntPtr L, int nargs, int nresults);
[DllImport("CSharpLua", EntryPoint = "lua_pcall")]
public static extern int lua_pcall(IntPtr L, int nargs, int nresults, int errfunc);　

```

#### 3.需要注意的几个地方
1. 返回char*时，不可直接使用string替换，否则调用会导致崩溃，因此需要像下面代码展示的那样进行一下转换才可以使用。
```
[DllImport("CSharpLua", EntryPoint = "lua_tolstring")]
private static extern IntPtr _lua_tolstring(IntPtr L, int idx, ref uint size);
public static string lua_tolstring(IntPtr L, int idx, ref uint size)
{<!-- -->
    IntPtr buffer = _lua_tolstring(L, idx, ref size);
    return Marshal.PtrToStringAnsi(buffer);
}


```
1. C#函数传递给Lua使用时，需要使用delegate委托类型。
```
public delegate int LuaFunction(IntPtr L);
[DllImport("CSharpLua", EntryPoint = "lua_pushcclosure")]
public static extern void lua_pushcclosure(IntPtr L, LuaFunction func, int idx);
public static void lua_pushcfunction(IntPtr L, LuaFunction func)
{<!-- -->
   lua_pushcclosure(L, func, 0);
}


```
1. 在lua源码中定义的宏代码是无法使用的，会提示找不到，需要在C#中手动实现，例如下面展示的2个宏。
```
[DllImport("CSharpLua", EntryPoint = "lua_getfield")]
public static extern void lua_getfield(IntPtr L, int idx, string s);
public static void lua_getglobal(IntPtr L, string s)
{<!-- -->
   lua_getfield(L, LUA_GLOBALSINDEX, s);
}
[DllImport("CSharpLua", EntryPoint = "lua_setfield")]
public static extern void lua_setfield(IntPtr L, int idx, string s);
public static void lua_setglobal(IntPtr L, string s)
{<!-- -->
   lua_setfield(L, LUA_GLOBALSINDEX, s);
}


```
1. 如需要将C#的类实例对象即userdata传递给lua，需要在C#中转换成IntPtr后传递，Lua返回的则需要通过IntPtr转换回C#的实例对象。
```
[DllImport("CSharpLua", EntryPoint = "lua_pushlightuserdata")]
public static extern void _lua_pushlightuserdata(IntPtr L, IntPtr p);
public static void lua_pushlightuserdata&lt;T&gt;(IntPtr L, T p)
{<!-- -->
    IntPtr obj = Marshal.GetIUnknownForObject(p);
    _lua_pushlightuserdata(L, obj);
}
[DllImport("CSharpLua", EntryPoint = "lua_touserdata")]
public static extern IntPtr _lua_touserdata(IntPtr L, int idx);
public static T lua_touserdata&lt;T&gt;(IntPtr L, int idx)
{<!-- -->
   IntPtr p = _lua_touserdata(L, idx);
   return (T)Marshal.GetObjectForIUnknown(p);
}


```

### 三、C#与Lua的相互调用举例

#### 1. C#中创建Lua环境

```
IntPtr L = LuaDll.luaL_newstate();
LuaDll.luaL_openlibs(L);


```

#### 2. 加载Lua代码并执行，调用Lua的函数及向Lua传递参数。

```
var data = Resources.Load&lt;TextAsset&gt;(lua_file);
int rc = LuaDll.luaL_loadbuffer(L, data.bytes, (uint)data.bytes.Length, lua_file);
rc = LuaDll.lua_pcall(L, 0, 0, 0)
LuaDll.lua_getglobal(L, "main");
// 传递参数
LuaDll.lua_pushinteger(L, 3333);
LuaDll.lua_pushnumber(L, 3.3);
// 执行main方法
int i = LuaDll.lua_pcall(L, 2, 0, 0);


```

#### 3. 将C#函数提供给Lua使用，需要使用静态方法参考上面LuaFunction的定义。

```
LuaDll.lua_pushcfunction(L, LuaPrint);
LuaDll.lua_setglobal(L, "print");
[MonoPInvokeCallback]   // 这个主要是在Android上需要。
static int LuaPrint(IntPtr L)
{<!-- -->
  Debug.Log(".....");
  return 0;
}


```

#### 4. Lua代码调用C#方法并提供回调，由C#函数调用。

```
static int FindAndBind(IntPtr L)
{<!-- -->
   GameObject go = LuaDll.lua_touserdata&lt;GameObject&gt;(L, 1);
   string path = LuaDll.lua_tostring(L, 2);
   // 这里将lua的函数放到LUA_REGISTRYINDEX上
   int idx = LuaDll.luaL_refEx(L);
   Transform t = go.transform.Find(path);
   Button btn = t.GetComponent&lt;Button&gt;();
   btn.onClick.AddListener(delegate() {<!-- -->
     // 从LUA_REGISTRYINDEX栈获取lua的函数进行执行。
     LuaDll.lua_rawgeti(L, LuaDll.LUA_REGISTRYINDEX, idx);
     LuaDll.lua_pcall(L, 0, 0, 0);
   });
   return 0;
}


```

### 四、总结

总体来说交互调用还是比较的简单方便，跟使用C/C++与Lua交互差不多。我仅仅简单使用Lua源码进行编译动态库使用，可以方便的替换各个版本的lua进行使用。C#导出方法给Lua使用也相对简单，但是Unity中使用Lua的时候，不可能每个类例如GameObject、Transform等都手动写导出的代码给Lua使用。这块就可以去看tolua、xlua的实现，需要考虑很多东西。

到此这篇关于原生实现C#与Lua相互调用方法的文章就介绍到这了。
