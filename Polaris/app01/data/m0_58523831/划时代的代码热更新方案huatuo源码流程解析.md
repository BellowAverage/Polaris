
--- 
title:  划时代的代码热更新方案huatuo源码流程解析 
tags: []
categories: [] 

---
## **前言**

前天听说了一个名为  的热更新方案横空出世，它基于IL2CPP对用户代码进行热更，本以为像一些热更方案一样自己实现了一整套虚拟机运行时，但看过源码之后我表示大为震撼，同时佩服作者的脑回路，简直巧夺天工。

## 热更新基础

我们需要先了解一下Mono和IL2Cpp这两个脚本后端

首先是Mono，结构相当简单，就是Mono VM解释执行IL代码

<img src="https://img-blog.csdnimg.cn/img_convert/4bcbf8bf7f68c652fca790b3e75a5b68.png" alt="">

然后是IL2CPP，相对复杂一些，需要将IL转译成C++代码，然后经过本地的`C++`编译器编译后使用IL2CPP的虚拟机运行时去执行我们转译的`C++`代码，IL2CPP的运行时做了相当多的事情，包括但不限于支持`C#`的反射，GC，泛型，虚函数，Interface，线程管理等，这样才可以让C#真正的运行在IL2CPP虚拟机上

<img src="https://img-blog.csdnimg.cn/img_convert/f19c2ab09d8f38faf1308fe75013ef0e.png" alt="">

抛开IOS以及一些主机平台的禁止JIT策略不谈，由于`C++`的语言限制，所以IL2CPP本身就是AOT的，所以类似LoadAssembly，Emit，Expression这种原本由`C#` JIT支持的骚操作在IL2CPP都是不支持，这也是为什么我们需要各种各样代码热更新方案的原因

## huatuo

### 简介

huatuo是一个**特性完整、零成本、高性能、低内存**的**近乎完美**的c#热更新方案。

huatuo提供一个非常完整的跨平台CLR运行时，不仅能在Android平台，也能在IOS、Consoles等限制了JIT的平台上高效地以**AOT+interpreter**混合模式执行。

huatuo特性：
- 特性完整。 近乎完整实现了，除了 下文中"限制和注意事项" 之外的特性都支持。- 零学习和使用成本。 huatuo是完整的CLR运行时，热更新代码与AOT代码无缝工作。不需要额外写任何特殊代码、没有代码生成，也没有什么特殊限制。脚本类与AOT类在同一个运行时内，即使反射、多线程(volatile、ThreadStatic、Task、async)之类的代码都能够正常工作。- 执行高效。实现了一个极其高效的寄存器解释器，所有指标都大幅优于其他热更新方案。- 内存高效。 热更新脚本中定义的类跟普通c#类占用一样的内存空间，远优于其他热更新方案。- 原生支持修复AOT部分代码。不额外增加任何开发和运行开销。
更具体地说，huatuo做了以下几点工作：
- 实现了一个高效的元数据(dll)解析库- 改造了il2cpp的元数据管理模块，实现了元数据的动态注册- 实现了一个IL指令集到自定义的寄存器指令集的compiler- 实现了一个高效的寄存器解释器- 额外提供大量的instinct函数，提升解释器性能- 提供hotfix AOT的支持 （进行中）
### 安装使用



### 基础架构

huatuo的基本原理非常简单，对于AOT的代码就使用IL2CPP执行，对于非AOT代码（比如我们提供的dll）则通过huatuo解释执行

### 运行流程图

先来看一张大的流程图，包括huatuo的Init，LoadAssembly和Execute流程，其中左侧是IL2CPP层调用，右侧是huatuo层调用

<img src="https://img-blog.csdnimg.cn/7f74c9f46cd94a33ad5f2bf700b9ce02.png" alt="">

运行流程图

#### Init

由Unity Native发起调用，执行 `bool Runtime::Init`， 随后会一路调用到 `void ModuleManager::Initialize`

