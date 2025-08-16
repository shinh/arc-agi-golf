# rotate the grid so flood fill can flow from one side only
def p(g):
 m=len(g)//2-1
 g[0][0]=1;g[-1][-1]=3
 for i in m,m+1:
  for r in g[m:m+2]:r[i]=r[i] or 2
 for _ in[0]*12:
  g=[[a or b*(b<4)for a,b in zip(r,(5,)+r)]for r in zip(*g[::-1])]
 return g

