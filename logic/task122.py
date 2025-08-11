# Far from the best (100)
def p(g):
    for sx in range(2):
        for y in range(len(g)-2):
            for x in range(len(g[0])-2):
                if[[r[x+1]for r in g[y:y+4]],g[y+1][x:x+4]][sx]==[2,3,2,3]:
                    for d in range(9):
                        if d!=4:
                            dy=2-d//3
                            dx=2-d%3
                            g[y+dy+2-sx*2][x+dx+sx*2]=g[y+dy][x+dx]
                            g[y+dy][x+dx]=0
                    return g
