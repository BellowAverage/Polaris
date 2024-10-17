
--- 
title:  python3向ftp服务器上传和下载封装（一） 
tags: []
categories: [] 

---
1、

2、

python3向ftp服务器上传和下载封装，源码如下，直接可用：

#### 封装一：

```
# -*- coding: UTF-8 -*-
from ftplib import FTP
import os
import sys
import time
import socket


class MyFTP:
    """ftp自动下载、自动上传脚本，可以递归目录操作"""

    def __init__(self, host, port=21):
        """ 初始化 FTP 客户端
        参数:
             host:ip地址
             port:端口号
        """
        # print(f"__init__()---&gt; host = {host} ,port = {port}")

        self.host = host
        self.port = port
        self.ftp = FTP()
        # 重新设置下编码方式
        self.ftp.encoding = 'gbk'
        self.log_file = open("log.txt", "a")
        self.file_list = []

    def login(self, username, password):
        """ 初始化 FTP 客户端
            参数:
                 username: 用户名
                 password: 密码
            """
        try:
            timeout = 60
            socket.setdefaulttimeout(timeout)
            # 0主动模式 1 #被动模式
            self.ftp.set_pasv(False)
            # 打开调试级别2，显示详细信息
            # self.ftp.set_debuglevel(2)

            self.debug_print(f'开始尝试连接到 {<!-- -->self.host}')
            self.ftp.connect(self.host, self.port)
            self.debug_print(f'成功连接到 {<!-- -->self.host}')

            self.debug_print(f'开始尝试登录到 {<!-- -->self.host}')
            self.ftp.login(username, password)
            self.debug_print(f'成功登录到 {<!-- -->self.host}')

            self.debug_print(self.ftp.welcome)
        except Exception as err:
            self.deal_error(f"FTP 连接或登录失败 ，错误描述为：{<!-- -->err}")
            pass

    def is_same_size(self, local_file, remote_file):
        """判断远程文件和本地文件大小是否一致
           参数:
                local_file: 本地文件
                remote_file: 远程文件
        """
        try:
            remote_file_size = self.ftp.size(remote_file)
        except Exception as err:
            self.debug_print(f"is_same_size() 错误描述为：{<!-- -->err}")
            remote_file_size = -1

        try:
            local_file_size = os.path.getsize(local_file)
        except Exception as err:
            self.debug_print(f"is_same_size() 错误描述为：{<!-- -->err}")
            local_file_size = -1

        self.debug_print(f'local_file_size: {<!-- -->local_file_size}  , remote_file_size: {<!-- -->remote_file_size}')
        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

    def download_file(self, local_file, remote_file):
        """从ftp下载文件
            参数:
                local_file: 本地文件
                remote_file: 远程文件
        """
        self.debug_print(f"download_file()---&gt; local_path = {<!-- -->local_file} ,remote_path = {<!-- -->remote_file}")

        if self.is_same_size(local_file, remote_file):
            self.debug_print('%s 文件大小相同，无需下载' % local_file)
            return
        else:
            try:
                self.debug_print(f'&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;下载文件 {<!-- -->local_file} ... ...')
                buf_size = 1024
                file_handler = open(local_file, 'wb')
                self.ftp.retrbinary(f'RETR {<!-- -->remote_file}', file_handler.write, buf_size)
                file_handler.close()
            except Exception as err:
                self.debug_print('下载文件出错，出现异常：%s ' % err)
                return

    def download_file_tree(self, local_path, remote_path):
        """从远程目录下载多个文件到本地目录
        参数:
            local_path: 本地路径
            remote_path: 远程路径
        """
        print(f"download_file_tree()---&gt;  local_path = {<!-- -->local_path} ,remote_path = {<!-- -->remote_path}")
        try:
            self.ftp.cwd(remote_path)
        except Exception as err:
            self.debug_print(f'远程目录 {<!-- -->remote_path} 不存在，继续...,具体错误描述为：{<!-- -->err}')
            return

        if not os.path.isdir(local_path):
            self.debug_print(f'本地目录 {<!-- -->local_path} 不存在，先创建本地目录')
            os.makedirs(local_path)

        self.debug_print(f'切换至目录: {<!-- -->self.ftp.pwd()}')

        self.file_list = []
        # 方法回调
        self.ftp.dir(self.get_file_list)

        remote_names = self.file_list
        self.debug_print('远程目录 列表: %s' % remote_names)
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_path, file_name)
            if file_type == 'd':
                print(f"download_file_tree()---&gt; 下载目录： {<!-- -->file_name}")
                self.download_file_tree(local, file_name)
            elif file_type == '-':
                print(f"download_file()---&gt; 下载文件： {<!-- -->file_name}")
                self.download_file(local, file_name)
            self.ftp.cwd("..")
            self.debug_print(f'返回上层目录 {<!-- -->self.ftp.pwd()}')
        return True

    def upload_file(self, local_file, remote_file):
        """从本地上传文件到ftp
           参数:
             local_path: 本地文件
             remote_path: 远程文件
        """
        if not os.path.isfile(local_file):
            self.debug_print('%s 不存在' % local_file)
            return

        if self.is_same_size(local_file, remote_file):
            self.debug_print('跳过相等的文件: %s' % local_file)
            return

        buf_size = 1024
        file_handler = open(local_file, 'rb')
        self.ftp.storbinary('STOR %s' % remote_file, file_handler, buf_size)
        file_handler.close()
        self.debug_print('上传: %s' % local_file + "成功!")

    def upload_file_tree(self, local_path, remote_path):
        """从本地上传目录下多个文件到ftp
           参数:
                local_path: 本地路径
                remote_path: 远程路径
        """
        if not os.path.isdir(local_path):
            self.debug_print('本地目录 %s 不存在' % local_path)
            return

        # 创建服务器目录
        try:
            self.ftp.cwd(remote_path)  # 切换工作路径
        except Exception as e:
            base_dir, part_path = self.ftp.pwd(), remote_path.split('/')
            for p in part_path[1:-1]:
                base_dir = base_dir + p + '/'  # 拼接子目录
                try:
                    self.ftp.cwd(base_dir)  # 切换到子目录, 不存在则异常
                except Exception as e:
                    print(f'INFO: {<!-- -->e}')
                    self.ftp.mkd(base_dir)  # 不存在创建当前子目录
        # self.ftp.cwd(remote_path)
        self.debug_print('切换至远程目录: %s' % self.ftp.pwd())

        local_name_list = os.listdir(local_path)
        self.debug_print('本地目录list: %s' % local_name_list)
        # self.debug_print(f'判断是否有服务器目录: {os.path.isdir()}')

        for local_name in local_name_list:
            src = os.path.join(local_path, local_name)
            print(f"src路径========== {<!-- -->src}")
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(local_name)
                except Exception as err:
                    self.debug_print(f"目录已存在 {<!-- -->local_name} ,具体错误描述为：{<!-- -->err}")
                self.debug_print(f"upload_file_tree()---&gt; 上传目录： {<!-- -->local_name}")
                self.debug_print(f"upload_file_tree()---&gt; 上传src目录： {<!-- -->src}")
                self.upload_file_tree(src, local_name)
            else:
                self.debug_print(f"upload_file_tree()---&gt; 上传文件： {<!-- -->local_name}")
                self.upload_file(src, local_name)
        self.ftp.cwd("..")

    def close(self):
        """ 退出ftp"""
        self.debug_print("close()---&gt; FTP退出")
        self.ftp.quit()
        self.log_file.close()

    def debug_print(self, s):
        """ 打印日志"""
        self.write_log(s)

    def deal_error(self, e):
        """ 处理错误异常
            参数：
                e：异常
        """
        log_str = f'发生错误: {<!-- -->e}'
        self.write_log(log_str)
        sys.exit()

    def write_log(self, log_str):
        """ 记录日志
            参数：
                log_str：日志
        """
        time_now = time.localtime()
        date_now = time.strftime('%Y-%m-%d', time_now)
        format_log_str = f"{<!-- -->date_now} ---&gt; {<!-- -->log_str} \n "
        print(format_log_str)
        self.log_file.write(format_log_str)

    def get_file_list(self, line):
        """ 获取文件列表
            参数：
                line：
        """
        file_arr = self.get_file_name(line)
        # 去除  . 和  ..
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    def get_file_name(self, line):
        """ 获取文件名
            参数：
                line：
        """
        pos = line.rfind(':')
        while line[pos] != ' ':
            pos += 1
        while line[pos] == ' ':
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr


if __name__ == "__main__":
    my_ftp = MyFTP("192.168.20.97")
    # my_ftp.set_pasv(False)
    my_ftp.login("ftpuser", "12345678")

    # 下载单个文件
    # FTP服务器目录   本地目录
    # my_ftp.download_file("/home/demo.mp4", "/demo.mp4")

    # 下载目录
    # my_ftp.download_file_tree("G:/ftp_test/", "App/AutoUpload/zhangsan/12/")

    # 上传单个文件
    # my_ftp.upload_file("D:/ftp_test/demo.apk", "/App/AutoUpload/XTCLauncher.apk")

    # 上传目录
    my_ftp.upload_file_tree("/home/java8", "/1234/5/")

    my_ftp.close()


```

