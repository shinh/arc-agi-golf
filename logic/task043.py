def p(g):
    w=len(g[0])
    r=[i for i in range(w)if g[0][i]>4]
    for row in g[1:]:
        if row[-1]==5:row[:]=[2*(i in r)for i in range(w)];row[-1]=5
    return g
