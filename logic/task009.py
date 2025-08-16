def p(g,R=range,E=enumerate):
 # connect same-colored dots
 C=g[0][2];o=[[0]*len(g[0])for _ in g]
 for _ in 0,1:
  for y,r in E(g):
   for x,v in E(r):
    if v==C:o[y][x]=v
    elif v:
     try:X=r.index(v,x+1);o[y][x:X+1]=[v]*(X+1-x)
     except:0
  g=[*zip(*g)];o=[list(r)for r in zip(*o)]
 return o
