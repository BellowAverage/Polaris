
--- 
title:  matlab中subs函数引用疑问 
tags: []
categories: [] 

---
matlab中subs函数引用疑问

%%%%%%%%%%%%%%%%%%%%% syms t y x w k d n c a b; f=a**x^n+b**y+k; r=sin(t);y=log(w);u=c**exp(-b**t); f=subs(f,{a b k},{r y u})%花括号与中括号都可以

j=subs(n,5) l=subs(k,pi) z=subs(k,1:4) %%%%%%%%%%%%%%%%%%% 结果 %%%%%%%%%%%%%%%% f =

c**exp(-b**t) + x^n**sin(t) + y**log(w)

j =

5

l =

pi

z =

[ 1, 2, 3, 4]

二 %%%%%%%%%%%%%%%%%% syms m Dv dv lv; pv=(4**m/(pi**(Dv<sup>2-dv</sup>2)**lv)); % ev=sqrt() m1=23.53; L=[25.22,25.28,25.26,25.24,25.26,25.28,25.24,25.26]; D=[23.84,23.86,23.88,23.88,23.86,23.88,23.86,23.89]; d=[12.08,12.11,12.06,12.12,12.08,12.09,12.09,12.08]; %L=input(‘输入数据格式[]：’)； % (p,q)=size(L)； nlv=L/8; nDv=D/8;**
