
--- 
title:  easyexcel的使用-个人笔记 
tags: []
categories: [] 

---
### 简单导出功能

>  
 数据封装格式 


```
public List&lt;List&lt;Object&gt;&gt; trendExcel(AdminCrystalTrendReq adminCrystalTrendReq) {<!-- -->
        CrystalTrendReq crystalTrendReq = new CrystalTrendReq();
        BeanUtils.copyProperties(adminCrystalTrendReq, crystalTrendReq);
        crystalTrendReq.setIsAsc(false);
        List&lt;CrystalTResp&gt; crystalTResps = crystalDataApiService.trendExcel(crystalTrendReq);
        return Optional
                .ofNullable(crystalTResps)
                .orElse(Collections.emptyList())
                .stream()
                .map(d -&gt; {<!-- -->
                    List&lt;Object&gt; res = new ArrayList&lt;&gt;();
                    res.add(d.getStatDate());
                    res.add(d.getGetCrystalTotal());
                    res.add(d.getGiveCrystalTotal());
                    res.add(d.getExpendCrystalTotal());
                    res.add(d.getPlatLaveCrystalTotal());
                    return res;
                }).collect(Collectors.toList());
    }

```

>  
 代码具体导出操作 


```
/**
     * 水晶数据-趋势分析数据导出接口
     *
     * @param adminCrystalTrendReq 管理水晶趋势要求
     * @param httpServletResponse  http servlet响应
     */
    @PostMapping("/trend/excel")
    @Permission(value = "data.crystal:trendExcel", name = "水晶数据-趋势分析数据导出接口")
    public void trendExcel(@RequestBody @Valid AdminCrystalTrendReq adminCrystalTrendReq, HttpServletResponse httpServletResponse) {<!-- -->
        try {<!-- -->
            List&lt;List&lt;Object&gt;&gt; sheet1 = crystalDataService.trendExcel(adminCrystalTrendReq);
            sheet1.add(0, Arrays.asList("日期", "用户获得水晶数", "平台赠送水晶数", "用户支出水晶数", "平台剩余水晶数"));
            // 这里注意 有同学反应使用swagger 会导致各种问题，请直接用浏览器或者用postman
            httpServletResponse.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
            httpServletResponse.setCharacterEncoding("utf-8");
            // 这里URLEncoder.encode可以防止中文乱码 当然和easyexcel没有关系
            DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy年MM月dd日HH时mm分ss秒");
            String fileName = URLEncoder.encode(
                    "水晶数据趋势分析数据列表" + LocalDateTime.now(ZoneOffset.ofHours(8)).format(dateTimeFormatter)
                    , "UTF-8"
            ).replaceAll("\\+", "%20");
            //前端可以通过这个配置获取头信息
            httpServletResponse.setHeader("Access-Control-Expose-Headers", "Content-Disposition");
            httpServletResponse.setHeader("Content-disposition", "attachment;filename=" + fileName + ".xlsx");
            EasyExcel.write(httpServletResponse.getOutputStream()).autoCloseStream(Boolean.TRUE).excelType(ExcelTypeEnum.XLSX).sheet("Sheet1").doWrite(sheet1);
        } catch (IOException e) {<!-- -->
            log.error("水晶数据-趋势分析数据导出接口", e);
        }
    }

```

>  
 效果如下： 


<img src="https://img-blog.csdnimg.cn/78c76b80c4174fd3ad01ee4a3e2fd7c6.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/11ae63ec8d0c41f39b37215840b9b764.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 如何合并表格呢

>  
 编写表格处理工具 


