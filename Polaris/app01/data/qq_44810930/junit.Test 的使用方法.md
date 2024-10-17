
--- 
title:  junit.Test 的使用方法 
tags: []
categories: [] 

---
在 Maven 项目中使用 JUnit，你需要在项目的 `pom.xml` 文件中添加 JUnit 依赖。然后，你可以创建测试类，并在测试类中使用 `@Test` 注解标识测试方法。 

#### 文章目录
- - - <ul><li>- - - - 


## 基本使用

以下是一般步骤：
1. **在 `pom.xml` 文件中添加 JUnit 依赖：**
```
&lt;dependencies&gt;
    &lt;!-- 其他依赖... --&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;junit&lt;/groupId&gt;
        &lt;artifactId&gt;junit&lt;/artifactId&gt;
        &lt;version&gt;4.12&lt;/version&gt; &lt;!-- 版本号可能会有更新 --&gt;
        &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;

```

确保将 JUnit 依赖的作用范围（`&lt;scope&gt;`）设置为 `test`，这样 JUnit 将只在测试阶段可用，而不会影响应用程序的运行时依赖。
1. **创建测试类：**
创建一个测试类，例如 `MyTestClass`，其中包含测试方法并使用 `@Test` 注解标识：

```
import org.junit.Test;
import static org.junit.Assert.*;

public class MyTestClass {<!-- -->

    @Test
    public void testAddition() {<!-- -->
        int result = 2 + 2;
        assertEquals(4, result); // 断言，验证结果是否符合预期
    }

    @Test
    public void testSubtraction() {<!-- -->
        int result = 5 - 3;
        assertTrue(result &gt; 0); // 断言，验证结果是否为真
    }
}

```
1. **运行测试：**
你可以使用 Maven 命令来运行测试。在项目的根目录下执行以下命令：

```
mvn test

```

或者直接在IDEA中点击左侧的绿色三角

这将会编译项目并运行所有的测试类。测试结果将会显示在控制台上。

注意：如果你使用的是 JUnit 5，依赖的坐标和测试类的注解会有所不同。

在这种情况下，你需要使用 `junit-jupiter-api` 和 `junit-jupiter-engine` 依赖，以及使用 `@Test` 注解来标识测试方法。在 `pom.xml` 中可能看起来类似于以下内容：

```
&lt;dependencies&gt;
    &lt;!-- 其他依赖... --&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.junit.jupiter&lt;/groupId&gt;
        &lt;artifactId&gt;junit-jupiter-api&lt;/artifactId&gt;
        &lt;version&gt;5.8.0&lt;/version&gt; &lt;!-- 版本号可能会有更新 --&gt;
        &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.junit.jupiter&lt;/groupId&gt;
        &lt;artifactId&gt;junit-jupiter-engine&lt;/artifactId&gt;
        &lt;version&gt;5.8.0&lt;/version&gt; &lt;!-- 版本号可能会有更新 --&gt;
        &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;

```

## 其他注解

JUnit 提供了多个注解，用于标识测试类和测试方法的不同方面。以下是一些常用的 JUnit 注解：

### @Before 和 @After
- `@Before` 注解标识的方法在每个测试方法之前执行，用于进行一些初始化操作。- `@After` 注解标识的方法在每个测试方法之后执行，用于进行一些清理操作。
```
```java
import org.junit.Before;
import org.junit.After;

public class MyTestClass {

    @Before
    public void setUp() {
        // 执行初始化操作
    }

    @After
    public void tearDown() {
        // 执行清理操作
    }

    // 测试方法...
}
```

```

### @BeforeClass 和 @AfterClass
- `@BeforeClass` 注解标识的方法在所有测试方法执行前执行，通常用于执行一次性的设置。- `@AfterClass` 注解标识的方法在所有测试方法执行完毕后执行，通常用于执行一次性的清理操作。
```
```java
import org.junit.BeforeClass;
import org.junit.AfterClass;

public class MyTestClass {

    @BeforeClass
    public static void setUpClass() {
        // 执行一次性的设置
    }

    @AfterClass
    public static void tearDownClass() {
        // 执行一次性的清理操作
    }

    // 测试方法...
}
```

```

### @Ignore
- `@Ignore` 注解用于标识不想执行的测试方法。可以用于临时禁用某些测试，通常在开发过程中用得较多。
```
```java
import org.junit.Ignore;

public class MyTestClass {

    @Test
    public void testMethod1() {
        // 测试代码...
    }

    @Ignore
    @Test
    public void testMethod2() {
        // 这个测试将会被忽略
    }
}
```

```

### @RunWith
- `@RunWith` 注解用于指定测试运行器（Runner）。JUnit 默认使用 `BlockJUnit4ClassRunner`，但你可以使用其他的运行器，例如 `Parameterized`，以实现不同的测试行为。
```
```java
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

@RunWith(Parameterized.class)
public class MyParameterizedTest {
    // 参数化测试代码...
}
```

```

这只是 JUnit 提供的一小部分注解，还有其他用于参数化测试、超时控制等的注解。不同版本的 JUnit 可能会引入新的注解或者修改现有注解的行为，因此查阅相应版本的文档是很重要的。

### 参数化测试

参数化测试是一种测试方法，它允许你使用不同的输入值多次运行相同的测试方法。 这对于测试同一片代码的不同输入或边缘情况非常有用。在 JUnit 4 中，参数化测试通常通过使用 `@RunWith` 注解和 `@Parameters` 注解来实现。

下面是一个简单的例子，演示了如何使用参数化测试：

```
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

import java.util.Arrays;
import java.util.Collection;

@RunWith(Parameterized.class)
public class MyParameterizedTest {<!-- -->

    private int input;
    private int expected;

    // 构造函数用于接收参数
    public MyParameterizedTest(int input, int expected) {<!-- -->
        this.input = input;
        this.expected = expected;
    }

    // 提供测试参数
    @Parameters
    public static Collection&lt;Object[]&gt; data() {<!-- -->
        return Arrays.asList(new Object[][] {<!-- -->
            {<!-- -->1, 2},
            {<!-- -->2, 4},
            {<!-- -->3, 6},
            {<!-- -->4, 8}
        });
    }

    // 实际测试方法
    @Test
    public void testMultiply() {<!-- -->
        MyClass myClass = new MyClass();
        assertEquals(expected, myClass.multiplyByTwo(input));
    }
}

```

在上面的例子中，`MyParameterizedTest` 类使用 `@RunWith(Parameterized.class)` 注解来告诉 JUnit 使用参数化运行器运行测试。然后，通过 `@Parameters` 注解提供了一组测试参数，其中每个参数是一个输入值和预期输出值的组合。测试方法 `testMultiply()` 会使用这些参数执行多次，确保代码在不同输入下的正确性。

需要注意的是，以上是基于 JUnit 4 的示例，JUnit 5 中引入了新的注解 `@ParameterizedTest`，并提供了更灵活的方式来执行参数化测试。在 JUnit 5 中，你可以使用 `@CsvSource`、`@ValueSource` 等注解来定义参数。
