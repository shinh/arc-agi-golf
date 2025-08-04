def p(g):
    cs={c for r in g for c in r if c}
    a,b=sorted(cs)
    ps=lambda v:[(i,j) for i,r in enumerate(g) for j,x in enumerate(r) if x==v]
    n=lambda s:{(i-min(i for i,_ in s),j-min(j for _,j in s)) for i,j in s}
    s1,s2=n(ps(a)),n(ps(b))
    for y1 in range(4):
        for x1 in range(4):
            t1={(i+y1,j+x1) for i,j in s1 if i+y1<3 and j+x1<3}
            if len(t1)!=len(s1):
                continue
            for y2 in range(4):
                for x2 in range(4):
                    t2={(i+y2,j+x2) for i,j in s2 if i+y2<3 and j+x2<3}
                    if len(t2)!=len(s2) or t1&t2 or len(t1|t2)!=9:
                        continue
                    o=[[b]*3 for _ in range(3)]
                    for i,j in t1:o[i][j]=a
                    return o
