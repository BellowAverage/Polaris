
--- 
title:  nvidia jetson xavier打开风扇，并设置开机启动 
tags: []
categories: [] 

---
1.打开风扇 英伟达的jetson xavier 或者NX打开风扇都是通过修改下面的文件实现的。

vim /sys/devices/pwm-fan/target_pwm 或者直接

sudo sh -c "echo 200 &gt; /sys/devices/pwm-fan/target_pwm" 但是修改上述文件的时候，重启之后失效，因此可以通过设置开启自启动的方式使风扇的设置重启继续生效，下面简单说一下步骤（专门开风扇）。 2.设置开机自动生效

1.在/usr/bin/（目录可随便找）下创建mirror-fan文件夹，创建mirror-fan.sh文件（开风扇脚本）

 set -x set -e

filepath="/sys/devices/pwm-fan/target_pwm" echo 0 &gt; ${filepath}

sleep 5

echo 200 &gt; ${filepath} exit 0

2.在/lib/systemd/system/目录下创建mirror-fan.service

[Unit] Description=Mirror fan

[Service] User=root Type=simple ExecStart=/bin/bash /usr/bin/mirror-fan/mirror-fan.sh

[Install] WantedBy=multi-user.target

 3.在任意一个命令窗口输入sudo systemctl enable mirror-fan.service 4.sudo reboot   #重启
