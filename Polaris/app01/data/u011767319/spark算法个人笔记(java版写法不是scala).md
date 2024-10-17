
--- 
title:  spark算法个人笔记(java版写法不是scala) 
tags: []
categories: [] 

---
### 测试使用的协同过滤使用的算法

>  
 注意.sort方法 .subList方法 都会是集合**序列化**失败。没有序列化 spark 做不了计算 要解决可以用本人的方法。或者去我的另外一篇文章查看： 


```
package com.hgj.recommend;

import com.alibaba.fastjson.JSON;
import com.hgj.common.util.LogPrintUtil;
import com.hgj.recommend.pojo.vo.MovieScore;
import com.hgj.recommend.pojo.vo.UserRecs;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.mllib.recommendation.ALS;
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel;
import org.apache.spark.mllib.recommendation.Rating;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import scala.Tuple2;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;


@SpringBootTest
class RecommendApplicationTests {<!-- -->

    @Resource
    private JavaSparkContext sc;

    @Test
    void contextLoads() {<!-- -->

        List&lt;Rating&gt; ratingList = new ArrayList&lt;&gt;();
        for (int i = 0; i &lt; 200; i++) {<!-- -->
            ratingList.add(new Rating(i, 10 + i, i));
        }

        JavaRDD&lt;Rating&gt; parallelize = sc.parallelize(ratingList);

        JavaRDD&lt;Integer&gt; uidList = sc.parallelize(ratingList.stream().map(Rating::user).collect(Collectors.toList()));
        JavaRDD&lt;Integer&gt; midList = sc.parallelize(ratingList.stream().map(Rating::product).collect(Collectors.toList()));

        int rank = 50;
        int iterations = 5;
        double lambda = 0.01;

        MatrixFactorizationModel train = ALS.train(parallelize.rdd(), rank, iterations, lambda);

        //制作笛卡尔积 用户-物品
        JavaPairRDD&lt;Integer, Integer&gt; cartesian = uidList.cartesian(midList);

        //根据协同过滤筛选出全部的数据
        JavaRDD&lt;Rating&gt; predict = train.predict(cartesian);

        List&lt;UserRecs&gt; collect = predict
                .filter(rating -&gt; rating.rating() &gt; 0)
                .mapToPair(rating -&gt; new Tuple2&lt;Integer, Tuple2&lt;Integer, Double&gt;&gt;(
                                rating.user(),
                                new Tuple2&lt;Integer, Double&gt;(
                                        rating.product(),
                                        rating.rating())
                        )
                )
                .groupByKey()
                .map(res -&gt; {<!-- -->
                    UserRecs userRecs = new UserRecs();
                    userRecs.setUid(res._1);
                    List&lt;MovieScore&gt; movieScores = new ArrayList&lt;&gt;();
                    for (Tuple2&lt;Integer, Double&gt; next : res._2) {<!-- -->
                        MovieScore movieScore = new MovieScore();
                        movieScore.setMid(next._1);
                        movieScore.setRating(next._2);
                        movieScores.add(movieScore);
                    }
                    
                    movieScores.sort((o1, o2) -&gt; -(o1.getRating().intValue() - o2.getRating().intValue()));

                    if (movieScores.size() &gt; 100) {<!-- -->
                        movieScores = movieScores.subList(0, 5);
                    }

					//大家肯定好奇为什么 我还要用JSON转一下数据。原因：.sort方法 .subList方法 都会是集合序列化失败。没有序列化 spark 做不了计算
                    userRecs.setMovieScores(
                            JSON.parseArray(
                                    JSON.toJSONString(movieScores),
                                    MovieScore.class
                            )
                    );
                    return userRecs;
                })
                .collect();
        LogPrintUtil.logRes(JSON.toJSONString(collect));
    }

}


```
