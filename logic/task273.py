def p(g):
    # fill rectangles enclosed by 4s
    d={}
    for y,r in enumerate(g):
        if 4in r:
            for R in g[-~d.setdefault((a:=r.index(4),b:=r.index(4,-~a)),y):y]:R[-~a:b]=[2]*(~a+b)
    return g
