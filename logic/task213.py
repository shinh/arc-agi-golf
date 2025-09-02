def p(g):
    o=[]
    for r in g:
        s={*r}-{0,5}
        l=len(s)
        if l>1:
            return[*zip(*p([*zip(*g)]))]
        if l:
            o+=[[*s][0]],
    o=[r*len(o)for r in o]
    return o


