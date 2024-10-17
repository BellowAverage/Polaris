
--- 
title:  AI之Sora：Sora(文本指令生成视频的里程碑模型)的简介(能力/安全性/技术细节)、使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
AI之Sora：Sora(文本指令生成视频的里程碑模型)的简介(能力/安全性/技术细节)、使用方法、案例应用之详细攻略



>  
 **<strong>导读**</strong>：Sora 是OpenAI研发的一个可以根据文字描述生成视频的AI模型。它的主要特性、功能以及OpenAI在安全和应用方面的策略的核心要点如下所示： 
 ****<strong><em>核心功能****</em></strong> 
 &gt;&gt; Sora可以根据文字描述直接生成视频，这种能力可以帮助人们用文字来传达想法和创造内容。能够根据用户提供的详细文字描述生成符合描述要求的视频。 
 &gt;&gt; Sora可以生成长达一分钟的视频，保证视频质量和符合用户描述。它还可以扩展已有视频为更长时间。 
 &gt;&gt; Sora不仅可以生成单个视频，还能够将已有视频或图片进行延续和补全， 确保目标即使暂时消失在视线之外也保持不变。 
 &gt;&gt; Sora可以生成包含多个场景和角色的复杂视频，角色表达会贯穿始终。它也可以基于图片生成视频。 
 ****<strong><em>核心技术****</em></strong> 
 &gt;&gt; Sora采用类似GPT的Transformer网络结构，它可以处理不同时长、分辨率和格式的视觉数据，可以很好地体现出深度学习模型在视觉领域的应用前景。 
 &gt;&gt; Sora采用DALL-E 3的重新描述技术，能够更好地根据用户文字描述中的细节生成视频内容。 
 &gt;&gt; OpenAI将进一步开展安全测试，同时构建检测模型识别生成视频的真实性。在产品化前将采取一系列措施防止滥用。 
 ****<strong><em>未来与影响****</em></strong> 
 &gt;&gt; OpenAI正在与相关机构合作，通过对抗测试来提升Sora识别误导内容和存在偏差的能力，以确保安全应用。OpenAI将与政府、教育机构等合作，研究如何将该技术应用于更多积极场景，同时防止滥用。 
 &gt;&gt; Sora可视为实现通用人工智能的一个里程碑，它可以更好地理解和模拟现实世界。将来Sora可能会用于开发更高水平的AI，例如通用人工智能。这需要不断完善技术并学习用户实际应用情况。 
 总体来说，Sora代表了视觉语言模型在视频生成领域的重要进步。它同时也将会面临一些技术挑战，例如复杂场景中的物理模拟效果需要进一步改进。OpenAI将持续跟进Sora的安全性研究工作。 




**目录**



















































































































## **相关文章**

### **<strong><strong>AI之Sora：Sora(文本指令生成视频的里程碑模型)的简介(能力/安全性/技术细节)、使用方法、案例应用之详细攻略**</strong></strong>





### **<strong><strong>VGM之Sora：OpenAI重磅发布一款“炸天”的视频生成模型—《Video generation models as world simulators视频生成模型作为世界模拟器》翻译与解读**</strong></strong>









## **Sora****的简介**

2024年2月16日，OpenAI重磅发布一款“炸天”的**<strong>视频生成模型**</strong>—Sora。Sora是一种**<strong>人工智能模型**</strong>，从文本创建视频，可以根据文本指令创建逼真和富有想象力的场景。本页所有视频均由Sora直接生成，未经修改。



### **<strong><strong>Capabilities**</strong>**<strong>功能**</strong></strong>

我们正在教人工智能理解和模拟**<strong>运动中**</strong>的物理世界，目标是训练模型，帮助人们解决需要与现实世界互动的问题。



#### **<strong><strong>Sora可以生成长达一分钟的视频**</strong></strong>

介绍Sora，我们的文本转视频模型。Sora可以生成长达一分钟的视频，同时保持视觉质量并遵守用户的提示。





##### **<strong><strong>Prompt: A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse. She wears sunglasses and red lipstick. She walks confidently and casually. The street is damp and reflective, creating a mirror effect of the colorful lights. Many pedestrians walk about.一个时尚的女人走在东京的街道上，到处都是温暖发光的霓虹灯和动态**</strong>**<strong>的**</strong>**<strong>城市标识。她穿着一件黑色皮夹克，一条长长的红色连衣裙，黑色靴子，背着一个黑色手提包。她戴着墨镜，涂着红色口红。她走起路来自信而随意。街道是潮湿和反光的，产生了五彩灯光的镜像效果。许多行人在街上走来走去。**</strong></strong>

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/24fe9f86e59041628289be8fb238ae1f.gif" width="847">

