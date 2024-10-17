
--- 
title:  kubernates dashboard管理界面安装及管理员用户配置 
tags: []
categories: [] 

---
**目录**













#### 1、执行以下命令安装 `kubernetes-dashboard` ：

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.3/aio/deploy/recommended.yaml
```

安装效果如下：

```
[root@etcd01 kubernates]# kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.3/aio/deploy/recommended.yaml
namespace/kubernetes-dashboard created
serviceaccount/kubernetes-dashboard created
service/kubernetes-dashboard created
secret/kubernetes-dashboard-certs created
secret/kubernetes-dashboard-csrf created
secret/kubernetes-dashboard-key-holder created
configmap/kubernetes-dashboard-settings created
role.rbac.authorization.k8s.io/kubernetes-dashboard created
clusterrole.rbac.authorization.k8s.io/kubernetes-dashboard created
rolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
clusterrolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
deployment.apps/kubernetes-dashboard created
service/dashboard-metrics-scraper created
deployment.apps/dashboard-metrics-scraper created
```

#### 2、使用 kubectl get service --all-namespaces 查看，成功创建

```
[root@etcd01 kubernates]# kubectl get service --all-namespaces
NAMESPACE              NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.96.0.1       &lt;none&gt;        443/TCP                  13d
kube-system            kube-dns                    ClusterIP   10.96.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   13d
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.98.214.124   &lt;none&gt;        8000/TCP                 52s
kubernetes-dashboard   kubernetes-dashboard        ClusterIP   10.106.132.40   &lt;none&gt;        443/TCP                  52s
```

#### 3、配置dashboard为nodeport类型，便于访问

 查看所有pod

```
[root@etcd01 kubernates]# kubectl get pods --all-namespaces
NAMESPACE              NAME                                         READY   STATUS             RESTARTS   AGE
default                test-k8s-7bcd8f88dd-4nhlh                    1/1     Running            0          30m
default                test-k8s-7bcd8f88dd-h7wqd                    1/1     Running            0          30m
default                test-k8s-7bcd8f88dd-snlhd                    1/1     Running            0          30m
kube-system            coredns-54d67798b7-6q9md                     1/1     Running            0          13d
kube-system            etcd-etcd01                                  1/1     Running            0          13d
kube-system            kube-apiserver-etcd01                        1/1     Running            0          13d
kube-system            kube-controller-manager-etcd01               1/1     Running            0          13d
kube-system            kube-proxy-vkh5d                             1/1     Running            0          13d
kube-system            kube-scheduler-etcd01                        1/1     Running            0          13d
kube-system            storage-provisioner                          0/1     ImagePullBackOff   0          13d
kubernetes-dashboard   dashboard-metrics-scraper-7b59f7d4df-2llpp   1/1     Running            0          26m
kubernetes-dashboard   kubernetes-dashboard-5dbf55bd9d-2jzt9        1/1     Running            0          26m
```

#### 4、修改nodeport类型

```
kubectl edit services -n kubernetes-dashboard kubernetes-dashboard
```

```
     42   name: kubernetes-dashboard
     43   namespace: kubernetes-dashboard
     44   resourceVersion: "10695"
     45   uid: dc5b4165-433e-4c30-a9ce-989135a0542e
     46 spec:
     47   clusterIP: 10.106.132.40
     48   clusterIPs:
     49   - 10.106.132.40
     50   externalTrafficPolicy: Cluster
     51   ports:
     52   - nodePort: 31059
     53     port: 443
     54     protocol: TCP
     55     targetPort: 8443
     56   selector:
     57     k8s-app: kubernetes-dashboard
     58   sessionAffinity: None
     59   type: NodePort
     60 status:
     61   loadBalancer: {}
```

#### 5、 再次使用kubectl -n kubernetes-dashboard get service kubernetes-dashboard 查看服务，已成功修改。

```
[root@etcd01 kubernates]# kubectl get service --all-namespaces                              
NAMESPACE              NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.96.0.1       &lt;none&gt;        443/TCP                  13d
kube-system            kube-dns                    ClusterIP   10.96.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   13d
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.98.214.124   &lt;none&gt;        8000/TCP                 29m
kubernetes-dashboard   kubernetes-dashboard        NodePort    10.106.132.40   &lt;none&gt;        443:31059/TCP            29m
```

使用nodeport端口访问

 

<img alt="" height="291" src="https://img-blog.csdnimg.cn/91588c85b36b4d92a5afc5802a218c1a.png" width="716">

1、创建admin-user账号 用于登录 kubernetes dashboard ，默认账号没有管理权限

```
[root@etcd01 kubernates]# cat dashboard-adminuser.yaml 
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
```

2、创建登录用户

```
[root@lanweihong k8s]# kubectl apply -f dashboard-adminuser.yaml
serviceaccount/admin-user created
clusterrolebinding.rbac.authorization.k8s.io/admin-user created
```

3、查看用户列表

```
[root@etcd01 kubernates]# kubectl get serviceaccounts -n kubernetes-dashboard
NAME                   SECRETS   AGE
admin-user             1         15m
default                1         32m
kubernetes-dashboard   1         32m
```

4、查看账号token

```
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
```

5、使用token登录界面

<img alt="" height="572" src="https://img-blog.csdnimg.cn/15ebb9cbdb3c434e88cc07cc3c024eec.png" width="1200">

 
