
--- 
title:  el-form的resetFields()不起作用没效果 
tags: []
categories: [] 

---
场景：新增与编辑共用一个组件，点击编辑弹框之后，关掉弹框，再点击新增，新增的时候先调用了resetFields方法，但是没有生效，弹框表单显示的还是编辑时候的数据

>  
 点击编辑的时候，一旦执行outerVisible = true， 就显示dialog，然后立马就执行给表单数据赋值的操作 此时数据修改了，但是dialog里面的el-form还没有mounted，也就是说，数据是在form表单mounted之前修改的，那么这个修改后的数据就成为了form表单的初始值。 而重点是，resetFields方法是用来把表单重置到初始值的，现在初始值都修改成回显数据了，再怎么调用resetFields都是徒劳 


##### 解决方法：

点击编辑后的赋值操作在this.$nextTick()中执行，也就是在dom渲染完之后再赋值

```
  @Watch('itemId', {<!-- --> immediate: true })
  private watchItemId(newVal: any) {<!-- -->
    console.log(this.itemId, this.itemData)
    this.$nextTick(() =&gt; {<!-- -->
      (this.$refs.dataForm as ElForm).resetFields()
      if (this.itemId) {<!-- -->
        this.dataForm.realName = this.itemData.username
      }
    })
  }

```

参考：