**原视频地址：**



##### **<strong><strong>Prompt: Several giant wooly mammoths approach treading through a snowy meadow, their long wooly fur lightly blows in the wind as they walk, snow covered trees and dramatic snow capped mountains in the distance, mid afternoon light with wispy clouds and a sun high in the distance creates a warm glow, the low camera view is stunning capturing the large furry mammal with beautiful photography, depth of field.几只巨大的长毛猛犸象穿过一片白雪覆盖的草地，它们长长的毛茸茸的皮毛在风中轻轻飘动，远处是被雪覆盖的树木和雪山，午后的光线与缕缕的云和远处的太阳创造了温暖的光芒，低角度的摄像机视角令人惊叹地捕捉到了这只大型毛茸茸的哺乳动物，配以美丽的摄影，景深效果。**</strong></strong>

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/2f414ac3ed4a4fc293a7c006afca9ca6.gif" width="847">

**原视频地址：**



##### **<strong><strong>Prompt: A movie trailer featuring the adventures of the 30 year old space man wearing a red wool knitted motorcycle helmet, blue sky, salt desert, cinematic style, shot on 35mm film, vivid colors.这是一部电影预告片，讲述了30岁的太空人戴着红色羊毛针织摩托车头盔的冒险经历，蓝天，盐沙漠，电影式风格，用35mm胶片拍摄，色彩鲜艳。**</strong></strong>

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/a946b8a198354a92a5be9344038c0682.gif" width="847">

**原视频地址：**



##### **<strong><strong>Prompt: Drone view of waves crashing against the rugged cliffs along Big Sur’s garay point beach. The crashing blue waters create white-tipped waves, while the golden light of the setting sun illuminates the rocky shore. A small island with a lighthouse sits in the distance, and green shrubbery covers the cliff’s edge. The steep drop from the road down to the beach is a dramatic feat, with the cliff’s edges jutting out over the sea. This is a view that captures the raw beauty of the coast and the rugged landscape of the Pacific Coast Highway.无人机拍摄的海浪冲击着Big Sur的Garay Point海滩上崎岖的悬崖。蓝色的海水拍打着白色的波浪，夕阳的金色光芒照亮了岩石海岸。远处有一座小岛，岛上有一座灯塔，悬崖边上长满了绿色的灌木丛。从公路到海滩的陡峭落差是一个壮观的壮举，悬崖的边缘突出在海面上。这是一幅捕捉到海岸原始美景和太平洋海岸公路崎岖的风景。**</strong></strong>

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/39cc4e12f9b648f5a3d81984543dc87b.gif" width="847">

**原视频地址：**





##### **<strong><strong>Prompt: Animated scene features a close-up of a short fluffy monster kneeling beside a melting red candle. The art style is 3D and realistic, with a focus on lighting and texture. The mood of the painting is one of wonder and curiosity, as the monster gazes at the flame with wide eyes and open mouth. Its pose and expression convey a sense of innocence and playfulness, as if it is exploring the world around it for the first time. The use of warm colors and dramatic lighting further enhances the cozy atmosphere of the image.动画场景展示了一个矮矮的毛绒怪物跪在一个融化的红色蜡烛旁边的特写镜头。艺术风格是3D和逼真的，重点放在光线和质感上。这幅画的气氛是一种惊奇和好奇，怪物用着大眼睛和张开的嘴巴凝视着火焰。它的姿势和表情传达了一种天真和顽皮的感觉，好像它是第一次探索周围的世界。温暖色调和戏剧性的光线进一步增强了图像的舒适氛围。**</strong></strong>

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/ca81b1387caa48558ddabbfbe76b7467.gif" width="847">

**原视频地址：**





#### **<strong><strong>创意**</strong></strong>

今天，Sora已经开始向红队成员提供服务，以评估危害或风险的关键领域。我们还向许多视觉艺术家、设计师和电影制作人提供了访问权限，以获取如何推进模型对创意专业人士最有帮助的反馈。

我们正在尽早分享我们的研究进展，以便开始与OpenAI之外的人合作，并从他们那里获得反馈，让公众了解即将出现的AI功能。





