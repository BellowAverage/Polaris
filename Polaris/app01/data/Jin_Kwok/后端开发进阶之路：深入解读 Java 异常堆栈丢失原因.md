
--- 
title:  后端开发进阶之路：深入解读 Java 异常堆栈丢失原因 
tags: []
categories: [] 

---
### 0.摘要

在应用程序的开发和维护中，通常需要借助运行日志来监控和定位问题。其中，在日志中打印异常堆栈信息对于定位问题极为重要，作为开发，对打印异常堆栈应该不陌生。笔者在实践中曾遇到一个奇怪的现象: Java 应用运行中，当发生 **NullPointerException、ArithmeticException、ArrayStoreException、ClassCastException、ArrayIndexOutOfBoundsException** 这几种异常时，异常的堆栈信息有时会莫名其妙地“丢失”。

以 NullPointerException 为例，正常情况下异常堆栈信息如下所示：

```
java.lang.NullPointerException
  at com.exception.test.core.TestNullPointerException.exceptionTest(TestNullPointerException.java:28)
  at com.exception.test.core.TestNullPointerException.main(TestNullPointerException.java:15)

```

基于上述堆栈，工程师可以迅速地定位问题。然而，有时异常的堆栈会“丢失”，仅能打印出异常的名字，如下所示：

```
java.lang.NullPointerException

```

如此简略的异常信息对于定位问题几乎没有意义，那么，究竟是什么原因导致这种现象出现的呢？要弄清其中缘由，还得从 Java 语言的编译、执行及优化原理谈起，本文将详细解答，主要内容如下：
- **现场还原：Java 异常堆栈丢失问题；**- **Java 语言的执行原理；**- **JIT 编译原理；**- **JVM 如何确定热点代码；**- **Java 8 后时代；**- **源码解读：Java 异常堆栈丢失的根因**- **总结**
### 1.问题场景

在应用程序的开发和维护中，通常需要借助运行日志来监控和定位问题。其中，在日志中打印异常堆栈信息对于定位问题极为重要，作为开发，对打印异常堆栈应该不陌生。笔者在实践中曾遇到一个奇怪的问题，NPE(NullPointerException) 的堆栈有时候能打印出来，有时却只能打印了一行 java.lang.NullPointerException。如下实例：

```
public class TestNullPointerException {<!-- -->

    public static void main(String[] args) {<!-- -->
        boolean flag = false;
        for (int i = 0; i &lt; Integer.MAX_VALUE; i++) {<!-- -->
            boolean isExceptionStackLoss = exceptionTest();
            if (isExceptionStackLoss) {<!-- -->
                flag = true;
                System.out.println("times:" + i + ", res:" + isExceptionStackLoss);
            } else if (flag) {<!-- -->
                System.out.println("times:" + i + ", res:" + isExceptionStackLoss);
            }
        }

    }

    public static boolean exceptionTest() {<!-- -->
        try {<!-- -->
            // 人为构造一个NPE异常
            ((Object) null).getClass();
        } catch (Exception e) {<!-- -->
            // 检测 NPE 异常堆栈，如果堆栈正常，length不可能为0
            if (e.getStackTrace().length == 0) {<!-- -->
                try {<!-- -->
                    // 当出现 NPE 异常堆栈为空的时候，停留5秒，便于观察
                    Thread.sleep(5000);
                } catch (Exception e1) {<!-- -->
                }
                // 如果出现 NPE 异常堆栈为空，返回true
                return true;
            }
        }
        return false;
    }
}

```

运行上述代码，结果如下（不同 JVM 会有差异）：

```
times:5677, res:true
times:5678, res:false
times:5679, res:false
times:5680, res:false
times:5681, res:false
times:5682, res:false
......中间省略
times:11551, res:false
times:11552, res:false
times:11553, res:false
times:11554, res:false
times:11555, res:false
times:11556, res:true
times:11557, res:true
times:11558, res:true
times:11559, res:true
times:11560, res:true
times:11561, res:true

Process finished with exit code 130 (interrupted by signal 2: SIGINT)

```

