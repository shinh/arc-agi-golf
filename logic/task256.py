# triangles at 2
def p(g):
 i=g.index(max(g));a=g[i].index(0)+i;t=a
 while t:y=a-t;g[y][:t]=[2+(i>y)-(y>i)]*t;t-=1
 return g

