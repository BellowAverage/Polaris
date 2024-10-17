
--- 
title:  STM32固件库控制LED灯 
tags: []
categories: [] 

---
STM32系列专为要求高性能、低成本、低功耗的嵌入式应用设计的ARM Cortex®-M0，M0+，M3, M4和M7内核 （ST's product portfolio contains a comprehensive range of microcontrollers, from robust, low-cost 8-bit MCUs up to 32-bit ARM-based Cortex®-M0 and M0+, Cortex®-M3, Cortex®-M4 Flash microcontrollers with a great choice of peripherals. ST has also extended this range to include an ultra-low-power MCU platform。

点亮发光二极管STM32嵌入式程序，程序代码并没有全部使用固件库，通过控制GPIOx寄存器组的方式对GPIO的端口进行控制，文本将使用固件库来控制GPIOx寄存器组。

#### STM32的时钟系统

STM32芯片通过复杂的时钟系统实现了低功耗，对外设的启用都是通过时钟来控制，若要启用某外部设备，需要先开启该外部设备对应的时钟。

STM32提供了四个时钟源：
-  高速外部时钟（HSE）：以外部晶振作为时钟源，晶振频率范围可取4~16MHZ，一般采用8MHZ的晶振。 -  高速内部时钟（HSI）：由内部RC震荡器产生，频率为8MHZ，但不够稳定。 -  低俗外部时钟（LSE）：以外部晶振作为时钟源，主要提供给实时时钟模块，一般采用32.768KHZ。 -  低速内部时钟（LSI）：由内部RC震荡器产生，也提供给实时时钟模块，频率一般为40KHZ。 
本文内容主要涉及到GPIOx时钟，GPIOx时钟由高速外部时钟经过9倍的倍频后，进入AHB预分频器，由AHB预分频器再进入APB1、APB2预分频器。GPIOx是挂载在APB2总线上的，APB2的时钟是APB2预分频器的输出，因此GPIOx的时钟频率即为APB2预分频器的输出频率。例如：若高速外部时钟频率为8MHZ，经过9倍的倍频后为72MHZ，若配置AHB、APB2不分频，则GPIOx时钟频率为72MHZ。

STM32提供的分频机制解决了总线匹配高速外设和低速外设的问题，每个外设都配备了外设时钟的开关，当我们不使用某个外设时，可以把这个外设时钟关闭，从而降低STM32的整体功耗，要启用外设时，一定要记得开启外设的时钟。

STM32固件库提供了开启和关闭外设时钟的封装函数：

void RCC_APB2PeriphClockCmd(uint32_t RCC_APB2Periph, FunctionalState NewState)

该函数在stm32f10x_rcc.c定义，参数RCC_APB2Perip是一个无符号32位整数，该参数给出了要启用和关闭的外设，其值在stm32f10x_rcc.h定义：

#define RCC_APB2Periph_GPIOA ((uint32_t)0x00000004)

#define RCC_APB2Periph_GPIOB ((uint32_t)0x00000008)

#define RCC_APB2Periph_GPIOC ((uint32_t)0x00000010)

#define RCC_APB2Periph_GPIOD ((uint32_t)0x00000020)

#define RCC_APB2Periph_GPIOE ((uint32_t)0x00000040)

#define RCC_APB2Periph_GPIOF ((uint32_t)0x00000080)

#define RCC_APB2Periph_GPIOG ((uint32_t)0x00000100)

参数NewState是枚举类型，在stm32f10x.h定义，其定义如下：

typedef enum {DISABLE = 0, ENABLE = !DISABLE} FunctionalState;

若NewState为ENABLE则启用RCC_APB2Periph指定的外设时钟，否则关闭RCC_APB2Periph指定的外设时钟。

#### STM32固件库对寄存器的封装

STM32用结构体的形式封装了寄存器组，在stm32f10x.h文件中，对GPIO的封装如下：

#define GPIOA ((GPIO_TypeDef *) GPIOA_BASE)





#define GPIOB ((GPIO_TypeDef *) GPIOB_BASE)





#define GPIOC ((GPIO_TypeDef *) GPIOC_BASE)





其中GPIOA_BASE是GPIOA寄存器组的基地址，GPIOx_BASE定义如下：





#define GPIOA_BASE (APB2PERIPH_BASE + 0x0800)





#define GPIOB_BASE (APB2PERIPH_BASE + 0x0C00)





#define GPIOC_BASE (APB2PERIPH_BASE + 0x1000)





#define GPIOD_BASE (APB2PERIPH_BASE + 0x1400)





APB2PERIPH_BASE是APB2总线外设的基地址，GPIOx是挂载在APB2总线上，因此通过宏GPIOx_BASE我们就可以得到GPIOx组的基地址，GPIOx宏将基地址转换为GPIO_TypeDef 结构，该结构同样在stm32f10x.h文件中被定义：





typedef struct





{<!-- -->





__IO uint32_t CRL;





__IO uint32_t CRH;





__IO uint32_t IDR;





__IO uint32_t ODR;





__IO uint32_t BSRR;





__IO uint32_t BRR;





__IO uint32_t LCKR;





} GPIO_TypeDef;





它是一个C结构体，结构体内定义了7个__IO uint32_t的变量，这些变量都是32位，即每个变量占4个字节的存储空间，每个变量对应GPIOx的一个寄存器地址。若需要修改某个寄存器的值，可以使用下面类似代码：





GPIO_TypeDef* GPIOx; // 定义GPIO_TypeDef结构体
