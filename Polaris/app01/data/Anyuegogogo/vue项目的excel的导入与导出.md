
--- 
title:  vue项目的excel的导入与导出 
tags: []
categories: [] 

---
 

在做人力资源管理的后台项目时，实现了excel表的导入导出功能。用到了vue-element-admin提供的框架（ ），我们只需要在自己的项目中封装改造即可。

下面，来讲一下在项目中实现excel表的导入与导出的步骤。

### 一、excel的导入

#### 1.excel导入功能需要使用npm包**`xlsx`**，所以需要安装**`xlsx`**插件

```
npm i xlsx
```

#### 2.将vue-element-admin提供的导入功能新建一个公共组件 ，将组件引入到我们的页面中

（为了让我们的项目每次跳转都跳转到一个统一的页面，我们的项目中封装了单独的路由和页面组件@/views/import/index.vue来放excel导入）

注意：这个页面结构用到了element-ui框架，但是如果用的是其他框架只需要改页面结构，逻辑代码是通用的。

@/components/UploadExcel/index.vue

代码到链接中复制即可，要改动的只有页面结构和样式。（）

#### 3.实现excel的导入

在我们的import/index.vue组件中，传给UploadExcel/index.vue一个**onsuccess**方法，在这个方法里面我们可以拿到excel表的header表头和results表格数据。拿到这些数据就可以根据我们的业务需求来转换数据，来实现我们的业务需求逻辑代码。

拿到的数据大概是如下这种：

```
      // 拿到的数据是如下这种，我们要将它转化成我们请求接口中所需要的数据
      console.log(header)
      // ["手机号", "姓名", "入职日期", "转正日期", "工号", ...]
      console.log(results)
      // [{入职日期: 'xxx', 姓名: 'xxx', 工号: 'xxx', ...}, {入职日期: 'xxx', 姓名: 'xxx', 工号: 'xxx', ...}]
      // 我们需要的数据是如下这种
      // [{timeOfEntry: 'xxx', username: 'xxx', workNumber: 'xxx', ...}, {timeOfEntry: 'xxx', username: 'xxx', workNumber: 'xxx', ...}]
```

 下面附上整个代码：

```
&lt;template&gt;
  &lt;upload-excel :on-success="success" /&gt;
&lt;/template&gt;

&lt;script&gt;
// 导入封装的导入excel表组件
import UploadExcel from '@/components/UploadExcel/index'
import { importEmployee } from '@/api/employees'
export default {
  components: {
    UploadExcel
  },
  data() {
  },
  methods: {
    // 要使用这个组件，可以传入beforeUpload和onSuccess这两个函数
    // beforeUpload要注意要return一个布尔值
    // onSuccess这里面可以拿到表格的header(表头)和results(表格内容)
    // 在我们自己的onSuccess函数里，可以拼接出我们需要的结构的数据
    async success({ header, results }) {
      // 拿到的数据是如下这种，我们要将它转化成我们请求接口中所需要的数据
      console.log(header)
      // ["手机号", "姓名", "入职日期", "转正日期", "工号", ...]
      console.log(results)
      // [{入职日期: 'xxx', 姓名: 'xxx', 工号: 'xxx', ...}]

      // 1.定义我们需要的表头的映射关系（表头的字段其实就是我们接口中所需要的参数）
      const userRelations = {
        '入职日期': 'timeOfEntry',
        '手机号': 'mobile',
        '姓名': 'username',
        '转正日期': 'correctionTime',
        '工号': 'workNumber'
      }
      // 2.进行数据转换，实现业务需求
      var newArr = results.map(item =&gt; {
        const userInfo = {}
        Object.keys(item).forEach(k =&gt; {
          // key是当前的中文名 找到对应的英文名
          if (userRelations[k] === 'timeOfEntry' || userRelations[k] === 'correctionTime') {
            userInfo[userRelations[k]] = new Date(this.formatDate(item[k], '/')) // 只有这样, 才能入库
            return
          }
          userInfo[userRelations[k]] = item[k]
        })
        return userInfo
      })
      await importEmployee(newArr)
      this.$message.success('导入成功')
      this.$router.back() // 回到上一页
    },
    formatDate(numb, format) {
      const time = new Date((numb - 1) * 24 * 3600000 + 1)
      time.setYear(time.getFullYear() - 70)
      const year = time.getFullYear() + ''
      const month = time.getMonth() + 1 + ''
      const date = time.getDate() - 1 + ''
      if (format &amp;&amp; format.length === 1) {
        return year + format + month + format + date
      }
      return year + (month &lt; 10 ? '0' + month : month) + (date &lt; 10 ? '0' + date : date)
    }
  }
}
&lt;/script&gt;
```

