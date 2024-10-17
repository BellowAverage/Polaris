
--- 
title:  uview一些使用的记录 
tags: []
categories: [] 

---
### u-upload获取不到文件数据

**解决：u-upload结合uni.chooseImage使用** html

```
	&lt;view class="upload-container" @click="uploadImage"&gt;
		&lt;u-upload
			:fileList="fileList"
			@delete="deletePic"
			useBeforeRead
			name="1"
			:maxCount="1"
			accept="image"
			:capture="['album']"
			:previewFullImage="true"
			:disabled="true"
		&gt;
			&lt;image src="@/static/img/upload.png" style="width: 160rpx;height: 160rpx;"&gt;&lt;/image&gt;
		&lt;/u-upload&gt;
	&lt;/view&gt;

```

js

```
data() {<!-- -->
	return {<!-- -->
		fileList: [],
	}
},

methods: {<!-- -->
	deletePic(event) {<!-- -->
		this.fileList.splice(event.index, 1);
	},
	
	uploadImage() {<!-- -->
		if (this.fileList.length !== 0) {<!-- -->
			return false;
		}
		uni.chooseImage({<!-- -->
			count: 1,
			sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
			sourceType: ['album'], //从相册选择
			success: (res) =&gt; {<!-- -->
				console.log(res, res.tempFiles[0].path);
				this.fileList.push({<!-- -->
					url: res.tempFiles[0].path,
					file: res.tempFiles[0],
				});
			},
			fail: function(err) {<!-- -->
				console.log(err.errMsg);
				uni.$u.toast('上传失败');
			}
		});
	},
}


```

参考链接：

### u–form表单校验

问题：同步的校验不通过，最终的this. 
     
      
       
       
         r 
        
       
         e 
        
       
         f 
        
       
         s 
        
       
         . 
        
       
         u 
        
       
         F 
        
       
         o 
        
       
         r 
        
       
         m 
        
       
         . 
        
       
         v 
        
       
         a 
        
       
         l 
        
       
         i 
        
       
         d 
        
       
         a 
        
       
         t 
        
       
         e 
        
       
         ( 
        
       
         ) 
        
       
         不会通过；但异步校验的报异常不通过， 
        
       
         t 
        
       
         h 
        
       
         i 
        
       
         s 
        
       
         . 
        
       
      
        refs.uForm.validate()不会通过；但异步校验的报异常不通过，this. 
       
      
    refs.uForm.validate()不会通过；但异步校验的报异常不通过，this.refs.uForm.validate()会通过 解决：this.$refs.uForm.validate()终验之前自己再调用一次异步方法自己判断是否可以通过 下面贴上部分代码

```
	&lt;u--form
		labelPosition="top"
		:model="formData"
		:rules="rules"
		ref="uForm"
		labelWidth="auto"
	&gt;
		&lt;u-form-item label="真实姓名" prop="name" required&gt;
			&lt;u--input v-model="formData.name" placeholder="请输入真实姓名"&gt;&lt;/u--input&gt;
		&lt;/u-form-item&gt;

		&lt;u-form-item label="身份证号码" prop="lawyerId" required&gt;
			&lt;u--input v-model="formData.lawyerId" placeholder="请输入身份证号码"&gt;&lt;/u--input&gt;
		&lt;/u-form-item&gt;

		&lt;u-form-item label="律师证号码" prop="idCard" required&gt;
			&lt;u--input v-model="formData.idCard" placeholder="请输入律师证号码"&gt;&lt;/u--input&gt;
		&lt;/u-form-item&gt;

		&lt;u-form-item label="手机号码" prop="phone" required&gt;
			&lt;u--input v-model="formData.phone" placeholder="请输入手机号码"&gt;&lt;/u--input&gt;
		&lt;/u-form-item&gt;

		&lt;u-form-item label="律师执照"&gt;
			&lt;view class="upload-container" @click="uploadImage"&gt;
				&lt;u-upload
					:fileList="fileList"
					@delete="deletePic"
					useBeforeRead
					name="1"
					:maxCount="1"
					accept="image"
					:capture="['album']"
					:previewFullImage="true"
					:disabled="true"
				&gt;
					&lt;image src="@/static/img/upload.png" style="width: 160rpx;height: 160rpx;"&gt;&lt;/image&gt;
				&lt;/u-upload&gt;
			&lt;/view&gt;
		&lt;/u-form-item&gt;

		&lt;u-form-item label=""&gt;
			&lt;u-button @click="exchangeClick" color="linear-gradient(180deg, #45BCFF 0%, #5191F0 100%)" class="btn" :loading="btnLoading"&gt;点击兑换&lt;/u-button&gt;
		&lt;/u-form-item&gt;
	&lt;/u--form&gt;

```

