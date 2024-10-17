
--- 
title:  java word转pdf 
tags: []
categories: [] 

---
```
public static int WordToPdf(String filename, String toFilename) throws Exception {
        File file = null;
        ActiveXComponent app = null;
        long start = System.currentTimeMillis();
        try {
            app = new ActiveXComponent("Word.Application");
            app.setProperty("Visible", false);
            Dispatch docs = app.getProperty("Documents").toDispatch();
            System.out.println("打开文档..." + filename);
            Dispatch doc = Dispatch.invoke(docs, "Open", Dispatch.Method, new Object[] { filename }, new int[1])
                    .toDispatch();
            System.out.println("转换文档到PDF..." + toFilename);
            File tofile = new File(toFilename);
            if (tofile.exists()) {
                tofile.delete();
            }
            Dispatch.invoke(doc, "SaveAs", Dispatch.Method, new Object[] { toFilename, new Variant(17) }, new int[1]);
            Dispatch.call(doc, "Close", false);
            long end = System.currentTimeMillis();
            System.out.println("转换完成..用时：" + (end - start) + "ms.");
            return 1;
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("========Error:文档转换失败：" + e.getMessage());
            return 0;
        } finally {
            if (app != null) {
                app.invoke("Quit", 0);
                ComThread.Release();
            }
        }

    }


//main方法调用
public static void main(String[] args) {
        String excelPath = "D:\\tt\\123.doc";
        String pdfPath = "D:\\tt\\我是测试.pdf";
        try {
            WordToPdf(excelPath, pdfPath);
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

```
