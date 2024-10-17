
--- 
title:  小程序pdf预览 以及 pdf（文件）下载 
tags: []
categories: [] 

---
### 一、PDF的预览

#### 1、web-view方式

```
  &lt;web-view class="webview"
            :src="url"&gt;&lt;/web-view&gt;

```

#### 2、wx.openDocument（）api实现查看pdf

```
  public clickHandle(): void {<!-- -->
    wx.showLoading({<!-- -->
      title: "下载中",
    });
    wx.downloadFile({<!-- -->
      url: "https://ts-file.aegis-info.com/file/2022-08-30/236e8b1b919843bc9b027b75487c8cd6.pdf", //仅为示例，并非真实的资源
      success(res) {<!-- -->
        // 只要服务器有响应数据，就会把响应内容写入文件并进入 success 回调，业务需要自行判断是否下载到了想要的内容
        if (res.statusCode === 200) {<!-- -->
          const fileManager = wx.getFileSystemManager();
          fileManager.saveFile({<!-- -->
            tempFilePath: res.tempFilePath,
            success: (res) =&gt; {<!-- -->
              console.log(res, "下载成功");
              wx.hideLoading();
              wx.openDocument({<!-- -->
                filePath: res.savedFilePath,
                showMenu: true,
              });
            },
          });
        }
      },
    });
  }

```

### 二、文件下载

wx.downloadFile（）只是将文件下载到临时路径里 wx.getFileSystemManager().saveFile(）说是说将文件下载到本地，但是拿到的路径找不到 **1、经过网上查询找了个比较取巧的方法，就是将文件下载后用wx.openDocument（）打开然后设置showMenu: true属性可以实现分享给微信好友 也就是以上第二点 wx.openDocument（）api实现查看pdf 可以实现**

还有就是有的说： **2、使用wx.downloadFile() 下载对应文件后，使用fileSystemManager.saveFile API保存文件为图片格式;保存成功后，再使用wx.saveImageToPhotosAlbum保存到相册，然后这个时候我们给出弹窗提醒让用户跑到相册文件中找到对应的文件重命名改掉文件格式 这种方式在微信开发者工具上是实现了的，不过在我的iphon上会报错，android机没试**

```
  public clickHandle(): void {<!-- -->
    wx.getSetting({<!-- -->
      success: (res) =&gt; {<!-- -->
        //检查是否有访问相册的权限，如果没有则通过wx.authorize方法授权
        if (!res.authSetting["scope.writePhotosAlbum"]) {<!-- -->
          console.log("没有获取授权");
          wx.authorize({<!-- -->
            scope: "scope.writePhotosAlbum",
            success: (res) =&gt; {<!-- -->
              //用户点击允许获取相册信息后进入下载保存逻辑
              this.save();
            },
          });
        } else {<!-- -->
          console.log("已获取授权");
          this.save();
        }
      },
    });
  }

  public save(): void {<!-- -->
    wx.downloadFile({<!-- -->
      url: "https://ts-file.aegis-info.com/file/2022-08-30/236e8b1b919843bc9b027b75487c8cd6.pdf",
      success(res) {<!-- -->
        console.log(res);
        var savePath = wx.env.USER_DATA_PATH + "/123.jpg";
        wx.getFileSystemManager().saveFile({<!-- -->
          //下载成功后保存到本地
          tempFilePath: res.tempFilePath,
          filePath: savePath,
          success(res2) {<!-- -->
            //获取了相册的访问权限，使用 wx.saveImageToPhotosAlbum 将图片保存到相册中
            wx.saveImageToPhotosAlbum({<!-- -->
              filePath: res2.savedFilePath,
              success: (res) =&gt; {<!-- -->
                //保存成功弹出提示，告知一下用户
                wx.showModal({<!-- -->
                  title: "文件已保存到手机相册",
                  content: "将保存的文件重命名改后缀即可",
                  confirmColor: "#0bc183",
                  confirmText: "知道了",
                  showCancel: false,
                });
              },
              fail(res) {<!-- -->
                console.log(res);
              },
            });
          },

          fail(res) {<!-- -->
            console.log(res);
          },
        });
      },

      fail(res) {<!-- -->
        console.log(res);
      },
    });
  }

```

以上两种方法其实都没有实现直接下载到本地，如果后面有新的方法会再补充，有知道好的方法的大佬也请多多指教呀~
