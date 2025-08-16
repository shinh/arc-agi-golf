def p(g):
    # count 2x2 blocks of color 1
    return [[1]*(c:=sum((1,)*4==y for a,b in zip(g,g[1:])for y in zip(a,a[1:],b,b[1:])))+[0]*(5-c)]
