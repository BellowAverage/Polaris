
--- 
title:  Unity热更新——AssetBundle（AB包）+管理器 
tags: []
categories: [] 

---
> 
  ❝ 
 <h2>什么是？</h2> 
 游戏或者软件更新时，无需重新下周客户端进行安装，而是在应用程序启动的情况下，在内部进行的资源或者代码更新 
 <h2>1、了解AB包是什么：</h2> 
 特定于平台的资产压缩包，有点类似压缩文件，资产包括：模型、贴图、预设体、音效、材质球等等 ❞ 


## 1、了解AB包是什么：

> 
  ❝ 
 <h2>2、AB包有什么作用：</h2> 
 相对Resources下的资源，AB包更好管理资源，区别是： 
 <table border="1" cellpadding="1" cellspacing="1"><tbody>|AssetBundle|Resources
|可以从网络下载，也可以本地自己打包，资源可以分布在多个包|在打包的时候会压缩一起打包，包括许多无用文件
|存储位置可自定义|Resouces文件夹下
|压缩方式可定义|只能压缩为二进制
|后续可以动态更新|只读（只能通过Resouces.Load加载），无法修改
</tbody></table> 
 **「作用是：」** 
 **「（1）减少包体大小：压缩资源（节约硬盘空间），减少初始包大小」** 
 **「（2）热更新：」** 
 资源热更新：对模型、贴图等进行更新 
 脚本热更新：版本更新添加活动等 
 热更新基本规则： 
 <img alt="" src="https://img-blog.csdnimg.cn/0ac9cf42dc794b70a95c49a5e678582c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAR29fQWNjZXB0ZWQ=,size_20,color_FFFFFF,t_70,g_se,x_16"> ❞ 


> 
  ❝ 
 <h2>3、生成AB包资源文件</h2> 
 <h4>（1）编辑器开发，自定义打包工具</h4> 
 <h4>（2）官方提供好的打包工具：Asset Bundle Browser</h4> 
 路径：Window-&gt;Package Manager-&gt;搜索Asset Bundle Browser，加载成功后在Window窗口会有AssetBundles 
 **「注意：高版本Unity用Addressables（以后会学习）功能封装了AB包功能，在Package Manager中可能搜不到Asset Bundle Browser，如果要使用在github上下载压缩包后解压到Packages文件夹下即可」** 
 注意：中的C#脚本不能被打包为AB包，所以采用Lua热更新（注意：物体的组件本质是根据反射来对数据进行解析，因此真正打包的不是C#代码本身，而是组件关联的数据） 
 在资源的Inspector窗口最下方有一个AssetBundle窗口，第一个窗口是包名，第二个窗口是后缀名（一般不修改），注意是针对预设体而言，如果是Heirachy中的对象在Inpector窗口是不会有此选项的！ 
 在AssetBundles面板中： 
 <table border="1" cellpadding="1" cellspacing="1"><tbody>|Configure<td colspan="3" rowspan="1">会出现关联的AB包</td>
<td colspan="1" rowspan="7">Build</td><td colspan="1" rowspan="7">进行AB包的生成</td><td colspan="2" rowspan="1">**「Build Target：」**构建的平台目标（IOS，Android，windows)</td>
<td colspan="2" rowspan="1">**「Output Path：」**输出路径</td>
<td colspan="2" rowspan="1">**「Clear Floders：」**是否清空文件夹，一般会选择，即在多次打包时，将原文件夹清空（即原来所有的包清空重新构建），但是资源很大时会很耗时</td>
<td colspan="2" rowspan="1">**「Copy to StreamingAssets：」**将打包的AB包从Output Path复制到特数的StreamingAssets文件夹（与备份不同，在某些平台是只读文件夹，在PC是可读可写）</td>
<td colspan="1" rowspan="3">**「Compression：」**压缩方式</td>|**「No Compression：」**不压缩，解压快，但包很大，不推荐使用
|**「LZMA：」**压缩最小，但解压很慢，缺点是如果只需要AB包中的一个资源，会将包中的所有资源解压
|**「LZ4：」**压缩率没有LZMA大，但是可以单独解压一个资源，内存占用低（建议使用）
</tbody></table> 
 打包之后： 
 分两个文件：*，*.manifest 
 （1）关键AB包（和目录名一样的包）：主包，存储着包与包之间的依赖关键关系 
 （2）*（没有后缀名的文件）：资源文件 
 （3）*.manifest：AB包文件信息，对应资源文件相关的关键配置信息。当加载时提供了资源信息，依赖关系，版本信息等关键信息。 
 其他：（了解即可） 
 ETI：在资源包中，不包含资源的类型信息 
 FR：重新打包时需要重新构建包，和ClearFolder类似，不同的是FR不会删除不再存在的包（即在打包的时候删除了某个包，但是原文件夹中的包不会被清除，浪费存储空间） 
 ITC：增量构建检查时，忽略类型数的更改 
 Append Hash：将文件哈希值附加到资源包名上（几乎不用） 
 SM：严格模式，如果打包时报错了，打包直接失败无法成功 
 DRB：运行时构建 
 Inspector界面：主要用于观测包的相关信息（大小，路径等） ❞ 