#### 第二个封装：

```
# -*- coding: utf-8 -*-
from ftplib import FTP
from logging import Logger


class LinkFTP:
    """
    连接 FTP 服务器
    """
    def __init__(self, host: str, port: int, username: str, password: str):
        ftp_ = FTP()
        # 连接
        ftp_.connect(host, port)
        # 登录
        ftp_.login(username, password)
        Logger.info(f"{<!-- -->host} {<!-- -->port} {<!-- -->username} {<!-- -->password} 连接成功")
        self.ftp = ftp_
        self.buffer_size = 2048

    def download_file(self, remote_path: str, local_path: str) -&gt; None:
        """
        从 ftp 下载文件
        :param remote_path: 远程服务器的目录绝对路径
        :param local_path:
        :return:
        """
        with open(local_path, 'wb') as fp:
            self.ftp.retrbinary('RETR ' + remote_path, fp.write, self.buffer_size)
            self.ftp.set_debuglevel(0)

    def upload_file(self, remote_path: str, local_path: str) -&gt; None:
        """
        从本地上传文件到 ftp
        :param remote_path: 远程服务器的目录绝对路径
        :param local_path:
        :return:
        """
        with open(local_path, 'rb') as fp:
            self.ftp.storbinary('STOR ' + remote_path, fp, self.buffer_size)
            self.ftp.set_debuglevel(0)

    def path_list(self, path: str) -&gt; list:
        """
        获取路径信息
        :param path: 路径
        :return:
        """
        # 获取 ftp
        ftp = self.ftp
        # 切换路径
        ftp.cwd(path)
        # 显示目录下所有目录信息
        ftp.dir()
        # 获取目录下的文件夹
        dir_list: list = ftp.nlst()
        # 排序
        dir_list.sort()
        return dir_list

```
