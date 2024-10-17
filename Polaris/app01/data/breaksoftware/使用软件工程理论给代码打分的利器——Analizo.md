
--- 
title:  使用软件工程理论给代码打分的利器——Analizo 
tags: []
categories: [] 

---


#### 大纲
- - - - <ul><li>- - - - - - - - - - - - - - - - 


Analizo是一款可以给C、C++、Java以及C#代码进行评分的开源软件。我们可以使用它来分析代码，并得到如下指标的评分
- Afferent Connections per Class (ACC) metric- Average Cyclomatic Complexity per Method (ACCM) metric- Average Method Lines of Code (AMLOC) metric- Average Number of Parameters (ANPM) metric- Coupling Between Objects (CBO) metric- Depth of Inheritance Tree (DIT) metric- Lack of Cohesion of Methods (LCOM4) metric- Lines of Code (LOC) metric- Number of Attributes (NOA) metric- Number of Children (NOC) metric- Number of Methods (NOM) metric- Number of Public Attributes (NPA) metric- Number of Public Methods (NPM) metric- Response for Class (RFC) metric- Structural Complexity (SC) metric
这些评分是我们评价代码质量和可维护性的一种依据。 比如Average Cyclomatic Complexity per Method (ACCM) metric，即平均圈复杂度。这是1976年由Thomas J. McCabe, Sr. 提出来的一种代码复杂度的衡量标准。它的算法也很简单，即

>  
 V(G) = e – n + 2 


其中e是边数量，n是节点数量。 <img src="https://img-blog.csdnimg.cn/direct/52bf013ef7c449fe8a855ba36ae237e7.png" alt="在这里插入图片描述">

比如上图显示，if else逻辑的圈复杂度是4-4+2=2;而switch case则是6-5+2=3。即上图中的switch case的复杂度要高些，这是因为它要处理的分支要多一些。更多的分支意味着逻辑复杂，也意味着程序写的复杂。 其他指标后面会展开说。我们先看看如何使用Analizo分析出这些指标。

## 环境准备

Analizo的安装依赖于perl以及其他相关组件，编译和安装的命令如下。

```
sudo apt update &amp;&amp; sudo apt upgrade -y
sudo apt install perl
sudo apt install doxygen-doxyparse
sudo apt install cpanminus
sudo cpanm File::ShareDir::Install
sudo cpanm FindBin::libs
sudo cpanm App::Cmd::Setup
sudo cpanm Class::Inspector
sudo cpanm Env::Path
sudo cpanm Class::Accessor::Fast
sudo cpanm Graph
sudo cpanm Graph::Writer::Dot
sudo cpanm YAML::XS
sudo cpanm Statistics::Descriptive
sudo cpanm File::HomeDir
sudo cpanm CHI
sudo cpanm File::Copy::Recursive
git clone https://git.launchpad.net/ubuntu/+source/analizo
cd analizo
perl Makefile.PL
make
sudo make install

```

## 分析代码

我们还是分析中的libevent源码。因为build文件夹是在编译过程中产生的，所以我们需要将其排除。（否则有很多中间文件）

```
analizo metrics ../../libevent/ --exclude ../../libevent/build &gt; libevent_matrics.yaml

```

## 整理结果

### 环境准备

我们使用pandas解析上面产生的yaml文件，所以需要安装一些python包。env.sh是中介绍的python虚拟环境管理脚本。

```
source env.sh init
source env.sh enter
source env.sh install pyyaml
source env.sh install pandas
source env.sh install tabulate

```

### 将结果转换成markdown格式

```
import pandas as pd
import yaml
import sys

def yaml2md(yaml_file, md_file):
    li = []
    summary = None
    with open(yaml_file, 'r') as f:
        for g in yaml.safe_load_all(f):
            if "_module" in g:
                li.append(g)
            else:
                summary = pd.json_normalize(yaml.safe_load_all(yaml.safe_dump_all([g])))
    df = pd.json_normalize(yaml.safe_load_all(yaml.safe_dump_all(li)))
    df.set_index("_module", inplace=True)
    column_to_move = df.pop("_filename")
    df.insert(len(df.columns), "name", column_to_move)
    with open(md_file, 'w') as f:
        f.write(df.to_markdown())
    
    
if __name__ == "__main__":
    yaml_path = sys.argv[1]
    md_path = sys.argv[2]
    yaml2md(yaml_path, md_path)

```

## 结果展示

