def p(g):# move 7,3 toward centers of 1,2
 d=[[]for _ in[0]*8]
 for y,r in enumerate(g):
  for x,v in enumerate(r):d[v]+=y,x;r[x]*=v<3
 for v,u in(1,7),(2,3):
  Y,X=d[v][:2]
  for a,b in zip(d[u][::2],d[u][1::2]):g[Y+(a>Y)-(a<Y)][X+(b>X)-(b<X)]=u
 return g