##### **<strong><strong>Prompt: Historical footage of California during the gold rush.淘金热时期加州的历史镜头。**</strong></strong>

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/913c8220838c41a0b1b06ad2da2f0f36.gif" width="847">

**原视频地址：**



##### **<strong><strong>Prompt: A close up view of a glass sphere that has a zen garden within it. There is a small dwarf in the sphere who is raking the zen garden and creating patterns in the sand.一个玻璃球的近景，里面有一个禅宗花园。球体中有一个小矮人正在耙禅宗花园，并在沙子上创造图案。**</strong></strong>



**原视频地址：**







##### **<strong><strong>Prompt: Extreme close up of a 24 year old woman’s eye blinking, standing in Marrakech during magic hour, cinematic film shot in 70mm, depth of field, vivid colors, cinematic一个24岁的女人眨着眼睛的极端特写，站在马拉喀什的神奇时刻，电影胶片拍摄在70mm，景深，生动的色彩，电影**</strong></strong>

**原视频地址：**



##### **<strong><strong>Prompt: A cartoon kangaroo disco dances.一只卡通袋鼠跳迪斯科。**</strong></strong>

**原视频地址：**



##### **<strong><strong>Prompt: A beautiful homemade video showing the people of Lagos, Nigeria in the year 2056. Shot with a mobile phone camera.一个美丽的自制视频，展示了2056年尼日利亚拉各斯的人们。用手机相机拍摄的。**</strong></strong>

**原视频地址：**







##### **<strong><strong>Prompt: A petri dish with a bamboo forest growing within it that has tiny red pandas running around.一个培养皿，里面生长着竹林，小熊猫在里面跑来跑去。**</strong></strong>

**原视频地址：**



##### **<strong><strong>Prompt: The camera rotates around a large stack of vintage televisions all showing different programs — 1950s sci-fi movies, horror movies, news, static, a 1970s sitcom, etc, set inside a large New York museum gallery.镜头围绕着一大堆老式电视旋转，这些电视都在播放不同的节目——20世纪50年代的科幻电影、恐怖电影、新闻、静态、70年代的情景喜剧等，背景设在纽约一家大型博物馆的画廊里。**</strong></strong>

**原视频地址：**



##### **<strong><strong>Prompt: 3D animation of a small, round, fluffy creature with big, expressive eyes explores a vibrant, enchanted forest. The creature, a whimsical blend of a rabbit and a squirrel, has soft blue fur and a bushy, striped tail. It hops along a sparkling stream, its eyes wide with wonder. The forest is alive with magical elements: flowers that glow and change colors, trees with leaves in shades of purple and silver, and small floating lights that resemble fireflies. The creature stops to interact playfully with a group of tiny, fairy-like beings dancing around a mushroom ring. The creature looks up in awe at a large, glowing tree that seems to be the heart of the forest.3D动画，一个小的，圆的，毛茸茸的生物，有一双大而富有表现力的眼睛，探索充满活力的魔法森林。这种动物是兔子和松鼠的异想天开的混合体，有着柔软的蓝色皮毛和浓密的条纹尾巴。它沿着波光粼粼的小溪跳跃，惊奇地睁大了眼睛。森林里充满了神奇的元素:发光和变色的花朵，紫色和银色叶子的树木，以及像萤火虫一样的小浮动灯。这只生物停下来和一群在蘑菇圈周围跳舞的小仙女嬉戏。这只生物敬畏地仰望着一棵巨大的、发光的树，这棵树似乎是森林的中心。**</strong></strong>

**原视频地址：**





#### **<strong><strong>复杂场景**</strong></strong>



Sora is able to generate complex scenes with multiple characters, specific types of motion, and accurate details of the subject and background. The model understands not only what the user has asked for in the prompt, but also how those things exist in the physical world.

Sora能够生成具有多个角色、特定类型动作和精确主题和背景细节的复杂场景。该模型不仅了解用户在提示中所要求的内容，还理解这些东西在物理世界中的存在方式。



