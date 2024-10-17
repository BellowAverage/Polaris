
--- 
title:  Web 开发未来会完全替代客户端开发吗？ 
tags: []
categories: [] 

---
大家好，我是恶霸

首先问大家一个问题，现在有一项业务需求，这个需求使用客户端应用实现还是网页来实现你会考虑哪些因素呢？可以在评论区告诉我。

曾几何时，想到网页可能我们第一时间想到的就是一些静态页面，但是经过数十年的蓬勃发展，网页开始承接越来越复杂的需求，包括复杂的管理系统、网络直播、云游戏等能力。

但或许你仍然会认为相比可以和系统底层直接交互的原生客户端应用还是太弱了，我们可能会因为浏览器“缺失” 了某一项能力而被迫选择开发一个客户端应用。

为此 `Google` 启动了一个名为 `Fugu` 的项目，它的目标就是让开发者能够在 `Web` 生态中做任何事情，包括以前只有客户端应用才能做的事情。

在 `Fugu` 项目中， `Google` 为 `Chrome` 规划了数百项能力，如今进展已经过半，我们一起来看看浏览器现在拥有了哪些或许你还不知道的能力吧 ...

### 和蓝牙设备交互 【Chrome 56】

`Web Bluetooth API` 为浏览器提供了连接蓝牙设备并与之交互的能力。

这意味着：你的网站可以直接连接你的运动手表，查看步数、心率等数据，可以直接控制你的蓝牙音响等等。而这些能力，之前你必须要下载一个 `App` 才能实现了 ...

获取是否支持蓝牙连接：

```
navigator.bluetooth.getAvailability().then((available) =&gt; {
  if (available) {
    console.log("设备支持蓝牙连接!");
  } else {
    console.log("设备不支持蓝牙");
  }
});
复制代码
```

连接到蓝牙设备：

```
navigator.bluetooth.requestDevice({ filters: [{ services: ['battery_service'] }] })
.then(device =&gt; {
  // 获取设备名称 [ConardLi]
  console.log(device.name);

  // 连接远程 GATT Server.
  return device.gatt.connect();
})
.then(server =&gt; { /* … */ })
.catch(error =&gt; { console.error(error); });
复制代码
```

了解更多：https://developer.chrome.com/articles/bluetooth/

### 和 USB 设备交互【Chrome 61】

`Web USB API` 为浏览器提供了和 `USB` 设备进行交互的能力。

说到 `USB` ，你很有可能会立即想到键盘、鼠标、音频、视频和一些存储设备。

这些非标准化的 `USB` 设备通常需要硬件供应商编写特定于平台的驱动程序和 `SDK`，开发非常繁琐。

如果可以在 `Web` 上和 `USB` 进行交互，这意味着硬件制造商将能够为其设备构建跨平台的 `JavaScript SDK`，这将极大简化一个 `SDK` 的开发成本！另外，通过将 `USB` 引入 `Web`，也可以使得 `USB` 更安全、更易于使用。

下面是一段简单的获取 `USB` 设备的代码：

```
navigator.usb.getDevices().then(devices =&gt; {
  devices.forEach(device =&gt; {
    console.log(device.productName);      // "[ConardLi] Arduino Micro "
    console.log(device.manufacturerName); // "[ConardLi] Arduino LLC"
  });
})
复制代码
```

你还可以在 `Chrome` 的内部页面 `about://device-log` 方便的调试 `USB` 设备：

了解更多：https://wicg.github.io/webusb/

### 异步剪贴板【Chrome 76】

在以前，我们一般使用 `document.execCommand()` 进行剪贴板交互。虽然浏览器兼容性还不错，但这种剪切和粘贴的方法有明显的缺点：剪贴板访问是同步的，只能读写 `DOM`。

对于少量文本的剪贴还好，但如果剪贴内容较大，在安全粘贴内容之前，可能还需要进行耗时的清理或图像解码，浏览器可能还需要从粘贴的文档加载或内联链接资源，这种情况下用户体验就比较糟糕了。

