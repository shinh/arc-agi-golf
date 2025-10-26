p=lambda g:(f:=lambda a:[~0,*[i for i,r in enumerate(a)if max(r)<1],len(a)],C:=f([*zip(*g)]),[[max(max(r[x+1:y])for r in g[a+1:b])for x,y in zip(C,C[1:])]for a,b in zip(f(g),f(g)[1:])])[-1]
