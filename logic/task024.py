def p(g):
    h=len(g);w=len(g[0]);o=create(h,w)
    for i,v in enumerate(zip(*g)):
        if 2 in v:
            for r in o:r[i]=2
    for y in range(h):
        for v in(1,3):
            if v in g[y]:o[y]=[v]*w
    return o