##### **<strong><strong>Prompt: The camera follows behind a white vintage SUV with a black roof rack as it speeds up a steep dirt road surrounded by pine trees on a steep mountain slope, dust kicks up from it’s tires, the sunlight shines on the SUV as it speeds along the dirt road, casting a warm glow over the scene. The dirt road curves gently into the distance, with no other cars or vehicles in sight. The trees on either side of the road are redwoods, with patches of greenery scattered throughout. The car is seen from the rear following the curve with ease, making it seem as if it is on a rugged drive through the rugged terrain. The dirt road itself is surrounded by steep hills and mountains, with a clear blue sky above with wispy clouds.镜头跟在一辆车顶有**</strong>**<strong>着**</strong>**<strong>黑色车顶架的白色复古SUV后面，它在陡峭的山坡上沿着松树环绕的陡峭土路加速行驶，灰尘从轮胎上扬起，阳光照在越野车上，在土路上加速行驶，给场景投下了温暖的光芒。这条土路弯弯曲曲地延伸到远处，看不到其他的车辆。道路两旁的树木都是红杉，点缀着一片片绿色植物。。车辆从后方看去，顺利地跟随着弯曲的道路，使它看起来好像是在崎岖不平的地形上行驶。土路本身被陡峭的丘陵和山脉包围，上面是清澈的蓝天和缕缕的云。**</strong></strong>

<img alt="" height="469" src="https://img-blog.csdnimg.cn/direct/96702dd850a540189df2d6f120f4d12c.gif" width="818">

**原视频地址：**



##### **<strong><strong>Prompt: Reflections in the window of a train traveling through the Tokyo suburbs.一列火车在东京郊区行驶时，车窗上的倒影。**</strong></strong>

<img alt="" height="469" src="https://img-blog.csdnimg.cn/direct/20e0e261e20f41e0b00e78067d6e569e.gif" width="818">

**原视频地址：**



##### **<strong><strong>Prompt: A drone camera circles around a beautiful historic church built on a rocky outcropping along the Amalfi Coast, the view showcases historic and magnificent architectural details and tiered pathways and patios, waves are seen crashing against the rocks below as the view overlooks the horizon of the coastal waters and hilly landscapes of the Amalfi Coast Italy, several distant people are seen walking and enjoying vistas on patios of the dramatic ocean views, the warm glow of the afternoon sun creates a magical and romantic feeling to the scene, the view is stunning captured with beautiful photography.一架无人机摄像机环绕着一座美丽的历史悠久的教堂，这座教堂建在阿马尔菲海岸的岩石上，这张照片展示了历史和宏伟的建筑细节，以及分层的通道和露台，海浪撞击着下面的岩石，俯瞰着意大利阿马尔菲海岸的海岸水域和丘陵景观，远处的几个人在露台上散步，欣赏着壮丽的海景。午后阳光的温暖光辉为现场创造了一种神奇而浪漫的感觉，这个景象被美丽的摄影所捕捉。**</strong></strong>

**原视频地址：**





#### **<strong><strong>创建多个镜头**</strong></strong>

该模型对语言有深刻的理解，使其能够准确地解释提示，并生成表达充满活力的情感的引人注目的角色。Sora还可以在单个生成的视频中创建多个镜头，这些镜头准确地延续了角色和视觉风格。

##### **<strong><strong>Prompt: Tour of an art gallery with many beautiful works of art in different styles.参观一个艺术画廊，那里有许多不同风格的美丽艺术品。**</strong></strong>

<img alt="" height="468" src="https://img-blog.csdnimg.cn/direct/1443bd3d676c4c5bb000b6242997401b.gif" width="821">

**原视频地址：**



##### **<strong><strong>Prompt: Beautiful, snowy Tokyo city is bustling. The camera moves through the bustling city street, following several people enjoying the beautiful snowy weather and shopping at nearby stalls. Gorgeous sakura petals are flying through the wind along with snowflakes.美丽、白雪皑皑的东京城市熙熙攘攘。镜头穿过繁华的城市街道，跟随几个人享受美丽的雪天气候，并在附近的摊位上购物。绚丽的樱花花瓣随着雪花在风中飞舞。**</strong></strong>

<img alt="" height="468" src="https://img-blog.csdnimg.cn/direct/6027075cc30848e1838832e5c1f7b3e5.gif" width="821">

**原视频地址：**



##### **<strong><strong>Prompt: A stop motion animation of a flower growing out of the windowsill of a suburban house.一个定格动画，一朵花从郊区房子的窗台上长出来。**</strong></strong>

**原视频地址：**



#### **<strong><strong>存在劣势：复杂物理、因果关系**</strong></strong>

##### **<strong><strong>弱点：Sora有时会创建不符合物理规律的动作**</strong></strong>

###### **Prompt: Step-printing scene of a person running, cinematic film shot in 35mm.一个人跑步的步印场景，35mm胶片拍摄**

Weakness: Sora sometimes creates physically implausible motion.

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/bcfd9f478add4e96872e77dc367fc9f6.gif" width="847">