C++

```
void InterpreterModule::Initialize()
{<!-- -->
	for (size_t i = 0; ; i++)
	{<!-- -->
		NativeCallMethod&amp; method = g_callStub[i];
		if (!method.signature)
		{<!-- -->
			break;
		}
		s_calls.insert_or_assign(method.signature, method);
	}
	for (size_t i = 0; ; i++)
	{<!-- -->
		NativeInvokeMethod&amp; method = g_invokeStub[i];
		if (!method.signature)
		{<!-- -->
			break;
		}
		s_invokes.insert_or_assign(method.signature, method);
	}
}

```

其中g_callStub和g_invokeStub就是huatuo提供的instinct函数

C++

```
NativeCallMethod huatuo::interpreter::g_callStub[] = 
{<!-- -->
	{<!-- -->"v", (Il2CppMethodPointer)__Native2ManagedCall_v, (Il2CppMethodPointer)__Native2ManagedCall_AdjustorThunk_v, __Managed2NativeCall_v},
	{<!-- -->"vi", (Il2CppMethodPointer)__Native2ManagedCall_vi, (Il2CppMethodPointer)__Native2ManagedCall_AdjustorThunk_vi, __Managed2NativeCall_vi},
	{<!-- -->"vf", (Il2CppMethodPointer)__Native2ManagedCall_vf, (Il2CppMethodPointer)__Native2ManagedCall_AdjustorThunk_vf, __Managed2NativeCall_vf},
	{<!-- -->"vii", (Il2CppMethodPointer)__Native2ManagedCall_vii, (Il2CppMethodPointer)__Native2ManagedCall_AdjustorThunk_vii, __Managed2NativeCall_vii},
	{<!-- -->"vfi", (Il2CppMethodPointer)__Native2ManagedCall_vfi, (Il2CppMethodPointer)__Native2ManagedCall_AdjustorThunk_vfi, __Managed2NativeCall_vfi},
	....
}
 
NativeInvokeMethod huatuo::interpreter::g_invokeStub[] = 
{<!-- -->
	{<!-- -->"v", __Invoke_instance_v, __Invoke_static_v},
	{<!-- -->"vi", __Invoke_instance_vi, __Invoke_static_vi},
	{<!-- -->"vf", __Invoke_instance_vf, __Invoke_static_vf},
	{<!-- -->"vii", __Invoke_instance_vii, __Invoke_static_vii},
	{<!-- -->"vfi", __Invoke_instance_vfi, __Invoke_static_vfi},
	{<!-- -->"vif", __Invoke_instance_vif, __Invoke_static_vif},
	{<!-- -->"vff", __Invoke_instance_vff, __Invoke_static_vff},
    ...
}

```

这里以__Invoke_instance_v这一常用函数为例，我们可以忽略一些栈帧构造相关的数据，但需要注意其中的 `Interpreter::Execute`，这是huatuo正式解释执行的起点，后面我们会继续提到它

C++

```
static void* __Invoke_static_v(Il2CppMethodPointer methodPtr, const MethodInfo* method, void* __this, void** __args)
{<!-- -->
    StackObject args[1] = {<!-- --> };
    ConvertInvokeArgs(args, method, __args);
    StackObject* ret = nullptr;
     Important 
    Interpreter::Execute(method, args, ret);
     Important 
    return nullptr;
}

```

#### LoadAssemblyLoadAssembly

同样由Unity Native发起调用，起点为IL2CPP层的`const Il2CppAssembly* Assembly::Load`，随后会调用到huatuo层的`Il2CppAssembly* Assembly::Create`用于解析这个Dll然后生成IL2CPP和huatuo需要用到的Image，Assembly以及元数据信息。在huatuo这边对于Assembly的解析是作者实现的，相当的硬核，可以认为是一比一复刻了CLR对Dll的解析行为，在这个过程中，`很多元数据类型都是直接使用的IL2CPP中的（比如Il2CppTypeDefinition，Il2CppMethodDefinition等），这也是为了与IL2CPP直接Hook联调打下基础`，当然了，huatuo这边要进行一些解释执行操作，所以也会生成一些huatuo专属的元数据（例如TbMethod，MethodBody，ilcodedata指针等，其中很多也包装了下IL2CPP元数据类型）

