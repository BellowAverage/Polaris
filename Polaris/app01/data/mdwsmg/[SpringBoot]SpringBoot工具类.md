
--- 
title:  [SpringBoot]SpringBoot工具类 
tags: []
categories: [] 

---
SpringBoot框架自带有一些工具类，不让加开源工具包的时候能用。 本文为转载，侵权联系删除。 作者：CadeCode 链接：https://juejin.cn/post/7043403364020781064

>  
 <s>虽是转载，但是也是费功夫调整为MD格式了的</s> 




#### SpringBoot工具类
- - - <ul><li>- - - - - - - - - - - - - - - 


## 1、断言Assert

断言是一个逻辑判断，用于检查不应该发生的情况 Assert 关键字在 JDK1.4 中引入，可通过 JVM 参数-enableassertions开启 SpringBoot 中提供了 Assert 断言工具类，通常用于数据合法性检查

```
// 要求参数 object 必须为非空（Not Null），否则抛出异常，不予放行
// 参数 message 参数用于定制异常信息。
void notNull(Object object, String message)
// 要求参数必须空（Null），否则抛出异常，不予『放行』。
// 和 notNull() 方法断言规则相反
void isNull(Object object, String message)
// 要求参数必须为真（True），否则抛出异常，不予『放行』。
void isTrue(boolean expression, String message)
// 要求参数（List/Set）必须非空（Not Empty），否则抛出异常，不予放行
void notEmpty(Collection collection, String message)
// 要求参数（String）必须有长度（即，Not Empty），否则抛出异常，不予放行
void hasLength(String text, String message)
// 要求参数（String）必须有内容（即，Not Blank），否则抛出异常，不予放行
void hasText(String text, String message)
// 要求参数是指定类型的实例，否则抛出异常，不予放行
void isInstanceOf(Class type, Object obj, String message)
// 要求参数 `subType` 必须是参数 superType 的子类或实现类，否则抛出异常，不予放行
void isAssignable(Class superType, Class subType, String message)


```

## 2、对象、数组、集合ObjectUtils

### 2.1、ObjectUtils获取对象的基本信息

```
// 获取对象的类名。参数为 null 时，返回字符串："null" 
String nullSafeClassName(Object obj)
// 参数为 null 时，返回 0
int nullSafeHashCode(Object object)
// 参数为 null 时，返回字符串："null"
String nullSafeToString(boolean[] array)
// 获取对象 HashCode（十六进制形式字符串）。参数为 null 时，返回 0 
String getIdentityHexString(Object obj)
// 获取对象的类名和 HashCode。 参数为 null 时，返回字符串："" 
String identityToString(Object obj)
// 相当于 toString()方法，但参数为 null 时，返回字符串：""
String getDisplayString(Object obj)

```

### 2.2、ObjectUtils判断方法

```
// 判断数组是否为空
boolean isEmpty(Object[] array)
// 判断参数对象是否是数组
boolean isArray(Object obj)
// 判断数组中是否包含指定元素
boolean containsElement(Object[] array, Object element)
// 相等，或同为 null时，返回 true
boolean nullSafeEquals(Object o1, Object o2)
/*
判断参数对象是否为空，判断标准为：
    Optional: Optional.empty()
       Array: length == 0
CharSequence: length == 0
  Collection: Collection.isEmpty()
         Map: Map.isEmpty()
 */
boolean isEmpty(Object obj)

```

### 2.3、ObjectUtils其他方法

```
// 向参数数组的末尾追加新元素，并返回一个新数组
&lt;A, O extends A&gt; A[] addObjectToArray(A[] array, O obj)
// 原生基础类型数组 --&gt; 包装类数组
Object[] toObjectArray(Object source)

```

## 3、字符串工具StringUtils

## 3.1、StringUtils判断方法

```
// 判断字符串是否为 null，或 ""。注意，包含空白符的字符串为非空
boolean isEmpty(Object str)
// 判断字符串是否是以指定内容结束。忽略大小写
boolean endsWithIgnoreCase(String str, String suffix)
// 判断字符串是否已指定内容开头。忽略大小写
boolean startsWithIgnoreCase(String str, String prefix) 
// 是否包含空白符
boolean containsWhitespace(String str)
// 判断字符串非空且长度不为 0，即，Not Empty
boolean hasLength(CharSequence str)
// 判断字符串是否包含实际内容，即非仅包含空白符，也就是 Not Blank
boolean hasText(CharSequence str)
// 判断字符串指定索引处是否包含一个子串。
boolean substringMatch(CharSequence str, int index, CharSequence substring)
// 计算一个字符串中指定子串的出现次数
int countOccurrencesOf(String str, String sub)

```

## 3.1、StringUtils字符串操作方法

