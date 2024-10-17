
--- 
title:  《Java 简易速速上手小册》第9章：Java 开发工具和框架 （2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/31a56835f64840babd18b978bd54d2c4.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 9.1 Maven 和 Gradle - 构建与依赖管理的神兵利器

在Java的世界里，Maven和Gradle是两位强大的法师，专门负责管理构建和依赖，确保开发者能够专注于编码而不是琐碎的构建细节。

### 9.1.1 基础知识
- **Maven**：通过`pom.xml`文件管理项目的生命周期、依赖、插件等。它遵循“约定优于配置”的原则，简化了项目构建过程。- **Gradle**：基于Groovy的DSL（领域特定语言）进行项目配置，提供了更高的灵活性和强大的性能。它允许开发者编写更简洁的构建脚本。
### 9.1.2 重点案例：使用 Maven 构建 Spring Boot 应用

让我们开始一个新的探险，使用Maven来构建一个简单的Spring Boot应用。

**步骤**:
1. 创建`pom.xml`文件，并添加Spring Boot起步依赖。
```
&lt;project&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;groupId&gt;com.adventure&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-quest&lt;/artifactId&gt;
    &lt;version&gt;1.0.0&lt;/version&gt;
    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
        &lt;version&gt;2.3.1.RELEASE&lt;/version&gt;
    &lt;/parent&gt;
    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;
&lt;/project&gt;

```
1. 创建主类`AdventureApplication.java`，并运行Spring Boot应用。
```
package com.adventure;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AdventureApplication {<!-- -->
    public static void main(String[] args) {<!-- -->
        SpringApplication.run(AdventureApplication.class, args);
    }
}

```

### 9.1.3 拓展案例 1：使用 Gradle 构建多模块项目

在一个更大的探险中，你可能需要将你的项目分成多个模块。Gradle提供了强大的多项目构建支持。

**根项目的`build.gradle`**:

```
allprojects {<!-- -->
    group 'com.adventure'
    version '1.0.0'
}

subprojects {<!-- -->
    apply plugin: 'java'
}

project(':library') {<!-- -->
    dependencies {<!-- -->
        // 依赖配置
    }
}

project(':application') {<!-- -->
    dependencies {<!-- -->
        implementation project(':library')
    }
}

```

**设置模块**:

在根项目的`settings.gradle`文件中声明模块。

```
rootProject.name = 'multi-module-adventure'
include 'application', 'library'

```

### 9.1.4 拓展案例 2：利用 Gradle Wrapper 确保构建的一致性

Gradle Wrapper是一个脚本和库的集合，它允许你不需要预先安装Gradle就能构建你的项目。这保证了每个开发者和CI/CD环境使用相同版本的Gradle，避免了“在我的机器上可以运行”的问题。

**生成Gradle Wrapper**:

在项目根目录执行以下命令：

```
gradle wrapper --gradle-version 6.3

```

这会生成`gradlew`和`gradlew.bat`脚本以及`gradle/wrapper`目录，你可以将这些文件加入版本控制。

**使用Gradle Wrapper构建项目**:

```
./gradlew build

```

通过这些案例，你已经学会了如何使用Maven和Gradle这两位强大的法师来管理你的Java项目。它们不仅可以帮助你轻松地构建和管理项目，还能确保项目的构建过程简洁高效。现在，带上这些神兵利器，继续你的Java冒险吧！

<img src="https://img-blog.csdnimg.cn/direct/08dc039e8be84a44bcaa618c2f580d2c.png#pic_center" alt="在这里插入图片描述" width="400">

## 9.2 Spring 框架概述 - Java 世界的魔法园林

Spring框架是Java开发中的一片魔法园林，它提供了一系列的魔法（框架特性）来帮助开发者高效地创建企业级应用。从依赖注入、面向切面编程到操作数据和构建Web应用，Spring让这一切变得简单而优雅。

### 9.2.1 基础知识
- **依赖注入（DI）**：Spring的核心特性，允许你通过声明方式而非硬编码方式来管理组件之间的依赖关系，增加了代码的灵活性和可测试性。- **面向切面编程（AOP）**：允许你定义通用的逻辑（如事务管理和安全），并将这些逻辑应用到多个点，减少了代码的重复。- **Spring MVC**：一个强大的构建Web应用的框架，它提供了一种分离控制器、模型对象、和视图的方法，使得Web应用的开发变得更加清晰和简单。- **Spring Boot**：在Spring的基础上进一步简化了配置和部署的流程，让开发者可以快速启动新项目。
### 9.2.2 重点案例：构建 RESTful Web 服务

我们将使用Spring Boot来构建一个简单的RESTful Web服务，展示如何快速开发和部署一个Spring应用。

**步骤**:
1. 创建一个新的Spring Boot项目。1. 添加`spring-boot-starter-web`依赖。1. 创建一个新的`RestController`来处理HTTP请求。
**示例代码**:

```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class MagicGardenApplication {<!-- -->

    public static void main(String[] args) {<!-- -->
        SpringApplication.run(MagicGardenApplication.class, args);
    }

    @GetMapping("/hello")
    public String sayHello() {<!-- -->
        return "Welcome to the Magic Garden of Spring!";
    }
}

```

### 9.2.3 拓展案例 1：使用 Spring Data JPA 操作数据库