```
package app.woya.service.admin.utils;

import com.alibaba.excel.metadata.Head;
import com.alibaba.excel.write.merge.AbstractMergeStrategy;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.util.CellRangeAddress;

import java.util.*;

public class MergeStrategyUtil extends AbstractMergeStrategy {<!-- -->

    // 合并的列编号，从0开始，指定的index或自己按字段顺序数
    private Set&lt;Integer&gt; mergeCellIndex = new HashSet&lt;&gt;();

    // 数据集大小，用于区别结束行位置
    private Integer maxRow = 0;

    // 禁止无参声明
    private MergeStrategyUtil() {<!-- -->
    }

    public MergeStrategyUtil(Integer maxRow, int... mergeCellIndex) {<!-- -->
        Arrays.stream(mergeCellIndex).forEach(item -&gt; {<!-- -->
            this.mergeCellIndex.add(item);
        });
        this.maxRow = maxRow;
    }

    // 记录上一次合并的信息
    private Map&lt;Integer, MergeRange&gt; lastRow = new HashMap&lt;&gt;();

    @Override
    protected void merge(Sheet sheet, Cell cell, Head head, Integer relativeRowIndex) {<!-- -->
        int currentCellIndex = cell.getColumnIndex();
        // 判断该列是否需要合并
        if (mergeCellIndex.contains(currentCellIndex)) {<!-- -->
            String currentCellValue = cell.getStringCellValue();
            int currentRowIndex = cell.getRowIndex();
            if (!lastRow.containsKey(currentCellIndex)) {<!-- -->
                // 记录首行起始位置
                lastRow.put(currentCellIndex, new MergeRange(currentCellValue, currentRowIndex, currentRowIndex, currentCellIndex, currentCellIndex));
                return;
            }
            //有上行这列的值了，拿来对比.
            MergeRange mergeRange = lastRow.get(currentCellIndex);
            if (!(mergeRange.lastValue != null &amp;&amp; mergeRange.lastValue.equals(currentCellValue))) {<!-- -->
                // 结束的位置触发下合并.
                // 同行同列不能合并，会抛异常
                if (mergeRange.startRow != mergeRange.endRow || mergeRange.startCell != mergeRange.endCell) {<!-- -->
                    sheet.addMergedRegionUnsafe(new CellRangeAddress(mergeRange.startRow, mergeRange.endRow, mergeRange.startCell, mergeRange.endCell));
                }
                // 更新当前列起始位置
                lastRow.put(currentCellIndex, new MergeRange(currentCellValue, currentRowIndex, currentRowIndex, currentCellIndex, currentCellIndex));
            }
            // 合并行 + 1
            mergeRange.endRow += 1;
            // 结束的位置触发下最后一次没完成的合并
            if (relativeRowIndex.equals(maxRow - 1)) {<!-- -->
                MergeRange lastMergeRange = lastRow.get(currentCellIndex);
                // 同行同列不能合并，会抛异常
                if (lastMergeRange.startRow != lastMergeRange.endRow || lastMergeRange.startCell != lastMergeRange.endCell) {<!-- -->
                    sheet.addMergedRegionUnsafe(new CellRangeAddress(lastMergeRange.startRow, lastMergeRange.endRow, lastMergeRange.startCell, lastMergeRange.endCell));
                }
            }
        }
    }

}

class MergeRange {<!-- -->
    public int startRow;
    public int endRow;
    public int startCell;
    public int endCell;
    public String lastValue;

    public MergeRange(String lastValue, int startRow, int endRow, int startCell, int endCell) {<!-- -->
        this.startRow = startRow;
        this.endRow = endRow;
        this.startCell = startCell;
        this.endCell = endCell;
        this.lastValue = lastValue;
    }
}

```

>  
 数据格式依旧是List&lt;List&gt;格式 


