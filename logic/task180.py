def p(g):
    h=w=4
    A=[r[:w]for r in g[:h]];B=[r[w:]for r in g[:h]]
    C=[r[w:]for r in g[h:]];D=[r[:w]for r in g[h:]]
    c=set(sum(A,[]))
    for q in B,C,D:c&=set(sum(q,[]))
    c=next(iter(c))
    o=[[c]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            for q in (A,C,D,B):
                v=q[i][j]
                if v!=c:o[i][j]=v
    return o
