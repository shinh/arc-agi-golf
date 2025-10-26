def p(g):
 t=g[1:-1];b=[*map(sum,zip(*t))][1:-1]
 for r in t:a=r[1:-1];r[1:-1]=(x or(sum(a)<1or y<1)*3for x,y in zip(a,b))
 return g