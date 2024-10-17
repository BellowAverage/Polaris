
--- 
title:  CompletableFuture的再次封装 
tags: []
categories: [] 

---
### CompletableFuture的再次封装

>  
 由于我们的业务会大量使用到重复性代码，所以封装了一个新工具类来，减少重复造轮子的问题 CompletableFuture没有全部重写，有需要自己重写封装 


```
package com.ljq.commons.utils;

import cn.hutool.core.map.MapUtil;
import cn.hutool.core.util.ObjUtil;
import cn.hutool.core.util.StrUtil;
import lombok.SneakyThrows;
import org.jetbrains.annotations.NotNull;

import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.function.Function;
import java.util.function.Supplier;

/**
 * CompletableFuture的工具类
 *
 * @author 刘俊秦
 * @date 2023/07/31
 */
public abstract class CompletableFutureUtil {<!-- -->

    private static CompletableFutureUtil createInstance() {<!-- -->
        return new CompletableFutureTaskUtil();
    }

    public static CompletableFutureUtil getInstance() {<!-- -->
        return createInstance();
    }

    private static CompletableFutureUtil createInstance(ExecutorService executorService) {<!-- -->
        return new CompletableFutureTaskUtil(executorService);
    }

    public static CompletableFutureUtil getInstance(ExecutorService executorService) {<!-- -->
        return createInstance(executorService);
    }

    public abstract &lt;U&gt; CompletableFuture&lt;U&gt; supplyAsync(Supplier&lt;U&gt; supplier);

    public abstract &lt;U&gt; CompletableFuture&lt;U&gt; supplyAsync(String key, Supplier&lt;U&gt; supplier);

    public abstract &lt;F, U&gt; CompletableFuture&lt;F&gt; thenApplyAsync(CompletableFuture&lt;U&gt; from, Function&lt;? super U, ? extends F&gt; function);

    public abstract &lt;F, U&gt; CompletableFuture&lt;F&gt; thenApplyAsync(String key, CompletableFuture&lt;U&gt; from, Function&lt;? super U, ? extends F&gt; function);

    public abstract void allOf();

    public abstract Object getMapValueByKey(String key);

    public abstract void shutdown();

}

class CompletableFutureTaskUtil extends CompletableFutureUtil {<!-- -->

    public ExecutorService executorService;

    public Map&lt;String, CompletableFuture&lt;?&gt;&gt; futureMap;

    public CompletableFutureTaskUtil() {<!-- -->
        //初始化futureMap
        generateFutureMap();
    }

    public CompletableFutureTaskUtil(ExecutorService executorService) {<!-- -->
        //赋值线程池
        if (ObjUtil.isNotNull(executorService)) {<!-- -->
            this.executorService = executorService;
        }
        //初始化futureMap
        generateFutureMap();
    }

    private void generateFutureMap() {<!-- -->
        this.futureMap = MapUtil.newHashMap();
    }

    public &lt;U&gt; CompletableFuture&lt;U&gt; supplyAsync(Supplier&lt;U&gt; supplier) {<!-- -->
        CompletableFuture&lt;U&gt; future = this.getCompletableFutureSupplyAsync(supplier);
        futureMap.put(UUID.randomUUID().toString(), future);
        return future;
    }

    public &lt;U&gt; CompletableFuture&lt;U&gt; supplyAsync(String key, Supplier&lt;U&gt; supplier) {<!-- -->
        CompletableFuture&lt;U&gt; future = this.getCompletableFutureSupplyAsync(supplier);
        futureMap.put(Optional.ofNullable(key).filter(StrUtil::isNotBlank).orElse(UUID.randomUUID().toString()), future);
        return future;
    }

    @Override
    public &lt;F, U&gt; CompletableFuture&lt;F&gt; thenApplyAsync(CompletableFuture&lt;U&gt; from, Function&lt;? super U, ? extends F&gt; function) {<!-- -->
        CompletableFuture&lt;F&gt; future = this.getCompletableFutureThenApplyAsync(from, function);
        futureMap.put(UUID.randomUUID().toString(), future);
        return future;
    }

    @Override
    public &lt;F, U&gt; CompletableFuture&lt;F&gt; thenApplyAsync(String key, CompletableFuture&lt;U&gt; from, Function&lt;? super U, ? extends F&gt; function) {<!-- -->
        CompletableFuture&lt;F&gt; future = this.getCompletableFutureThenApplyAsync(from, function);
        futureMap.put(Optional.ofNullable(key).filter(StrUtil::isNotBlank).orElse(UUID.randomUUID().toString()), future);
        return future;
    }

    @NotNull
    private &lt;U&gt; CompletableFuture&lt;U&gt; getCompletableFutureSupplyAsync(Supplier&lt;U&gt; supplier) {<!-- -->
        CompletableFuture&lt;U&gt; future;
        if (ObjUtil.isNotNull(this.executorService)) {<!-- -->
            future = CompletableFuture.supplyAsync(supplier, this.executorService);
        } else {<!-- -->
            future = CompletableFuture.supplyAsync(supplier);
        }
        return future;
    }

    @NotNull
    private &lt;F, U&gt; CompletableFuture&lt;F&gt; getCompletableFutureThenApplyAsync(CompletableFuture&lt;U&gt; from, Function&lt;? super U, ? extends F&gt; function) {<!-- -->
        CompletableFuture&lt;F&gt; future;
        if (ObjUtil.isNotNull(this.executorService)) {<!-- -->
            future = from.thenApplyAsync(function, this.executorService);
        } else {<!-- -->
            future = from.thenApplyAsync(function);
        }
        return future;
    }

    @SneakyThrows
    public void allOf() {<!-- -->
        CompletableFuture.allOf(this.futureMap.values().toArray(new CompletableFuture[0])).get();
    }

    @SneakyThrows
    @Override
    public Object getMapValueByKey(String key) {<!-- -->
        return this.futureMap.get(key).get();
    }

    @Override
    public void shutdown() {<!-- -->
        this.executorService = null;
        this.futureMap = null;
    }

}

```

