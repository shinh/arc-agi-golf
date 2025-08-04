def p(g):
    h=len(g);w=len(g[0]);d={}
    for r in g:
        for v in r:d[v]=d.get(v,0)+1
    b=max(d,key=d.get);d.pop(b);m=max(d,key=d.get)
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v not in (b,m):
                s=(y>0 and g[y-1][x]==m)+(y<h-1 and g[y+1][x]==m)+(x>0 and r[x-1]==m)+(x<w-1 and r[x+1]==m)
                r[x]=m if s>1 else b
    return g