<th align="left">_module</th><th align="right">acc</th><th align="right">accm</th><th align="right">amloc</th><th align="right">anpm</th><th align="right">cbo</th><th align="right">dit</th><th align="right">lcom4</th><th align="right">loc</th><th align="right">mmloc</th><th align="right">noa</th><th align="right">noc</th><th align="right">nom</th><th align="right">npa</th><th align="right">npm</th><th align="right">rfc</th><th align="right">sc</th><th align="left">name</th>
|------
<td align="left">getopt</td><td align="right">5</td><td align="right">8</td><td align="right">40</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">80</td><td align="right">66</td><td align="right">12</td><td align="right">0</td><td align="right">2</td><td align="right">12</td><td align="right">2</td><td align="right">8</td><td align="right">0</td><td align="left">[‘WIN32-Code/getopt.c’, ‘WIN32-Code/getopt.h’]</td>
<td align="left">getopt_long</td><td align="right">0</td><td align="right">5.33333</td><td align="right">49.3333</td><td align="right">3</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">148</td><td align="right">75</td><td align="right">5</td><td align="right">0</td><td align="right">3</td><td align="right">5</td><td align="right">3</td><td align="right">18</td><td align="right">1</td><td align="left">[‘WIN32-Code/getopt_long.c’]</td>
<td align="left">tree</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘WIN32-Code/tree.h’]</td>
<td align="left">arc4random</td><td align="right">1</td><td align="right">2.73333</td><td align="right">16.4</td><td align="right">0.733333</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">246</td><td align="right">40</td><td align="right">8</td><td align="right">0</td><td align="right">15</td><td align="right">8</td><td align="right">15</td><td align="right">61</td><td align="right">0</td><td align="left">[‘arc4random.c’]</td>
<td align="left">buffer</td><td align="right">37</td><td align="right">5.16327</td><td align="right">29.7551</td><td align="right">2.29592</td><td align="right">5</td><td align="right">0</td><td align="right">21</td><td align="right">2916</td><td align="right">133</td><td align="right">11</td><td align="right">0</td><td align="right">98</td><td align="right">11</td><td align="right">98</td><td align="right">605</td><td align="right">105</td><td align="left">[‘buffer.c’, ‘include/event2/buffer.h’]</td>
<td align="left">buffer_iocp</td><td align="right">0</td><td align="right">1.22222</td><td align="right">26.2222</td><td align="right">1.88889</td><td align="right">2</td><td align="right">0</td><td align="right">2</td><td align="right">236</td><td align="right">72</td><td align="right">7</td><td align="right">0</td><td align="right">9</td><td align="right">7</td><td align="right">9</td><td align="right">79</td><td align="right">4</td><td align="left">[‘buffer_iocp.c’]</td>
<td align="left">bufferevent-internal</td><td align="right">9</td><td align="right">3</td><td align="right">9</td><td align="right">3</td><td align="right">2</td><td align="right">0</td><td align="right">1</td><td align="right">9</td><td align="right">9</td><td align="right">57</td><td align="right">0</td><td align="right">1</td><td align="right">57</td><td align="right">1</td><td align="right">9</td><td align="right">2</td><td align="left">[‘bufferevent-internal.h’]</td>
<td align="left">bufferevent</td><td align="right">25</td><td align="right">2.09259</td><td align="right">15.6296</td><td align="right">2.05556</td><td align="right">10</td><td align="right">0</td><td align="right">28</td><td align="right">844</td><td align="right">78</td><td align="right">0</td><td align="right">0</td><td align="right">54</td><td align="right">0</td><td align="right">54</td><td align="right">296</td><td align="right">280</td><td align="left">[‘bufferevent.c’, ‘include/event2/bufferevent.h’]</td>
<td align="left">bufferevent_async</td><td align="right">0</td><td align="right">2.5</td><td align="right">19.4286</td><td align="right">2.03571</td><td align="right">9</td><td align="right">0</td><td align="right">4</td><td align="right">544</td><td align="right">54</td><td align="right">10</td><td align="right">0</td><td align="right">28</td><td align="right">10</td><td align="right">28</td><td align="right">208</td><td align="right">36</td><td align="left">[‘bufferevent_async.c’]</td>
<td align="left">bufferevent_filter</td><td align="right">2</td><td align="right">2.57895</td><td align="right">24</td><td align="right">2.57895</td><td align="right">5</td><td align="right">0</td><td align="right">2</td><td align="right">456</td><td align="right">77</td><td align="right">10</td><td align="right">0</td><td align="right">19</td><td align="right">10</td><td align="right">19</td><td align="right">113</td><td align="right">10</td><td align="left">[‘bufferevent_filter.c’]</td>
<td align="left">bufferevent_mbedtls</td><td align="right">3</td><td align="right">2</td><td align="right">10</td><td align="right">1.75862</td><td align="right">8</td><td align="right">0</td><td align="right">15</td><td align="right">290</td><td align="right">50</td><td align="right">3</td><td align="right">0</td><td align="right">29</td><td align="right">3</td><td align="right">29</td><td align="right">85</td><td align="right">120</td><td align="left">[‘bufferevent_mbedtls.c’]</td>
<td align="left">bufferevent_openssl</td><td align="right">4</td><td align="right">2.82759</td><td align="right">12.7586</td><td align="right">1.86207</td><td align="right">8</td><td align="right">0</td><td align="right">19</td><td align="right">370</td><td align="right">55</td><td align="right">2</td><td align="right">0</td><td align="right">29</td><td align="right">2</td><td align="right">29</td><td align="right">89</td><td align="right">152</td><td align="left">[‘bufferevent_openssl.c’]</td>
<td align="left">bufferevent_pair</td><td align="right">1</td><td align="right">3.28571</td><td align="right">18.8571</td><td align="right">1.85714</td><td align="right">6</td><td align="right">0</td><td align="right">2</td><td align="right">264</td><td align="right">40</td><td align="right">4</td><td align="right">0</td><td align="right">14</td><td align="right">4</td><td align="right">14</td><td align="right">82</td><td align="right">12</td><td align="left">[‘bufferevent_pair.c’]</td>
<td align="left">bufferevent_ratelim</td><td align="right">3</td><td align="right">2.81818</td><td align="right">20.3864</td><td align="right">1.70455</td><td align="right">7</td><td align="right">0</td><td align="right">17</td><td align="right">897</td><td align="right">76</td><td align="right">0</td><td align="right">0</td><td align="right">44</td><td align="right">0</td><td align="right">44</td><td align="right">319</td><td align="right">119</td><td align="left">[‘bufferevent_ratelim.c’]</td>
<td align="left">bufferevent_sock</td><td align="right">15</td><td align="right">5.57143</td><td align="right">26.619</td><td align="right">2.71429</td><td align="right">8</td><td align="right">0</td><td align="right">8</td><td align="right">559</td><td align="right">112</td><td align="right">1</td><td align="right">0</td><td align="right">21</td><td align="right">1</td><td align="right">21</td><td align="right">177</td><td align="right">64</td><td align="left">[‘bufferevent_sock.c’]</td>
<td align="left">bufferevent_ssl</td><td align="right">3</td><td align="right">5.06977</td><td align="right">22.6744</td><td align="right">1.83721</td><td align="right">9</td><td align="right">0</td><td align="right">3</td><td align="right">975</td><td align="right">86</td><td align="right">1</td><td align="right">0</td><td align="right">43</td><td align="right">1</td><td align="right">43</td><td align="right">400</td><td align="right">27</td><td align="left">[‘bufferevent_ssl.c’, ‘include/event2/bufferevent_ssl.h’]</td>
<td align="left">changelist-internal</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">5</td><td align="right">0</td><td align="right">0</td><td align="right">5</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘changelist-internal.h’]</td>
<td align="left">CheckFileOffsetBits</td><td align="right">1</td><td align="right">1</td><td align="right">5</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">5</td><td align="right">5</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">1</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="left">[‘cmake/CheckFileOffsetBits.c’]</td>
<td align="left">queue</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘compat/sys/queue.h’]</td>
<td align="left">defer-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘defer-internal.h’]</td>
<td align="left">epoll_sub</td><td align="right">0</td><td align="right">1.33333</td><td align="right">8.33333</td><td align="right">3</td><td align="right">1</td><td align="right">0</td><td align="right">3</td><td align="right">25</td><td align="right">12</td><td align="right">0</td><td align="right">0</td><td align="right">3</td><td align="right">0</td><td align="right">3</td><td align="right">4</td><td align="right">3</td><td align="left">[‘epoll_sub.c’]</td>
<td align="left">epolltable-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">3</td><td align="right">0</td><td align="right">0</td><td align="right">3</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘epolltable-internal.h’]</td>
<td align="left">evbuffer-internal</td><td align="right">6</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">49</td><td align="right">0</td><td align="right">0</td><td align="right">49</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘evbuffer-internal.h’]</td>
<td align="left">evdns</td><td align="right">6</td><td align="right">5.26087</td><td align="right">27.236</td><td align="right">2.32919</td><td align="right">13</td><td align="right">0</td><td align="right">2</td><td align="right">4385</td><td align="right">202</td><td align="right">158</td><td align="right">0</td><td align="right">161</td><td align="right">158</td><td align="right">161</td><td align="right">1177</td><td align="right">26</td><td align="left">[‘evdns.c’]</td>
<td align="left">event-internal</td><td align="right">13</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">82</td><td align="right">0</td><td align="right">0</td><td align="right">82</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘event-internal.h’]</td>
<td align="left">event</td><td align="right">58</td><td align="right">3.22485</td><td align="right">19.4201</td><td align="right">1.75148</td><td align="right">12</td><td align="right">0</td><td align="right">31</td><td align="right">3282</td><td align="right">170</td><td align="right">11</td><td align="right">0</td><td align="right">169</td><td align="right">11</td><td align="right">169</td><td align="right">989</td><td align="right">372</td><td align="left">[‘event.c’]</td>
<td align="left">event_iocp</td><td align="right">3</td><td align="right">1.76923</td><td align="right">15.3846</td><td align="right">1.76923</td><td align="right">3</td><td align="right">0</td><td align="right">6</td><td align="right">200</td><td align="right">49</td><td align="right">2</td><td align="right">0</td><td align="right">13</td><td align="right">2</td><td align="right">13</td><td align="right">27</td><td align="right">18</td><td align="left">[‘event_iocp.c’]</td>
<td align="left">event_tagging</td><td align="right">4</td><td align="right">2.62069</td><td align="right">12</td><td align="right">2.48276</td><td align="right">2</td><td align="right">0</td><td align="right">3</td><td align="right">348</td><td align="right">46</td><td align="right">0</td><td align="right">0</td><td align="right">29</td><td align="right">0</td><td align="right">29</td><td align="right">92</td><td align="right">6</td><td align="left">[‘event_tagging.c’]</td>
<td align="left">evmap-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘evmap-internal.h’]</td>
<td align="left">evmap</td><td align="right">0</td><td align="right">1.84615</td><td align="right">18.0769</td><td align="right">2.5641</td><td align="right">7</td><td align="right">0</td><td align="right">6</td><td align="right">705</td><td align="right">77</td><td align="right">8</td><td align="right">0</td><td align="right">39</td><td align="right">8</td><td align="right">39</td><td align="right">228</td><td align="right">42</td><td align="left">[‘evmap.c’]</td>
<td align="left">evrpc-internal</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">37</td><td align="right">0</td><td align="right">0</td><td align="right">37</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘evrpc-internal.h’]</td>
<td align="left">evrpc</td><td align="right">1</td><td align="right">3.26087</td><td align="right">20.6304</td><td align="right">2.63043</td><td align="right">10</td><td align="right">0</td><td align="right">14</td><td align="right">949</td><td align="right">57</td><td align="right">0</td><td align="right">0</td><td align="right">46</td><td align="right">0</td><td align="right">46</td><td align="right">297</td><td align="right">140</td><td align="left">[‘evrpc.c’]</td>
<td align="left">evsignal-internal</td><td align="right">4</td><td align="right">1</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">1</td><td align="right">1</td><td align="right">6</td><td align="right">0</td><td align="right">1</td><td align="right">6</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="left">[‘evsignal-internal.h’]</td>
<td align="left">evthread-internal</td><td align="right">0</td><td align="right">2</td><td align="right">11</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">11</td><td align="right">11</td><td align="right">4</td><td align="right">0</td><td align="right">1</td><td align="right">4</td><td align="right">1</td><td align="right">3</td><td align="right">1</td><td align="left">[‘evthread-internal.h’]</td>
<td align="left">evthread</td><td align="right">5</td><td align="right">3.22222</td><td align="right">17</td><td align="right">1.22222</td><td align="right">3</td><td align="right">0</td><td align="right">1</td><td align="right">306</td><td align="right">54</td><td align="right">13</td><td align="right">0</td><td align="right">18</td><td align="right">13</td><td align="right">18</td><td align="right">103</td><td align="right">3</td><td align="left">[‘evthread.c’]</td>
<td align="left">evthread_pthread</td><td align="right">1</td><td align="right">3.09091</td><td align="right">14.6364</td><td align="right">1.36364</td><td align="right">2</td><td align="right">0</td><td align="right">1</td><td align="right">161</td><td align="right">56</td><td align="right">4</td><td align="right">0</td><td align="right">11</td><td align="right">4</td><td align="right">11</td><td align="right">31</td><td align="right">2</td><td align="left">[‘evthread_pthread.c’]</td>
<td align="left">evthread_win32</td><td align="right">5</td><td align="right">2.9</td><td align="right">18</td><td align="right">1.4</td><td align="right">2</td><td align="right">0</td><td align="right">1</td><td align="right">180</td><td align="right">65</td><td align="right">5</td><td align="right">0</td><td align="right">10</td><td align="right">5</td><td align="right">10</td><td align="right">40</td><td align="right">2</td><td align="left">[‘evthread_win32.c’]</td>
<td align="left">evutil</td><td align="right">38</td><td align="right">4.01389</td><td align="right">29.4861</td><td align="right">1.86111</td><td align="right">8</td><td align="right">0</td><td align="right">27</td><td align="right">2123</td><td align="right">189</td><td align="right">17</td><td align="right">0</td><td align="right">72</td><td align="right">17</td><td align="right">72</td><td align="right">214</td><td align="right">216</td><td align="left">[‘evutil.c’]</td>
<td align="left">evutil_rand</td><td align="right">6</td><td align="right">1.125</td><td align="right">6.5</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="right">5</td><td align="right">52</td><td align="right">10</td><td align="right">1</td><td align="right">0</td><td align="right">8</td><td align="right">1</td><td align="right">8</td><td align="right">14</td><td align="right">5</td><td align="left">[‘evutil_rand.c’]</td>
<td align="left">evutil_time</td><td align="right">22</td><td align="right">2.45455</td><td align="right">17.7273</td><td align="right">1.63636</td><td align="right">3</td><td align="right">0</td><td align="right">7</td><td align="right">195</td><td align="right">50</td><td align="right">0</td><td align="right">0</td><td align="right">11</td><td align="right">0</td><td align="right">11</td><td align="right">20</td><td align="right">21</td><td align="left">[‘evutil_time.c’]</td>
<td align="left">ht-internal</td><td align="right">0</td><td align="right">1.5</td><td align="right">11</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">22</td><td align="right">12</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">0</td><td align="right">2</td><td align="right">2</td><td align="right">0</td><td align="left">[‘ht-internal.h’]</td>
<td align="left">http-internal</td><td align="right">4</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">57</td><td align="right">0</td><td align="right">0</td><td align="right">57</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘http-internal.h’]</td>
<td align="left">http</td><td align="right">10</td><td align="right">3.77523</td><td align="right">21.3853</td><td align="right">2.00917</td><td align="right">17</td><td align="right">0</td><td align="right">55</td><td align="right">4662</td><td align="right">264</td><td align="right">23</td><td align="right">0</td><td align="right">218</td><td align="right">23</td><td align="right">218</td><td align="right">1257</td><td align="right">935</td><td align="left">[‘http.c’, ‘include/event2/http.h’]</td>
<td align="left">buffer_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/buffer_compat.h’]</td>
<td align="left">bufferevent_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/bufferevent_compat.h’]</td>
<td align="left">bufferevent_struct</td><td align="right">13</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">15</td><td align="right">0</td><td align="right">0</td><td align="right">15</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/bufferevent_struct.h’]</td>
<td align="left">dns</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/dns.h’]</td>
<td align="left">dns_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/dns_compat.h’]</td>
<td align="left">dns_struct</td><td align="right">4</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">6</td><td align="right">0</td><td align="right">0</td><td align="right">6</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/dns_struct.h’]</td>
<td align="left">event2/event</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/event.h’]</td>
<td align="left">event_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/event_compat.h’]</td>
<td align="left">event_struct</td><td align="right">6</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">32</td><td align="right">0</td><td align="right">0</td><td align="right">32</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/event_struct.h’]</td>
<td align="left">http_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/http_compat.h’]</td>
<td align="left">http_struct</td><td align="right">5</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">34</td><td align="right">0</td><td align="right">0</td><td align="right">34</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/http_struct.h’]</td>
<td align="left">keyvalq_struct</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/keyvalq_struct.h’]</td>
<td align="left">listener</td><td align="right">13</td><td align="right">4.25</td><td align="right">18.875</td><td align="right">2</td><td align="right">5</td><td align="right">0</td><td align="right">1</td><td align="right">302</td><td align="right">77</td><td align="right">18</td><td align="right">0</td><td align="right">16</td><td align="right">18</td><td align="right">16</td><td align="right">96</td><td align="right">5</td><td align="left">[‘include/event2/listener.h’, ‘listener.c’]</td>
<td align="left">rpc</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/rpc.h’]</td>
<td align="left">rpc_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/rpc_compat.h’]</td>
<td align="left">rpc_struct</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">15</td><td align="right">0</td><td align="right">0</td><td align="right">15</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/rpc_struct.h’]</td>
<td align="left">tag</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/tag.h’]</td>
<td align="left">tag_compat</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/tag_compat.h’]</td>
<td align="left">thread</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">11</td><td align="right">0</td><td align="right">0</td><td align="right">11</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/thread.h’]</td>
<td align="left">util</td><td align="right">9</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">8</td><td align="right">0</td><td align="right">0</td><td align="right">8</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/util.h’]</td>
<td align="left">visibility</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘include/event2/visibility.h’]</td>
<td align="left">watch</td><td align="right">2</td><td align="right">1.33333</td><td align="right">7.16667</td><td align="right">2.33333</td><td align="right">3</td><td align="right">0</td><td align="right">4</td><td align="right">43</td><td align="right">14</td><td align="right">0</td><td align="right">0</td><td align="right">6</td><td align="right">0</td><td align="right">6</td><td align="right">24</td><td align="right">12</td><td align="left">[‘include/event2/watch.h’, ‘watch.c’]</td>
<td align="left">ws</td><td align="right">3</td><td align="right">3.35294</td><td align="right">22.2353</td><td align="right">2.58824</td><td align="right">7</td><td align="right">0</td><td align="right">4</td><td align="right">378</td><td align="right">88</td><td align="right">2</td><td align="right">0</td><td align="right">17</td><td align="right">2</td><td align="right">17</td><td align="right">72</td><td align="right">28</td><td align="left">[‘include/event2/ws.h’, ‘ws.c’]</td>
<td align="left">iocp-internal</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘iocp-internal.h’]</td>
<td align="left">ipv6-internal</td><td align="right">8</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">4</td><td align="right">0</td><td align="right">0</td><td align="right">4</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘ipv6-internal.h’]</td>
<td align="left">kqueue-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘kqueue-internal.h’]</td>
<td align="left">log-internal</td><td align="right">23</td><td align="right">1</td><td align="right">1</td><td align="right">2.77778</td><td align="right">0</td><td align="right">0</td><td align="right">9</td><td align="right">9</td><td align="right">1</td><td align="right">2</td><td align="right">0</td><td align="right">9</td><td align="right">2</td><td align="right">9</td><td align="right">9</td><td align="right">0</td><td align="left">[‘log-internal.h’]</td>
<td align="left">log</td><td align="right">5</td><td align="right">1.78571</td><td align="right">10.0714</td><td align="right">2.21429</td><td align="right">1</td><td align="right">0</td><td align="right">2</td><td align="right">141</td><td align="right">26</td><td align="right">3</td><td align="right">0</td><td align="right">14</td><td align="right">3</td><td align="right">14</td><td align="right">33</td><td align="right">2</td><td align="left">[‘log.c’]</td>
<td align="left">minheap-internal</td><td align="right">2</td><td align="right">1.93333</td><td align="right">7.6</td><td align="right">1.66667</td><td align="right">1</td><td align="right">0</td><td align="right">3</td><td align="right">114</td><td align="right">20</td><td align="right">3</td><td align="right">0</td><td align="right">15</td><td align="right">3</td><td align="right">15</td><td align="right">56</td><td align="right">3</td><td align="left">[‘minheap-internal.h’]</td>
<td align="left">mm-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘mm-internal.h’]</td>
<td align="left">openssl-compat</td><td align="right">0</td><td align="right">2</td><td align="right">10</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">10</td><td align="right">10</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="left">[‘openssl-compat.h’]</td>
<td align="left">ratelim-internal</td><td align="right">1</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">9</td><td align="right">0</td><td align="right">0</td><td align="right">9</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘ratelim-internal.h’]</td>
<td align="left">becat</td><td align="right">0</td><td align="right">4.68</td><td align="right">22.28</td><td align="right">2.08</td><td align="right">13</td><td align="right">0</td><td align="right">2</td><td align="right">557</td><td align="right">157</td><td align="right">35</td><td align="right">0</td><td align="right">25</td><td align="right">35</td><td align="right">25</td><td align="right">176</td><td align="right">26</td><td align="left">[‘sample/becat.c’]</td>
<td align="left">dns-example</td><td align="right">0</td><td align="right">7</td><td align="right">35.1667</td><td align="right">2.66667</td><td align="right">7</td><td align="right">0</td><td align="right">1</td><td align="right">211</td><td align="right">111</td><td align="right">1</td><td align="right">0</td><td align="right">6</td><td align="right">1</td><td align="right">6</td><td align="right">49</td><td align="right">7</td><td align="left">[‘sample/dns-example.c’]</td>
<td align="left">event-read-fifo</td><td align="right">0</td><td align="right">4</td><td align="right">40.3333</td><td align="right">2.66667</td><td align="right">3</td><td align="right">0</td><td align="right">1</td><td align="right">121</td><td align="right">77</td><td align="right">0</td><td align="right">0</td><td align="right">3</td><td align="right">0</td><td align="right">3</td><td align="right">19</td><td align="right">3</td><td align="left">[‘sample/event-read-fifo.c’]</td>
<td align="left">hello-world</td><td align="right">0</td><td align="right">2.4</td><td align="right">18.8</td><td align="right">3</td><td align="right">6</td><td align="right">0</td><td align="right">1</td><td align="right">94</td><td align="right">47</td><td align="right">2</td><td align="right">0</td><td align="right">5</td><td align="right">2</td><td align="right">5</td><td align="right">32</td><td align="right">6</td><td align="left">[‘sample/hello-world.c’]</td>
<td align="left">hostcheck</td><td align="right">1</td><td align="right">8.8</td><td align="right">28.2</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">141</td><td align="right">58</td><td align="right">0</td><td align="right">0</td><td align="right">5</td><td align="right">0</td><td align="right">5</td><td align="right">11</td><td align="right">0</td><td align="left">[‘sample/hostcheck.c’, ‘sample/hostcheck.h’]</td>
<td align="left">http-connect</td><td align="right">0</td><td align="right">1.16667</td><td align="right">17.1667</td><td align="right">1.83333</td><td align="right">6</td><td align="right">0</td><td align="right">1</td><td align="right">103</td><td align="right">43</td><td align="right">2</td><td align="right">0</td><td align="right">6</td><td align="right">2</td><td align="right">6</td><td align="right">51</td><td align="right">6</td><td align="left">[‘sample/http-connect.c’]</td>
<td align="left">http-server</td><td align="right">1</td><td align="right">10.875</td><td align="right">57.25</td><td align="right">2</td><td align="right">10</td><td align="right">0</td><td align="right">2</td><td align="right">458</td><td align="right">165</td><td align="right">23</td><td align="right">0</td><td align="right">8</td><td align="right">23</td><td align="right">8</td><td align="right">79</td><td align="right">20</td><td align="left">[‘sample/http-server.c’]</td>
<td align="left">https-client</td><td align="right">0</td><td align="right">15.8333</td><td align="right">89.6667</td><td align="right">1.33333</td><td align="right">10</td><td align="right">0</td><td align="right">1</td><td align="right">538</td><td align="right">409</td><td align="right">3</td><td align="right">0</td><td align="right">6</td><td align="right">3</td><td align="right">6</td><td align="right">57</td><td align="right">10</td><td align="left">[‘sample/https-client.c’]</td>
<td align="left">le-proxy</td><td align="right">0</td><td align="right">5</td><td align="right">36.1429</td><td align="right">2.28571</td><td align="right">7</td><td align="right">0</td><td align="right">1</td><td align="right">253</td><td align="right">102</td><td align="right">6</td><td align="right">0</td><td align="right">7</td><td align="right">6</td><td align="right">7</td><td align="right">61</td><td align="right">7</td><td align="left">[‘sample/le-proxy.c’]</td>
<td align="left">openssl_hostname_validation</td><td align="right">1</td><td align="right">5</td><td align="right">30.6667</td><td align="right">2</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">92</td><td align="right">39</td><td align="right">0</td><td align="right">0</td><td align="right">3</td><td align="right">0</td><td align="right">3</td><td align="right">7</td><td align="right">1</td><td align="left">[‘sample/openssl_hostname_validation.c’, ‘sample/openssl_hostname_validation.h’]</td>
<td align="left">signal-test</td><td align="right">2</td><td align="right">4.5</td><td align="right">24.5</td><td align="right">2.5</td><td align="right">2</td><td align="right">0</td><td align="right">1</td><td align="right">49</td><td align="right">38</td><td align="right">1</td><td align="right">0</td><td align="right">2</td><td align="right">1</td><td align="right">2</td><td align="right">12</td><td align="right">2</td><td align="left">[‘sample/signal-test.c’]</td>
<td align="left">ssl-client-mbedtls</td><td align="right">0</td><td align="right">4</td><td align="right">41.2</td><td align="right">2.4</td><td align="right">7</td><td align="right">0</td><td align="right">1</td><td align="right">206</td><td align="right">159</td><td align="right">0</td><td align="right">0</td><td align="right">5</td><td align="right">0</td><td align="right">5</td><td align="right">27</td><td align="right">7</td><td align="left">[‘sample/ssl-client-mbedtls.c’]</td>
<td align="left">time-test</td><td align="right">0</td><td align="right">1.66667</td><td align="right">26</td><td align="right">2.66667</td><td align="right">5</td><td align="right">0</td><td align="right">1</td><td align="right">78</td><td align="right">48</td><td align="right">2</td><td align="right">0</td><td align="right">3</td><td align="right">2</td><td align="right">3</td><td align="right">25</td><td align="right">5</td><td align="left">[‘sample/time-test.c’]</td>
<td align="left">watch-timing</td><td align="right">0</td><td align="right">3.3</td><td align="right">24.1</td><td align="right">2.2</td><td align="right">3</td><td align="right">0</td><td align="right">1</td><td align="right">241</td><td align="right">84</td><td align="right">15</td><td align="right">0</td><td align="right">10</td><td align="right">15</td><td align="right">10</td><td align="right">72</td><td align="right">3</td><td align="left">[‘sample/watch-timing.c’]</td>
<td align="left">ws-chat-server</td><td align="right">0</td><td align="right">2.1</td><td align="right">17.5</td><td align="right">2.3</td><td align="right">8</td><td align="right">0</td><td align="right">1</td><td align="right">175</td><td align="right">32</td><td align="right">2</td><td align="right">0</td><td align="right">10</td><td align="right">2</td><td align="right">10</td><td align="right">52</td><td align="right">8</td><td align="left">[‘sample/ws-chat-server.c’]</td>
<td align="left">sha1</td><td align="right">1</td><td align="right">2.8</td><td align="right">40.4</td><td align="right">2.2</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">202</td><td align="right">117</td><td align="right">3</td><td align="right">0</td><td align="right">5</td><td align="right">3</td><td align="right">5</td><td align="right">10</td><td align="right">0</td><td align="left">[‘sha1.c’, ‘sha1.h’]</td>
<td align="left">signal</td><td align="right">0</td><td align="right">3</td><td align="right">27.1538</td><td align="right">1.92308</td><td align="right">6</td><td align="right">0</td><td align="right">3</td><td align="right">353</td><td align="right">50</td><td align="right">5</td><td align="right">0</td><td align="right">13</td><td align="right">5</td><td align="right">13</td><td align="right">93</td><td align="right">18</td><td align="left">[‘signal.c’]</td>
<td align="left">signalfd</td><td align="right">0</td><td align="right">4.4</td><td align="right">30.8</td><td align="right">3.2</td><td align="right">6</td><td align="right">0</td><td align="right">2</td><td align="right">154</td><td align="right">86</td><td align="right">1</td><td align="right">0</td><td align="right">5</td><td align="right">1</td><td align="right">5</td><td align="right">33</td><td align="right">12</td><td align="left">[‘signalfd.c’]</td>
<td align="left">ssl-compat</td><td align="right">3</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">38</td><td align="right">0</td><td align="right">0</td><td align="right">38</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘ssl-compat.h’]</td>
<td align="left">strlcpy-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘strlcpy-internal.h’]</td>
<td align="left">strlcpy</td><td align="right">0</td><td align="right">7</td><td align="right">24</td><td align="right">3</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">24</td><td align="right">24</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">1</td><td align="right">0</td><td align="left">[‘strlcpy.c’]</td>
<td align="left">test-export</td><td align="right">0</td><td align="right">1.5</td><td align="right">12.5</td><td align="right">1</td><td align="right">2</td><td align="right">0</td><td align="right">1</td><td align="right">25</td><td align="right">15</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">0</td><td align="right">2</td><td align="right">6</td><td align="right">2</td><td align="left">[‘test-export/test-export.c’]</td>
<td align="left">bench</td><td align="right">0</td><td align="right">9.66667</td><td align="right">51.6667</td><td align="right">1.66667</td><td align="right">4</td><td align="right">0</td><td align="right">1</td><td align="right">155</td><td align="right">93</td><td align="right">10</td><td align="right">0</td><td align="right">3</td><td align="right">10</td><td align="right">3</td><td align="right">42</td><td align="right">4</td><td align="left">[‘test/bench.c’]</td>
<td align="left">bench_cascade</td><td align="right">0</td><td align="right">5.33333</td><td align="right">39.3333</td><td align="right">2</td><td align="right">4</td><td align="right">0</td><td align="right">1</td><td align="right">118</td><td align="right">57</td><td align="right">3</td><td align="right">0</td><td align="right">3</td><td align="right">3</td><td align="right">3</td><td align="right">19</td><td align="right">4</td><td align="left">[‘test/bench_cascade.c’]</td>
<td align="left">bench_http</td><td align="right">0</td><td align="right">8.5</td><td align="right">63.5</td><td align="right">2</td><td align="right">5</td><td align="right">0</td><td align="right">1</td><td align="right">127</td><td align="right">116</td><td align="right">2</td><td align="right">0</td><td align="right">2</td><td align="right">2</td><td align="right">2</td><td align="right">22</td><td align="right">5</td><td align="left">[‘test/bench_http.c’]</td>
<td align="left">bench_httpclient</td><td align="right">52</td><td align="right">3.4</td><td align="right">31.8</td><td align="right">1.6</td><td align="right">6</td><td align="right">0</td><td align="right">1</td><td align="right">159</td><td align="right">63</td><td align="right">12</td><td align="right">0</td><td align="right">5</td><td align="right">12</td><td align="right">5</td><td align="right">49</td><td align="right">6</td><td align="left">[‘test/bench_httpclient.c’]</td>
<td align="left">print-winsock-errors</td><td align="right">0</td><td align="right">4</td><td align="right">74</td><td align="right">2</td><td align="right">3</td><td align="right">0</td><td align="right">1</td><td align="right">74</td><td align="right">74</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">4</td><td align="right">3</td><td align="left">[‘test/print-winsock-errors.c’]</td>
<td align="left">regress</td><td align="right">20</td><td align="right">2.77419</td><td align="right">24.2419</td><td align="right">1.56452</td><td align="right">11</td><td align="right">0</td><td align="right">13</td><td align="right">3006</td><td align="right">142</td><td align="right">76</td><td align="right">0</td><td align="right">124</td><td align="right">76</td><td align="right">124</td><td align="right">825</td><td align="right">143</td><td align="left">[‘test/regress.c’, ‘test/regress.h’]</td>
<td align="left">regress.gen</td><td align="right">0</td><td align="right">1.06557</td><td align="right">16.4918</td><td align="right">1.88525</td><td align="right">2</td><td align="right">0</td><td align="right">61</td><td align="right">1006</td><td align="right">85</td><td align="right">71</td><td align="right">0</td><td align="right">61</td><td align="right">71</td><td align="right">61</td><td align="right">346</td><td align="right">122</td><td align="left">[‘test/regress.gen.c’, ‘test/regress.gen.h’]</td>
<td align="left">regress_buffer</td><td align="right">0</td><td align="right">3.30909</td><td align="right">48.6182</td><td align="right">1.45455</td><td align="right">9</td><td align="right">0</td><td align="right">38</td><td align="right">2674</td><td align="right">240</td><td align="right">15</td><td align="right">0</td><td align="right">55</td><td align="right">15</td><td align="right">55</td><td align="right">485</td><td align="right">342</td><td align="left">[‘test/regress_buffer.c’]</td>
<td align="left">regress_bufferevent</td><td align="right">0</td><td align="right">2.07407</td><td align="right">19.0926</td><td align="right">1.7037</td><td align="right">15</td><td align="right">0</td><td align="right">12</td><td align="right">1031</td><td align="right">99</td><td align="right">16</td><td align="right">0</td><td align="right">54</td><td align="right">16</td><td align="right">54</td><td align="right">317</td><td align="right">180</td><td align="left">[‘test/regress_bufferevent.c’]</td>
<td align="left">regress_dns</td><td align="right">0</td><td align="right">4.39286</td><td align="right">42.8929</td><td align="right">1.75</td><td align="right">15</td><td align="right">0</td><td align="right">12</td><td align="right">2402</td><td align="right">389</td><td align="right">40</td><td align="right">0</td><td align="right">56</td><td align="right">40</td><td align="right">56</td><td align="right">601</td><td align="right">180</td><td align="left">[‘test/regress_dns.c’]</td>
<td align="left">regress_et</td><td align="right">0</td><td align="right">2.28571</td><td align="right">26.4286</td><td align="right">1.85714</td><td align="right">6</td><td align="right">0</td><td align="right">4</td><td align="right">185</td><td align="right">56</td><td align="right">6</td><td align="right">0</td><td align="right">7</td><td align="right">6</td><td align="right">7</td><td align="right">43</td><td align="right">24</td><td align="left">[‘test/regress_et.c’]</td>
<td align="left">regress_finalize</td><td align="right">0</td><td align="right">1.35714</td><td align="right">19.0714</td><td align="right">1.71429</td><td align="right">5</td><td align="right">0</td><td align="right">4</td><td align="right">267</td><td align="right">88</td><td align="right">8</td><td align="right">0</td><td align="right">14</td><td align="right">8</td><td align="right">14</td><td align="right">78</td><td align="right">20</td><td align="left">[‘test/regress_finalize.c’]</td>
<td align="left">regress_http</td><td align="right">1</td><td align="right">3.02186</td><td align="right">28.4536</td><td align="right">1.87978</td><td align="right">21</td><td align="right">0</td><td align="right">7</td><td align="right">5207</td><td align="right">436</td><td align="right">38</td><td align="right">0</td><td align="right">183</td><td align="right">38</td><td align="right">183</td><td align="right">1511</td><td align="right">147</td><td align="left">[‘test/regress_http.c’, ‘test/regress_http.h’]</td>
<td align="left">regress_iocp</td><td align="right">0</td><td align="right">1.75</td><td align="right">20.4167</td><td align="right">1.83333</td><td align="right">4</td><td align="right">0</td><td align="right">3</td><td align="right">245</td><td align="right">57</td><td align="right">12</td><td align="right">0</td><td align="right">12</td><td align="right">12</td><td align="right">12</td><td align="right">76</td><td align="right">12</td><td align="left">[‘test/regress_iocp.c’]</td>
<td align="left">regress_listener</td><td align="right">0</td><td align="right">1.92308</td><td align="right">23.6923</td><td align="right">2.38462</td><td align="right">6</td><td align="right">0</td><td align="right">5</td><td align="right">308</td><td align="right">75</td><td align="right">2</td><td align="right">0</td><td align="right">13</td><td align="right">2</td><td align="right">13</td><td align="right">68</td><td align="right">30</td><td align="left">[‘test/regress_listener.c’]</td>
<td align="left">regress_main</td><td align="right">8</td><td align="right">4</td><td align="right">23.8333</td><td align="right">1.58333</td><td align="right">11</td><td align="right">0</td><td align="right">7</td><td align="right">286</td><td align="right">88</td><td align="right">11</td><td align="right">0</td><td align="right">12</td><td align="right">11</td><td align="right">12</td><td align="right">56</td><td align="right">77</td><td align="left">[‘test/regress_main.c’]</td>
<td align="left">regress_mbedtls</td><td align="right">1</td><td align="right">2.25</td><td align="right">19.75</td><td align="right">1.91667</td><td align="right">3</td><td align="right">0</td><td align="right">2</td><td align="right">237</td><td align="right">67</td><td align="right">6</td><td align="right">0</td><td align="right">12</td><td align="right">6</td><td align="right">12</td><td align="right">41</td><td align="right">6</td><td align="left">[‘test/regress_mbedtls.c’]</td>
<td align="left">regress_minheap</td><td align="right">0</td><td align="right">1.33333</td><td align="right">18.3333</td><td align="right">1</td><td align="right">3</td><td align="right">0</td><td align="right">3</td><td align="right">55</td><td align="right">40</td><td align="right">1</td><td align="right">0</td><td align="right">3</td><td align="right">1</td><td align="right">3</td><td align="right">10</td><td align="right">9</td><td align="left">[‘test/regress_minheap.c’]</td>
<td align="left">regress_openssl</td><td align="right">2</td><td align="right">2.4</td><td align="right">16.8667</td><td align="right">1.4</td><td align="right">2</td><td align="right">0</td><td align="right">2</td><td align="right">253</td><td align="right">40</td><td align="right">5</td><td align="right">0</td><td align="right">15</td><td align="right">5</td><td align="right">15</td><td align="right">41</td><td align="right">4</td><td align="left">[‘test/regress_openssl.c’]</td>
<td align="left">regress_rpc</td><td align="right">0</td><td align="right">4.41667</td><td align="right">32.5</td><td align="right">1.83333</td><td align="right">13</td><td align="right">0</td><td align="right">3</td><td align="right">780</td><td align="right">147</td><td align="right">6</td><td align="right">0</td><td align="right">24</td><td align="right">6</td><td align="right">24</td><td align="right">212</td><td align="right">39</td><td align="left">[‘test/regress_rpc.c’]</td>
<td align="left">regress_ssl</td><td align="right">2</td><td align="right">3.66667</td><td align="right">38.1333</td><td align="right">2.86667</td><td align="right">11</td><td align="right">0</td><td align="right">2</td><td align="right">572</td><td align="right">118</td><td align="right">25</td><td align="right">0</td><td align="right">15</td><td align="right">25</td><td align="right">15</td><td align="right">169</td><td align="right">22</td><td align="left">[‘test/regress_ssl.c’]</td>
<td align="left">regress_testutils</td><td align="right">4</td><td align="right">1.11111</td><td align="right">26.7778</td><td align="right">2.77778</td><td align="right">6</td><td align="right">0</td><td align="right">2</td><td align="right">241</td><td align="right">71</td><td align="right">9</td><td align="right">0</td><td align="right">9</td><td align="right">9</td><td align="right">9</td><td align="right">58</td><td align="right">12</td><td align="left">[‘test/regress_testutils.c’, ‘test/regress_testutils.h’]</td>
<td align="left">regress_thread</td><td align="right">0</td><td align="right">2.82353</td><td align="right">24.8824</td><td align="right">1.88235</td><td align="right">7</td><td align="right">0</td><td align="right">2</td><td align="right">423</td><td align="right">98</td><td align="right">21</td><td align="right">0</td><td align="right">17</td><td align="right">21</td><td align="right">17</td><td align="right">121</td><td align="right">14</td><td align="left">[‘test/regress_thread.c’, ‘test/regress_thread.h’]</td>
<td align="left">regress_timer_timeout</td><td align="right">0</td><td align="right">1.875</td><td align="right">11.875</td><td align="right">1.625</td><td align="right">3</td><td align="right">0</td><td align="right">2</td><td align="right">95</td><td align="right">23</td><td align="right">4</td><td align="right">0</td><td align="right">8</td><td align="right">4</td><td align="right">8</td><td align="right">26</td><td align="right">6</td><td align="left">[‘test/regress_timer_timeout.c’]</td>
<td align="left">regress_util</td><td align="right">1</td><td align="right">3.07143</td><td align="right">33.4762</td><td align="right">1.19048</td><td align="right">10</td><td align="right">0</td><td align="right">31</td><td align="right">1406</td><td align="right">144</td><td align="right">32</td><td align="right">0</td><td align="right">42</td><td align="right">32</td><td align="right">42</td><td align="right">180</td><td align="right">310</td><td align="left">[‘test/regress_util.c’]</td>
<td align="left">regress_watch</td><td align="right">0</td><td align="right">1.1</td><td align="right">15</td><td align="right">2.2</td><td align="right">5</td><td align="right">0</td><td align="right">2</td><td align="right">150</td><td align="right">30</td><td align="right">9</td><td align="right">0</td><td align="right">10</td><td align="right">9</td><td align="right">10</td><td align="right">67</td><td align="right">10</td><td align="left">[‘test/regress_watch.c’]</td>
<td align="left">regress_ws</td><td align="right">1</td><td align="right">4.4</td><td align="right">29.2</td><td align="right">2.6</td><td align="right">7</td><td align="right">0</td><td align="right">2</td><td align="right">292</td><td align="right">59</td><td align="right">1</td><td align="right">0</td><td align="right">10</td><td align="right">1</td><td align="right">10</td><td align="right">63</td><td align="right">14</td><td align="left">[‘test/regress_ws.c’, ‘test/regress_ws.h’]</td>
<td align="left">regress_zlib</td><td align="right">0</td><td align="right">1.66667</td><td align="right">25.5556</td><td align="right">2.33333</td><td align="right">7</td><td align="right">0</td><td align="right">2</td><td align="right">230</td><td align="right">72</td><td align="right">5</td><td align="right">0</td><td align="right">9</td><td align="right">5</td><td align="right">9</td><td align="right">46</td><td align="right">14</td><td align="left">[‘test/regress_zlib.c’]</td>
<td align="left">test-changelist</td><td align="right">0</td><td align="right">2</td><td align="right">25.8</td><td align="right">2.6</td><td align="right">7</td><td align="right">0</td><td align="right">1</td><td align="right">129</td><td align="right">62</td><td align="right">2</td><td align="right">0</td><td align="right">5</td><td align="right">2</td><td align="right">5</td><td align="right">29</td><td align="right">7</td><td align="left">[‘test/test-changelist.c’]</td>
<td align="left">test-closed</td><td align="right">0</td><td align="right">3.5</td><td align="right">27</td><td align="right">2.5</td><td align="right">5</td><td align="right">0</td><td align="right">1</td><td align="right">54</td><td align="right">39</td><td align="right">1</td><td align="right">0</td><td align="right">2</td><td align="right">1</td><td align="right">2</td><td align="right">18</td><td align="right">5</td><td align="left">[‘test/test-closed.c’]</td>
<td align="left">test-dumpevents</td><td align="right">0</td><td align="right">1.75</td><td align="right">31.75</td><td align="right">2.25</td><td align="right">4</td><td align="right">0</td><td align="right">1</td><td align="right">127</td><td align="right">112</td><td align="right">0</td><td align="right">0</td><td align="right">4</td><td align="right">0</td><td align="right">4</td><td align="right">19</td><td align="right">4</td><td align="left">[‘test/test-dumpevents.c’]</td>
<td align="left">test-eof</td><td align="right">13</td><td align="right">4</td><td align="right">29</td><td align="right">2.5</td><td align="right">4</td><td align="right">0</td><td align="right">1</td><td align="right">58</td><td align="right">35</td><td align="right">3</td><td align="right">0</td><td align="right">2</td><td align="right">3</td><td align="right">2</td><td align="right">16</td><td align="right">4</td><td align="left">[‘test/test-eof.c’]</td>
<td align="left">test-fdleak</td><td align="right">0</td><td align="right">2.66667</td><td align="right">16.3333</td><td align="right">2.11111</td><td align="right">6</td><td align="right">0</td><td align="right">1</td><td align="right">147</td><td align="right">43</td><td align="right">2</td><td align="right">0</td><td align="right">9</td><td align="right">2</td><td align="right">9</td><td align="right">56</td><td align="right">6</td><td align="left">[‘test/test-fdleak.c’]</td>
<td align="left">test-init</td><td align="right">0</td><td align="right">1</td><td align="right">16</td><td align="right">2</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">16</td><td align="right">16</td><td align="right">0</td><td align="right">0</td><td align="right">1</td><td align="right">0</td><td align="right">1</td><td align="right">2</td><td align="right">1</td><td align="left">[‘test/test-init.c’]</td>
<td align="left">test-ratelim</td><td align="right">2</td><td align="right">4.75</td><td align="right">31.875</td><td align="right">2.3125</td><td align="right">12</td><td align="right">0</td><td align="right">1</td><td align="right">510</td><td align="right">236</td><td align="right">46</td><td align="right">0</td><td align="right">16</td><td align="right">46</td><td align="right">16</td><td align="right">180</td><td align="right">12</td><td align="left">[‘test/test-ratelim.c’]</td>
<td align="left">test-time</td><td align="right">15</td><td align="right">3</td><td align="right">21.3333</td><td align="right">2</td><td align="right">3</td><td align="right">0</td><td align="right">1</td><td align="right">64</td><td align="right">41</td><td align="right">3</td><td align="right">0</td><td align="right">3</td><td align="right">3</td><td align="right">3</td><td align="right">19</td><td align="right">3</td><td align="left">[‘test/test-time.c’]</td>
<td align="left">test-weof</td><td align="right">0</td><td align="right">3.5</td><td align="right">26</td><td align="right">2.5</td><td align="right">3</td><td align="right">0</td><td align="right">1</td><td align="right">52</td><td align="right">33</td><td align="right">3</td><td align="right">0</td><td align="right">2</td><td align="right">3</td><td align="right">2</td><td align="right">16</td><td align="right">3</td><td align="left">[‘test/test-weof.c’]</td>
<td align="left">tinytest</td><td align="right">5</td><td align="right">5.26667</td><td align="right">30.8</td><td align="right">1.46667</td><td align="right">2</td><td align="right">0</td><td align="right">3</td><td align="right">462</td><td align="right">117</td><td align="right">26</td><td align="right">0</td><td align="right">15</td><td align="right">26</td><td align="right">15</td><td align="right">71</td><td align="right">6</td><td align="left">[‘test/tinytest.c’, ‘test/tinytest.h’]</td>
<td align="left">tinytest_demo</td><td align="right">1</td><td align="right">1.42857</td><td align="right">22</td><td align="right">1.28571</td><td align="right">2</td><td align="right">0</td><td align="right">7</td><td align="right">154</td><td align="right">40</td><td align="right">8</td><td align="right">0</td><td align="right">7</td><td align="right">8</td><td align="right">7</td><td align="right">14</td><td align="right">14</td><td align="left">[‘test/tinytest_demo.c’]</td>
<td align="left">tinytest_local</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘test/tinytest_local.h’]</td>
<td align="left">tinytest_macros</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘test/tinytest_macros.h’]</td>
<td align="left">time-internal</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">2</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘time-internal.h’]</td>
<td align="left">util-internal</td><td align="right">3</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="right">10</td><td align="right">0</td><td align="right">0</td><td align="right">10</td><td align="right">0</td><td align="right">0</td><td align="right">0</td><td align="left">[‘util-internal.h’]</td>
<td align="left">wepoll</td><td align="right">0</td><td align="right">2.47115</td><td align="right">12.625</td><td align="right">1.53846</td><td align="right">2</td><td align="right">0</td><td align="right">3</td><td align="right">1313</td><td align="right">77</td><td align="right">76</td><td align="right">0</td><td align="right">104</td><td align="right">76</td><td align="right">104</td><td align="right">439</td><td align="right">6</td><td align="left">[‘wepoll.c’, ‘wepoll.h’]</td>

