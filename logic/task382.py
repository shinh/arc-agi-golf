def p(g):
    # draw a right-moving trail of 8s that climbs once for each 2 in the bottom row
    r=lambda t:[*map(list,zip(*t[::-1]))]
    h=lambda t:[row[::-1]for row in t]
    for k in range(4):
        if 2 in g[-1] and any(8 in (row[0],row[-1])for row in g):
            f=all(row[0]-8 for row in g)
            if f:g=h(g)
            o=[[2*(c==2)for c in row]for row in g]
            for y,row in enumerate(g):
                if row[0]==8:
                    z=y
                    for x,c in enumerate(g[-1]):
                        z-=c==2
                        if z<0:break
                        o[z][x]=8
            if f:o=h(o)
            for _ in range(4-k):o=r(o)
            return o
        g=r(g)

