
--- 
title:  【java】ObjectUtils 
tags: []
categories: [] 

---
### 检查两个对象的属性是否相同，可以排除不需要比较的属性

```
package com.ljq.common.lib.util;

import org.springframework.util.CollectionUtils;

import java.lang.reflect.Field;
import java.util.Set;

public class ObjectUtils {<!-- -->

    /**
     * 检查两个对象的属性是否相同，可以排除不需要比较的属性
     *
     * @param obj1          第一个对象
     * @param obj2          第二个对象
     * @param excludeFields 不需要比较的属性名称
     * @return 如果相同字段的数据不相同，返回true，否则返回false
     */
    public static boolean checkFieldEquals(Object obj1, Object obj2, Set&lt;String&gt; excludeFields) {<!-- -->
        if (obj1 == null || obj2 == null) {<!-- -->
            return false;
        }
        if (!obj1.getClass().equals(obj2.getClass())) {<!-- -->
            return false;
        }
        Field[] fields = obj1.getClass().getDeclaredFields();
        for (Field field : fields) {<!-- -->
            if (excludeFields != null &amp;&amp; (!CollectionUtils.isEmpty(excludeFields)) &amp;&amp; excludeFields.contains(field.getName())) {<!-- -->
                continue;
            }
            field.setAccessible(true);
            try {<!-- -->
                Object value1 = field.get(obj1);
                Object value2 = field.get(obj2);
                if (value1 == null &amp;&amp; value2 == null) {<!-- -->
                    continue;
                }
                if (value1 == null || value2 == null) {<!-- -->
                    return true;
                }
                if (!value1.equals(value2)) {<!-- -->
                    return true;
                }
            } catch (IllegalAccessException e) {<!-- -->
                e.printStackTrace();
            }
        }
        return false;
    }
	
	/**
     * 检查两个对象的属性是否相同（只校验需要验证的字段）
     */
    public static boolean checkNeedFieldEquals(Object obj1, Object obj2, Set&lt;String&gt; excludeFields) {<!-- -->
        if (obj1 == null || obj2 == null) {<!-- -->
            return false;
        }
        if (!obj1.getClass().equals(obj2.getClass())) {<!-- -->
            return false;
        }
        Field[] fields = obj1.getClass().getDeclaredFields();
        for (Field field : fields) {<!-- -->
            if (excludeFields != null &amp;&amp; (!CollectionUtils.isEmpty(excludeFields)) &amp;&amp; !excludeFields.contains(field.getName())) {<!-- -->
                continue;
            }
            field.setAccessible(true);
            try {<!-- -->
                Object value1 = field.get(obj1);
                Object value2 = field.get(obj2);
                if (value1 == null &amp;&amp; value2 == null) {<!-- -->
                    continue;
                }
                if (value1 == null || value2 == null) {<!-- -->
                    return true;
                }
                if (!value1.equals(value2)) {<!-- -->
                    return true;
                }
            } catch (IllegalAccessException e) {<!-- -->
                e.printStackTrace();
            }
        }
        return false;
    }

	/**
     * 存放Beancopier的MAp 拷贝使用
     */
    static final ConcurrentHashMap&lt;String, BeanCopier&gt; BEAN_COPIER_MAP = new ConcurrentHashMap&lt;&gt;();

    /**
     * 复制开始
     */
    public static &lt;T&gt; T copy(Object source, Class&lt;T&gt; target) {<!-- -->
        try {<!-- -->
            T instance = target.newInstance();
            copy(source, instance, null);
            return instance;
        } catch (InstantiationException | IllegalAccessException e) {<!-- -->
            throw new RuntimeException(e);
        }
    }

    /**
     * 创建复制：列表使用这个会性能更好。
     */
    public static void copy(Object source, Object target, Converter converter) {<!-- -->
        String key = genKey(source.getClass(), target.getClass());
        BeanCopier beanCopier;
        if (BEAN_COPIER_MAP.containsKey(key)) {<!-- -->
            beanCopier = BEAN_COPIER_MAP.get(key);
        } else {<!-- -->
            beanCopier = BeanCopier.create(source.getClass(), target.getClass(), false);
            BEAN_COPIER_MAP.put(key, beanCopier);
        }
        beanCopier.copy(source, target, converter);
    }

    /**
     * 生成key
     *
     * @param srcClazz 源文件的class
     * @param tgtClazz 目标文件的class
     * @return string
     */
    private static String genKey(Class&lt;?&gt; srcClazz, Class&lt;?&gt; tgtClazz) {<!-- -->
        return srcClazz.getName() + tgtClazz.getName();
    }

}



```
