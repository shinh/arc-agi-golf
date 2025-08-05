def p(g):
    w=h=20
    a=sum(g,[]);bg=max(set(a),key=a.count)
    seen=set();objs=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]==bg or (i,j) in seen:continue
            c=g[i][j];q=[(i,j)];seen.add((i,j));cells=[]
            while q:
                y,x=q.pop();cells+=[(y,x)]
                for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                    u,v=y+a,x+b
                    if 0<=u<h and 0<=v<w and g[u][v]==c and (u,v)not in seen:
                        seen.add((u,v));q+=[(u,v)]
            objs+=[cells]
    frames=[]
    for s in objs:
        ys=[y for y,x in s];xs=[x for y,x in s]
        t,b=min(ys),max(ys);l,r=min(xs),max(xs)
        if all(y in(t,b) or x in(l,r) for y,x in s) and len(s)==2*(b-t+r-l+2)-4:
            frames+=[(t,b,l,r)]
    t,b,l,r=max(frames,key=lambda z:(z[1]-z[0])*(z[3]-z[2]))
    t+=1;b-=1;l+=1;r-=1
    pat=[(y,x) for y in range(t,b+1) for x in range(l,r+1) if g[y][x]!=bg]
    col=g[pat[0][0]][pat[0][1]]
    mi=min(y for y,x in pat);mj=min(x for y,x in pat)
    shp={(y-mi,x-mj) for y,x in pat}
    for s in objs:
        mi=min(y for y,x in s);mj=min(x for y,x in s)
        if {(y-mi,x-mj) for y,x in s}==shp:
            for y,x in s:g[y][x]=col
    return g
