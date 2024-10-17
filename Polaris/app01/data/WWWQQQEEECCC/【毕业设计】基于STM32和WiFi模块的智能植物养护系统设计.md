
--- 
title:  【毕业设计】基于STM32和WiFi模块的智能植物养护系统设计 
tags: []
categories: [] 

---
>  
 🆔作者简介：一名电子信息大学生. 📑 个人主页： 📫 如果文章知识点有错误的地方,请指正！和大家一起学习进步 🔥 如果感觉博主的文章还不错的话，还请不吝关注、点赞、收藏 




#### 函数目录
- - - <ul><li>- - - - - - <ul><li>- - - - - - 


## 前言

【毕业设计】：基于STM32和WIFI模块的智能植物养护系统设计 【工程链接】：https://oshwhub.com/wyb1661463799/zhi-neng-zhi-wu-yang-hu-ji-tong-she-ji 【代码链接】：https://www.wcfaka.com/details/AE408673 【项目备注】：原理图和PCB见上方的【工程链接】，希望该设计能够为大家提供一些帮助，同时也感谢大家一键三连对UP的支持。最新代码暂不更新，有需要的可以点击上方【代码链接】获取哦！ 【项目简介】：主控采用STM32F103C8T6单片机，同时对植物成长的多个环境参数进行实时采集，如土壤湿度、土壤PH值、室内温湿度和光照强度等环境数据，并发送给主控制器；然后通过WiFi模块无线传输到后台上位机对数据进行分析处理，并可以通过手机APP端或者语音助手进行补水和补光的智能养护控制。 下面是STM32单片机的代码整体思路梳理，还有LD3320模块的代码下篇文章再展示！



历时一个月毕业设计终于要完成咯！



## 一、主函数【main()】

`提示：这里是该项目的-&gt;主函数【main()】，下面代码仅供参考`

首先该函数执行 【**Sys_Init();**】即系统初始化函数，这个函数里面包含了该项目所需初始化的所有函数；其次执行【**TIM4_Init(20-1,3600-1);**】该函数是将定时器4设置为1ms的定时器，为执行【**Sound_Output();**】即蜂鸣器驱动和串口接收数据做准备；最后在主循环里面执行【**GUI_Refresh();**】即OLED更新显示函数，为实现OLED的多级菜单做准备。

```
/*--------------------------------------------------*/
/*函数名：系统主函数                                  */
/*参  数：无                                     	  */
/*返回值：无                                         */
/*--------------------------------------------------*/
int main(void)
{<!-- -->
	Sys_Init();//系统初始化函数
	/*F=72MHz/(arr+1)/(psc+1)=(72000 000)/10000/7200=1Hz*/
	TIM4_Init(20-1,3600-1);//每隔1ms进入中断一次
	while(1)
	{<!-- -->
		GUI_Refresh();//OLED更新显示函数
	}
}

```

### 1、系统初始化函数【Sys_Init()】

`提示：以下是该项目的-&gt;系统初始化函数【Sys_Init()】，下面代码仅供参考`

```
/*--------------------------------------------------*/
/*函数名：系统初始化函数           	                */
/*参  数：无                                        */
/*返回值：无                                        */
/*--------------------------------------------------*/
void Sys_Init()
{<!-- -->
	Delay_Init();//延时函数初始化
	Usart1_Init(9600);//串口1功能初始化，波特率9600
	Usart3_Init(9600);//串口3功能初始化，波特率9600
	OLED_Init();//OLED初始化
	OLED_Clear();//OLED清屏
	KEY_Init();//按键初始化
	BEEP_Init();//蜂鸣器初始化
	LED_Init();//LED初始化
 	/*数据初始化*/
	DHT11_Init();//DHT11初始化 PB14
	ADC_Configuration();//3通道ADC采集配置函数
	/*WIFI始化*/
	WiFi_ResetIO_Init();//初始化WiFi的复位IO
	AliIoT_Parameter_Init();//初始化连接阿里云IoT平台MQTT服务器的参数
}

```

### 2、定时器4初始化函数【TIM4_Init()】

`提示：以下是该项目的-&gt;定时器4初始化函数【TIM4_Init()】，下面代码仅供参考`