## 指标说明

### Afferent Connections per Class (ACC) metric

类连接性指标。它表示类之间的关联程度。**如果关联度越高，值越大，程序越复杂。** 举个例子，如果Ci类访问了Cj类的一个方法或者属性，则 client(Ci, Cj)值为1；否则值为0。代码中所有类（N个）这样的关系值总和即ACC的值。 数据公式是：

>  
 client(Ci, Cj) = 1, if (Ci =&gt; Cj) and (Ci != Cj) client(Ci, Cj) = 0, otherwise. ACC(Cj) = (sum(client(Ci, Cj)), i = 1 to N) 


它是基于这篇论文。 其他参考见
- - 
### Average Cyclomatic Complexity per Method (ACCM) metric

每个函数的圈复杂度指标。**如果值越大，代码越复杂。** 它是计算代码中节点（区块）和边（跳转）之间关系的方法，即

>  
 V(G) = e – n + 2 


其中e表示边的数量，n表示节点的数量。 比如下面的代码在逻辑上是相同的，但是写法不同

```
void foo(void) {<!-- -->
    if (a &amp;&amp; b)
        x=1;
    else
        x=2;
}

```

```
void foo(void) {<!-- -->
    if (a)
        if (b) 
            x=1;
    else
        x=2;
 }

```

