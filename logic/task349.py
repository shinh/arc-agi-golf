def p(g):
    h,w=len(g),len(g[0]);f=sum(g,[]);b=max(f,key=f.count)
    o=[r[:]for r in g]
    idx=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==9]
    for i,j in idx:
        for k in range(i+1,h):
            if o[k][j]==b:o[k][j]=1
    s,setq=set,set
    seen=s();comps=[]
    for i,j in idx:
        if (i,j)in seen:continue
        q=[(i,j)];c=s()
        while q:
            x,y=q.pop()
            if (x,y)in c:continue
            c.add((x,y));seen.add((x,y))
            for a in(-1,0,1):
                for d in(-1,0,1):
                    if a or d:
                        u,v=x+a,y+d
                        if 0<=u<h and 0<=v<w and g[u][v]==9 and(u,v)not in c:q.append((u,v))
        comps.append(c)
    for c in comps:
        i0=min(x for x,_ in c);i1=max(x for x,_ in c)
        j0=min(y for _,y in c);j1=max(y for _,y in c);n=(j1-j0+1)//2
        for i in range(max(0,i0-n),min(h,i1+n+1)):
            for j in range(max(0,j0-n),min(w,j1+n+1)):
                if (i,j)not in c and g[i][j]==b:o[i][j]=3
    return o
