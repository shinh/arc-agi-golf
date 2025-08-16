def p(g):
    # draw a right-moving trail of 8s that climbs once for each 2 in the bottom row
    r=lambda t:[list(x)for x in zip(*t[::-1])]
    for k in range(4):
        if 2 in g[-1]:
            a=any(row[0]==8 for row in g)
            if a or any(row[-1]==8 for row in g):
                f=0
                if not a:g=[row[::-1]for row in g];f=1
                b=g[-1];o=[[2*(c==2)for c in row]for row in g]
                for y,row in enumerate(g):
                    if row[0]==8:
                        z=y
                        for x,c in enumerate(b):
                            z-=c==2
                            if z<0:break
                            o[z][x]=8
                if f:o=[row[::-1]for row in o]
                for _ in range(4-k):o=r(o)
                return o
        g=r(g)

