
--- 
title:  hashCode equals 在集合添加时的区别 
tags: []
categories: [] 

---
参考 ，整理了一下，方便以后查看

### hashCode equals 在集合添加时的区别

假设我在集合添加的时候，规定相同的内容就不要重复添加了：
1. 重写了 equals 集合添加的时候，当只重写equals而没有重写 hashCode时，则会出现重复的内容依然会添加到集合中。这是因为添加判断的时候，先调用 hashCode(),再调用 equals来进行判断的
```

import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;

/**
 *  集合添加对象时  先调用 hashCode(),再调用 equals
 *  当对象的内容相同时，此时仍然会添加到集合中，就会出现重复数据
 */
public class HashCodeTest {<!-- -->
    public static void main(String[] args) {<!-- -->
        Collection set = new HashSet();
        Point p1 = new Point(1, 1);
        Point p2 = new Point(1, 1);

        System.out.println(p1.equals(p2));
        set.add(p1); // (1)
        set.add(p2); // (2)
        set.add(p1); // (3)

        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {<!-- -->
            Object object = iterator.next();
            System.out.println(object);
        }
    }
}

class Point {<!-- -->
    private int x;
    private int y;

    public Point(int x, int y) {<!-- -->
        super();
        this.x = x;
        this.y = y;
    }

    /**
     *  在比较的时候，重写 equals 方法
     * @param obj
     * @return
     */
    @Override
    public boolean equals(Object obj) {<!-- -->
        if (this == obj) {<!-- -->
            return true;
        }
        if (obj == null) {<!-- -->
            return false;
        }
        if (getClass() != obj.getClass()) {<!-- -->
            return false;
        }
        Point other = (Point) obj;
        if (x != other.x) {<!-- -->
            return false;
        }
        if (y != other.y) {<!-- -->
            return false;
        }
        return true;
    }

    @Override
    public String toString() {<!-- -->
        return "x:" + x + ",y:" + y;
    }

}

```
1. 重写了 hashCode 集合添加的时候，当只重写hashCode 而没有重写 equals时，则会出现重复的内容依然会添加到集合中。这是因为添加判断的时候，先调用 hashCode(),再调用 equals来进行判断的
```

import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;


/**
 *  集合添加对象时  先调用 hashCode(),再调用 equals
 */
public class HashCodeTest {<!-- -->
    public static void main(String[] args) {<!-- -->
        Collection set = new HashSet();
        Point p1 = new Point(1, 1);
        Point p2 = new Point(1, 1);

        System.out.println(p1.equals(p2));
        set.add(p1); // (1)
        set.add(p2); // (2)
        set.add(p1); // (3)

        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {<!-- -->
            Object object = iterator.next();
            System.out.println(object);
        }
    }
}

class Point {<!-- -->
    private int x;
    private int y;

    public Point(int x, int y) {<!-- -->
        super();
        this.x = x;
        this.y = y;
    }

    @Override
    public int hashCode() {<!-- -->
        final int prime = 31;
        int result = 1;
        result = prime * result + x;
        result = prime * result + y;
        return result;
    }

    @Override
    public String toString() {<!-- -->
        return "x:" + x + ",y:" + y;
    }

}

```
1. 用时重写了 hashCode equals,当插入内容相同的数据时， 则会抛弃这个对象，不再添加到集合中， 在HashSet中插入同一个元素（hashCode和equals均相等）时，保证了数据的唯一性
```

import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;


/**
 *  用时重写了  hashCode  equals,当插入内容相同的数据时， 则会抛弃这个对象，不再添加到集合中
 *  在HashSet中插入同一个元素（hashCode和equals均相等）时，保证了数据的唯一性
 */
public class HashCodeTest {<!-- -->
    public static void main(String[] args) {<!-- -->
        Collection set = new HashSet();
        Point p1 = new Point(1, 1);
        Point p2 = new Point(1, 1);
        Point p3 = new Point(1, 2);

        set.add(p1);
        set.add(p2);
        set.add(p3);
        set.add(p1);

//        p2.setX(10);
//        p2.setY(10);
//
//        set.remove(p2);
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {<!-- -->
            Object object = iterator.next();
            System.out.println(object);
        }
    }
}

class Point {<!-- -->
    private int x;
    private int y;

    public Point(int x, int y) {<!-- -->
        super();
        this.x = x;
        this.y = y;
    }

    public int getX() {<!-- -->
        return x;
    }

    public void setX(int x) {<!-- -->
        this.x = x;
    }

    public int getY() {<!-- -->
        return y;
    }

    public void setY(int y) {<!-- -->
        this.y = y;
    }

    @Override
    public int hashCode() {<!-- -->
        final int prime = 31;
        int result = 1;
        result = prime * result + x;
        result = prime * result + y;
        return result;
    }

    @Override
    public boolean equals(Object obj) {<!-- -->
        if (this == obj) {<!-- -->
            return true;
        }
        if (obj == null) {<!-- -->
            return false;
        }
        if (getClass() != obj.getClass()) {<!-- -->
            return false;
        }
        Point other = (Point) obj;
        if (x != other.x) {<!-- -->
            return false;
        }
        if (y != other.y) {<!-- -->
            return false;
        }
        return true;
    }

    @Override
    public String toString() {<!-- -->
        return "x:" + x + ",y:" + y;
    }

}

```
1. 添加数据后，当修改了 hashcode 值后，在查找时，hashCode值就不一样了这时查找结果空，jdk认为该对象不在集合中，所以不会进行删除操作。 然而用户以为该对象已经被删除，导致该对象长时间不能被释放，造成内存泄露。 解决该问题的办法是不要在执行期间修改与hashCode值有关的对象信息，如果非要修改，则必须先从集合中删除，更新信息后再加入集合中。
```

import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;


/**
 *  添加数据后，当修改了 hashcode 值后，在查找时，hashCode值就不一样了这时查找结果空，jdk认为该对象不在集合中，所以不会进行删除操作。
 *  然而用户以为该对象已经被删除，导致该对象长时间不能被释放，造成内存泄露。
 *  解决该问题的办法是不要在执行期间修改与hashCode值有关的对象信息，如果非要修改，则必须先从集合中删除，更新信息后再加入集合中。
 */
public class HashCodeTest {<!-- -->
    public static void main(String[] args) {<!-- -->
        Collection set = new HashSet();
        Point p1 = new Point(1, 1);
        Point p2 = new Point(1, 2);

        set.add(p1);
        set.add(p2);
        set.add(p1);

//        p2.setX(10);
//        p2.setY(10);
//        set.remove(p2);

        /**
         * 先从集合中删除，更新信息后再加入集合中,这种方式则不会出现内存泄露的问题
         */
        set.remove(p2);
        p2.setX(10);
        p2.setY(10);

        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {<!-- -->
            Object object = iterator.next();
            System.out.println(object);
        }
    }
}

class Point {<!-- -->
    private int x;
    private int y;

    public Point(int x, int y) {<!-- -->
        super();
        this.x = x;
        this.y = y;
    }

    public int getX() {<!-- -->
        return x;
    }

    public void setX(int x) {<!-- -->
        this.x = x;
    }

    public int getY() {<!-- -->
        return y;
    }

    public void setY(int y) {<!-- -->
        this.y = y;
    }

    @Override
    public int hashCode() {<!-- -->
        final int prime = 31;
        int result = 1;
        result = prime * result + x;
        result = prime * result + y;
        return result;
    }

    @Override
    public boolean equals(Object obj) {<!-- -->
        if (this == obj) {<!-- -->
            return true;
        }
        if (obj == null) {<!-- -->
            return false;
        }
        if (getClass() != obj.getClass()) {<!-- -->
            return false;
        }
        Point other = (Point) obj;
        if (x != other.x) {<!-- -->
            return false;
        }
        if (y != other.y) {<!-- -->
            return false;
        }
        return true;
    }

    @Override
    public String toString() {<!-- -->
        return "x:" + x + ",y:" + y;
    }

}

```