### 二、excel的导出

#### 1.下载所需js文件

Excel 的导入导出都是依赖于来实现的。

在 `js-xlsx`的基础上又封装了来方便导出数据。所以我们可以先下载该js文件到我们的项目目录下（）

src/vendor/Export2Excel.js

#### 2.安装导出excel所需依赖

由于 `Export2Excel`不仅依赖`js-xlsx`还依赖`file-saver`和`script-loader，所以我们要再下载两个依赖包。`

```
npm install xlsx file-saver -S
npm install script-loader -S -D
```

#### 3.按需导入引用方法

由于下载的Export2Excel.js文件还挺大的，我们可以用按需导入的方法导入到我们的组件中。然后调用导入文件的导出对象上的方法，这个方法需要我们传入一些参数。

```
// 懒加载
import('@/vendor/Export2Excel').then(excel =&gt; {
  // excel是引入文件（也就是@/ventor/Export2Excel）的导出对象
  excel.export_json_to_excel({
    header: tHeader, // 表头 必填  []
    data, // 具体数据 必填  [[], [], ...]
    filename: 'excel-list', // 导出文件名 非必填 
    autoWidth: true, // 单元格是否要自适应宽度 非必填  true / false
    bookType: 'xlsx' // 导出文件类型 非必填  'xlsx'/'csv'/'txt'等
  })
})
```

在导出的函数我们，我们需要将我们项目中拿到的数据转化成参数所需要的数据格式

```
        // 拿到的数据是这种
        //  [{ username: 'xxx', mobile: 'xxx', ... }, { username: 'xxx', mobile: 'xxx', ... }]
        // 要转化的是如下这种
        // header: ['姓名', '手机号', '入职日期', ...]
        // data: [['张三', '138xxxxxxxx', '1992-08-04', ...], ['李四', '135xxxxxxxx', '1992-08-04', ...]]
```

下面附上整个代码

```
    // 导出数据
    exportData() {
      // 1.定义表头对应关系
      const headers = {
        '姓名': 'username',
        '手机号': 'mobile',
        '入职日期': 'timeOfEntry',
        '聘用形式': 'formOfEmployment',
        '转正日期': 'correctionTime',
        '工号': 'workNumber',
        '部门': 'departmentName'
      }
      // 懒加载
      import('@/vendor/Export2Excel').then(async excel =&gt; {
        // excel是引入文件（也就是@/ventor/Export2Excel）的导出对象
        // 获取所有的数据
        const { rows } = await getEmployeeList({ page: 1, size: this.page.total })
        const data = this.formatJson(headers, rows) // 返回的data就是我们转化后的数据
        excel.export_json_to_excel({
          // 要求转出的表头是中文
          header: Object.keys(headers), // 表头 必填
          data, // //具体数据 必填
          filename: 'excel-list', // 非必填
          autoWidth: true, // 非必填
          bookType: 'xlsx' // 非必填
        })
        // 拿到的数据是这种
        //  [{ username: 'xxx', mobile: 'xxx', ... }, { username: 'xxx', mobile: 'xxx', ... }]
        // 要转化的是如下这种
        // header: ['姓名', '手机号', '入职日期', ...]
        // data: [['张三', '138xxxxxxxx', '1992-08-04', ...], ['李四', '135xxxxxxxx', '1992-08-04', ...]]
      })
    },
    formatJson(headers, rows) {
      return rows.map(item =&gt; {
        console.log(item)
        return Object.keys(headers).map(k =&gt; {
          if (headers[k] === 'timeOfEntry' || headers[k] === 'correctionTime') {
            return formatDate(item[headers[k]]) // 返回格式化之前的时间
          } else if (headers[k] === 'formOfEmployment') {
            return EmployeeEnum.hireType[item.formOfEmployment] ? EmployeeEnum.hireType[item.formOfEmployment] : '未知'
          }
          return item[headers[k]]
        })
      })
    }
```

好啦，以上就是excel表导入导出的步骤啦，有不对的地方欢迎指正哦！~