它们的流程如下 <img src="https://img-blog.csdnimg.cn/direct/c0c0554401f84b518c77d512ae1b82d8.png" alt="在这里插入图片描述"> 第一种写法的圈复杂度是：6（边）-6（节点）+2=2；第二种写法的圈复杂度是：7（边）-6（节点）+2=3。即第二种写法比第一种写法复杂度要高一些。我们从代码层面也能看出来如此。

它是基于论文。 其他参考资料
- - - 
### Average Method Lines of Code (AMLOC) metric

方法的平均行数指标。如果这个**值很大就不好**，说明大量的逻辑集中在少数方法中，意味着方法逻辑可能比较臃肿，进而意味着复杂度很高。当然也不是越少越好，比如一行逻辑写一个方法。该指标**鼓励大家写出更多短小、易于理解的方法，而不是内部极度臃肿的少数方法。**

它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

### Average Number of Parameters (ANPM) metric

方法的平均参数个数指标。这个值最小是0，最大未知。但是如果值很大，意味着方法关联的参数很多，可能是因为这个方法内部逻辑没有拆解好，导致其包含太多可以独立出去的逻辑，进而需要更多参数来支持。所以这个值越小越好，**越大意味着越复杂**。 它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

### Coupling Between Objects (CBO) metric

对象之间的耦合 (CBO) 是耦合到特定类的类数量的计数，即一个类的方法调用另一个类的方法或访问另一个类的变量的情况。这些调用需要在两个方向上计数，因此类 A 的 CBO 是类 A 引用的类集合和引用类 A 的类集合的大小。由于这是一个集合 - 每个类仅计数一次，即使引用在两个方向上运行，即如果 A 引用 B 并且 B 引用 A，则 B 只计算一次。**越大意味着耦合度越高。** <img src="https://img-blog.csdnimg.cn/direct/da6def67f8024fc48accda2dd9466306.png" alt="在这里插入图片描述"> 比如上图中C的CBO就高，它关联的类也是最多的。

