def p(g):
    h=len(g);w=len(g[0])
    cs={c for r in g for c in r}
    c=min(cs,key=lambda k:sum(r.count(k)for r in g))
    o={(i,j)for i in range(h)for j in range(w)if g[i][j]==c}
    s=set(o);ch=1
    while ch:
        ch=0
        for i in range(h):
            xs=[j for j in range(w)if(i,j)in s]
            for a,b in zip(xs,xs[1:]):
                if b-a<5:
                    for k in range(a+1,b):
                        if(i,k)not in s:s.add((i,k));ch=1
        for j in range(w):
            ys=[i for i in range(h)if(i,j)in s]
            for a,b in zip(ys,ys[1:]):
                if b-a<5:
                    for k in range(a+1,b):
                        if(k,j)not in s:s.add((k,j));ch=1
    cts={(i,j)for i,j in s if((i,j-1)in s or(i,j+1)in s)and((i-1,j)in s or(i+1,j)in s)}
    rem=set(s);info=[]
    while rem:
        stack=[rem.pop()];comp=[]
        while stack:
            i,j=stack.pop();comp.append((i,j))
            for di in(-1,0,1):
                for dj in(-1,0,1):
                    if di or dj:
                        n=(i+di,j+dj)
                        if n in rem:rem.remove(n);stack.append(n)
        ys=[i for i,_ in comp];xs=[j for _,j in comp]
        h0=max(ys)-min(ys)+1;w0=max(xs)-min(xs)+1
        info.append((comp,min(ys),min(xs),h0,w0,max(h0,w0)))
    L=max(d for *_,d in info)
    for comp,y0,x0,h0,w0,d in info:
        if len(comp)==L and (h0==1 or w0==1):cts.add((y0+h0//2,x0+w0//2))
    m=L//2
    for i,j in cts:
        for d in range(-m,m+1):
            if 0<=i+d<h:s.add((i+d,j))
            if 0<=j+d<w:s.add((i,j+d))
    r=[r[:]for r in g]
    for i,j in s:r[i][j]=8
    for i,j in o:r[i][j]=c
    return r

# Failed attempt:
# def p(g):
#     H=len(g);W=len(g[0])
#     for l in range(2,6):
#         seen={}
#         for y in range(H):
#             for x in range(W):
#                 if (x,y)in seen:continue
#                 ok=1
#                 for i in range(-l,l+1):
#                     if x+i>=0 and x+i<W and g[y][x+i]==0:
#                         ok=0
#                     if y+i>=0 and y+i<H and g[y+i][x]==0:
#                         ok=0
#                 if ok:
#                     seen[(x,y)]=1
#                     for i in range(-l,l+1):
#                         if x+i>=0 and x+i<W:
#                             g[y][x+i]=8
#                         if y+i>=0 and y+i<H:
#                             g[y+i][x]=8
#     show(g,"out")
#     return g
