
--- 
title:  Java Web文件下载示例 
tags: []
categories: [] 

---
一、服务端存在模板文件

```
@ApiOperation(value = "知识导入模板", notes = "下载")
    @GetMapping("down/knowinfo")
    public void downKnowInfo(HttpServletResponse response){
        response.setContentType("application/vnd.ms-excel");
        response.setCharacterEncoding("utf-8");
        OutputStream out = null;
        BufferedOutputStream bos =null;
        InputStream inputStream=null;
        try {
            out = response.getOutputStream();
            bos = new BufferedOutputStream(out);
            DefaultResourceLoader resourceLoader = new DefaultResourceLoader();
            Resource resource = resourceLoader.getResource("classpath:file/知识数据导入模板.xlsx");
            inputStream = resource.getInputStream();
            String downFileName = URLEncoder.encode("知识数据导入模板", "UTF-8")+".xlsx";
            response.setHeader("Content-disposition", "attachment;filename=" + downFileName);
            ExcelWriter excelWriter = EasyExcel.write(bos).withTemplate(inputStream).build();
            WriteSheet writeSheet = EasyExcel.writerSheet().build();
            excelWriter.fill("",writeSheet);
            excelWriter.finish();
            bos.flush();
        } catch (IOException e) {
            // 重置response
            response.reset();
            response.setContentType("application/json");
            response.setCharacterEncoding("utf-8");
            Map&lt;String, String&gt; map = new HashMap&lt;String, String&gt;();
            map.put("status", "failure");
            map.put("message", "下载文件失败" + e.getMessage());
            try {
                response.getWriter().println(JSON.toJSONString(map));
            } catch (IOException e1) {
                e1.printStackTrace();
            }
        }

    }
```

```
         &lt;resources&gt;
            &lt;resource&gt;
                &lt;directory&gt;src/main/resources&lt;/directory&gt;
                &lt;includes&gt;
                    &lt;include&gt;**/*.*&lt;/include&gt;
                &lt;/includes&gt;
                &lt;filtering&gt;false&lt;/filtering&gt;
            &lt;/resource&gt;

        &lt;/resources&gt;
```

 

二、文件在服务器的固定目录下

```
@ApiOperation(value ="下载文件",notes ="根据文件ID，下载文件")
    @GetMapping(value = "/download")
    public void download(@RequestParam("id")Long fileId) {
        FileInfo info = fileInfoService.selectById(fileId);
        String location = info.getRelativePath()+ File.separator+info.getName();
        String fileName = info.getName();
        HttpServletResponse response = getResponse();
        Path path = Paths.get(location);
        if(Files.exists(path)){
            try {
                // 创建输出流对象
                ServletOutputStream outputStream = response.getOutputStream();
                //以字节数组的形式读取文件
                byte[] bytes = FileUtil.readBytes(location);
                // 告诉浏览器输出内容为流
                response.setHeader("Content-Type", "application/octet-stream;charset=utf-8");
                // 把文件名按UTF-8取出并按ISO8859-1编码，保证弹出窗口中的文件名中文不乱码
                // 中文不要太多，最多支持17个中文，因为header有150个字节限制。
                // 这一步一定要在读取文件之后进行，否则文件名会乱码，找不到文件
                fileName = new String(fileName.getBytes("UTF-8"), "ISO8859-1");
                // 设置下载弹窗的文件名和格式（文件名要包括名字和文件格式）
                response.setHeader("Content-Disposition", "attachment;filename=" + URLEncoder.encode(fileName, "utf-8"));
                // 返回数据到输出流对象中
                outputStream.write(bytes);
                // 关闭流对象
                IoUtil.close(outputStream);
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }
/**
     * 获取request对象
     */
    public HttpServletRequest getRequest() {
        return ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
    }

    /**
     * 获取Response对象
     */
    public HttpServletResponse getResponse() {
        return ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getResponse();
    }

    /**
     * 获取Session对象
     */
    public HttpSession getSession() {
        return ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest().getSession();
    }



```

三、知道文件的url网址

```
@ApiOperation(value = "下载",notes = "日报")
    @GetMapping("down/{id}")
    public void downDayFile(@PathVariable("id")Long id){
        log.info("下载文件：{}",id);
        DayReport dayReport = dayReportMapper.selectById(id);
        if(dayReport==null){
            throw new BusinessException("系统异常");
        }
        String location = dayReport.getFileLocation();
        int i = location.lastIndexOf(File.separator);
        String s = location.substring(i + 1, location.length());
        String url = baseUrl + s + "/" + dayReport.getFileIdentity() + "/" + dayReport.getFileName();
        HttpServletResponse response = getResponse();
        String fileName = dayReport.getFileName();
        try {
            // 创建输出流对象
            ServletOutputStream outputStream = response.getOutputStream();
            //以字节数组的形式读取文件
            URL url1 = new URL(url);
            URLConnection connection = url1.openConnection();
            InputStream stream = connection.getInputStream();

            // 告诉浏览器输出内容为流
            response.setHeader("Content-Type", "application/octet-stream;charset=utf-8");
            // 把文件名按UTF-8取出并按ISO8859-1编码，保证弹出窗口中的文件名中文不乱码
            // 中文不要太多，最多支持17个中文，因为header有150个字节限制。
            // 这一步一定要在读取文件之后进行，否则文件名会乱码，找不到文件
            fileName = new String(fileName.getBytes("UTF-8"), "ISO8859-1");
            // 设置下载弹窗的文件名和格式（文件名要包括名字和文件格式）
            response.setHeader("Content-Disposition", "attachment;filename=" + URLEncoder.encode(fileName, "utf-8"));
            // 返回数据到输出流对象中
        //    outputStream.write(bytes);
            byte[] bytes = new byte[1024];
            int length=0;
            while ((length=stream.read(bytes,0,1024))!=-1){
                outputStream.write(bytes,0,length);
            }
            IoUtil.close(stream);
            // 关闭流对象
            IoUtil.close(outputStream);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }



    }
    /**
     * 获取Response对象
     */
    public HttpServletResponse getResponse() {
        return ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getResponse();
    }
```

 
