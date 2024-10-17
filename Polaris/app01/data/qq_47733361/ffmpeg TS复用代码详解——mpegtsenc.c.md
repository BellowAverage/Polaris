
--- 
title:  ffmpeg TS复用代码详解——mpegtsenc.c 
tags: []
categories: [] 

---
### 一、mpegtsenc.c 整体架构

<img src="https://img-blog.csdnimg.cn/direct/c4f64536d0fc4277ab5eedafe270f363.png" alt="在这里插入图片描述">

### 二、主要函数

```
mpegts_write_pes(AVFormatContext *s, AVStream *st, const uint8_t *payload, int payload_size, int64_t pts, int64_t dts)

```

这个函数就是TS打包的主函数了，这个函数主要功能就是把一帧数据拆分成188字节的TS包，并加入PTS，DTS同步信息，这个函数封装的对象是一帧视频或者音频数据，payload，payload_size分别是数据和大小。

PTS，DTS就是音视频同步时间戳，时间戳其实就是一次采样的颗粒(简单理解就是数据)，以视频来举例，视频同步时钟90K hz（27M/300），如果帧率是25fps的话，一帧数据采样时间40ms，那么时间戳就是90K x 40ms = 3600（估算值）。

```
static void mpegts_write_pes(AVFormatContext *s, AVStream *st,
                             const uint8_t *payload, int payload_size,
                             int64_t pts, int64_t dts, int key)
{<!-- -->   
........
    while (payload_size &gt; 0) {<!-- -->
        retransmit_si_info(s, force_pat);   //评估是否需要插入PAT、PMT
        force_pat = 0;

        write_pcr = 0;
        if (ts_st-&gt;pid == ts_st-&gt;service-&gt;pcr_pid) {<!-- -->    //评估pes中是否需要插入PCR，一个PCR周期
            if (ts-&gt;mux_rate &gt; 1 || is_start) // VBR pcr period is based on frames
                ts_st-&gt;service-&gt;pcr_packet_count++;
            if (ts_st-&gt;service-&gt;pcr_packet_count &gt;=
                ts_st-&gt;service-&gt;pcr_packet_period) {<!-- -->
                ts_st-&gt;service-&gt;pcr_packet_count = 0;
                write_pcr = 1;
            }
        }
		
		// 若dts-pcr&gt;delay 则需要插入空包，但此时也需要插入pcr则优先插入pcr
        if (ts-&gt;mux_rate &gt; 1 &amp;&amp; dts != AV_NOPTS_VALUE &amp;&amp;
            (dts - get_pcr(ts, s-&gt;pb)/300) &gt; delay) {<!-- -->   //CBR考虑(插入pcr_only或null_packet)
            /* pcr insert gets priority over null packet insert */
            if (write_pcr)
                mpegts_insert_pcr_only(s, st);
            else
                mpegts_insert_null_packet(s);
            continue; /* recalculate write_pcr and possibly retransmit si_info */
        }

		// 写入TS包头
        /* prepare packet header */
        q = buf;
        *q++ = 0x47;
        val = (ts_st-&gt;pid &gt;&gt; 8);
        if (is_start)
            val |= 0x40;    //payload_unit_start_indicator
        *q++ = val;
        *q++ = ts_st-&gt;pid;
        ts_st-&gt;cc = (ts_st-&gt;cc + 1) &amp; 0xf;  //continuity_counter
        *q++ = 0x10 | ts_st-&gt;cc; // payload indicator + CC
        /*********写入adaptation_field(如果需要) *********/
        if (key &amp;&amp; is_start &amp;&amp; pts != AV_NOPTS_VALUE) {<!-- --> // 是否需要写入PCR
            if (ts_st-&gt;pid == ts_st-&gt;service-&gt;pcr_pid)
                write_pcr = 1;
            set_af_flag(buf, 0x40); //set Random Access for key frames
            q = get_ts_payload_start(buf);
        }
        if (write_pcr) {<!-- --> // 写入PCR
            set_af_flag(buf, 0x10); //PCR_flag
            q = get_ts_payload_start(buf);
            // add 11, pcr references the last byte of program clock reference base
            if (ts-&gt;mux_rate &gt; 1)
                pcr = get_pcr(ts, s-&gt;pb);
            else
                pcr = (dts - delay)*300;
            if (dts != AV_NOPTS_VALUE &amp;&amp; dts &lt; pcr / 300)
                av_log(s, AV_LOG_WARNING, "dts &lt; pcr, TS is invalid\n");
            extend_af(buf, write_pcr_bits(q, pcr)); //写入pcr
            q = get_ts_payload_start(buf);
        }
        /*********写入payload*********/
        if (is_start) {<!-- -->
            int pes_extension = 0;
            int pes_header_stuffing_bytes = 0;
            /* write PES header */
            *q++ = 0x00;
            *q++ = 0x00;
            *q++ = 0x01;
            is_dvb_subtitle = 0;
            is_dvb_teletext = 0;
            /* 写入stream_id */
            if (st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_VIDEO) {<!-- -->
                if (st-&gt;codec-&gt;codec_id == AV_CODEC_ID_DIRAC) {<!-- -->
                    *q++ = 0xfd;
                } else
                    *q++ = 0xe0;    //video stream
            } else if (st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_AUDIO &amp;&amp;
                       (st-&gt;codec-&gt;codec_id == AV_CODEC_ID_MP2 ||
                        st-&gt;codec-&gt;codec_id == AV_CODEC_ID_MP3 ||
                        st-&gt;codec-&gt;codec_id == AV_CODEC_ID_AAC)) {<!-- -->
                *q++ = 0xc0;
            } else if (st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_AUDIO &amp;&amp;
                        st-&gt;codec-&gt;codec_id == AV_CODEC_ID_AC3 &amp;&amp;
                        ts-&gt;m2ts_mode) {<!-- -->
                *q++ = 0xfd;
            } else {<!-- -->
                *q++ = 0xbd;
                if(st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_SUBTITLE) {<!-- -->
                    if (st-&gt;codec-&gt;codec_id == AV_CODEC_ID_DVB_SUBTITLE) {<!-- -->
                        is_dvb_subtitle = 1;
                    } else if (st-&gt;codec-&gt;codec_id == AV_CODEC_ID_DVB_TELETEXT) {<!-- -->
                        is_dvb_teletext = 1;
                    }
                }
            }
            header_len = 0;
            flags = 0;
            /* 处理PTS_DTS_flags */
            if (pts != AV_NOPTS_VALUE) {<!-- -->
                header_len += 5;
                flags |= 0x80;
            }
            if (dts != AV_NOPTS_VALUE &amp;&amp; pts != AV_NOPTS_VALUE &amp;&amp; dts != pts) {<!-- -->
                header_len += 5;
                flags |= 0x40;
            }
........
            len = payload_size + header_len + 3;
            /* 3 extra bytes should be added to DVB subtitle payload: 0x20 0x00 at the beginning and trailing 0xff */
            if (is_dvb_subtitle) {<!-- -->
                len += 3;
                payload_size++;
            }
            if (len &gt; 0xffff)
                len = 0;
            if (ts-&gt;omit_video_pes_length &amp;&amp; st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_VIDEO) {<!-- -->
                len = 0;
            }
            *q++ = len &gt;&gt; 8;    //PES_packet_length
            *q++ = len;
            val = 0x80; //'10'
            /* data alignment indicator is required for subtitle and data streams */
            if (st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_SUBTITLE || st-&gt;codec-&gt;codec_type == AVMEDIA_TYPE_DATA)
                val |= 0x04;
            *q++ = val;
            *q++ = flags;
            *q++ = header_len;  //PES_header_data_length
            if (pts != AV_NOPTS_VALUE) {<!-- -->
                write_pts(q, flags &gt;&gt; 6, pts);  //写入pts
                q += 5;
            }
            if (dts != AV_NOPTS_VALUE &amp;&amp; pts != AV_NOPTS_VALUE &amp;&amp; dts != pts) {<!-- -->
                write_pts(q, 1, dts);   //写入dts
                q += 5;
            }
........
        /* 处理完header，下面开始处理数据 */
        /* header size */
        header_len = q - buf;
        /* data len */
        len = TS_PACKET_SIZE - header_len;
        if (len &gt; payload_size) //pes包太大，一个ts包发不完，就得拆包。
            len = payload_size;
        stuffing_len = TS_PACKET_SIZE - header_len - len;   //相反，如果太小，就加入填充。
        if (stuffing_len &gt; 0) {<!-- -->
            /* add stuffing with AFC */     //
            if (buf[3] &amp; 0x20) {<!-- -->
                /* stuffing already present: increase its size */
                afc_len = buf[4] + 1;
                memmove(buf + 4 + afc_len + stuffing_len,
                        buf + 4 + afc_len,
                        header_len - (4 + afc_len));
                buf[4] += stuffing_len;
                memset(buf + 4 + afc_len, 0xff, stuffing_len);
            } else {<!-- -->
                /* add stuffing */
                memmove(buf + 4 + stuffing_len, buf + 4, header_len - 4);
                buf[3] |= 0x20;
                buf[4] = stuffing_len - 1;
                if (stuffing_len &gt;= 2) {<!-- -->
                    buf[5] = 0x00;
                    memset(buf + 6, 0xff, stuffing_len - 2);
                }
            }
        }

        if (is_dvb_subtitle &amp;&amp; payload_size == len) {<!-- -->
            memcpy(buf + TS_PACKET_SIZE - len, payload, len - 1);
            buf[TS_PACKET_SIZE - 1] = 0xff; /* end_of_PES_data_field_marker: an 8-bit field with fixed contents 0xff for DVB subtitle */
        } else {<!-- -->
            memcpy(buf + TS_PACKET_SIZE - len, payload, len);   //写入payload数据
        }

        payload += len;
        payload_size -= len;
        mpegts_prefix_m2ts_header(s);
        avio_write(s-&gt;pb, buf, TS_PACKET_SIZE); //写入avio(缓存到avio_buf中)
    }
    avio_flush(s-&gt;pb);  //把avio_buf的数据写入后端(file/udp等)
    ts_st-&gt;prev_payload_key = key;
}

```

