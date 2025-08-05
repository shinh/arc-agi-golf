def p(g):
    d=[(i//3-1,i%3-1)for i in range(9)if i-4]
    z=[];o={};c=[0]*10
    def f(y,x):
        t=g[y][x]%10;s=[(y,x)];r=[];e=not t
        while s:
            y,x=s.pop()
            v=g[y][x]
            if v>9 or v%10!=t:continue
            g[y][x]=v+10;r.append((y,x))
            for dy,dx in d:
                Y,X=y+dy,x+dx
                if 0<=Y<10 and 0<=X<10:
                    v=g[Y][X]
                    if v<10 and v%10==t:s.append((Y,X))
                    elif not t and v%10 and v%10-5:e=0
                elif not t:e=0
        return r,e
    for y in range(10):
        for x in range(10):
            if g[y][x]<10:
                r,e=f(y,x);t=g[y][x]%10
                if t and t!=5:
                    c[t]+=1;r.sort();Y,X=r[0];k=tuple((y-Y)*10+x-X for y,x in r)
                    o.setdefault(k,[]).append((r,t))
                elif not t and e:
                    r.sort();z.append(r)
    for r in z:
        Y,X=r[0];k=tuple((y-Y)*10+x-X for y,x in r)
        a=o.get(k)
        if a:
            i=next((i for i,(q,t) in enumerate(a) if c[t]==1),-1)
            if i+1:
                q,t=a.pop(i)
                for y,x in q:g[y][x]=0
                for y,x in r:g[y][x]=t
    return[[x%10 for x in r]for r in g]

