
--- 
title:  ansible使用yum模块安装rpm包失败 
tags: []
categories: [] 

---
>  
 **今天使用ansible批量部署zabbix-agent，但是总是报错** 


```
[root@zabbix-server ~]# ansible-playbook zabbix_agent.yml -k
SSH password: 

PLAY [webserver] ********************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************
ok: [192.168.20.13]
ok: [192.168.20.12]

TASK [Install zabbix agent - CentOS6] ***********************************************************************************
skipping: [192.168.20.12]
skipping: [192.168.20.13]

TASK [Install zabbix agent - CentOS7] ***********************************************************************************
fatal: [192.168.20.13]: FAILED! =&gt; {"changed": false, "msg": "Failure downloading https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-agent-4.0.0-2.el7.x86_64.rpm, Request failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:618)&gt;"}
fatal: [192.168.20.12]: FAILED! =&gt; {"changed": false, "msg": "Failure downloading https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-agent-4.0.0-2.el7.x86_64.rpm, Request failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:618)&gt;"}

PLAY RECAP **************************************************************************************************************
192.168.20.12              : ok=1    changed=0    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0   
192.168.20.13              : ok=1    changed=0    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0   
```

>  
 **解决方法：将剧本中的rpm源地址的https换成http，就可以了。** 


```
    - name: Install zabbix agent - CentOS7
      yum: name=http://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-agent-4.0.0-2.el7.x86_64.rpm state=present
      when: ansible_distribution == "CentOS" and ansible_distribution_major_version == "7"

```

>  
 **再执行ansible剧本就可以正常安装了。** 


```
[root@zabbix-server ~]# ansible-playbook zabbix_agent.yml -k
SSH password: 

PLAY [webserver] ********************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************
ok: [192.168.20.13]
ok: [192.168.20.12]

TASK [Install zabbix agent - CentOS6] ***********************************************************************************
skipping: [192.168.20.12]
skipping: [192.168.20.13]

TASK [Install zabbix agent - CentOS7] ***********************************************************************************
changed: [192.168.20.12]
changed: [192.168.20.13]

TASK [Copy zabbix agent configuration file] *****************************************************************************
changed: [192.168.20.13]
changed: [192.168.20.12]

TASK [Start zabbix agent] ***********************************************************************************************
changed: [192.168.20.12]
changed: [192.168.20.13]

PLAY RECAP **************************************************************************************************************
192.168.20.12              : ok=4    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
192.168.20.13              : ok=4    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   


```


