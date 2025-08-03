def p(g):
    r=[]
    for y in range(0,21,7):
        q=[]
        for x in range(0,21,7):
            m={}
            for j in range(7):
                for i in range(7):
                    v=g[y+j][x+i]
                    if v:m[v]=m.get(v,0)+1
            q.append(max(m,key=m.get) if m else 0)
        r.append(q)
    t=[]
    for c in zip(*r):
        if any(c) and (not t or c!=t[-1]):t.append(c)
    r=[list(c) for c in zip(*t)]
    t=[]
    for c in r:
        if any(c) and (not t or c!=t[-1]):t.append(c)
    return t
