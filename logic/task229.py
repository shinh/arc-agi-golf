def p(g):
    f=[c for r in g for c in r];m=max(f,key=f.count)
    return[[[5,v][v==m]for v in r]for r in g]
