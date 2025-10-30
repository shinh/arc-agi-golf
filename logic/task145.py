def p(g):# paint max area 1 and min area 8
 e=enumerate;s=[]
 def f(y,x):
  if len(g)>y>-1<x<len(g[0]) and g[y][x]<1:
   g[y][x]=10+len(s);return 1+f(y+1,x)+f(y-1,x)+f(y,x+1)+f(y,x-1)
  return 0
 for y,r in e(g):
  for x,v in e(r):
   if v<1:s+=f(y,x),
 m=max(s);n=min(s)
 for y,r in e(g):
  for x,v in e(r):
   if v>9:r[x]=(v:=s[v-10])==m or v==n and 8
 return g
