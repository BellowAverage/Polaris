
--- 
title:  小程序uniapp播放录音，uni.createInnerAudioContext（）苹果手机播放报错，安卓手机可以正常播放问题解决 
tags: []
categories: [] 

---
**解决思路：经过测试发现虽然苹果手机uni.createInnerAudioContext() api播放不了，会进入错误监听里面。但是uni.getBackgroundAudioManager()背景音乐播放在苹果手机上播放是正常的。所以我们采取能正常录音播放的就用uni.createInnerAudioContext()音频播放组件，如果播放进入createInnerAudioContext的错误监听事件，就使用uni.getBackgroundAudioManager()背景音乐播放组件。（因为苹果手机使用uni.createInnerAudioContext()是一进入页面就会报错，甚至还没点。所以一进入页面我们就可以知道是用createInnerAudioContext还是getBackgroundAudioManager）**

以下是封装的组件：

```
&lt;template&gt;
  &lt;!-- 音频播放器组件 --&gt;
  &lt;view v-if='url'
        class='flex justify-between align-center audio'&gt;
    &lt;view class='mr-3'
          @click='start(audioId)'&gt;
      &lt;image src='@/static/daily-supervision/play.png'
             class='icon'
             v-show='!status'&gt;&lt;/image&gt;
      &lt;image src='@/static/daily-supervision/pause.png'
             class='icon'
             v-show='status'&gt;&lt;/image&gt;
    &lt;/view&gt;
    &lt;view class='flex-1'&gt;
      &lt;slider @change='changeAudio'
              :activeColor='activeColor'
              :min='0'
              :max='duration ? duration.toFixed(0) : "00:00"'
              :value='currentTime.toFixed(0)'
              :step='0.1'&gt;&lt;/slider&gt;
    &lt;/view&gt;
    &lt;!-- &lt;view class='ml-3'&gt;{<!-- -->{<!-- -->getTime(Math.round(currentTime))}}&lt;/view&gt; --&gt;
    &lt;view class='ml-3'&gt;{<!-- -->{<!-- -->getTime(Math.round(totalDuration))}}&lt;/view&gt;
  &lt;/view&gt;
&lt;/template&gt;

&lt;script&gt;
export default {<!-- -->
  data() {<!-- -->
    return {<!-- -->
      context: null,
      currentTime: 0,
      duration: 100,
      status: false,
      totalDuration: 0,
      bgAudioManager: null,
      useBackgroundAudioManager: false,
      flag: true
    };
  },
  props: {<!-- -->
    url: String,
    activeColor: {<!-- -->
      type: String,
      default: '#0E7EFC'
    },
    // startPic: String,
    // endPic: String,
    audioId: [String,Number]
  },
  created() {<!-- -->
    this.bgAudioManager = uni.getBackgroundAudioManager();
    this.context = uni.createInnerAudioContext();
    this.context.src = this.url;
    // uni.createInnerAudioContext事件听
    this.onTimeUpdate();
    this.onCanplay();
    this.onEnded();
    this.onErrorHandle();

    // uni.getBackgroundAudioManager事件监听
    this.onBgCanplay();
    this.onBgTimeUpdate();
    this.onBgEnded();
    this.onBgStop();

    uni.$on('stop',(id)=&gt; {<!-- -->
      if(id &amp;&amp; id != this.audioId) {<!-- -->
        this.context.stop();
        this.status = false;
      } else if(!id){<!-- -->
        this.context.stop();
        this.status = false;
      }
    });

    uni.$on('BackgroundAudioStop',(id)=&gt; {<!-- -->
      if(id &amp;&amp; id != this.audioId) {<!-- -->
        this.bgAudioManager.stop();
        this.status = false;
      } else if(!id){<!-- -->
        this.bgAudioManager.stop();
        this.status = false;
      }
    });

    uni.setInnerAudioOption({<!-- -->  
      obeyMuteSwitch: false  
    });
  },
  methods: {<!-- -->
    /**
     * uni.getBackgroundAudioManager事件监听
     */
    onBgCanplay() {<!-- -->
      this.bgAudioManager.onCanplay(() =&gt; {<!-- -->
        setTimeout(()=&gt;{<!-- -->
          this.duration = this.bgAudioManager.duration;
          this.totalDuration = this.bgAudioManager.duration;
          console.log(this.duration, this.totalDuration);
        },1000);
      });
    },
    onBgTimeUpdate() {<!-- -->
      console.log('onBgTimeUpdate');
      this.bgAudioManager.onTimeUpdate(() =&gt; {<!-- -->
        console.log('onTimeUpdate');
        if (!Number.isFinite(this.bgAudioManager.duration)) {<!-- -->
          this.duration = this.bgAudioManager.currentTime + 10;
          this.currentTime = this.bgAudioManager.currentTime;
        } else {<!-- -->
          this.duration = this.bgAudioManager.duration;
          this.currentTime = this.bgAudioManager.currentTime;
        }
      });
    },
    onBgEnded() {<!-- -->
      this.bgAudioManager.onEnded(() =&gt; {<!-- -->
        this.status = false;
        this.currentTime = 0;
        this.flag = true;
        console.log('onBgEnded');
      });
    },
    onBgStop() {<!-- -->
      this.bgAudioManager.onStop(() =&gt; {<!-- -->
        this.status = false;
        this.currentTime = 0;
        this.flag = true;
        console.log('onBgStop');
      });
    },
    /**
     * uni.createInnerAudioContext事件听
     */
    start(id) {<!-- --> //点击播放
      let audioId = id;
      if (this.useBackgroundAudioManager) {<!-- -->
        console.log(this.bgAudioManager.src);
        if (this.flag) {<!-- -->
          this.bgAudioManager.src = this.url;
          this.flag = false;
        }
        this.duration = this.bgAudioManager.duration;
        console.log(21222, this.duration);
        if(this.status) {<!-- -->
          this.bgAudioManager.pause();
          this.status = !this.status;
        }else {<!-- -->
          // uni.$emit('BackgroundAudioStop',id);
          this.bgAudioManager.play();
          this.status = !this.status;
        }
        return;
      }
      if(this.status) {<!-- -->
        this.context.pause();
        this.status = !this.status;
      }else {<!-- -->
        uni.$emit('stop',id);
        this.context.play();
        this.status = !this.status;
      }
    },
    onCanplay() {<!-- --> //进入可播放状态
      this.context.onCanplay(() =&gt; {<!-- -->
        this.context.duration;
        setTimeout(()=&gt;{<!-- -->
          this.duration = this.context.duration;
          this.totalDuration = this.context.duration;
        },1000);
      });
    },
    onTimeUpdate() {<!-- --> //音频播放进度
      this.context.onTimeUpdate(() =&gt; {<!-- -->
        console.log('onTimeUpdate');
        if (!Number.isFinite(this.context.duration)) {<!-- -->
          this.duration = this.context.currentTime + 10;
          this.currentTime = this.context.currentTime;
        } else {<!-- -->
          this.duration = this.context.duration;
          this.currentTime = this.context.currentTime;
        }
      });
    },
    onEnded() {<!-- --> //播放结束
      this.context.onEnded(()=&gt; {<!-- -->
        this.status = false;
        this.currentTime = 0;
      });
    },
    onErrorHandle() {<!-- -->
      this.context.onError((res) =&gt; {<!-- -->
        console.log(res.errMsg);
        console.log(res.errCode);
        this.useBackgroundAudioManager = true;
        this.bgAudioManager.title = '报告回听';
        console.log('bgAudioManager.duration', this.bgAudioManager.duration);
      });
    },
    changeAudio(e) {<!-- -->
      // let paused = this.context.paused;
      // this.context.pause();
      // this.context.seek(e.detail.value);
      // if(!paused) {<!-- -->
      //   this.context.play();
      // } 
    },
    getTime(time) {<!-- -->
      let m = parseInt(time / 60);
      let s = time % 60;
      return this.towNum(m) + ':' + this.towNum(s);
    },
    towNum(num) {<!-- -->
      if(num &gt;= 10) {<!-- -->
        return num;
      }else {<!-- -->
        return '0' + num;
      }
    }
  }
};
&lt;/script&gt;

&lt;style&gt;
.audio {<!-- -->
  background: #f4f4f4;
  padding: 20rpx;
}

.icon {<!-- -->
  width: 60rpx;
  height: 60rpx;
}

.flex {<!-- -->
  display: flex;
  flex-direction: row;
}

.justify-between {<!-- -->
  justify-content: between;
}

.align-center {<!-- -->
  align-items: center;
}

.flex-1 {<!-- -->
  flex: 1;
}

.ml-3 {<!-- -->
  margin-left: 30rpx;
}

.mr-3 {<!-- -->
  margin-right: 30rpx;
}
&lt;/style&gt;


```

使用

```
          &lt;UniAudio :audioId='item.id'
                    :url="audioUrl"&gt;&lt;/UniAudio&gt;

```
