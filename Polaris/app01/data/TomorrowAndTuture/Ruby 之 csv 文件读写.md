
--- 
title:  Ruby 之 csv 文件读写 
tags: []
categories: [] 

---
## csv 文件写入

```
require 'csv'

title = ["col1", "col2"]
contents = [["row11", "row12"], ["row21", "row22"]]

csv1 = CSV.open("test1.csv", "wb") do |csv|
  # write file title
  csv &lt;&lt; title

  # write file body
  contents.each do |line|
    csv &lt;&lt; line
  end
end

puts csv1.class
puts csv1.inspect

# UTF-8编码的文件，开头会加入BOM来表明编码方式
csv2 = CSV.generate("\xEF\xBB\xBF") do |csv|
    # write file title
    csv &lt;&lt; title

    # write file body
    contents.each do |line|
      csv &lt;&lt; line
    end
end
File.open("test2.csv", "wb"){|f| f &lt;&lt; csv2}

puts csv2.class
puts csv2.inspect
```

```
Array
[["row11", "row12"], ["row21", "row22"]]
String
"﻿col1,col2\nrow11,row12\nrow21,row22\n"
```

## csv 文件读取

test.csv

```
col1,col2
row11,row12
row21,row22

```

### 按行读取 

```
require 'csv'

csv3 = []
CSV.open("test1.csv") do |csv|
  csv.each do |line|
    csv3 &lt;&lt; line
  end
end

puts csv3.class
puts csv3.inspect

csv4 = []
File.open("test2.csv", "rb") do |f|
  f.each do |line|
    csv4 &lt;&lt; line
  end
end
puts csv4.class
puts csv4.inspect
```

```
Array
[["col1", "col2"], ["row11", "row12"], ["row21", "row22"]]
Array
["\xEF\xBB\xBFcol1,col2\n", "row11,row12\n", "row21,row22\n"]
```

### 以键值对形式读取

```
require 'csv'

rows = CSV.read("test.csv", headers:true)
title = rows.headers
contents = []
rows.each do |row|
  contents &lt;&lt; row.to_h
end
puts title.inspect
puts contents.inspect

puts
rows = CSV.parse("col1,col2\nrow11,row12\nrow21,row22", headers:true)
title = rows.headers
contents = []
rows.each do |row|
  contents &lt;&lt; row.to_h
end
puts title.inspect
puts contents.inspect
```

```
["col1", "col2"]
[{"col1"=&gt;"row11", "col2"=&gt;"row12"}, {"col1"=&gt;"row21", "col2"=&gt;"row22"}]

["col1", "col2"]
[{"col1"=&gt;"row11", "col2"=&gt;"row12"}, {"col1"=&gt;"row21", "col2"=&gt;"row22"}]
```