`Asynchronous Clipboard API` 的出现解决了这些问题，比如我们要将一段文本复制到剪贴板，可以调用一个异步的 `writeText` 函数：

```
async function copyPageUrl() {
  try {
    await navigator.clipboard.writeText(location.href);
    console.log('Page URL 已赋值到剪贴板');
  } catch (err) {
    console.error('失败了～);
  }
}
复制代码
```

从剪贴板读取数据一样也可以是异步的：

```
async function getClipboardContents() {
  try {
    const text = await navigator.clipboard.readText();
    console.log('粘贴文本: ', text);
  } catch (err) {
    console.error('读取剪贴板文本失败: ', err);
  }
}
复制代码
```

另外，`document.execCommand()` 还有一个非常明显的问题就是权限控制过于宽松了，在很多情况下我们可能会担心网站是否会私自读取我们剪贴板的信息，`Asynchronous Clipboard API` 仅支持 `HTTPS` 页面，另外在读取剪贴板是会向用户发送许可，这保证了网页必须在用户同意的情况下才能读取剪贴板：





了解更多：https://developer.mozilla.org/docs/Web/API/Clipboard_API

### 应用安装【Chrome 80】

`getInstalledRelatedApps` 方法可以让浏览器知道某些应用程序是否已在电脑上安装了，当然目前仅限于 `Android、Windows` 或 `PWA` 应用。

```
const relatedApps = await navigator.getInstalledRelatedApps();
relatedApps.forEach((app) =&gt; {
  // 注意只能获取到已经授权的应用，并不是所有应用
  console.log(app.id, app.platform, app.url);
});
复制代码
```

想象一下你开发了一个产品的官网，在用户下载页面你可以根据应用的安装状态提示用户是下载还是更新，甚至可以直接打开应用...

了解更多：https://github.com/WICG/get-installed-related-apps

### 获取联系人【Chrome 80】

在以前，能够在移动设备上访问用户的联系人一直是移动 `Web` 应用开发者最想要的功能之一，这也是促使他们必须选择开发一个 `App` 的重要原因...

`Contact Picker API`  为浏览器提供了获取手机联系人的能力。

假如我们有一个基于 `Web` 的电子邮件客户端，可以直接使用 `Contact Picker API` 来选择电子邮件的收件人。一个基于 `Web` 的 `IP` 语音应用程序可以直接查找要拨打的电话号码。或者一些 Web 社交应用可以帮助用户发现哪些朋友已经加入了。

比如，你打开一个网页游戏，他可以直接告诉你，你的好兄弟 `ConardLi` 也在玩哟，快和他一起组队来砍我吧...

下面是一个简单的使用示例：

```
const props = ['name', 'email', 'tel', 'address', 'icon'];
const opts = {multiple: true};

try {
  const contacts = await navigator.contacts.select(props, opts);
  handleResults(contacts);
} catch (ex) {
  // 一些错误...
}
复制代码
```

了解更多：https://wicg.github.io/contact-api/spec/

### 编解码能力【Chrome 80】

在以前，浏览器提供了诸如 `HTMLMediaElement、WebAudio、WebRTC` 等实现媒体编解码器能力的 `API`，但是没有通用的方法来灵活配置和使用这些媒体编解码器。因此，在有性能差、耗电快等问题的情况下，许多 `Web` 应用还是会求助于在 `JavaScript` 或 `WebAssembly` 中实现媒体编解码器。

`WebCodecs` 为网页提供了对内置（软件和硬件）媒体编码器和解码器的高效访问能力。

这项能力为网页直播、云游戏等对流媒体处理性能要求较高的场景下大地来了很大便利。

下面是一个从视频渲染到 `Canvas` 来实现极低延迟流的示例：

