
--- 
title:  [文字识别-tess4j]java文字识别之tess4j 
tags: []
categories: [] 

---
### 1、tess4j使用

先说结论，不好用。文字识别还是需要训练。

#### 无法做到单图多语言识别

tess4j依赖语言包文件做OCR，语言选择需要在有语言包文件时在代码中 setLanguage,默认eng ，设置后覆盖上一个。

#### 语言包看起来没人维护了

<img src="https://img-blog.csdnimg.cn/5e44b2fd7d0f47d78dc2f179bdeca326.png" alt="在这里插入图片描述">

#### 支持的图片格式

<img src="https://img-blog.csdnimg.cn/173b9065f6ba4838bc2f864195c128bf.png" alt="在这里插入图片描述">

### 2、实现

使用任意maven构建的工程即可(gradle也行)

#### 官网与依赖
- github项目 https://github.com/tesseract-ocr- 官网 http://tess4j.sourceforge.net/
在官网可以跳转到maven仓库，引入最新依赖

```
&lt;!-- https://mvnrepository.com/artifact/net.sourceforge.tess4j/tess4j --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;net.sourceforge.tess4j&lt;/groupId&gt;
    &lt;artifactId&gt;tess4j&lt;/artifactId&gt;
    &lt;version&gt;5.4.0&lt;/version&gt;
&lt;/dependency&gt;


```

#### 代码

贴一段官方demo，自己的中文注释

```

import java.io.File;
import net.sourceforge.tess4j.*;

public class TesseractExample {<!-- -->

    public static void main(String[] args) {<!-- -->
    	// 需要识别的图片
        File imageFile = new File("eurotext.tif");
        // 创建一个实例
        ITesseract instance = new Tesseract();  // JNA Interface Mapping
        // ITesseract instance = new Tesseract1(); // JNA Direct Mapping
        // 需要提供语言包的路径 需要注意，下章节说明
        instance.setDatapath("tessdata"); // path to tessdata directory

        try {<!-- -->
            String result = instance.doOCR(imageFile);
            System.out.println(result);
        } catch (TesseractException e) {<!-- -->
            System.err.println(e.getMessage());
        }
    }
}

```

#### 代码实现需要注意的事项
-  tessdata 语言包资源，把官方github项目下下来就有语言包了。语言包名字就是文件名去掉后缀。 -  tessdata路径 如果是相对路径或者使用程序默认路径，需要配置环境变量TESSDATA_PREFIX，配置到tessdata文件的上级目录地址就可以了(windows系统)。 建议使用绝对路径做测试，反正不好用。 