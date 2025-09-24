def p(g):
 # paint max area 1 and min area 8
 h=len(g);w=len(g[0]);R=range;s=[]
 def f(y,x):
  if-1<y<h and-1<x<w and g[y][x]<1:
   g[y][x]=10+len(s);return 1+f(y+1,x)+f(y-1,x)+f(y,x+1)+f(y,x-1)
  return 0
 for y in R(h):
  for x in R(w):
   if g[y][x]<1:
    s+=f(y,x),
 m=max(s);n=min(s)
 for y in R(h):
  for x in R(w):
   if(v:=g[y][x])>9:g[y][x]=s[v-10]==m or(s[v-10]==n)*8
 return g

