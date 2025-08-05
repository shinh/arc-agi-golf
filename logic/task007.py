def p(g):
    c=[0]*3
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:c[(y+x)%3]=v
    return [[c[(y+x)%3]for x in range(7)]for y in range(7)]
