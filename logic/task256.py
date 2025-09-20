# triangles at 2
def p(g):
 i=g.index(max(g));d=g[i].index(0);t=i+d
 while t:g[i+d-t][:t]=[2+(t>d)-(t<d)]*t;t-=1
 return g