```
/*-------------------------------------------------*/
/*函数名：定时器4初始化                            */
/*参  数：arr：自动重装值   0~65535                */
/*参  数：psc：时钟预分频数 0~65535                */
/*返回值：无                                       */
/*说  明：定时时间：arr*psc*1000/72000000  单位ms  */
/*-------------------------------------------------*/
void TIM4_Init(u16 arr,u16 psc)
{<!-- -->  
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4,ENABLE);//使能TIM4和相关GPIO时钟
	//TIM4 PWM初始化 arr重装载值 psc预分频系数  f=72MHz/(arr+1)/(psc+1) =&gt;1Hz=72000 000/7200/10000
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;
	TIM_TimeBaseInitStructure.TIM_Period = arr;//设置自动重装载值
	TIM_TimeBaseInitStructure.TIM_Prescaler = psc;//预分频系数
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up;//计数器向上溢出
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;//时钟的分频因子，起到了一点点的延时作用，一般设为TIM_CKD_DIV1
	TIM_TimeBaseInit(TIM4,&amp;TIM_TimeBaseInitStructure);//TIM4初始化设置(设置PWM的周期)
	TIM_ClearFlag(TIM4,TIM_FLAG_Update);
	TIM_ITConfig(TIM4,TIM_IT_Update,ENABLE);

	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	NVIC_InitTypeDef NVIC_InitStructure;
	NVIC_InitStructure.NVIC_IRQChannel = TIM4_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 2;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;
	NVIC_Init(&amp;NVIC_InitStructure);
	TIM_Cmd(TIM4,ENABLE);//使能TIM4
}

```

### 3、OLED更新显示函数【GUI_Refresh()】

`提示：以下是该项目的-&gt;OLED更新显示函数【GUI_Refresh()】，下面代码仅供参考`

```
/*
函数功能：刷新界面
参数：无
返回值：无
*/
void GUI_Refresh(void)
{<!-- -->
	u8 key_val=KEY_Scan(0);//读取按键的键值
	if(key_val!=0)//只有按键按下才刷屏
	{<!-- -->
		last_index=func_index;//更新上一界面索引值
		switch(key_val)
		{<!-- -->
			case KEY_PREVIOUS: func_index=table[func_index].previous;//更新索引值
					break;
			case KEY_ENTER: func_index=table[func_index].enter;//更新索引值
					break;
			case KEY_NEXT:func_index=table[func_index].next;//更新索引值
					break;
			case KEY_BACK:func_index=table[func_index].back;//更新索引值
					break;
			default:break;
		}
		OLED_Clear();//清屏
	}
	current_operation_func=table[func_index].current_operation;
	(*current_operation_func)(func_index,key_val);//执行当前索引对应的函数
}

```

## 二、阿里云服务器连接及信息显示界面【Wifi_Child()】

`提示：以下是该项目的-&gt;阿里云服务器连接及信息显示界面【Wifi_Child()】，下面代码仅供参考` 以下函数是WIFI连接及信息显示界面，通过按键选择进入该界面函数后，执行WIFI和阿里云服务器额的连接、报文的处理以及空气温湿度等数据的上传。

```
/*
函数功能：Wifi选项子菜单
参数：u8 page_index,u8 key_val
返回值：无
*/
u8 Mode=0;//养护模式模式: 0自动养护模式 1手动养护模式
void Wifi_Child(u8 page_index,u8 key_val)
{<!-- -->
	static u8 cur_pos=1;
	OLED_ShowCHineseWord_Line(0,0,"智能植物养护系统",1);//显示智能植物养护系统
	if(last_index!=_Wifi_Option)//判断是否是第一次进入此界面
	{<!-- -->
		switch(key_val)
		{<!-- -->
			case KEY_PREVIOUS: 
					break;
			case KEY_ENTER: Mode^=1;//切换模式
							Led_flag=0;
							Fan_flag=0;
							Pump_flag=0;
					break;
			case KEY_NEXT: beep_mode^=1;//切换报警模式
					break;
			default:break;
		}
	}
	else cur_pos=1;//第一次进入此界面,界面指针清零
	
	if(cur_pos&lt;=4)
	{<!-- -->
		if(Connect_flag==1)//Connect_flag=1同服务器建立了连接
		{<!-- -->
			Connet_On();//程序连接成功接收处理程序
			Data_State();//数据上传函数
		}else Connet_First();//准备连接服务器
	}
}

```

**该界面主要的逻辑函数如下：** 首先STM32单片机进行WIFI的连接，然后再进行阿里云服务器的连接；若未连接上阿里云服务器便一直进行阿里云服务器的连接，当连接阿里云服务器成功之后进行报文的处理和数据的上传！

```
if(cur_pos&lt;=4)
	{<!-- -->
		if(Connect_flag==1)//Connect_flag=1同服务器建立了连接
		{<!-- -->
			Connet_On();//程序连接成功接收处理程序
			Data_State();//数据上传函数
		}else Connet_First();//准备连接服务器
	}

```

### 1、连接阿里云服务器函数【Connet_First()】

`提示：以下是该项目的-&gt;连接阿里云服务器函数【Connet_First()】，下面代码仅供参考`

