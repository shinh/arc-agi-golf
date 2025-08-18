def p(g):
    # fill square holes
    for s in range(2,12):
        for y in range(12-s):
            for x in range(12-s):
                 if all(g[y][x+i]==g[y+s][x+i]==g[y+i][x]==g[y+i][x+s]==5 for i in range(s+1))*all(sum(g[y+i][x+1:x+s])<1 for i in range(1,s)):
                    for r in g[y+1:y+s]:r[x+1:x+s]=[2]*(s-1)
    return g