```
	data() {<!-- -->
		return {<!-- -->
			btnLoading: false,
			formData: {<!-- -->
				name: '',
				idCard: '',
				phone: '',
				lawyerId: ''
			},
			fileList: [],
			rules: {<!-- -->
				name: [
					{<!-- -->
						required: true,
						message: '请输入姓名',
						trigger: ['blur']
					}
				],
				idCard: [
					{<!-- -->
						required: true,
						message: '请输入律师证号码',
						trigger: ['blur']
					}, 
					{<!-- -->
						type: 'number',
						max: 17,
						message: '请输入正确的律师证号码',
						trigger: ['blur']
					},
					{<!-- -->
						// validator: (rule, value, callback) =&gt; {<!-- -->
						// 	// 返回true表示校验通过，返回false表示不通过
						// 	// 律师证号，包括尾数为"X"的类型，可以校验通过，结果返回true或者false
						// 	return uni.$u.test.idCard(value);
						// },
						// validator: 
						asyncValidator: (rule, value, callback) =&gt; this.checkIdCard(rule, value, callback),
						trigger: ['blur']
					}
				],
				phone: [
					{<!-- -->
						required: true,
						message: '请输入手机号码',
						trigger: ['blur']
					}, 
					{<!-- -->
						message: '请输入正确的手机号码',
						validator: (rule, value, callback) =&gt; {<!-- -->
							// 返回true表示校验通过，返回false表示不通过
							// uni.$u.test.mobile()就是返回true或者false的
							return uni.$u.test.mobile(value);
						},
						trigger: ['blur']
					}
				],
				lawyerId: [
					{<!-- -->
						required: true,
						message: '请输入身份证号码',
						trigger: ['blur']
					},
					{<!-- -->
						max: 18,
						message: '请输入正确的身份证号码',
						trigger: ['blur']
					}, 
				],
			}
		};
	},
	methods: {<!-- -->
		checkIdCard(rule, value, callback) {<!-- -->
			if (!value) {<!-- -->
				callback(new Error('请输入律师证号码'));
				return;
			}
			uni.$u.http.post('/exchange/query/idCard', {<!-- -->
				idCard: this.formData.idCard
			}).then(res =&gt; {<!-- -->
				// tag:1 不存在 2 存在
				if (res.data &amp;&amp; res.data === []) {<!-- -->
					callback(new Error('请输入正确的律师证号码'));
					uni.showModal({<!-- -->
						title: '提示',
						content: '温馨提醒：您好，您输入的信息找不到积分记录，请确认您信息是否有误～'
					});
				}
				callback();
			}).catch((err) =&gt; {<!-- -->
				callback(new Error('律师证校验失败'));
			});
		},

		async queryStatus() {<!-- -->
			try {<!-- -->
				this.btnLoading = true;
				const res = await uni.$u.http.post('/exchange/query/status', {<!-- -->
					idCard: this.formData.idCard,
				}, {<!-- -->
					header: {<!-- -->
						'Content-Type': 'application/x-www-form-urlencoded'
					}
				});
				this.btnLoading = false;
				return res.data;
			} catch (error) {<!-- -->
				this.btnLoading = false;
			}
		},
		
		async exchangeClick() {<!-- -->
			if (this.formData.idCard) {<!-- -->
				try {<!-- -->
					const response = await uni.$u.http.post('/exchange/query/idCard', {<!-- -->
						idCard: this.formData.idCard
					});
					if (response.data &amp;&amp; response.data === []) {<!-- -->
						return;
					}
				} catch (error) {<!-- -->
					console.log(error);
					return;
				}
			}

			// const result = await this.queryStatus();
			// this.$refs.confirmPopup &amp;&amp; this.$refs.confirmPopup.open();
			this.$refs.uForm.validate().then(async (res) =&gt; {<!-- -->
				// if (this.fileList.length === 0) {<!-- -->
				// 	uni.$u.toast('请上传律师执照');
				// 	return;
				// }
				// console.log(666,res);
				uni.$u.http.post('/exchange/query/status', {<!-- -->
					idCard: this.formData.idCard,
				}, {<!-- -->
					header: {<!-- -->
						'Content-Type': 'application/x-www-form-urlencoded'
					}
				}).then(response =&gt; {<!-- -->
					// exchangeStatus：1 已兑换 2 未兑换
					if (response.data === null) {<!-- -->
						this.$refs.confirmPopup &amp;&amp; this.$refs.confirmPopup.open();
					} else if (response.data &amp;&amp; response.data.exchangeStatus &amp;&amp; response.data.exchangeStatus === 2) {<!-- -->
						this.$refs.confirmPopup &amp;&amp; this.$refs.confirmPopup.open();
					}else if (response.data &amp;&amp; response.data.exchangeStatus &amp;&amp; response.data.exchangeStatus === 1) {<!-- -->
						uni.showModal({<!-- -->
							title: '提示',
							content: '您的积分已登记兑换'
						});
					} else {<!-- -->
						uni.showModal({<!-- -->
							title: '提示',
							content: '其他'
						});
					}

				}); 
			}).catch(errors =&gt; {<!-- -->
				// uni.$u.toast('校验失败');
			});
		}
	}

```