```
/*第一次连接*/
/*程序开始连接*/
void Connet_First(void)
{<!-- -->
	u1_printf("准备连接服务器\r\n");//串口输出信息
	OLED_ShowCHineseWord_Line(0,2,"&gt;正在连接服务器&lt;",0);//显示:准备连接服务器
	Usart2_Init(115200);//串口2功能初始化，波特率115200	
	//TIM_Cmd(TIM4,DISABLE);//关闭TIM4 
	TIM_Cmd(TIM3,DISABLE);//关闭TIM3  
	TIM_Cmd(TIM2,DISABLE);//关闭TIM2    
	WiFi_RxCounter=0;//WiFi接收数据量变量清零                        
	memset(WiFi_RX_BUF,0,WiFi_RXBUFF_SIZE);//清空WiFi接收缓冲区 
	if(WiFi_Connect_IoTServer()==0)//如果WiFi连接云服务器函数返回0，表示正确，进入if
	{<!-- -->
		u1_printf("建立TCP连接成功\r\n");//串口输出信息
		Delay_Ms(3000);//延时3s
		OLED_Clear();//清屏
		Usart2_IDELInit(115200);//串口2 开启DMA 和 空闲中断
		Connect_flag = 1;//Connect_flag置1，表示连接成功	
		WiFi_RxCounter=0;//WiFi接收数据量变量清零                        
		memset(WiFi_RX_BUF,0,WiFi_RXBUFF_SIZE);//清空WiFi接收缓冲区 
		MQTT_Buff_Init();//初始化发送接收命令缓冲区 
		TIM3_ENABLE_30S();//启动定时器3 30s的PING保活定时器
		TIM2_ENABLE_1S();//启动定时器2 1s的定时器
	}
}

```

### 2、报文处理函数【Connet_On()】

`提示：以下是该项目的-&gt;报文处理函数【Connet_On()】，下面代码仅供参考` 连接成功之后处理服务器发来的报文。

