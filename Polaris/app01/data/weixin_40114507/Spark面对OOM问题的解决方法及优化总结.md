
--- 
title:  Spark面对OOM问题的解决方法及优化总结 
tags: []
categories: [] 

---


#### Spark面对OOM问题的解决方法及优化总结 
- - <ul><li>- - 


## out of memory
- map执行中内存溢出- shuffle后内存溢出
map执行中内存溢出代表了所有map类型的操作，包括：flatMap，filter，mapPatitions等。shuffle后内存溢出的shuffle操作包括join，reduceByKey，repartition等操作。

### 1. map过程产生大量对象导致内存溢出：

这种溢出的原因是在单个map中产生了大量的对象导致的，例如：rdd.map(x=&gt;for(i &lt;- 1 to 10000) yield i.toString)，这个操作在rdd中，每个对象都产生了10000个对象，这肯定很容易产生内存溢出的问题。针对这种问题，在不增加内存的情况下，可以通过减少每个Task的大小，以便达到每个Task即使产生大量的对象Executor的内存也能够装得下。具体做法可以在会产生大量对象的map操作之前调用repartition方法，分区成更小的块传入map。例如：rdd.repartition(10000).map(x=&gt;for(i &lt;- 1 to 10000) yield i.toString)。 面对这种问题注意，不能使用rdd.coalesce方法，这个方法只能减少分区，不能增加分区，不会有shuffle的过程。

### 2.数据不平衡导致内存溢出：

数据不平衡除了有可能导致内存溢出外，也有可能导致性能的问题，解决方法和上面说的类似，就是调用repartition重新分区。这里就不再累赘了。

### 3.coalesce调用导致内存溢出：

这是我最近才遇到的一个问题，因为hdfs中不适合存小问题，所以Spark计算后如果产生的文件太小，我们会调用coalesce合并文件再存入hdfs中。但是这会导致一个问题，例如在coalesce之前有100个文件，这也意味着能够有100个Task，现在调用coalesce(10)，最后只产生10个文件，因为coalesce并不是shuffle操作，这意味着coalesce并不是按照我原本想的那样先执行100个Task，再将Task的执行结果合并成10个，而是从头到位只有10个Task在执行，原本100个文件是分开执行的，现在每个Task同时一次读取10个文件，使用的内存是原来的10倍，这导致了OOM。解决这个问题的方法是令程序按照我们想的先执行100个Task再将结果合并成10个文件，这个问题同样可以通过repartition解决，调用repartition(10)，因为这就有一个shuffle的过程，shuffle前后是两个Stage，一个100个分区，一个是10个分区，就能按照我们的想法执行。
