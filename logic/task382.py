def p(g):
    h=len(g);w=len(g[0]);o=[[2*(c==2)for c in r]for r in g]
    if any(r[0]==8 or r[-1]==8 for r in g):
        b=g[-1]
        for y,r in enumerate(g):
            if r[0]==8 or r[-1]==8:
                d=1 if r[0]==8 else-1
                x=0 if d>0 else w-1;kk=y
                while 0<=x<w:
                    if b[x]==2:
                        kk-=1
                        if kk<0:break
                    o[kk][x]=8;x+=d
        return o
    s=[i for i,v in enumerate(g[0]) if v==8]
    for y in range(h):
        if g[y][0]==2:s=[x+1 for x in s if x+1<w]
        if g[y][-1]==2:s=[x-1 for x in s if x]
        for x in s:o[y][x]=8
    return o

