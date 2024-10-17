
--- 
title:  thumbnailator个人使用笔记 
tags: []
categories: [] 

---
### 导包 就不解释了

```
&lt;properties&gt;
	&lt;thumbnailator.version&gt;0.4.8&lt;/thumbnailator.version&gt;
&lt;/properties&gt;
&lt;dependencies&gt;
	&lt;!-- thumbnailator 谷歌图片压缩工具 --&gt;
	 &lt;dependency&gt;
	     &lt;groupId&gt;net.coobird&lt;/groupId&gt;
	     &lt;artifactId&gt;thumbnailator&lt;/artifactId&gt;
	     &lt;version&gt;${<!-- -->thumbnailator.version}&lt;/version&gt;
	 &lt;/dependency&gt;
&lt;/dependencies&gt;

```

### 使用thumbnailator给原图添加水印

```
// 原图片地址
        String imageUrl = "C:/Users/Administrator/Desktop/墨花.jpg";
        // 水印图片 相对于resource目录
        String watermark = "C:/Users/Administrator/Desktop/水印.jpg";
        // 输出到文件
        String outputFile = "C:/Users/Administrator/Desktop/test.jpeg";
        // 不透明度
        float opacity = 0.25f;
        try {<!-- -->
            // 获取原图文件
            File file = new File(imageUrl);
            // ImageIO读取图片
            BufferedImage image = ImageIO.read(file);

            File sy_file = new File(watermark);
            // ImageIO读取图片
            BufferedImage sy_image = ImageIO.read(sy_file);

            Thumbnails.of(image)
                    // 设置图片大小
                    .size(image.getWidth(), image.getHeight())
                    // 加水印 参数：1.水印位置 2.水印图片 3.不透明度0.0-1.0
                    .watermark(Positions.BOTTOM_LEFT, sy_image, opacity)
                    // 输出到文件
                    .toFile(outputFile);
        } catch (Exception e){<!-- -->
            LogPrintUtil.logRunTimeError(e);
        }

```

>  
 效果： 原图： <img src="https://img-blog.csdnimg.cn/20200506154335647.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 水印： <img src="https://img-blog.csdnimg.cn/20200506154351233.jpg" alt="在这里插入图片描述"> 结果：（水印使用的图片是jpg的所有它不是透明背景，所有这个水印加的有点不好看，读者见谅） <img src="https://img-blog.csdnimg.cn/20200506154419302.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 


>  
 本人刚2020-5-13踩的坑，当天解决，图片以字节流形式添加水印。水印用的是远程图片。代码如下： 


```
/*
     * 功能描述:
     * 〈图片加水印〉
     *
     * @param io 1
     * @param watermarkPath 2
     * @param positions 3
     * @param opacity 4
     * @param is_compression 5
     * @return : java.io.ByteArrayInputStream
     * @author : ljq-刘俊秦
     * @date : 2020/5/12 0012 下午 7:12
     */
    public static ByteArrayInputStream addWatermarkUrl(
            InputStream io,
            String watermarkPath,
            Position positions,
            float opacity

    ) {<!-- -->

        try {<!-- -->
            var os = new ByteArrayOutputStream();
            // ImageIO读取图片
            BufferedImage image = ImageIO.read(io);
            //水印图片 取url图片
            URL url = new URL(watermarkPath);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            //设置请求方式为"GET"
            conn.setRequestMethod("GET");
            //超时响应时间为5秒
            conn.setConnectTimeout(5 * 1000);
            //通过输入流获取图片数据
            var watermarkIo = conn.getInputStream();
            // ImageIO读取图片
            BufferedImage sy_image = ImageIO.read(watermarkIo);
            Thumbnails.of(image)// 设置图片大小
                    .size(image.getWidth(), image.getHeight())
                    // 加水印 参数：1.水印位置 2.水印图片 3.不透明度0.0-1.0
                    .watermark(
                            positions,
                            sy_image,
                            opacity
                    )
                    .outputFormat("png") //流是图片BufferedImageSource 必须定义类型。不然报错 定义输出图片类型
                    // 输出到输出流
                    .toOutputStream(os);
            var bio = new ByteArrayInputStream(os.toByteArray());

            //用完关掉
            os.close();
            io.close();
            watermarkIo.close();

            return bio;
        } catch (Exception e) {<!-- -->
            LogPrintUtil.logRunTimeError(e);
            return null;
        }
    }

```

### 文件压缩

>  
 本人用的是字节流形式，读者可自行改写。 


```
/*
     * 功能描述:
     * 〈图片大于1M的就进行压缩〉
     *
     * @param io 1
     * @return : java.io.ByteArrayInputStream
     * @author : ljq-刘俊秦
     * @date : 2020/5/12 0012 下午 7:12
     */
    public static ByteArrayInputStream imgHalfCompression(InputStream io) {<!-- -->
        try {<!-- -->
            ByteArrayOutputStream os = new ByteArrayOutputStream();
            //判断是否是图片，是否大于1M
            if (io.available() &gt; 1024) {<!-- -->
                //处理图片进行压缩
                Thumbnails.of(io)
                        .scale(1f)
                        .outputQuality(0.5f)
                        .toOutputStream(os);
            }
            var bio = new ByteArrayInputStream(os.toByteArray());

            io.close();
            os.close();

            return bio;
        } catch (Exception e) {<!-- -->
            LogPrintUtil.logRunTimeError(e);
            return null;
        }
    }

```