```
public List&lt;List&lt;Object&gt;&gt; trendExcel(AUnionDailyReq aUnionDailyReq) {<!-- -->
        aUnionDailyReq.setPageNo(1);
        aUnionDailyReq.setPageSize(999999);
        AppPageResp&lt;AUnionDailyTreeResp&gt; dataList = getDataList(aUnionDailyReq);
        List&lt;List&lt;Object&gt;&gt; all = new ArrayList&lt;&gt;();
        if (Objects.nonNull(dataList) &amp;&amp; !CollectionUtils.isEmpty(dataList.getList())) {<!-- -->
            List&lt;AUnionDailyTreeResp&gt; list = dataList.getList();
            list.forEach(l -&gt; {<!-- -->
                if (!CollectionUtils.isEmpty(l.getDailyResps())) {<!-- -->
                    List&lt;AUnionDailyResp&gt; dailyResps = l.getDailyResps();
                    dailyResps.forEach(d2 -&gt; {<!-- -->
                        List&lt;Object&gt; res = new ArrayList&lt;&gt;();
                        res.add(d2.getNickName() + "(" + d2.getImNumber() + ")");
                        res.add(d2.getDate());
                        res.add(d2.getOnlineTime());
                        res.add(d2.getCallCount());
                        res.add(d2.getCallPeopleCount());
                        res.add(d2.getCallTime());
                        res.add(d2.getSendCount());
                        res.add(d2.getReceiveCount());
                        res.add(d2.getGreetCount());
                        res.add(d2.getBeGreetCount());
                        res.add(d2.getSendMsgScale());
                        res.add(d2.getCrystal());
                        all.add(res);
                    });
                }
            });
        }
        return all;

```

>  
 导出代码 


```
/**
     * 导出公会每日数据数据
     *
     * @param aUnionDailyReq 工会的日常需要
     * @return {@link ApiResult}&lt;{@link AppPageResp}&lt;{@link AUnionDailyResp}&gt;&gt;
     */
    @PostMapping("/data/export")
    @Permission(value = "union.daily:trendExcel", name = "导出公会每日数据数据")
    public void trendExcel(@RequestBody @Valid AUnionDailyReq aUnionDailyReq, HttpServletResponse httpServletResponse) {<!-- -->
        try {<!-- -->
            List&lt;List&lt;Object&gt;&gt; sheet1 = unionDailyService.trendExcel(aUnionDailyReq);
            sheet1.add(
                    0,
                    Arrays.asList(
                            "主播昵称（im）",
                            "日期", "在线时长",
                            "主动呼叫次数",
                            "主动呼叫人数",
                            "通话时长",
                            "发送消息数",
                            "接收消息数",
                            "主动打招呼",
                            "被打招呼",
                            "发送消息率",
                            "水晶收益"
                    )
            );
            // 这里注意 有同学反应使用swagger 会导致各种问题，请直接用浏览器或者用postman
            httpServletResponse.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
            httpServletResponse.setCharacterEncoding("utf-8");
            // 这里URLEncoder.encode可以防止中文乱码 当然和easyexcel没有关系
            DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy年MM月dd日HH时mm分ss秒");
            String fileName = URLEncoder.encode(
                    "导出公会每日数据数据" + LocalDateTime.now(ZoneOffset.ofHours(8)).format(dateTimeFormatter)
                    , "UTF-8"
            ).replaceAll("\\+", "%20");
            //前端可以通过这个配置获取头信息
            httpServletResponse.setHeader("Access-Control-Expose-Headers", "Content-Disposition");
            httpServletResponse.setHeader("Content-disposition", "attachment;filename=" + fileName + ".xlsx");
            EasyExcel.write(httpServletResponse.getOutputStream())
                    .registerWriteHandler(new MergeStrategyUtil(sheet1.size(), 0))
                    .autoCloseStream(Boolean.TRUE)
                    .excelType(ExcelTypeEnum.XLSX)
                    .sheet("Sheet1")
                    .doWrite(sheet1);
        } catch (IOException e) {<!-- -->
            log.error("导出公会每日数据数据接口", e);
        }

```

>  
 效果图： 


<img src="https://img-blog.csdnimg.cn/f039dc9d05eb45db828a992a802a4ba9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7c1eccf1c10b4f7caa20b852b09d258a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 详细合并(自己指定某行某列合并)

>  
 使用ExcelWriterSheetBuilder 


