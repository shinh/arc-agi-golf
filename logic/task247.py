def p(g):
    d={};f={}
    for r in g:
        for x,v in enumerate(r):
            if v:d[v]=d.get(v,0)+1;f.setdefault(v,x)
    m=max(d.values())
    c=sorted([k for k,v in d.items()if v==m],key=f.get)
    return [c]*m
