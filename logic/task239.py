def p(g):
    d={}
    for r in g:
        for c in r:
            if c:d[c]=d.get(c,0)+1
    s=sorted(d,key=lambda k:(-d[k],k))
    m=d[s[0]]
    return [[(d[c]>i)*c for c in s]for i in range(m)]