其中比较重要的是Method元数据的构造，大家可以参考下CLR的Method Table，差不太多

<img src="https://img-blog.csdnimg.cn/img_convert/eb4622908582f5f11eab3dfb444469cb.webp?x-oss-process=image/format,png" alt="">

CLR的Method Table

#### Execute

我们以官方演示Demo为例，当由`LoadDll.cs`脚本的LoadGameDll函数反射调用`APP.cs`脚本的`APP.Main`函数时堆栈如下

C++

```
 	GameAssembly.dll!il2cpp::vm::SetupMethodsLocked(Il2CppClass * klass, const il2cpp::os::FastAutoLock &amp; lock) 行 1192	C++
 	GameAssembly.dll!il2cpp::vm::Class::SetupMethods(Il2CppClass * klass) 行 1279	C++
 	GameAssembly.dll!huatuo::metadata::GetMethodInfoFromMethodDef(const Il2CppType * type, const Il2CppMethodDefinition * methodDef) 行 572	C++
 	GameAssembly.dll!huatuo::metadata::GetMethodInfo(const Il2CppType * containerType, const Il2CppMethodDefinition * methodDef, const Il2CppGenericInst * instantiation, const Il2CppGenericContext * genericContext) 行 1076	C++
 	GameAssembly.dll!huatuo::metadata::ReadMethodInfoFromToken(huatuo::metadata::Image &amp; image, const Il2CppGenericContainer * klassGenericContainer, const Il2CppGenericContainer * methodGenericContainer, const Il2CppGenericContext * genericContext, Il2CppGenericInst * genericInst, huatuo::metadata::TableType tableType, unsigned int rowIndex) 行 1135	C++
 	GameAssembly.dll!huatuo::metadata::Image::GetMethodInfoFromToken(unsigned int token, const Il2CppGenericContainer * klassGenericContainer, const Il2CppGenericContainer * methodGenericContainer, const Il2CppGenericContext * genericContext) 行 1195	C++
 	GameAssembly.dll!huatuo::transform::HiTransform::Transform(huatuo::metadata::Image * image, const MethodInfo * methodInfo, huatuo::metadata::MethodBody &amp; body, huatuo::interpreter::InterpMethodInfo &amp; result) 行 2405	C++
 	GameAssembly.dll!huatuo::interpreter::InterpreterModule::GetInterpMethodInfo(huatuo::metadata::Image * image, const MethodInfo * methodInfo) 行 332	C++
 	GameAssembly.dll!huatuo::interpreter::Interpreter::Execute(const MethodInfo * methodInfo, huatuo::interpreter::StackObject * args, huatuo::interpreter::StackObject * ret) 行 888	C++
&gt;	GameAssembly.dll!__Invoke_static_i(void(*)() methodPtr, const MethodInfo * method, void * __this, void * * __args) 行 22127	C++
 	GameAssembly.dll!il2cpp::vm::Runtime::Invoke(const MethodInfo * method, void * obj, void * * params, Il2CppException * * exc) 行 575	C++
 	GameAssembly.dll!il2cpp::vm::InvokeConvertThis(const MethodInfo * method, void * thisArg, void * * convertedParameters, Il2CppException * * exception) 行 684	C++
 	GameAssembly.dll!il2cpp::vm::Runtime::InvokeConvertArgs(const MethodInfo * method, void * thisArg, Il2CppObject * * parameters, int paramCount, Il2CppException * * exception) 行 778	C++
 	GameAssembly.dll!il2cpp::vm::Runtime::InvokeArray(const MethodInfo * method, void * obj, Il2CppArray * params, Il2CppException * * exc) 行 594	C++
 	GameAssembly.dll!il2cpp::icalls::mscorlib::System::Reflection::MonoMethod::InternalInvoke(Il2CppReflectionMethod * method, Il2CppObject * thisPtr, Il2CppArray * params, Il2CppException * * exc) 行 240	C++
 	GameAssembly.dll!MonoMethod_InternalInvoke_mFF7E631020CDD3B1CB47F993ED05B4028FC40F7E(MonoMethod_t * __this, Il2CppObject * ___obj0, ObjectU5BU5D_tC1F4EE0DB0B7300255F5FD4AF64FE4C585CF5ADE * ___parameters1, Exception_t * * ___exc2, const MethodInfo * method) 行 39012	C++
 	GameAssembly.dll!MonoMethod_Invoke_mD6E222F8DAB5483E6640B8E399A56B366635B923(MonoMethod_t * __this, Il2CppObject * ___obj0, int ___invokeAttr1, Binder_t2BEE27FD84737D1E79BC47FD67F6D3DD2F2DDA30 * ___binder2, ObjectU5BU5D_tC1F4EE0DB0B7300255F5FD4AF64FE4C585CF5ADE * ___parameters3, CultureInfo_t1B787142231DB79ABDCE0659823F908A040E9A98 * ___culture4, const MethodInfo * method) 行 39080	C++
 	GameAssembly.dll!VirtFuncInvoker5&lt;Il2CppObject *,Il2CppObject *,int,Binder_t2BEE27FD84737D1E79BC47FD67F6D3DD2F2DDA30 *,ObjectU5BU5D_tC1F4EE0DB0B7300255F5FD4AF64FE4C585CF5ADE *,CultureInfo_t1B787142231DB79ABDCE0659823F908A040E9A98 *&gt;::Invoke(unsigned short slot, Il2CppObject * obj, Il2CppObject * p1, int p2, Binder_t2BEE27FD84737D1E79BC47FD67F6D3DD2F2DDA30 * p3, ObjectU5BU5D_tC1F4EE0DB0B7300255F5FD4AF64FE4C585CF5ADE * p4, CultureInfo_t1B787142231DB79ABDCE0659823F908A040E9A98 * p5) 行 71	C++
 	GameAssembly.dll!MethodBase_Invoke_m5DA5E74F34F8FFA8133445BAE0266FD54F7D4EB3(MethodBase_t * __this, Il2CppObject * ___obj0, ObjectU5BU5D_tC1F4EE0DB0B7300255F5FD4AF64FE4C585CF5ADE * ___parameters1, const MethodInfo * method) 行 18289	C++
 	GameAssembly.dll!LoadDll_RunMain_mEDAF0764CCCFDE2F0B9801051CCD5FFDF0241B4C(LoadDll_tF4302664700CA4FCBC0471B8C95631AE6442BC68 * __this, const MethodInfo * method) 行 41550	C++
 	GameAssembly.dll!LoadDll_Start_m9DCFAB46D91AA07BA3DD00B2F19473B66E1E78DB(LoadDll_tF4302664700CA4FCBC0471B8C95631AE6442BC68 * __this, const MethodInfo * method) 行 41413	C++
 	GameAssembly.dll!RuntimeInvoker_TrueVoid_t700C6383A2A510C2CF4DD86DABD5CA9FF70ADAC5(void(*)() methodPointer, const MethodInfo * methodMetadata, void * obj, void * * args) 行 216780	C++
 	GameAssembly.dll!il2cpp::vm::Runtime::Invoke(const MethodInfo * method, void * obj, void * * params, Il2CppException * * exc) 行 575	C++
 	GameAssembly.dll!il2cpp_runtime_invoke(const MethodInfo * method, void * obj, void * * params, Il2CppException * * exc) 行 1118	C++
 	[外部代码]	
 	huatuo.exe!wWinMain(HINSTANCE__ * hInstance, HINSTANCE__ * hPrevInstance, wchar_t * lpCmdLine, int nShowCmd) 行 16	C++
 	[外部代码]	

```

