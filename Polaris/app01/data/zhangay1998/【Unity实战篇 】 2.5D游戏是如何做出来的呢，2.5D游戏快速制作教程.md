
--- 
title:  【Unity实战篇 】| 2.5D游戏是如何做出来的呢，2.5D游戏快速制作教程 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">



####  
- <ul><li><ul><li>- - - - - <ul><li>- 


<img src="https://img-blog.csdnimg.cn/b51b61c05c284ed1bfd51798b877e405.png" alt="请添加图片描述">

#### 前言
- 玩过游戏的朋友都知道，市面上最常见的游戏多数分为2D和3D两种。- 2D和3D游戏之间的差异大家都知道，一个是类似纸片游戏属于二维层面，另一个则是在3D立体空间中游玩。- 其中还夹杂着一个`2.5D游戏`，本篇文章就来讲一下怎么通过Unity进行2.5D游戏是怎样的以及如何制作2.5D游戏。- 制作方法很简单，文中使用到了`Tile Map`制作2D地图，通过控制相机角度来形成伪3D来制作2.5D效果的游戏。- 下面就一起来看看到底是怎样制作的吧！
## <font color="#ff6984" size="5"> 【Unity实战篇 】</font> | 如何制作一款2.5D游戏，2.5D游戏制作案例

### 一、2.5D 游戏概念

`2.5D游戏` 是一种介于二维和三维之间的游戏形式。它通常在二维平面上展示游戏内容，但利用三维技术来实现更加逼真的图像效果。

在2.5D游戏中，角色和环境通常是以平面的形式呈现，但可以在垂直方向上移动。这意味着玩家可以在一个相对较薄的虚拟空间内进行自由探索和交互，同时享受到更加立体感的视觉效果。

与传统的二维游戏相比，2.5D游戏可以通过使用透视、光影效果和深度感等技术来增强场景的真实感。这为玩家提供了更好的沉浸式体验，同时保留了传统2D游戏的简单和直观性。

许多平台游戏、角色扮演游戏和冒险游戏都采用了2.5D的形式，从而使玩家能够在一个相对较小的空间内尽情探索。2.5D游戏的发展也受益于技术的进步，使得游戏制作人员能够创建更加精美、逼真的图像效果，为玩家带来更好的游戏体验。

这种类型的游戏在平台游戏、动作游戏和冒险游戏等类型中比较常见， 例如`八方旅人/歧路旅人`这种游戏就是2.5D这类游戏的标杆之作了。 <img src="https://img-blog.csdnimg.cn/08b4533dc00046be8c3640c97d41c248.png" alt="在这里插入图片描述">



八方旅人画面演示



下面来看一下在Unity中如何制作一款2.5D的游戏吧！ <img src="https://img-blog.csdnimg.cn/cb804c151349440dbee4446b70c28f29.gif" alt="请添加图片描述">

### 二、绘制地图

首先我们需要搭建一个地图用于游戏测试，这里使用Unity的 `Tile Map Editor` 来搭建地图。

`Tile Map Editor` 的使用方法也很简单，可以看这篇文章学习下怎样使用`Tile Map` 快速搭建一个地图。 

<img src="https://img-blog.csdnimg.cn/20ccdadd6d0f43a08b21682896d893c6.gif" alt="请添加图片描述">

层级需要特别注意，这里把 `TileMap Renderer` 的 `Order in Layer` 设置为0，这一层用于最下层背景显示，防止遮盖到其他对象。

搭建好的地图如下所示： <img src="https://img-blog.csdnimg.cn/fa348599688a46db9e0ab37cceb370d0.png" alt="在这里插入图片描述">

此时还需要在地图中增加一些场景物品，如大树、石头等等。

这里在面板中右键 `2D Object -&gt; Sprite ` 创建一个Sprite，然后在Sprite Renderer中设置想要的场景物体精灵图即可，这里要把 `Order in Layer` 设置为1，否则会看不到新创建的对象。 <img src="https://img-blog.csdnimg.cn/44fc5d4a66454e538a3f947888c24f47.png" alt="在这里插入图片描述">

同时 要给这些添加的场景物品增加碰撞器，让玩家不能穿过该物体。 <img src="https://img-blog.csdnimg.cn/87fd03c818014020aeef2152745282da.png" alt="在这里插入图片描述">

下面是添加完场景物品后的地图，看起来内容丰富了不少，效果好了很多。 <img src="https://img-blog.csdnimg.cn/635fe0fc3bb74ef0a16e28a64c7a1f7e.png" alt="在这里插入图片描述">

在场景中新建一个游戏对象`InteractionObject`，将这些新建的场景物体全部放到InteractionObject对象下当做子物体，方便后期统一处理。

### 三、添加玩家动画和移动等操作

