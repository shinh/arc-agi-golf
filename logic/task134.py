def p(g):
    ac={*sum(g,[])}
    for r,pr in zip(g,g[1:]):
        for x in range(len(r)-2):
            s={*r[x:x+2],*pr[x:x+2]}
            if len(s)==1 and s!={0}:
                c,=[*s]
    ac,=[*(ac-{0,c})]
    for o in range(96):
        g=[*map(list,zip(*g[-2+(c in g[-1])::-1]))]

    ratio=len(g)//3
    return[[[0,ac][g[y*ratio][x*ratio]==c]for x in range(3)]for y in range(3)]
