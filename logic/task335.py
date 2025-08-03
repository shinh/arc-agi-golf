def p(g):
 a=b=c=d=0
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==8:a,b=y,x
   if v==2:c,d=y,x
 if c!=a:
  s=1 if c>a else-1
  for y in range(a+s,c,s):g[y][b]=4
 if d!=b:
  s=1 if d>b else-1
  for x in range(b,d,s):g[c][x]=4
 return g