尤其需要注意的是`il2cpp::vm::SetupMethodsLocked`，`这个函数会将MethodInfo的methodPointer和invoker_method绑定好（我们初始化时构造的那些s_calls和s_invokes）`，用于Hook到huatuo进行解释执行

MethodInfo中的函数指针绑定

methodPointer：

C++

```
Il2CppMethodPointer il2cpp::vm::MetadataCache::GetMethodPointer(const Il2CppImage* image, uint32_t token)
{<!-- -->
    uint32_t rid = GetTokenRowId(token);
    uint32_t table =  GetTokenType(token);
    if (rid == 0)
        return NULL;
 
    // === huatuo
    if (huatuo::metadata::IsInterpreterImage(image))
    {<!-- -->
        return huatuo::metadata::MetadataModule::GetMethodPointer(image, token);
    }
    // === huatuo
 
    IL2CPP_ASSERT(rid &lt;= image-&gt;codeGenModule-&gt;methodPointerCount);
 
    return image-&gt;codeGenModule-&gt;methodPointers[rid - 1];
}

```

invoker_method：

C++

```
InvokerMethod il2cpp::vm::MetadataCache::GetMethodInvoker(const Il2CppImage* image, uint32_t token)
{<!-- -->
    uint32_t rid = GetTokenRowId(token);
    uint32_t table = GetTokenType(token);
    if (rid == 0)
        return NULL;
    // === huatuo
    if (huatuo::metadata::IsInterpreterImage(image))
    {<!-- -->
        return huatuo::metadata::MetadataModule::GetMethodInvoker(image, token);
    }
    // === huatuo
    int32_t index = image-&gt;codeGenModule-&gt;invokerIndices[rid - 1];
 
    if (index == kMethodIndexInvalid)
        return NULL;
 
    IL2CPP_ASSERT(index &gt;= 0 &amp;&amp; static_cast&lt;uint32_t&gt;(index) &lt; s_Il2CppCodeRegistration-&gt;invokerPointersCount);
    return s_Il2CppCodeRegistration-&gt;invokerPointers[index];
}

```