很明显，第一次出现 NPE 堆栈丢失是在执行 5677 次异常触发操作的时候，之后异常堆栈恢复。在触发 11555 次 NPE 后，异常堆栈“稳定”丢失，没有再恢复。是不是很奇怪？异常堆栈居然会丢失！

修改一下上面的代码，将堆栈信息打印出来，我们来直观的感受一下，堆栈有无的差异。修改后的代码如下：

```
public class TestNullPointerException {<!-- -->
    public static void main(String[] args) {<!-- -->
        boolean flag = false;
        for (int i = 0; i &lt; Integer.MAX_VALUE; i++) {<!-- -->
            boolean isExceptionStackLoss = exceptionTest();
            if (isExceptionStackLoss) {<!-- -->
                flag = true;
                System.out.println("times:" + i + ", res:" + isExceptionStackLoss);
            } else if (flag) {<!-- -->
                System.out.println("times:" + i + ", res:" + isExceptionStackLoss);
            }
        }
    }

    public static boolean exceptionTest() {<!-- -->
        try {<!-- -->
            // 人为构造一个NPE异常
            ((Object) null).getClass();
        } catch (Exception e) {<!-- -->
            // 检测 NPE 异常堆栈，如果堆栈正常，length不可能为0
            if (e.getStackTrace().length == 0) {<!-- -->
                // 打印堆栈信息
                e.printStackTrace();
                try {<!-- -->
                    // 当出现 NPE 异常堆栈为空的时候，停留5秒，便于观察
                    Thread.sleep(5000);
                } catch (Exception e1) {<!-- -->
                }
                // 如果出现 NPE 异常堆栈为空，返回true
                return true;
            }
            // 打印堆栈信息
            e.printStackTrace();
        }

        return false;
    }
}

```

部分运行结果如下(不同 JVM 执行结果有差异)。通过异常的堆栈，我们可以很容易定位问题，但是如果仅仅打印出异常，如 java.lang.NullPointerException，是很难定位问题的。

```
// ...略
java.lang.NullPointerException
    at com.alipay.alipaymember.test.core.TestNullPointerException.exceptionTest(TestNullPointerException.java:28)
    at com.alipay.alipaymember.test.core.TestNullPointerException.main(TestNullPointerException.java:15)
times:11595, res:false
java.lang.NullPointerException
times:11596, res:true
java.lang.NullPointerException
times:11597, res:true
java.lang.NullPointerException
times:11598, res:true
java.lang.NullPointerException
times:11599, res:true
// ...略

```

### 2.知识点回顾

#### 2.1 Java 语言的执行原理

计算机本身只能识别 0 和 1 构成的机器码，因此，任何编程语言最终都需要编译成机器码才能被计算机执行。以 C/C++ 为例，用它们编写的程序首先被编译，然后被连接成单独的、支持特定硬件平台和操作系统的二进制文件。通常情况下，一个平台上的二进制可执行文件不能在其它平台上工作。

Java 在诞生之初便提出了著名的 slogan：**“Write Once, Run Anywhere”**，为了实现这一目标，Java 虚拟机应运而生。目前，Java 虚拟机有很多版本，但它们都具有一个共同的特征——可以载入并执行同一种与平台无关的字节码(ByteCode)。 因为 Java 虚拟机的出现，Java 源代码不必根据不同平台编译成 0 和 1，而是间接翻译成字节码，储存字节码的文件再交由运行于不同平台上的 Java 虚拟机去读取执行，从而实现一次编写，到处运行的目的。

