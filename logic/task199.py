def p(g):
 s=sum(g,[]);i,j=divmod(s.index(v:=max(s)),len(g));g[i+1][j]=v
 for r in g[:i+1]:r[j&1::2]=[4]*len(r[j&1::2])
 return g