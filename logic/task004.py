# Shift each color right except bottom and right edges.

def p(g,E=enumerate):
 o=[[0]*len(r)for r in g]
 for v in{*sum(g,[])}-{0}:
  P=[(i,j)for i,r in E(g)for j,x in E(r)if x==v];b,m=map(max,zip(*P))
  for i,j in P:o[i][j+(i<b)*(j<m)]=v
 return o
