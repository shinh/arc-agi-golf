def p(g):# move 7,3 toward centers of 1,2
 d=[[]for _ in' '*8]
 for y,r in enumerate(g):
  for x,v in enumerate(r):d[v]+=[(y,x)];r[x]*=v<3
 for v,u in(1,7),(2,3):
  Y,X=[sum(q)//len(q)for q in zip(*d[v])]
  for a,b in d[u]:g[Y+(a>Y)-(a<Y)][X+(b>X)-(b<X)]=u
 return g
