def p(g):
    o=[];s=1
    for r in g:
        if all(v==0 for v in r):s=1
        elif s:
            u=[];p0=0
            for v in r:
                if v:
                    if p0==0 or v!=p0:u.append(v)
                    p0=v
                else:p0=0
            o.append(u);s=0
    return o
