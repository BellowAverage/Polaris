
--- 
title:  Spring Boot 自动配置原理 
tags: []
categories: [] 

---
### 1 加载

SpringBoot 应用启动的时候，从主方法进行启动。

```
@SpringBootApplication
public class XxxApplication {<!-- -->
  public static void main(String[] args) {<!-- -->
    SpringApplication.run(XxxApplication.class, args);
  }
}

```

@SpringBootApplication 是一个组合注解。包含如下注解：

```
@Target({<!-- -->ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(
    excludeFilters = {<!-- -->@Filter(
    type = FilterType.CUSTOM,
    classes = {<!-- -->TypeExcludeFilter.class}
), @Filter(
    type = FilterType.CUSTOM,
    classes = {<!-- -->AutoConfigurationExcludeFilter.class}
)}
)

```

@EnableAutoConfiguration 为开启自动配置，其也是组合注解。包含如下注解：

```
@Target({<!-- -->ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@AutoConfigurationPackage
@Import({<!-- -->AutoConfigurationImportSelector.class})

```

主要功能由 @Import 提供，其导入的 AutoConfigurationImportSelector 的 selectImports 方法。

```
public String[] selectImports(AnnotationMetadata annotationMetadata) {<!-- -->
    if (!this.isEnabled(annotationMetadata)) {<!-- -->
        return NO_IMPORTS;
    } else {<!-- -->
        AutoConfigurationMetadata autoConfigurationMetadata = AutoConfigurationMetadataLoader.loadMetadata(this.beanClassLoader);
        AutoConfigurationImportSelector.AutoConfigurationEntry autoConfigurationEntry = this.getAutoConfigurationEntry(autoConfigurationMetadata, annotationMetadata);
        return StringUtils.toStringArray(autoConfigurationEntry.getConfigurations());
    }
}

```

调用 getAutoConfigurationEntry 方法。

```
protected AutoConfigurationImportSelector.AutoConfigurationEntry getAutoConfigurationEntry(AutoConfigurationMetadata autoConfigurationMetadata, AnnotationMetadata annotationMetadata) {<!-- -->
  if (!this.isEnabled(annotationMetadata)) {<!-- -->
    return EMPTY_ENTRY;
  } else {<!-- -->
    AnnotationAttributes attributes = this.getAttributes(annotationMetadata);
    List&lt;String&gt; configurations = this.getCandidateConfigurations(annotationMetadata, attributes);
    configurations = this.removeDuplicates(configurations);
    Set&lt;String&gt; exclusions = this.getExclusions(annotationMetadata, attributes);
    this.checkExcludedClasses(configurations, exclusions);
    configurations.removeAll(exclusions);
    configurations = this.filter(configurations, autoConfigurationMetadata);
    this.fireAutoConfigurationImportEvents(configurations, exclusions);
    return new AutoConfigurationImportSelector.AutoConfigurationEntry(configurations, exclusions);
  }
}

```

调用 getCandidateConfigurations 方法。

```
protected List&lt;String&gt; getCandidateConfigurations(AnnotationMetadata metadata, AnnotationAttributes attributes) {<!-- -->
  List&lt;String&gt; configurations = SpringFactoriesLoader.loadFactoryNames(this.getSpringFactoriesLoaderFactoryClass(), this.getBeanClassLoader());
  Assert.notEmpty(configurations, "No auto configuration classes found in META-INF/spring.factories. If you are using a custom packaging, make sure that file is correct.");
  return configurations;
}

```

通过 loadFactoryNames 方法扫描 spring.factories 文件中包含的 JAR 文件，加载到 Spring 容器。

```
public static AutoConfigurationMetadata loadMetadata(ClassLoader classLoader) {<!-- -->
    return loadMetadata(classLoader, "META-INF/spring-autoconfigure-metadata.properties");
}

```

### 2 生效

这些自动配置类都是在某些条件下生效。

```
@ConditionalOnBean：当容器里有指定的bean的条件下
@ConditionalOnMissingBean：当容器里不存在指定bean的条件下
@ConditionalOnClass：当类路径下有指定类的条件下
@ConditionalOnMissingClass：当类路径下不存在指定类的条件下
@ConditionalOnProperty：指定的属性是否有指定的值

```

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
