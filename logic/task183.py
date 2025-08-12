def p(g):
        H=len(g)
        W=len(g[0])
        return[[(g[y][x]>0)*g[-(y>=H/2)][-(x>=W/2)]for x in range(2,W-2)]for y in range(2,H-2)]
