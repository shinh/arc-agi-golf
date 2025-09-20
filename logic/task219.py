def p(g):
 #copybig8
 q=[];b=-9
 for y,r in enumerate(g):
  if 8 in r:q+=[set()]*(y-b>1);q[-1]|={(y,x)for x,v in enumerate(r)if v==8};b=y
 T=max(q,key=lambda s:max(x for _,x in s)-min(x for _,x in s));q.remove(T)
 a=min(y for y,_ in T);b=min(x for _,x in T);T={(y-a,x-b)for y,x in T}
 for s in q:
  m=max(x for _,x in s);b=set();t=()
  for i in range(-15,15):
   for j in range(-10,20):
    S={(y+i,x+j)for y,x in T if 15>y+i>-1<x+j<10}
    if (D:=S-s) and min(x for _,x in D)>m and (k:=(len(s&S),j,i))>t:t=k;b=D
  for y,x in b:g[y][x]=1
 return g
