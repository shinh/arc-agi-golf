def p(g):
    c={}
    for r in g:
        for v in r:c[v]=c.get(v,0)+1
    bg=max(c,key=c.get)
    ys=[y for y,r in enumerate(g) for x,v in enumerate(r) if v!=bg]
    xs=[x for y,r in enumerate(g) for x,v in enumerate(r) if v!=bg]
    a=[r[min(xs):max(xs)+1]for r in g[min(ys):max(ys)+1]]
    H=len(a);W=len(a[0])
    o=[[bg]*((W-1)//2+1)for _ in range((H-1)//2+1)]
    for y,r in enumerate(a):
        for x,v in enumerate(r):
            if v!=bg:o[(y+1)//2][(x+1)//2]=v
    return o