```
/*程序连接成功*/
void Connet_On(void)
{<!-- -->
	if(MQTT_TxDataOutPtr != MQTT_TxDataInPtr)//if成立的话，说明发送缓冲区有数据了
	{<!-- -->
		//3种情况可进入if
		//第1种：0x10 连接报文
		//第2种：0x82 订阅报文，且ConnectPack_flag置位，表示连接报文成功
		//第3种：SubcribePack_flag置位，说明连接和订阅均成功，其他报文可发
		if((MQTT_TxDataOutPtr[2]==0x10)||((MQTT_TxDataOutPtr[2]==0x82)&amp;&amp;(ConnectPack_flag==1))||(SubcribePack_flag==1))
		{<!-- -->
			u1_printf("发送数据:0x%x\r\n",MQTT_TxDataOutPtr[2]);//串口提示信息
			MQTT_TxData(MQTT_TxDataOutPtr);//发送数据
			MQTT_TxDataOutPtr += TBUFF_UNIT;//指针下移
			if(MQTT_TxDataOutPtr==MQTT_TxDataEndPtr)//如果指针到缓冲区尾部了
				MQTT_TxDataOutPtr = MQTT_TxDataBuf[0];//指针归位到缓冲区开头
		}
	}//处理发送缓冲区数据的else if分支结尾
	/*-------------------------------------------------------------*/
	/*                     处理接收缓冲区数据                      */
	/*-------------------------------------------------------------*/
	if(MQTT_RxDataOutPtr != MQTT_RxDataInPtr)//if成立的话，说明接收缓冲区有数据了	
	{<!-- -->
	u1_printf("接收到数据:");//串口提示信息
	/*-----------------------------------------------------*/
	/*                    处理CONNACK报文                  */
	/*-----------------------------------------------------*/				
	//if判断，如果第一个字节是0x20，表示收到的是CONNACK报文
	//接着我们要判断第4个字节，看看CONNECT报文是否成功
	if(MQTT_RxDataOutPtr[2]==0x20){<!-- -->             			
			switch(MQTT_RxDataOutPtr[5]){<!-- -->					
			case 0x00 : u1_printf("CONNECT报文成功\r\n");//串口输出信息	
							ConnectPack_flag = 1;//CONNECT报文成功
						break;//跳出分支case 0x00                                              
			case 0x01 : u1_printf("连接已拒绝，不支持的协议版本，准备重启\r\n");//串口输出信息
						Connect_flag = 0;//Connect_flag置零，重启连接
						break;//跳出分支case 0x01   
			case 0x02 : u1_printf("连接已拒绝，不合格的客户端标识符，准备重启\r\n");//串口输出信息
						Connect_flag = 0;//Connect_flag置零，重启连接
						break;//跳出分支case 0x02 
			case 0x03 : u1_printf("连接已拒绝，服务端不可用，准备重启\r\n");//串口输出信息
						Connect_flag = 0;//Connect_flag置零，重启连接
						break;//跳出分支case 0x03
			case 0x04 : u1_printf("连接已拒绝，无效的用户名或密码，准备重启\r\n");//串口输出信息
						Connect_flag = 0;//Connect_flag置零，重启连接						
						break;//跳出分支case 0x04
			case 0x05 : u1_printf("连接已拒绝，未授权，准备重启\r\n");//串口输出信息
						Connect_flag = 0;//Connect_flag置零，重启连接						
						break;//跳出分支case 0x05 		
			default   : u1_printf("连接已拒绝，未知状态，准备重启\r\n");//串口输出信息 
						Connect_flag = 0;//Connect_flag置零，重启连接					
						break;//跳出分支case default 								
		}	
	}
	/*-----------------------------------------------------*/
	/*                    处理SUBACK报文                   */
	/*-----------------------------------------------------*/				
	//if判断，第一个字节是0x90，表示收到的是SUBACK报文
	//接着我们要判断订阅回复，看看是不是成功
	else if(MQTT_RxDataOutPtr[2]==0x90){<!-- -->
			switch(MQTT_RxDataOutPtr[6]){<!-- -->					
			case 0x00 :
			case 0x01 : u1_printf("订阅成功\r\n");//串口输出信息
								  SubcribePack_flag = 1;//SubcribePack_flag置1，表示订阅报文成功
									/*上报服务器当前设备状态*/
									Param_State();//上传阈值参数
									LED_State();//上报LED状态
									//AIDE_State();//上报语音助手状态
									FAN_State();//上报风扇状态
									PUMP_State();//上报水泵状态
						break;//跳出分支                                             
			default   : u1_printf("订阅失败，准备重启\r\n");//串口输出信息 
						Connect_flag = 0;//Connect_flag置零，重启连接
						break;//跳出分支 								
		}
	}
	/*-----------------------------------------------------*/
	/*                  处理PINGRESP报文                   */
	/*-----------------------------------------------------*/
	//if判断，第一个字节是0xD0，表示收到的是PINGRESP报文
	else if(MQTT_RxDataOutPtr[2]==0xD0){<!-- --> 
		u1_printf("PING报文回复\r\n");//串口输出信息 
		if(Ping_flag==1){<!-- -->//如果Ping_flag=1，表示第一次发送
			 Ping_flag = 0;//要清除Ping_flag标志
		}else if(Ping_flag&gt;1){<!-- -->//如果Ping_flag&gt;1，表示是多次发送了，而且是2s间隔的快速发送
			Ping_flag = 0;//要清除Ping_flag标志
			TIM3_ENABLE_30S();//PING定时器重回30s的时间
		}
	}
	/*-----------------------------------------------------*/
	/*                  处理数据推送报文                    */
	/*-----------------------------------------------------*/				
	//if判断，如果第一个字节是0x30，表示收到的是服务器发来的推送数据
	//我们要提取控制命令
	else if((MQTT_RxDataOutPtr[2]==0x30)){<!-- --> 
		u1_printf("服务器等级0推送\r\n");//串口输出信息 
		MQTT_DealPushdata_Qs0(MQTT_RxDataOutPtr);//处理等级0推送数据
	}

	MQTT_RxDataOutPtr +=RBUFF_UNIT;//接收指针下移
	if(MQTT_RxDataOutPtr==MQTT_RxDataEndPtr)//如果接收指针到接收缓冲区尾部了
		MQTT_RxDataOutPtr = MQTT_RxDataBuf[0];//接收指针归位到接收缓冲区开头                        
	}
	/*-------------------------------------------------------------*/
	/*                     处理命令缓冲区数据                      */
	/*-------------------------------------------------------------*/
	if(MQTT_CMDOutPtr != MQTT_CMDInPtr)//if成立的话，说明命令缓冲区有数据了			  
	{<!-- -->
		Publish_Message();//订阅信息函数
		MQTT_CMDOutPtr += CBUFF_UNIT;//指针下移
		if(MQTT_CMDOutPtr==MQTT_CMDEndPtr)//如果指针到缓冲区尾部了
			MQTT_CMDOutPtr = MQTT_CMDBuf[0];//指针归位到缓冲区开头				
	}//处理命令缓冲区数据的else if分支结尾	
}

```

### 3、数据上传阿里云服务器函数【Data_State()】

`提示：以下是该项目的-&gt;数据上传阿里云服务器函数【Data_State()】，下面代码仅供参考` 将各种数据上传到阿里云服务器显示在手机APP同时也可以在OLED显示屏上显示数据。

