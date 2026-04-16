# fill the bridge between the two anchors
def p(g):
 a,b=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 q=a[0]!=b[0]
 if q:g=[*map(list,zip(*g))]
 m=(b[1-q]-a[1-q]-1)>>1
 for d,u in((1,a),(-1,b)):
  x=u[q];y=u[1-q];w=y+d*m;c=g[x][y]
  g[x][y:w:d]=[c]*m
  for r in g[x-2:x+3]:r[w-d]=c
  g[x-2][w]=g[x+2][w]=c
 return(g,[*zip(*g)])[q]
