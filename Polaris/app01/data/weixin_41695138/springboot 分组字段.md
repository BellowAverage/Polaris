
--- 
title:  springboot 分组字段 
tags: []
categories: [] 

---
springboot 分组字段：想实现在新增和更新的时候，不同的字段进行不同的校验 参考，结合自己的实际情况，先整理一下，方便自己日后的学习，感谢博主的分享。
1. 定义一个校验组类，声明四个接口对应不同场景校验
```

/**
 *  校验组类
 */
public class ValidationGroups {<!-- -->
    public interface Update {<!-- -->
    }

    public interface Insert {<!-- -->
    }

    public interface Detail {<!-- -->
    }


    public interface Delete{<!-- -->

    }
}

```
1. 在实体类具体属性添加校验规则及校验分组
```

import com.csjbot.platform.common.entity.BaseEntity;
import com.csjbot.platform.common.valid.ValidationGroups;
import io.swagger.annotations.ApiModelProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import javax.persistence.Table;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;


@AllArgsConstructor
@NoArgsConstructor
@Data
@Table(name="robot_banner")
public class RobotBannerEntity extends BaseEntity&lt;Long&gt;  {<!-- -->
	private static final long serialVersionUID = 1L;

    //所属数据字典的类型
    @NotNull(message = "所属数据字典的类型不能为空")
    @ApiModelProperty(value = "所属数据字典的类型", required = true)
    private Long sysDictionaryId;

    //图片的地址
    @NotNull(message = "图片的地址不能为空",groups ={<!-- -->ValidationGroups.Insert.class})
    @ApiModelProperty(value = "图片的地址", required = true)
    private String imgUrl;

    //宣传文字
    @NotNull(message = "宣传文字不能为空",groups ={<!-- -->ValidationGroups.Update.class})
    @ApiModelProperty(value = "宣传文字", required = true)
    private String propaganda;

    //要跳转的链接
    @NotEmpty(message = "要跳转的链接不能为空")
    @ApiModelProperty(value = "要跳转的链接", required = true)
    private String jumpUrl;

    //备注
    @ApiModelProperty(value = "备注", required = true)
    private String remark;

}


```

<img src="https://img-blog.csdnimg.cn/eacbe965eea7438dac18279b8fec2f04.png" alt="在这里插入图片描述"> 3. 在控制层@Validated注解后添加具体校验的分组名

```
	/**
	 * 新增记录
	 * @param entity RobotBannerEntity
	 * @return R
	 */
	//@SysLog("新增机器人Banner")
    @ApiOperation(value = "新增一条数据", notes = "新增一条数据")
	@RequestMapping(value = "/save", method = RequestMethod.POST)
	public R save(@RequestBody @Validated(ValidationGroups.Insert.class) RobotBannerEntity entity, BindingResult bindingResult) {<!-- -->
        if (bindingResult.hasErrors()) {<!-- -->
            return R.error(bindingResult.getFieldError().getDefaultMessage());
        }
        R save = this.robotBannerService.save(entity);
        return save;
	}

	/**
	 * 更新记录
	 * @param entity RobotBannerEntity
	 * @return R
	 */
	//@SysLog("修改机器人Banner")
	@RequestMapping(value = "/update",method = RequestMethod.POST)
	public R update(@RequestBody @Validated(ValidationGroups.Update.class) RobotBannerEntity entity, BindingResult bindingResult) {<!-- -->
        if (bindingResult.hasErrors()) {<!-- -->
            return R.error(bindingResult.getFieldError().getDefaultMessage());
        }
		return this.robotBannerService.update(entity);
	}

```
1. 测试新增： <img src="https://img-blog.csdnimg.cn/4e7d9939bc8f4ca5adf4bd46f4c2a543.png" alt="在这里插入图片描述"> 没有imgUrl字段则提示不能为空 <img src="https://img-blog.csdnimg.cn/266747e2fe754f42bd46705a1251ec47.png" alt="在这里插入图片描述"> 带上imgUrl字段，则响应操作成功1. 测试更新 <img src="https://img-blog.csdnimg.cn/6a4d89c6d3f5464ca6384e76b9f5f0f7.png" alt="在这里插入图片描述">
没有propaganda字段则提示不能为空 <img src="https://img-blog.csdnimg.cn/90cc73be86f34737a7ebeadb027e8535.png" alt="在这里插入图片描述">带上propagand字段，则响应操作成功