>  
 使用效果 


```
CompletableFutureUtil completableFutureUtil = CompletableFutureUtil.getInstance(AsyncConfiguration.myExecutorService);
CompletableFuture&lt;List&lt;Long&gt;&gt; idListCompletableFuture = completableFutureUtil.supplyAsync(() -&gt; page.getRecords().stream().map(Entity::getId).collect(Collectors.toList()));
CompletableFuture&lt;List&lt;SaleOutboundItem&gt;&gt; itemCompletableFuture = completableFutureUtil.thenApplyAsync(idListCompletableFuture, saleOutboundItemService::getDataByOutboundIds);
CompletableFuture&lt;List&lt;Long&gt;&gt; itemIdsCompletableFuture = completableFutureUtil.thenApplyAsync(itemCompletableFuture, list -&gt; Optional.ofNullable(list).filter(CollUtil::isNotEmpty).map(m -&gt; m.stream().map(SaleOutboundItem::getId).collect(Collectors.toList())).orElse(null));
completableFutureUtil.thenApplyAsync(itemCompletableFuture, items -&gt; Optional.ofNullable(items).filter(CollUtil::isNotEmpty).map(m -&gt; m.stream().collect(Collectors.groupingBy(SaleOutboundItem::getOutboundId))).orElse(MapUtil.newHashMap()));
completableFutureUtil.thenApplyAsync("itemBoltMap", itemIdsCompletableFuture, itemIds -&gt; Optional.ofNullable(itemIds).filter(CollUtil::isNotEmpty).map(ids -&gt; Optional.ofNullable(saleOutboundItemBoltService.getDataByOutboundItemIds(ids)).filter(CollUtil::isNotEmpty).map(bolts -&gt; bolts.stream().collect(Collectors.groupingBy(SaleOutboundItemBolt::getOutboundItemId))).orElse(MapUtil.newHashMap())).orElse(MapUtil.newHashMap()));
completableFutureUtil.thenApplyAsync("itemWarehouseLocationMap", itemIdsCompletableFuture, itemIds -&gt; Optional.ofNullable(itemIds).filter(CollUtil::isNotEmpty).map(ids -&gt; Optional.ofNullable(saleOutboundItemWarehouseLocationService.getDataByOutboundItemIds(ids)).filter(CollUtil::isNotEmpty).map(bolts -&gt; bolts.stream().collect(Collectors.groupingBy(SaleOutboundItemWarehouseLocation::getOutboundItemId))).orElse(MapUtil.newHashMap())).orElse(MapUtil.newHashMap()));
completableFutureUtil.allOf();
Map&lt;Long, List&lt;SaleOutboundItem&gt;&gt; itemMap = (Map&lt;Long, List&lt;SaleOutboundItem&gt;&gt;) completableFutureUtil.getMapValueByKey("itemMap");
Map&lt;Long, List&lt;SaleOutboundItemBolt&gt;&gt; itemBoltMap = (Map&lt;Long, List&lt;SaleOutboundItemBolt&gt;&gt;) completableFutureUtil.getMapValueByKey("itemBoltMap");
Map&lt;Long, List&lt;SaleOutboundItemWarehouseLocation&gt;&gt; itemWarehouseLocationMap = (Map&lt;Long, List&lt;SaleOutboundItemWarehouseLocation&gt;&gt;) completableFutureUtil.getMapValueByKey("itemWarehouseLocationMap");
completableFutureUtil.shutdown();

```