Spring Data JPA让操作数据库变得轻松愉快，我们将通过一个简单的例子来展示如何使用Spring Data JPA来持久化数据到数据库。

**步骤**:
1. 添加`spring-boot-starter-data-jpa`和数据库驱动的依赖。1. 创建一个实体类和一个Repository接口。1. 使用Repository接口进行数据操作。
**示例代码**:

```
import org.springframework.data.jpa.repository.JpaRepository;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Adventure {<!-- -->
    @Id
    @GeneratedValue
    private Long id;
    private String name;
    // Getters and setters omitted for brevity
}

public interface AdventureRepository extends JpaRepository&lt;Adventure, Long&gt; {<!-- -->
}

```

### 9.2.4 拓展案例 2：利用 Spring Security 增强应用安全

Spring Security提供了一系列强大的安全特性，帮助你保护你的应用免受常见安全威胁。我们将展示如何添加基本的HTTP认证。

**步骤**:
1. 添加`spring-boot-starter-security`依赖。1. 创建一个`WebSecurityConfigurerAdapter`的实现，来配置安全策略。
**示例代码**:

```
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

public class SecurityConfig extends WebSecurityConfigurerAdapter {<!-- -->

    @Override
    protected void configure(HttpSecurity http) throws Exception {<!-- -->
        http
            .authorizeRequests().anyRequest().authenticated()
            .and()
            .httpBasic();
    }
}

```

通过以上案例，你已经学会了如何使用 Spring 框架来快速开发一个 RESTful Web 服务，如何使用 Spring Data JPA 操作数据库，以及如何利用 Spring Security 增强应用的安全性。Spring 框架的魔法园林中藏着无尽的可能，探索它们将使你的 Java 开发之旅充满乐趣和惊喜。

<img src="https://img-blog.csdnimg.cn/direct/bc981438a9944d8088272d56c1e70b47.png#pic_center" alt="在这里插入图片描述" width="400">

## 9.3 JUnit 测试 - 保证你的魔法不会走火

在Java世界的冒险中，编写魔法（代码）是一件充满乐趣的事情，但要确保每次施法都能精准有效，就需要一位可靠的法术校验师——这就是JUnit测试的角色。通过JUnit测试，我们可以确保我们的魔法（代码逻辑）正如我们所期望的那样工作，避免在实际使用中出现意外。

### 9.3.1 基础知识
- **JUnit 5**：是当前最新的Java测试框架版本，提供了更加强大和灵活的测试特性，包括但不限于显示名称的测试、动态测试、参数化测试以及更多的生命周期回调。- **断言**：JUnit提供了一系列的断言方法，用于验证测试结果是否符合预期，是测试中最常用的工具之一。- **测试注解**：JUnit 5引入了一系列新的注解来支持更复杂的测试场景，如`@BeforeEach`、`@AfterEach`、`@BeforeAll`、`@AfterAll`、`@Test`等。
### 9.3.2 重点案例：测试一个简单的计算器类

假设我们有一个简单的计算器类，提供了加法和减法功能，我们将编写测试用例来验证这些功能。

**Calculator.java**:

```
public class Calculator {<!-- -->
    public int add(int a, int b) {<!-- -->
        return a + b;
    }

    public int subtract(int a, int b) {<!-- -->
        return a - b;
    }
}

```

**CalculatorTest.java**:

```
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class CalculatorTest {<!-- -->
    private final Calculator calculator = new Calculator();

    @Test
    void testAdd() {<!-- -->
        assertEquals(5, calculator.add(2, 3), "2 + 3 should equal 5");
    }

    @Test
    void testSubtract() {<!-- -->
        assertEquals(1, calculator.subtract(3, 2), "3 - 2 should equal 1");
    }
}

```

### 9.3.3 拓展案例 1：使用参数化测试

当我们需要对同一方法使用不同的参数进行测试时，参数化测试可以大大简化测试代码。

**ParameterizedCalculatorTest.java**:

```
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class ParameterizedCalculatorTest {<!-- -->
    private final Calculator calculator = new Calculator();

    @ParameterizedTest
    @CsvSource({<!-- -->"2, 3, 5", "3, 5, 8", "-1, -2, -3"})
    void testAdd(int a, int b, int expectedResult) {<!-- -->
        assertEquals(expectedResult, calculator.add(a, b),
            () -&gt; a + " + " + b + " should equal " + expectedResult);
    }
}

```

### 9.3.4 拓展案例 2：模拟外部依赖

在测试时，经常需要模拟外部依赖，以确保测试的独立性。我们可以使用Mockito框架来模拟这些依赖。

假设我们的计算器现在需要记录每次计算的结果，我们将模拟这个记录器。

**CalculatorWithLoggerTest.java**:

```
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(MockitoExtension.class)
public class CalculatorWithLoggerTest {<!-- -->
    @Mock
    private Logger logger;

    @Test
    void testAdd() {<!-- -->
        Calculator calculator = new Calculator(logger);
        calculator.add(2, 3);
        verify(logger).log("Adding 2 + 3");
    }
}

```

通过这些案例，你已经学会了如何使用JUnit进行基本测试、参数化测试以及如何在测试中模拟外部依赖。这些技巧将帮助你确保你的Java代码更加健壮、可靠。记住，一个好的魔法师不仅仅会施法，还会确保每次施法都是安全可控的。
