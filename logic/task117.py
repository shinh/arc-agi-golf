def p(g):
    h=len(g);w=len(g[0]);cnt={}
    for r in g:
        for c in r:cnt[c]=cnt.get(c,0)+1
    bg=max(cnt,key=cnt.get)
    for v in cnt:
        if v!=bg and cnt[v]==5:
            pts=[(y,x)for y,row in enumerate(g) for x,c in enumerate(row) if c==v]
            ys=[y for y,_ in pts];xs=[x for _,x in pts]
            if max(ys)-min(ys)==max(xs)-min(xs)==2:
                i=min(ys);j=min(xs)
                if {(i,j),(i+2,j),(i,j+2),(i+2,j+2),(i+1,j+1)}<=set(pts):
                    s=i+i+2;t=j+j+2
                    r=[r[:]for r in g]
                    for y,row in enumerate(g):
                        for x,c in enumerate(row):
                            if c!=bg:
                                for Y,X in((y,x),(s-y,x),(y,t-x),(s-y,t-x)):
                                    if 0<=Y<h and 0<=X<w:r[Y][X]=c
                    return r
