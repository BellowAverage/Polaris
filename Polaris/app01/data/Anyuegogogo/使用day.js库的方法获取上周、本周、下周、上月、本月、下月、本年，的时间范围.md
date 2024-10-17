
--- 
title:  使用day.js库的方法获取上周、本周、下周、上月、本月、下月、本年，的时间范围 
tags: []
categories: [] 

---
```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="UTF-8"&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
  &lt;title&gt;Document&lt;/title&gt;
  &lt;script src="https://cdn.jsdelivr.net/npm/dayjs@1.10.6/dayjs.min.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;script&gt;
  const weekStart = 1; // 1表示周一是一周的开始，0表示周日是一周的开始

  // 获取上周的起始日期和结束日期
  function getLastWeek() {<!-- -->
    const startOfWeek = dayjs().subtract(1, 'week').day(weekStart).format('YYYY-MM-DD') + ' 00:00:00';
    const endOfWeek = dayjs().subtract(1, 'week').day(weekStart + 6).format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfWeek, endOfWeek };
  }

  // 获取本周的起始日期和结束日期
  function getCurrentWeek() {<!-- -->
    const startOfWeek = dayjs().day(weekStart).format('YYYY-MM-DD') + ' 00:00:00';
    const endOfWeek = dayjs().day(weekStart + 6).format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfWeek, endOfWeek };
  }

  // 获取下周的起始日期和结束日期
  function getNextWeek() {<!-- -->
    const startOfWeek = dayjs().add(1, 'week').day(weekStart).format('YYYY-MM-DD') + ' 00:00:00';
    const endOfWeek = dayjs().add(1, 'week').day(weekStart + 6).format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfWeek, endOfWeek };
  }

  // 获取上个月的起始日期和结束日期
  function getLastMonth() {<!-- -->
    const startOfMonth = dayjs().subtract(1, 'month').startOf('month').format('YYYY-MM-DD') + ' 00:00:00';
    const endOfMonth = dayjs().subtract(1, 'month').endOf('month').format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfMonth, endOfMonth };
  }

  // 获取本月的起始日期和结束日期
  function getCurrentMonth() {<!-- -->
    const startOfMonth = dayjs().startOf('month').format('YYYY-MM-DD') + ' 00:00:00';
    const endOfMonth = dayjs().endOf('month').format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfMonth, endOfMonth };
  }

  // 获取下个月的起始日期和结束日期
  function getNextMonth() {<!-- -->
    const startOfMonth = dayjs().add(1, 'month').startOf('month').format('YYYY-MM-DD') + ' 00:00:00';
    const endOfMonth = dayjs().add(1, 'month').endOf('month').format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfMonth, endOfMonth };
  }

  // 获取本年的起始日期和结束日期
  function getCurrentYear() {<!-- -->
    const startOfYear = dayjs().startOf('year').format('YYYY-MM-DD') + ' 00:00:00';
    const endOfYear = dayjs().endOf('year').format('YYYY-MM-DD') + ' 23:59:59';
    return {<!-- --> startOfYear, endOfYear };
  }

  // 示例
  console.log(getLastWeek());
  console.log(getCurrentWeek());
  console.log(getNextWeek());
  console.log(getLastMonth());
  console.log(getCurrentMonth());
  console.log(getNextMonth());
  console.log(getCurrentYear());
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

```