它是基于Shyam R. Chidamber和Chris F. Kemerer的论文。 其他参考资料
- 
### Depth of Inheritance Tree (DIT) metric

最长继承树深度指标。它表示模块到最底层类的继承深度。**越大代表越复杂。** 数学公式是

>  
 DIT(m) = DIT(s(m)) + 1, ifc m != rootClass DIT(m) = 0, otherwise. 


<img src="https://img-blog.csdnimg.cn/direct/11c148469ede47fbb19a35397b226000.png" alt="在这里插入图片描述"> 比如上图中D的深度就是3，F的深度就是1。D就比F复杂。

它是基于Eduardo Kessler Piveta, Ana Moreira, Marcelo Soares Pimenta, Joao Araujo, Pedro Guerreiro和R. Tom Price的。 其他参考资料
- 
### Lack of Cohesion of Methods (LCOM4) metric

方法缺乏内聚性指标。在软件工程中，我们希望代码是高内聚低耦合。耦合指标我们可以通过上面的CBO来看，而内聚性则可以看LCOM4指标。**该值越高，表示越缺乏内聚性，表示越不好。**

该指标基于Martin Hitz和Behzad Montazeri的 。 更多资料参考
- - - - - 
### Lines of Code (LOC) metric

不包括空行和注释的代码行数。可以很好理解：**一般情况下，代码越长越复杂。** 它是基于Taghi M. Khoshgoftaar和John C. Munson的。

