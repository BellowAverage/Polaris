
--- 
title:  解决 kubernetes 重启报错的问题 
tags: []
categories: [] 

---
参考了 

由于意外突发情况，公司服务器断电关机，重启服务器后发现k8s集群起不来，有几台node节点状态是NotReady，下面展示一下吧！

```
kubectl get pods --all-namespaces
显示:
The connection to the server 192.168.37.201:6443 was refused - did you specify the right host or port?
```

```
[root@k8s-node1 ~]# systemctl status kubelet
● kubelet.service - kubelet: The Kubernetes Node Agent
   Loaded: loaded (/etc/systemd/system/kubelet.service; enabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/kubelet.service.d
           └─10-kubeadm.conf
   Active: activating (auto-restart) (Result: exit-code) since Wed 2019-01-30 10:26:33 CST; 8s ago
     Docs: https://kubernetes.io/docs/
  Process: 9648 ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS (code=exited, status=255)
 Main PID: 9648 (code=exited, status=255)

Jan 30 10:26:33 k8s-node1 systemd[1]: Unit kubelet.service entered failed state.
Jan 30 10:26:33 k8s-node1 systemd[1]: kubelet.service failed.
```

这里报错显示的不明显，接下来通过这个查看：

```
通过 journalctl -xefu kubelet 看到了

-- The start-up result is done.
Jan 30 10:27:34 k8s-node1 kubelet[9831]: Flag --cgroup-driver has been deprecated, This parameter should be set via the config file specified by the Kubelet's --config flag. See https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ for more information.
Jan 30 10:27:34 k8s-node1 kubelet[9831]: Flag --cgroup-driver has been deprecated, This parameter should be set via the config file specified by the Kubelet's --config flag. See https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ for more information.
Jan 30 10:27:34 k8s-node1 kubelet[9831]: I0130 10:27:34.877299    9831 server.go:407] Version: v1.13.2
Jan 30 10:27:34 k8s-node1 kubelet[9831]: I0130 10:27:34.877538    9831 plugins.go:103] No cloud provider specified.
Jan 30 10:27:34 k8s-node1 kubelet[9831]: I0130 10:27:34.892361    9831 certificate_store.go:130] Loading cert/key pair from "/var/lib/kubelet/pki/kubelet-client-current.pem".
Jan 30 10:27:34 k8s-node1 kubelet[9831]: I0130 10:27:34.926248    9831 server.go:666] --cgroups-per-qos enabled, but --cgroup-root was not specified.  defaulting to /
Jan 30 10:27:34 k8s-node1 kubelet[9831]: F0130 10:27:34.926665    9831 server.go:261] failed to run Kubelet: Running with swap on is not supported, please disable swap! or set --fail-swap-on flag to false. /proc/swaps contained: [Filename                                Type                Size        Used        Priority /swapfile                               file                2097148        0        -2]
Jan 30 10:27:34 k8s-node1 systemd[1]: kubelet.service: main process exited, code=exited, status=255/n/a
Jan 30 10:27:34 k8s-node1 systemd[1]: Unit kubelet.service entered failed state.
Jan 30 10:27:34 k8s-node1 systemd[1]: kubelet.service failed.
```

上面就说得很清楚了，是没有禁用 swap 导致的；

找到原因后,解决就快了。

```
[root@k8s-node2 ~]# 关闭 Swap，机器重启后不生效
[root@k8s-node2 ~]# swapoff -a
[root@k8s-node2 ~]# cp -p /etc/fstab /etc/fstab.bak$(date '+%Y%m%d%H%M%S')
[root@k8s-node2 ~]# sed -i "s/\/dev\/mapper\/centos-swap/\#\/dev\/mapper\/centos-swap/g" /etc/fstab

[root@k8s-node2 ~]# systemctl daemon-reload
[root@k8s-node2 ~]# systemctl restart kubelet
```

<img alt="" height="538" src="https://img-blog.csdnimg.cn/9e5ca4a5882c49e5ba7b9f6fc0715dc0.png" width="1200">

 