Java 编译生成的字节码文件为 ".class " 文件，它是一种二进制文件，其中包含了 Java 虚拟机指令集和符号表以及若干其它辅助信息。但是 .class 文件并不能在机器上直接执行，而是需要解释器(Interpreter)对字节码逐条解释执行，因此 Java 本质上也是解释型语言。这种解释执行的方式效率比较低，尤其当某个方法或代码块运行得特别频繁时，这种方式的执行效率就显得更低了。鉴于此，后来在虚拟机中引入了 JIT(Just In Time)编译器(即时编译器)，其核心原理为：当虚拟机发现某个方法或代码块运行特别频繁时，就会把这些代码认定为“Hot Spot Code”（热点代码），为了提高热点代码的执行效率，JIT 在程序执行的时候，会将热点代码编译成机器码并进行各层次的优化，然后存储于内存中。当再次执行热点代码时就不需要再去加载、解释字节码，而是直接执行相应的机器码。

#### 2.2 哪些代码会被 JIT 编译成机器码

既然 JIT 可以改善性能，那么，是否可以将所有字节码都编译成机器码呢？答案是否定的，当 JVM 执行代码时，它并不会立即开始编译代码。如果某段代码或方法在将来只会被执行一次，那么，将它编译成本地可执行的机器码就“很不划算”，因为编译会占用程序运行时间、内存等资源。相较之下，解释执行 Java 字节码更合适。特别是当程序需要迅速启动和执行时，解释器可以首先发挥作用，省去编译的时间，立即执行；当程序运行后，随着时间的推移，编译器再将热点代码编译、优化成可在本地直接执行的机器码，从而提高执行效率。简而言之，解释执行可以节约内存，而编译执行可以提升效率，根据场景的不同，二者协同作用。

现在主流的商用虚拟机(Sun HotSpot、IBM J9)中几乎都同时包含解释器和编译器。其中，HotSpot 虚拟机中内置了两个JIT编译器(自 Java 9 起出现重大变化，下文详述)：Client Complier 和 Server Complier，分别用在客户端和服务端，目前主流的 HotSpot 虚拟机中默认是采用解释器与其中一个编译器直接配合的方式工作。运行过程中会被即时编译器编译的“热点代码”有两类：
- **被多次调用的方法。**- **被多次调用的循环体。**
两种情况，编译器都是以整个方法作为编译对象，这种编译也是虚拟机中标准的编译方式。

#### 2.3 如何确定热点代码

JVM 通过热点探测(Hot Spot Detection)来检测热点代码，目前主要的热点判定方式有以下两种：

##### 2.3.1 基于采样的热点探测：

采用这种方法的虚拟机会周期性地检查各个线程的栈顶，如果发现某些方法经常出现在栈顶，那这段方法代码就是“热点代码”。这种探测方法的好处是实现简单高效，还可以很容易地获取方法调用关系，缺点是很难精确地确认一个方法的热度，容易因为受到线程阻塞或别的外界因素的影响而扰乱热点探测。

##### 2.3.2 基于计数器的热点探测：

采用这种方法的虚拟机会为每个方法，甚至是代码块建立计数器，用于统计方法的执行次数，当执行次数超过一定阈值，就判定它是“热点方法”。这种统计方法实现复杂一些，需要为每个方法建立并维护计数器，而且不能直接获取到方法的调用关系，但是它的统计结果相对更加精确严谨。

HotSpot 虚拟机采用的是第二种，即基于计数器的热点探测方法，它为每个方法准备了两个计数器：方法调用计数器（Invocation Counter）和回边计数器（Back Edge Counter 在程序中遇到控制流向后跳转的指令称为“回边”）。

其中，方法调用计数器被用来统计方法调用的次数，在默认设置下，方法调用计数器统计的并不是方法被调用的绝对次数，而是一段时间内方法被调用的次数，本质上是执行频率。回边计数器用于统计一个方法中循环体代码执行的次数（准确地说是回边的次数，因为并非所有的循环都是回边）。

