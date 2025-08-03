def p(g):
    c=[0,0]
    for y,r in enumerate(g):
        for v in r:
            if v:c[y>4]=v
    o=create(10,10)
    for y in range(10):
        t=c[y>4];r=o[y];r[0]=r[9]=t
        if y in(0,2,7,9):o[y]=[t]*10
    return o
