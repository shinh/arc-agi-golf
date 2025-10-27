def p(g):#crop interior
 b=bytes(sum(g,[]));m=len(g[0]);i=b.find(c:=next(filter(abs,b)));j=b.rfind(c);return[[c*(x>0)for x in r[i%m+1:j%m]]for r in g[i//m+1:j//m]]
