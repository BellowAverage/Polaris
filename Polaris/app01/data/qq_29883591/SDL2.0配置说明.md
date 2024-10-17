
--- 
title:  SDL2.0配置说明 
tags: []
categories: [] 

---
这篇文章主要是介绍如何在windows上部署SDL。



1、首先在浏览器中输入网址http://libsdl.org/download-2.0.php，找到Development Libraries，下面会有windows、max os、linux不同版本的库，我们可以选择自己电脑操作系统的版本进行下载，我的电脑是windows64位，就选择了图中画圈处进行下载。

<img src="https://img-blog.csdn.net/20160927160506051?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">

 



2、将上一步中下载好的SDL文件进行解压缩，得到如下的文件，这里面我们将会用到的是lib和include两个文件夹：

<img src="https://img-blog.csdn.net/20161002180313251?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

3、找到自己的vs中vc文件夹，我的是D:\Program Files (x86)\Microsoft Visual Studio 10.0\VC，首先打开vc文件夹中的include文件夹，在里面新建一个SDL（路径为：D:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include\SDL，这里我要啰嗦一句，新建这个SDL文件夹是为了使头文件的放置更加规范，但这也有一个副作用，那就是我们在写程序include这些头文件时，要加上SDL/，比如我们要使用SDL.h,那就是include&lt;SDL/SDL.h&gt;，这点要切记哦），然后将刚刚解压缩的SDL文件夹中的include中的文件全部拷贝到这个新建的SDL中，如下图所示：

<img src="https://img-blog.csdn.net/20161002181107793?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

4、在刚刚的vc文件夹中打开lib文件夹（路径为：D:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\lib），将刚刚我们解压缩的SDL库的文件夹中的lib/x86文件夹打开，会看到四个文件，如下图所示：

<img src="https://img-blog.csdn.net/20161002185517352?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

此时我们将三个以lib结尾的文件拷贝到上面我们提到的lib文件夹中，如下图所示：

<img src="https://img-blog.csdn.net/20161002181901319?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

5、到这里，我们会发现，lib下文件夹中怎么出现以dll结尾的文件，这是程序在运行时用到的一个动态链接文件，处理的办法有两种，一种是将它放在C:WINDOW/system32中（这是添加到系统中），另一种是将这个dll文件放在我们项目编译所得的exe文件所在的文件夹中，这里我们采用这一种方法，下面将会介绍。

 

6、首先在vs中新建一个项目，这个步骤我这里就省略了，建完项目如下图：

<img src="https://img-blog.csdn.net/20161002182632018?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

7、下面我们来配置这个项目的属性，打开项目属性，进入到如下界面中：

<img src="https://img-blog.csdn.net/20161002182830926?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

接下来，我们点开左侧的c/c++，然后点击代码生成，在右侧栏目运行库中选择多线程 DLL (/MD)，然后点击确认：

<img src="https://img-blog.csdn.net/20161002183303102?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

再然后，我们点击左侧的链接库，然后点击输入，在右侧栏目的附加依赖项中点编辑，然后将SDL2.lib、SDL2main.lib和SDL2test.lib（这里先声明，这三个名字是我们解压缩得到的文件夹中x86文件夹中的，依照具体填写）填写进去，然后点击确认：

<img src="https://img-blog.csdn.net/20161002183212227?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 

8、至此，我们离成功便只差一步了，大家一定会想到了那个dll文件吧，是的，你没猜错，就是这个文件，下面我们在文件夹中打开这个文件（我的是在D:\myhomewok\Second），并将SDL2文件添加到exe所在文件夹中（在vs中是Debug文件夹，当然我们也可以把dll放在D:\myhomewok\Second\Second中，我选择此种做法）：

<img src="https://img-blog.csdn.net/20161002184141334?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 



到此为止，我们的SDL已经部署好了，之后便可以使用了，下面我们找个示例程序进行测试，运行截图如下：

<img src="https://img-blog.csdn.net/20160927160916106?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

 



到此，我们的SDL已经部署完成了（最后，附上我部署SDL的一个视频链接：http://pan.baidu.com/s/1qYAgtE8）。

关于测试的代码，我是在github上找的，如下：



