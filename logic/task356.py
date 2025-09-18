def p(g):
    # link
    o=[*zip(*g)]
    for _ in 0,1:
        g=[r[:(s:=p.index(8))]+(8,)*((e:=len(r)-p[::-1].index(8))-s)+r[e:]if 8 in p else r for r,p in zip(zip(*g),o)]
        o=zip(*o)
    return g
