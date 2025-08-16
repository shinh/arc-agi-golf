def p(g):
 # find rare color then crop its bbox
 f=sum(g,[])
 k=min({*f}-{0},key=f.count)
 y=[i for i,r in enumerate(g) if k in r]
 x=[i for i,c in enumerate(zip(*g)) if k in c]
 return [r[x[0]:x[-1]+1] for r in g[y[0]:y[-1]+1]]
