def p(g):
    for r,pr in zip(g,g[1:]):
        for x in range(len(r)):
            s={*r[x:x+3],pr[x:x+3]}-{0}
            if len(s)==1:
                c,=[*s]
