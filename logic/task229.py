def p(g):
    f=[c for r in g for c in r];m=max(f,key=f.count)
    return[[v if v==m else 5 for v in r]for r in g]
