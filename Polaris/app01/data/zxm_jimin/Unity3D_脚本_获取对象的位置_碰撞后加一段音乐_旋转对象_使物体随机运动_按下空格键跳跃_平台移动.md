
--- 
title:  Unity3D_脚本_获取对象的位置_碰撞后加一段音乐_旋转对象_使物体随机运动_按下空格键跳跃_平台移动 
tags: []
categories: [] 

---


#### Unity3D一些技巧
- - - - - - - 


## 获取对象的位置（Position）

<img src="https://img-blog.csdnimg.cn/2019051721153099." alt="在这里插入图片描述"> 在代码中加上

```
public Rigidbody cd;
cd = GetComponent&lt;Rigidbody&gt;();
Vector3 m=cd.transform.position;

```

m[0]为x轴世界坐标 m[1]为y轴世界坐标 m[2]为z轴世界坐标

## 碰撞后加一段音乐

<img src="https://img-blog.csdnimg.cn/20190517211502287.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sound : MonoBehaviour
{

    //播放音乐
    public AudioClip[] bg_sounds;
	private AudioSource audio_source;
 
	void Awake ()
	{
		audio_source = GetComponent&lt;AudioSource&gt; ();
		audio_source.volume = 1;
		audio_source.clip = bg_sounds [0];
        audio_source.Play();
	}
	
	// Update is called once per frame
	void Update ()
	{


	}
    void OnCollisionEnter(Collision collison)
    {
        audio_source.clip = bg_sounds[1];
        audio_source.Play();
        Application.LoadLevel("endGame");
    }
}

```

## 旋转对象

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(15, 30, 45) * Time.deltaTime);
    }
}

```

## 使物体随机运动

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rend : MonoBehaviour {
    public float speed;
 
    private float moveSpeed=4;//移动速度.

    void Start () {
        //设置初始位置.
    transform.position=new Vector3(5,0,0);
    }
    // Update is called once per frame
    void Update () {
        if(transform.position.x&gt;-22){
             //移动.
             transform.Translate(Vector3.right*-moveSpeed*Time.deltaTime);
         }
        else{
            transform.position=new Vector3(5,0,0);
        }
    }
}

```

## 按下空格键跳跃

```
if (Input.GetKeyDown(KeyCode.Space)) //按下空格就跳跃
        {
            cd.AddForce(JumpSpeed * Vector3.up);
        }

```

## 平台移动

```
PlatformController.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// 来回移动平台的控制
public class PlatformController : MonoBehaviour
{

    [Tooltip("平台移动的结束位置")]
    public Vector3 stopPosiiton;
    [Tooltip("平台移动一次的时间")]
    public float moveTime = 1f;
    [Tooltip("平台到边界后的停留时间")]
    public float stayTime = 1f;

    private bool toStop = false; 		// 是否朝结束位置移动
    private float speed;				// 移动的速度
    private Vector3 startPostion;		// 开始位置

    internal bool on = true;			// 平台移动开关，是否允许平台移动
    void Start()
    {
        startPostion = transform.position;
        speed = Vector3.Distance(transform.position, stopPosiiton) / moveTime;
    }
    void Update()
    {
        PlatformMoveOn(on);
    }

 
    /// 平台移动控制
    void PlatformMoveOn(bool on)
    {
        if (!on) { return; }
        StartCoroutine(PlatformMove(stopPosiiton));
    }

  
    /// 具体平台移动控制
    IEnumerator PlatformMove(Vector3 stopPosiiton)
    {
        Vector3 tempPosition = transform.position;
        if (toStop)
        {
            tempPosition = Vector3.MoveTowards(tempPosition, stopPosiiton, speed * Time.deltaTime);
            transform.position = tempPosition;
            if (transform.position == stopPosiiton)
            {
                yield return new WaitForSeconds(stayTime);
                toStop = false;
            }
        }
        else if (!toStop)
        {
            tempPosition = Vector3.MoveTowards(tempPosition, startPostion, speed * Time.deltaTime);
            transform.position = tempPosition;
            if (transform.position == startPostion)
            {
                yield return new WaitForSeconds(stayTime);
                toStop = true;
            }
        }
    }

    // 相对运动
    void OnTriggerEnter(Collider other)
    {
        other.transform.SetParent(transform);
    }
    void OnTriggerExit(Collider other)
    {
        other.transform.SetParent(null);
    }

    // 便于调试
    void OnDrawGizmosSelected()
    {
        Gizmos.color = Color.red;
        //Gizmos.DrawWireCube(stopPosiiton, transform.GetChild(0).localScale);
    }
}

```

## 重力感应（手机设备）

```
 Vector3 dir = Vector3.zero;
        dir.x = Input.acceleration.x;
        dir.z = Input.acceleration.y;
        if (dir.sqrMagnitude &gt; 1)//向量规范化
        {
            dir.Normalize();
        }
        dir *= Time.deltaTime;
        this.transform.GetComponent&lt;Rigidbody&gt;().AddForce(dir * speed, ForceMode.Impulse);

```

出处有的找不到了，如果侵权，请留言。