```
// 查找并替换指定子串
String replace(String inString, String oldPattern, String newPattern)
// 去除尾部的特定字符
String trimTrailingCharacter(String str, char trailingCharacter) 
// 去除头部的特定字符
String trimLeadingCharacter(String str, char leadingCharacter)
// 去除头部的空白符
String trimLeadingWhitespace(String str)
// 去除头部的空白符
String trimTrailingWhitespace(String str)
// 去除头部和尾部的空白符
String trimWhitespace(String str)
// 删除开头、结尾和中间的空白符
String trimAllWhitespace(String str)
// 删除指定子串
String delete(String inString, String pattern)
// 删除指定字符（可以是多个）
String deleteAny(String inString, String charsToDelete)
// 对数组的每一项执行 trim() 方法
String[] trimArrayElements(String[] array)
// 将 URL 字符串进行解码
String uriDecode(String source, Charset charset)

```

### 3.1、StringUtils路径相关方法

```
// 解析路径字符串，优化其中的 “..” 
String cleanPath(String path)
// 解析路径字符串，解析出文件名部分
String getFilename(String path)
// 解析路径字符串，解析出文件后缀名
String getFilenameExtension(String path)
// 比较两个两个字符串，判断是否是同一个路径。会自动处理路径中的 “..” 
boolean pathEquals(String path1, String path2)
// 删除文件路径名中的后缀部分
String stripFilenameExtension(String path) 
// 以 “. 作为分隔符，获取其最后一部分
String unqualify(String qualifiedName)
// 以指定字符作为分隔符，获取其最后一部分
String unqualify(String qualifiedName, char separator)

```

## 4、集合判断工具CollectionUtils

```
// 判断 List/Set 是否为空
boolean isEmpty(Collection&lt;?&gt; collection)
// 判断 Map 是否为空
boolean isEmpty(Map&lt;?,?&gt; map)
// 判断 List/Set 中是否包含某个对象
boolean containsInstance(Collection&lt;?&gt; collection, Object element)
// 以迭代器的方式，判断 List/Set 中是否包含某个对象
boolean contains(Iterator&lt;?&gt; iterator, Object element)
// 判断 List/Set 是否包含某些对象中的任意一个
boolean containsAny(Collection&lt;?&gt; source, Collection&lt;?&gt; candidates)
// 判断 List/Set 中的每个元素是否唯一。即 List/Set 中不存在重复元素
boolean hasUniqueObject(Collection&lt;?&gt; collection)

```

### 4.1、CollectionUtils集合操作方法

```
// 将 Array 中的元素都添加到 List/Set 中
&lt;E&gt; void mergeArrayIntoCollection(Object array, Collection&lt;E&gt; collection)  
// 将 Properties 中的键值对都添加到 Map 中
&lt;K,V&gt; void mergePropertiesIntoMap(Properties props, Map&lt;K,V&gt; map)
// 返回 List 中最后一个元素
&lt;T&gt; T lastElement(List&lt;T&gt; list)  
// 返回 Set 中最后一个元素
&lt;T&gt; T lastElement(Set&lt;T&gt; set) 
// 返回参数 candidates 中第一个存在于参数 source 中的元素
&lt;E&gt; E findFirstMatch(Collection&lt;?&gt; source, Collection&lt;E&gt; candidates)
// 返回 List/Set 中指定类型的元素。
&lt;T&gt; T findValueOfType(Collection&lt;?&gt; collection, Class&lt;T&gt; type)
// 返回 List/Set 中指定类型的元素。如果第一种类型未找到，则查找第二种类型，以此类推
Object findValueOfType(Collection&lt;?&gt; collection, Class&lt;?&gt;[] types)
// 返回 List/Set 中元素的类型
Class&lt;?&gt; findCommonElementType(Collection&lt;?&gt; collection)

```

## 5、文件、资源、IO 流FileCopyUtils

### 5.1、输入

```
// 从文件中读入到字节数组中
byte[] copyToByteArray(File in)
// 从输入流中读入到字节数组中
byte[] copyToByteArray(InputStream in)
// 从输入流中读入到字符串中
String copyToString(Reader in)

```

### 5.2、输出

```
// 从字节数组到文件
void copy(byte[] in, File out)
// 从文件到文件
int copy(File in, File out)
// 从字节数组到输出流
void copy(byte[] in, OutputStream out) 
// 从输入流到输出流
int copy(InputStream in, OutputStream out) 
// 从输入流到输出流
int copy(Reader in, Writer out)
// 从字符串到输出流
void copy(String in, Writer out)

```

## 6、ResourceUtils从资源路径获取文件

