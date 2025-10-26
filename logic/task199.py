def p(g):
 s=sum(g,[]);v=max(s);i,j=divmod(s.index(v),len(g));g[i+1][j]=v
 for r in g[:i+1]:r[j&1::2]=[4]*len(r[j&1::2])
 return g