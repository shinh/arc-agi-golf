def p(g):
    # map colors by period and crop blank box
    py=next(p for p in range(1,99)if all(a==b or a*b<1 for r,s in zip(g,g[p:])for a,b in zip(r,s)))
    px=next(p for p in range(1,99)if all(a==b or a*b<1 for r in g for a,b in zip(r,r[p:])))
    d={(y%py,x%px):v for y,r in enumerate(g)for x,v in enumerate(r)if v}
    ys=[i for i,r in enumerate(g)if 0 in r];xs=[i for i,c in enumerate(zip(*g))if 0 in c]
    y0,y1=ys[0],ys[-1];x0,x1=xs[0],xs[-1]
    return [[d[y%py,x%px]for x in range(x0,x1+1)]for y in range(y0,y1+1)]