```
/**
     * 每日用户数据统计-导出接口
     */
    @PostMapping("/statExport")
    @Permission(value = "data.new_user_stat:statexp", name = "每日用户数据统计-导出接口")
    public void statExport(@RequestBody @Valid GetCountryDayStatDetailListReq getCountryDayStatDetailListReq, HttpServletResponse httpServletResponse) {<!-- -->
        try {<!-- -->
            ExcelWriterSheetBuilder excelWriterSheetBuilder = EasyExcel.write(httpServletResponse.getOutputStream())
                    .autoCloseStream(Boolean.TRUE).excelType(ExcelTypeEnum.XLSX).sheet("Sheet1");
            List&lt;List&lt;Object&gt;&gt; sheet1 = dayStatService.statDetailExport(getCountryDayStatDetailListReq, excelWriterSheetBuilder);
            sheet1.add(0, Arrays.asList("日期", "国家", "渠道", "登录人数", "新增人数", "充值人数", "充值笔数", "新增充值人数", "新增充值笔数", "充值金额", "官网充值", "新增充值金额", "付费率", "新增付费率"));
            // 这里注意 有同学反应使用swagger 会导致各种问题，请直接用浏览器或者用postman
            httpServletResponse.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
            httpServletResponse.setCharacterEncoding("utf-8");
            // 这里URLEncoder.encode可以防止中文乱码 当然和easyexcel没有关系
            String fileName = URLEncoder.encode("每日用户新增数据统计报表", "UTF-8").replaceAll("\\+", "%20");
            //前端可以通过这个配置获取头信息
            httpServletResponse.setHeader("Access-Control-Expose-Headers", "Content-Disposition");
            httpServletResponse.setHeader("Content-disposition", "attachment;filename=" + fileName + ".xlsx");
            excelWriterSheetBuilder.doWrite(sheet1);
        } catch (IOException e) {<!-- -->
            log.error("公会待结算报表导出发生异常", e);
        }
    }

```

```
public List&lt;List&lt;Object&gt;&gt; statDetailExport(GetCountryDayStatDetailListReq getCountryDayStatDetailListReq, ExcelWriterSheetBuilder excelWriterSheetBuilder) {<!-- -->
        ApiResult&lt;AppPageResp&lt;DayStatData&gt;&gt; appPageRespApiResult = countryDayStatsApiService.statDetail(getCountryDayStatDetailListReq);
        if (!appPageRespApiResult.resultIsSuccess()) {<!-- -->
            return Collections.emptyList();
        }
        if (StringUtils.isEmpty(appPageRespApiResult.getData().getList())) {<!-- -->
            return Collections.emptyList();
        }
        List&lt;List&lt;Object&gt;&gt; allRowData = new ArrayList&lt;&gt;();
        AtomicInteger rowIndex = new AtomicInteger(1);
        appPageRespApiResult.getData().getList().forEach(dayStatData -&gt; {<!-- -->
            //日期 国家 渠道 登录人数 新增人数 充值人数 充值笔数 新增充值人数 新增充值笔数 充值金额 官网充值 新增充值金额 付费率 新增付费率
            if (dayStatData.getCountryList().size() &gt; 0) {<!-- -->
                int lastRowIndex = rowIndex.get() + dayStatData.getCountryList().stream().map(cd -&gt; cd.getSubDeviceDatas().size()).reduce(Integer::sum).orElse(0) - 1;
                excelWriterSheetBuilder.registerWriteHandler(new OnceAbsoluteMergeStrategy(rowIndex.get(), lastRowIndex, 0, 0));
            }
            dayStatData.getCountryList().forEach(countryStatData -&gt; {<!-- -->

                if (countryStatData.getSubDeviceDatas().size() &gt; 0) {<!-- -->
                    int lastRowIndex = rowIndex.get() + countryStatData.getSubDeviceDatas().size() - 1;
                    excelWriterSheetBuilder.registerWriteHandler(new OnceAbsoluteMergeStrategy(rowIndex.get(), lastRowIndex, 1, 1));
                    excelWriterSheetBuilder.registerWriteHandler(new OnceAbsoluteMergeStrategy(rowIndex.get(), lastRowIndex, 10, 10));
                }
                countryStatData.getSubDeviceDatas().forEach(subDeviceStatDataResp -&gt; {<!-- -->
                    List&lt;Object&gt; rowData = new ArrayList&lt;&gt;();
                    rowData.add(dayStatData.getDate());
                    rowData.add(countryStatData.getCountryName());
                    rowData.add(subDeviceStatDataResp.getSubDeviceType() == 11 ? "安卓" : "ios");
                    rowData.add(subDeviceStatDataResp.getTotalSignInUser());
                    rowData.add(subDeviceStatDataResp.getTotalNewUser());
                    rowData.add(subDeviceStatDataResp.getTotalRechargeUsers());
                    rowData.add(subDeviceStatDataResp.getTotalRechargeOrders());
                    rowData.add(subDeviceStatDataResp.getTotalNewUserRechargeUsers());
                    rowData.add(subDeviceStatDataResp.getTotalNewUserRechargeOrders());
                    rowData.add(subDeviceStatDataResp.getTotalRechargeAmount());
                    rowData.add(countryStatData.getTotalThirdPartyRechargeAmount());
                    rowData.add(subDeviceStatDataResp.getTotalNewUserRechargeAmount());
                    rowData.add(subDeviceStatDataResp.getTotalSignInUser().intValue() == 0 ? 0L : BigDecimal.valueOf(subDeviceStatDataResp.getTotalRechargeUsers()).divide(BigDecimal.valueOf(subDeviceStatDataResp.getTotalSignInUser()), 2, RoundingMode.DOWN));
                    rowData.add(subDeviceStatDataResp.getTotalNewUser() == 0 ? 0L : BigDecimal.valueOf(subDeviceStatDataResp.getTotalNewUserRechargeUsers()).divide(BigDecimal.valueOf(subDeviceStatDataResp.getTotalNewUser()), 2, RoundingMode.DOWN));
                    allRowData.add(rowData);
                    rowIndex.incrementAndGet();
                });
            });

        });
        return allRowData;

    }

```