在确定 JVM 运行参数的前提下，上述两种计数器都有一个确定的阈值，当计数器的值超过阈值时，就会触发 JIT 编译。触发 JIT 编译后，在默认设置下，执行引擎并不会同步等待编译请求完成，而是继续进入解释器按照解释方式执行字节码，直到提交的请求被编译器编译完成为止（编译工作在后台线程中进行）。当编译工作完成后，下一次调用该方法或代码时，就会使用已编译的版本。方法调用计数器触发即时编译的流程如下图所示(回边计数器触发即时编译的过程与之类似)： <img src="https://img-blog.csdnimg.cn/e72f3f63f17c496588d485e94ffdd794.png#pic_center" alt="在这里插入图片描述" width="600" height="600">

JIT 运行时将字节码编译成机器码。这种将 .java 文件编译成 .class 文件的编译叫前端编译，运行时将字节码编译成机器码的叫后端编译。关于编译比较复杂，本篇不展开论述。

#### 2.4 关于 JIT 优化

JIT 编译优化技术涉及面比较广，本文不做详述，仅介绍两种典型的优化策略：方法内联，栈上分配。
-  **方法内联:** 调用一个方法通常要经历压栈和出栈，这种执行操作要求在执行前保护现场并记忆执行的地址，并按原来保存的地址返回执行，这个调用过程会产生一定的时间和空间方面的开销。如何优化呢？编译器将程序中较小的、多次出现被调用的函数，用该函数的函数体来直接替换函数调用表达式，如此便省去了方法调用的消耗。 -  **栈上分配:** 一般地，在 Java 中创建一个对象默认是在堆中分配内存的，当该对象不再被使用时将通过垃圾回收机制回收。试想这样一种情况：如果一个对象只在方法内部使用(如局部对象)，那么，不妨将这个对象在栈上分配内存，如此，对象所占用的内存空间就可以随栈帧出栈而销毁。相较于在堆中创建、回收对象，栈上操作效率要高得多。 
#### 2.5 Java 8 后时代

在上文中已经提及，在 Java8 之前，HotSpot 集成了两个 JIT，用 Client Complier(下文简称 C1) 和 Server Complier(下文简称 C2) 来完成 JVM 中的即时编译。虽然 JIT 优化了代码，但收集监控信息也会消耗运行时的性能，且编译过程会占用程序运行时间、内存等资源。

自 Java9 开始，AOT(Ahead-Of-Time) 编译器被引入。与 JIT 的设计思想不同，AOT 是在程序运行前进行的静态编译，这样就可以避免运行时的编译消耗和内存消耗，而且 .class 文件可以通过 AOT 编译器编译成 .so 的二进制文件。

到了 Java10，全新的 JIT 编译器 Graal 被引入。Graal 是一个以 Java 为主要编程语言，面向 Java 字节码的编译器。与用 C++ 实现的 C1 和 C2 相比，它的模块化更加明显，也更容易维护。Graal 不仅可以作为动态编译器，在运行时编译热点方法，而且可以作为静态编译器，实现 AOT 编译。

### 3.根因分析

#### 3.1 参数 OmitStackTraceInFastThrow

经过前面大量的铺垫，我们回到正题——为什么异常堆栈会丢失？在 Oracle 官方文档中，关于一种被称为 **“fast throw**” 的优化，有这么一段描述：The compiler in the server VM now provides correct stack backtraces for all “cold” built-in exceptions. For performance purposes, when such an exception is thrown a few times, the method may be recompiled. After recompilation, the compiler may choose a faster tactic using preallocated exceptions that do not provide a stack trace. To disable completely the use of preallocated exceptions, use this new flag: -XX:-OmitStackTraceInFastThrow.

关于上述内容，stackoverflow 上有个大牛做了如下解释：The optimization is that when an exception (typically a NullPointerException) occurs for the first time, the full stack trace is printed and the JVM remembers the stack trace (or maybe just the location of the code). When that exception occurs often enough, the stack trace is not printed anymore, both to achieve better performance and not to flood the log with identical stack traces.