```
/*-------------------------------------------------*/
/*函数名：定时上传各种数据的任务                   */
/*参  数：无                                       */
/*返回值：无                                       */
/*-------------------------------------------------*/
void Data_State(void)
{<!-- -->
	char temp[500];//缓冲区
	if((SystemTimer-TEHUTimer)&gt;=2)//全局时间和温湿度计时时间至少差2s，进入if
	{<!-- -->
		TEHUTimer = SystemTimer;//把当前的全局时间，记录到温湿度计时变量
		//*数据上传阿里云*//
		//Param_State();//上传阈值参数
	  	Information();//OLED显示实时数据信息函数
		u1_printf("温度：%d  湿度：%d\r\n",tempdata,humidata);//串口输出数据:温湿度
		u1_printf("光照：%d  土壤湿度：%d  土壤PH值：%d\r\n",light_intensity,soil_humi,soil_PH);//串口输出数:光照强度、土壤湿度
		sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\
		\"air_humidity\":%d,\"air_temperature\":%d,\"illuminanceState\":%d,\"soilhumidity\":%d,\"soil_PH\":%d,\
		\"tempdata_hight\":%d,\"tempdata_low\":%d,\"humidata_hight\":%d,\"humidata_low\":%d,\"soil_humi_hight\":%d,\
		\"soil_humi_low\":%d,\"light_intensity_hight\":%d,\"light_intensity_low\":%d,\"soil_PH_hight\":%d,\"soil_PH_low\":%d},\
		\"version\":\"1.0.0\"}",humidata,tempdata,light_intensity,soil_humi,soil_PH,tempdata_hight,tempdata_low,humidata_hight,
		humidata_low,soil_humi_hight,soil_humi_low,light_intensity_hight,light_intensity_low,soil_PH_hight,soil_PH_low);//构建数据
		MQTT_PublishQs0(P_TOPIC_NAME,temp,strlen(temp));//添加数据到发送缓冲区
	}
}

```

#### ※OLED显示实时数据信息函数※【Information()】

`提示：以下是该项目的-&gt;OLED显示实时数据信息函数【Information()】，下面代码仅供参考` 第一行显示：智能植物养护系统 第二行显示：温度: C 湿度: % 第三行显示：光照: % 土湿: % 第三行显示：PH值: 自动模式/手动模式 出现以下四种情况: 1、空气温度过高-&gt;打开排风扇 2、空气湿度过高-&gt;打开排风扇 3、土壤湿度过低-&gt;打开补水泵 4、光照强度过低-&gt;打开补光灯

```
void Information(void)//OLED显示实时数据信息
{<!-- -->
	/*第1行*/
	OLED_ShowCHineseWord_Line(0,0,"智能植物养护系统",1);//显示:智能植物养护系统
	/*第2行*/
	OLED_ShowCHineseWord_Line(0,2,"温度:  C",0);//显示:"温度:  C"
	OLED_ShowNum(40,2,tempdata,2,16);//显示温度
	OLED_ShowCHineseWord_Line(64,2,"湿度:  %",0);//显示:"湿度:  %"
	OLED_ShowNum(104,2,humidata,2,16);//显示湿度
	/*第3行*/
	OLED_ShowCHineseWord_Line(0,4,"光照:  %",0);//显示:"光照:  %"
	OLED_ShowNum(40,4,light_intensity,2,16);//显示光照强度
	OLED_ShowCHineseWord_Line(64,4,"土湿:  %",0);//显示:"土湿:  %"
	OLED_ShowNum(104,4,soil_humi,2,16);//显示土壤湿度
	/*第4行*/
	OLED_ShowCHineseWord_Line(0,6,"PH值:  ",0);//显示:"PH值:  "
	OLED_ShowNum(40,6,soil_PH,2,16);//显示PH值
	
	if(Mode==0)//自动养护模式
	{<!-- -->
		OLED_ShowCHineseWord_Line(64,6,"自动模式",1);//显示：自动模式
		//1、空气温度过高-&gt;打开排风扇
		//2、空气湿度过高-&gt;打开排风扇
		//3、土壤湿度过低-&gt;打开补水泵
		//4、光照强度过低-&gt;打开补光灯
		if((tempdata&gt;tempdata_hight)&amp;&amp;(beep_mode==0))//默认启动报警模式
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"温度过高",1);//显示：空气温度过高-&gt;打开排风扇
			if((tempdata&gt;tempdata_hight)&amp;&amp;(beep_mode==0)&amp;&amp;(Fan_flag==0))
			{<!-- -->
				data_sta(""APP_air_temperature_alarm"", 1);//给app发布空气温度报警信息
				u3_printf("FAN_ON\r\n");//串口3发送打开风扇指令
				Fan_flag=1;//关闭排风扇启动标志位
			}
			beep_flag=1;//打开蜂鸣器开关
		}else if((tempdata_low&gt;tempdata)&amp;&amp;(beep_mode==0))
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"温度过低",1);//显示：空气温度过低
			beep_flag=1;//打开蜂鸣器开关
		}else if((humidata&gt;humidata_hight)&amp;&amp;(beep_mode==0)) 
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"湿度过高",1);//显示：空气湿度过高-&gt;打开排风扇
			if((humidata&gt;humidata_hight)&amp;&amp;(beep_mode==0)&amp;&amp;(Fan_flag==0))
			{<!-- -->
				data_sta(""APP_air_humidity_alarm"",1);//给app发布空气湿度报警信息
				u3_printf("FAN_ON\r\n");//串口3发送打开风扇指令
				Fan_flag=1;//关闭排风扇启动标志位
			}
			beep_flag=1;//打开蜂鸣器开关
		}else if((humidata_low&gt;humidata)&amp;&amp;(beep_mode==0))
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"湿度过低",1);//显示：空气湿度过低
			beep_flag=1;//打开蜂鸣器开关
		}else if((soil_humi&gt;soil_humi_hight)&amp;&amp;(beep_mode==0)) 
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"土湿过高",1);//显示：土湿过高
			beep_flag=1;//打开蜂鸣器开关
		}else if((soil_humi_low&gt;soil_humi)&amp;&amp;(beep_mode==0))
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"土湿过低",1);//显示：土湿过低
			//OLED_ShowString(64,6,"Soil Low",16);//显示土壤湿度过低-&gt;打开补水泵
			if((soil_humi_low&gt;soil_humi)&amp;&amp;(beep_mode==0)&amp;&amp;(Pump_flag==0))
			{<!-- -->
				data_sta(""APP_soil_moisture_alarm"", 1);//给app发布土壤湿度报警信息
				u3_printf("PUMP_ON\r\n");//串口3发送打开水泵指令
				Pump_flag=1;//关闭补水泵启动标志位
			}
			beep_flag=1;//打开蜂鸣器开关
		}else if((light_intensity&gt;light_intensity_hight)&amp;&amp;(beep_mode==0)) 
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"光照过高",1);//显示：光照强度过高
			beep_flag=1;//打开蜂鸣器开关
		}else if((light_intensity_low&gt;light_intensity)&amp;&amp;(beep_mode==0))
		{<!-- -->
			OLED_ShowCHineseWord_Line(64,6,"光照过低",1);//显示：光照强度过低-&gt;打开补光灯
			if((light_intensity_low&gt;light_intensity)&amp;&amp;(beep_mode==0)&amp;&amp;(Led_flag==0))
			{<!-- -->
				data_sta(""APP_light_intensity_alarm"", 1);//给app发布光照强度报警信息
				u3_printf("LED_ON\r\n");//串口3发送开灯指令
				Led_flag=1;//关闭补光灯启动标志位
			}
			beep_flag=1;//打开蜂鸣器开关
		}
		else if((soil_PH&gt;soil_PH_hight)&amp;&amp;(beep_mode==0))
		{<!-- -->
			OLED_ShowString(64,6,"PH Hig!",16);//显示土壤PH值过高-&gt;打开补水泵
			beep_flag=1;//打开蜂鸣器开关
		}else if((soil_PH_low&gt;soil_PH)&amp;&amp;(beep_mode==0))
		{<!-- -->
			OLED_ShowString(64,6,"PH Low!",16);//显示土壤PH值过低
			beep_flag=1;//打开蜂鸣器开关
		}
	}else if(Mode==1)//手动养护模式
	{<!-- -->
		OLED_ShowCHineseWord_Line(64,6,"手动模式",1);//显示：手动模式
	}
}

```

