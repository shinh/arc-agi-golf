def p(g):
 a=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 q=a[0][0]!=a[1][0]
 if q:g=[*map(list,zip(*g))]
 m=(a[1][1-q]-a[0][1-q]-1)>>1
 for d in 1,-1:
  y=a[d<0];x=y[q];j=y[1-q];w=j+d*m;c=g[x][j]
  g[x][j:w:d]=[c]*m
  for r in g[x-2:x+3]:r[w-d]=c
  g[x-2][w]=g[x+2][w]=c
 return (g,[*zip(*g)])[q]