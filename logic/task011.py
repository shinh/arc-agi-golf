def p(g):
    for y in range(0,len(g),4):
        for x in range(0,len(g),4):
            m=[[g[y+i][x+j]for j in range(3)]for i in range(3)]
            if 8 not in sum(m,[]):
                o=[r[:] for r in g]
                for i,Y in enumerate(range(0,len(g),4)):
                    for j,X in enumerate(range(0,len(g),4)):
                        v=m[i][j]
                        for dy in range(3):
                            for dx in range(3):
                                o[Y+dy][X+dx]=v
                return o
