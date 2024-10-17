
--- 
title:  java excle转pdf 
tags: []
categories: [] 

---
要先下载jacob.jar和jacob-1.17-M2-x64.dll两个jar包，放到jdk下面的jre的bin文件夹里，还要确定office的excle另存为pdf可以用  excle转pdf 这是我之前在网上找的，挺好使的，分享一下方便使用

```
public static void els2pdf(String els, String pdf) {
        System.out.println("Starting excel...");
        long start = System.currentTimeMillis();
        ActiveXComponent app = new ActiveXComponent("Excel.Application");
        try {
            app.setProperty("Visible", false);
            Dispatch workbooks = app.getProperty("Workbooks").toDispatch();
            System.out.println("opening document:" + els);
            Dispatch workbook = Dispatch.invoke(workbooks, "Open", Dispatch.Method,
                    new Object[] { els, new Variant(false), new Variant(false) }, new int[3]).toDispatch();
            Dispatch.invoke(workbook, "SaveAs", Dispatch.Method,
                    new Object[] { pdf, new Variant(57), new Variant(false), new Variant(57), new Variant(57),
                            new Variant(false), new Variant(true), new Variant(57), new Variant(true),
                            new Variant(true), new Variant(true) },
                    new int[1]);
            Variant f = new Variant(false);
            System.out.println("to pdf " + pdf);
            Dispatch.call(workbook, "Close", f);
            long end = System.currentTimeMillis();
            System.out.println("completed..used:" + (end - start) / 1000 + " s");
        } catch (Exception e) {
            System.out.println("========Error:Operation fail:" + e.getMessage());
        } finally {
            if (app != null) {
                app.invoke("Quit", new Variant[] {});
            }
        }
    }

//main方法调用
public static void main(String[] args) {
        String excelPath = "D:\\tt\\123.xls";
        String pdfPath = "D:\\tt\\我是测试.pdf";
        try {
            els2pdf(excelPath, pdfPath);
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
```