**原视频地址：**





##### **<strong><strong>弱点：在包含许多实体的场景中，动物或人物可能会突然出现**</strong></strong>

###### **Prompt: Five gray wolf pups frolicking and chasing each other around a remote gravel road, surrounded by grass. The pups run and leap, chasing each other, and nipping at each other, playing.五只小灰狼在一条偏僻的砾石路上嬉戏追逐，周围长满了草。幼崽们又跑又跳，互相追逐，互相咬咬，玩耍。**

Weakness: Animals or people can spontaneously appear, especially in scenes containing many entities.

<img alt="" height="553" src="https://img-blog.csdnimg.cn/direct/8d75301135f047c1b7443ce9143ad17a.gif" width="784">

**原视频地址：**



##### **<strong><strong>弱点：不准确的物理建模和不自然的物体“变形”。**</strong></strong>

###### **Prompt: Basketball through hoop then explodes.篮球穿过篮筐然后爆炸。**

Weakness: An example of inaccurate physical modeling and unnatural object “morphing.”

<img alt="" height="475" src="https://img-blog.csdnimg.cn/direct/c85379654a144373a4db7532a99be154.gif" width="847">

**原视频地址：**



##### **<strong><strong>弱点：在这个例子中，Sora未能将椅子建模为刚体物体，导致**</strong>**<strong>不准确的物理交互**</strong>**<strong>。**</strong></strong>

###### **Prompt: Archeologists discover a generic plastic chair in the desert, excavating and dusting it with great care.考古学家在沙漠中发现了一把普通的塑料椅子，他们小心翼翼地挖掘并掸去了上面的灰尘。**

Weakness: In this example, Sora fails to model the chair as a rigid object, leading to inaccurate physical interactions.

<img alt="" height="466" src="https://img-blog.csdnimg.cn/direct/0257c78a58764ecba4b9325c9767b4d3.gif" width="829">

**原视频地址：**





##### **<strong><strong>弱点：模拟对象和多个角色之间的复杂互动对模型来说通常是具有挑战性的，有时会导致幽默的产生。**</strong></strong>

###### **Prompt: A grandmother with neatly combed grey hair stands behind a colorful birthday cake with numerous candles at a wood dining room table, expression is one of pure joy and happiness, with a happy glow in her eye. She leans forward and blows out the candles with a gentle puff, the cake has pink frosting and sprinkles and the candles cease to flicker, the grandmother wears a light blue blouse adorned with floral patterns, several happy friends and family sitting at the table can be seen celebrating, out of focus. The scene is beautifully captured, cinematic, showing a 3/4 view of the grandmother and the dining room. Warm color tones and soft lighting enhance the mood..木餐桌前，一位头发花白、梳得整整齐齐的老奶奶站在五彩缤纷的生日蛋糕后面，蜡烛点着，脸上流露出喜悦和幸福的神情，眼里闪着幸福的光芒。她身体前倾，轻轻地吹灭了蜡烛，蛋糕上有粉红色的糖霜和糖屑，蜡烛也不再闪烁，祖母穿着一件浅蓝色的衬衫，上面装饰着花卉图案，可以看到几个快乐的朋友和家人坐在桌子旁庆祝，模糊了焦点。这个场景拍得很漂亮，像电影一样，展示了祖母和餐厅的3/4视图。温暖的色调和柔和的灯光增强了情绪。**

Weakness: Simulating complex interactions between objects and multiple characters is often challenging for the model, sometimes resulting in humorous generations.

<img alt="" height="445" src="https://img-blog.csdnimg.cn/direct/d39efd9f7b7e4df395e5e498384f9296.gif" width="796">

**原视频地址：**







### **<strong><strong>Safety安全性**</strong></strong>

在将Sora应用于OpenAI的产品之前，我们将采取一些重要的安全措施。我们正在与红队合作，这些**<strong>红队**</strong>成员是针对误导信息、仇恨内容和偏见等领域的专家，他们将对模型进行对抗性测试。

我们还在构建工具来帮助检测误导性内容，比如检测分类器，它可以判断视频是是否由Sora生成的。如果我们在OpenAI产品中部署该模型，我们计划在将来包含C2PA元数据。

除了开发新技术为部署做准备外，我们还利用了我们为使用DALL·E 3的产品构建的现有安全方法，这些方法也适用于Sora。