>  
 导出效果 


<img src="https://img-blog.csdnimg.cn/47b70cb199b54303ad89fe8076a026f8.png" alt="在这里插入图片描述">

### 如何制作模板并添加批注

**jar包及版本**

```
&lt;!--hutool工具包--&gt;
&lt;dependency&gt;
    &lt;groupId&gt;cn.hutool&lt;/groupId&gt;
    &lt;artifactId&gt;hutool-all&lt;/artifactId&gt;
    &lt;version&gt;5.5.1&lt;/version&gt;
&lt;/dependency&gt;
&lt;!-- EasyExcel文档处理工具 --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
    &lt;artifactId&gt;easyexcel&lt;/artifactId&gt;
    &lt;version&gt;2.2.8&lt;/version&gt;
&lt;/dependency&gt;

```

```
@ApiOperation("获取批量导入会员模板")
    @GetMapping("/get/excel/template")
    @ApiImplicitParams({<!-- -->
            @ApiImplicitParam(name = "type", value = "类型: 1个人,2企业", required = true, dataType = "Integer")
    })
    public void getExcelTemplate(@RequestParam("type") Long type, HttpServletResponse httpServletResponse) {<!-- -->
        try {<!-- -->
            List&lt;List&lt;Object&gt;&gt; dataList = new ArrayList&lt;&gt;();
            dataList.add(new ArrayList&lt;&gt;(Collections.singletonList("注意：")));
            dataList.add(new ArrayList&lt;&gt;(Collections.singletonList("1、请勿修改表格中的注意事项、字段顺序，或随意增加、删除表格字段")));
            dataList.add(new ArrayList&lt;&gt;(Collections.singletonList("2、申请职务请务必保持与本商协会职务列表内的相同")));
            dataList.add(new ArrayList&lt;&gt;(Collections.singletonList(" ")));
            dataList.add(new ArrayList&lt;&gt;(Collections.singletonList(" ")));
            dataList.add(new ArrayList&lt;&gt;(type == 1 ?
                    Arrays.asList(
                            "姓名（必填）",
                            "出生日期（必填）",
                            "性别（必填）",
                            "学历（选填）",
                            "身份证号码（必填）",
                            "申请职务（必填）",
                            "联系电话（必填）",
                            "公司名称（必填）",
                            "担任职位（必填）",
                            "所属行业（必填）"
                    ) :
                    Arrays.asList(
                            "企业名称（必填）",
                            "企业成立时间（必填）",
                            "所属行业（必填）",
                            "企业员工数量（必填）",
                            "统一社会信用代码（必填）",
                            "法人姓名（必填）",
                            "法人身份证号码（必填）",
                            "法人联系电话（必填）",
                            "联系人姓名（必填）",
                            "联系人电话（必填）",
                            "担任职位（必填）",
                            "申请职位（必填）"
                    )));
            String sheetName = "模板";
            List&lt;CommentModel&gt; commentList = new ArrayList&lt;&gt;();
            //查询行业
            List&lt;CategoryDto&gt; categoryDtoList = memberService.getIndustryList();
            String industryNotation = "注：\n";
            if (!CollectionUtils.isEmpty(categoryDtoList)) {<!-- -->
                industryNotation = industryNotation.concat(categoryDtoList.stream().map(CategoryDto::getName).collect(Collectors.joining("、")));
            }
            if (type == 1) {<!-- -->
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 1, "注：\n1999/09/09\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 2, "注：\n男/女\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 3, "注：\n博士、通硕士、本科、专科、普通中专、其它\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 5, "注：\n商协会职务\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 9, industryNotation));
            } else {<!-- -->
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 1, "注：\n1999/09/09\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 2, industryNotation));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 3, "注：\n" +
                        "20-99人\n" +
                        "100-499人\n" +
                        "500-999人\n" +
                        "1000-9999人\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 9, "注：\n" +
                        "手机号码\n"));
                commentList.add(CommentModel.createCommentModel(sheetName, 5, 11, "注：\n" +
                        "商协会职务\n"));
            }

            // 这里注意 有同学反应使用swagger 会导致各种问题，请直接用浏览器或者用postman
            httpServletResponse.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
            httpServletResponse.setCharacterEncoding("utf-8");
            // 这里URLEncoder.encode可以防止中文乱码 当然和easyexcel没有关系
            DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy年MM月dd日HH时mm分ss秒");
            String fileName = URLEncoder.encode(
                    (type == 1 ? "个人" : "企业") + "模板" + LocalDateTime.now(ZoneOffset.ofHours(8)).format(dateTimeFormatter)
                    , "UTF-8"
            ).replaceAll("\\+", "%20");
            //前端可以通过这个配置获取头信息
            httpServletResponse.setHeader("Access-Control-Expose-Headers", "Content-Disposition");
            httpServletResponse.setHeader("Content-disposition", "attachment;filename=" + fileName + ".xlsx");
            ExcelWriter excelWriter = EasyExcel.write(httpServletResponse.getOutputStream())
                    .inMemory(Boolean.TRUE)
                    .registerWriteHandler(new CommentWriteHandler(commentList, "xlsx"))
                    .build();
            WriteSheet writeSheet = EasyExcel.writerSheet(sheetName).build();
            excelWriter.write(dataList, writeSheet);
            //千万别忘记finish 会帮忙关闭流
            excelWriter.finish();
        } catch (IOException e) {<!-- -->
            log.error("批量导入会员模板-生成接口异常", e);
        }
    }

```

