def p(g):
 # paint max area 1 and min area 8
 h=len(g);w=len(g[0]);R=range;s=[]
 def f(y,x,k):
  if-1<y<h and-1<x<w and g[y][x]<1:
   g[y][x]=k;return 1+f(y+1,x,k)+f(y-1,x,k)+f(y,x+1,k)+f(y,x-1,k)
  return 0
 k=9
 for y in R(h):
  for x in R(w):
   if g[y][x]<1:
    k+=1;s+=[f(y,x,k)]
 m=max(s);n=min(s)
 for y in R(h):
  for x in R(w):
   v=g[y][x];g[y][x]=v>9 and(s[v-10]==m or(s[v-10]==n)*8)or v*(v<10)
 return g

