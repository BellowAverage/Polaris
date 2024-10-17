
--- 
title:  Java实现AES加解密 
tags: []
categories: [] 

---
## 一、需求
- 算法支持16位密钥和32位密钥加密。- 支持CBC、EBC模式- base64、HEX返回值
### 二、实现32位密钥加密

jdk默认只支持16位密钥，如果直接使用32位密钥，报错：

<img alt="" src="https://img-blog.csdnimg.cn/20210406194630565.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjU4OTc1,size_16,color_FFFFFF,t_70">

因此，让算法支持32位密钥加密。需要更新默认jar包：

<img alt="" height="515" src="https://img-blog.csdnimg.cn/84109978c7a14a0c8c2063b54de2b685.png" width="1200">

 jar包下载地址(jdk8)：http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html

或者：



## 三、代码

```
package com.example.zichu.util;

import org.apache.commons.codec.binary.Hex;
import org.apache.commons.lang3.StringUtils;
import org.springframework.util.Base64Utils;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

/**
 * AES加密工具类
 *
 * @author ACGkaka
 * @since 2021-06-18 19:11:03
 */

public class AESUtil {

    /**
     * 日志相关
     */
//    private static final Logger LOGGER = LoggerFactory.getLogger(AESUtil.class);
    /**
     * 编码
     */
    private static final String ENCODING = "UTF-8";
    /**
     * 算法定义
     */
    private static final String AES_ALGORITHM = "AES";
    /**
     * 指定填充方式
     */
    private static final String CIPHER_PADDING = "AES/ECB/PKCS5Padding";
    private static final String CIPHER_CBC_PADDING = "AES/CBC/PKCS5Padding";
    /**
     * 偏移量(CBC中使用，增强加密算法强度)
     */

    /**
     * AES加密
     *
     * @param content 待加密内容
     * @param aesKey  密码
     * @return
     */
    public static String encrypt(String content, String aesKey) {
        if (StringUtils.isBlank(content)) {
            System.out.println("AES encrypt: the content is null!");
            return null;
        }
        //判断秘钥是否为16位
        if (StringUtils.isNotBlank(aesKey) &amp;&amp; aesKey.length() == 16) {
            try {
                //对密码进行编码
                byte[] bytes = aesKey.getBytes(ENCODING);
                //设置加密算法，生成秘钥
                SecretKeySpec skeySpec = new SecretKeySpec(bytes, AES_ALGORITHM);
                // "算法/模式/补码方式"
                Cipher cipher = Cipher.getInstance(CIPHER_PADDING);
                //选择加密
                cipher.init(Cipher.ENCRYPT_MODE, skeySpec);
                //根据待加密内容生成字节数组
                byte[] encrypted = cipher.doFinal(content.getBytes(ENCODING));
                //返回base64字符串
                return Base64Utils.encodeToString(encrypted);
            } catch (Exception e) {
                System.out.println("AES encrypt exception:" + e.getMessage());
                throw new RuntimeException(e);
            }

        } else {
            System.out.println("AES encrypt: the aesKey is null or error!");
            return null;
        }
    }

    /**
     * 解密
     *
     * @param content 待解密内容
     * @param aesKey  密码
     * @return
     */
    public static String decrypt(String content, String aesKey) {
        if (StringUtils.isBlank(content)) {
            System.out.println("AES decrypt: the content is null!");
            return null;
        }
        //判断秘钥是否为16位
        if (StringUtils.isNotBlank(aesKey) &amp;&amp; aesKey.length() == 16) {
            try {
                //对密码进行编码
                byte[] bytes = aesKey.getBytes(ENCODING);
                //设置解密算法，生成秘钥
                SecretKeySpec skeySpec = new SecretKeySpec(bytes, AES_ALGORITHM);
                // "算法/模式/补码方式"
                Cipher cipher = Cipher.getInstance(CIPHER_PADDING);
                //选择解密
                cipher.init(Cipher.DECRYPT_MODE, skeySpec);

                //先进行Base64解码
                byte[] decodeBase64 = Base64Utils.decodeFromString(content);

                //根据待解密内容进行解密
                byte[] decrypted = cipher.doFinal(decodeBase64);
                //将字节数组转成字符串
                return new String(decrypted, ENCODING);
            } catch (Exception e) {
                System.out.println("AES decrypt exception:" + e.getMessage());
                throw new RuntimeException(e);
            }

        } else {
            System.out.println("AES decrypt: the aesKey is null or error!");
            return null;
        }
    }

    /**
     * AES_CBC加密
     *
     * @param content 待加密内容
     * @param aesKey  密码-base64
     * @return
     */
    public static String encryptCBC(String content, String aesKey, String IV_SEED) {
        if (StringUtils.isBlank(content)) {
            System.out.println("AES_CBC encrypt: the content is null!");
            return null;
        }
        //判断秘钥是否为32位
        if (StringUtils.isNotBlank(aesKey) &amp;&amp; aesKey.length() == 32) {
            try {
                //对密码进行编码
                byte[] bytes = aesKey.getBytes(ENCODING);
                //设置加密算法，生成秘钥
                SecretKeySpec skeySpec = new SecretKeySpec(bytes, AES_ALGORITHM);
                // "算法/模式/补码方式"
                Cipher cipher = Cipher.getInstance(CIPHER_CBC_PADDING);
                //偏移
                IvParameterSpec iv = new IvParameterSpec(IV_SEED.getBytes(ENCODING));
                //选择加密
                cipher.init(Cipher.ENCRYPT_MODE, skeySpec, iv);
                //根据待加密内容生成字节数组
                byte[] encrypted = cipher.doFinal(content.getBytes(ENCODING));
                //返回base64字符串
                return Base64Utils.encodeToString(encrypted);
            } catch (Exception e) {
                System.out.println("AES_CBC encrypt exception:" + e.getMessage());
                throw new RuntimeException(e);
            }

        } else {
            System.out.println("AES_CBC encrypt: the aesKey is null or error!");
            return null;
        }
    }

    /**
     * AES_CBC解密
     *
     * @param content 待解密内容
     * @param aesKey  密码
     * @return
     */
    public static String decryptCBC(String content, String aesKey, String IV_SEED) {
        if (StringUtils.isBlank(content)) {
            System.out.println("AES_CBC decrypt: the content is null!");
            return null;
        }
        //判断秘钥是否为32位
        if (StringUtils.isNotBlank(aesKey) &amp;&amp; aesKey.length() == 32) {
            try {
                //对密码进行编码
                byte[] bytes = aesKey.getBytes(ENCODING);
                //设置解密算法，生成秘钥
                SecretKeySpec skeySpec = new SecretKeySpec(bytes, AES_ALGORITHM);
                //偏移
                IvParameterSpec iv = new IvParameterSpec(IV_SEED.getBytes(ENCODING));
                // "算法/模式/补码方式"
                Cipher cipher = Cipher.getInstance(CIPHER_CBC_PADDING);
                //选择解密
                cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv);

                //先进行Base64解码
                byte[] decodeBase64 = Base64Utils.decodeFromString(content);

                //根据待解密内容进行解密
                byte[] decrypted = cipher.doFinal(decodeBase64);
                //将字节数组转成字符串
                return new String(decrypted, ENCODING);
            } catch (Exception e) {
                System.out.println("AES_CBC decrypt exception:" + e.getMessage());
                throw new RuntimeException(e);
            }

        } else {
            System.out.println("AES_CBC decrypt: the aesKey is null or error!");
            return null;
        }
    }


    /**
     * AES_CBC加密
     *
     * @param content 待加密内容
     * @return
     */
    public static String encryptCBC_HEX(String content) {
        if (StringUtils.isBlank(content)) {
            System.out.println("AES_CBC_HEX encrypt: the content is null!");
            return null;
        }
        //判断秘钥是否为16位
        if (StringUtils.isNotBlank(aesKey) &amp;&amp; aesKey.length() == 16) {
            try {
                //对密码进行编码
                byte[] bytes = aesKey.getBytes(ENCODING);
                //设置加密算法，生成秘钥
                SecretKeySpec skeySpec = new SecretKeySpec(bytes, AES_ALGORITHM);
                // "算法/模式/补码方式"
                Cipher cipher = Cipher.getInstance(CIPHER_CBC_PADDING);
                //偏移
                IvParameterSpec iv = new IvParameterSpec(IV_SEED.getBytes(ENCODING));
                //选择加密
                cipher.init(Cipher.ENCRYPT_MODE, skeySpec, iv);
                //根据待加密内容生成字节数组
                byte[] encrypted = cipher.doFinal(content.getBytes(ENCODING));
                String s = Hex.encodeHexString(encrypted);
                //返回
                return s;
            } catch (Exception e) {
                System.out.println("AES_CBC_HEX encrypt exception:" + e.getMessage());
                throw new RuntimeException(e);
            }

        } else {
            System.out.println("AES_CBC_HEX encrypt: the aesKey is null or error!");
            return null;
        }
    }

   
}

```