IL2CPP侧小结

其余情况可能堆栈会和这里的例子不一样，但是核心都是一样的：
1. 由Unity Native发起调用1. 执行`il2cpp::vm::SetupMethodsLocked`构造MethodInfo中的函数指针（如果需要的话）1. `huatuo::interpreter::Interpreter::Execute`解释执行1. (非必定)调用IL2CPP函数完成功能实现，对于一些简单的数理运算和逻辑huatuo自定义实现了，如果一些功能IL2CPP已经提供了相应接口，则调用IL2CPP接口
Interpreter::Execute

这部分在流程图中已经说明的相当详细了，这个函数就是huatuo解释执行的核心，有7k行左右的switch invoke。

C++

```
void Interpreter::Execute(const MethodInfo* methodInfo, StackObject* args, StackObject* ret)
{<!-- -->
	INIT_CLASS(methodInfo-&gt;klass);
	MachineState&amp; machine = InterpreterModule::GetCurrentThreadMachineState();
	InterpFrameGroup interpFrameGroup(machine);
	const InterpMethodInfo* imi;
	InterpFrame* frame;
	StackObject* localVarBase;
	byte* ipBase;
	byte* ip;
	PREPARE_NEW_FRAME(methodInfo, args, ret, false);
	// exception handler
	Il2CppException* curException = nullptr;
LoopStart:
	try
	{<!-- -->
		Execute Interpreter ... 
	}
	catch (Il2CppExceptionWrapper ex)
	{<!-- -->
		curException = ex.ex;
		PREPARE_EXCEPTION();
		FIND_NEXT_EX_HANDLER_OR_UNWIND();
	}
	catch (Il2CppException* ex)
	{<!-- -->
		curException = ex;
		PREPARE_EXCEPTION();
		FIND_NEXT_EX_HANDLER_OR_UNWIND();
	}
	return;
UnWindFail:
	IL2CPP_ASSERT(curException);
	interpFrameGroup.CleanUpFrames();
	il2cpp::vm::Exception::Raise(curException);
}

```

