
--- 
title:  mybatis-xml个人使用笔记 
tags: []
categories: [] 

---
### like 查询

```
SELECT  
*  
FROM  
user  
WHERE  
name like CONCAT('%',#{<!-- -->name},'%')

```

### in

```
&lt;foreach  item="item" collection="listTag" index="index"  open="(" separator="," close=")"&gt;

#{<!-- -->item}

&lt;/foreach&gt;

```

### if-else

>  
 其中choose为一个整体 when是if otherwise是else 


```
&lt;select id="selectSelective" resultMap="xxx" parameterType="xxx"&gt;
    select
    &lt;include refid="Base_Column_List"/&gt;
    from xxx
    where del_flag=0
    &lt;choose&gt;
        &lt;when test="xxx !=null and xxx != ''"&gt;
            and xxx like concat(concat('%', #{<!-- -->xxx}), '%')
        &lt;/when&gt;
        &lt;otherwise&gt;
            and xxx like '**%'
        &lt;/otherwise&gt;
    &lt;/choose&gt;
&lt;/select&gt;

```

### 插入语句并校验是否存在，存在就不执行的例子

>  
 数据存在就不插入 DUAL 是个零时表，临时储存数据 insert 默认不反悔id的，需要加上keyColumn=“id” keyProperty=“id” useGeneratedKeys=“true” 这几个参数 


```
&lt;insert id="saveCommentOnlyData" keyColumn="id" keyProperty="id" useGeneratedKeys="true"
            parameterType="shop.easysell.lib.facebook.domain.po.LiveComment"&gt;
        insert into l_live_comment (live_id, face_comment_id, from_customer_id, from_id, from_name, to_id, to_name,
                                    content, is_keyword, is_fans, error_msg_status, created)
        select #{<!-- -->liveComment.liveId}        as live_id,
               #{<!-- -->liveComment.faceCommentId} as face_comment_id,
               #{<!-- -->liveComment.fromCustomerId} as from_customer_id,
               #{<!-- -->liveComment.fromId}         as from_id,
               #{<!-- -->liveComment.fromName}      as from_name,
               #{<!-- -->liveComment.toId}          as to_id,
               #{<!-- -->liveComment.toName}        as to_name,
               #{<!-- -->liveComment.content}       as content,
               #{<!-- -->liveComment.isKeyword}     as is_keyword,
               #{<!-- -->liveComment.isFans}        as is_fans,
               #{<!-- -->liveComment.errorMsgStatus} as error_msg_status,
               #{<!-- -->liveComment.created}       as created
        from DUAL
        where not exists(select id
                         from l_live_comment
                         where live_id = #{<!-- -->liveComment.liveId} and face_comment_id = #{<!-- -->liveComment.faceCommentId})
    &lt;/insert&gt;

```

### 编写动态排序

>  
 由于业务之中，出现动态排序的需求，后端不需要平凡改动排序规则，需要前端判断传参 


**排序实体**

```
package com.ushangxie.cca.common.lib.domain.dto;

import io.swagger.annotations.ApiModelProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SortFieldDTO {<!-- -->

    @ApiModelProperty("字段")
    private String field;

    @ApiModelProperty("字段")
    private Boolean isAsc;

}


```

**传参对象**

```
package com.ushangxie.cca.lib.community.domain.req;

import com.ushangxie.cca.common.lib.domain.dto.SortFieldDTO;
import com.ushangxie.cca.common.lib.domain.dto.req.ApiPageReq;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;

import java.util.List;

@EqualsAndHashCode(callSuper = true)
@Data
@ApiModel("admin圈子分页-请求实体")
public class AdminPageCircleReq extends ApiPageReq {<!-- -->

    @ApiModelProperty(value = "关键字")
    private String keyword;

    @ApiModelProperty("排序: user_number（成员数量）,post_number（帖子数量）")
    private List&lt;SortFieldDTO&gt; sortFields;

}


```

**xml实体**

>  
 记住循环的不能使用#{},会报错（超出边界）。得用${}（预防sql注入，加入’'） 


```
&lt;select id="adminPage" resultType="com.ushangxie.cca.lib.community.domain.resp.AdminPageCircleResp"&gt;
        select c.id as id,
        c.`name` as `name`,
        c.created as created,
        c.create_id as create_id,
        c.create_name as create_name,
        cs.user_number as user_number,
        cs.post_number as post_number
        from cca_circle c
        left join cca_circle_statis cs on c.id = cs.circle_id
        order by
        &lt;choose&gt;
            &lt;when test="adminPageCircleReq.sortFields != null"&gt;
                &lt;foreach collection="adminPageCircleReq.sortFields" item="item" separator=","&gt;
                    '${<!-- -->item.field}'
                    &lt;choose&gt;
                        &lt;when test="item.isAsc == true"&gt;
                            asc
                        &lt;/when&gt;
                        &lt;otherwise&gt;
                            desc
                        &lt;/otherwise&gt;
                    &lt;/choose&gt;
                &lt;/foreach&gt;
            &lt;/when&gt;
            &lt;otherwise&gt;
                created desc
            &lt;/otherwise&gt;
        &lt;/choose&gt;
    &lt;/select&gt;

```

**运行效果**

```
2023-02-03 14:34:27.503 DEBUG 18964 --- [           main]  c.u.c.s.c.m.CcaCircleMapper.adminPage    : ==&gt;  Preparing: SELECT COUNT(1) FROM cca_circle c LEFT JOIN cca_circle_statis cs ON c.id = cs.circle_id 
2023-02-03 14:34:27.530 DEBUG 18964 --- [           main]  c.u.c.s.c.m.CcaCircleMapper.adminPage    : ==&gt; Parameters: 
2023-02-03 14:34:27.557 DEBUG 18964 --- [           main]  c.u.c.s.c.m.CcaCircleMapper.adminPage    : ==&gt;  Preparing: select c.id as id, c.`name` as `name`, c.created as created, c.create_id as create_id, c.create_name as create_name, cs.user_number as user_number, cs.post_number as post_number from cca_circle c left join cca_circle_statis cs on c.id = cs.circle_id order by created desc LIMIT ?,? 
2023-02-03 14:34:27.558 DEBUG 18964 --- [           main]  c.u.c.s.c.m.CcaCircleMapper.adminPage    : ==&gt; Parameters: 0(Long), 0(Long)
2023-02-03 14:34:27.564 DEBUG 18964 --- [           main]  c.u.c.s.c.m.CcaCircleMapper.adminPage    : &lt;==      Total: 0

```