```
/*
  Copyright (C) 1997-2016 Sam Lantinga &lt;slouken@libsdl.org&gt;
  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.
  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely.
*/

#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;

#ifdef __EMSCRIPTEN__
#include &lt;emscripten/emscripten.h&gt;
#endif

#include "SDL/SDL_test_common.h"

static SDLTest_CommonState *state;
int done;

static const char *cursorNames[] = {
        "arrow",
        "ibeam",
        "wait",
        "crosshair",
        "waitarrow",
        "sizeNWSE",
        "sizeNESW",
        "sizeWE",
        "sizeNS",
        "sizeALL",
        "NO",
        "hand",
};
int system_cursor = -1;
SDL_Cursor *cursor = NULL;

/* Call this instead of exit(), so we can clean up SDL: atexit() is evil. */
static void
quit(int rc)
{
    SDLTest_CommonQuit(state);
    exit(rc);
}

void
loop()
{
    int i;
    SDL_Event event;
        /* Check for events */
        while (SDL_PollEvent(&amp;event)) {
            SDLTest_CommonEvent(state, &amp;event, &amp;done);

            if (event.type == SDL_WINDOWEVENT) {
                if (event.window.event == SDL_WINDOWEVENT_RESIZED) {
                    SDL_Window *window = SDL_GetWindowFromID(event.window.windowID);
                    if (window) {
                        SDL_Log("Window %d resized to %dx%d\n",
                            event.window.windowID,
                            event.window.data1,
                            event.window.data2);
                    }
                }
                if (event.window.event == SDL_WINDOWEVENT_MOVED) {
                    SDL_Window *window = SDL_GetWindowFromID(event.window.windowID);
                    if (window) {
                        SDL_Log("Window %d moved to %d,%d (display %s)\n",
                            event.window.windowID,
                            event.window.data1,
                            event.window.data2,
                            SDL_GetDisplayName(SDL_GetWindowDisplayIndex(window)));
                    }
                }
            }
            if (event.type == SDL_KEYUP) {
                SDL_bool updateCursor = SDL_FALSE;

                if (event.key.keysym.sym == SDLK_LEFT) {
                    --system_cursor;
                    if (system_cursor &lt; 0) {
                        system_cursor = SDL_NUM_SYSTEM_CURSORS - 1;
                    }
                    updateCursor = SDL_TRUE;
                } else if (event.key.keysym.sym == SDLK_RIGHT) {
                    ++system_cursor;
                    if (system_cursor &gt;= SDL_NUM_SYSTEM_CURSORS) {
                        system_cursor = 0;
                    }
                    updateCursor = SDL_TRUE;
                }
                if (updateCursor) {
                    SDL_Log("Changing cursor to \"%s\"", cursorNames[system_cursor]);
                    SDL_FreeCursor(cursor);
                    cursor = SDL_CreateSystemCursor((SDL_SystemCursor)system_cursor);
                    SDL_SetCursor(cursor);
                }
            }
        }

        for (i = 0; i &lt; state-&gt;num_windows; ++i) {
            SDL_Renderer *renderer = state-&gt;renderers[i];
            SDL_RenderClear(renderer);
            SDL_RenderPresent(renderer);
        }
#ifdef __EMSCRIPTEN__
    if (done) {
        emscripten_cancel_main_loop();
    }
#endif
}

int
main(int argc, char *argv[])
{
    int i;

    /* Enable standard application logging */
    SDL_LogSetPriority(SDL_LOG_CATEGORY_APPLICATION, SDL_LOG_PRIORITY_INFO);

    SDL_assert(SDL_arraysize(cursorNames) == SDL_NUM_SYSTEM_CURSORS);

    /* Initialize test framework */
    state = SDLTest_CommonCreateState(argv, SDL_INIT_VIDEO);
    if (!state) {
        return 1;
    }
    for (i = 1; i &lt; argc;) {
        int consumed;

        consumed = SDLTest_CommonArg(state, i);
        if (consumed == 0) {
            consumed = -1;
        }
        if (consumed &lt; 0) {
            SDL_Log("Usage: %s %s\n", argv[0], SDLTest_CommonUsage(state));
            quit(1);
        }
        i += consumed;
    }
    if (!SDLTest_CommonInit(state)) {
        quit(2);
    }

    for (i = 0; i &lt; state-&gt;num_windows; ++i) {
        SDL_Renderer *renderer = state-&gt;renderers[i];
        SDL_SetRenderDrawColor(renderer, 0xA0, 0xA0, 0xA0, 0xFF);
        SDL_RenderClear(renderer);
    }
 
    /* Main render loop */
    done = 0;
#ifdef __EMSCRIPTEN__
    emscripten_set_main_loop(loop, 0, 1);
#else
    while (!done) {
        loop();
    }
#endif
    SDL_FreeCursor(cursor);

    quit(0);
    /* keep the compiler happy ... */
    return(0);
}
```


