def p(g):
    r=[i for i,v in enumerate(g[0])if v==5];w=len(g[0])
    for row in g[1:]:
        if row[-1]==5:row[:]=[2*(i in r)for i in range(w)];row[-1]=5
    return g
