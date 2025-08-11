def p(g):
    for sy,sx in(2,0),(0,2):
        for y in range(len(g)-2-sy):
            for x in range(len(g[0])-2-sx):
                if[[r[x+1]for r in g[y:y+4]],g[y+1][x:x+4]][sx//2]==[2,3,2,3]:
                    for d in range(9):
                        if d!=4:
                            dy=2-d//3
                            dx=2-d%3
                            g[y+dy+sy][x+dx+sx]=g[y+dy][x+dx]
                            g[y+dy][x+dx]=0
                    return g
