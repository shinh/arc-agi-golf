def p(g):
 # crop rare color
 b=sum(g,[])
 c=min({*b}-{0},key=b.count)
 t=[i for r in g if c in r for i,v in enumerate(r) if v==c]
 return [r[min(t):max(t)+1]for r in g if c in r]
