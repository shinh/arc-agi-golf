def p(g):
    a=[r[:4]for r in g];b=[r[5:9]for r in g];c=[r[10:]for r in g]
    s=lambda x:set(sum(x,[]))
    t=(s(a)&s(b)&s(c)).pop()
    u=[(s(a)-{t}).pop(),(s(b)-{t}).pop(),(s(c)-{t}).pop()]
    o=[[t]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if c[i][j]==u[2]:o[i][j]=u[2]
            if b[i][j]==u[1]:o[i][j]=u[1]
            if a[i][j]==u[0]:o[i][j]=u[0]
    return o
