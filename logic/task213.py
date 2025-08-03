def p(g):
    h=len(g);w=len(g[0])
    for y in range(h):
        for x in range(w):
            c=g[y][x]
            if c not in (0,5):
                Y=[i for i in range(h)for j in range(w)if g[i][j]==c]
                X=[j for i in range(h)for j in range(w)if g[i][j]==c]
                v=max(Y)-min(Y)>max(X)-min(X)
                break
        else:continue
        break
    d=[]
    if v:
        for x in range(w):
            for y in range(h):
                c=g[y][x]
                if c not in (0,5)and c not in d:
                    d.append(c);break
        return [d]*len(d)
    for r in g:
        for c in r:
            if c not in (0,5)and c not in d:d.append(c)
    n=len(d)
    return [[c]*n for c in d]
