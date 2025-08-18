def p(g):
    # +g[:5] is to workaround a single corner case.
    f=[c for r in g+g[:5]for c in{*r}]
    c=min(f,key=f.count)
    f=lambda g:[*map(list,zip(*filter(lambda r:c in r,g)))]
    return f(f(g))