### 三、原理分析

#### 1、ffmpeg TS复用什么时候写入PCR？
- 满足一个PCR周期， ts_st-&gt;service-&gt;pcr_packet_period，会写入一个PCR；PCR周期计算方式：
>  
 (int64_t)ts-&gt;mux_rate * ts-&gt;pcr_period / (TS_PACKET_SIZE * 8 * 1000); 


ts-&gt;pcr_period 默认为20ms；
- 如果当前帧是关键帧，并且当前TS包数据是一帧的开始，pts 值正常，会写入一个PCR；
#### 2、怎样得到一个PCR？

在ffmpeg中，get_pcr() 方法获取一个pcr，代码如下：

```
av_rescale(avio_tell(pb) + 11, 8 * PCR_TIME_BASE, ts-&gt;mux_rate) +
           ts-&gt;first_pcr;

```
<li> first_pcr 和 muxdelay参数有关，默认为0.7，可以通过命令行设置，first_pcr计算方式： <pre><code class="prism language-c"> ts-&gt;first_pcr = av_rescale(s-&gt;max_delay, 27000000, 1000000);
</code></pre> </li>
#### 3、什么时候插入一个空包呢？

可以看下面代码，当 **dts - pcr &gt; delay** 的时候就会插入一个空包，但若此时正好到达一个PCR周期，即需要插入一个PCR了，需要优先插入一个只有PCR的TS包（PID为视频PID）。

```
if (ts-&gt;mux_rate &gt; 1 &amp;&amp; dts != AV_NOPTS_VALUE &amp;&amp;
    (dts - get_pcr(ts, s-&gt;pb)/300) &gt; delay) {<!-- -->   //CBR考虑(插入pcr_only或null_packet)
        /* pcr insert gets priority over null packet insert */
        if (write_pcr)
            mpegts_insert_pcr_only(s, st);
        else
            mpegts_insert_null_packet(s);
        continue; /* recalculate write_pcr and possibly retransmit si_info */
    }

```
