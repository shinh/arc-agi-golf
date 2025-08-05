def p(g):
    h=9;w=3
    def vsplit(n):
        hh=h//n;off=h%n!=0
        return [g[i*hh+i*off:(i+1)*hh+i*off] for i in range(n)]
    def hsplit(n):
        ww=w//n;off=w%n!=0
        return [[row[i*ww+i*off:(i+1)*ww+i*off] for row in g] for i in range(n)]
    n=max(h,w)//min(h,w)
    parts=vsplit(n) if h>w else hsplit(n)
    for pce in parts:
        if pce!=[list(r) for r in zip(*pce)]:return pce
