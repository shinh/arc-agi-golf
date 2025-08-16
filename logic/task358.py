def p(g):# expand patterns horizontally then vertically
    for r in g:
        if (S:=[x for x,v in enumerate(r) if v])[1:]:R=r[S[0]:S[-1]+1];break
    r[:]=[R[(x-S[0])%len(R)]for x in range(len(r))]
    for X,C in enumerate(zip(*g)):
        if (T:=[y for y,v in enumerate(C) if v])[1:]:C=C[T[0]:T[-1]+1];break
    for y,v in enumerate(g):v[X]=C[(y-T[0])%len(C)]
    return g
