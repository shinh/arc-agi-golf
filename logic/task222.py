def p(g):
    h=w=16;best=()
    for y0 in range(h):
        for y1 in range(y0+1,h+1):
            for x0 in range(w):
                c=g[y0][x0]
                if c==0:continue
                for x1 in range(x0+1,w+1):
                    a=(y1-y0)*(x1-x0)
                    if best and a<=best[0]:continue
                    ok=1
                    for y in range(y0,y1):
                        for x in range(x0,x1):
                            if g[y][x]!=c:ok=0;break
                        if not ok:break
                    if ok:best=(a,y0,y1,x0,x1,c)
    o=create(h,w)
    if best:
        a,y0,y1,x0,x1,c=best
        for y in range(y0,y1):
            for x in range(x0,x1):o[y][x]=c
    return o