```
function onDecoderError(error) { ... }

function streamEncodedChunks(decodeCallback) { ... }

const canvasElement = document.getElementById("canvas");
const canvasContext = canvas.getContext('2d', canvasOptions)

function paintFrameToCanvas(videoFrame) {
  canvasContext.drawImage(frame, 0, 0);

  frame.close();
}

const videoDecoder = new VideoDecoder({
  output: paintFrameToCanvas,
  error: onDecoderError
});

videoDecoder.configure({codec: 'vp8'}).then(() =&gt; {
  streamEncodedChunks(videoDecoder.decode.bind(videoDecoder));
}).catch(() =&gt; {});
复制代码
```

了解更多：https://github.com/w3c/webcodecs/blob/main/explainer.md

### 为图标添加徽章【Chrome 81】

`App Badging API` 可以让 Web 应用为图标添加一些徽章。

比如一个 Web 聊天室可以在徽章上显示未读的消息数；一个 `Web` 象棋游戏可以通过标记提醒轮到你下棋了；一些长耗时的后台任务可以通过标记告诉你任务已经成功 ...

下面是一个简单的代码示例：

```
// 设置徽章
const unreadCount = 17;
navigator.setAppBadge(unreadCount).catch((error) =&gt; {
  // 异常捕获...
});

// 清除徽章
navigator.clearAppBadge().catch((error) =&gt; {
  // 异常捕获...
});
复制代码
```

了解更多：https://w3c.github.io/badging/

### 形状检测【Chrome 83】

在以前，我们想在 `Web` 上读取一些图片上的数据是相当困难的，比如开发者想在客户端提取一些些特征来构建一个二维码阅读器，必须要依赖一个庞大的外部 `JavaScript` 库，而且性能可能很差。

但是，包括 `Android、iOS` 和 `macOS` 在内的操作系统，以及相机模块中的硬件芯片，通常已经具有高性能和高度优化的特征检测器，例如 `Android` 的 `FaceDetector` 或 `iOS` 的 `CIDetector` 通用特征检测器。

`Shape Detection API` 通过一组 `JavaScript` 接口公开了这些实现。目前支持的功能有人脸检测、条码检测以及文字检测，这意味着我们可以在 Web 上实现下面的功能：
- 购物网站可以让用户直接扫描商品条码查询商品信息；- 社交网站可以检测人脸面部特征，自动添加墨镜、胡子等道具；- 内容网站可以自动识别图片上的文本，例如餐厅菜单。
下面是一段简单的人脸识别代码：

```
// [ConardLi]
const faceDetector = new FaceDetector({
  // 限制识别人脸的数量
  maxDetectedFaces: 5,
  // 降低精度提升速度
  fastMode: false
});
try {
  const faces = await faceDetector.detect(image);
  faces.forEach(face =&gt; drawMustache(face));
} catch (e) {
  console.error('Face detection failed:', e);
}
复制代码
```

了解更多：https://wicg.github.io/shape-detection-api/

### 获取验证码【Chrome 84】

当我们在一些网站上进行注册或登录时，可能需要验证手机号。网页一般会发送一个验证码，我们需要将验证码提交到网页上来完成验证。但是切到短信后复制验证码，再回来提交整个过程是比较繁琐的。

`WebOTP API` 为浏览器提供了快捷读取短信验证码的能力。

用法也非常简单，首先我们可以为 `input` 添加一个 `autocomplete` 属性：

```
&lt;form&gt;
  &lt;input autocomplete="one-time-code" required/&gt;
  &lt;input type="submit"&gt;
&lt;/form&gt;
复制代码
```

然后调用 `navigator.credentials` 获取验证码信息：

```
if ('OTPCredential' in window) {
  window.addEventListener('DOMContentLoaded', e =&gt; {
    const input = document.querySelector('input[autocomplete="one-time-code"]');
    if (!input) return;
    const ac = new AbortController();
    const form = input.closest('form');
    if (form) {
      form.addEventListener('submit', e =&gt; {
        ac.abort();
      });
    }
    navigator.credentials.get({
      otp: { transport:['sms'] },
      signal: ac.signal
    }).then(otp =&gt; {
      input.value = otp.code;
      if (form) form.submit();
    }).catch(err =&gt; {
      console.log(err);
    });
  });
}
复制代码
```

