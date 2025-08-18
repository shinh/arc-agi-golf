def p(g):
    # detect repeat and fill zero box
    f=lambda a:next(p for p in range(1,len(a)+1)if all(x==y or x*y<1 for r,s in zip(a,a[p:])for x,y in zip(r,s)))
    py=f(g);px=f(list(zip(*g)))
    d={(y%py,x%px):v for y,r in enumerate(g)for x,v in enumerate(r)if v}
    ys,xs=[[i for i,r in enumerate(a)if 0 in r]for a in(g,zip(*g))]
    return [[d[y%py,x%px]for x in range(xs[0],xs[-1]+1)]for y in range(ys[0],ys[-1]+1)]
