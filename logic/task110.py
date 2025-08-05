def p(g):
    h=w=29
    for q in range(1,h+1):
        for p in range(1,w+1):
            t=[[0]*p for _ in range(q)];ok=1
            for y in range(h):
                for x,v in enumerate(g[y]):
                    if v:
                        yy=y%q;xx=x%p;tv=t[yy][xx]
                        if tv and tv!=v:ok=0;break
                        t[yy][xx]=v
                if not ok:break
            if ok:
                for y in range(h):
                    r=g[y];tt=t[y%q]
                    for x in range(w):r[x]=tt[x%p]
                return g
