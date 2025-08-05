def p(g):
    fg=(set(g[0])-{0}).pop()
    for t in range(30):
        best_y=max_size=0
        for o in range(4):
            for sx in range(-1,30):
                for ex in range(sx+3,32):
                    if any(g[0][max(sx,0):ex]):continue
                    connected=0
                    for ey in range(30):
                        if any(fg==c for c in g[ey][max(sx,0):ex]):
                            ey -= 1
                            break
                        if all(c==3 for c in g[ey][max(sx,0):ex]):
                            connected=1
                            break
                        ey+=1
                    if max_size<(ex-sx)*ey+ey and(t<2 or connected):
                        max_size=(ex-sx)*ey+ey
                        best_sx,best_ex,best_y,best_o=sx,ex,ey,o
            g=[list(r)for r in zip(*g[::-1])]
        for o in range(4):
            if best_o==o and best_y>3:
                for y in range(best_y):
                    for x in range(best_sx+1,best_ex-1):
                        g[y][x]=3
            g=[list(r)for r in zip(*g[::-1])]


    #show(g,"out")

    return g
