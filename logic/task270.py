def p(g):# move 7,3 toward centers of 1,2
 d=[[]for _ in[0]*10]
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   d[v]+=((y,x),)
   if v%4>2:g[y][x]=0
 for v,u in(1,7),(2,3):
  if d[v]:
   Y,X=[(min(q)+max(q))//2for q in zip(*d[v])]
   for a,b in d[u]:g[Y+(a>Y)-(a<Y)][X+(b>X)-(b<X)]=u
 return g
