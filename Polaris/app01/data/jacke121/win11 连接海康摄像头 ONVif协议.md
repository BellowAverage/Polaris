
--- 
title:  win11 连接海康摄像头 ONVif协议 
tags: []
categories: [] 

---
**目录**











### Win 11 通过脚本打开自带的IE浏览器访问海康摄像头

第一步、桌面右键新建一个 txt 的文档 

第二步、打开文档并且复制粘贴下面代码

CreateObject("InternetExplorer.Application").Visible=true  第三步、保存并且关闭，修改文件后缀名为 vbs



第四步、双击打开即可。

对您有帮助给我个点赞关注吧！ 原文链接：https://blog.csdn.net/weixin_46091775/article/details/125496631

### 海康摄像头设置支持onvif协议

2、其次，单击上面菜单上的配置，然后单击网络-高级配置，如下图所示，然后进入下一步。





3、接着，在“集成协议”中选中“启用onivif”，然后单击“添加”，如下图所示，然后进入下一步。





4、然后，在弹出的小窗口中，创建一个帐户名和密码，检查管理员，然后确认，如下图所示，然后进入下一步。　





### 安装onvif协议

pip install --upgrade onvif_zeep



### onvif协议示例代码

```
import time

import requests
import zeep
from onvif import ONVIFCamera
from requests.auth import HTTPDigestAuth


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


class Onvif_hik(object):

    def __init__(self, ip: str, username: str, password: str):
        self.ip = ip
        self.username = username
        self.password = password
        self.save_path = "./{}T{}.jpg".format(self.ip, str(time.time()))  # 截图保存路径
        self.content_cam()

    def content_cam(self):
        """
        链接相机地址
        :return:
        """
        try:
            self.mycam = ONVIFCamera(self.ip, 80, self.username, self.password)
            self.media = self.mycam.create_media_service()  # 创建媒体服务
            # 得到目标概要文件
            zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue
            self.media_profile = self.media.GetProfiles()[0]  # 获取配置信息
            self.ptz = self.mycam.create_ptz_service()  # 创建控制台服务
            return True
        except Exception as e:
            return False

    def Snapshot(self):
        """
        截图
        :return:
        """
        res = self.media.GetSnapshotUri({'ProfileToken': self.media_profile.token})

        response = requests.get(res.Uri, auth=HTTPDigestAuth(self.username, self.password))
        with open(self.save_path, 'wb') as f:  # 保存截图
            f.write(response.content)

    def get_presets(self):
        """
        获取预置点列表
        :return:预置点列表--所有的预置点
        """
        presets = self.ptz.GetPresets({'ProfileToken': self.media_profile.token})  # 获取所有预置点,返回值：list
        return presets

    def goto_preset(self, presets_token: int):
        """
        移动到指定预置点
        :param presets_token: 目的位置的token，获取预置点返回值中
        :return:
        """
        try:
            # self.ptz.GotoPreset(
            #     {'ProfileToken': self.media_profile.token, "PresetToken": presets_token})  # 移动到指定预置点位置
            params = self.ptz.create_type('GotoPreset')
            params.ProfileToken = self.media_profile.token
            params.PresetToken = presets_token
            self.ptz.GotoPreset(params)
        except Exception as e:
            print(e)

    def zoom(self, zoom: str, timeout: int = 1):
        """
        变焦
        :param zoom: 1为拉近或-1为远离 
        :param timeout: 生效时间
        :return:
        """
        request = self.ptz.create_type('ContinuousMove')
        request.ProfileToken = self.media_profile.token
        request.Velocity = {"Zoom": zoom}
        self.ptz.ContinuousMove(request)
        time.sleep(timeout)
        self.ptz.Stop({'ProfileToken': request.ProfileToken})

    def get_status(self):
        """
        获取当前预置点的信息
        :return:
        """
        params = self.ptz.create_type('GetStatus')
        params.ProfileToken = self.media_profile.token
        res = self.ptz.GetStatus(params)
        # print(res)
        return res


if __name__ == '__main__':
    o = Onvif_hik(ip="192.168.0.1", username="admin", password="password")
    o.goto_preset(3)

```



感谢博主：


