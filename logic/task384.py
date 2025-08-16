# crop bbox of nonzeros and double size
def p(g):y,x=zip(*((i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v));return[[v for v in r[min(x):max(x)+1]for _ in(0,0)]for r in g[min(y):max(y)+1]for _ in(0,0)]
