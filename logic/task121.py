def p(g):
    for y,r in enumerate(g):
        if 8 in r:
            x=r.index(8);o=[g[y-1][x-1:x+2],r[x-1:x+2],g[y+1][x-1:x+2]]
            o[1][1]=max(o[0]+o[1][:1]+o[1][2:]+o[2])
            return o
