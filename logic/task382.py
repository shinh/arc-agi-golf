def p(g):
    # draw a right-moving trail of 8s that climbs once for each 2 in the bottom row
    R=lambda g:[*zip(*g[::-1])];F=lambda g:[r[::-1]for r in g]
    for k in range(4):
        if 2 in g[-1]and any(r[0]>7or r[-1]>7for r in g):
            f=max(r[0]for r in g)<8
            if f:g=F(g)
            o=[[c&2for c in r]for r in g]
            for y,r in enumerate(g):
                if r[0]>7:
                    z=y
                    for x,c in enumerate(g[-1]):
                        z-=c==2
                        if z<0:break
                        o[z][x]=8
            if f:o=F(o)
            for _ in range(4-k):o=R(o)
            return o
        g=R(g)

