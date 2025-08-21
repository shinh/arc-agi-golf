def p(g,E=enumerate):
 # connect same-colored dots
 C=g[0][2];o=[[0]*len(r)for r in g]
 for _ in 0,1:
  for y,r in E(g):
   for x,v in E(r):
    if v==C:o[y][x]=v
    elif v in r[x+1:]and v:X=r.index(v,x+1)+1;o[y][x:X]=[v]*(X-x)
  g=[*zip(*g)];o=[*map(list,zip(*o))]
 return o
