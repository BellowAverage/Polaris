
--- 
title:  HTTP状态返回代码大全 
tags: []
categories: [] 

---
## HTTP状态返回代码大全

#### 1、HTTP状态返回代码 1xx（临时响应）：

表示临时响应并需要请求者继续执行操作的状态代码。

<th align="left">Code</th><th align="left">代码</th><th align="left">说明</th>
|------
<td align="left">100</td><td align="left">继续</td><td align="left">服务器返回此代码表示已收到请求的第一部分，正在等待其余部分</td>
<td align="left">101</td><td align="left">切换协议</td><td align="left">请求者已要求服务器切换协议，服务器已确认并准备切换</td>

#### 2、HTTP状态返回代码 2xx （成功）：

表示成功处理了请求的状态代码。

<th align="left">Code</th><th align="left">代码</th><th align="left">说明</th>
|------
<td align="left">200</td><td align="left">成功</td><td align="left">服务器已成功处理了请求。 通常，这表示服务器提供了请求的网页</td>
<td align="left">201</td><td align="left">已创建</td><td align="left">请求成功并且服务器创建了新的资源</td>
<td align="left">202</td><td align="left">已接受</td><td align="left">服务器已接受请求，但尚未处理</td>
<td align="left">203</td><td align="left">非授权信息</td><td align="left">服务器已成功处理了请求，但返回的信息可能来自另一来源</td>
<td align="left">204</td><td align="left">无内容</td><td align="left">服务器成功处理了请求，但没有返回任何内容</td>
<td align="left">205</td><td align="left">重置内容</td><td align="left">服务器成功处理了请求，但没有返回任何内容</td>
<td align="left">206</td><td align="left">部分内容</td><td align="left">服务器成功处理了部分GET请求</td>

#### 3、HTTP状态返回代码 3xx （重定向）：

表示要完成请求，需要进一步操作。 通常，这些状态代码用来重定向。

<th align="left">Code</th><th align="left">代码</th><th align="left">说明</th>
|------
<td align="left">300</td><td align="left">多种选择</td><td align="left">针对请求，服务器可执行多种操作。 服务器可根据请求者 (user agent) 选择一项操作，或提供操作列表供请求者选择。</td>
<td align="left">301</td><td align="left">永久移动</td><td align="left">请求的网页已永久移动到新位置。 服务器返回此响应（对 GET 或 HEAD 请求的响应）时，会自动将请求者转到新位置。</td>
<td align="left">302</td><td align="left">临时移动</td><td align="left">服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。</td>
<td align="left">303</td><td align="left">查看其他位置</td><td align="left">请求者应当对不同的位置使用单独的 GET 请求来检索响应时，服务器返回此代码。</td>
<td align="left">304</td><td align="left">未修改</td><td align="left">自从上次请求后，请求的网页未修改过。 服务器返回此响应时，不会返回网页内容。</td>
<td align="left">305</td><td align="left">使用代理</td><td align="left">请求者只能使用代理访问请求的网页。如果服务器返回此响应，还表示请求者应使用代理。</td>
<td align="left">307</td><td align="left">临时重定向</td><td align="left">服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。</td>

#### 4、HTTP状态返回代码 4xx（请求错误）：

这些状态代码表示请求可能出错，妨碍了服务器的处理。

<th align="left">Code</th><th align="left">代码</th><th align="left">说明</th>
|------
<td align="left">400</td><td align="left">错误请求</td><td align="left">服务器不理解请求的语法。</td>
<td align="left">401</td><td align="left">未授权</td><td align="left">请求要求身份验证。对于需要登录的网页，服务器可能返回此响应。</td>
<td align="left">403</td><td align="left">禁止</td><td align="left">服务器拒绝请求。</td>
<td align="left">404</td><td align="left">未找到</td><td align="left">服务器找不到请求的网页。</td>
<td align="left">405</td><td align="left">方法禁用</td><td align="left">禁用请求中指定的方法。</td>
<td align="left">406</td><td align="left">不接受</td><td align="left">无法使用请求的内容特性响应请求的网页。</td>
<td align="left">407</td><td align="left">需要代理授权</td><td align="left">此状态代码与 401（未授权）类似，但指定请求者应当授权使用代理。</td>
<td align="left">408</td><td align="left">请求超时</td><td align="left">服务器等候请求时发生超时。</td>
<td align="left">409</td><td align="left">冲突</td><td align="left">服务器在完成请求时发生冲突。 服务器必须在响应中包含有关冲突的信息。</td>
<td align="left">410</td><td align="left">已删除</td><td align="left">如果请求的资源已永久删除，服务器就会返回此响应。</td>
<td align="left">411</td><td align="left">需要有效长度</td><td align="left">服务器不接受不含有效内容长度标头字段的请求。</td>
<td align="left">412</td><td align="left">未满足前提条件</td><td align="left">服务器未满足请求者在请求中设置的其中一个前提条件。</td>
<td align="left">413</td><td align="left">请求实体过大</td><td align="left">服务器无法处理请求，因为请求实体过大，超出服务器的处理能力。</td>
<td align="left">414</td><td align="left">请求的 URI 过长</td><td align="left">请求的 URI（通常为网址）过长，服务器无法处理。</td>
<td align="left">415</td><td align="left">不支持的媒体类型</td><td align="left">请求的格式不受请求页面的支持。</td>
<td align="left">416</td><td align="left">请求范围不符合要求</td><td align="left">如果页面无法提供请求的范围，则服务器会返回此状态代码。</td>
<td align="left">417</td><td align="left">未满足期望值</td><td align="left">服务器未满足"期望"请求标头字段的要求。</td>

#### 5、HTTP状态返回代码 5xx（服务器错误）：

这些状态代码表示服务器在尝试处理请求时发生内部错误。 这些错误可能是服务器本身的错误，而不是请求出错。

<th align="left">Code</th><th align="left">代码</th><th align="left">说明</th>
|------
<td align="left">500</td><td align="left">服务器内部错误</td><td align="left">服务器遇到错误，无法完成请求。</td>
<td align="left">501</td><td align="left">尚未实施</td><td align="left">服务器不具备完成请求的功能。例如，服务器无法识别请求方法时可能会返回此代码。</td>
<td align="left">502</td><td align="left">错误网关</td><td align="left">服务器作为网关或代理，从上游服务器收到无效响应。</td>
<td align="left">503</td><td align="left">服务不可用</td><td align="left">服务器目前无法使用（由于超载或停机维护）。 通常，这只是暂时状态。</td>
<td align="left">504</td><td align="left">网关超时</td><td align="left">服务器作为网关或代理，但是没有及时从上游服务器收到请求。</td>
<td align="left">505</td><td align="left">HTTP 版本不受支持</td><td align="left">服务器不支持请求中所用的 HTTP 协议版本。</td>
