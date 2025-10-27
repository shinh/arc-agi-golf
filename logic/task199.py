def p(g):
 i=g.index(r:=max(g));j=r.index(v:=max(r));g[i+1][j]=v
 for r in g[:i+1]:r[j&1::2]=[4]*len(r[j&1::2])
 return g