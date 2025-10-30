def p(g):# extend max column
 i=g.index(r:=max(g))+1;j=r.index(v:=max(r));g[i][j]=v
 for r in g[:i]:r[j&1::2]=[4]*len(r[j&1::2])
 return g