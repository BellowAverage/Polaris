
--- 
title:  django测试——关于登录态 
tags: []
categories: [] 

---
在进行 django 的测试过程中，经常会遇到需要登录的情况。并且，登录还分普通的账号密码登录和oauth的方式进行登录。虽然登录是一件比较麻烦的事情，但是大多数时候我们都可以采用一定的方式将这个环节绕过去。在进行这一步骤之前，我们先简单说下django对需要发请求的单元测试方案。

### 测试请求

在 django 中进行 request 的发送有几种方式，这里简单列一下：
- 使用 TestCase 下的 Client 进行请求- 使用 RequestFactory 构建 request 进行测试- 使用最简单的 requests 库进行单元测试（比较少用）- 在引入 django-rest-framework 的情况下，还可以使用 ApiTestCase 进行单元测试，里面对 Client 又做了一层封装- 除此之外，还有其他一些测试方式，就不再赘述
### 解决登录

#### 屏蔽中间件

有一种比较暴力的方式，就是把django工程中有关于登录的中间件全部屏蔽。虽然这不是一种好的方案，但是可以短暂解决一些不需要获取登录态的视图函数的测试。 在django中有个默认的用户认证中间件。`django.contrib.auth.middleware.AuthenticationMiddleware` 可以在settings.py的中间件配置中注释掉。如果有其他登录相关的中间件，也需要注释掉。虽然这样可以解决简单登录的问题，但是并不是一种友好的测试方式。修改了原先的工程代码。

### 使用mock和patch

python 有个非常好用的测试框架mock，可以提供非常多的测试方案。比方说刚才的操作，我们可以在单元测试的函数上加上`@patch('django.contrib.auth.middleware.AuthenticationMiddleware', return_value=None)`的装饰器，这样就可以不用修改settings.py的代码，还可以绕过登录中间件。但是这样依旧不能解决视图函数中需要获取用户登录后的信息的问题。

### 主动登录

django的client提供了登录函数 login(username, password)，在简单情况下，可以使用这个login函数登录，然后就可以正常执行所有中间件和视图函数。但是这个函数有点问题，就是有些用户是不会有密码的，而是利用token之类的方式进行登录，如oauth2之类的方式。

### force_login和force_authenticate

在django中有这样的一个函数`force_login(user, backend=None)`，如果使用django-rest-framework的话，也会有`force_authenticate(user=None, token=None)` 的函数。在使用client登录后，可以在view函数中获取用户的登录信息。不过这就有个问题，在中间件中是没有办法获取到登录态的。而且force_login函数在django1.9之前是没有的。

### get_user

最终极的解决方案，其实我们可以看一下django的`django.contrib.auth.middleware.AuthenticationMiddleware`里面的逻辑。从中发现一些猫腻。

```
class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: get_user(request))

```

我们可以发现，有个函数`get_user`，源代码如下：

```
def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user

```

从上我们可以看出，`get_user`函数其实就是中间件获取用户的逻辑，我们只要mock掉这个函数就可以了。`@patch('django.contrib.auth.middleware.get_user', return_value=User.objects.first())` 只要把用户model注入到 patch的return_value中去就可以了。解决了中间件和view函数登录态的问题。