```
// 判断字符串是否是一个合法的 URL 字符串。
static boolean isUrl(String resourceLocation)
// 获取 URL
static URL getURL(String resourceLocation) 
// 获取文件（在 JAR 包内无法正常使用，需要是一个独立的文件）
static File	getFile(String resourceLocation)

```

## 7、Resource实现类

```
// 文件系统资源 D:\...
FileSystemResource
// URL 资源，如 file://... http://...
UrlResource
// 类路径下的资源，classpth:...
ClassPathResource
// Web 容器上下文中的资源（jar 包、war 包）
ServletContextResource

```

### 7.1、Resource实现类方法

```
// 判断资源是否存在
boolean exists()
// 从资源中获得 File 对象
File getFile()
// 从资源中获得 URI 对象
URI getURI()
// 从资源中获得 URI 对象
URL getURL()
// 获得资源的 InputStream
InputStream getInputStream()
// 获得资源的描述信息
String getDescription()

```

## 8、StreamUtils

### 8.1、StreamUtils输入

```
void copy(byte[] in, OutputStream out)
int copy(InputStream in, OutputStream out)
void copy(String in, Charset charset, OutputStream out)
long copyRange(InputStream in, OutputStream out, long start, long end)

```

### 8.1、StreamUtils输出

```
byte[] copyToByteArray(InputStream in)
String copyToString(InputStream in, Charset charset)
// 舍弃输入流中的内容
int drain(InputStream in) 

```

## 9、反射、AOP ReflectionUtils

### 9.1、获取方法

```
// 在类中查找指定方法
Method findMethod(Class&lt;?&gt; clazz, String name) 
// 同上，额外提供方法参数类型作查找条件
Method findMethod(Class&lt;?&gt; clazz, String name, Class&lt;?&gt;... paramTypes) 
// 获得类中所有方法，包括继承而来的
Method[] getAllDeclaredMethods(Class&lt;?&gt; leafClass) 
// 在类中查找指定构造方法
Constructor&lt;T&gt; accessibleConstructor(Class&lt;T&gt; clazz, Class&lt;?&gt;... parameterTypes) 
// 是否是 equals() 方法
boolean isEqualsMethod(Method method) 
// 是否是 hashCode() 方法 
boolean isHashCodeMethod(Method method) 
// 是否是 toString() 方法
boolean isToStringMethod(Method method) 
// 是否是从 Object 类继承而来的方法
boolean isObjectMethod(Method method) 
// 检查一个方法是否声明抛出指定异常
boolean declaresException(Method method, Class&lt;?&gt; exceptionType) 

```

### 9.2、执行方法

```
// 执行方法
Object invokeMethod(Method method, Object target)  
// 同上，提供方法参数
Object invokeMethod(Method method, Object target, Object... args) 
// 取消 Java 权限检查。以便后续执行该私有方法
void makeAccessible(Method method) 
// 取消 Java 权限检查。以便后续执行私有构造方法
void makeAccessible(Constructor&lt;?&gt; ctor) 

```

### 9.3、获取字段

```
// 在类中查找指定属性
Field findField(Class&lt;?&gt; clazz, String name) 
// 同上，多提供了属性的类型
Field findField(Class&lt;?&gt; clazz, String name, Class&lt;?&gt; type) 
// 是否为一个 "public static final" 属性
boolean isPublicStaticFinal(Field field) 

```

### 9.4、设置字段

```
// 获取 target 对象的 field 属性值
Object getField(Field field, Object target) 
// 设置 target 对象的 field 属性值，值为 value
void setField(Field field, Object target, Object value) 
// 同类对象属性对等赋值
void shallowCopyFieldState(Object src, Object dest)
// 取消 Java 的权限控制检查。以便后续读写该私有属性
void makeAccessible(Field field) 
// 对类的每个属性执行 callback
void doWithFields(Class&lt;?&gt; clazz, ReflectionUtils.FieldCallback fc) 
// 同上，多了个属性过滤功能。
void doWithFields(Class&lt;?&gt; clazz, ReflectionUtils.FieldCallback fc, 
                  ReflectionUtils.FieldFilter ff) 
// 同上，但不包括继承而来的属性
void doWithLocalFields(Class&lt;?&gt; clazz, ReflectionUtils.FieldCallback fc) 

```

## 10、代理工具类AopUtils

### 10.1、判断代理类型

```
// 判断是不是 Spring 代理对象
boolean isAopProxy()
// 判断是不是 jdk 动态代理对象
isJdkDynamicProxy()
// 判断是不是 CGLIB 代理对象
boolean isCglibProxy()

```

### 10.2、获取被代理对象的 class

```
// 获取被代理的目标 class
Class&lt;?&gt; getTargetClass()

```

## 11、获取当前对象的代理对象AopContext

```
Object currentProxy()


```
