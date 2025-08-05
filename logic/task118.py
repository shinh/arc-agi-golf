def p(g):
    h=len(g);w=len(g[0])
    cs={c for r in g for c in r};c=min(cs,key=lambda v:sum(r.count(v)for r in g))
    o={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==c}
    s=set(o);ch=1
    while ch:
        ch=0
        for y in range(h):
            xs=sorted(x for x in range(w)if(y,x)in s)
            for a,b in zip(xs,xs[1:]):
                if b-a<5:
                    for x in range(a+1,b):
                        if(y,x)not in s:s.add((y,x));ch=1
        for x in range(w):
            ys=sorted(y for y in range(h)if(y,x)in s)
            for a,b in zip(ys,ys[1:]):
                if b-a<5:
                    for y in range(a+1,b):
                        if(y,x)not in s:s.add((y,x));ch=1
    cts={(y,x)for y,x in s if({(y,x-1),(y,x+1)}&s and {(y-1,x),(y+1,x)}&s)}
    rem=s.copy();info=[]
    while rem:
        st=[rem.pop()];comp=[]
        while st:
            y,x=st.pop();comp.append((y,x))
            for dy in(-1,0,1):
                for dx in(-1,0,1):
                    if dy or dx:
                        n=(y+dy,x+dx)
                        if n in rem:rem.remove(n);st.append(n)
        ys=[y for y,_ in comp];xs=[x for _,x in comp]
        h0=max(ys)-min(ys)+1;w0=max(xs)-min(xs)+1
        info.append((comp,min(ys),min(xs),h0,w0,max(h0,w0)))
    L=max(d for *_,d in info);m=L//2
    for comp,y0,x0,h0,w0,d in info:
        if len(comp)==L and (h0==1 or w0==1):cts.add((y0+h0//2,x0+w0//2))
    for y,x in cts:
        for d in range(-m,m+1):
            if 0<=y+d<h:s.add((y+d,x))
            if 0<=x+d<w:s.add((y,x+d))
    r=[r[:]for r in g]
    for y,x in s:r[y][x]=8
    for y,x in o:r[y][x]=c
    return r
