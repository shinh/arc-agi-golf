def p(g):
 k=max(set(sum(g,[]))-{x for r in g[1:-1]for x in r[1:-1]});return[[k*(k in(r[0],r[~0],a,b))for a,b in zip(g[0],g[~0])]for r in g]