## 三、※报文处理函数※【Connet_On()】

### 1、处理SUBACK报文

当报文订阅成功之后，向服务器上报当前设备的状态，下面代码展示了本项目进行：参数阈值、LED、风扇和水泵的初始状态。

```
/*-----------------------------------------------------*/
/*                    处理SUBACK报文                   */
/*-----------------------------------------------------*/				
//if判断，第一个字节是0x90，表示收到的是SUBACK报文
//接着我们要判断订阅回复，看看是不是成功
else if(MQTT_RxDataOutPtr[2]==0x90)
{<!-- -->
	switch(MQTT_RxDataOutPtr[6])
	{<!-- -->					
			case 0x00 :
			case 0x01 : u1_printf("订阅成功\r\n");//串口输出信息
						SubcribePack_flag = 1;//SubcribePack_flag置1，表示订阅报文成功
						/*上报服务器当前设备状态*/
						Param_State();//上传阈值参数
						LED_State();//上报LED状态
						//AIDE_State();//上报语音助手状态
						FAN_State();//上报风扇状态
						PUMP_State();//上报水泵状态
						break;//跳出分支                                             
			default   : u1_printf("订阅失败，准备重启\r\n");//串口输出信息 
						Connect_flag = 0;//Connect_flag置零，重启连接
						break;//跳出分支 								
	}
}

```

### 2、处理命令缓冲区数据

在命令缓冲区进行执行订阅信息函数。

```
/*-------------------------------------------------------------*/
/*                     处理命令缓冲区数据                      */
/*-------------------------------------------------------------*/
if(MQTT_CMDOutPtr != MQTT_CMDInPtr)//if成立的话，说明命令缓冲区有数据了			  
{<!-- -->
	Publish_Message();//订阅信息函数
	MQTT_CMDOutPtr += CBUFF_UNIT;//指针下移
	if(MQTT_CMDOutPtr==MQTT_CMDEndPtr)//如果指针到缓冲区尾部了
		MQTT_CMDOutPtr = MQTT_CMDBuf[0];//指针归位到缓冲区开头				
}//处理命令缓冲区数据的else if分支结尾	

```