PREPARE_NEW_FRAME中会先通过 `InterpreterModule::GetInterpMethodInfo`获取huatuo能识别的MethodInfo，如果已经有缓存了就直接返回，不用再进行转义

C++

```
InterpMethodInfo* InterpreterModule::GetInterpMethodInfo(metadata::Image* image, const MethodInfo* methodInfo)
{<!-- -->
	il2cpp::os::FastAutoLock lock(&amp;il2cpp::vm::g_MetadataLock);
	if (methodInfo-&gt;huatuoData)
	{<!-- -->
		return (InterpMethodInfo*)methodInfo-&gt;huatuoData;
	}
	metadata::MethodBody&amp; originMethod = image-&gt;GetMethodBody(methodInfo-&gt;token);
	InterpMethodInfo* imi = new (IL2CPP_MALLOC_ZERO(sizeof(InterpMethodInfo))) InterpMethodInfo;
	transform::HiTransform::Transform(image, methodInfo, originMethod, *imi);
	il2cpp::os::Atomic::FullMemoryBarrier();
	const_cast&lt;MethodInfo*&gt;(methodInfo)-&gt;huatuoData = imi;
	return imi;
}

```

如果没有缓存则通过 `transform::HiTransform::Transform` 进行翻译，并将翻译的codes缓存到il2cpp-class-internals::MethodInfo.huatuoData中

### 其他

#### 源码Debug



可以方便的进行断点跟踪出包后脚本执行流程

### 总结

我们可以看到，其实`huatuo自身并没有一个完整的虚拟机系统，而是借由Unity Native和IL2CPP本身驱动执行自己的一套简单的解释执行栈帧，并且由于其自身就是IL2CPP的拓展，所以跨域调用性能也很强劲（毕竟只是几次指针跳转和函数调用）`，借助于`C++`的指针偏移和函数调用能获得相当强力的性能

## 为什么说是划时代的代码热更新方案

想一想广大的商业项目目前正在经受怎样的折磨
- 一个项目为了热更可能混用多个语言，Lua，`C#`，TS，一个框架要在每个语言里都实现一套。究其原因要么是跨域调用性能太过难看，要么是只能这么做- 想接个可能会涉及热更的第三方插件，要做到稳定可用，那一个星期的人日应该是没跑了，比如Protobuf，接在`C#`热更层就得专门修改其源码适配C#热更框架的实现，各种重定向才能得到一个仍然颤颤巍巍，得当成宝贝护着不敢随便用的插件，Lua更不要提了，lua-protobuf光注释工具都够人喝一壶的了，况且还需要根据项目需要对源码进行修改定制呢。问题的关键在哪里呢，因为这些热更方案脱离了CLR Runtime，CLR根本不知道有这些额外信息，那就只能人为的去构造，去维护- `C#`高级特性唯唯诺诺不敢用，生怕惊动了那位大人- 跨域调用，跨域继承这两个原本相当自然的功能却需要让开发者关注大量的细节，重定向，生成代码，否则就是铺天盖地的GC和卡顿- Lua和C#毕竟是不同域的东西，各种`p/invoke`下来之后还有多少能让开发者大展手脚的空间呢- 尤其点名批评Lua，这东西真的可以用来做游戏框架和业务吗，重写比重构还快，换个兄弟接手直接就寄了
而这些在huatuo这里，统统不是问题，因为他从最底层支持了热更，huatuo对IL2CPP的拓展让Unity Native看来我们的热更代码和AOT代码都一样，也就是说我们即使跑IL2CPP后端，也完全可以当成Mono后端下的PC，安卓来写。
