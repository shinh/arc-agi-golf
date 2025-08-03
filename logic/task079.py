def p(g):
    d={}
    for y in range(len(g)-2):
        for x in range(len(g[0])-2):
            s=[r[x:x+3] for r in g[y:y+3]]
            for c in {v for r in s for v in r if v>1}:
                k=sum(v==c for r in s for v in r)
                if k>3:d.setdefault((c,tuple(map(tuple,s))),[0,(y,x)])[0]+=1
    m=b=k=0;t=None
    for (c,s),(n,pos) in d.items():
        kc=sum(v==c for r in s for v in r)
        if n>1 and (c>m or c==m and (kc>k or kc==k and n>b)):
            m,b,k,t=c,n,kc,s
    return [list(r) for r in t]
