def p(g):
    h,w=3,6
    v=[[r[:w//2]for r in g],[r[w//2:]for r in g]]
    a,b=v if all(len({c for r in p for c in r})==2 for p in v) else [g[:h//2],g[h//2:]]
    s=lambda p:set(sum(p,[]))
    bg=(s(a)&s(b)).pop()
    ca=(s(a)-{bg}).pop();cb=(s(b)-{bg}).pop()
    o=[[bg]*len(a[0])for _ in a]
    for t,p in ((ca,a),(cb,b)):
        for i,r in enumerate(p):
            for j,v in enumerate(r):
                if v==t:o[i][j]=6
    return o
