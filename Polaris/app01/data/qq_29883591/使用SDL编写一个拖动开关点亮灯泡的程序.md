
--- 
title:  使用SDL编写一个拖动开关点亮灯泡的程序 
tags: []
categories: [] 

---
对于SDL我也只是一个初学的菜鸟，接下来和大家分享一个我自己写的拖动开关点亮灯泡的一个C++程序。

如果你同样是一个SDL的初学者，那么推荐给你一个连接：http://adolfans.github.io/sdltutorialcn/blog/2013/01/25/sdl-2-dot-0-tutorial-index/，这里面有一些关于SDL库使用的简单介绍，是我初学时在网上搜索到的，感觉很不错，推荐给大家。

那么废话不多说，下面我们进入正题：

首先，为了更好的解决问题，我们首先得把程序要实现的主要功能说清楚了，下面看一张图：

<img src="https://img-blog.csdn.net/20161004222032326?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

突然发现csdn好流氓啊，这是我的一张程序运行的截图啊，里面就被它打上了自己的标签。。。

       从上面的图片我们可以看出，这个程序实现的功能是，当你将鼠标放到那个灰白色的按钮上时，按钮要变色（作为一种交互的表现），当你用鼠标按下按钮时，按钮会显现出凹下去的形态，然后在你拖动按钮往左滑动后灯泡点亮，这就是我们程序实现的简单功能。

下面我们先不谈程序，我们先来一起头脑风暴一下，简单想想我们怎么做、需要什么：

其实我们大家都知道，动画就是一帧一帧的图片叠加的效果，我们要实现这个程序，就需要把图片准备好，那么我们来看一下需要哪些图片

1、首先，从灯泡看起，灯要实现亮起来的要求，那么我们就需要至少两张图，一张是灯没亮时的图片，另一张是灯亮了的图片

2、其次，从按钮看，我们需要的图就更多了，首先将底层的off和on这个显示做成一张图，然后上面用于滑动的按钮要单独分离出做出三张效果图，一张是正常状态下的灰白色，一张是鼠标触碰到按钮后按钮变色，最后一张是鼠标按下去后按钮要显现出凹下去的形态

3、最后，准备一张白色的背景图，这个就比较简单了。

这些图我都已经准备好了，如下图：

<img src="https://img-blog.csdn.net/20161004223612541?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">               <img src="https://img-blog.csdn.net/20161004223738179?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">      <img src="https://img-blog.csdn.net/20161004223804664?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">      <img src="https://img-blog.csdn.net/20161004223826399?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

<img src="https://img-blog.csdn.net/20161004223846105?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">               <img src="https://img-blog.csdn.net/20161004223857887?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

素材是已经准备好了，那么下面我们进入到程序方面的讨论：

1、首先，我们得给整个画面做一个初始化，也就是哪些东西是程序一运行我们就要展现出来的，我们可以看出，我上面展示的那张图就是初始化的界面图，要做到这我们需要好好了解一下SDL的工作方式。在SDL中，图片是画在渲染器上的，然后在将渲染器“推到“窗口上显示（这些初始化的东西可以在我文章开头提供的链接里了解到的）。

2、其次，我们得管理好鼠标和界面间的交互。在这个程序中，我们要处理的交互还是很多的，鼠标触碰到滑动按钮时按钮需要变色（作为一种交互形式，当然也可以自己设计如何表现），当我们用鼠标点击滑动按钮时，按钮要有凹陷的感觉，当我们鼠标拖动滑动按钮时，按钮要能随鼠标一起移动，当按钮到达边界时灯要亮起来，做到这些就需要我们处理好事件的响应工作。

当然，这些工作我会在代码中用注释的形式进行解释，这样才更利于理解。

首先得声明，要看懂这些代码，一定要了解SDL的简单操作（可以自己查找资料也可以使用我提供的链接）。

对于代码，先声明一句，由于是初学SDL,所以就想到哪写到哪了，没有用类进行处理，多以main函数中比较冗长，如果有机会的话，我后边会做出改进，希望大家见谅。

下面直接上代码：



