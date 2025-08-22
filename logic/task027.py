def p(g):
    # mirror pattern and overlay symmetrically
    r=range(10);a={(y,x)for y in r for x in r if g[y][x]}
    sh=max((len(a&b),b)for d in range(19)if len(b:={(d-x,y)for y,x in a})==len(a))[1]
    for y,x in sh-a:g[y][x]=2
    return g
