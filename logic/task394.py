def p(g):
    # find tile period and crop around blanks
    h=len(g);w=len(g[0])
    py=px=1
    while py<h and any(a-b and a*b for r,s in zip(g,g[py:])for a,b in zip(r,s)):py+=1
    while px<w and any(a-b and a*b for r in g for a,b in zip(r,r[px:])):px+=1
    ys=[i for i,r in enumerate(g)if 0 in r];xs=[i for i,c in enumerate(zip(*g))if 0 in c]
    y0=min(ys);x0=min(xs);y1=max(ys);x1=max(xs)
    t=[[0]*px for _ in[0]*py]
    [v and t[y%py].__setitem__(x%px,v)for y,r in enumerate(g)for x,v in enumerate(r)]
    return [[t[y%py][x%px]for x in range(x0,x1+1)]for y in range(y0,y1+1)]
