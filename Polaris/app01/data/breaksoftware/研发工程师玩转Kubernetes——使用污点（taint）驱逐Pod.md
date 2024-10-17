
--- 
title:  研发工程师玩转Kubernetes——使用污点（taint）驱逐Pod 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - - 


在中，有一次Pod被分配到Master Node——UbuntuA上。进一步的实验需要我们关闭其所在的Node，而Master Node又不能关闭，否则我们将无法对Kubernetes进行操作。这个时候我只能使用Pod调度技法来将其从Master Node上驱逐。

## preferredDuringSchedulingIgnoredDuringExecution优先调度

因为实验要求Pod可以运行在任意Node上，所以不能指定它必须运行在哪些Node上。我们需要使用具有优先级的字段preferredDuringSchedulingIgnoredDuringExecution来描述Pod对Node的亲和性。

### 查看Node的Labels

```
kubectl get nodes --show-labels

```

```
NAME      STATUS   ROLES    AGE   VERSION   LABELS
ubuntua   Ready    &lt;none&gt;   15h   v1.27.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntua,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-controlplane=microk8s-controlplane
ubuntuc   Ready    &lt;none&gt;   15h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntuc,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntud   Ready    &lt;none&gt;   15h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntud,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntub   Ready    &lt;none&gt;   15h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntub,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker
ubuntue   Ready    &lt;none&gt;   15h   v1.26.4   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=ubuntue,kubernetes.io/os=linux,microk8s.io/cluster=true,node.kubernetes.io/microk8s-worker=microk8s-worker

```

可以看到只有Master Node（UbuntuA）的Labels含有node.kubernetes.io/microk8s-controlplane=microk8s-controlplane，我们就用这个去做条件选择。

### 清单文件

Node（nodeAffinity）的亲和性（affinity）有两套调度方案：
- requiredDuringSchedulingIgnoredDuringExecution： 调度器**只有在规则被满足**的时候才能执行调度。此功能类似于nodeSelector（详见）， 但其语法表达能力更强。- preferredDuringSchedulingIgnoredDuringExecution： 调度器会**尝试**寻找满足对应规则的节点。如果找不到匹配的节点，调度器仍然会调度该 Pod。 因为后续我们要求Pod可以被调度到其他Node上，所以更好的方法是选择带权重的preferredDuringSchedulingIgnoredDuringExecution，而不是“必须满足规则”的requiredDuringSchedulingIgnoredDuringExecution。
```
# nginx_deployment.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            preference:
              matchExpressions:
              - key: node.kubernetes.io/microk8s-controlplane
                operator: In
                values:
                - microk8s-controlplane
      containers:
      - name: nginx-container
        image: nginx
        ports:
        - containerPort: 80

```

preferredDuringSchedulingIgnoredDuringExecution的具体结构见：

