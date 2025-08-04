def p(g):
    h=len(g);w=len(g[0]);c=[0]*3
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:c[(y+x)%3]=v
    return [[c[(y+x)%3]for x in range(w)]for y in range(h)]
