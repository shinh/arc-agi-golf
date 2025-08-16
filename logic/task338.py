# Just solved.
#
# Based on 029
def p(g):
    for sy in range(len(g)):
        for sx in range(len(g[0])):
            for ey in range(len(g),sy+1,-1):
                for ex in range(len(g[0]),sx+1,-1):
                    if{2}=={*g[sy][sx:ex],*g[ey-1][sx:ex],*[g[y][x]for y in range(sy,ey)for x in(sx,ex-1)]}:
                        for y in range(sy,ey):
                            for x in range(sx,ex):
                                g[y][x]=3*(g[y][x]<2)
    return g
