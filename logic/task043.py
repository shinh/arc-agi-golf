def p(g):
    r=[i for i in range(10)if g[0][i]>4]
    for row in g[1:]:
        if row[-1]==5:row[:]=[2*(i in r)for i in range(10)];row[-1]=5
    return g