```
type Affinity struct {<!-- -->
	NodeAffinity *NodeAffinity `json:"nodeAffinity,omitempty"`
}

type NodeAffinity struct {<!-- -->
	// If the affinity requirements specified by this field are not met at
	// scheduling time, the pod will not be scheduled onto the node.
	// If the affinity requirements specified by this field cease to be met
	// at some point during pod execution (e.g. due to a node label update),
	// the system will try to eventually evict the pod from its node.
	RequiredDuringSchedulingRequiredDuringExecution *NodeSelector  `json:"requiredDuringSchedulingRequiredDuringExecution,omitempty"`
	// If the affinity requirements specified by this field are not met at
	// scheduling time, the pod will not be scheduled onto the node.
	// If the affinity requirements specified by this field cease to be met
	// at some point during pod execution (e.g. due to a node label update),
	// the system may or may not try to eventually evict the pod from its node.
	RequiredDuringSchedulingIgnoredDuringExecution  *NodeSelector  `json:"requiredDuringSchedulingIgnoredDuringExecution,omitempty"`
	// The scheduler will prefer to schedule pods to nodes that satisfy
	// the affinity expressions specified by this field, but it may choose
	// a node that violates one or more of the expressions. The node that is
	// most preferred is the one with the greatest sum of weights, i.e.
	// for each node that meets all of the scheduling requirements (resource
	// request, RequiredDuringScheduling affinity expressions, etc.),
	// compute a sum by iterating through the elements of this field and adding
	// "weight" to the sum if the node matches the corresponding MatchExpressions; the
	// node(s) with the highest sum are the most preferred.
	PreferredDuringSchedulingIgnoredDuringExecution []PreferredSchedulingTerm  `json:"preferredDuringSchedulingIgnoredDuringExecution,omitempty"`
}

// An empty preferred scheduling term matches all objects with implicit weight 0
// (i.e. it's a no-op). A null preferred scheduling term matches no objects.
type PreferredSchedulingTerm struct {<!-- -->
    // weight is in the range 1-100
	Weight int  `json:"weight"`
	// matchExpressions is a list of node selector requirements. The requirements are ANDed.
	MatchExpressions []NodeSelectorRequirement  `json:"matchExpressions,omitempty"`
}

// A node selector requirement is a selector that contains values, a key, and an operator
// that relates the key and values.
type NodeSelectorRequirement struct {<!-- -->
	// key is the label key that the selector applies to.
	Key string `json:"key" patchStrategy:"merge" patchMergeKey:"key"`
	// operator represents a key's relationship to a set of values.
	// Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
	Operator NodeSelectorOperator `json:"operator"`
	// values is an array of string values. If the operator is In or NotIn,
	// the values array must be non-empty. If the operator is Exists or DoesNotExist,
	// the values array must be empty. If the operator is Gt or Lt, the values
	// array must have a single element, which will be interpreted as an integer.
    // This array is replaced during a strategic merge patch.
	Values []string `json:"values,omitempty"`
}

// A node selector operator is the set of operators that can be used in
// a node selector requirement.
type NodeSelectorOperator string

const (
	NodeSelectorOpIn           NodeSelectorOperator = "In"
	NodeSelectorOpNotIn        NodeSelectorOperator = "NotIn"
	NodeSelectorOpExists       NodeSelectorOperator = "Exists"
	NodeSelectorOpDoesNotExist NodeSelectorOperator = "DoesNotExist"
	NodeSelectorOpGt           NodeSelectorOperator = "Gt"
	NodeSelectorOpLt           NodeSelectorOperator = "Lt"
)

```

### 部署

针对上述文件部署Pod

```
kubectl create -f nginx_deployment.yaml

```

>  
 deployment.apps/nginx-deployment created 


### 观察变化

```
kubectl get pod --watch -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-55d4bfd4bb-xlvvm   0/1     Pending   0          0s    &lt;none&gt;   &lt;none&gt;   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     Pending   0          0s    &lt;none&gt;   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     ContainerCreating   0          0s    &lt;none&gt;   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     ContainerCreating   0          1s    &lt;none&gt;   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   1/1     Running             0          3s    10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   1/1     Running             0          29s   10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;

```

可以看到Master Node(UbunutA)上创建了Pod。

## 驱逐

因为我们不希望Master Node运行业务的Pod，于是要将其驱逐到其他Worker Node上。 我们只要给Node增加污点（taint）即可。

### Taint

```
kubectl taint node ubuntua node_type=master:NoExecute

```

>  
 node/ubuntua tainted 


上述命令给Master Node（UbuntuA）的污点（taint）新增了一组Key:Value(node_type:master)，该组的作用（effect）是NoExecute。NoExecute会将不能容忍污点的Pod从该Node上驱逐走，而effect另外两个值NoSchedule和PreferNoSchedule则不具备驱逐功能。 （如果需要清除污点，使用kubectl taint node ubuntua node_type=master:NoExecute-，即在之前指令后面加个-号）

### 观察变化

```
kubectl get pod --watch -o wide

```

```
NAME                                READY   STATUS    RESTARTS   AGE   IP       NODE     NOMINATED NODE   READINESS GATES
nginx-deployment-55d4bfd4bb-xlvvm   1/1     Terminating         0          29s   10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-w2pt5   0/1     Pending             0          0s    &lt;none&gt;       ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   1/1     Terminating         0          29s   10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-w2pt5   0/1     ContainerCreating   0          0s    &lt;none&gt;       ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     Terminating         0          29s   &lt;none&gt;       ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     Terminating         0          30s   10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     Terminating         0          30s   10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-xlvvm   0/1     Terminating         0          30s   10.1.94.74   ubuntua   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-w2pt5   0/1     ContainerCreating   0          1s    &lt;none&gt;       ubuntue   &lt;none&gt;           &lt;none&gt;
nginx-deployment-55d4bfd4bb-w2pt5   1/1     Running             0          3s    10.1.226.5   ubuntue   &lt;none&gt;           &lt;none&gt;

```

## 参考资料
- - - 