了解更多：https://wicg.github.io/WebOTP/

### 唤醒屏幕【Chrome 84】

试想一下，当你在某个网站上看着菜谱做饭，由于长时间未操作手机自动锁屏了，你还需要去定期触碰一下手机，是不是有点头大。

`Screen Wake Lock API` 可体让浏览器在网页需要继续运行时防止调暗或锁定屏幕。

使用方式也很简单，可以直接调用 `navigator.wakeLock.request()` 方法，返回一个 `WakeLockSentinel` 对象。

>  
 据说在实施了 `Screen Wake Lock API` 后，美国主要烹饪网站 `Betty Crocker` 的用户购买意向指标增加了 300% ... 


了解更多：https://w3c.github.io/screen-wake-lock

### 文件访问【Chrome 86】

在以前，我们只能通过 `&lt;input type="file"&gt;` 在浏览器上访问文件，需要写出类似下面的代码：

```
const openFile = async () =&gt; {
  return new Promise((resolve) =&gt; {
    const input = document.createElement('input');
    input.type = 'file';
    input.addEventListener('change', () =&gt; {
      resolve(input.files[0]);
    });
    input.click();
  });
};
复制代码
```

`File System Access API` 为浏览器提供了更好的和文件系统交互的能力：

```
const openFile = async () =&gt; {
  try {
    // Always returns an array.
    const [handle] = await window.showOpenFilePicker();
    return handle.getFile();
  } catch (err) {
    console.error(err.name, err.message);
  }
};
复制代码
```

了解更多：https://wicg.github.io/file-system-access/

### Web NFC【Chrome 89】

`NFC` 代表 `Near Field Communications`，这是一种以 `13.56 MHz` 频率运行的短距离无线技术，能够在小于 `10` 厘米的距离内实现设备之间的通信，传输速率高达 `424 kbit/s`。

`Web NFC` 为网站提供了在靠近用户设备时读取和写入 `NFC` 标签的能力，这意味着你只需要打开一个网站就可以刷地铁进站了...

要扫描 `NFC` 标签，首先需要实例化一个 `NDEFReader` 对象，并调用 `scan` 方法，下面是一个简单的代码示例：

```
const ndef = new NDEFReader();
ndef.scan().then(() =&gt; {
  console.log("扫描开始");
  ndef.onreadingerror = () =&gt; {
    console.log("无法读取NFC数据！");
  };
  ndef.onreading = event =&gt; {
    console.log("NFC数据读取成功...");
  };
}).catch(error =&gt; {
  console.log(`Error! Scan failed to start: ${error}.`);
});
复制代码
```

了解更多：https://wicg.github.io/file-system-access/

### 人机接口设备【Chrome 89】

`WebHID API` 为浏览器提供了和人机接口设备（简称 HID）交互的能力。

比如键盘、鼠标、触摸板、游戏手柄等都属于 HID 设备，`WebHID API` 提供了一系列 `JavaScript API` 来和这些设备进行交互。而在以前，你必须要有一个特定的游戏主机才可以...

想象一下，以后再也不用纠结于国行外行了，因为你直接可以在网页里打开 `Switch` 游戏了...

下面是一个简单的代码示例：

```
// 在具有 Switch Joy-Con USB 供应商/产品id的设备上进行筛选。
const filters = [
  {
    vendorId: 0x057e, // Nintendo Co., Ltd
    productId: 0x2006 // Joy-Con Left
  },
  {
    vendorId: 0x057e, // Nintendo Co., Ltd
    productId: 0x2007 // Joy-Con Right
  }
];

// 提示用户选择 Joy-Con 设备。
const [device] = await navigator.hid.requestDevice({ filters });
复制代码
```

了解更多：https://wicg.github.io/webhid/index.html

### 和串口设备交互【Chrome 89】

串行接口（`Serial port`），也称串行接口或串行端口，串行通信接口，COM接口，简称串口。主要用于串行式逐位数据传输。

`Web Serial API` 为网站提供了一种使用 `JavaScript` 读取和写入串行设备的方法。

