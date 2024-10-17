
--- 
title:  Unity IK 反向动力学 学习笔记 
tags: []
categories: [] 

---
**目录**







### Unity IK 反向动力学

“**IK是Inverse Kinematic的缩写，也就是反向动力学。是根据骨骼的终节点来推算其他父节点的位置的一种方法。比如通过手的位置推算手腕、胳膊肘的骨骼的位置。**”

适用的场景：**比如角色需要拿各种不同的东西，让角色的手能符合各种不同的东西的握持位置，这样就不用针对每种不同的东西单独制作动画了！**”

**其他的用途其实还有比如：角色的头的旋转，这样可以和你视角的方向一致。角色的脚的位置，这样可以让角色踩在地面跟贴合。**” “对对对，我只想到手了。那还有其他的么？” “**Unity中IK能设置的部位就是5个，分别是：头、左右手、左右脚。**所以没有其他部位的IK了，我们常见的其实也都是这些。”



参考：



### ik 示例代码：



Fabrik 是一种是现实逆向动力学 IK （Inverse Knematics）的迭代算法，迭代次数越多效果越好。逆向动力学一般可以用来实现骨骼动画。这里就以实现骨骼动画为例来说明。

每次迭代都包括一次正向迭代和反向迭代。

正向迭代是指从骨骼的控制点开始，以控制点的位置不变，并以他为基准，其他点进行移动；反向迭代则是使骨骼根部的位置为初始位置不变，其他点以他为基准进行移动。这样进行了一次迭代后所有点即向控制点进行了移动又保持的根骨骼的位置不变，从而实现了 IK 的效果。

算法描述：

1.记录根节点的初始位置、控制点位置以及各点之间的距离。

2.正向迭代：把末端节点设置到控制点位置。末端节点的前一节点向末端节点移动到距离为初始记录的距离，如此向后类推到根节点。

3.反向迭代：把根节点设置到根节点初始位置。根节点的后一节点向根节点移动到距离为初始记录的距离，如此向前类推到末端节点。

4.完成设点的迭代次数后，更新节点位置。

**示例代码：**

```
 public class FabrikIK : MonoBehaviour
{
        public bool applyIK;

        public Transform ikPos;

        public Transform[] controlPoints;

        public Transform[] limbs;

        public int iterateTimes = 1;

        private List&lt;float&gt; _dists;

        private int _lastPointIndex;

        private Vector3 _rootPos;

        private int _interatedTimes = 0;

        private void Start()
        {
            _dists = new List&lt;float&gt;();

            _rootPos = controlPoints[0].position;

            _lastPointIndex = controlPoints.Length - 1;
            
            //记录初始位置
            for (int i = 1; i &lt; controlPoints.Length; i++)
            {
                float dist = Vector3.Distance(controlPoints[i].position, controlPoints[i - 1].position);
                _dists.Add(dist);
            }
        }

        private void LateUpdate()
        {
            if (applyIK)
            {
                _interatedTimes = 0;
                while (_interatedTimes &lt; iterateTimes)
                {
                    if (Vector3.Distance(controlPoints[_lastPointIndex].position, ikPos.position) &gt; 0.1f)
                    {
                        ForwadIteration();
                        BackwardIteration();
                        LimbsUpdate();
                    }
                    _interatedTimes++;
                }
            }
        }

        //正向迭代
        private void ForwadIteration()
        {
            controlPoints[_lastPointIndex].position = ikPos.position;//从控制点开始

            for (int i = _lastPointIndex - 1; i &gt;= 0; i--)
            {
                Vector3 dir = (controlPoints[i].position - controlPoints[i + 1].position).normalized;
                controlPoints[i].position = controlPoints[i + 1].position + dir * _dists[i];
            }
        }
        
        //反向迭代
        private void BackwardIteration()
        {
            controlPoints[0].position = _rootPos;//从根部开始

            for (int i = 1; i &lt; controlPoints.Length; i++)
            {
                Vector3 dir = (controlPoints[i].position - controlPoints[i - 1].position).normalized;
                controlPoints[i].position = controlPoints[i - 1].position + dir * _dists[i - 1];
            }
        }

        private void LimbsUpdate()
        {
            for (int i = 0; i &lt; limbs.Length; i++)
            {
                if (limbs[i] != null)
                {
                    Vector3 mid = Vector3.Lerp(controlPoints[i].position, controlPoints[i + 1].position, .5f);
                    Vector3 dir = (controlPoints[i + 1].position - controlPoints[i].position).normalized;
                    limbs[i].position = mid;
                    limbs[i].right = dir;
                }
            }
        }

#if UNITY_EDITOR
        private void OnDrawGizmos()
        {
            if (controlPoints != null &amp;&amp; controlPoints.Length &gt; 0)
            {
                Gizmos.color = Color.blue;

                for (int i = 0; i &lt; controlPoints.Length; i++)
                {
                    if (controlPoints[i] != null)
                    {
                        Gizmos.DrawSphere(controlPoints[i].position, 0.2f);
                    }
                }
            }
        }
#endif
}
```

 