结合第二节关于 JIT 的介绍，不难理解上述内容：<font color="red"> 为了改善性能，HotSpot 虚拟机做了一个优化，对于特定的隐式异常类型（典型如 NullPointerException），如果在代码里某个特定位置被抛出的次数超过一定阈值后，编译器（HotSpot Server Compiler）将对相关方法进行重新编译（编译原理见上文介绍过的 JIT）。之后，编译器会采用“fast throw”来优化这个抛出异常的地方——直接抛出一个事先分配好的、类型匹配的异常对象。这个对象的 message 和 stack trace 都被清空(这就是异常堆栈丢失的原因)。由于无需额外分配内存，而且不用爬取堆栈，抛出这个异常的速度非常快。</font>

当然，这种优化是一把双刃剑：一方面，该优化可以提高应用程序的性能，同时避免大量异常堆栈信息打印出来消耗服务器磁盘空间 (日志风暴)；另一方面，当应用程序出现问题的时候，可能没有可供查看的异常堆栈，增加定位问题的难度，不过，异常最初还是会打印异常堆栈的，通过追述日志可找到堆栈信息，只是对于经验不够丰富的工程师，恐怕并不会想到这一点。从Sun JDK5 开始，可通过设置 VM 参数来避免编译器做这个优化：-XX:-OmitStackTraceInFastThrow。

#### 3.2 源码分析

Hotspot 中 Globals.hpp 有如下一个配置项:

```
product(bool, OmitStackTraceInFastThrow, true, 
          "Omit backtraces for some 'hot' exceptions in optimized code") 

```

上面是 OpenJDK 的 Hotspot 中定义的一个配置项，默认值为 true，配置项的含义是在优化的代码中抑制堆栈。相关的代码在 hotspot\src\share\vm\opto\graphKit.cpp 中，这部分是在 C2（HotSpot Server Compiler）编译器把 bytecode 做优化的代码（如下代码中忽略了与本问题无关的部分): 

