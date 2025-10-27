# slide the 3x3 chunk below/right of a 2,3 stripe
p=lambda g,n=1:-n*g or p([*zip(*((g,g[-2-len(g)%2:][:2]+g[:-2])[sum(3 in r for r in g)>1]))],n-1)