```
#include&lt;iostream&gt;
#include&lt;SDL/SDL.h&gt;
#include &lt;string&gt;

using namespace std;

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

SDL_Window *window = nullptr;
SDL_Renderer *renderer = nullptr;

//此函数用于加载图像
SDL_Texture* LoadImage(std::string file);

//此函数用于将纹理画到渲染器上
void ApplySurface(int x, int y, SDL_Texture *tex, SDL_Renderer *rend);

//此函数用于显示将要展示的画面，将各个图片画在渲染器上并展示出来
void PresentImage(SDL_Renderer *rend,SDL_Texture *background,SDL_Texture *light,int light_x,int light_y,SDL_Texture *baseButton,
	int baseButton_x,int baseButton_y,SDL_Texture *button,int button_x,int button_y);

int main(int argc, char** argv)
{
    if (SDL_Init(SDL_INIT_EVERYTHING) == -1){
        std::cout &lt;&lt; SDL_GetError() &lt;&lt; std::endl; 
        return 1;
    }
 
    window = SDL_CreateWindow("LightDemo", SDL_WINDOWPOS_CENTERED, 
        SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);  //创建一个绘制图片的窗口
    if (window == nullptr){
        std::cout &lt;&lt; SDL_GetError() &lt;&lt; std::endl;
        return 2;
    }
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED 
        | SDL_RENDERER_PRESENTVSYNC);   //创建一个指定到窗口的渲染器
    if (renderer == nullptr){
        std::cout &lt;&lt; SDL_GetError() &lt;&lt; std::endl;
        return 3;
    }
	//定义我们程序需要用到的图片并加载它们
	SDL_Texture *background = nullptr, *light_off = nullptr,*baseButton=nullptr,*initButton,*onButton,
		        *downButton,*light_on;
    background = LoadImage("bg.bmp");
    light_off = LoadImage("light_off.bmp");
	light_on=LoadImage("light_on.bmp");
	baseButton=LoadImage("base_button.bmp");
	initButton=LoadImage("init_button.bmp");
	onButton=LoadImage("on_button.bmp");
	downButton=LoadImage("down_button.bmp");
	
	//判断图片是否加载成功
    if (background == nullptr || light_off == nullptr||light_on==nullptr||initButton==nullptr||
		onButton==nullptr||baseButton==nullptr||downButton==nullptr)
        return 4;

	SDL_RenderClear(renderer);   //清空屏幕

	//设置背景图片的放置
    int bW, bH;
    SDL_QueryTexture(background, NULL, NULL, &amp;bW, &amp;bH);
    ApplySurface(0, 0, background, renderer);

	//设置熄灭的灯的放置位置
	int iW, iH;
    SDL_QueryTexture(light_off, NULL, NULL, &amp;iW, &amp;iH);
    int light_x = SCREEN_WIDTH / 2 - iW / 2;
    int light_y = SCREEN_HEIGHT / 3 - iH / 2;
    ApplySurface(light_x, light_y, light_off, renderer);

	//设置基础开关的位置
	int buttonW,buttonH;
	SDL_QueryTexture(baseButton,NULL,NULL,&amp;buttonW,&amp;buttonH);
	int baseButton_x=SCREEN_WIDTH/2-buttonW/2;
	int baseButton_y=SCREEN_WIDTH/3*2-2*buttonH;
	ApplySurface(baseButton_x,baseButton_y,baseButton,renderer);

	//设置开关滑动按钮的位置
	int initButtonW,initButtonH;
	SDL_QueryTexture(initButton,NULL,NULL,&amp;initButtonW,&amp;initButtonH);
	//滑动按钮右边界的坐标
	int moveToRight_x=baseButton_x+0.75*buttonW-initButtonW/2;
	int moveToRight_y=baseButton_y+buttonH/2-initButtonH/2;
	//滑动按钮左边界的坐标
	int moveToLeft_x=baseButton_x+0.25*buttonW-initButtonW/2;
	int moveToLeft_y=baseButton_y+buttonH/2-initButtonH/2;
	ApplySurface(moveToRight_x,moveToRight_y,initButton,renderer);


	SDL_RenderPresent(renderer);
//    SDL_Delay(10000);

	SDL_Event e;
	bool quit=false;    //用于标记用户是否想退出程序
	int preMouseX,preMouseY;
	int mouse_x,mouse_y;  
	bool mouseDown=false;   //此变量用于指示鼠标是否一直按着没有松开
	bool moveTo=false;  //此变量用于表示滑动按钮可以移动的方向，false代表向左移动，true代表向右移动
	int curButton_x=moveToRight_x;  //此变量代表滑动按钮X轴方向的坐标
	int curButton_y=moveToRight_y;
	while(!quit)
	{
		while(SDL_PollEvent(&amp;e))
		{
			switch(e.type)
			{
            //此种情况是退出程序用的，当你点击窗口的红X时就会关闭界面
			case SDL_QUIT:   
				quit=true;
				break;
			//此处处理的是鼠标按下事件
			case SDL_MOUSEBUTTONDOWN:    
				mouseDown=true;
				preMouseX=e.button.x;
				preMouseY=e.button.y;
			    //当鼠标在当前按钮的区域中时，此if语句得到执行
				if(preMouseX&gt;=curButton_x&amp;&amp;preMouseX&lt;=curButton_x+initButtonW&amp;&amp;preMouseY&gt;=curButton_y&amp;&amp;preMouseY&lt;=curButton_y+initButtonH)
				{
					//当按钮位于最左面时，灯亮
					if(curButton_x==moveToLeft_x)
					{
						PresentImage(renderer,background,light_on,light_x,light_y,baseButton,baseButton_x,baseButton_y,downButton,
							curButton_x,curButton_y);
					}
					else //当按钮不在最左面时，画灯不亮的图
					{
						PresentImage(renderer,background,light_off,light_x,light_y,baseButton,baseButton_x,baseButton_y,downButton,
							curButton_x,curButton_y);
					}
				}
				break;
			 //鼠标弹起操作
			case SDL_MOUSEBUTTONUP:     
				mouseDown=false;   //表示用户鼠标点击已经松开了
				break;
			//鼠标移动操作
			case SDL_MOUSEMOTION:
				//记录鼠标移动时的坐标
				mouse_x=e.motion.x;  
				mouse_y=e.motion.y;
				if(!mouseDown)   //此时处理的是鼠标有可能放到滑动按钮上的情况
				{
					if(curButton_x==moveToRight_x)
					{
						//此if语句在鼠标在按钮区域内且点击了按钮时执行，此时会刷新窗口，将按钮换成变色的按钮
						if(mouse_x&gt;=moveToRight_x&amp;&amp;mouse_x&lt;=moveToRight_x+initButtonW&amp;&amp;mouse_y&gt;=moveToRight_y&amp;&amp;mouse_y&lt;=moveToRight_y+initButtonH)
						{
							PresentImage(renderer,background,light_off,light_x,light_y,baseButton,baseButton_x,baseButton_y,onButton,
						         curButton_x,moveToRight_y);
							
						}
						else  //此时表示鼠标点击在了空白区域，并不对它做出什么反应，将初始化的按钮画在窗口
						{
							PresentImage(renderer,background,light_off,light_x,light_y,baseButton,baseButton_x,baseButton_y,initButton,
						         curButton_x,moveToRight_y);
						}
					}
					//此if语句执行的操作和上一个相似
					if(curButton_x==moveToLeft_x)
					{
						if(mouse_x&gt;=moveToLeft_x&amp;&amp;mouse_x&lt;=moveToLeft_x+initButtonW&amp;&amp;mouse_y&gt;=moveToLeft_y&amp;&amp;mouse_y&lt;=moveToLeft_y+initButtonH)
						{
							PresentImage(renderer,background,light_on,light_x,light_y,baseButton,baseButton_x,baseButton_y,onButton,
						        curButton_x,moveToLeft_y);
						}
						else
						{
							PresentImage(renderer,background,light_on,light_x,light_y,baseButton,baseButton_x,baseButton_y,initButton,
						        curButton_x,moveToLeft_y);
						}
					}
				}
				else  //此处处理的是鼠标拖动情况
				{
					if(!moveTo)   //当moveTo为false时执行，此时表示滑动按钮向左移动的操作
					{
						//当鼠标位于滑动按钮区域时
						if(mouse_x&gt;=curButton_x&amp;&amp;mouse_x&lt;=curButton_x+initButtonW&amp;&amp;mouse_y&gt;=curButton_y&amp;&amp;mouse_y&lt;=curButton_y+initButtonH)
						{
							if(mouse_x&gt;=preMouseX)  //当鼠标往反方向移动时，不做操作
								break;
							curButton_x+=mouse_x-preMouseX;  //移动后的button的x坐标位置
							if(curButton_x&lt;moveToLeft_x)  //当鼠标移动后的距离超过了滑动按钮可移动的位置，便不再改变其位置
							{
								moveTo=true;   //滑动按钮已经移动到最左端，将移动设置为可以向右移动
								curButton_x=moveToLeft_x;  //将滑动按钮的位置设置为边界值
								PresentImage(renderer,background,light_on,light_x,light_y,baseButton,baseButton_x,baseButton_y,initButton,
						              curButton_x,curButton_y);
							}
							else  //滑动按钮在鼠标拖动下的实时移动
							{
								PresentImage(renderer,background,light_off,light_x,light_y,baseButton,baseButton_x,baseButton_y,downButton,
						            curButton_x,curButton_y);
								SDL_Delay(80);  //使滑动按钮的滑动速度慢些
							}
						}
				     }
					else   //滑动按钮向右移动的操作
					{
						if(mouse_x&gt;=curButton_x&amp;&amp;mouse_x&lt;=curButton_x+initButtonW&amp;&amp;mouse_y&gt;=curButton_y&amp;&amp;mouse_y&lt;=curButton_y+initButtonH)
						{
							SDL_RenderClear(renderer);
							if(mouse_x&lt;=preMouseX)
								break;
							curButton_x+=mouse_x-preMouseX;  //移动后的button的x坐标位置
							if(curButton_x&gt;moveToRight_x)  //当鼠标移动后的距离超过了滑动按钮可移动的位置，便不再改变其位置
							{
								moveTo=false;   //滑动按钮已经移动到最右端，将移动设置为可以向左移动
								curButton_x=moveToRight_x;  //将滑动按钮的位置设置为边界值
								PresentImage(renderer,background,light_off,light_x,light_y,baseButton,baseButton_x,baseButton_y,initButton,
						             curButton_x,curButton_y);
							}
							else  //滑动按钮在鼠标拖动下的实时移动
							{
								PresentImage(renderer,background,light_on,light_x,light_y,baseButton,baseButton_x,baseButton_y,downButton,
						             curButton_x,curButton_y);
								SDL_Delay(50);  //使滑动按钮的滑动速度慢些
							}
						}
					}
				}
				break;
				
			default:
				break;
			}
		}
	}
	//做好善后工作，释放掉资源
	SDL_DestroyTexture(background);
    SDL_DestroyTexture(light_off);
	SDL_DestroyTexture(light_on);
    SDL_DestroyTexture(baseButton);
	SDL_DestroyTexture(initButton);
    SDL_DestroyTexture(onButton);
	SDL_DestroyTexture(downButton);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
 
    SDL_Quit();
	return 0;
}

SDL_Texture* LoadImage(std::string file)
{
    SDL_Surface *loadedImage = nullptr;
    SDL_Texture *texture = nullptr;
  
    loadedImage = SDL_LoadBMP(file.c_str());   //加载图层
    if (loadedImage != nullptr)
	{
        texture = SDL_CreateTextureFromSurface(renderer, loadedImage);   //将图层转化为纹理
        SDL_FreeSurface(loadedImage);   //释放掉图层
    }
    else
        std::cout &lt;&lt; SDL_GetError() &lt;&lt; std::endl;
    return texture;
}

//此函数用于将纹理画到渲染器上
void ApplySurface(int x, int y, SDL_Texture *tex, SDL_Renderer *rend)
{
    SDL_Rect pos;
	//x，y是图片左上角的坐标
    pos.x = x;
    pos.y = y;
    SDL_QueryTexture(tex, NULL, NULL, &amp;pos.w, &amp;pos.h); 
 
    SDL_RenderCopy(rend, tex, NULL, &amp;pos);   //将纹理tex画到渲染器rend
}

void PresentImage(SDL_Renderer *rend,SDL_Texture *background,SDL_Texture *light,int light_x,int light_y,SDL_Texture *baseButton,
	int baseButton_x,int baseButton_y,SDL_Texture *button,int button_x,int button_y)
{
	SDL_RenderClear(renderer);   //清空屏幕
	ApplySurface(0, 0, background, renderer);
	ApplySurface(light_x, light_y, light, renderer);
	ApplySurface(baseButton_x,baseButton_y,baseButton,renderer);
	ApplySurface(button_x,button_y,button,renderer);
	SDL_RenderPresent(renderer);
}
```



 