### Number of Attributes (NOA) metric

类的属性数量指标。如果一个类的属性数量很多，预示着它可能拥有太多的功能，即功能冗余。应该考虑将其拆解成更多高内聚、功能简单的类。**一般情况下，该值越大意味着越复杂。** 它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

### Number of Children (NOC) metric

从属于某个类的直接子类的数量指标。它是一个类对设计和系统的潜在影响的指标。子级的数量越多，父级不正确抽象的可能性就越大，并且可能是滥用子类的情况。但是子级的数量越多，可重用性就越大，因为继承是重用的一种形式。如果一个类有大量子类，则可能需要对该类的方法进行更多测试，从而增加测试时间。所以这个值没有很强的预示性。

它是基于Linda H. Rosenberg和Lawrence E. Hyatt的《Software Quality Metrics for Object-Oriented Environments》。 更多参考资料
- 
### Number of Methods (NOM) metric

类的方法数指标。如果一个类的方法很多，可能预示着它有太多的功能，缺乏内聚性。最好将其拆解成功能独立的小型类。**该指标越大表示越复杂。** 它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

### Number of Public Attributes (NPA) metric

类的公有属性数指标。类的属性应该通过方法来访问，而不是直接暴露给外面使用。所以**该值应该为0，否则就可能不是好的设计。** 它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

