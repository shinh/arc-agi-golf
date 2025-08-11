def p(g):
    for o in range(4):
        if o==0 or o==3:
            ok=0
            for y in range(len(g)-2):
                for x in range(len(g[0])-3):
                    if g[y+1][x:x+4]==[2,3,2,3]:
                        for dy in 2,1,0:
                            for dx in 2,1,0:
                                if dy!=1 or dx!=1:
                                    g[y+dy][x+dx+2]=g[y+dy][x+dx]
                                    g[y+dy][x+dx]=0
                                    ok=1
                    if ok:break
                if ok:break
        g=[list(r)for r in zip(*g[::-1])]
    return g
