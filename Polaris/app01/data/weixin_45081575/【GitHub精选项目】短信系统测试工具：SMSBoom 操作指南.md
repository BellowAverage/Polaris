
--- 
title:  【GitHub精选项目】短信系统测试工具：SMSBoom 操作指南 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/394b1563b5c044fabfe9171d763f5ab2.png" alt="在这里插入图片描述">

## 前言

>  
 本文为大家带来的是 `OpenEthan` 开发的 `SMSBoom` 项目 —— 一种用于短信服务测试的工具。这个工具能够发送大量短信，通常用于测试短信服务的稳定性和处理能力。在合法和道德的范畴内，`SMSBoom` 可以作为一种有效的测试工具，帮助开发者和系统管理员评估短信服务的性能。 


然而，值得注意的是调 `SMSBoom` 的使用必须严格遵守法律法规和道德标准。错误使用此类工具不仅违反法律，而且可能导致严重的骚扰行为。因此，本文将仅聚焦于其在合法和道德框架下的使用，如压力测试和系统稳定性评估。

在这篇文章中，我们将探讨 `SMSBoom` 的安装、配置和合法使用方法，旨在为需要进行合法短信服务测试的专业人士提供指导。

项目地址：

## 项目概览

`SMSBoom` 是一款专门设计用于发送大量短信的工具。其主要用途是为系统管理员和开发者提供一种手段来测试短信服务的负载能力和稳定性。通过模拟高流量短信发送，`SMSBoom` 能够帮助识别和解决短信服务平台在极端情况下可能遇到的问题。

该工具的核心特点包括其能够快速生成和发送大量短信，从而使用户能够评估短信服务的响应速度和处理能力。这在测试短信服务的稳定性、扩展性和可靠性时尤为重要。

具体的功能可以看项目所展示的 `README` 文档。

<img src="https://img-blog.csdnimg.cn/direct/bd5ad5806651434ba5b0872b138e60f1.png" alt="在这里插入图片描述">

### 克隆项目

**git clone**

最简单的，在命令行工具数据以下命令即可，如下图所示：

```
git clone https://github.com/OpenEthan/SMSBoom

```

<img src="https://img-blog.csdnimg.cn/direct/a945139819dd4ea99b8886d9b81fe38f.png" alt="在这里插入图片描述">

**Download ZIP**

当然，使用 `Download ZIP` 也是个不错的下载方式。

<img src="https://img-blog.csdnimg.cn/direct/1839293158c94cc098e90bbcb961073a.png" alt="在这里插入图片描述">

可以看到，这个效果是非常不错的！

<img src="https://img-blog.csdnimg.cn/img_convert/4595fb86c3ada96011e0d8d3a738ab0d.gif#pic_center" alt="在这里插入图片描述">

## 使用指南

本项目由 Python 所编写，所以特别容易理解上手。 在前面将项目拷贝下来后，去到项目目录下，需要安装所需要的库。在命令行执行以下命令即可。

```
pip install -r requirement.txt

```

### 命令行版

接下来，我们去在命令行执行 `python mssboom.py`，可以看到以下画面。

<img src="https://img-blog.csdnimg.cn/direct/57a84eb612af4ffabde7c9b6028a2f1b.png" alt="在这里插入图片描述">
<li>提示有4个可接收的命令，分别是 
  - `asyncrun`：以最快的方式请求接口，使用真正的异步处理方式，支持高并发。- `onerun`：单线程模式，通常用于测试和调试。- `run`：传入线程数和手机号，启动，支持同时测试多个手机号。- `update`：从 GitHub 获取最新的接口和代码更新。 </li>
我们可以在命令行中输入 `smsboom.py` 后跟随一个命令和相应的选项和参数来执行不同的操作。例如，如果要使用 `asyncrun` 命令，可以执行类似以下的命令：

```
python smsboom.py asyncrun [OPTIONS] [ARGS]

```

另外还可以使用 `--help` 选项来获取有关每个命令的详细帮助信息，例如我们需要查看单线程模式，

```
python smsboom.py onerun --help

```

可以看到以下画面， <img src="https://img-blog.csdnimg.cn/direct/ad12aba9d40240009b2b169fa76bbe5a.png" alt="在这里插入图片描述">

在真正要测试的时候，就可以使用来进行使用了。

```
python smsboom.py onerun --phone 13xxxxxxxxx

```

### GUI版

在命令行中输入，

```
python smsboom_GUI.py 

```

就可以看到以下画面了，真正的简洁明了！

<img src="https://img-blog.csdnimg.cn/direct/76aa41fb614d4ff98cbd1018bc103a7b.png" alt="在这里插入图片描述">

### 代码摘选

#### run 模式

`run` 模式默认是64线程，速度非常快！

```
@click.command()
@click.option("--thread", "-t", help="线程数(默认64)", default=64)
@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", multiple=True, type=str)
@click.option('--frequency', "-f", default=1, help="执行次数(默认1次)", type=int)
@click.option('--interval', "-i", default=60, help="间隔时间(默认60s)", type=int)
@click.option('--enable_proxy', "-e", is_flag=True, help="开启代理(默认关闭)", type=bool)
def run(thread: int, phone: Union[str, tuple], frequency: int, interval: int, enable_proxy: bool = False):
    """传入线程数和手机号启动测试,支持多手机号"""
    with ThreadPoolExecutor(max_workers=thread) as pool:
    	...
    	

```

#### asyncRun 模式

`asyncRun` 使用 `asyncio` 构建了异步任务，速度是嘎嘎快的！

```
@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.command()
def asyncRun(phone):
    """以最快的方式请求接口(真异步百万并发)"""
    _api = load_json()
    _api_get = load_getapi()

    apis = _api + _api_get

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runAsync(apis, phone))
    

```

#### onerun 模式

`onerun` 模式是简根据传入的手机号码作为测试，单线程。

```
@click.option("--phone", "-p", help="手机号,可传入多个再使用-p传递", prompt=True, required=True, multiple=True)
@click.command()
def oneRun(phone):
    """单线程(测试使用)"""
    _api = load_json()
    _api_get = load_getapi()

    apis = _api + _api_get

    for api in apis:
        try:
            reqFunc(api, phone)
        except:
            pass


```

## 总结

`SMSBoom` 是一个功能强大的工具，专为短信服务的压力测试和性能评估而设计。通过模拟高流量短信发送，它帮助用户在实际环境中测试和评估短信服务平台的稳定性和扩展性。该工具提供了多种运行模式，包括异步处理和单线程模式，以适应不同的测试需求。

在使用 `SMSBoom` 时，需要强调的是，这个工具应仅用于合法的测试和评估目的，如系统性能测试、软件开发中的压力测试等。非法或不道德的使用，例如发送垃圾短信或进行骚扰，是严格禁止的，并可能导致法律后果。

`SMSBoom` 项目的便捷性和高效性使它成一个有用工具，但它也是一把双刃剑。因此，鼓励所有用户在使用时遵循道德规范和法律要求，确保其应用仅限于正当和合法的场景。

## 后话

本次分享到此结束， see you~~🎈🎈
