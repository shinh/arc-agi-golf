def p(g):
    t=g[0][0];s=[r[0]for r in g]
    if 0 in s:
        a=[c for c in s if c];a=a[1:]+a[:1];s=a+[a[0]]
    o=[[0]*10 for _ in range(10)]
    for y in range(5):
        for x in range(5):
            o[y][x]=g[y][x] or t
            o[y+5][x+5]=s[max(y,x)]
        o[y][5:]=s
        o[y+5][:5]=[s[y]]*5
    return o