例如，一旦投入OpenAI产品中，我们的文本分类器将检查并拒绝违反我们使用政策的文本输入提示，例如那些请求极端暴力、性内容、仇恨图像、名人肖像或他人IP知识产权的提示。我们还开发了强大的图像分类器，用于审查生成的每个视频帧，以确保其符合我们的使用政策，然后再向用户显示。

我们将与全球的政策制定者、教育工作者和艺术家进行交流，了解他们的担忧，并确定这项新技术的积极应用案例。尽管进行了广泛的研究和测试，但我们无法预测人们使用我们技术的所有有益方式，也无法预测人们滥用它的所有方式。这就是为什么我们相信，随着时间的推移，从现实世界的使用中学习是创建和发布越来越安全的人工智能系统的关键组成部分。

##### **<strong><strong>Prompt: The camera directly faces colorful buildings in Burano Italy. An adorable dalmation looks through a window on a building on the ground floor. Many people are walking and cycling along the canal streets in front of the buildings.**</strong></strong>

提示:镜头正对着意大利布拉诺五颜六色的建筑。一只可爱的dalation从一楼的窗户往外看。许多人沿着建筑物前的运河街道散步或骑自行车。

<img alt="" height="469" src="https://img-blog.csdnimg.cn/direct/55b8650057ae4e6087bbe31f920db6be.gif" width="838">

**原视频地址：**





##### **<strong><strong>Prompt: An adorable happy otter confidently stands on a surfboard wearing a yellow lifejacket, riding along turquoise tropical waters near lush tropical islands, 3D digital render art style.**</strong></strong>

提示:一只可爱的快乐水獭自信地站在冲浪板上，穿着黄色救生衣，沿着绿松石般的热带水域骑行，附近是郁郁葱葱的热带岛屿，3D数字渲染艺术风格。

**原视频地址：**



##### **<strong><strong>Prompt: This close-up shot of a chameleon showcases its striking color changing capabilities. The background is blurred, drawing attention to the animal’s striking appearance.**</strong></strong>

提示:这张变色龙的特写照片展示了它惊人的变色能力。背景是模糊的，吸引人们注意到动物引人注目的外表。

**原视频地址：**



### **<strong><strong>Research techniques研究技术**</strong></strong>

#### **<strong><strong>本质：一种扩散模型**</strong></strong>

Sora是一个扩散模型，它从一个看起来像静态噪声的视频开始，然后通过许多步骤去除噪声来逐渐改变它。

Sora能够**<strong>一次生成整个**</strong>视频，或者**<strong>延长生成的视频**</strong>使其更长。通过赋予模型一次许多帧的预见能力，我们解决了一个具有挑战性的问题，即确保一个主题即使暂时消失在视野之外也保持不变。



#### **<strong><strong>基于**</strong>**<strong>transformer **</strong>**<strong>架构**</strong>**<strong>、统一数据表示(基于patch的小数据集合)**</strong></strong>

与GPT模型类似，Sora使用**<strong>transformer **</strong>架构，具有出色的扩展性能。

我们将视频和图像表示为称为patch的较小数据单元的集合，每个patch都类似于GPT中的令牌。通过统一我们表示数据的方式，我们可以在比以前更广泛的视觉数据上训练扩散转换器，跨越不同的持续时间、分辨率和长宽比。



#### **<strong><strong>基于**</strong>**<strong>DALL·E和GPT模型**</strong></strong>

Sora建立在过去对DALL·E和GPT模型的研究基础上。它使用来自DALL·E 3的重捕获技术，该技术涉及为视觉训练数据生成高度描述性的标题。因此，该模型能够更忠实地遵循用户在生成的视频中的文字指令。



#### **<strong><strong>文本指令生成视频、**</strong>**<strong>静止图像中生成视频**</strong>**<strong>、视频延长或填充**</strong></strong>

除了能够仅从文本指令生成视频外，该模型还能够接受现有的静止图像并从中生成视频，并精确地将图像内容动画化，并关注小细节。该模型还可以接受现有的视频并对其进行扩展或填充缺失的帧。在我们的技术报道中了解更多信息。

Sora是能够**<strong>理解和模拟现实世界的模型的基础**</strong>，我们相信这一能力将是**<strong>实现AGI的重要里程碑**</strong>。





## **Sora****的使用方法**

更新中……







## **Sora****的案例应用**

### **<strong><strong>1、文本生成视频**</strong></strong>

更新中……







### **<strong><strong>2、视频拓展**</strong></strong>

更新中……





### **<strong><strong>3、图片动画化**</strong></strong>

更新中……














