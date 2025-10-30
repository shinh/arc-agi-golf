def p(g,m=-1):
 for r in g[::-1]:p=m;m=-1;[m:=x for x,v in enumerate(r)if v];r[:0]=0,;r[p]+=r.pop(p+1)
 return g
