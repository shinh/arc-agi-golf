def p(g):
    bg=max(g[0],key=g[0].count)
    for o in range(4):
        for y in range(len(g)):
            for x in range(len(g[0])-2):
                c=g[y][x]
                if c!=bg and(x<1or g[y][x-1]==bg)and(g[y][x+1]==bg or g[y][x+2]==bg):
                    for nx in range(x,len(g[0])):
                        u=g[y][nx]
                        if u!=bg and u!=c:
                            if g[y][nx+1]==u:
                                for rx in range(x,nx):
                                    g[y][rx]=c
                            break
        g=[list(r)for r in zip(*g[::-1])]
    return g