接下来再创建一个Sprite作为玩家，将 `Order in Layer 层级` 设置为1，并给玩家添加 `Rigidbody2D刚体` 和 `Collider碰撞体`并适当的调整大小。 <img src="https://img-blog.csdnimg.cn/f23c2f48ad75469c9a466054416f3ac9.png" alt="在这里插入图片描述">

接下来在Project下右键 `Create -&gt; Animatior Controller`创建一个 `Animatior Controller` 用来管理玩家的动画，主要有 上、下、左、右移动和默认的Idle动画。

点开Animatior面板后创建两个 `BlendTree混合树` 。 <img src="https://img-blog.csdnimg.cn/46d0bf3f3de04ef58c8bcb1cf1403183.png" alt="在这里插入图片描述">

接下来在Animator面板创建两个 Float类型的参数 InputX 和 InputY 用来在混合树中接收使用。 <img src="https://img-blog.csdnimg.cn/37d380fa35eb4a799790d9d5efda17b3.png" alt="在这里插入图片描述">

双击点开Idle混合树，将`Blend Type`设置为 `2D Simple Doirectional`，这样我们就有两个参数用来表示二维平面上移动。 <img src="https://img-blog.csdnimg.cn/c5f2d30be5234fe58a06532566f34be4.png" alt="在这里插入图片描述">

然后点击混合树面板的 `+` 添加四个`Motion`，分别将Idle的上、下、左、右动画添加上去，并将对应的PosX和PosY数值添加上去。

这里的PosX和PosY代表分别代表玩家按下X轴和Y轴的方向。

例如 PosX为1时代表玩家按下右方向键 此时X轴上的值为1，所以播放Idle_Right动画； PosY为1时代表玩家按下上方向键 此时Y轴上的值为1，所以播放Idle_Back动画。 <img src="https://img-blog.csdnimg.cn/67d9052651f44943a73b54e4db035454.png" alt="在这里插入图片描述">

动画需要自己找资源配套使用哦！ <img src="https://img-blog.csdnimg.cn/5efbe3bfdf6f455f9683397c14c08819.png" alt="在这里插入图片描述">

同样的操作给Walk混合树也配置一下。 <img src="https://img-blog.csdnimg.cn/7db7311e3f3d4a749ee46ffaf6264815.png" alt="在这里插入图片描述">

然后在Animator面板继续添加一个Bool类型的参数 `IsMove`，用来控制玩家的Idle和Walk状态的切换。 <img src="https://img-blog.csdnimg.cn/c0446ad4e5ad4bc09d8c5162148dccbd.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/151b93ba121d4a159bb0789fe3c90b95.png" alt="在这里插入图片描述">

这样我们角色的动画就算配置好了，接下来写代码完成角色的移动方法和动画的播放就好了。

如果动画这块还不是很明白的话，也可以再去学习一下Unity中的动画相关知识： 

创建一个脚本PlayerMovement ，将其挂载到玩家身上。

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{<!-- -->
    public float speed;
    new private Rigidbody2D rigidbody;
    private Animator animator;
    private float inputX, inputY;
    private float stopX, stopY;

    void Start()
    {<!-- -->
        rigidbody = GetComponent&lt;Rigidbody2D&gt;();
        animator = GetComponent&lt;Animator&gt;();
    }

    void Update()
    {<!-- -->
        inputX = Input.GetAxisRaw("Horizontal");
        inputY = Input.GetAxisRaw("Vertical");
        
        //让玩家根据自己本地坐标进行向量计算
        Vector2 input = (transform.right * inputX + transform.up * inputY).normalized;
        rigidbody.velocity = input * speed;

        if (input != Vector2.zero)
        {<!-- -->
            animator.SetBool("IsMove", true);
            stopX = inputX;
            stopY = inputY;
        }
        else
        {<!-- -->
            animator.SetBool("IsMove", false);
        }
        animator.SetFloat("InputX", stopX);
        animator.SetFloat("InputY", stopY);

    }
}

```

可以选择将Main Camera放到玩家对象当做子物体，这样玩家移动时相机也可以跟着玩家移动，此时运行程序进行测试。 <img src="https://img-blog.csdnimg.cn/c84edcca876f4876a70607d761c2a4df.gif" alt="请添加图片描述">

可以看到，此时的游戏画面就是单纯的2D游戏画面，看起来也没有2.5D的既视感，所以还需要对相机进行设置。

### 四、视角配置

#### 4.1 调整摄像机与场景对象的角度

相机的设置其实很简单，只需要让其视选择45°，以俯视角的视角来观看场景。

先来新建一个游戏对象`CameraPosition`，将MainCamera放到该物体下作为子对象，再将MainCamera的Rotation设置为（-45,0，0），Position的数值可以根据搭建的地图进行微调，新建一个脚本`RotatingCamera`挂载到该对象上。

该脚本的作用是让相机一直跟随玩家移动，脚本内容如下：

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RotatingCamera : MonoBehaviour
{<!-- -->
    private Transform player;
    void Start()
    {<!-- -->
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }

    void Update()
    {<!-- -->
        transform.position = player.position;
    }
}

```

