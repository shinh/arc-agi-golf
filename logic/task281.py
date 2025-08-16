def p(g):
    # surround non-unique colors with a frame including the lone cell
    h=len(g);w=len(g[0]);f=sum(g,[])
    c=[0]*10
    for v in f:c[v]+=v>0
    for i,v in enumerate(f):
        if c[v]==1:u=v;uy,ux=divmod(i,w);break
    t=h;l=w;b=r=0
    for i,v in enumerate(f):
        if v*(v!=u):y,x=divmod(i,w);t=min(t,y);b=max(b,y);l=min(l,x);r=max(r,x)
    B=g[t][l];C=g[t+1][l+1]
    t=min(t,uy);l=min(l,ux);b=max(b,uy);r=max(r,ux)
    o=create(h,w)
    for y in range(t,b+1):
        for x in range(l,r+1):
            o[y][x]=[C,B][y in(t,b)or x in(l,r)]
    return o
