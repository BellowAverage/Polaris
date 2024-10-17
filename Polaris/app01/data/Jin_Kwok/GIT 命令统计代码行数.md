
--- 
title:  GIT 命令统计代码行数 
tags: []
categories: [] 

---
### GIT 命令统计代码行数

#### 1.统计指定时间段内的新增/删除代码行数 

```
git log --since=2020-01-01 --until=2021-01-01 --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | grep "\(.html\|.java\|.xml\|.properties\)$" | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
```

#### 2.统计指定时间段内+指定作者的新增/删除代码行数

指定时间：2020-01-01～2021-01-01 ；指定作者：dagongren

```
git log --author=dagongren --since=2020-01-01 --until=2021-01-01 --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | grep "\(.html\|.java\|.xml\|.properties\)$" | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
```

#### 3.统计指定项目所有的代码行数

```
git log  --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'

```

 