**批注信息类**

```
package com.ljq.cca.lib.ccadmin.api.domain.dto.easyExcel;

import lombok.Getter;

/**
 * 批注信息类
 *
 * @author 刘俊秦
 */
@Getter
public class CommentModel {<!-- -->

    /**
     * sheet页名称
     */
    private String sheetName;
    /**
     * 列索引
     */
    private int colIndex;
    /**
     * 行索引
     */
    private int rowIndex;
    /**
     * 行索引
     */
    private String commentContent;

    private void setSheetName(String sheetName) {<!-- -->
        this.sheetName = sheetName;
    }

    private void setColIndex(int colIndex) {<!-- -->
        this.colIndex = colIndex;
    }

    private void setRowIndex(int rowIndex) {<!-- -->
        this.rowIndex = rowIndex;
    }

    private void setCommentContent(String commentContent) {<!-- -->
        this.commentContent = commentContent;
    }

    private CommentModel() {<!-- -->

    }

    /**
     * 生成批注信息
     *
     * @param sheetName      sheet页名称
     * @param rowIndex       行号
     * @param columnIndex    列号
     * @param commentContent 批注内容
     * @return
     */
    public static CommentModel createCommentModel(String sheetName, int rowIndex, int columnIndex, String commentContent) {<!-- -->
        CommentModel commentModel = new CommentModel();
        //sheet页名称
        commentModel.setSheetName(sheetName);
        //行号
        commentModel.setRowIndex(rowIndex);
        //列号
        commentModel.setColIndex(columnIndex);
        //批注内容
        commentModel.setCommentContent(commentContent);
        return commentModel;
    }

}


```

