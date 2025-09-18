def p(g):
 # extend 8 pairs sideways
 [(r,s)[r[n]>0].__setitem__(n,1)for r,s in zip(g,g[1:])for x in range(7)if r[x]&s[x]for n in(x-1,x+1)if~n%8 and r[n]^s[n]]
 return g