```
void GraphKit::builtin_throw(Deoptimization::DeoptReason reason, Node* arg) {<!-- -->
  bool must_throw = true;
  //...略
  // If this particular condition has not yet happened at this
  // bytecode, then use the uncommon trap mechanism, and allow for
  // a future recompilation if several traps occur here.
  // If the throw is hot, try to use a more complicated inline mechanism
  // which keeps execution inside the compiled code.
  bool treat_throw_as_hot = false;
  ciMethodData* md = method()-&gt;method_data();

  if (ProfileTraps) {<!-- -->
    if (too_many_traps(reason)) {<!-- -->
      treat_throw_as_hot = true;
    }
    // (If there is no MDO at all, assume it is early in
    // execution, and that any deopts are part of the
    // startup transient, and don't need to be remembered.)

    // Also, if there is a local exception handler, treat all throws
    // as hot if there has been at least one in this method.
    if (C-&gt;trap_count(reason) != 0
        &amp;&amp; method()-&gt;method_data()-&gt;trap_count(reason) != 0
        &amp;&amp; has_ex_handler()) {<!-- -->
        treat_throw_as_hot = true;
    }
  }

  // If this throw happens frequently, an uncommon trap might cause
  // a performance pothole.  If there is a local exception handler,
  // and if this particular bytecode appears to be deoptimizing often,
  // let us handle the throw inline, with a preconstructed instance.
  // Note:   If the deopt count has blown up, the uncommon trap
  // runtime is going to flush this nmethod, not matter what.
  if (treat_throw_as_hot
      &amp;&amp; (!StackTraceInThrowable || OmitStackTraceInFastThrow)) {<!-- -->
    // If the throw is local, we use a pre-existing instance and
    // punt on the backtrace.  This would lead to a missing backtrace
    // (a repeat of 4292742) if the backtrace object is ever asked
    // for its backtrace.
    // Fixing this remaining case of 4292742 requires some flavor of
    // escape analysis.  Leave that for the future.
    ciInstance* ex_obj = NULL;
    switch (reason) {<!-- -->
    case Deoptimization::Reason_null_check:
      ex_obj = env()-&gt;NullPointerException_instance();
      break;
    case Deoptimization::Reason_div0_check:
      ex_obj = env()-&gt;ArithmeticException_instance();
      break;
    case Deoptimization::Reason_range_check:
      ex_obj = env()-&gt;ArrayIndexOutOfBoundsException_instance();
      break;
    case Deoptimization::Reason_class_check:
      if (java_bc() == Bytecodes::_aastore) {<!-- -->
        ex_obj = env()-&gt;ArrayStoreException_instance();
      } else {<!-- -->
        ex_obj = env()-&gt;ClassCastException_instance();
      }
      break;
    default:
      break;
    }
    if (failing()) {<!-- --> stop(); return; }  // exception allocation might fail
    if (ex_obj != NULL) {<!-- -->
      // Cheat with a preallocated exception object.
      if (C-&gt;log() != NULL)
        C-&gt;log()-&gt;elem("hot_throw preallocated='1' reason='%s'",
                       Deoptimization::trap_reason_name(reason));
      const TypeInstPtr* ex_con  = TypeInstPtr::make(ex_obj);
      Node*              ex_node = _gvn.transform(ConNode::make(ex_con));

      // Clear the detail message of the preallocated exception object.
      // Weblogic sometimes mutates the detail message of exceptions
      // using reflection.
      int offset = java_lang_Throwable::get_detailMessage_offset();
      const TypePtr* adr_typ = ex_con-&gt;add_offset(offset);

      Node *adr = basic_plus_adr(ex_node, ex_node, offset);
      const TypeOopPtr* val_type = TypeOopPtr::make_from_klass(env()-&gt;String_klass());
      Node *store = access_store_at(ex_node, adr, adr_typ, null(), val_type, T_OBJECT, IN_HEAP);

      add_exception_state(make_exception_state(ex_node));
      return;
    }
  }

```

从上述源码中可以看到，可被编译器优化的异常有 NullPointerException，ArithmeticException，ArrayIndexOutOfBoundsException，ArrayStoreException，ClassCastException。这里仅以 NullPointerException 的处理流程为例介绍，上面的代码的大致逻辑是:

>  
 - 根据 methodData 中的 profile 数据判断异常处理是否足够热。- 如果足够的热的话，从全局对象区(Universe)中获取到 NullPointerException 对象。- 替换掉原来获取抛出的 NPE 的对象，取而代之的是 Universe 的 NPE 对象，由于 Universe 中的 NPE 对象并没有 Stacktrace 信息，因此无法打印出堆栈信息。 


那又怎么判断代码是否为足够热呢？

```
bool Compile::too_many_traps(ciMethod* method,
                             int bci,
                             Deoptimization::DeoptReason reason) {<!-- -->
  ciMethodData* md = method-&gt;method_data();
  if (md-&gt;is_empty()) {<!-- -->
    // Assume the trap has not occurred, or that it occurred only
    // because of a transient condition during start-up in the interpreter.
    return false;
  }
  if (md-&gt;has_trap_at(bci, reason) != 0) {<!-- -->
    return true;
  } else {<!-- -->
    // Ignore method/bci and see if there have been too many globally.
    return too_many_traps(reason, md);
  }
}

```

上面代码的意思是根据 Method 的 profile 数据判断指定的 bci(bytecode index) 对应的异常执行次数是不是超过了配置项 PerMethodTrapLimit (现在配置的是100)。那是不是一个异常代码是不是超过 100 次就一定会呢？也不一定,编译的代码在一定情况下会 Deoptimization，在什么情况下会 deoptimizatoin？例如有新的 class 加载等。到这里我们大致了解了 Hotspot 如何抑制 NPE 的堆栈的了。 如果有兴趣的话，可以自己再 debug 一下看看。

