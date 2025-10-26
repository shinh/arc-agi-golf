def p(g):
 f=sum(g,[]);i=f.index(max(f));r=range(n:=len(g))
 return [[f[i]*(abs(Y-i//n)==abs(X-i%n)) for X in r] for Y in r]