再新建一个脚本`FacingCamera`，将其挂载到前面搭建的场景对象的父物体`InteractionObject`上。

该脚本的作用是让该对象下的所有子物体的角度始终与相机的旋转角度对齐，代码如下：

```
using UnityEngine;

public class FacingCamera : MonoBehaviour
{<!-- -->
    Transform[] childs;
    void Start()
    {<!-- -->
        childs = new Transform[transform.childCount];
        for (int i = 0; i &lt; transform.childCount; i++)
        {<!-- -->
            childs[i] = transform.GetChild(i);
        }
    }

    void Update()
    {<!-- -->
        for (int i = 0; i &lt; childs.Length; i++)
        {<!-- -->
            childs[i].rotation = Camera.main.transform.rotation;
        }
    }
}

```

此时运行游戏查看效果： <img src="https://img-blog.csdnimg.cn/4cf5e1b501ba4be4837bfeb696a1e9ac.gif" alt="请添加图片描述">

#### 4.2 增加镜头旋转功能

在有些2.5D游戏中还支持镜头的旋转，这里也加上这个功能看一下效果。

首先要修改RotatingCamera的代码：

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RotatingCamera : MonoBehaviour
{<!-- -->
    public float rotateTime = 0.2f;
    private Transform player;
    private bool isRotating = false;
    void Start()
    {<!-- -->
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }

    void Update()
    {<!-- -->
        transform.position = player.position;

        Rotate();
    }

    void Rotate()
    {<!-- -->
        if (Input.GetKeyDown(KeyCode.Q) &amp;&amp; !isRotating)
        {<!-- -->
            StartCoroutine(RotateAround(-45, rotateTime));
        }
        if (Input.GetKeyDown(KeyCode.E) &amp;&amp; !isRotating)
        {<!-- -->
            StartCoroutine(RotateAround(45, rotateTime));
        }
    }

    IEnumerator RotateAround(float angel, float time)
    {<!-- -->
        float number = 60 * time;
        float nextAngel = angel / number;
        isRotating = true;

        WaitForFixedUpdate wait = new WaitForFixedUpdate();
        for (int i = 0; i &lt; number; i++)
        {<!-- -->
            transform.Rotate(new Vector3(0, 0, nextAngel));
            yield return wait;
        }

        isRotating = false;
    }
}

```

加入一个按下 Q/E 键进行旋转的方法，通过协程每次按下时旋转45°，此时就大功告成了，下面一起看一下最终效果。 <img src="https://img-blog.csdnimg.cn/cb804c151349440dbee4446b70c28f29.gif" alt="请添加图片描述">

### 五、游戏效果展示

下面是2D风格 和 2.5D风格的对比，相对于2D画面，此处的2.5D仅仅是增加了一个相机的拍摄角度，画面风格看起来就有挺大的差异。

|2D风格|2.5D风格
|------
|<img src="https://img-blog.csdnimg.cn/c84edcca876f4876a70607d761c2a4df.gif" alt="请添加图片描述">|<img src="https://img-blog.csdnimg.cn/cb804c151349440dbee4446b70c28f29.gif" alt="请添加图片描述">

真正在制作2.5D游戏时，有非常多的细节需要处理，对于美术风格的标准要求也比较高，制作出来的画面也会更加好看。

<img src="https://img-blog.csdnimg.cn/0f9d103227514ba3a1b2a69f794958fa.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1389f9960ffd4277a53ba125ea4e406f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0fec92e4b0c84b94bb890189ca162e2f.png" alt="在这里插入图片描述">

## 总结
- 本文讲了一下关于2.5D游戏及其制作方法的演示。- 关于2.5D很多人的说法都不同，制作方案也有很多种，本文演示的也只是其中的一种解决方案。- 主要还是让大家了解一下关于2.5D的知识，以及简单的制作方法，不至于在提及2.5D游戏时一脸茫然。
>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创 🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">

<font color="#ff6984" size="5"> **资料白嫖，技术互助**</font>

|学习路线指引（点击解锁）|知识定位|人群定位
|------
||入门级|本专栏从Unity入门开始学习，快速达到Unity的入门水平
||进阶级|计划制作Unity的 100个实战案例！助你进入Unity世界，争取做最全的Unity原创博客大全。
||难度偏高|分享学习一些Unity成品的游戏Demo和其他语言的小游戏！
||互助/吹水|数万人游戏爱好者社区，聊天互助，白嫖奖品
||Unity查漏补缺|针对一些Unity中经常用到的一些小知识和技能进行学习介绍，核心目的就是让我们能够快速学习Unity的知识以达到查漏补缺

<img src="https://img-blog.csdnimg.cn/20210613033645219.gif#pic_center" alt="在这里插入图片描述">