### 4.总结
1. 在排查异常时，如果发现异常没有打印堆栈，特别关注是否为 NullPointerException，ArithmeticException，ArrayIndexOutOfBoundsException，ArrayStoreException，ClassCastException，如果是，大概率就是虚拟机开启了 FastThrow 优化，参数为：-XX:+OmitStackTraceInFastThrow。1. 关于是否关闭 FastThrow 优化，应该根据业务场景综合衡量，如果关闭，就需要预防产生“日志风暴”，否则，一旦高频应用出现异常可能很快用满服务器磁盘。1. 学如逆水行舟，不进则退，作为一名工程师，每当 JDK 新版发布时，有必要关注一下主要的更新。
### 5. 推荐一本书

业界首部体系化、全景式解读服务端开发的著作——**《服务端开发：技术、方法与实用解决方案》**，在此推荐给大家。该书作者曾获得<font color="#dd0000">阿里第二届技术讲师课程大赛年度冠军</font>（由阿里 CPO 和 CSDN CEO 共同颁奖），在阿里和蚂蚁内部所授技术课程口碑甚好。全书分 14 章，约 30 万字，正文 373 页，共 389 页，由机械工业出版社出版发行。内容分为上下两篇。上篇 1～6 章，主题为技术和方法；下篇 7～14章，主题为解决方案。书中列举了大量实用案例，为了便于读者理解，作者还绘制了超过 200 幅插图，可谓图文并茂。 <img src="https://img-blog.csdnimg.cn/e84687ceb157470db6946fb9513a36ab.png#pic_center" alt="在这里插入图片描述" width="400" height="450">

#### 5.1 读者对象

这本书体系化地解读了服务端开发的方方面面，特别提供了针对高并发、高可用、高性能、数据一致性等重难点的行业经典解决方案，极具价值。
- **IT 从业人员**：服务端开发工程师、客户端开发工程师、产品经理、测试开发工程师等。- **高校学生**：计算机、软件、自动化、电气、通信等专业有志于进入 IT 行业的在校学生。- **求职面试**：不同于一般的“面试宝典”仅仅侧重对某种语言、框架、中间件等进行解读，本书立足于服务端开发的全局视角，体系化解读服务端开发的大厂规范流程和重难点，面试必备。
#### 5.2 该书特色

无论技术如何演进，其背后的方法往往大同小异，经典解决方案历久弥新。因此，掌握方法和实用解决方案尤为必要。不同于一般的 IT 技术书籍，这本书不局限于任何一种具体的编程语言、框架、容器、中间件或编程思想，而是致力于全景式、体系化地解读服务端开发的流程和重难点。

该书共 14 章，内容从逻辑上可以分为两大部分。

**第一部分为第 1～6 章，主题是技术和方法**。首先概述服务端开发的职责、技术栈、核心流程和进阶路径，然后从需求分析、抽象建模、系统设计、数据设计、非功能性设计 5 个方面逐一展开，结合案例深入解读服务端开发的实操方法和重难点，为读者清晰呈现服务端开发的全景图。通过学习本篇内容，读者可以快速、体系化地掌握服务端开发的相关知识和方法。

**第二部分为第 7～14 章，主题是解决方案**。针对高并发、高可用、高性能、缓存、幂等、数据一致性等服务端开发的典型问题，结合业务场景进行系统性分析并给出解决方案。此外，就接口设计、日志打印、异常处理、代码编写、代码注释等实施细节给出行业案例和规范。本篇内容如同一本服务端开发问题手册，当读者在实践中遇到问题时，可以从中查找解决方案。

目前，本书已经在**京东、淘宝、当当、拼多多**等电商平台发售。在电商 APP 搜索关键词 **“服务端开发”、“服务端开发技术”**，即可搜索到该书。

### 6.引用

本文由原作者授权发表，原文发表于公众号 “互联网技术人进阶之路”，特此声明。
