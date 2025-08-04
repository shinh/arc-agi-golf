def p(g):
    h=len(g);w=len(g[0]);d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):d.setdefault(v,[]).append((y,x))
    s=[]
    for c,ps in d.items():
        f=0
        for y,x in ps:
            for ny in range(max(0,y-1),min(h,y+2)):
                for nx in range(max(0,x-1),min(w,x+2)):
                    if (ny,nx)!=(y,x) and g[ny][nx]==c:f=1;break
                if f:break
            if f:break
        if not f:s.append(c)
    a,b=s[0],s[-1]
    def mc(ps):
        l=[]
        for y,x in ps:
            for ny in range(max(0,y-1),min(h,y+2)):
                for nx in range(max(0,x-1),min(w,x+2)):
                    if (ny,nx)!=(y,x):l.append(g[ny][nx])
        return max(set(l),key=l.count)
    ca,cb=mc(d[a]),mc(d[b]);S=set()
    for y,x in d[a]+d[b]:
        for dy,dx in ((1,1),(1,-1),(-1,1),(-1,-1)):
            ny,nx=y,x
            while 0<=ny<h and 0<=nx<w:S.add((ny,nx));ny+=dy;nx+=dx
    o=[r[:] for r in g]
    for y,x in S:
        v=g[y][x]
        if v==ca:o[y][x]=a
        if v==cb:o[y][x]=b
    return o
