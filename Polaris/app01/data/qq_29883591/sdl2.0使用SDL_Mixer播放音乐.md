
--- 
title:  sdl2.0使用SDL_Mixer播放音乐 
tags: []
categories: [] 

---
今天给大家分享一个使用sdl播放音乐的一个特别简单的例子：

     对于SDL_2.0中自带的播放wav格式音乐的功能我就不说了，本人用起来感觉特别麻烦，操作好多，而SDL_Mixer库中加载播放wav只要三行代码，是的，你没有看错，就是三行代码，我当时都有点不可思议，那么进入正题吧。

```
#include&lt;SDL/SDL.h&gt;
#include&lt;SDL\SDL_mixer.h&gt;
#include&lt;iostream&gt;

int main(int argc,char *argv)
{
	if (SDL_Init(SDL_INIT_EVERYTHING) == -1){
        std::cout &lt;&lt; SDL_GetError() &lt;&lt; std::endl; 
        return 1;
    }
	
	//加载声音文件
	Mix_OpenAudio(44100,MIX_DEFAULT_FORMAT,2,2048);
        Mix_Music *sound=Mix_LoadMUS("D://sound.wav");
	Mix_PlayMusic(sound,1);
	SDL_Delay(10000);    //一定要有此句话，否则程序会立即关闭，而不会听到声音
	return 0;
}
```


