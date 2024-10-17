
--- 
title:  Ruby 将项目打成 gem 包 
tags: []
categories: [] 

---
直接使用例子来讲的话就清晰得多了。

假如我有一个 zshell-sdk 的 ruby 小项目（项目目录结构如下）：

```
root@localhost ~# tree zshell-sdk/
zshell-sdk/
├── README.md
├── rebuild_and_install_gem
├── zshell
│   ├── file_command.rb
│   ├── ftp_command.rb
│   ├── lurker_command.rb
│   ├── macaddr.rb
│   ├── service_command.rb
│   ├── shell_command.rb
│   ├── system_command.rb
│   └── unsafe_command.rb
├── zshell.gemspec
└── zshell.rb

1 directory, 12 files

```

打包的话，最重要的则是写好那个 zshell.gemspec 文件了，一般文件里边会包含如下信息（记得要将打包的 rb 文件 join 到 s.files 里边）。

```
Gem::Specification.new do |s|
    s.homepage = "http://www.xxx.cn"
    s.license = 'xxx'
    s.name = "zshell"
    s.version = "0.0.1"
    s.date = "2022-05-12"
    s.authors = ["Knet xxx"]
    s.email = "xxx@xxx"
    s.summary = "xxx"
    s.description = "xxx"
    s.files += Dir["zshell.rb"]
    s.files += Dir["zshell/*.rb"]
    s.bindir = "bin"
    s.require_paths &lt;&lt; '.'
end
```

zhell.rb 里边一般不写业务代码，而是专门做 require 其他业务模块的功能。

```
require_relative "zshell/macaddr"
require_relative "zshell/shell_command"
require_relative "zshell/lurker_command"
require_relative "zshell/service_command"
require_relative "zshell/system_command"
require_relative "zshell/file_command"
require_relative "zshell/ftp_command"
require_relative 'zshell/unsafe_command'
```

一切准备好以后，就可以 build 和 install 了。

```
gem build zshell.gemspec
gem install zshell -l --no-ri --no-rdoc

root@localhost ~/zshell-sdk# sh rebuild_and_install_gem 
  Successfully built RubyGem
  Name: zshell
  Version: 0.0.1
  File: zshell-0.0.1.gem
Successfully installed zshell-0.0.1
1 gem installed

```

使用的话也简单。

```
root@localhost ~/zshell-sdk# pry
[1] pry(main)&gt; require 'zshell'
=&gt; true
[2] pry(main)&gt; DDI::ZShell::get_routing_table.split("\n")
=&gt; ["Kernel IP routing table",
 "Destination     Gateway         Genmask         Flags Metric Ref    Use Iface",
 "0.0.0.0         10.2.18.1       0.0.0.0         UG    0      0        0 eth0",
 "10.2.18.0       0.0.0.0         255.255.254.0   U     0      0        0 eth0",
 "169.254.0.0     0.0.0.0         255.255.0.0     U     1002   0        0 eth0"]

```

```
ruby tests/sdk/shell_command_test.rb --name test_get_file_lines
```