这样，我们的网站又能控制更多设备了，比如打印机、路由器、交换机等等。

下面是一个简单的代码示例：

```
document.querySelector('button').addEventListener('click', async () =&gt; {
  // 提示用户选择串口
  const port = await navigator.serial.requestPort();
});
复制代码
```

从串口读取数据：

```
const reader = port.readable.getReader();

// 监听来自串行设备的数据
while (true) {
  const { value, done } = await reader.read();
  if (done) {
    reader.releaseLock();
    break;
  }
  console.log(value);
}
复制代码
```

同样的，你也可以在 `Chrome` 的 `about://device-log` 对串口设备进行调试。

### 空闲检测【Chrome 94】

`Idle Detection API` 为网站提供了检测用户当前是否空闲（例如在一段时间内没有与键盘、鼠标、屏幕的交互）的能力。

例如，一个 `Web` 聊天室应用可以让你知道你的好友当前是否在线，下面是一个空闲检测的简单示例：

```
// [ConardLi] 创建空闲探测器
const idleDetector = new IdleDetector();

// 设置一个在用户空闲时触发的监听器
idleDetector.addEventListener('change', () =&gt; {
  const uState = idleDetector.userState;
  const sState = idleDetector.screenState;
  console.log(`Idle change: ${uState}, ${sState}.`);
});

// 开始监听
await idleDetector.start({
  threshold: 60000,
  signal,
});
复制代码
```

了解更多：https://wicg.github.io/idle-detection

### WebTransport【Chrome 97】

`WebTransport` 是一种新的 `API`，使用 `HTTP/3` 协议作为双向传输，为网站提供低延迟、双向、客户端-服务器消息传递能力。

你可能会问和 `WebSockets` 的区别是啥？

`WebSockets` 的消息流特点是单一、可靠、有序，这对于某些场景的通信需求来说是很好的；但是 `WebTransport` 的数据的特点是低延迟，但不保证可靠性或排序，因为它底层使用的 `QUIC` 握手比通过 `TLS` 启动 `TCP` 更快。

如果你的数据通信需要非常好的性能，但是对偶尔的丢包和排序可以容忍，比如一些网页游戏的场景，`WebTransport` 是一个更好的选择。

下面是一个简单的使用示例：

```
// 向服务器发送数据
const writer = transport.datagrams.writable.getWriter();
const data1 = new Uint8Array([65, 66, 67]);
const data2 = new Uint8Array([68, 69, 70]);
writer.write(data1);
writer.write(data2);

// 从服务器读取数据
const reader = transport.datagrams.readable.getReader();
while (true) {
  const {value, done} = await reader.read();
  if (done) {
    break;
  }
  // 值为 Uint8Array。
  console.log(value);
}
复制代码
```

了解更多：https://wicg.github.io/web-transport/#web-transport

### 多屏窗口放置【Chrome 100】

`Multi-Screen Window Placement API` 为网页了提供了枚举显示器并将窗口放置在特定屏幕上的能力。

下面是一个简单的监听屏幕数量变化的示例：

```
// 获取所有屏幕
const screenDetails = await window.getScreenDetails();
let cachedScreensLength = screenDetails.screens.length;
// 监听屏幕变化
screenDetails.addEventListener('screenschange', (event) =&gt; {
  if (screenDetails.screens.length !== cachedScreensLength) {
    console.log(
      `屏幕数量从 ${cachedScreensLength} 变化到 ${screenDetails.screens.length}`,
    );
    cachedScreensLength = screenDetails.screens.length;
  }
});
复制代码
```

了解更多：https://w3c.github.io/window-placement

### 最后

当然，以上我提到的只是 `Fugu` 项目的很小一部分，大家感兴趣可以去 `Fugu` 官网查看更多信息：**「Fugu API Tracker」**（https://fugu-tracker.web.app/#）

你觉得上面哪些能力对你最有用呢？

你觉得未来网页可以完全替代客户端么？

欢迎在评论区和我留言。