## 四、订阅信息函数【Publish_Message()】

`提示：以下是该项目的-&gt;订阅信息函数【Publish_Message()】，下面代码仅供参考` 用于STM32接收手机APP端进行开关灯、风扇以及水泵和调节各种阈值参数的指令！

```
/*
下发数据的样式:
命令:{"method":"thing.service.property.set","id":"1087087436","params":{"TempH":41},"version":"1.0.0"}
star_data=params":{"TempH":41},"version":"1.0.0"}
star_data+10=TempH":41},"version":"1.0.0"}
end_data=":41},"version":"1.0.0"}
*/

/*-------------------------------------------------*/
/*函数名：信息订阅函数,从服务器订阅信息              */
/*参  数：无                                       */
/*返回值：无                                       */
/*-------------------------------------------------*/
void Publish_Message(void)
{<!-- -->
	char *star_data,*end_data; //用于提取标识符
	char identifier_temp[50];//用于存放标识符
	int identifier_data;//用于存放下发的数据
	
	u1_printf("命令:%s\r\n",&amp;MQTT_CMDOutPtr[2]);//串口输出信息
	star_data=strstr((char *)MQTT_CMDOutPtr + 2, (char *)"params");
	
	/*定位得到标识符前面的字符,用于求出标识符有多大*/
	if(star_data==strstr((char *)MQTT_CMDOutPtr + 2, (char *)"params"))
  	{<!-- -->
		end_data=strstr(star_data+10,"\":");//数据尾端:end_data=":41},"version":"1.0.0"}
		memcpy(identifier_temp,star_data+10,(end_data)-(star_data+10));//将标识符提取
		identifier_data = Extract_digit((unsigned char *)end_data+2); //得到下发的数据
		u1_printf("end_data+2为：%s\r\n", end_data+2);//串口输出信息
		u1_printf("identifier_data为：%d\r\n", identifier_data);//串口输出信息
		
		//*空气温湿度、土壤湿度、光照强度和土壤PH值参数修改区*//
		if(!(strcmp(identifier_temp,""APP_Temp_Hight"")))
		{<!-- -->
			tempdata_hight = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Temp_Low"")))
		{<!-- -->
			tempdata_low = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Humi_Hight"")))
		{<!-- -->
			humidata_hight = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Humi_Low"")))
		{<!-- -->
			humidata_low = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Soilhumi_Hight"")))
		{<!-- -->
			soil_humi_hight = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Soilhumi_Low"")))
		{<!-- -->
			soil_humi_low = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Light_Intensity_Hight"")))
		{<!-- -->
			light_intensity_hight = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Light_Intensity_Low"")))
		{<!-- -->
			light_intensity_low = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Soil_PH_Hight"")))
		{<!-- -->
			soil_PH_hight = identifier_data;
		}else if(!(strcmp(identifier_temp,""APP_Soil_PH_Low"")))
		{<!-- -->
			soil_PH_low = identifier_data;
		}
		memset(identifier_temp, 0, 255);
	}
	
	//*补光灯、风扇、水泵控制区*//
	if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"fill_light\":1}"))//如果搜索到"params":{"fill_light":1}说明服务器下发打开开关1
	{<!-- -->
		//LED1_ON;//打开LED
		u3_printf("LED_ON\r\n");//串口3发送开灯指令
		LED_State();//判断补光灯状态,并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"fill_light\":0}"))//如果搜索到"params":{"fill_light":0}说明服务器下发关闭开关1
	{<!-- -->
		//LED1_OFF;//关闭LED
		u3_printf("LED_OFF\r\n");//串口3发送关灯指令
		LED_State();//判断补光灯状态,并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"Voice_Assistant\":1}"))//如果搜索到"params":{"Voice_Assistant":1}说明服务器下发打开开关2
	{<!-- -->
		//LED2_ON;//打开语音助手
		u3_printf("AIDE_ON\r\n");//串口3发送打开语音助手指令
		AIDE_State();//判断开关状态，并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"Voice_Assistant\":0}"))//如果搜索到"params":{"Voice_Assistant":0}说明服务器下发关闭开关2
	{<!-- -->
		//LED2_OFF;//关闭语音助手
		u3_printf("AIDE_OFF\r\n");//串口3发送关闭语音助手指令
		AIDE_State();//判断开关状态，并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"exhaust_fan\":1}"))//如果搜索到"params":{"exhaust_fan":1}说明服务器下发打开开关3
	{<!-- -->
		//LED3_ON;//打开风扇
		u3_printf("FAN_ON\r\n");//串口3发送打开风扇指令
		FAN_State();//判断风扇状态，并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"exhaust_fan\":0}"))//如果搜索到"params":{"exhaust_fan":0}说明服务器下发关闭开关3
	{<!-- -->
		//LED3_OFF;//关闭风扇
		u3_printf("FAN_OFF\r\n");//串口3发送关闭风扇指令
		FAN_State();//判断风扇状态，并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"small_pump\":1}"))//如果搜索到"params":{"small_pump":1}说明服务器下发打开开关4
	{<!-- -->
		//LED4_ON;//打开水泵
		u3_printf("PUMP_ON\r\n");//串口3发送打开水泵指令
		PUMP_State();//判断水泵状态，并发布给服务器
	}else if(strstr((char *)MQTT_CMDOutPtr+2,"\"params\":{\"small_pump\":0}"))//如果搜索到"params":{"small_pump":0}说明服务器下发关闭开关4
	{<!-- -->
		//LED4_OFF;//关闭水泵
		u3_printf("PUMP_OFF\r\n");//串口3发送关闭水泵指令
		PUMP_State();//判断水泵状态，并发布给服务器
	}
}

```

