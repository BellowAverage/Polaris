
--- 
title:  HashSet存储自定义类型元素 
tags: []
categories: [] 

---
## 一、HashSet不重复原理

前提：所存储的类型已经重写了hashCode方法和equals方法

### 存储原理：

         假设，我要将  "abc" "西瓜" "喝茶"  "123" "123" ，共五个元素存入HashSet集合里，可知，要存储的类型为:String类型，通过查看String的源码可知，该类已经重写了hashSet和equals方法，我们这块主要分析它存储原理，所以直接使用即可，具体代码如下：

```
public static void main(String[] args) {
		HashSet&lt;String&gt; hashSet = new HashSet&lt;String&gt;();
		//存储: "abc" "西瓜" "喝茶"  "123" "123"
		hashSet.add("abc");
		hashSet.add("123");
		hashSet.add("西瓜");
		hashSet.add("喝茶");
		hashSet.add("123");
//哈希值的算法,比如abc,a对应的ASCII为:97,b-98,c-99,hashCode=97*31^2+98*31^1+99*31^0=96354
		System.out.println("abc的哈希值为:"+"abc".hashCode());
		System.out.println("123的哈希值为:"+"123".hashCode());
		System.out.println("西瓜的哈希值为:"+"西瓜".hashCode());
		System.out.println("喝茶的哈希值为:"+"喝茶".hashCode());

		System.out.println("集合的大小为:"+hashSet.size()+",其中所存储的元素为:");
		for(String str:hashSet)	System.out.println(str);
		
	}
```

结果:

<img alt="" class="has" height="206" src="https://img-blog.csdnimg.cn/20190810161120133.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="897">

### 那么，如何保证所存入的元素的唯一性呢？

这个时候，就要求我们必须重写所存入元素的hashCode和equals方法，通过hashCode方法得到的哈希码作为这个元素的存储地址（这个值跟地址有关，但不是实际地址），通过equals方法比较是否相同，相同则不再存储，不相同的话就会产生冲突，会产生一个链接表，将这两个元素串起来放在同一个哈希码指定的位置上，而实际上会尽量避免哈希冲突。如果直接调用equals方法，当数据量过大时，每次都会调用一次equals方法，效率低。

第一步：hashSet.add("abc");  //abc所对应的的哈希值为:96354

           //在集合中查找有没有哈希值为96354的元素，发现没有，存入

第二步:  hashSet.add("123");   //123对应的哈希值为：48690

           //在集合中查找有没有哈希值为48690的元素，发现没有，存入 第三步:  hashSet.add("西瓜");    //西瓜对应的哈希值为：713017(这里使用假设值)

           //会在集合中查找有没有哈希值为713017的元素，是否有元素，发现没有 第四步 : hashSet.add("喝茶");   //713017           //会在集合中查找有没有哈希值为713017的元素，是否有元素，发现已经有了，此时，会调用equals方法，判断这两个元素是否相同，发现相同，则不会再存储，发现不相同，则会在当前位置上加一个链表，将此元素加入此位置的链表上。

第五步:hashSet.add("123"); //48690

         //已经有了哈希值为48690了，通过equals方法发现相同，此时，不会再存储此元素。

### 运行完的存储状态如图:

<img alt="" class="has" height="210" src="https://img-blog.csdnimg.cn/20190810164525894.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="341">

## 二、存储自定义类型

自定义类型也就是我们自己创建的实体类。

### 2.1创建实体类Student

```
public class Student {
	private String id;   //学号
	private String name; //姓名
	private Integer age; //年龄
	public Student(){}
	public Student(String id, String name, Integer age) {
		this.id = id;
		this.name = name;
		this.age = age;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
	@Override
	public String toString() {
		return "id=" + id + ", name=" + name + ", age=" + age;
	}
	
}
```

### 2.1.1使用HashSet集合:

```
public static void main(String[] args) {
		Student stu1 = new Student("2019", "第一人", 1);
		Student stu2 = new Student("2019", "第二人", 2);
		Student stu3 = new Student("2019", "第一人", 1);
		HashSet&lt;Student&gt; hasStudents = new HashSet&lt;Student&gt;();
		hasStudents.add(stu1);
		hasStudents.add(stu2);
		hasStudents.add(stu3);
		System.out.println("集合大小:"+hasStudents.size());
		for(Student student:hasStudents)	System.out.println(student);
		
	}
```

### 2.1.2结果:

<img alt="" class="has" height="102" src="https://img-blog.csdnimg.cn/20190810170233142.png" width="814">

其实，这两个对象的属性虽然是一模一样的，但是它是两个对象，我们可以看一下stu1和stu3对应的哈希值，可以推测一下，既然能够存储，那么这两个的哈希值肯定不一样。

又出现了一个问题，自定义的类中并没有重写hashCode方法为什么会出现哈希值呢？

其实，所有的类都默认继承了Object类，因此呢，此处肯定，调用了Object类中的hashCode方法

<img alt="" class="has" height="49" src="https://img-blog.csdnimg.cn/20190810171427292.png" width="614">

但是，在现实生活中，当一个学生的id，姓名，年龄三者都一模一样，那么肯定为同一个人，所以上述所体现的存储效果就和现实生活有差别了，因此呢，此时必须重写hashCode和equals方法，我们可以自定义比较方法来判断是否为同一个人！

### 2.2复写hashCode方法

