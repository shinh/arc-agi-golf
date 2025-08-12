# rotate the grid so flood fill can flow from one side only
def p(g):
 m=len(g)//2
 g[0][0]=1;g[-1][-1]=3
 for i in range(4):
  y=m-1+i//2;x=m-1+i%2;g[y][x]=g[y][x] or 2
 for _ in range(80):
  g=[[a or(0<b<4 and b)for a,b in zip(r,r[1:]+(5,))]for r in zip(*g[::-1])]
 return g

