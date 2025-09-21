def p(g):
    # >=2 big neighbors ->3
    for n in range(289):
        if (r:=g[y:=n//17])[x:=n%17]==1<sum(r[x]>2 for r in g[y:y+2]+g[y-1:y])+(r[x-1:x]>[2])+(r[x+1:x+2]>[2]):
            r[x]=3;return p(g)
    return g