```
	//重写hashCode的第一种方法
    @Override
	public int hashCode() {//是用来util包的Objects类，1.7出现的，可以看一下源码
		return Objects.hash(id,name,age);
	}
    //重写hashCode的第二种方法
    @Override
	public int hashCode() {
		return this.id.hashCode()+this.name.hashCode()+this.age.hashCode();
	}

/*---------------------------------源码如下：------------------------------
//Objects类
 public static int hash(Object... values) {
        return Arrays.hashCode(values);
    }
//Arrays类
 public static int hashCode(Object a[]) {
        if (a == null)
            return 0;

        int result = 1;

        for (Object element : a)
            result = 31 * result + (element == null ? 0 : element.hashCode());

        return result;
    }
//Object类
public native int hashCode();
*/
```

#### 结果

<img alt="" class="has" height="159" src="https://img-blog.csdnimg.cn/20190810175819252.png" width="317">                                      <img alt="" class="has" height="154" src="https://img-blog.csdnimg.cn/20190810175854388.png" width="312">

会发现两种方式都实现了重写hashCode方法，虽然哈希值虽然已经一样（此处有个小问题，两个复写hashCode方法的区别是什么？后边我会说....），但还是3个人，意思就是系统还是认为这就是三个不一样的人，接下来就要重写equals方法，告诉系统，通过什么规则来比较是否为同一个元素。

### 2.3复写equals方法

```
//第一种方法
@Override
	public boolean equals(Object obj) {
		if(this == obj)	return true;  //判断地址
		if(obj == null || !(obj instanceof Student))	return false;//为null或根本没有可比性
		Student stu = (Student) obj;
		return Objects.equals(id, stu.id)   //可以看一下源码
				&amp;&amp; Objects.equals(name, stu.name)
				&amp;&amp; this.age == stu.age;
		
	}
//第二种方法
@Override
	public boolean equals(Object obj) {
		if(this == obj)	return true;  //两个对象的地址一样
		if(obj == null || !(obj instanceof Student))	return false;//为null或根本没有可比性
		Student stu = (Student) obj;
		return this.id.equals(stu.id)
				&amp;&amp; this.name.equals(stu.name)
				&amp;&amp; this.age == stu.age;
		
	}

/*----------------------------源码如下--------------------------
 public static boolean equals(Object a, Object b) {
        return (a == b) || (a != null &amp;&amp; a.equals(b));
    }
*/
```

#### 结果

<img alt="" class="has" height="71" src="https://img-blog.csdnimg.cn/20190810181351781.png" width="313">         <img alt="" class="has" height="72" src="https://img-blog.csdnimg.cn/20190810181528763.png" width="318">

（可以发现，两个equals方法都已经实现了我们想要的效果，但细心地小伙伴会发现，这两个equals方法区别是什么呢？还有之前两种复写hashCode方法的区别呢？）

### 2.4结论

#### 2.4.1第一种复写hashCode和equals方法

都是通过java.util下的工具类Objects中的方法来实现的

```
@Override
	public int hashCode() {
		return Objects.hash(id,name,age);
	}
	@Override
	public boolean equals(Object obj) {
		if(this == obj)	return true;  //两个对象的地址一样
		if(obj == null || !(obj instanceof Student))	return false;//为null或根本没有可比性
		Student stu = (Student) obj;
		return Objects.equals(id, stu.id)
				&amp;&amp; Objects.equals(name, stu.name)
				&amp;&amp; this.age == stu.age;
		
	}
```

#### 2.4.2第二种复写hashCode和equals方法

```
@Override
	public int hashCode() {
		return id.hashCode()+name.hashCode()+age.hashCode();
	}
	@Override
	public boolean equals(Object obj) {
		if(this == obj)	return true;  //两个对象的地址一样
		if(obj == null || !(obj instanceof Student))	return false;//为null或根本没有可比性
		Student stu = (Student) obj;
		return this.id.equals(stu.id)
				&amp;&amp; this.name.equals(stu.name)
				&amp;&amp; this.age == stu.age;
		
	}
```

通过，第一种方法的源码不难发现，两者之间的差别就在于，第一种多了一步判断是否为Null的条件，这也就让第一种方法比第二种方法更加鲁棒(健壮)，但是通过我以上代码的演示来看，并没有出现空指针异常啊，其实，那是因为我故意避开了这个错误，要想看到这个错误很简单，我们加这样一个构造函数，比如:

```
public Student(String id, Integer age) {//只对id和年龄构造
		this.id = id;
		this.age = age;
	}
```

接下来使用第二种重写的方法，

最后，修改测试对象，如下

```
Student stu1 = new Student("2019", 1);
Student stu2 = new Student("2019", "第二人", 2);
Student stu3 = new Student("2019", 1);
```

运行，会发现

<img alt="" class="has" height="133" src="https://img-blog.csdnimg.cn/20190810183445834.png" width="633">

找到，com.duotai包下的Student类hashCode方法，也就是第46行，

<img alt="" class="has" height="23" src="https://img-blog.csdnimg.cn/20190810183631296.png" width="720">

也就是，name.hashCode()报错，因为我们并没有给对象的name属性进行初始化，你就直接拿它来调用方法，所以报空指针异常。

#### 因此，在实际应用中，我们一定要尽量使用第一种复写方法，因为它包含了对null的判断，或者自己写对null值的判断，这样会让我们的程序更加健壮！
