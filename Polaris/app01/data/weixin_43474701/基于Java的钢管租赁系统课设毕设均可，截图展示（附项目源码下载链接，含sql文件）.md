
--- 
title:  基于Java的钢管租赁系统课设毕设均可，截图展示（附项目源码下载链接，含sql文件） 
tags: []
categories: [] 

---
### 基于Java的钢管租赁系统

 **项目基本信息** 项目：基于Java的钢管租赁系统 **开发运行环境** JDK：1.8.0_144 IDE：Intellij IDEA 2019.3.3 数据库：MySQL Community Server 8.0.15 服务器：Tomcat 7 浏览器：Google Chrome 81 **启动步骤**
1.  将项目克隆到本地 <li> idea打开项目 <img src="https://img-blog.csdnimg.cn/direct/cab549f00b49428081efc0ff0b09e9d4.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/711a24dc54e0406690f36236425db5d1.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/e4fdedb6d80b4bd4936e6af4e5d94734.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b57c0519192e42e8b64c2af74a4a4a92.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/c2e13925f2194421b77e84dd79b57cc4.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/85d9f9cc3bd347dc95e22d602e585a7b.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/e36c4782298142cbb7fdc72e913febf0.png" alt="请添加图片描述"> **部分代码展示：** /** 
  1.  @param page 1.  @param limit 1.  @param orderSearch 查询参数 1.  @return */ @RequestMapping(“/list-order.do”) @ResponseBody public String doListOrders(Integer page, Integer limit, OrderSearch orderSearch) {<!-- --> // Log.log(“AdminController 类 doListOrders 方法”, “获取订单信息”); // Log.log(orderSearch.toString()); // Log.log(“page”, page); // Log.log(“limit”, limit); // Log.log(“待查询的材料”, order.toString()); // 按照创建时间降序排序 List allOrders = orderService.selectFuzzyOrderByDateDesc(orderSearch); // Log.log(“查询到的订单”); // for (Order o : allOrders) {<!-- --> // Log.log(o.toString()); // } // Log.logLn(); int fromIndex = (page - 1) * limit; int toIndex = Math.min(fromIndex + limit, allOrders.size()); List currentPageOrders = allOrders.subList(fromIndex, toIndex); // Log.log(“第” + page + “页的” + limit + “个订单是”); // for (Order o : currentPageOrders) {<!-- --> // Log.log(o.toString()); // } // Log.logLn(); JSONObject jsonObject = new JSONObject(); jsonObject.put(“code”, 0); jsonObject.put(“msg”, “订单信息”); jsonObject.put(“data”, currentPageOrders); jsonObject.put(“count”, allOrders.size()); // Log.log(“返回给前端的数据是”, jsonObject.toString()); return jsonObject.toString(); }  @RequestMapping(“/add-order.do”) @ResponseBody public Message doAddOrder(Order order) {<!-- --> // Log.log(“OrderController.doAddOrder”); // Log.log(order.toString()); <pre><code> Message message = new Message();

 List&lt;OrderDetail&gt; orderDetails = order.getOrderDetails();
 // Log.log(orderDetails.toString());

 if (order.getType().equals("租")) {
     // 减少库存量
     message = materialService.reduceStocks(orderDetails);
     // Log.log(message.toString());
 } else if (order.getType().equals("还")) {
     message = materialService.increaseStocks(orderDetails);
 }

 if (message.getMsgCode() == Message.SF_FAILURE) {
     return message;
 }

 // 成功减少库存量，接下来保存订单信息
 int count = orderService.insert(order);
 if (count == 0) {
     message.setMsg("订单添加失败！");
     if (order.getType().equals("租")) {
         materialService.increaseStocks(orderDetails);
     } else if (order.getType().equals("还")) {
         materialService.reduceStocks(orderDetails);
     }
     // Log.log(message.toString());
     return message;
 }

 // 添加订单明细到数据库
 Message orderDetailMessage = orderDetailService.insert(orderDetails);
 if (orderDetailMessage.getMsgCode() == Message.SF_FAILURE) {
     return orderDetailMessage;
 }

 message.setMsg("订单添加成功！");
 message.setMsgCode(Message.SF_SUCCESS);
 // Log.log("返回值", message.toString());
 return message;
</code></pre> } @RequestMapping(“/delete.do”) @ResponseBody public Message doDeleteOrder(Order order) {<!-- --> // Log.log(“OrderController.doDeleteOrder”); // Log.log(order.toString()); <pre><code> Message message = new Message();
 int count = 0;

 if (order == null) {
     message.setMsg("参数错误！");
     return message;
 }

 // 更新库存
 if (order.getType().equals("租")) {
     message = materialService.increaseStocks(order.getOrderDetails());
 } else if (order.getType().equals("还")) {
     message.setMsgCode(Message.SF_SUCCESS);
     message.setMsg("库存更新成功");
 }
 if (message.getMsgCode() == Message.SF_FAILURE) {
     return message;
 }

 count = orderDetailService.deleteLogicallyByOrderID(order.getId());
 if (count &lt; order.getOrderDetails().size()) {
     message.setMsg("订单明细删除失败！");
     return message;
 }

 count = orderService.delete(order);
 if (count == 1) {
     message.setMsgCode(Message.SF_SUCCESS);
     message.setMsg("订单删除成功！");
 } else {
     message.setMsg("订单删除失败！");
 }

 return message;
</code></pre> } </li>
}


