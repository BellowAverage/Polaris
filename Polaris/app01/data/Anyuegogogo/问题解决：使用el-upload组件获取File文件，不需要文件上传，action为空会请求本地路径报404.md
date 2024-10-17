
--- 
title:  问题解决：使用el-upload组件获取File文件，不需要文件上传，action为空会请求本地路径报404 
tags: []
categories: [] 

---
可以自定义上传方法、覆盖默认的上传行为 主要是这个属性 `:http-request="uploadFn"`

```
&lt;template&gt;
  &lt;span&gt;
    &lt;el-upload
      action="#"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :before-remove="beforeRemove"
      :on-success="handleSuccess"
      :limit="limit"
      :http-request="uploadFn"
      :on-exceed="handleExceed"
      :file-list="fileList"
			:on-change="hanldeChange"
			:accept="accept"&gt;
      &lt;el-button size="small" type="primary"&gt;点击上传&lt;/el-button&gt;
      &lt;div slot="tip" class="el-upload__tip"&gt;{<!-- -->{<!-- --> tipText }}&lt;/div&gt;
    &lt;/el-upload&gt;
  &lt;/span&gt;
&lt;/template&gt;

&lt;script&gt;

export default {<!-- -->
	props: {<!-- -->
		fileList: {<!-- -->
			type: Array,
			default: () =&gt; {<!-- -->}
		},
		limit: {<!-- -->
			type: Number,
			default: 1
		},
		tipText: {<!-- -->
			type: String,
			default: '请上传文件'
		},
		accept: {<!-- -->
			type: String,
			default: ''
		}
	},
	data() {<!-- -->
		return {<!-- -->
			// fileList: []
		};
	},
	methods: {<!-- -->
		uploadFn() {<!-- -->},
		
		hanldeChange(file) {<!-- -->
			//新增筛选代码
			this.fileList.push(file);
			if (file.status !== 'ready') return;
			this.$emit('fileSelect', file);
		},

		handleSuccess(file) {<!-- -->
			this.$emit('success', file);
		},

		handleRemove(file, fileList) {<!-- -->
			this.$emit('remove', fileList)
		},

		handlePreview(file) {<!-- -->
			console.log(file);
		},

		handleExceed(files, fileList) {<!-- -->
			this.$message.warning(`当前限制最多可选择 ${<!-- -->this.limit} 个文件`);
		},

		beforeRemove(file, fileList) {<!-- -->
			return this.$confirm(`确定移除 ${<!-- --> file.name }？`);
		}
	}
};
&lt;/script&gt;

&lt;style lang="scss" scoped&gt;

&lt;/style&gt;


```
