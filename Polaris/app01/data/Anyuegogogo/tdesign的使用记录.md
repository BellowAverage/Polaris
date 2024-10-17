
--- 
title:  tdesign的使用记录 
tags: []
categories: [] 

---
#### 1、复杂表单校验

复杂类型的数据（两级数组）

```
const dataForm = ref({<!-- -->
	configTalkTemplateProblemCoList: [
    {<!-- -->
        "id":"1744302859557920769",
        "templateId":"1744302859511783426",
        "parentId":null,
        "level":null,
        "deleted":"0",
        "createTime":"2024-01-08 18:19:44",
        "createUserId":"1001",
        "createUserName":"admin",
        "updateTime":"2024-01-08 18:19:44",
        "updateUserId":null,
        "updateUserName":null,
        "tenantId":null,
        "list":[
            {<!-- -->
                "id":"1744302859591475201",
                "templateId":"1744302859511783426",
                "parentId":"1744302859557920769",
                "problem":"问题1",
                "level":null,
                "deleted":"0",
                "createTime":"2024-01-08 18:19:44",
                "createUserId":"1001",
                "createUserName":"admin",
                "updateTime":"2024-01-08 18:19:44",
                "updateUserId":null,
                "updateUserName":null,
                "tenantId":null,
                "list":null
            },
            {<!-- -->
                "id":"1744302859620835330",
                "templateId":"1744302859511783426",
                "parentId":"1744302859557920769",
                "problem":"问题2",
                "level":null,
                "deleted":"0",
                "createTime":"2024-01-08 18:19:44",
                "createUserId":"1001",
                "createUserName":"admin",
                "updateTime":"2024-01-08 18:19:44",
                "updateUserId":null,
                "updateUserName":null,
                "tenantId":null,
                "list":null
            }
        ],
        "classify":"分类一"
    },
    {<!-- -->
        "id":"1744302859658584065",
        "templateId":"1744302859511783426",
        "parentId":null,
        "level":null,
        "deleted":"0",
        "createTime":"2024-01-08 18:19:44",
        "createUserId":"1001",
        "createUserName":"admin",
        "updateTime":"2024-01-08 18:19:44",
        "updateUserId":null,
        "updateUserName":null,
        "tenantId":null,
        "list":[
            {<!-- -->
                "id":"1744302859687944194",
                "templateId":"1744302859511783426",
                "parentId":"1744302859658584065",
                "problem":"问题1",
                "level":null,
                "deleted":"0",
                "createTime":"2024-01-08 18:19:44",
                "createUserId":"1001",
                "createUserName":"admin",
                "updateTime":"2024-01-08 18:19:44",
                "updateUserId":null,
                "updateUserName":null,
                "tenantId":null,
                "list":null
            },
            {<!-- -->
                "id":"1744302859755053057",
                "templateId":"1744302859511783426",
                "parentId":"1744302859658584065",
                "problem":"问题2",
                "level":null,
                "deleted":"0",
                "createTime":"2024-01-08 18:19:44",
                "createUserId":"1001",
                "createUserName":"admin",
                "updateTime":"2024-01-08 18:19:44",
                "updateUserId":null,
                "updateUserName":null,
                "tenantId":null,
                "list":null
            }
        ],
        "classify":"分类2"
    }
]
}) 

```

表单写法

```
    &lt;t-form
		ref="formRef"
		:data="dataForm"
		:rules="dataRules"
		label-width="100px"
		label-align="right"
		reset-type="initial"
		@submit="onSubmit"
	&gt;
        &lt;div class="question" v-for="(item, index) in dataForm.configTalkTemplateProblemCoList" :key="item.id" :label-width="0"&gt;
          &lt;div class="content br12"&gt;
            &lt;t-form-item label="问题分类" :name="`configTalkTemplateProblemCoList[${index}].classify`" requiredMark&gt;
              &lt;t-input v-model="item.classify" placeholder="请输入问题分类" style="width: 400px" :readonly="props.isView"&gt;&lt;/t-input&gt;
            &lt;/t-form-item&gt;
            &lt;t-form-item v-for="(v, i) in item.list" :key="v.id" label="问题" :name="`configTalkTemplateProblemCoList[${index}].list[${i}].problem`" requiredMark&gt;
              &lt;t-textarea v-model="v.problem" placeholder="请输入问题" style="width: 400px" :readonly="props.isView"&gt;&lt;/t-textarea&gt;

            &lt;/t-form-item&gt;
          &lt;/div&gt;
        &lt;/div&gt;
&lt;/t-form&gt;


```

表单校验

```
const dataRules = {<!-- -->
  classify: [{<!-- --> required: true, message: '请输入问题分类', type: 'error', trigger: 'blur' }],
  problem: [{<!-- --> required: true, message: '请输入问题', type: 'error', trigger: 'blur' }],
};


```

**注意：重点就是name属性必须是你的数据的属性开头，如configTalkTemplateProblemCoList，如果不用configTalkTemplateProblemCoList，直接用item或者v，是不行的。**