## 五、各设备状态上传服务器函数

`提示：以下是该项目的-&gt;各设备状态上传服务器函数【Param_State()】【LED_State()】【FAN_State()】【PUMP_State()】，下面代码仅供参考`

### 1、各种参数数据状态上传函数

```
/*-------------------------------------------------*/
/*函数名：上传各种参数数据的任务                   */
/*参  数：无                                       */
/*返回值：无                                       */
/*-------------------------------------------------*/
void Param_State(void)
{<!-- -->
	char temp[TBUFF_UNIT];//缓冲区
	sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\
	\"tempdata_hight\":%d,\"tempdata_low\":%d,\"humidata_hight\":%d,\"humidata_low\":%d,\"soil_humi_hight\":%d,\
	\"soil_humi_low\":%d,\"light_intensity_hight\":%d,\"light_intensity_low\":%d,\"soil_PH_hight\":%d,\"soil_PH_low\":%d},\
	\"version\":\"1.0.0\"}",tempdata_hight,tempdata_low,humidata_hight,humidata_low,soil_humi_hight,soil_humi_low,light_intensity_hight,light_intensity_low,soil_PH_hight,soil_PH_low);//构建数据
	MQTT_PublishQs0(P_TOPIC_NAME,temp,strlen(temp));//添加数据到发送缓冲区
}

```

### 2、LED状态上传函数

```
/*-------------------------------------------------*/
/*函数名：判断LED的状态，并发布给服务器              */
/*参  数：无                                       */
/*返回值：无                                       */
/*-------------------------------------------------*/
void LED_State(void)
{<!-- -->
	char temp[TBUFF_UNIT];//定义一个临时缓冲区
	if(LED_STA==1) sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\"fill_light\":1},\"version\":\"1.0.0\"}");
	else            sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\"fill_light\":0},\"version\":\"1.0.0\"}");
	MQTT_PublishQs0(P_TOPIC_NAME,temp,strlen(temp));//添加数据，发布给服务器	
}

```

### 2、风扇状态上传函数

```
/*-------------------------------------------------*/
/*函数名：判断风扇状态，并发布给服务器               */
/*参  数：无                                       */
/*返回值：无                                       */
/*-------------------------------------------------*/
void FAN_State(void)
{<!-- -->
	char temp[TBUFF_UNIT];//定义一个临时缓冲区
	if(FAN_STA==1) sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\"exhaust_fan\":1},\"version\":\"1.0.0\"}");
	else            sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\"exhaust_fan\":0},\"version\":\"1.0.0\"}");
	MQTT_PublishQs0(P_TOPIC_NAME,temp,strlen(temp));//添加数据，发布给服务器		
}

```

### 2、水泵状态上传函数

```
/*-------------------------------------------------*/
/*函数名：判断水泵状态，并发布给服务器              */
/*参  数：无                                       */
/*返回值：无                                       */
/*-------------------------------------------------*/
void PUMP_State(void)
{<!-- -->
	char temp[TBUFF_UNIT];//定义一个临时缓冲区
	if(PUMP_STA==1) sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\"small_pump\":1},\"version\":\"1.0.0\"}");
	else            sprintf(temp,"{\"method\":\"thing.event.property.post\",\"id\":\"203302322\",\"params\":{\"small_pump\":0},\"version\":\"1.0.0\"}");
	MQTT_PublishQs0(P_TOPIC_NAME,temp,strlen(temp));//添加数据，发布给服务器		
}

```

## 总结

【工程链接】：https://oshwhub.com/wyb1661463799/zhi-neng-zhi-wu-yang-hu-ji-tong-she-ji 【代码链接】：https://www.wcfaka.com/details/AE408673 【项目备注】：原理图和PCB见上方的【工程链接】，希望该设计能够为大家提供一些帮助，同时也感谢大家一键三连对UP的支持。最新代码暂不更新，有需要的可以点击上方【代码链接】获取哦！ 下面是视频介绍：



历时一个月的毕业设计—硬件部分介绍

历时一个月的毕业设计成果演示（一）





历时一个月的毕业设计成果演示（二）