**自定义批注处理器**

```
package com.ljq.cca.service.ccadmin.util;

import cn.hutool.core.collection.CollUtil;
import cn.hutool.core.util.StrUtil;
import com.alibaba.excel.write.handler.AbstractRowWriteHandler;
import com.alibaba.excel.write.metadata.holder.WriteSheetHolder;
import com.alibaba.excel.write.metadata.holder.WriteTableHolder;
import com.ushangxie.cca.lib.ccadmin.api.domain.dto.easyExcel.CommentModel;
import org.apache.poi.hssf.usermodel.HSSFClientAnchor;
import org.apache.poi.hssf.usermodel.HSSFRichTextString;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFClientAnchor;
import org.apache.poi.xssf.usermodel.XSSFRichTextString;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 自定义批注处理器
 *
 * @author 刘俊秦
 * @date 2022/07/12
 */
public class CommentWriteHandler extends AbstractRowWriteHandler {<!-- -->

    /**
     * sheet页名称列表
     */
    private List&lt;String&gt; sheetNameList;
    List&lt;CommentModel&gt; commentList = new ArrayList&lt;&gt;();

    /**
     * 自定义批注适配器构造方法
     *
     * @param commentList 批注信息
     * @param extension   文件后缀（xlsx、xls）
     */
    public CommentWriteHandler(List&lt;CommentModel&gt; commentList, String extension) {<!-- -->
        if (CollUtil.isEmpty(commentList)) {<!-- -->
            return;
        }
        //文件不为指定的格式时，默认为Xlsx
        if (!StrUtil.equals(extension, "xlsx") &amp;&amp; !StrUtil.equals(extension, "xls")) {<!-- -->
            extension = "xlsx";
        }
        this.commentList = commentList.stream().filter(x -&gt;
                StrUtil.isNotBlank(x.getSheetName()) &amp;&amp; x.getColIndex() &gt;=0 &amp;&amp; x.getRowIndex() &gt;= 0 &amp;&amp; StrUtil.isNotBlank(x.getCommentContent())
        ).collect(Collectors.toList());
        sheetNameList = this.commentList.stream().map(x -&gt; x.getSheetName()).distinct().collect(Collectors.toList());
        this.extension = extension;
    }

    /**
     * 文档后缀名
     */
    private String extension;

    @Override
    public void afterRowDispose(WriteSheetHolder writeSheetHolder, WriteTableHolder writeTableHolder, Row row,
                                Integer relativeRowIndex, Boolean isHead) {<!-- -->
        Sheet sheet = writeSheetHolder.getSheet();
        //不需要添加批注，或者当前sheet页不需要添加批注
        if (CollUtil.isEmpty(commentList) || sheetNameList.contains(sheet.getSheetName()) == false) {<!-- -->
            return;
        }
        //获取当前行的批注信息
        List&lt;CommentModel&gt; rowCommentList = commentList.stream().filter(x -&gt;
                StrUtil.equals(x.getSheetName(), sheet.getSheetName())
                        &amp;&amp; EqualsUtilEquals(relativeRowIndex, x.getRowIndex())).collect(Collectors.toList());
        //当前行没有批注信息
        if (CollUtil.isEmpty(rowCommentList)) {<!-- -->
            return;
        }
        List&lt;Integer&gt; colIndexList = rowCommentList.stream().map(x -&gt; x.getColIndex()).distinct().collect(Collectors.toList());
        for (Integer colIndex : colIndexList) {<!-- -->
            //同一单元格的批注信息
            List&lt;CommentModel&gt; cellCommentList = rowCommentList.stream().filter(x -&gt;
                    EqualsUtilEquals(colIndex, x.getColIndex())).collect(Collectors.toList());
            if (CollUtil.isEmpty(cellCommentList)) {<!-- -->
                continue;
            }
            //批注内容拼成一条
            String commentContent = cellCommentList.stream().map(x -&gt; x.getCommentContent()).collect(Collectors.joining());
            Cell cell = row.getCell(colIndex);
            POIUtilAddComment(cell, commentContent, extension);
        }
        //删除批注信息
        commentList.remove(rowCommentList);
        //重新获取要添加的sheet页姓名
        sheetNameList = commentList.stream().map(x -&gt; x.getSheetName()).distinct().collect(Collectors.toList());
    }

    /**
     * 判断相等
     *
     * @param num1
     * @param num2
     * @return true相等，false不相等
     */
    public static boolean EqualsUtilEquals(Object num1, Object num2) {<!-- -->
        if (num1 == null &amp;&amp; num2 == null) {<!-- -->
            return true;
        }
        if (num1 == null || num2 == null) {<!-- -->
            return false;
        }
        //==比较比equals比较性能更好
        if (num1 == num2) {<!-- -->
            return true;
        }
        return num1.equals(num2);
    }

    /**
     * 给Cell添加批注
     *
     * @param cell 单元格
     * @param value 批注内容
     * @param extension 扩展名
     */
    public static void POIUtilAddComment(Cell cell, String value, String extension) {<!-- -->
        Sheet sheet = cell.getSheet();
        cell.removeCellComment();
        if ("xls".equals(extension)) {<!-- -->
            ClientAnchor anchor = new HSSFClientAnchor();
            // 关键修改
            anchor.setDx1(0);
            anchor.setDx2(0);
            anchor.setDy1(0);
            anchor.setDy2(0);
            anchor.setCol1(cell.getColumnIndex());
            anchor.setRow1(cell.getRowIndex());
            anchor.setCol2(cell.getColumnIndex() + 5);
            anchor.setRow2(cell.getRowIndex() + 6);
            // 结束
            Drawing drawing = sheet.createDrawingPatriarch();
            Comment comment = drawing.createCellComment(anchor);
            // 输入批注信息
            comment.setString(new HSSFRichTextString(value));
            // 将批注添加到单元格对象中
            cell.setCellComment(comment);
        } else if ("xlsx".equals(extension)) {<!-- -->
            ClientAnchor anchor = new XSSFClientAnchor();
            // 关键修改
            anchor.setDx1(0);
            anchor.setDx2(0);
            anchor.setDy1(0);
            anchor.setDy2(0);
            anchor.setCol1(cell.getColumnIndex());
            anchor.setRow1(cell.getRowIndex());
            anchor.setCol2(cell.getColumnIndex() + 5);
            anchor.setRow2(cell.getRowIndex() + 6);
            // 结束
            Drawing drawing = sheet.createDrawingPatriarch();
            Comment comment = drawing.createCellComment(anchor);
            // 输入批注信息
            comment.setString(new XSSFRichTextString(value));
            // 将批注添加到单元格对象中
            cell.setCellComment(comment);
        }
    }

}


```