#### （2）官方提供好的打包工具：Asset Bundle Browser

> 
  ❝ 
 <h2>4、使用AB包资源文件</h2> 
 使用Unity的API进行加载使用:AssetBundle.*** 
 <h4>（1）加载AB包</h4> 
 <pre><code>// 从StreamAssets读取有专门的APIAssetBundle ab = AssetBundle.LoadFromFile(Application.streamingAssetsPath + "/" + 包名（无后缀）);
</code></pre> 
 <h4>（2）加载AB包中的资源</h4> 
 <pre><code>ab.LoadAsset(“Cube")
</code></pre> 
 有三个重载：资源名，Type指定类型，泛型 
 注意：只是用名字加载，会出现同名不同类型资源分不清，因此不建议使用，且：同一个AB包不能够重复加载，否则报错 
 eg： 
 <pre><code>// 同步加载GameObject obj = ab.LoadAsset&lt;GameObject&gt;("Cube");GameObject obj = ab.LoadAsset("Cube", typeof(GameObject)) as GameObject;（通过Lua在C#代码加载对象时只能通过类型，因为Lua不支持泛型）Instantiate(obj)；
</code></pre> 
 <pre><code>//异步加载——&gt;协程public GameObject obj;StartCoroutine(LoadABRes("modle", "Cube"))
</code></pre> 
 <pre><code>IEnumerator LoadABRes(string ABName, string resName) {    // 第一步：加载AB包    AssetBundleCreateRequest abcr = AssetBundle.LoadFromFileAsync(Application.streamingAssetsPath + "/" + ABName）;    yield return abcr;    // 第二步：加载资源    AssetBundleRequest abq = abcr.assetBundle.LoadAssetAsync(resName, typeof(GameObject));    yield return abq;    obj = abq.asset as GameObject;}
</code></pre> 
 <pre><code>// 为了解除所有AB包的绑定，可以使用以下APIAssetBundle.UnloadAllAssetBundles()；
</code></pre> 
 **「如果参数为true，那么解绑定包时会将场景中通过AB包加载的资源一起卸载，false时只对AB包解绑」** 
 <pre><code>// 解绑单个AB包ab.Unload()
</code></pre> 
 参数true/false的意义与UnloadAllAssetBundles()相同 ❞ 


#### （2）加载AB包中的资源

> 
  ❝ 
 <h2>5、AB包的依赖</h2> 
 在包中的一个资源A如果使用了另一个资源B，那么会自动的将B放在同一个包中，但是如果将B的AssetBundle选择另一个包，那么B会打包到另一个包中，此时如果加载包中的A并创建对象，那么A组件中与B相关的内容会丢失，除非此时也将另一个包中的B进行加载，即： 
 **「加载AB包中的资源需要将资源的依赖包一起加载才能正常显示」** 
 步骤： 
 （1）加载AB包1号（假设此包中的资源对2号包中的资源有依赖） 
 （2）加载AB包2号 
 （3）加载1号包中的资源 
 但是实际要完成以上操作，我们需要提前知道哪些包之间存在依赖关系，因此需要利用**「主包获取依赖信息」**。 
 步骤：假设寻找包"model“的依赖包 
 （1）加载主包，假设主包名为Main（打包后主包名和路径名一样） 
 <pre><code>AssetBundle abMain = AssetBundle.LoadFromFIle(Application.streamingAssetsPath + "/" + ”Main"）；
</code></pre> 
 （2）加载主包中的固定文件 
 <pre><code>AssetBundleManifest abManifest = abMain.LoadAsset&lt;AssetBundleManifest&gt;("AssetBundleManifest");
</code></pre> 
 （3）从固定文件中，得到依赖信息，返回的即是依赖包的名字 
 <pre><code>string[] strs = abManifest.GetAllDependecies(”model");
</code></pre> 
 （4）加载相关依赖包 
 <pre><code>List&lt;AssetBundle&gt; dependecies = new LIst&lt;AssetBundle&gt;();for(int = 0; i &lt; strs.Length; ++i) {    dependecies.Add( AssetBundle.LoadFromFIle(Application.streamingAssetsPath + "/" + strs[i]）)；}
</code></pre> 
 注意，只能知道包与包之间的依赖关系，不能具体知道包中的资源的具体依赖关系 ❞ 


> 
  ❝ 
 <h2>**「6、AB包资源加载管理器」**</h2> 
 需要用到：字典、协程、单例模式、AB包相关API，委托（Lambda表达式） 
 <pre><code>// 继承这种自动创建的单例模式基类不需要我们手动去拖动或者API去添加// 使用时直接GetInstance即可public class SingletonAutoMono&lt;T&gt; : MonoBehaviour where T:MonoBehaviour {    private static T instance;     public static T GetInstance(){        if (istance == null) {            GameObject obj = new GameObject();            // 设置对象名字为脚本名            obj.name = typeof(T).ToString();            // 让这个单例模式对象过场景不移除，因为单例模式对象往往是存在于            // 整个程序生命周期的            DontDestroyOnLoad(obj);            instance = obj.AddComponent&lt;T&gt;();          }        return instance;    }}
</code></pre> 
 <pre><code>public class ABMgr : SingletonAutoMono&lt;ABMgr&gt; { // AB包管理器目的是：让外部更方便地进行资源加载 // AB包不能重复加载，重复加载会报错，其中的资源不限制 // 用字典来存储加载过的AB包 private Dictionary&lt;string, AssetBundle&gt; abDic = new Dictionary&lt;string, AssetBundle&gt; ();    // 主包和相关配置文件只需要加载一次即可，因此声明相关变量 // 主包 private AssetBundle mainAB  = null;  // 依赖包获取用的配置文件 private AssetBundleManifest manifest = null;     private ABMgr() { }  // AB包存放路径，方便修改 private string PathUrl {  get { return Application.streamingAssetsPath + "/";  /* 假设是该路径 */ } }  // 主包名，方便修改 private string MainABName {  get {#if UNITY_IOS   return "IOS";#elif UNITY_ANDROID   return "Andriod";#else   return "PC";#endif  } }  // 确保了每个包都只加载了一次 public void LoadAB(string abName) {  // 加载AB主包和其中的关键配置文件  if (mainAB == null) {   mainAB = AssetBundle.LoadFromFile(PahtUrl + MainABName);   manifest = mainAB.LoadAsset&lt;AssetBundleManifest&gt;("AssetBundleManifest");  }   // 获取依赖包的信息  AssetBundle ab = null；  string[] strs = manifest.GetAllDependencies(abName);   for(int i = 0; i &lt; strs.Length; ++i) {   if (!abDic.ContainsKey(strs[i])) {    ab = AssetBundle.LoadFromFile(PathUrl + str[i]);       abDic.Add(strs[i],ab);   }  }   // 加载资源来源包      // 如果没有加载过，再加载  if （!abDic.ContainsKey(abName)) {   ab = AssetBundle.LoadFromFile(PathUrl + abName);   abDic.Add(abName. ab);  } }    // 对同步加载进行重载，因为通过泛型可以避免as转换，并且Lua不支持泛型，    // 因此还需要使用type重载 // 同步加载, 不指定类型    // 加载abName包中的resName资源 public Object LoadRes(string abName, string resName) {  // 加载AB包  LoadAB(abName);  // 加载资源  Object obj = abDic[abName].LoadAsset(resName);  // 为了外面方便，再加载资源时，判断一下资源是不是GameObject  // 如果是，直接实例化，否则返回给外部  if (obj is GameObject)   return Instantiate(obj);  else   return obj; }  // 同步加载，根据type指定类型 public Object LoadRes(string abName, string resName, System.Type type) {  // 加载AB包  LoadAB(abName);  // 加载资源  Object obj = abDic[abName].LoadAsset(resName, type);  // 为了外面方便，再加载资源时，判断一下资源是不是GameObject  // 如果是，直接实例化，否则返回给外部  if (obj is GameObject)   return Instantiate(obj);  else   return obj; }  // 同步加载，根据泛型指定类型 // 必须要加约束，因为LoadAsset&lt;T&gt;方法带有约束 public T LoadRes&lt;T&gt; (string abName, string resName)  where T:Object{  // 加载AB包  LoadAB(abName);  // 加载资源  T obj = abDic[abName].LoadAsset&lt;T&gt;(resName, type);  // 为了外面方便，再加载资源时，判断一下资源是不是GameObject  // 如果是，直接实例化，否则返回给外部  if (obj is GameObject)   return Instantiate(obj);  else   return obj; }  // 异步加载的方法，由于异步加载无法马上使用资源，需要使用委托    // 来知道资源加载完后应该怎样使用资源    // 这里的异步加载，AB包并没有使用异步加载    // 只是从AB包中加载资源时，使用异步    // 和同步一样重载    // 根据名字异步加载资源    public void LoadResAsync(string abName, string resName, UnityAction&lt;Object&gt; callBack) {        StartCoroutine(ReallyLoadResAsync(abName, resName, callBack));    }     private IEnumerator ReallyLoadResAsync(string abName, string resName, UnityAction&lt;Object&gt; callBack) {  LoadAB(abName);  AssetBundlesRequest abr = abDic[abName].LoadAssetAsync(resName);        yield return abr;                // 异步加载结束后，通过委托传递给外部来使用  if (abr.asset is GameObject)   callBack(Instantiate(abr.asset));  else   callBack(abr.asset);    }     // 根据type异步加载资源    public void LoadResAsync(string abName, string resName, System.Type type, UnityAction&lt;Object&gt; callBack) {        StartCoroutine(ReallyLoadResAsync(abName, resName, type, callBack));    }     private IEnumerator ReallyLoadResAsync(string abName, string resName, System.Type type, UnityAction&lt;Object&gt; callBack) {  LoadAB(abName);  AssetBundlesRequest abr = abDic[abName].LoadAssetAsync(resName, type);        yield return abr;                // 异步加载结束后，通过委托传递给外部来使用  if (abr.asset is GameObject)   callBack(Instantiate(abr.asset));  else   callBack(abr.asset);    }     // 根据泛型异步加载资源    public void LoadResAsync&lt;T&gt;(string abName, string resName, UnityAction&lt;T&gt; callBack) where T:Object{        StartCoroutine(ReallyLoadResAsync&lt;T&gt;(abName, resName, callBack));    }     private IEnumerator ReallyLoadResAsync&lt;T&gt;(string abName, string resName, UnityAction&lt;T&gt; callBack) {  LoadAB(abName);  AssetBundlesRequest abr = abDic[abName].LoadAssetAsync&lt;T&gt;(resName);        yield return abr;                // 异步加载结束后，通过委托传递给外部来使用  if (abr.asset is GameObject)   callBack(Instantiate(abr.asset) as T);  else   callBack(abr.asset as T);    }   // 单个包的卸载 public void UnLoad(string abName) {   if (abDic.ContainsKey(abName) {    abDic[abName].Unload(false);    abDic.Remove(abName);   }    }  // 所有包的卸载 public void ClearAB() {  AssetBundle.UnloadAllAssetBundles(false);  abDic.Clear();  mainAB = null;  manifest = null; }}
</code></pre> 
 **「留个坑，上面只实现了资源的异步加载，以后实现AB包的异步加载；」** 
 调用时： 
 同步加载： 
 (1)通过名字： 
 <pre><code>Object obj = ABMgr.GetInstance().LoadRes("model", "Cube");
</code></pre> 
 或者 
 <pre><code>GameObject obj = ABMgr.GetInstance().LoadRes("model", "Cube") as GameObject;
</code></pre> 
 (2)通过类型： 
 <pre><code>GameObject obj = ABMgr.GetInstance().LoadRes("model", "Cube"， typeof(GameObject)) as GameObject;
</code></pre> 
 (3)通过泛型： 
 <pre><code>GameObject obj = ABMgr.GetInstance().LoadRes&lt;GameObject&gt;("model", "Cube");
</code></pre> 
 异步加载： 
 （1）通过名字 
 <pre><code>ABMgr.GetInstance().LoadResAsync("model","Cube", (obj) =&gt; {    (obj as GameObject).transform.position = -Vector3.up;});
</code></pre> 
 （2）通过类型 
 <pre><code>ABMgr.GetInstance().LoadResAsync("model","Cube", typeof(GameObject), (obj) =&gt; {    (obj as GameObject).transform.position = -Vector3.up;});
</code></pre> 
 （3）通过泛型 
 <pre><code>ABMgr.GetInstance().LoadResAsync&lt;GameObject&gt;("model","Cube", (obj) =&gt; {    obj.transform.position = -Vector3.up;});
</code></pre> ❞ 


 参考：