### Number of Public Methods (NPM) metric

类的公有方法数指标。如果类的公有方法比较多，意味着它对外提供的服务很多。这个不符合高内聚的设计思想。最好将这样的类拆解成功能独立的类。所以**这个值越小越好。** 它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

### Response for Class (RFC) metric

类的响应指标。它是指一个类的方法数，加上在它内部调用的其他类的方法数。如果这个数越大，说明这个类的耦合性越大，或者功能太多。这个就是需要拆解的类。所以**该值越大，表示越复杂。**

```
class BirdTeam {<!-- -->
public:
	void Run() {<!-- -->
			Bird * bird = new Bird();
			bird-&gt;run();
		}
		
	void Fly() {<!-- -->
		Bird * bird = new Bird();
		bird-&gt;FlyUp();
		bird-&gt;FlyDown();
	}

```

比如上面BirdTeam这个类，它有2个方法，其中调用了Bird的类3的方法。这样它的RFC就是2+3=5。

它是基于Shyam R. Chidamber和Chris F. Kemerer的 其他参考资料
- 
### Structural Complexity (SC) metric

结构复杂度。CBO（耦合度指标）和LCOM4（缺乏内聚性）的乘积与该指标正相关。所以**它越大表示越不好**，因为可能内聚比较差，也可能耦合性太高，也可能两者都很差。 它是基于Paulo Roberto Miranda Meirelles的《Monitoring of source code metrics in open source projects》。

## 代码



## 参考资料
- - - - - - 