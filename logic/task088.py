def p(g):#crop interior
 a=sum(g,[]);m=len(g[0]);c=a[i:=a.index(next(filter(abs,a)))];j=~a[::-1].index(c)
 return[[x and c for x in r[i%m+1:j%m]]for r in g[i//m+1:j//m]]
