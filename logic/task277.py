def p(g):# flood fill shapes, count patterns, recolor odd one
 g=sum(g,[]);m={}
 for k in range(100):
  if g[k]:
   q=[k];g[k]=0
   for i in q:
    for n in-11,-10,-9,-1,1,9,10,11:
     j=i+n
     if 0<=j<100>-2<j%10-i%10<2 and g[j]:g[j]=0;q+=j,
   s=tuple(j-q[0]for j in q)
   m[s]=m.get(s,[])+[q]
 t=min(m,key=lambda k:len(m[k]))
 for k in m:
  c=1+(k==t)
  for q in m[k]:
   for j in q:g[j]=c
   c=1
 return[g[i:i+10]for i in range(0,91,10)]
